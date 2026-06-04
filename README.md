



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W422ZM2%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T144642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjXvmu49lQXyUM6dzmc4GAb9kGt9nePFOWzwd6RDo1%2FAiAP0pBJtRp%2FiObJjUARQQzsWSX3tWow2fqOe1YLiQHZNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM7DqB7EHRkqvVqT%2FmKtwD791vk9ldBWn7Sxr%2F%2F%2BvkCEURYU0m8kNcFVsiYEfOqBhscEKLL47zaHmw%2F7yFZuYlXxdhFhRgEJLSJJM15M0%2FRl7rDTsdNflOBtx5ekpv%2FFmdQA%2FVwoZjdk7R3JbbLctFIwNDc%2FilDoS95qcdYip7KYkjMR0NVqTAZz71Ov0k4k%2FtsjRWQdDvMCPbgArttDcjWGK3hyCEqapDSPZnpq4If1OA1PornF6SmpM%2F4VqWRK5j5B28rHES1JMpV4BQSwnlNB4FKnIKEWmxPRxwe%2BcQ3nLf4lcSvq2r3muHarH7sYn2c%2FX%2BggrjjDvqcsweFLyK5RUDmMV0DVLh68%2Ft7QG4OKFoVqvr6t6LfVm4H8fRR62ZQ9r0yxAtLXoHjwFEwwhoJDoeMR0CpeJkPmVYtiF%2Bk7K9g2geRHvBrEmVEKUNmI8BBUx%2Bs%2FW5K2738wkQgFIwvetS%2F3wIT%2BfpJqfF4UvtKhGPRQCDb4NP217COM14MK8uoTKKf1sIKBaXrImtfgSXlMIX1XtFtRESjB9lbSJcPoI11r9S7soxXp%2Fl6gUSL5OJLrWeoMayQZh%2B31t4tV5l%2B8NDSxvNDLIPHwoTknu%2FloByFGAVv%2Bbcml%2FdefkoZUl%2FD6rdq99Fo52f1fkwqf%2BF0QY6pgEaDSJqxT7gMGjACb3wzt166hyrwHWmyBnsB2UwzA%2B1ovddhGFmK3RVqVo837q35ildGaCJJblNG8WiGYgWpCUJfRMJRbdXe1gO7EI2h7asmwu%2FYFpyUSzc2WGHCrIH9DpDMFbLTe1BiYCFDZkoZuM944BdYPfhQQyMkKZ5%2BS4xY24uwybzBIUhG9xRR8XH47%2BbhHCDD8j3aOkRHrRWPO0Y2dQ%2Biy2d&X-Amz-Signature=fd7545309360017f7065e609845ce253ea193cc554ee62c16bcd9f799600f7fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W422ZM2%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T144642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjXvmu49lQXyUM6dzmc4GAb9kGt9nePFOWzwd6RDo1%2FAiAP0pBJtRp%2FiObJjUARQQzsWSX3tWow2fqOe1YLiQHZNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM7DqB7EHRkqvVqT%2FmKtwD791vk9ldBWn7Sxr%2F%2F%2BvkCEURYU0m8kNcFVsiYEfOqBhscEKLL47zaHmw%2F7yFZuYlXxdhFhRgEJLSJJM15M0%2FRl7rDTsdNflOBtx5ekpv%2FFmdQA%2FVwoZjdk7R3JbbLctFIwNDc%2FilDoS95qcdYip7KYkjMR0NVqTAZz71Ov0k4k%2FtsjRWQdDvMCPbgArttDcjWGK3hyCEqapDSPZnpq4If1OA1PornF6SmpM%2F4VqWRK5j5B28rHES1JMpV4BQSwnlNB4FKnIKEWmxPRxwe%2BcQ3nLf4lcSvq2r3muHarH7sYn2c%2FX%2BggrjjDvqcsweFLyK5RUDmMV0DVLh68%2Ft7QG4OKFoVqvr6t6LfVm4H8fRR62ZQ9r0yxAtLXoHjwFEwwhoJDoeMR0CpeJkPmVYtiF%2Bk7K9g2geRHvBrEmVEKUNmI8BBUx%2Bs%2FW5K2738wkQgFIwvetS%2F3wIT%2BfpJqfF4UvtKhGPRQCDb4NP217COM14MK8uoTKKf1sIKBaXrImtfgSXlMIX1XtFtRESjB9lbSJcPoI11r9S7soxXp%2Fl6gUSL5OJLrWeoMayQZh%2B31t4tV5l%2B8NDSxvNDLIPHwoTknu%2FloByFGAVv%2Bbcml%2FdefkoZUl%2FD6rdq99Fo52f1fkwqf%2BF0QY6pgEaDSJqxT7gMGjACb3wzt166hyrwHWmyBnsB2UwzA%2B1ovddhGFmK3RVqVo837q35ildGaCJJblNG8WiGYgWpCUJfRMJRbdXe1gO7EI2h7asmwu%2FYFpyUSzc2WGHCrIH9DpDMFbLTe1BiYCFDZkoZuM944BdYPfhQQyMkKZ5%2BS4xY24uwybzBIUhG9xRR8XH47%2BbhHCDD8j3aOkRHrRWPO0Y2dQ%2Biy2d&X-Amz-Signature=d2f0ea05aa9cc5dd6f402b4f8b999ebc85d07b1909208b0b86d8649851d18f54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







