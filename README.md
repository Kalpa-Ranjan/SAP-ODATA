



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC42FAKF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T184348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDy18D2Hy4LKSHYqvSdmXGhVjIolh4MzUNJ3p6KwLQewwIgBLh0n9CZFlop5m6rzUzeFbUvMEUCVgw3po3ibtkgjXkqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLjvTV84R3QpDL3R0CrcA1LkXyqUPap0q0nKxQzl97ulm5syp7pX9eLQFjg6dJU3KVC2cWK0zSA7FiZeZLFnlQMdSURKpyRzLvLXvDMUEHTK8Texhw1cMnB2uLgBe1v4DbQOsslqovDaa1fBPmFtp%2FQyFytDc7rz3tqYqbP7l0HA4DsiW2hrveunY6SJQu2uBs3vMPvhuMF0azF%2Ff83baDF2nhDYF%2Bv0wdM%2FsNQtRU5JYSk7zds3RzqweA1deFd8pQJ5leWRAH94C6TnCPuhbzW0hTByoDbM2hqTlXqcT53Qh0NzoE3VSkQ6lWzM78fJX5bBaTFtGUvr%2BGO2JMO4XUrvhRmgRPQEJ%2B2nhY34A7spULX6kSwcI0bcFmESQ1IIq1usBJ9n%2BUFjrtVqiOJMeYvMBXW%2FBpsaz4zwyVsTVevN9UZKjc%2FHJZo702L1x1uSYkbuYfCl9W1R3x2MckexOQ5y3SNyUrvXa3m67Ejm2G%2FVtQS1LHFHaJ84bSnVnQOJ%2BJBfx0mJOS4xUlkc1EUzN6D8f1w8mEpBaZ%2BIv2gfDsABiSDRMzhUpTDay3yRm8dpkYX6GlWxBhGVZe%2BzIXjLE%2BqIC1BTqFZZXbtCiAiiXzt0gLDCr9x9HFnkobox%2BSyZgSQtkgVCC769KfFfMOyG3cwGOqUB24QPe243ShSZmtLHZefCXVa7ytX77st5%2FMnE06s0iIbsJSZPiOrVE3kjVyPUgNda8mqH93beE%2FWSUapYX8PDYqDW7A6iBykysZuKXusRKkdZZKUG2g%2FKWOmkQa479IdWOdlUhyVMTryK%2BRxGQr6RUjt2Tdz%2FVcDwfu2WE2jILzH4hn47XFMKGg9iBoCKIR4XtylGxtJT8J0IRwyWilA%2B6FU3wbhq&X-Amz-Signature=33ad8cd7555cf23945c3e5a56f947316baf5938d360560fa162f65801eed4f99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC42FAKF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T184348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDy18D2Hy4LKSHYqvSdmXGhVjIolh4MzUNJ3p6KwLQewwIgBLh0n9CZFlop5m6rzUzeFbUvMEUCVgw3po3ibtkgjXkqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLjvTV84R3QpDL3R0CrcA1LkXyqUPap0q0nKxQzl97ulm5syp7pX9eLQFjg6dJU3KVC2cWK0zSA7FiZeZLFnlQMdSURKpyRzLvLXvDMUEHTK8Texhw1cMnB2uLgBe1v4DbQOsslqovDaa1fBPmFtp%2FQyFytDc7rz3tqYqbP7l0HA4DsiW2hrveunY6SJQu2uBs3vMPvhuMF0azF%2Ff83baDF2nhDYF%2Bv0wdM%2FsNQtRU5JYSk7zds3RzqweA1deFd8pQJ5leWRAH94C6TnCPuhbzW0hTByoDbM2hqTlXqcT53Qh0NzoE3VSkQ6lWzM78fJX5bBaTFtGUvr%2BGO2JMO4XUrvhRmgRPQEJ%2B2nhY34A7spULX6kSwcI0bcFmESQ1IIq1usBJ9n%2BUFjrtVqiOJMeYvMBXW%2FBpsaz4zwyVsTVevN9UZKjc%2FHJZo702L1x1uSYkbuYfCl9W1R3x2MckexOQ5y3SNyUrvXa3m67Ejm2G%2FVtQS1LHFHaJ84bSnVnQOJ%2BJBfx0mJOS4xUlkc1EUzN6D8f1w8mEpBaZ%2BIv2gfDsABiSDRMzhUpTDay3yRm8dpkYX6GlWxBhGVZe%2BzIXjLE%2BqIC1BTqFZZXbtCiAiiXzt0gLDCr9x9HFnkobox%2BSyZgSQtkgVCC769KfFfMOyG3cwGOqUB24QPe243ShSZmtLHZefCXVa7ytX77st5%2FMnE06s0iIbsJSZPiOrVE3kjVyPUgNda8mqH93beE%2FWSUapYX8PDYqDW7A6iBykysZuKXusRKkdZZKUG2g%2FKWOmkQa479IdWOdlUhyVMTryK%2BRxGQr6RUjt2Tdz%2FVcDwfu2WE2jILzH4hn47XFMKGg9iBoCKIR4XtylGxtJT8J0IRwyWilA%2B6FU3wbhq&X-Amz-Signature=3a296c26c86399231b0bca7eb558ef89bb5022a6281e32000e2ed92b408b821a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







