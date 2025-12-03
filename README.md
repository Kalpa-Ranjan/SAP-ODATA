



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWFZAJDJ%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T123405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFpFfEFK3Bj%2FB3iSt2%2FNT3s%2BM2N0kCESzzG7dDDZWwQEAiEAvBqjpk17t5a6tPDJK6tl%2FuZGBxd3gHgrwox5jLntaa8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDIVaz87%2FM%2B%2BhJjb3OSrcAzMFSvyM56bUKtCgQrMZErlLRbMRLRxPiLMmFHVQ9BEmOwI6Pv5bg%2FEsmAfLxlzV0JdeCIesCkVYEW1nus2zRnzQnTRUolnW6H8GLGDP7GvQArjujLRkSd%2FO9bgyNxl84voRkBtgTOblQu7k2z5%2F7LThBvVNVwJgyQUSLq89820I0uxfJz%2FShw2TKgTk2DDpgiBv%2BcNtkdxoOsJyUpdqj%2FebTk7JgUSLA5MJGFwvfAfVTse6zo8FhjPK5%2FZMS%2FLcwGGWu3YYG5%2FSYSETSMfrfcdAIU6%2FeN9Y9PrqN0SNMHutWrooBU79vEVavHSbvb57wFEaSxNu11%2B8f0%2FhGeL58C5DSGfnrHvrrYerwM3GdLTqu2Splba155gjK2fsBAs4nMOj2p5ySGrkera%2B3ct8pAa%2FfhtoJKiyfcFmcI%2BfCb6RAksNxYtfKa7yH98iWVbaSCpyqH19zITUlqn0WwnVokp%2BE310G89AY0%2BGzfXbXcqeKCfuYP74Yj8ugtGC3gUyBjYCiWMSTN5hEZxtxNMw5dz0LZke28qwlto6kAbf5B8B5bIDJecbKWhE%2BSp%2FYLweEvOdxT6WcWVJoI%2BiwVMgOvzuGheXYJ1j1M6S%2BWtrFQkWgyn%2BkvBOX0l%2BE9TMMKvNwMkGOqUBTiYnZYV4zLsTOsqgRoIMldWDGTqqWT1JmQ5zhlwBvKpl1EKBlGqH8D%2FuGmkRdN59r9Id7BejJHM1me0Z8Eso122juSD8BQHSGm4KMjX%2BnMtoQSnPj7NWhAw9VDXWcKWjtsIGgQTbnA8fQ%2FoLGllZTcOMFbXOnC9Jg2eQlEJbTCGKAGrsjbU90gEWdb40xb7GcRGh7d0hiC2Q9Vbc52c1nUO4sRWE&X-Amz-Signature=a3e6db0254d4d3fa8df590930406d371686b34f5f4b55ae87bf557c8fe004fe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWFZAJDJ%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T123406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFpFfEFK3Bj%2FB3iSt2%2FNT3s%2BM2N0kCESzzG7dDDZWwQEAiEAvBqjpk17t5a6tPDJK6tl%2FuZGBxd3gHgrwox5jLntaa8q%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDIVaz87%2FM%2B%2BhJjb3OSrcAzMFSvyM56bUKtCgQrMZErlLRbMRLRxPiLMmFHVQ9BEmOwI6Pv5bg%2FEsmAfLxlzV0JdeCIesCkVYEW1nus2zRnzQnTRUolnW6H8GLGDP7GvQArjujLRkSd%2FO9bgyNxl84voRkBtgTOblQu7k2z5%2F7LThBvVNVwJgyQUSLq89820I0uxfJz%2FShw2TKgTk2DDpgiBv%2BcNtkdxoOsJyUpdqj%2FebTk7JgUSLA5MJGFwvfAfVTse6zo8FhjPK5%2FZMS%2FLcwGGWu3YYG5%2FSYSETSMfrfcdAIU6%2FeN9Y9PrqN0SNMHutWrooBU79vEVavHSbvb57wFEaSxNu11%2B8f0%2FhGeL58C5DSGfnrHvrrYerwM3GdLTqu2Splba155gjK2fsBAs4nMOj2p5ySGrkera%2B3ct8pAa%2FfhtoJKiyfcFmcI%2BfCb6RAksNxYtfKa7yH98iWVbaSCpyqH19zITUlqn0WwnVokp%2BE310G89AY0%2BGzfXbXcqeKCfuYP74Yj8ugtGC3gUyBjYCiWMSTN5hEZxtxNMw5dz0LZke28qwlto6kAbf5B8B5bIDJecbKWhE%2BSp%2FYLweEvOdxT6WcWVJoI%2BiwVMgOvzuGheXYJ1j1M6S%2BWtrFQkWgyn%2BkvBOX0l%2BE9TMMKvNwMkGOqUBTiYnZYV4zLsTOsqgRoIMldWDGTqqWT1JmQ5zhlwBvKpl1EKBlGqH8D%2FuGmkRdN59r9Id7BejJHM1me0Z8Eso122juSD8BQHSGm4KMjX%2BnMtoQSnPj7NWhAw9VDXWcKWjtsIGgQTbnA8fQ%2FoLGllZTcOMFbXOnC9Jg2eQlEJbTCGKAGrsjbU90gEWdb40xb7GcRGh7d0hiC2Q9Vbc52c1nUO4sRWE&X-Amz-Signature=01460a99112e369b8e4fef03a2e14a1d4f47be23a7537b1c20597761bf77c600&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







