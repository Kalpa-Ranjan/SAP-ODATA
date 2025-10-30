# sync_notion.py
import os
from notion_client import Client
from github import Github
import traceback

# ========== CONFIGURATION ==========
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")  # Example: "username/notion-sync"
FILE_PATH = os.getenv("FILE_PATH", "README.md")

# ========== INITIALIZE CLIENTS ==========
notion = Client(auth=NOTION_TOKEN)
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# ========== NOTION HELPERS ==========

def extract_block_text(block, indent=0, num_counter=None):
    """Recursively extract Markdown text from Notion blocks (with children)."""
    prefix = " " * indent
    block_type = block["type"]
    text = ""

    def join_text(rt):
        return "".join(r["plain_text"] for r in rt)

    # Initialize local numbering
    if num_counter is None:
        num_counter = {"count": 1}

    if block_type == "paragraph":
        text += prefix + join_text(block["paragraph"]["rich_text"]) + "\n\n"
    elif block_type == "heading_1":
        text += "# " + join_text(block["heading_1"]["rich_text"]) + "\n\n"
    elif block_type == "heading_2":
        text += "## " + join_text(block["heading_2"]["rich_text"]) + "\n\n"
    elif block_type == "heading_3":
        text += "### " + join_text(block["heading_3"]["rich_text"]) + "\n\n"
    elif block_type == "bulleted_list_item":
        text += prefix + "- " + join_text(block["bulleted_list_item"]["rich_text"]) + "\n"
    elif block_type == "numbered_list_item":
        text += prefix + f"{num_counter['count']}. " + join_text(block["numbered_list_item"]["rich_text"]) + "\n"
        num_counter["count"] += 1
    elif block_type == "to_do":
        checked = "x" if block["to_do"].get("checked") else " "
        text += prefix + f"- [{checked}] " + join_text(block["to_do"]["rich_text"]) + "\n"
    elif block_type == "quote":
        text += prefix + "> " + join_text(block["quote"]["rich_text"]) + "\n\n"
    elif block_type == "callout":
        emoji = ""
        icon = block["callout"].get("icon")
        if isinstance(icon, dict) and "emoji" in icon:
            emoji = icon["emoji"] + " "
        text += prefix + f"> {emoji}" + join_text(block["callout"]["rich_text"]) + "\n\n"
    elif block_type == "code":
        language = block["code"].get("language", "plaintext")
        code_text = join_text(block["code"]["rich_text"])
        text += f"```{language}\n{code_text}\n```\n\n"
    elif block_type == "divider":
        text += "\n---\n\n"
    elif block_type == "image":
        image_url = (
            block["image"]["external"]["url"]
            if "external" in block["image"]
            else block["image"]["file"]["url"]
        )
        text += f"![Image]({image_url})\n\n"
    elif block_type == "toggle":
        text += prefix + "▶️ " + join_text(block["toggle"]["rich_text"]) + "\n"
    else:
        text += ""

    # Handle children recursively
    if block.get("children"):
        child_counter = {"count": 1} if block_type == "numbered_list_item" else num_counter
        for child in block["children"]:
            text += extract_block_text(child, indent + 2, child_counter)

    return text


def get_all_blocks(notion, block_id):
    """Recursively fetch all Notion blocks and their children."""
    all_blocks = []
    next_cursor = None

    while True:
        response = notion.blocks.children.list(block_id=block_id, start_cursor=next_cursor)
        results = response.get("results", [])
        all_blocks.extend(results)

        for block in results:
            if block.get("has_children"):
                block["children"] = get_all_blocks(notion, block["id"])

        if not response.get("has_more"):
            break
        next_cursor = response.get("next_cursor")

    return all_blocks


def get_page_content(page_id):
    """Fetch all Notion blocks as markdown text."""
    print("📥 Fetching Notion content...")
    blocks = get_all_blocks(notion, page_id)
    print(f"✅ Retrieved {len(blocks)} top-level blocks.")
    return "".join(extract_block_text(b) for b in blocks)


# ========== GITHUB HELPERS ==========

def update_readme(content):
    """Create or update README.md (or any specified file) in the repo."""
    try:
        file = repo.get_contents(FILE_PATH, ref="main")
        repo.update_file(
            path=FILE_PATH,
            message="🔄 Auto-synced from Notion",
            content=content,
            sha=file.sha,
            branch="main",
        )
        print("✅ File updated successfully.")
    except Exception:
        print("ℹ️ File not found, creating new one...")
        repo.create_file(
            path=FILE_PATH,
            message="🆕 Initial Notion sync",
            content=content,
            branch="main",
        )
        print("✅ File created successfully.")


# ========== MAIN ==========

def main():
    print("🚀 Starting Notion → GitHub sync...")
    try:
        notion_content = get_page_content(PAGE_ID)
        print("\n📝 Preview (first 400 chars):\n", notion_content[:400])
        update_readme(notion_content)
        print("🎉 Sync complete!")
    except Exception as e:
        print("❌ Error during sync:", e)
        traceback.print_exc()


if __name__ == "__main__":
    main()
