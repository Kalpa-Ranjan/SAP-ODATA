



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBBW37CO%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIH0Eu4%2Fpvz4AgnIa4iPj0q%2FOaJStdx%2FGNhI%2FaI0BNRXuAiEA2pwlCghBu1Usr2S3MpcbuEHKtOYZ6KwkCfUqOjzuv%2Bcq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDMQq4u44xQZhtzzkkSrcA%2BuaVY1mL%2FQyGGNMucuq9mVzW%2FLG5%2FVah%2BBxIbZOflGOHGkS6bdidFZgIkfwyCvoYGZ7BZYgRF%2B7gxt5oofvsHSAicdRGMyJm8zu%2B%2FCwc0HejnlKsIJHWgeqrSlJmA6qQInPvuGmxSOn5jZOom81f1koogKNFbyyc0bJlu1%2FjBfI3vjNCnpuQF0RLTyYnIqIDhb3I6D1lH34jwV5jmLup2BfaW%2BUbkyRTHrddWYwasr2vUZD4BMD5fcayybdUJS1yKz0uwDILSX0%2FwnKSsTNIS%2FPA1w9O0le95zZge%2BupkwUkgg0KJ%2BNl6BREPRCpdI%2Fusnp47cP3tbC0%2BBYA%2BWz3JUPToZ40Xxh2V0CRu5FbIeFismu%2FNQKXmFyZFF4BVcP4raJkYP%2FHFzY6ZCnIEL%2FPuRJTGeK7HAVFnkAQJNI6q6TUy8AAyFhZQex4t1eur47KEc859DzYuyEZDGuNTKJ3wlQ6q8ltgxq7op%2BX0MI7dwBls%2BYSuFoHheQgSsB9iyUsCjhEpG0Sz6vpjFYNfwRsQqi%2F9itzHMFjMtDlM4iGcloKBTODtU2iNP1TjqBaPCt7axq6hiUQtXL9aZ4A3ImEnoKu7YnQsPvVFln3yjXjFdxw5ebfJPd%2BgCAPkZQMNedqdIGOqUBL7t1R1InJMZ37GZ0FSvQP2%2BvXiw%2BVu2FLep3tgBy6BgZbHEwPGtxJ6DZ3qwksIFX9eViZjMETZ2xYgaBaEaBXOwvvhIZVNGxNTDOBKIl%2BmhDdkl2Pb5OxuZAnY3VJoT5jMi0gitjJKQHDJFdGeUQj3wnNs2e4LpeUh08j5%2FeVUNg%2F04zMkLAYjb%2Fb%2FlKt5ptck7P30sozUL4fTzCyOyd87urc5GA&X-Amz-Signature=c5935e6d20254d500194e0bdd0fb339541a92cab5c1882254d1db5c08b07359f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBBW37CO%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIH0Eu4%2Fpvz4AgnIa4iPj0q%2FOaJStdx%2FGNhI%2FaI0BNRXuAiEA2pwlCghBu1Usr2S3MpcbuEHKtOYZ6KwkCfUqOjzuv%2Bcq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDMQq4u44xQZhtzzkkSrcA%2BuaVY1mL%2FQyGGNMucuq9mVzW%2FLG5%2FVah%2BBxIbZOflGOHGkS6bdidFZgIkfwyCvoYGZ7BZYgRF%2B7gxt5oofvsHSAicdRGMyJm8zu%2B%2FCwc0HejnlKsIJHWgeqrSlJmA6qQInPvuGmxSOn5jZOom81f1koogKNFbyyc0bJlu1%2FjBfI3vjNCnpuQF0RLTyYnIqIDhb3I6D1lH34jwV5jmLup2BfaW%2BUbkyRTHrddWYwasr2vUZD4BMD5fcayybdUJS1yKz0uwDILSX0%2FwnKSsTNIS%2FPA1w9O0le95zZge%2BupkwUkgg0KJ%2BNl6BREPRCpdI%2Fusnp47cP3tbC0%2BBYA%2BWz3JUPToZ40Xxh2V0CRu5FbIeFismu%2FNQKXmFyZFF4BVcP4raJkYP%2FHFzY6ZCnIEL%2FPuRJTGeK7HAVFnkAQJNI6q6TUy8AAyFhZQex4t1eur47KEc859DzYuyEZDGuNTKJ3wlQ6q8ltgxq7op%2BX0MI7dwBls%2BYSuFoHheQgSsB9iyUsCjhEpG0Sz6vpjFYNfwRsQqi%2F9itzHMFjMtDlM4iGcloKBTODtU2iNP1TjqBaPCt7axq6hiUQtXL9aZ4A3ImEnoKu7YnQsPvVFln3yjXjFdxw5ebfJPd%2BgCAPkZQMNedqdIGOqUBL7t1R1InJMZ37GZ0FSvQP2%2BvXiw%2BVu2FLep3tgBy6BgZbHEwPGtxJ6DZ3qwksIFX9eViZjMETZ2xYgaBaEaBXOwvvhIZVNGxNTDOBKIl%2BmhDdkl2Pb5OxuZAnY3VJoT5jMi0gitjJKQHDJFdGeUQj3wnNs2e4LpeUh08j5%2FeVUNg%2F04zMkLAYjb%2Fb%2FlKt5ptck7P30sozUL4fTzCyOyd87urc5GA&X-Amz-Signature=ff5cffb0d1399b693d5151ea1d0b7784ce30ff826529d1b8209ef7d417a5d9e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







