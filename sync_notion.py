# sync_notion.py
import os
from notion_client import Client
from github import Github
import base64

# Read tokens and configuration from environment variables
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
FILE_PATH = os.getenv("FILE_PATH", "README.md")

# Initialize clients
notion = Client(auth=NOTION_TOKEN)
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def extract_block_text(block):
    """Recursively extract text or code from Notion blocks"""
    block_type = block["type"]
    if block_type == "paragraph":
        return "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n\n"
    elif block_type == "heading_1":
        return "# " + "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n\n"
    elif block_type == "heading_2":
        return "## " + "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n\n"
    elif block_type == "heading_3":
        return "### " + "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n\n"
    elif block_type == "bulleted_list_item":
        return "- " + "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n"
    elif block_type == "numbered_list_item":
        return "1. " + "".join([r["plain_text"] for r in block[block_type]["rich_text"]]) + "\n"
    elif block_type == "code":
        language = block["code"].get("language", "plaintext")
        code_text = "".join([r["plain_text"] for r in block["code"]["rich_text"]])
        return f"```{language}\n{code_text}\n```\n\n"
    elif block_type == "divider":
        return "\n---\n\n"
    else:
        return ""
        
def get_all_blocks(notion, block_id):
    """Recursively fetch all Notion blocks, including nested children."""
    all_blocks = []
    next_cursor = None

    while True:
        response = notion.blocks.children.list(block_id=block_id, start_cursor=next_cursor)
        results = response.get("results", [])
        all_blocks.extend(results)

        # Recursive call for nested children
        for block in results:
            if block.get("has_children"):
                block["children"] = get_all_blocks(notion, block["id"])

        if not response.get("has_more"):
            break
        next_cursor = response.get("next_cursor")

    return all_blocks

def get_page_content(page_id):
    """Fetch all Notion blocks as markdown text"""
    blocks = get_all_blocks(notion, page_id)
    return "".join(extract_block_text(b) for b in blocks)


def update_readme(content):
    """Create or update README.md (or any specified file) in the repo"""
    try:
        file = repo.get_contents(FILE_PATH, ref="main")
        repo.update_file(
            path=FILE_PATH,
            message="🔄 Auto-synced from Notion",
            content=content,
            sha=file.sha,
            branch="main"
        )
        print("✅ File updated successfully.")
    except Exception:
        repo.create_file(
            path=FILE_PATH,
            message="🆕 Initial Notion sync",
            content=content,
            branch="main"
        )
        print("✅ File created successfully.")

def main():
    notion_content = get_page_content(PAGE_ID)
    update_readme(notion_content)

if __name__ == "__main__":
    main()
