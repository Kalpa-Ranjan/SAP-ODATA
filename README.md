



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URFYCLVJ%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T152501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXNlOnM6AabQ32vBNgZbvM%2FzYK7Qk7%2FD%2Bi874U65l1xgIhAIpVTVa7wtbxSnD5p6WNKZ6HMwTagtfg8e0%2FPyYhF6JyKogECJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGGV3TEDUVgZnUPZsq3AMO0jwyk0yE24gh%2BLg6JCi%2FIHBCYoZ7J9%2BcbQzrrjDLfimjHElr080xeO%2FMhx7ReUz6Ici6bUvHRSSIfOJPZgolQ2SbXbgPjhZ3NDsjSYM69UAsgk04mAHnAqU04G3xu0vyVRXU5b4Mt%2B6LO3DmnoBxb%2BqfPL4aKqOSwgeBIYaau4woE6sc0vy2puddskAO7wyT9eL%2Byzz1BGJSAU3ow1smxPh2XFa6OObc1uXHMS207VDW08u5d0lkELEZ8Ooa9xCmFe5IzJSiUmh%2B7Cw1b%2BEEfDyCLTw3J4K8ZAPMx4CeyW1Q7R56hK5EHipxg5lCAsLxO7r5EqTuyBQsIGd9%2FsSDg1unRcbS%2FissDhcnskiyHbJnGv0Lc6iwy38K5KtADef6PCbDM%2BGShfg3Hj3lbB%2FXAYotThn985s4LjnBWY8qoIE9p3Acjx9NYRaks21PQtH%2FT1Wc2yL3rueq8qCIpCve57OO60tQn9Q%2Bh%2FT0MwbtGqYUCumqG6B1UII%2Fk96GUB0892QGpX9379vbP%2Fu1tUY%2Bz3qLq1hXv2PRgPVZfaVqzfpljcjMRbhqxX%2FMqAzRqBDNZECAEi69Y9BixVDmKA0gLaUz6Zq5Fx0Ilh0bAuMcbs7RQUAMLT35Rqvc7TCOg9zQBjqkATXFlNjuH5pkPDueuZqUer%2Fz4p32PEE9E2IrmSkgLeLteeCU%2FWPQxSXTNSQzMFh1OYnKiJCh4mG5vcaDlJFXfyDLFn9rZGsNFJiZ4R7T%2BY46V4z7vBcHLlMChD%2BlnFa0%2ByjXZU6i4k%2BuOfI7S8oYiMtdhijOD8%2BbEksja3tu%2Fc7ipGVsT2G3g9yPLmaqK%2BYJLvXxxQ745BrRIEJFaZdf40hPOEcw&X-Amz-Signature=b78bd2ac17cbfa94926528c36808cac3acdda661bab573132de42f50ba451f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URFYCLVJ%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T152501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXNlOnM6AabQ32vBNgZbvM%2FzYK7Qk7%2FD%2Bi874U65l1xgIhAIpVTVa7wtbxSnD5p6WNKZ6HMwTagtfg8e0%2FPyYhF6JyKogECJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGGV3TEDUVgZnUPZsq3AMO0jwyk0yE24gh%2BLg6JCi%2FIHBCYoZ7J9%2BcbQzrrjDLfimjHElr080xeO%2FMhx7ReUz6Ici6bUvHRSSIfOJPZgolQ2SbXbgPjhZ3NDsjSYM69UAsgk04mAHnAqU04G3xu0vyVRXU5b4Mt%2B6LO3DmnoBxb%2BqfPL4aKqOSwgeBIYaau4woE6sc0vy2puddskAO7wyT9eL%2Byzz1BGJSAU3ow1smxPh2XFa6OObc1uXHMS207VDW08u5d0lkELEZ8Ooa9xCmFe5IzJSiUmh%2B7Cw1b%2BEEfDyCLTw3J4K8ZAPMx4CeyW1Q7R56hK5EHipxg5lCAsLxO7r5EqTuyBQsIGd9%2FsSDg1unRcbS%2FissDhcnskiyHbJnGv0Lc6iwy38K5KtADef6PCbDM%2BGShfg3Hj3lbB%2FXAYotThn985s4LjnBWY8qoIE9p3Acjx9NYRaks21PQtH%2FT1Wc2yL3rueq8qCIpCve57OO60tQn9Q%2Bh%2FT0MwbtGqYUCumqG6B1UII%2Fk96GUB0892QGpX9379vbP%2Fu1tUY%2Bz3qLq1hXv2PRgPVZfaVqzfpljcjMRbhqxX%2FMqAzRqBDNZECAEi69Y9BixVDmKA0gLaUz6Zq5Fx0Ilh0bAuMcbs7RQUAMLT35Rqvc7TCOg9zQBjqkATXFlNjuH5pkPDueuZqUer%2Fz4p32PEE9E2IrmSkgLeLteeCU%2FWPQxSXTNSQzMFh1OYnKiJCh4mG5vcaDlJFXfyDLFn9rZGsNFJiZ4R7T%2BY46V4z7vBcHLlMChD%2BlnFa0%2ByjXZU6i4k%2BuOfI7S8oYiMtdhijOD8%2BbEksja3tu%2Fc7ipGVsT2G3g9yPLmaqK%2BYJLvXxxQ745BrRIEJFaZdf40hPOEcw&X-Amz-Signature=f1272c55e8c2b7d6fe456aa589c584797d4ca5c305804a86eae7654e99bff0ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







