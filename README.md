



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FEXADTM%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T014417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF40vPjw2DBGF2xVRZfIG8JQkT0MH%2FkJsGWfQHWmxUucAiAVecU1QXr1t5PeSdJ3cb6IUrBxmBrR75rFHI0ELu7jgyqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhI2aQ3QYeoVSjGYUKtwDuti%2BfRq2fPiSux7kWb4yl9rotUMgTxsB1OYSq0qFs4ci28DPYPiEufFSb1nRftGxbem78AI9ouFfOWvlld3MpiMZ5%2FYGfkEn5pVGybP5%2Fo%2B01wHdd%2FY5VjJthdP%2FPxCt3P7b0%2F1UxoyQgc19%2FS%2F2qL4v2XP4inDjlKEJ0EHj6VLjSqmWvafmcmggWMyz4UYA1CCb10y53hK8e1AfeMxe%2BtR8q2f5giJDbiGmlDsOBZNmA4HagnrGe7R9OMjO2NvHFnvzI9nnrQbwyzB5dsNsXchB%2BxQZps1YxHOPLkwPEp5%2FDa6Ldcc2ds0xtLZQu4xM5uAjE2%2Fx12YcaqWrLjtB1aCDqmo%2B1VgVBbJdi%2BlJoG2QsCWI0TZaqngXejuWyZWpPG6HPSY8p0ccn6eLWWw4iLNoSYd38RkK1JIk381uDpk9AzvxaQeQvcV4%2FyZAkVMv%2FmxAzLxRYHugoDHB8CHinfbuaYMc7K3xVVktEvdhlcllYsJLVdpLBBdvMtDBxusQJxkWy%2FgsRD%2BRZHxv7J5o%2B517FHR8eu%2BXNAQAB98rgYqRJgpZ1Hakd18R1wf91GodZxYzhqqQOyrnWmsF9ro7J%2BH9x4o9ahAfgqunP8ZtJ0ychQ1Y1T7%2B%2BjE6FnEwjLjNzQY6pgH8D%2BhxmcTqzURslfQcMMe1lEl0mMLzqP4d0BIibteHeb86nX9IRCJxRr5ediTwViN5gAPpKt7LCZ%2F%2F%2FXLzR5iDzgJ2%2FvXZZyycBNhPyt13SNYQ1VAith5opBuLjeoI%2FjdP7LgRNGw%2FQoiWHa7NWwTcWdbFGpcmwNnEi2tF0ZT089MkUKQTrDMCmbRcouIFIesLcsC5X2vqFYCK0cG9HehcSwTQeD9z&X-Amz-Signature=ee372dc79d9c7740a79fc0ffe388ce8dd5930a54fd27cd80632721ce699d4d73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FEXADTM%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T014417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF40vPjw2DBGF2xVRZfIG8JQkT0MH%2FkJsGWfQHWmxUucAiAVecU1QXr1t5PeSdJ3cb6IUrBxmBrR75rFHI0ELu7jgyqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhI2aQ3QYeoVSjGYUKtwDuti%2BfRq2fPiSux7kWb4yl9rotUMgTxsB1OYSq0qFs4ci28DPYPiEufFSb1nRftGxbem78AI9ouFfOWvlld3MpiMZ5%2FYGfkEn5pVGybP5%2Fo%2B01wHdd%2FY5VjJthdP%2FPxCt3P7b0%2F1UxoyQgc19%2FS%2F2qL4v2XP4inDjlKEJ0EHj6VLjSqmWvafmcmggWMyz4UYA1CCb10y53hK8e1AfeMxe%2BtR8q2f5giJDbiGmlDsOBZNmA4HagnrGe7R9OMjO2NvHFnvzI9nnrQbwyzB5dsNsXchB%2BxQZps1YxHOPLkwPEp5%2FDa6Ldcc2ds0xtLZQu4xM5uAjE2%2Fx12YcaqWrLjtB1aCDqmo%2B1VgVBbJdi%2BlJoG2QsCWI0TZaqngXejuWyZWpPG6HPSY8p0ccn6eLWWw4iLNoSYd38RkK1JIk381uDpk9AzvxaQeQvcV4%2FyZAkVMv%2FmxAzLxRYHugoDHB8CHinfbuaYMc7K3xVVktEvdhlcllYsJLVdpLBBdvMtDBxusQJxkWy%2FgsRD%2BRZHxv7J5o%2B517FHR8eu%2BXNAQAB98rgYqRJgpZ1Hakd18R1wf91GodZxYzhqqQOyrnWmsF9ro7J%2BH9x4o9ahAfgqunP8ZtJ0ychQ1Y1T7%2B%2BjE6FnEwjLjNzQY6pgH8D%2BhxmcTqzURslfQcMMe1lEl0mMLzqP4d0BIibteHeb86nX9IRCJxRr5ediTwViN5gAPpKt7LCZ%2F%2F%2FXLzR5iDzgJ2%2FvXZZyycBNhPyt13SNYQ1VAith5opBuLjeoI%2FjdP7LgRNGw%2FQoiWHa7NWwTcWdbFGpcmwNnEi2tF0ZT089MkUKQTrDMCmbRcouIFIesLcsC5X2vqFYCK0cG9HehcSwTQeD9z&X-Amz-Signature=fe820fc9e454d0d40287a87e77a66440d5295200eafa66857afdbe6b8c002d8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







