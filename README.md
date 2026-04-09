



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBB2HCWO%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T015103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjl1qPTOglkURfgnRLl3cmIj9UcpRrSLmlRCwXWgQDWQIgPd4tsu%2Fi%2B2jo4zoXqRrPAzA7Fw8ohoH8y9U1YvnmUdkq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDCZMHFKfQrIsz1i1IircA%2B6vkE9qBBWF0mybBCKftYyKKSP2VBRaCBnx5ODTSLGqfbOPBZd0akKKDDYpFNVjIxg1VDDUab1nN6SnVHJOni16QO%2BBmG9MPRqtbEwZdSz9sXNQbJTMGA8ICy21lHYV%2BpstXM1w85WdDzBccatFZcrxPnWzZpL8hkiaI%2Fq%2F5njY6iBjnfQ0mufUd28dzEQ%2BdXXyOOXROBxLrl6weiRewj9Lo3YgpO66MXfcTu0UAtks1GV5tx6MKTW%2BgpC4SIfSk%2FBWtmu3RnnsYN0WXtLRtpcry7RCOsP5P1QJgWYo7tHSg1Ed%2F8KjgGu4U%2BKfRVGAvoyTCAyqzoFZ%2BTQIS7QcaDlBIrgWD8o5ALmCs4eGdGyaHqGnDB6IgftawbzY9krFarRsUB1vP1HnLaq2cel9%2F3lPAaWoI6gFlVosZR3ISi%2BFJ2xiyzAw50EV1CkqUK4LSDQX4w%2BKgLiCjog2V1Mj2IQGN9ttJfMa%2Bm9QUsEnpjaaUqcUkT3XJlyUYSGWGrVye1BkPSTLd7wnaV4edwmvpG%2BWYu%2F8jDp%2FYMQgn%2BlwajVt1xs5hZrnZSiT0aYQCx4ZphzduZFqZZJzI3DNKkEcTKQmjlx90FYlqHXNMTdmILkY3CAVofuCHOkZ2L5SMJ77284GOqUBxr%2BP254XxOlYjSZzUYnWo2S6VkQ9QdHnIjQzbYTWzXXP2nLH0ObBL%2FOV6raf5fHg2bZPzgUvjkv0urKk3BGHwciQs7HTLmLgAZ3Qbi5kpgdetIrNbtdejZtpczhIR27WAE%2F%2B0vd8PY3JTiIZRakyzHLozqCk%2F2rd2QMzN0VkYb4slYtBD%2BmUAsDfL1a7EASPAbHWmjZJvQhihXE%2FCNOBKGR2D%2BxW&X-Amz-Signature=d991bdb0da5d2ff44cb57d8902a6abd20213e45b32b45da69e9daa0e604428e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBB2HCWO%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T015104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjl1qPTOglkURfgnRLl3cmIj9UcpRrSLmlRCwXWgQDWQIgPd4tsu%2Fi%2B2jo4zoXqRrPAzA7Fw8ohoH8y9U1YvnmUdkq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDCZMHFKfQrIsz1i1IircA%2B6vkE9qBBWF0mybBCKftYyKKSP2VBRaCBnx5ODTSLGqfbOPBZd0akKKDDYpFNVjIxg1VDDUab1nN6SnVHJOni16QO%2BBmG9MPRqtbEwZdSz9sXNQbJTMGA8ICy21lHYV%2BpstXM1w85WdDzBccatFZcrxPnWzZpL8hkiaI%2Fq%2F5njY6iBjnfQ0mufUd28dzEQ%2BdXXyOOXROBxLrl6weiRewj9Lo3YgpO66MXfcTu0UAtks1GV5tx6MKTW%2BgpC4SIfSk%2FBWtmu3RnnsYN0WXtLRtpcry7RCOsP5P1QJgWYo7tHSg1Ed%2F8KjgGu4U%2BKfRVGAvoyTCAyqzoFZ%2BTQIS7QcaDlBIrgWD8o5ALmCs4eGdGyaHqGnDB6IgftawbzY9krFarRsUB1vP1HnLaq2cel9%2F3lPAaWoI6gFlVosZR3ISi%2BFJ2xiyzAw50EV1CkqUK4LSDQX4w%2BKgLiCjog2V1Mj2IQGN9ttJfMa%2Bm9QUsEnpjaaUqcUkT3XJlyUYSGWGrVye1BkPSTLd7wnaV4edwmvpG%2BWYu%2F8jDp%2FYMQgn%2BlwajVt1xs5hZrnZSiT0aYQCx4ZphzduZFqZZJzI3DNKkEcTKQmjlx90FYlqHXNMTdmILkY3CAVofuCHOkZ2L5SMJ77284GOqUBxr%2BP254XxOlYjSZzUYnWo2S6VkQ9QdHnIjQzbYTWzXXP2nLH0ObBL%2FOV6raf5fHg2bZPzgUvjkv0urKk3BGHwciQs7HTLmLgAZ3Qbi5kpgdetIrNbtdejZtpczhIR27WAE%2F%2B0vd8PY3JTiIZRakyzHLozqCk%2F2rd2QMzN0VkYb4slYtBD%2BmUAsDfL1a7EASPAbHWmjZJvQhihXE%2FCNOBKGR2D%2BxW&X-Amz-Signature=11d59f9872f3dc5a87cacd1698a1668a7b003106c5389ddccbbff03d2d9a56b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







