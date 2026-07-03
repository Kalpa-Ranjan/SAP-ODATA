



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DPJO77G%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T022851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCICPewpInKm9h9Q93z%2B2R0SKEDEJESo3ZSf3bOb5f6nLyAiAuCFLhBw60Dl3Z1sPDI1tEO6j%2FDUcwqhmmvQyZgVS6tCr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMhiAhj1Wl39N9CqC9KtwDOZ8adsaddAtJn0bnHp0ty6pfmn%2B4j7%2B9aGwNVPRETuJ62%2FH3XZrkn%2FR9kLpRbj4ZUKg2Y2LFOYgR8lAHDHiJON8WV204QV64QSHSobyjZP6MjH8ccDQK7XjXWuSWRHbHtFt4TdEKsWX7MD0Q9Tfrh38WryfVQ5GHIsxYaxck%2Bu%2FOZeZHXyLsgn9PP5h0pHbTYE%2Fox3MUmy3%2Bpng3tB8pQYkp98gbct7ZxMGi0w%2B2P854yrxIkGF5IaH90Hx6QgqkAPjXYz6ZuHiJgMoE0WvojHbs%2FUsE6UE4VsNL%2BklzibEUsxEHF%2BK%2BhiDfIh%2BwzBEc1ig1MBdp3StR1ATxn4b%2BoUGXGTYM8VpkCVi3bTRYxStAFDyIR1GlN%2F%2B7zZxORwqCXGYSy60oWi0EZAbGLcbGWoS5tGCv9Uq00D8OpompFU3Zg3lNl3ujk2Sl%2Fj4Hw9g3pAsHN8C7tMRb9fkgl5Loentra68UI01nwQVXq9bPvKT7vgrqqQmqD1nx6yXjf1bhaiTexWUDLgXLkgiQdFFN9GHw6SrLZnrlmLXZeNJp%2BbOQt8IfoH%2FKgQp4mc%2Bopyozdn86cG8f9i%2BeqAtqx%2FbQ8ykVg4j%2FVcST8L6bF5ZW51J7LRXTHVOcWd%2ByLq8wwbmc0gY6pgFvYGIt1qh5dG95tU7nzTG4bThN%2FrPE2kbJv%2BKdAvZoLjoNwVKnc2nfyE2IvwCrqaDMmWKQ1S5NFNsGnc1cnoyaBTnhouVsc7iYUDjG7w9ResyCyHvh%2BEjE75CSZghKkN0jAk6u4ZN5chSLvLjVQ2Kq%2BaAZc%2FKfaNUwPHg7nI0gYrozIkG6p3sAOX%2Ffhro3PWjwyxGMyacb%2BBQKmV%2FvxWGX58vcz80s&X-Amz-Signature=b116fc428a850cb5d6870e11113d94e8484d19f34a75b9944bc23e882318e1d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DPJO77G%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T022851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCICPewpInKm9h9Q93z%2B2R0SKEDEJESo3ZSf3bOb5f6nLyAiAuCFLhBw60Dl3Z1sPDI1tEO6j%2FDUcwqhmmvQyZgVS6tCr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMhiAhj1Wl39N9CqC9KtwDOZ8adsaddAtJn0bnHp0ty6pfmn%2B4j7%2B9aGwNVPRETuJ62%2FH3XZrkn%2FR9kLpRbj4ZUKg2Y2LFOYgR8lAHDHiJON8WV204QV64QSHSobyjZP6MjH8ccDQK7XjXWuSWRHbHtFt4TdEKsWX7MD0Q9Tfrh38WryfVQ5GHIsxYaxck%2Bu%2FOZeZHXyLsgn9PP5h0pHbTYE%2Fox3MUmy3%2Bpng3tB8pQYkp98gbct7ZxMGi0w%2B2P854yrxIkGF5IaH90Hx6QgqkAPjXYz6ZuHiJgMoE0WvojHbs%2FUsE6UE4VsNL%2BklzibEUsxEHF%2BK%2BhiDfIh%2BwzBEc1ig1MBdp3StR1ATxn4b%2BoUGXGTYM8VpkCVi3bTRYxStAFDyIR1GlN%2F%2B7zZxORwqCXGYSy60oWi0EZAbGLcbGWoS5tGCv9Uq00D8OpompFU3Zg3lNl3ujk2Sl%2Fj4Hw9g3pAsHN8C7tMRb9fkgl5Loentra68UI01nwQVXq9bPvKT7vgrqqQmqD1nx6yXjf1bhaiTexWUDLgXLkgiQdFFN9GHw6SrLZnrlmLXZeNJp%2BbOQt8IfoH%2FKgQp4mc%2Bopyozdn86cG8f9i%2BeqAtqx%2FbQ8ykVg4j%2FVcST8L6bF5ZW51J7LRXTHVOcWd%2ByLq8wwbmc0gY6pgFvYGIt1qh5dG95tU7nzTG4bThN%2FrPE2kbJv%2BKdAvZoLjoNwVKnc2nfyE2IvwCrqaDMmWKQ1S5NFNsGnc1cnoyaBTnhouVsc7iYUDjG7w9ResyCyHvh%2BEjE75CSZghKkN0jAk6u4ZN5chSLvLjVQ2Kq%2BaAZc%2FKfaNUwPHg7nI0gYrozIkG6p3sAOX%2Ffhro3PWjwyxGMyacb%2BBQKmV%2FvxWGX58vcz80s&X-Amz-Signature=a96f5ec6ca585ec86fb4fada2bdaf0628d4e549ce0e4e527bbecc184746e40fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







