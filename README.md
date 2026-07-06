



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627GAN37G%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T024043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUDEfcgJvBCrV7E8IREJfPsucyGSk%2FkyDLYSX0EKPjZQIgDovJJAGjecxMSF%2B0Q0Nxbbv8NIUcx8gkugNUYaL0EJgq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDFh%2BXKTI1CCLqJZW4yrcA2BURa7hVD5dsb6caLlQT51pyPSFMUBztL9kqOcGinPw843ISDce0SS1OOYbfY1SyXUlRYLL0emkTIkDQpbH%2Fk%2FktRFO1L0SIyH%2FubJ67hZUEQ2zxsWmdgmbPA1R495a0G%2FYycE%2F6FCTjZnAPeMO4US0%2BbgXxFYUJwHZZso9f3jSWU24V31yPoMVxDVoxICwaw7rAYJTgo7PJpaU0Mpkg4V%2FtyxJ%2F6b2scyZgscsFck5q4nz%2FQ4bf2Keri7C%2B81feBCSlBUMz4bK9C3%2Bjkg1WgoSF3zjagnY1nmgUFO2bUOOWa7%2Bi2ihgg2nBotCpq%2FukSIn2YijO3zPgzcAxjXq5RcDjdjjcCtS5orc7iISh0L49vodixLfeJueg5fWZDyIlIcSlmSlgoSh9ogOzwIoksbUon1lr45D%2Fb3rpNu%2BXcyf1Katok8a9KgRejXlhCYp7jx3qOx2GDm%2B%2FTk23KrLocyIBzUIhbHfsGnM45CMdxClVb6zMTGNnCAJKIfK2PAntS31I6y6tbsuFSt1SmBlceCRwaC9fl5h%2BYUQ2PC1FNI1RehNetXBcRD7WqO01nD6DqufygdZMqrCeeZNOvdIUMdUVzOOLOKzTbnJWmeXp2hZel40sTfV5a2Wfc2DML6QrNIGOqUBtjcELVp4%2FyusF6Aq%2BgdQghoMWPxZ9Wi5325H1bRlQlbsvlmabVA70arLmIPZ7FQYfh1OC1oWEzLi5DLYhH%2BFZeBXxEJB4yE2xZo%2BNkXx7ckYHCfJw857OQUL4lnwQFOQ4RZhxr20bJCobVHZRAqtv7lwzpU4E9q64iR2AmFtklWK9zDFnz4ISiOCx0Zovf0QcB%2B1T0An9ohVBPGVwTXLicbdlwL1&X-Amz-Signature=2ebdad2ab4989be1f566700753a1df38144e8d405d3f51116c8ab156d6492699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627GAN37G%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T024043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUDEfcgJvBCrV7E8IREJfPsucyGSk%2FkyDLYSX0EKPjZQIgDovJJAGjecxMSF%2B0Q0Nxbbv8NIUcx8gkugNUYaL0EJgq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDFh%2BXKTI1CCLqJZW4yrcA2BURa7hVD5dsb6caLlQT51pyPSFMUBztL9kqOcGinPw843ISDce0SS1OOYbfY1SyXUlRYLL0emkTIkDQpbH%2Fk%2FktRFO1L0SIyH%2FubJ67hZUEQ2zxsWmdgmbPA1R495a0G%2FYycE%2F6FCTjZnAPeMO4US0%2BbgXxFYUJwHZZso9f3jSWU24V31yPoMVxDVoxICwaw7rAYJTgo7PJpaU0Mpkg4V%2FtyxJ%2F6b2scyZgscsFck5q4nz%2FQ4bf2Keri7C%2B81feBCSlBUMz4bK9C3%2Bjkg1WgoSF3zjagnY1nmgUFO2bUOOWa7%2Bi2ihgg2nBotCpq%2FukSIn2YijO3zPgzcAxjXq5RcDjdjjcCtS5orc7iISh0L49vodixLfeJueg5fWZDyIlIcSlmSlgoSh9ogOzwIoksbUon1lr45D%2Fb3rpNu%2BXcyf1Katok8a9KgRejXlhCYp7jx3qOx2GDm%2B%2FTk23KrLocyIBzUIhbHfsGnM45CMdxClVb6zMTGNnCAJKIfK2PAntS31I6y6tbsuFSt1SmBlceCRwaC9fl5h%2BYUQ2PC1FNI1RehNetXBcRD7WqO01nD6DqufygdZMqrCeeZNOvdIUMdUVzOOLOKzTbnJWmeXp2hZel40sTfV5a2Wfc2DML6QrNIGOqUBtjcELVp4%2FyusF6Aq%2BgdQghoMWPxZ9Wi5325H1bRlQlbsvlmabVA70arLmIPZ7FQYfh1OC1oWEzLi5DLYhH%2BFZeBXxEJB4yE2xZo%2BNkXx7ckYHCfJw857OQUL4lnwQFOQ4RZhxr20bJCobVHZRAqtv7lwzpU4E9q64iR2AmFtklWK9zDFnz4ISiOCx0Zovf0QcB%2B1T0An9ohVBPGVwTXLicbdlwL1&X-Amz-Signature=89ec345e05871a0ee77f69321d852614662768ecd306adf35ef8f17a9d300782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







