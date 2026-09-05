



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFOJ7MM%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T095101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiCl%2FAaYuHQ43GmgXSb3GDta6W9Q%2F%2BPZXFEKyD4udZZwIgSJRZ%2FLBCJ4Pf%2FQfiZ4wHLFe0yghb62GXJfUI5ISv8tsq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDOud6eFl5dwS8Oq6gCrcAyjJeuP3wImDRfvsTCMpohJa52hX4bThh83ZhHsD3Zu7OSm3kXa4eEPt2U7XhGIut8V%2B%2B3nq5ny3erZqH7sm4BPFjrgBgkiipM9b4t1HtO5vaDIE2xFxiabe8%2Fl4PAdv7qyTFMCc%2BS53mjVOIbzus7U9guFSQyc%2FHH0OtdX3wKtcou%2BAY5f4UkOFgZ%2BcUx8v1kngrCWMSg6yOP26ExTkWGqVv8ObulY4nn8GBVUbi7EE6v3FzbKzHxo7mtqC%2BdlA1dRsvUSqd%2B3lWrF39fiGf3aNJch0YhWZd7ufjp%2Bpt%2FBDMIBt%2FPuyt6wrp8CMaCXB20GKHlhNWJZtUm5c5l%2FvC9xDOhFbbg%2FP6KWyLuNmnhwf0mFwjIP3BDqQykTH7hStmCi1BIuAhvZHFP2xvg66gSO6d60M2yfBlOUtp5Wi2pyMd%2FhzYlrYIhme5zYFDRhpJa7yDfWF695wiUPyL1bwhPJk7n%2BbIidUSN0ArysTNiMcgBu0oJCmpMcLUhSrpQVPqg2HzGI6JKl9SYwOWgdLOtzI8mkzIr2sHdfeIWxJ9Ec6NKuYE1KkEToKo1fcf2oURMHdFzanp%2BJjYnzMCuW4yAgsVf%2Bzvmt%2FGk5XrQTgok%2BrCCveXkDaE%2FFiiv2jMJWl79QGOqUByknEOHXiyBFKhgpkb3ABDME8ZyfaYqpTDIy3CQdjKaQVOfRmJpNs%2F3fK18XcDNaVtb3cjGYS4Y%2F%2BhswusXkiO4mAQ5GPorbXnFdJe53ZAf9hh8GmNuj6W3dhbyn9ceFQ076tjFsZ8mnYg%2BHoHkasFTqXD9pHrg66qWIbsrLS05wsfSw9pphB3bEFmo0Y%2BWRrQNVW7yJXCQhPVjFjH9XU57mzwiHi&X-Amz-Signature=9f24cad5067ee2284e255e413f6323cf35628f6300d2a5b882cefd60019df9fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFOJ7MM%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T095101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDiCl%2FAaYuHQ43GmgXSb3GDta6W9Q%2F%2BPZXFEKyD4udZZwIgSJRZ%2FLBCJ4Pf%2FQfiZ4wHLFe0yghb62GXJfUI5ISv8tsq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDOud6eFl5dwS8Oq6gCrcAyjJeuP3wImDRfvsTCMpohJa52hX4bThh83ZhHsD3Zu7OSm3kXa4eEPt2U7XhGIut8V%2B%2B3nq5ny3erZqH7sm4BPFjrgBgkiipM9b4t1HtO5vaDIE2xFxiabe8%2Fl4PAdv7qyTFMCc%2BS53mjVOIbzus7U9guFSQyc%2FHH0OtdX3wKtcou%2BAY5f4UkOFgZ%2BcUx8v1kngrCWMSg6yOP26ExTkWGqVv8ObulY4nn8GBVUbi7EE6v3FzbKzHxo7mtqC%2BdlA1dRsvUSqd%2B3lWrF39fiGf3aNJch0YhWZd7ufjp%2Bpt%2FBDMIBt%2FPuyt6wrp8CMaCXB20GKHlhNWJZtUm5c5l%2FvC9xDOhFbbg%2FP6KWyLuNmnhwf0mFwjIP3BDqQykTH7hStmCi1BIuAhvZHFP2xvg66gSO6d60M2yfBlOUtp5Wi2pyMd%2FhzYlrYIhme5zYFDRhpJa7yDfWF695wiUPyL1bwhPJk7n%2BbIidUSN0ArysTNiMcgBu0oJCmpMcLUhSrpQVPqg2HzGI6JKl9SYwOWgdLOtzI8mkzIr2sHdfeIWxJ9Ec6NKuYE1KkEToKo1fcf2oURMHdFzanp%2BJjYnzMCuW4yAgsVf%2Bzvmt%2FGk5XrQTgok%2BrCCveXkDaE%2FFiiv2jMJWl79QGOqUByknEOHXiyBFKhgpkb3ABDME8ZyfaYqpTDIy3CQdjKaQVOfRmJpNs%2F3fK18XcDNaVtb3cjGYS4Y%2F%2BhswusXkiO4mAQ5GPorbXnFdJe53ZAf9hh8GmNuj6W3dhbyn9ceFQ076tjFsZ8mnYg%2BHoHkasFTqXD9pHrg66qWIbsrLS05wsfSw9pphB3bEFmo0Y%2BWRrQNVW7yJXCQhPVjFjH9XU57mzwiHi&X-Amz-Signature=8f567995e90a6f0149e5ed3c3e8039ce6329804fb3b09bd2dea953b1994df7b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







