



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2AEZYVO%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T123929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7XU7E1A7V7X6VaS82wyEO0HCFsYOd92ZRwV4F3NK0dAIgKC8%2B7HMKftLqp8HyYKM3cfEGXVq304Ihfkc%2ByxdcWn0qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPA1OwmAWpTyGTotSrcA%2FEny80dHHd7yXkA5CmjO7fXLW8uSPAbKrTPR2dd6r5FhXYFz4sG6cVCe96TdCo0yB7uZmbYzW5Sj9qk2O2P69tjWU9p05f7JyEH4zohl57g1Em7BpfjrT55BtuH5eipDSvB6zwdsxTa4J5iw3F2c%2FHPqtOyWg5QeYFiPZUKNuCPKmtctBn9enIi6uOuYmp%2BCFfZhdRlkApMdlW0Iarauk6YhnPOBSlftbyhFEvdbh9n7DVw9%2F5f1EeNW2Q9zRyUFISGBAyrSCDKZzx5NOhSI9gLUj6fw%2B8VO4eLLZy0Bkq6yy%2Bxp7IQJI3MxPLky%2By%2BNHxw8d2iWzM3sWGe03VLSFcLXwbSs%2FQzXPwzcb6%2F3TnVBUYak71gT%2FfYIKjmHkQ4VB0I%2BV3pe03CFjQoQzhunU8y5xJl3Jh%2FZTE4hVi%2FRZUeboTKOlIxqb%2FeCfqDmnUHRYBeLIswSXF2liFtVxImzYn96tbcqPbS1jxuOqXhq5ad1N5hrXWDtL9z67cLAQ8i82JcQ7gwc0coStKLWJ0zFK1uaifPtXh%2BpExWvYuGMkvdH5OZSzfV0g86BlLS0SADcKqr%2BnKxBxfs9aItdVspBoyaWgWI6nkp%2F0H4%2FaT8d9GWJs9MaPW%2B4ZdL5Q%2BcMITUvcsGOqUBLXBO4kpshVsjP6pfnFaqrVBENkNkFstENXBeNlvfw8tRMLL7Mn9WCGJY91pdC5WPYdZIck3r9LLHka5HrzkfTjfBMcxvhLpX9%2FpLvbpPMKUjFFcgNq7BQf70rY8KpF45vSIF42VM0hxj7yn4Ea2jpA7Wm3HoaTz3X6Y8m0wQYBxY8PSBaeAvfIdvsPx9K%2BBMwGuN4pDNe8Vh39AMp8lkHUaF7RxN&X-Amz-Signature=1772e03b3b4c4a9c5d9d3f3988b469a744f264dc95cb95894ca7ca73ffc9feb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2AEZYVO%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T123929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7XU7E1A7V7X6VaS82wyEO0HCFsYOd92ZRwV4F3NK0dAIgKC8%2B7HMKftLqp8HyYKM3cfEGXVq304Ihfkc%2ByxdcWn0qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPA1OwmAWpTyGTotSrcA%2FEny80dHHd7yXkA5CmjO7fXLW8uSPAbKrTPR2dd6r5FhXYFz4sG6cVCe96TdCo0yB7uZmbYzW5Sj9qk2O2P69tjWU9p05f7JyEH4zohl57g1Em7BpfjrT55BtuH5eipDSvB6zwdsxTa4J5iw3F2c%2FHPqtOyWg5QeYFiPZUKNuCPKmtctBn9enIi6uOuYmp%2BCFfZhdRlkApMdlW0Iarauk6YhnPOBSlftbyhFEvdbh9n7DVw9%2F5f1EeNW2Q9zRyUFISGBAyrSCDKZzx5NOhSI9gLUj6fw%2B8VO4eLLZy0Bkq6yy%2Bxp7IQJI3MxPLky%2By%2BNHxw8d2iWzM3sWGe03VLSFcLXwbSs%2FQzXPwzcb6%2F3TnVBUYak71gT%2FfYIKjmHkQ4VB0I%2BV3pe03CFjQoQzhunU8y5xJl3Jh%2FZTE4hVi%2FRZUeboTKOlIxqb%2FeCfqDmnUHRYBeLIswSXF2liFtVxImzYn96tbcqPbS1jxuOqXhq5ad1N5hrXWDtL9z67cLAQ8i82JcQ7gwc0coStKLWJ0zFK1uaifPtXh%2BpExWvYuGMkvdH5OZSzfV0g86BlLS0SADcKqr%2BnKxBxfs9aItdVspBoyaWgWI6nkp%2F0H4%2FaT8d9GWJs9MaPW%2B4ZdL5Q%2BcMITUvcsGOqUBLXBO4kpshVsjP6pfnFaqrVBENkNkFstENXBeNlvfw8tRMLL7Mn9WCGJY91pdC5WPYdZIck3r9LLHka5HrzkfTjfBMcxvhLpX9%2FpLvbpPMKUjFFcgNq7BQf70rY8KpF45vSIF42VM0hxj7yn4Ea2jpA7Wm3HoaTz3X6Y8m0wQYBxY8PSBaeAvfIdvsPx9K%2BBMwGuN4pDNe8Vh39AMp8lkHUaF7RxN&X-Amz-Signature=47186aa54771a423707f2d0d0d680afcd93d1d8aa58a153f86fd303db7148aab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







