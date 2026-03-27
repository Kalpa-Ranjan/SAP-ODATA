



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCDEDN6R%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T070040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDy4nWPBn4zeACaJPs2CwjY9yUS8PuanhkSY3Z6lZp%2FZgIgOeGZyLCUcQNdqJcqfVD99hT6tzm6nPaZY5gwv%2BHkczwqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJJ8zoaCa8u7Cq6GSrcAwYA09RvPrRE2tRaO4j5dbYgqEPSxzkR8cx1CWiqIfn02vUU00hs6O0%2F%2B%2BYyNlnWXWJCckYcWABp%2BJcvpe%2BU%2B9cJWJaZGfCXl4%2BPDt4dfk6ngfSvkBqu1ump33sjV94ZYHo6JNnN0Gke8hc89ZxKQ3Y52gtf8uK%2BjLszcDnLUKOIDXVzRrB%2FCDhpWUw%2FFjutX12GUvitu49Ti%2FwApaIjhz8Tx5dTXiErewtOztjxZlvly4wvi89CZ1I8Mgz24yNAZ8VA8M50xz85oLYoAyUnr0mZpagpkuwRByB12eUte7Rv06AFpdUlx5Pt9V8MgvcP%2Bd2HEd5c29LnFHgitiZ3NnztZiA16nTdjSa0wqTQIH0wyYs5zJy6ARuM3GN9Dqa126rGPTUSfQgCj0V8vSGp85t8EW2hItWKLlmer2iM9eab4mYzqUKLZbH5lJ6VCf%2Bv4YuLzlaYxn7BxdTlv%2Fnz4nwZnxyQH6aZcY%2Fuj%2BwQ4Fjy89bSrobtRK3exdDYmwnE%2Bnbdmt6H6ebKZJ9pO%2BAOY8g%2FEjFj1t2sBWlr0pI3AY8V7iYw3iXFVCno4wpLhf0Yi0wSvWVoyIYNwHbNX%2FHUWb8kOawxxlgZSejI7iv4niJ%2FGnmaZwVAdoXbQ7AlMMGLmM4GOqUBU2KNkIVkVlfo3Dsbj91pMe%2BaGKhQD%2B748iO%2BEv5ySyg3TlqzrKiMxkZ51jl3kjY1BN268j8utzSqD%2F%2FetrQOFzgZqDWC2%2F8YZ841a1BT%2BY%2BOLGy%2FTfjdNsNtjgY12v%2BpoJHYbjKA3HWOmbM%2Bgolfj4tdvS%2FM266tcnmm5%2B3gBSosWQsQ5fyfAPduDNYhYPTrjqISGmDgVKIY2fCBuMGbDnlx%2FKgJ&X-Amz-Signature=dd2d07cdb7a4d86afbf1b930a8d0259c86c4e3565e5c226380d36bbcb8bf64f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCDEDN6R%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T070041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDy4nWPBn4zeACaJPs2CwjY9yUS8PuanhkSY3Z6lZp%2FZgIgOeGZyLCUcQNdqJcqfVD99hT6tzm6nPaZY5gwv%2BHkczwqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJJ8zoaCa8u7Cq6GSrcAwYA09RvPrRE2tRaO4j5dbYgqEPSxzkR8cx1CWiqIfn02vUU00hs6O0%2F%2B%2BYyNlnWXWJCckYcWABp%2BJcvpe%2BU%2B9cJWJaZGfCXl4%2BPDt4dfk6ngfSvkBqu1ump33sjV94ZYHo6JNnN0Gke8hc89ZxKQ3Y52gtf8uK%2BjLszcDnLUKOIDXVzRrB%2FCDhpWUw%2FFjutX12GUvitu49Ti%2FwApaIjhz8Tx5dTXiErewtOztjxZlvly4wvi89CZ1I8Mgz24yNAZ8VA8M50xz85oLYoAyUnr0mZpagpkuwRByB12eUte7Rv06AFpdUlx5Pt9V8MgvcP%2Bd2HEd5c29LnFHgitiZ3NnztZiA16nTdjSa0wqTQIH0wyYs5zJy6ARuM3GN9Dqa126rGPTUSfQgCj0V8vSGp85t8EW2hItWKLlmer2iM9eab4mYzqUKLZbH5lJ6VCf%2Bv4YuLzlaYxn7BxdTlv%2Fnz4nwZnxyQH6aZcY%2Fuj%2BwQ4Fjy89bSrobtRK3exdDYmwnE%2Bnbdmt6H6ebKZJ9pO%2BAOY8g%2FEjFj1t2sBWlr0pI3AY8V7iYw3iXFVCno4wpLhf0Yi0wSvWVoyIYNwHbNX%2FHUWb8kOawxxlgZSejI7iv4niJ%2FGnmaZwVAdoXbQ7AlMMGLmM4GOqUBU2KNkIVkVlfo3Dsbj91pMe%2BaGKhQD%2B748iO%2BEv5ySyg3TlqzrKiMxkZ51jl3kjY1BN268j8utzSqD%2F%2FetrQOFzgZqDWC2%2F8YZ841a1BT%2BY%2BOLGy%2FTfjdNsNtjgY12v%2BpoJHYbjKA3HWOmbM%2Bgolfj4tdvS%2FM266tcnmm5%2B3gBSosWQsQ5fyfAPduDNYhYPTrjqISGmDgVKIY2fCBuMGbDnlx%2FKgJ&X-Amz-Signature=8d2bc5c245f34b2ef2335a0432b36a9d847391290e07688e2134efc31b37fe89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







