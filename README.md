



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5UNSL24%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T062625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbkq8U4bnDQgfDEDUUy6rPRHHNmKn3%2BlCXtxYd55DtIQIhAOkWXszM5mwQ2UIPkUXsXHFfRMewUv%2BsNeiCFMrSTnKCKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk8VN6BTFq83VDcNkq3APCXImwOMe7YJS4UzxbXfdHvpzd4MHGyRemE2PTnpXCDPZpLuJafE1ahXlQbZLSuH%2Ba%2BmJPXxlJF%2BnikIwB%2BJxZz8OScqZ9xPLQRUkRH%2FxG0jE94fGo%2FtFlH9DE%2FnzIT3%2BehNA%2BUXQqkaBEAc0SXJFIGUyLZma089H982KMkEKCmNH9tgWV4Os%2FVQ%2FlxOzoJPZXxVCqgLQDcbOOcKUZzCC4rSO2lkeOFJG9vOrfXFMR59cdUKIKwwYNSsJKq4pyFSfYU%2BigQocp5ceTeVac75hUHGXgfJb7WVjuVfC1utQiTKmSuMvzsQi9oiU%2BBUopVISCo9mCfU0LmqH9QXugLQri9o7DkeEglZM%2BDoIpmNhxxdpAwV4lTLtiNJ6bqYwWjg3PoL5ZdQVpJy22m5KC2CKODbJ1WpbllaAtXMTQH5eUK0u3iF7TkCMculbGCdGFwuNOgKxgNfBQHHjAZ5RapbnQXmHmPs7IscPPjW420vAR8w%2FLcqK%2FEfLmg1Lu73z8gGgtgSzGh%2BI7MTmAjcdANrZTC2JiSLd977QtK7cZ59t9XgjFd8wZO%2FhBfcS91I%2F4Xa6T%2FhMB16U0nOo4v1R4UnHa4OjylUTPBfGpc5BM2zkQCSOt8XLYjJ6Ru6uBuzD6s83KBjqkAfsDTw2aeBhltGmRhmaZnEAlCBI4gK4xQ%2BSi39q0Wo8rXgrngtBUzo6MCbz%2BdXIN3yCOTOM%2F127ODtgoCLQiyQOA5%2BwSkkHhc626LNu6Q0qj3lSD5moUvEwjnlH64v901MDf7YuyyvQhS5drbGCCt%2B9Re6wjenqqorRjwmDW5KNNfvJn6%2FbPrsbrc7FxWVeVO4GwBP3SJ9ulLQRwXKDSgJyiXJro&X-Amz-Signature=92da3c828b99e3397fa70345fb73be00b03a95b393f778a7583639484fd7b54a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5UNSL24%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T062625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbkq8U4bnDQgfDEDUUy6rPRHHNmKn3%2BlCXtxYd55DtIQIhAOkWXszM5mwQ2UIPkUXsXHFfRMewUv%2BsNeiCFMrSTnKCKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk8VN6BTFq83VDcNkq3APCXImwOMe7YJS4UzxbXfdHvpzd4MHGyRemE2PTnpXCDPZpLuJafE1ahXlQbZLSuH%2Ba%2BmJPXxlJF%2BnikIwB%2BJxZz8OScqZ9xPLQRUkRH%2FxG0jE94fGo%2FtFlH9DE%2FnzIT3%2BehNA%2BUXQqkaBEAc0SXJFIGUyLZma089H982KMkEKCmNH9tgWV4Os%2FVQ%2FlxOzoJPZXxVCqgLQDcbOOcKUZzCC4rSO2lkeOFJG9vOrfXFMR59cdUKIKwwYNSsJKq4pyFSfYU%2BigQocp5ceTeVac75hUHGXgfJb7WVjuVfC1utQiTKmSuMvzsQi9oiU%2BBUopVISCo9mCfU0LmqH9QXugLQri9o7DkeEglZM%2BDoIpmNhxxdpAwV4lTLtiNJ6bqYwWjg3PoL5ZdQVpJy22m5KC2CKODbJ1WpbllaAtXMTQH5eUK0u3iF7TkCMculbGCdGFwuNOgKxgNfBQHHjAZ5RapbnQXmHmPs7IscPPjW420vAR8w%2FLcqK%2FEfLmg1Lu73z8gGgtgSzGh%2BI7MTmAjcdANrZTC2JiSLd977QtK7cZ59t9XgjFd8wZO%2FhBfcS91I%2F4Xa6T%2FhMB16U0nOo4v1R4UnHa4OjylUTPBfGpc5BM2zkQCSOt8XLYjJ6Ru6uBuzD6s83KBjqkAfsDTw2aeBhltGmRhmaZnEAlCBI4gK4xQ%2BSi39q0Wo8rXgrngtBUzo6MCbz%2BdXIN3yCOTOM%2F127ODtgoCLQiyQOA5%2BwSkkHhc626LNu6Q0qj3lSD5moUvEwjnlH64v901MDf7YuyyvQhS5drbGCCt%2B9Re6wjenqqorRjwmDW5KNNfvJn6%2FbPrsbrc7FxWVeVO4GwBP3SJ9ulLQRwXKDSgJyiXJro&X-Amz-Signature=b556269d64ca7925fd1913883f1c003fafd83b2465aa3ed31f7a1a8a1877d80a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







