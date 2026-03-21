



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAL2OFNV%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T182932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQoN0M2Nzr5xslmdxoR58kXCmc1vA1XrrHpRX4%2Fkv5OAiB6mLX5K%2BOLWU3GFwKJaAQWH07f9a5Z%2FWcI1d5zZC0u%2BCr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMsgdsfPEPksWhkAFTKtwDSr4%2FA4USXam8zxCuUYdqp7TvY8rMqfOBX0OZddLnE%2FIHcJGExDQSCF%2F9RZw1S4HWpOBNZo1Kob1Lq9Pw61iAjj7dwk3viSphM0nID0Xd8P7Vm6j9MHvd2BUc1V3BBpfDX5XP28lRT04oDGVhMiVDafaWjtSj3%2F6BWq4H0HIhFLpqhEtu04TC8MKD%2FKqYMnnWtubqLIoz9bUS35bRZkwbbAKMyUK49362Rlug7o%2BK%2BmN6A3%2FZohisRJtjfAqrO1lL%2FJi0Xh1hUHm8DRtcQkgeE44nid6j6%2BiYEYUWlOkVUo3MjEGkb6wTiPFUsk4tDGKzW1NBjJKwj%2F0gm4DhOjJx8%2FspD6lomuFt2KCPMAWLRJWbAZ3XBOUaibhpVGXPDg0d7ydj5ahAuc2BkrOCKwoikBG6jZzMHfEFTmVsCZF%2B3syLnPn%2Bi%2Fl3rYRJCUhYmH8JEODfcFaPvMA1yCvSSGNiRNuGyuQ5qsWiTUFpOh1Rwwu6Fs1YMJ8L2geYzw1Lvz2kVDx9UcY47dHiZJuQKv5S5My7gkDBSjTzp0E6%2B0bIauiIUfKb7EhVuIJGMdgWx%2BwEzvRAWDiVvGdHJYUb1qPyUhzIkqIbpko4tKiQ0ARm%2B%2BZK7WjS1SPWN1fApeswir37zQY6pgEGiwKQtdoA8VFjpHEczgrO09xjvmjM3%2Bm8i407W%2BM6bdBgPqs3xrWZOZ1d0Fm%2BhaqZn6CAtLTTg0zdJoS8JkBYLTCfV1XAyZhegScDGQ8fbv5QTqBnmgxWiLVQ3OKAf1qAT4T2JdKcEpdvZZAK9I0K6ZuX0kLTOCtuKcpWWHolfhgrQZIPkuWmYNwFLmpvXjRdMKBX7GloZKMa5D3tuQg5ZGfq%2FCDk&X-Amz-Signature=df9c0333b6ecff954044e9ffcf5fc77dce766b1af07142533924963ba87ec9cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAL2OFNV%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T182932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQoN0M2Nzr5xslmdxoR58kXCmc1vA1XrrHpRX4%2Fkv5OAiB6mLX5K%2BOLWU3GFwKJaAQWH07f9a5Z%2FWcI1d5zZC0u%2BCr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMsgdsfPEPksWhkAFTKtwDSr4%2FA4USXam8zxCuUYdqp7TvY8rMqfOBX0OZddLnE%2FIHcJGExDQSCF%2F9RZw1S4HWpOBNZo1Kob1Lq9Pw61iAjj7dwk3viSphM0nID0Xd8P7Vm6j9MHvd2BUc1V3BBpfDX5XP28lRT04oDGVhMiVDafaWjtSj3%2F6BWq4H0HIhFLpqhEtu04TC8MKD%2FKqYMnnWtubqLIoz9bUS35bRZkwbbAKMyUK49362Rlug7o%2BK%2BmN6A3%2FZohisRJtjfAqrO1lL%2FJi0Xh1hUHm8DRtcQkgeE44nid6j6%2BiYEYUWlOkVUo3MjEGkb6wTiPFUsk4tDGKzW1NBjJKwj%2F0gm4DhOjJx8%2FspD6lomuFt2KCPMAWLRJWbAZ3XBOUaibhpVGXPDg0d7ydj5ahAuc2BkrOCKwoikBG6jZzMHfEFTmVsCZF%2B3syLnPn%2Bi%2Fl3rYRJCUhYmH8JEODfcFaPvMA1yCvSSGNiRNuGyuQ5qsWiTUFpOh1Rwwu6Fs1YMJ8L2geYzw1Lvz2kVDx9UcY47dHiZJuQKv5S5My7gkDBSjTzp0E6%2B0bIauiIUfKb7EhVuIJGMdgWx%2BwEzvRAWDiVvGdHJYUb1qPyUhzIkqIbpko4tKiQ0ARm%2B%2BZK7WjS1SPWN1fApeswir37zQY6pgEGiwKQtdoA8VFjpHEczgrO09xjvmjM3%2Bm8i407W%2BM6bdBgPqs3xrWZOZ1d0Fm%2BhaqZn6CAtLTTg0zdJoS8JkBYLTCfV1XAyZhegScDGQ8fbv5QTqBnmgxWiLVQ3OKAf1qAT4T2JdKcEpdvZZAK9I0K6ZuX0kLTOCtuKcpWWHolfhgrQZIPkuWmYNwFLmpvXjRdMKBX7GloZKMa5D3tuQg5ZGfq%2FCDk&X-Amz-Signature=578a34d8917b04deb7e60f3adec5e39156c2ef9b292bbc198a922d9a4ce252e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







