



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHFRZC2%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T184946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIHTApE7F7Zz1xPRsM00XjHXS72JM9ZvRBCqjUjNL%2FkqVAiEAl28%2FwlSY2miGdd5VlfwkXi%2F%2Bumk%2FcmWbDN0eYzFrc8UqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdhfxIYfZh7R%2FKQTyrcA6GCkSK%2FHzw87PXfqTybeO6dCXFuexcap5q4gZIR6hrNN6bTxgoI%2FHfa3baE1IyjVcpR4D7JeTS5gxo5Ph97gxonhkhZNXWnyIxJbzf9PxJ3wRrT6d1knIUw8FNeMqHZ%2Bxepz0NNsSSSDRdE9g5URjBnv4mufPAwrHCPH4qBitKOJZuFq7YXHPdDfHdcFLZpLQf97m5WYxdacVhPKM8XNbEgyOXVwBoidyoaqCQK60mIwqfz1apH5wSJiu%2FCoU4AR3NZ5V%2Bk4tmBmAhIU6A8YJDI7VFXWDXssrKTi0roQGSp4G5hsn1IGvm05jZ7%2FsfTYWaoRuiO29ccn5HZCeypvI%2F5vi4hqbKtX3CXGFuTB96Jx%2Bbyo1Tur8o4TuDz5fl4PAUhAAzuDb2hzQ%2FwzqUpZ08xH7HqeOO1OGwZB%2BOQtVWIkS8uVUUl8B4kUPo0DR2tvx8gzIv68ZCqgHo9WcrCVrLHPLqtP3syruS%2FL4kkL39Yl9tb8tr9FdovIIcuOqlakKvVVwh2ImLwYq%2B834paViyK%2FHVt3SjTzM2ysQmgspDNzmqxiK%2FZq6D%2B%2FkuvXhYstjlppubtjt9tqXXIv09Bt9w%2BZ7SJCgamxxoUbWEwDw09NaPcbJOaASjVeckDMLjOms4GOqUBeY1ZWPB0uhk40bHVV0nqN1UAuzKTmA54WVJOEdGSwWFPDthe2Z2EM0bOScF0gPjN6Yp%2BNsjZYFN6zaK%2BN0rjyBnttJ8dhN9llKwoIdlEOUgNhaYEHO84QB2YVgtgxe8W7gyRX31qHF%2B917hGZG8F%2BzVGMK4twCfS3Hh3wxq131cxreIpq2UFgaRz5EQjP7MML%2B1%2Fpa8e5Bi6HDs3%2FNroF%2FgizaIw&X-Amz-Signature=cf70f909e66c25a8b4c959e39f72017dfc09e541f62222ce77de226c88a9bcc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHFRZC2%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T184946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIHTApE7F7Zz1xPRsM00XjHXS72JM9ZvRBCqjUjNL%2FkqVAiEAl28%2FwlSY2miGdd5VlfwkXi%2F%2Bumk%2FcmWbDN0eYzFrc8UqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdhfxIYfZh7R%2FKQTyrcA6GCkSK%2FHzw87PXfqTybeO6dCXFuexcap5q4gZIR6hrNN6bTxgoI%2FHfa3baE1IyjVcpR4D7JeTS5gxo5Ph97gxonhkhZNXWnyIxJbzf9PxJ3wRrT6d1knIUw8FNeMqHZ%2Bxepz0NNsSSSDRdE9g5URjBnv4mufPAwrHCPH4qBitKOJZuFq7YXHPdDfHdcFLZpLQf97m5WYxdacVhPKM8XNbEgyOXVwBoidyoaqCQK60mIwqfz1apH5wSJiu%2FCoU4AR3NZ5V%2Bk4tmBmAhIU6A8YJDI7VFXWDXssrKTi0roQGSp4G5hsn1IGvm05jZ7%2FsfTYWaoRuiO29ccn5HZCeypvI%2F5vi4hqbKtX3CXGFuTB96Jx%2Bbyo1Tur8o4TuDz5fl4PAUhAAzuDb2hzQ%2FwzqUpZ08xH7HqeOO1OGwZB%2BOQtVWIkS8uVUUl8B4kUPo0DR2tvx8gzIv68ZCqgHo9WcrCVrLHPLqtP3syruS%2FL4kkL39Yl9tb8tr9FdovIIcuOqlakKvVVwh2ImLwYq%2B834paViyK%2FHVt3SjTzM2ysQmgspDNzmqxiK%2FZq6D%2B%2FkuvXhYstjlppubtjt9tqXXIv09Bt9w%2BZ7SJCgamxxoUbWEwDw09NaPcbJOaASjVeckDMLjOms4GOqUBeY1ZWPB0uhk40bHVV0nqN1UAuzKTmA54WVJOEdGSwWFPDthe2Z2EM0bOScF0gPjN6Yp%2BNsjZYFN6zaK%2BN0rjyBnttJ8dhN9llKwoIdlEOUgNhaYEHO84QB2YVgtgxe8W7gyRX31qHF%2B917hGZG8F%2BzVGMK4twCfS3Hh3wxq131cxreIpq2UFgaRz5EQjP7MML%2B1%2Fpa8e5Bi6HDs3%2FNroF%2FgizaIw&X-Amz-Signature=074430571a8071b18a3681e73e42dc1b48df3cc62939d55fa589bc500b5659ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







