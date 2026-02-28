



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGZ3KRS%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T123541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdLOJM4cdL%2Bq2e0cABgK5e%2FDehIt0vRT3wGn5aTlPW5AiBrh0qHIsYx22b3%2FxIWrUr%2FC3zUHxhiUEU4I8pgtT7w9Cr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMUhwYkISwBekcZizMKtwD8%2Bv89br438fkQxMOPt04HdeSmxJdbqMhySJ5kOYz6KdVX9F3yJtr0v8g4ecZi53xORCpKy3Bcts3SVXUOxNlCNZ0MpvI%2FCFiNhIiNmFj%2BbLG8TlMj%2F0Tf67NvdYFRBsV8p%2BO%2Bp%2F0rFAo6VetcMXx2iP25rWZdXBpLP6s7Ye3wSVyoneDp2kamgj7KQeYNVXdsz%2F6svzWLtj6%2B0mgkH2zt6XIbrEzbn4t3Eiz8K17GwrCgBXSZEuabFcEF%2Bt5fZVEFz0n0wYt3nV2P2CRN74YlPq7cIX8QKjk%2FwHfjoNtcWDmwLaLimKe%2FXR4NvHueyWBRRSrXOrCdXQ%2BBlK5VPwkzE9S7Wdd9bqt4UWWMrPrLOGI9Wf6X7Ol1j6%2F1zqlbDyaBc%2FT6sAfO9ZQnSMMA9n22CPmkE7It1wpKsM%2BVlJj1cDMgPrljwaoi85djMMzffdwdWRW7vjjTkYDfkY6T%2B9MDabaTgclsv4jOV1YmUqhNrW4Q6qxtaQq9MuEj0VFqdnvGQ1e6Be3JHYWdjNhk%2FHIPN9saZmd6wpHU5xu%2BYtUyFSixSaSwU8PNSbjwAYioYBEK5qTTF0jUDABeT481C58p%2Ff5Zs5z7AeQfDgf8bjIvULZaHshSq3k1qapct4wvv%2BKzQY6pgGueXjZ%2BEbHIw8W%2F%2F1h6PTnoeeLg9InVWxQOJN6bdB8z7vxlQ6G%2FjuJYFX%2FCrrYGsL5NU4tE%2BHpcIeg0HG35iOBl3hLveLp5TJ8AWrdiOka7rZAsRRAnGxU9%2F%2Bmqz3mhZRORy%2Fj26iapRCwgesBjtGNmqYGQbjJ1Q%2FURtTufTGeOHOe7upgh9Z26UeHsXcEIp3GeAq9hj6UfTLNzQSPuWPWxxYPjQ7A&X-Amz-Signature=f0ce634b34288a1efbb7341a32a5aaa49203a087b2cb159b5481e6fabcb912a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGZ3KRS%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T123541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdLOJM4cdL%2Bq2e0cABgK5e%2FDehIt0vRT3wGn5aTlPW5AiBrh0qHIsYx22b3%2FxIWrUr%2FC3zUHxhiUEU4I8pgtT7w9Cr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMUhwYkISwBekcZizMKtwD8%2Bv89br438fkQxMOPt04HdeSmxJdbqMhySJ5kOYz6KdVX9F3yJtr0v8g4ecZi53xORCpKy3Bcts3SVXUOxNlCNZ0MpvI%2FCFiNhIiNmFj%2BbLG8TlMj%2F0Tf67NvdYFRBsV8p%2BO%2Bp%2F0rFAo6VetcMXx2iP25rWZdXBpLP6s7Ye3wSVyoneDp2kamgj7KQeYNVXdsz%2F6svzWLtj6%2B0mgkH2zt6XIbrEzbn4t3Eiz8K17GwrCgBXSZEuabFcEF%2Bt5fZVEFz0n0wYt3nV2P2CRN74YlPq7cIX8QKjk%2FwHfjoNtcWDmwLaLimKe%2FXR4NvHueyWBRRSrXOrCdXQ%2BBlK5VPwkzE9S7Wdd9bqt4UWWMrPrLOGI9Wf6X7Ol1j6%2F1zqlbDyaBc%2FT6sAfO9ZQnSMMA9n22CPmkE7It1wpKsM%2BVlJj1cDMgPrljwaoi85djMMzffdwdWRW7vjjTkYDfkY6T%2B9MDabaTgclsv4jOV1YmUqhNrW4Q6qxtaQq9MuEj0VFqdnvGQ1e6Be3JHYWdjNhk%2FHIPN9saZmd6wpHU5xu%2BYtUyFSixSaSwU8PNSbjwAYioYBEK5qTTF0jUDABeT481C58p%2Ff5Zs5z7AeQfDgf8bjIvULZaHshSq3k1qapct4wvv%2BKzQY6pgGueXjZ%2BEbHIw8W%2F%2F1h6PTnoeeLg9InVWxQOJN6bdB8z7vxlQ6G%2FjuJYFX%2FCrrYGsL5NU4tE%2BHpcIeg0HG35iOBl3hLveLp5TJ8AWrdiOka7rZAsRRAnGxU9%2F%2Bmqz3mhZRORy%2Fj26iapRCwgesBjtGNmqYGQbjJ1Q%2FURtTufTGeOHOe7upgh9Z26UeHsXcEIp3GeAq9hj6UfTLNzQSPuWPWxxYPjQ7A&X-Amz-Signature=168b8bde2cdc46307be7e23ee412d3f770949d556d413dee7a9f33aea97eeeb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







