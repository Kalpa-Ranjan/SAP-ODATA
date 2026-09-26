



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W26KSGZ%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T002028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAmUU9aDV1HIVVCnFGHK1glKF7xUwLRM0a7b0jb0cLT8AiB2Rlthj3msyt25Xlzz0IO6h82rXjzfSUQxtuBE3L5TgSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr9ez8yikPKRktuIRKtwDug8MDoKbEcOQ9I7Q4e3hfFj%2F17UIIc85XMX%2FefvRxlf9qmH0HkvMHRoVEUGdzpzYSxwO5qHN9toKFn2cLxF7WLXt%2BOnFpjH230X7APAltUafxyA1dEgA2U7wIK1QWbi6q%2B5T6wEyYB6fipLx9%2FpY2fwj%2BWbQmZQ2dwo1f0krkCDj72j2k439P2i4u0Xo9%2F835yPvswRMDIH3TwLfziqRFYIssDxoLRdiMnAoj5DC%2B1L6mG192GUwO81ZGl3rV6YJhdbCz2H4buE0O7a4J2cd8%2BFJoShf0EU1sG056Ud6gMft9sNOP6RjJhrf0KGb2xADQAKiIzzcD5DeJWtQTQeUkQNFwrHuRZ2od3El1JMlXYNppx%2BSz%2FkH1AJpZaLdxgm6NAgN8V6zkGzxCsMO3u98X2n0DY1%2FTKc1CO7CiqUE%2FyySg5l6hGg%2BA%2FKvfaoRcqV8ZInCtzoO73U6kMRk7GhROpMG99gFGqP3M2UoSgueB87JDkArD1bu99RBGQj8uDx6RrDMx7cn0rMHci36emGnT%2Fqdza0MCVmkNvEMUQuu6%2F0lNhlz1YM3YKPreJU9zoLorrD%2BO7BDnrJpcAbpKe0ael5d6bdSO6EqJRdjuwxoMCPrInXEbDmkfNDzA68wiPLb1QY6pgEVt2Yj4q0M8LNy1%2F1Ki9E05WTDTpAc5B6W6GN8FkDGfS%2FOyTY%2FZSXF0hNPsBfzTNc9tw2LoLkwt%2B9B3FzAVu02AThdYg7jVXyXsg%2F45jodBpy80STJmJGwkXgsYu61j4Yv%2F1ZRK%2Fvu3YFuV%2FOPaZXaqSsYuJFhQMWiqwxCCodu4ekqe3yAdbBL%2FnFXbS9iYPOHIb7y6LgVfgFzJSb01Ofxj8gedf9F&X-Amz-Signature=84a21eff3f6d12cee60f6b89e7092d6217eccd51401b172fd3f9853ecac0d444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W26KSGZ%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T002028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIAmUU9aDV1HIVVCnFGHK1glKF7xUwLRM0a7b0jb0cLT8AiB2Rlthj3msyt25Xlzz0IO6h82rXjzfSUQxtuBE3L5TgSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr9ez8yikPKRktuIRKtwDug8MDoKbEcOQ9I7Q4e3hfFj%2F17UIIc85XMX%2FefvRxlf9qmH0HkvMHRoVEUGdzpzYSxwO5qHN9toKFn2cLxF7WLXt%2BOnFpjH230X7APAltUafxyA1dEgA2U7wIK1QWbi6q%2B5T6wEyYB6fipLx9%2FpY2fwj%2BWbQmZQ2dwo1f0krkCDj72j2k439P2i4u0Xo9%2F835yPvswRMDIH3TwLfziqRFYIssDxoLRdiMnAoj5DC%2B1L6mG192GUwO81ZGl3rV6YJhdbCz2H4buE0O7a4J2cd8%2BFJoShf0EU1sG056Ud6gMft9sNOP6RjJhrf0KGb2xADQAKiIzzcD5DeJWtQTQeUkQNFwrHuRZ2od3El1JMlXYNppx%2BSz%2FkH1AJpZaLdxgm6NAgN8V6zkGzxCsMO3u98X2n0DY1%2FTKc1CO7CiqUE%2FyySg5l6hGg%2BA%2FKvfaoRcqV8ZInCtzoO73U6kMRk7GhROpMG99gFGqP3M2UoSgueB87JDkArD1bu99RBGQj8uDx6RrDMx7cn0rMHci36emGnT%2Fqdza0MCVmkNvEMUQuu6%2F0lNhlz1YM3YKPreJU9zoLorrD%2BO7BDnrJpcAbpKe0ael5d6bdSO6EqJRdjuwxoMCPrInXEbDmkfNDzA68wiPLb1QY6pgEVt2Yj4q0M8LNy1%2F1Ki9E05WTDTpAc5B6W6GN8FkDGfS%2FOyTY%2FZSXF0hNPsBfzTNc9tw2LoLkwt%2B9B3FzAVu02AThdYg7jVXyXsg%2F45jodBpy80STJmJGwkXgsYu61j4Yv%2F1ZRK%2Fvu3YFuV%2FOPaZXaqSsYuJFhQMWiqwxCCodu4ekqe3yAdbBL%2FnFXbS9iYPOHIb7y6LgVfgFzJSb01Ofxj8gedf9F&X-Amz-Signature=ef876ebf0da1d0ccfd0b044997603c76564d96663eb3ebccb5187a74afb12507&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







