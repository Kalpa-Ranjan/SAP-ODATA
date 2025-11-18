



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIFBPBBF%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T123302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6z8TLIBio6OffldMd%2Bvjc0Y0Gfg8xlIjSR9ixpyJ70AIhAKs313%2BysTONawY%2Fc6ieOExWve9hnapGaCw5JlDUdIa5KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUpsiyw6y%2B1QQNiVsq3ANTmuqBEbqXNQujTmjyos95XdtRYe%2FV8FD6PWnMFWodyAB1h7hXHHnJtAd1XMuf1YppFsKRd1Hf0HgGz9pxFDdZCcNKpiGUKhwtJpt9SC2QZuVkGRryFwfIGExBy3YdpFdEZoWfpop6vthfE4t8wLzwQjY%2B%2FbrbRuuVY%2FtIA9Af6o5i2iKUmh9otEpEVQRQtwvj7C%2BouYBvGPwFGRp%2F%2FEn5t5KyP1n4oDF%2BgQsHdpmxKULe%2BUy426t60XTeMeWSdm60EVWcQcoISIXB7wOkoS30Hen0w3XcFOA0Pv8vWCCIpNls2J5O4bGW9MjjpNRfDDhZrvpVs5MephnI9dGLLCWLibCYbfOWjqU%2FF5brH%2FCanwURPx%2BZgs9voBr2mDxjjekxhTAWkBh4xR0Bll0%2FydxUPeoIFUemqD93YV4zLSqZpBjh%2BnREQ15YX6%2FRp1sY7hh5V3XM5zk7omzfSLMYvHDGt1Ch%2BxUzNAbA9BiI4G6LjRnYvRP1xenOOQ7e6Q7Bcf3V5cCj1UB9bifglngMqUdVJiAnQfy1T%2FNp0Eao6wjSBbi2uPA7S7bz5OQvPQgBb%2FjGDVSKkhQsni%2FKfuRpoOQSVJ8lyIq4is7vARZB79jPb5gYBy78GMP0nJzn%2FzDmuvHIBjqkAbaVs7Iz3R3j4upey4Yx0fa51wHl1kP9Yr%2FDB%2F3ImjeTN3NstenIDbIz6nGtzYrlAeEd82Wxa40Uk4o%2BkYZKLQec7K3yQO59lGdDeLy6fh3iPfDh2L4ojkMIGsgaJ8CmIJ9pXtNODosTETQ3rr5TQD%2B7R%2BjAm0a7%2Fu8%2F3t2OqXIuhd9IA1lyrRZJ4DugMTBC%2FQVjeh5gpccDiSiHQRvLzCBCgvlJ&X-Amz-Signature=4d70e6cddcf596f92c66c27211d6b775104abe91575e6954a2d13549fa4afa4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIFBPBBF%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T123302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6z8TLIBio6OffldMd%2Bvjc0Y0Gfg8xlIjSR9ixpyJ70AIhAKs313%2BysTONawY%2Fc6ieOExWve9hnapGaCw5JlDUdIa5KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUpsiyw6y%2B1QQNiVsq3ANTmuqBEbqXNQujTmjyos95XdtRYe%2FV8FD6PWnMFWodyAB1h7hXHHnJtAd1XMuf1YppFsKRd1Hf0HgGz9pxFDdZCcNKpiGUKhwtJpt9SC2QZuVkGRryFwfIGExBy3YdpFdEZoWfpop6vthfE4t8wLzwQjY%2B%2FbrbRuuVY%2FtIA9Af6o5i2iKUmh9otEpEVQRQtwvj7C%2BouYBvGPwFGRp%2F%2FEn5t5KyP1n4oDF%2BgQsHdpmxKULe%2BUy426t60XTeMeWSdm60EVWcQcoISIXB7wOkoS30Hen0w3XcFOA0Pv8vWCCIpNls2J5O4bGW9MjjpNRfDDhZrvpVs5MephnI9dGLLCWLibCYbfOWjqU%2FF5brH%2FCanwURPx%2BZgs9voBr2mDxjjekxhTAWkBh4xR0Bll0%2FydxUPeoIFUemqD93YV4zLSqZpBjh%2BnREQ15YX6%2FRp1sY7hh5V3XM5zk7omzfSLMYvHDGt1Ch%2BxUzNAbA9BiI4G6LjRnYvRP1xenOOQ7e6Q7Bcf3V5cCj1UB9bifglngMqUdVJiAnQfy1T%2FNp0Eao6wjSBbi2uPA7S7bz5OQvPQgBb%2FjGDVSKkhQsni%2FKfuRpoOQSVJ8lyIq4is7vARZB79jPb5gYBy78GMP0nJzn%2FzDmuvHIBjqkAbaVs7Iz3R3j4upey4Yx0fa51wHl1kP9Yr%2FDB%2F3ImjeTN3NstenIDbIz6nGtzYrlAeEd82Wxa40Uk4o%2BkYZKLQec7K3yQO59lGdDeLy6fh3iPfDh2L4ojkMIGsgaJ8CmIJ9pXtNODosTETQ3rr5TQD%2B7R%2BjAm0a7%2Fu8%2F3t2OqXIuhd9IA1lyrRZJ4DugMTBC%2FQVjeh5gpccDiSiHQRvLzCBCgvlJ&X-Amz-Signature=03304a4a61f7660557e7ded97c387da58e99debac8343ecb3db62acccbeac131&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







