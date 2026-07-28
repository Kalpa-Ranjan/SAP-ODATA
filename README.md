



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRCOUNEN%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T020244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUk7%2B1dOWKIhLT5rUPcjbwF8%2B%2Bhc9xQIxmh9lqBXloMQIhAJXFv5rICrAuEnLDpC3Sk6e7zoy8bVES0m3za0eUVHMMKv8DCFgQABoMNjM3NDIzMTgzODA1IgzCa0mYCBIcftSoVMcq3AMLyEyi9qthYFyVpQM%2BytWRf40x9OwMdLN7v8SxTipwikcLhUDpnVzkfZb6sjLfufN4%2BTxlV0ohXiq3Whdt9u%2FylThjXtGuA9w%2FYSBLs6%2BNBEXYfx5RQovzxseLxGkgJKLtS8DDLlDokdyTc6LZG4X7Fmrpuq5n%2BVr3Apxgn%2BKgK6mEH5IEYqEzpTeqPW%2BIuOqBjHzRRZgGY%2BuL04fjrwzNzPIrMCK8lpZ09CzDxIHIxPezc2eTukUo1Nm02fE4AAE8YWHGc%2BA6eCwZG16KulWouEUPOzunO6M3ihmvMDFEqHshfEKwHY5Md%2BvXklL3GwaC8iPPaSXg%2Bgio%2BEpCILZcNyG9AQ8jkKQhMrO1eIg6f9h%2BVJwSKWxUKDaubZQLJqC0PkeyntHCiFMvINFirO%2BIZqP6bd24Njr23lqonayvjrZ4MhmooZffcbhD2XI0Jm3YLvcNIchnz5GXFYoD8yRczFR6k26nRYq3KfSQAzQb6A%2FjIxhkp0pbKjImxxGe0E1ZR9D6GQkMpG%2FuqJqzX9DnA8NrDrbpTcI%2F3Wl5gF8wZ4z%2FkFsPe7RHhD8wBSw%2BoKN9LvcDVsFW65tEpu5DqXJNaTzk12x1N8uoMvr3TI3U97aH5OWfioPg7CgzZDDxxJ%2FTBjqkAWt66DlNXG%2BlbeM9XhGTD7%2BD1CQ%2B5Ha0Yf4gB9T9HU1OuMC4xnfh2YuPtx4gZzk8VHWxECyDySxs5Xe6R2tFuotXdEUiCBcOXu5y7Y45%2BF7z1jwhI4UoE5KUyDztowQudSeywKczZmTpYQFZ0TK5Jsgt53n3vIg%2FSd7S6NKuwLXf2yOKsI5x048FpLGULf7YzLmAYyUPak5TD0MhjFgakt983COu&X-Amz-Signature=1c05d9c2b1231ee87eac5102a2e14258d5d3c3e09cdfd1dfd5870aad83a8545f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRCOUNEN%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T020244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUk7%2B1dOWKIhLT5rUPcjbwF8%2B%2Bhc9xQIxmh9lqBXloMQIhAJXFv5rICrAuEnLDpC3Sk6e7zoy8bVES0m3za0eUVHMMKv8DCFgQABoMNjM3NDIzMTgzODA1IgzCa0mYCBIcftSoVMcq3AMLyEyi9qthYFyVpQM%2BytWRf40x9OwMdLN7v8SxTipwikcLhUDpnVzkfZb6sjLfufN4%2BTxlV0ohXiq3Whdt9u%2FylThjXtGuA9w%2FYSBLs6%2BNBEXYfx5RQovzxseLxGkgJKLtS8DDLlDokdyTc6LZG4X7Fmrpuq5n%2BVr3Apxgn%2BKgK6mEH5IEYqEzpTeqPW%2BIuOqBjHzRRZgGY%2BuL04fjrwzNzPIrMCK8lpZ09CzDxIHIxPezc2eTukUo1Nm02fE4AAE8YWHGc%2BA6eCwZG16KulWouEUPOzunO6M3ihmvMDFEqHshfEKwHY5Md%2BvXklL3GwaC8iPPaSXg%2Bgio%2BEpCILZcNyG9AQ8jkKQhMrO1eIg6f9h%2BVJwSKWxUKDaubZQLJqC0PkeyntHCiFMvINFirO%2BIZqP6bd24Njr23lqonayvjrZ4MhmooZffcbhD2XI0Jm3YLvcNIchnz5GXFYoD8yRczFR6k26nRYq3KfSQAzQb6A%2FjIxhkp0pbKjImxxGe0E1ZR9D6GQkMpG%2FuqJqzX9DnA8NrDrbpTcI%2F3Wl5gF8wZ4z%2FkFsPe7RHhD8wBSw%2BoKN9LvcDVsFW65tEpu5DqXJNaTzk12x1N8uoMvr3TI3U97aH5OWfioPg7CgzZDDxxJ%2FTBjqkAWt66DlNXG%2BlbeM9XhGTD7%2BD1CQ%2B5Ha0Yf4gB9T9HU1OuMC4xnfh2YuPtx4gZzk8VHWxECyDySxs5Xe6R2tFuotXdEUiCBcOXu5y7Y45%2BF7z1jwhI4UoE5KUyDztowQudSeywKczZmTpYQFZ0TK5Jsgt53n3vIg%2FSd7S6NKuwLXf2yOKsI5x048FpLGULf7YzLmAYyUPak5TD0MhjFgakt983COu&X-Amz-Signature=175d1dba86184c1698ddf10e6fa4595588ae7140c916bb1525dd7ebb1c5c5dcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







