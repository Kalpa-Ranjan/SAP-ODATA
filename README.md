



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DVFZQZJ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T062527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1XDnQUyePHT7GOjmJ0PzdnS3uMMQ7DGDAfiA2Mut6lAiEAyKXyCiZbiNn6c4tpNeDHAx4PPAqnNanzW1Zx%2BWkLRTIqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQ216jL%2B8NQxRIDvCrcA5vUeMCWu2dCKzqRhTw3ZB38SZq7%2FnZa%2BOkAZx9i9xmxkR9VRT9kYgSV252WKEoD2UMvfBaRJuqtMJrJ8UXCpEHQywL3q1OWClCcHJlP9jkvief6LXLe2DCUQCtSareqThxLG%2FOW49TqUOZ1DZ2GARtWy%2FAa9hGUJ5GVlzLS1yfPD2j6PFkHRm8HhwD%2BCW6upkRMFrSjvCaD9zl4fs89dejBbKVtnbkHyDrKTpX8rjwkHx4e2BZbxJSifaCt0Ee3vfjiwg0fVfrJA0jtdbDZ6jxC4Lhrkt%2B8WQS4wrXHt%2FAkDu1GM3Qg0%2FcKtCduWg0dJR0X0DCWDSqSF%2FWpAGNn8SCrByOXW5ia6e2U52ifXpSsasoH6cnf3s9uNVnsBfZTj9tObxMbBHVbTIS2VuVsOu1l7kcqJBZhQE0zgsS6hyyXy3wz9RK69NbhbGa6Fw5iIxOZLN629WkiO38q5Riz64lLYDEPuA7XAK91bXrxdTsLvRDbBIHkWc1aIvBo8NWyfvKsBSbhpXrHsp8nnc%2BbwlINmwjCB3Zw0w9u9ukZWFuM1DjI7fZdwILDi8nJEIa%2FnEu8mbgCi5jpjJS7uyg1oXclQjjApf4DGYqtRIe%2F2ur0NxZokcG9G%2F3FWMtxMM7LnskGOqUBZ9jOizK%2F603WzqJ5JViic8m6nuMY6%2Bd8PXMl98fGmpa4xK%2FzPE9fKqtjZ8iCliGT0f3kGAOxVTyO40dcA0IiXnfAM4zzT84CbZ3tJQArmFVIXlzgIDxdL6CWyJ%2FTIfEhDGRV0GL7TT0z%2FRsBVBsPl1O6kjmS9zhlecDBASTr6iYdV%2FhdueZ8VzTwDpHAk4bqEss0PvCePJ43E2IlvnCD%2BzLe2Anx&X-Amz-Signature=6f329c6aa2ecb0c4b8a283576b579075b2bb6e2e0f36f636b1c8da406dff264c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DVFZQZJ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T062527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1XDnQUyePHT7GOjmJ0PzdnS3uMMQ7DGDAfiA2Mut6lAiEAyKXyCiZbiNn6c4tpNeDHAx4PPAqnNanzW1Zx%2BWkLRTIqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQ216jL%2B8NQxRIDvCrcA5vUeMCWu2dCKzqRhTw3ZB38SZq7%2FnZa%2BOkAZx9i9xmxkR9VRT9kYgSV252WKEoD2UMvfBaRJuqtMJrJ8UXCpEHQywL3q1OWClCcHJlP9jkvief6LXLe2DCUQCtSareqThxLG%2FOW49TqUOZ1DZ2GARtWy%2FAa9hGUJ5GVlzLS1yfPD2j6PFkHRm8HhwD%2BCW6upkRMFrSjvCaD9zl4fs89dejBbKVtnbkHyDrKTpX8rjwkHx4e2BZbxJSifaCt0Ee3vfjiwg0fVfrJA0jtdbDZ6jxC4Lhrkt%2B8WQS4wrXHt%2FAkDu1GM3Qg0%2FcKtCduWg0dJR0X0DCWDSqSF%2FWpAGNn8SCrByOXW5ia6e2U52ifXpSsasoH6cnf3s9uNVnsBfZTj9tObxMbBHVbTIS2VuVsOu1l7kcqJBZhQE0zgsS6hyyXy3wz9RK69NbhbGa6Fw5iIxOZLN629WkiO38q5Riz64lLYDEPuA7XAK91bXrxdTsLvRDbBIHkWc1aIvBo8NWyfvKsBSbhpXrHsp8nnc%2BbwlINmwjCB3Zw0w9u9ukZWFuM1DjI7fZdwILDi8nJEIa%2FnEu8mbgCi5jpjJS7uyg1oXclQjjApf4DGYqtRIe%2F2ur0NxZokcG9G%2F3FWMtxMM7LnskGOqUBZ9jOizK%2F603WzqJ5JViic8m6nuMY6%2Bd8PXMl98fGmpa4xK%2FzPE9fKqtjZ8iCliGT0f3kGAOxVTyO40dcA0IiXnfAM4zzT84CbZ3tJQArmFVIXlzgIDxdL6CWyJ%2FTIfEhDGRV0GL7TT0z%2FRsBVBsPl1O6kjmS9zhlecDBASTr6iYdV%2FhdueZ8VzTwDpHAk4bqEss0PvCePJ43E2IlvnCD%2BzLe2Anx&X-Amz-Signature=6f69c652787f024410819563b4290dbbd8c840fbb5e129bb99109f4bb9b77ea9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







