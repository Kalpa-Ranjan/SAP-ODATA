



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KMUMRHI%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T063608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICS2kB9juilnqeSB3l4NzV%2BXWQWJa1wZGY2a84blIvDZAiEAmtpmEdtG9sviKOSHrW0YLwLOj7%2B%2BLJY74b33XEqKxV0q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDIFvCg801iRDoJcLmSrcA0pi6CThKkKEo5RUwYhYXYOSbWkWLjqp5LUwANLcoNy7aL6AUQpkJj%2BWBoapJR4k0x9F61IxcKtuCXYJAvCJdmOhbhk7oaenhRHtwZ5R0tYpaGCx82%2F8d%2F4LOdOqHrncTB9eYa%2BOrymauztUAy1eMBHDs62Ny%2Fxcakazi20qBtU4S0U0tbwzmN2E3NuC3Uvgio8Q6nc1XmIM9kScdyCIs4kn0j9djsaVngDoOU6LyVTcARnxm3pPwzuINj18xnDS6ZinNiWyiBfVWZApASRqfMP5fHXUXqB8dP%2FCOJwGqJQHQXItC7yPDnj6f3dThH6RIcgsCENCkx32tIoI74a%2FZfakIzqZf81r4vgvY%2BS8cw74fWhLSGpOI%2FtYHaMlUgWpv99yvKU%2FIn3fHScvojOBxU67eDcAOSIaOsJHyIriPKu9O9tHo1apXVg3vTdeBltjyMcc0pwnSuug7RmfEWYxdD0nVhZGNTXw%2FNr7jFHXdxvGgYwa%2BICNLcO3b8rlMcSUfwhp5wOd%2Bs9Je2KCBQeoOlhz%2Blo61gRCVtz2%2FDyb9F8S76og%2FQZCa4XUCeXqsVhcAu0FLOqXpzQTYm4YyMkOJTb3Ce%2FhLDTgDbh6jDrJdypDmkNC9u%2FAbowBhMtsMNuum8wGOqUBADGIkMRy7u41Ty%2BJIZZA8ZwZg%2FJgd8p4hHJi%2FqWk%2FiRMa1Zb%2BeGDk7zG8BSw5OjHYS6dcVLY%2BwZTb6%2Bz02SoAsEWtWcbq1etsza8K6qGEPV5AD%2FKRtGYqMR%2BK5UCAtFkINQgwnNFeI2BEDqKgKZUfUDkfmn735DGLqen1tML9efwcP3TIrEO9C4U8wPJMQjSJs6kNB8dsM0VJpHztIQbk%2F9v5iRq&X-Amz-Signature=13a2a5beb053d4a6245466923a1fd01525c56168c2104532cbfc6cddb34e3116&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KMUMRHI%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T063608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICS2kB9juilnqeSB3l4NzV%2BXWQWJa1wZGY2a84blIvDZAiEAmtpmEdtG9sviKOSHrW0YLwLOj7%2B%2BLJY74b33XEqKxV0q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDIFvCg801iRDoJcLmSrcA0pi6CThKkKEo5RUwYhYXYOSbWkWLjqp5LUwANLcoNy7aL6AUQpkJj%2BWBoapJR4k0x9F61IxcKtuCXYJAvCJdmOhbhk7oaenhRHtwZ5R0tYpaGCx82%2F8d%2F4LOdOqHrncTB9eYa%2BOrymauztUAy1eMBHDs62Ny%2Fxcakazi20qBtU4S0U0tbwzmN2E3NuC3Uvgio8Q6nc1XmIM9kScdyCIs4kn0j9djsaVngDoOU6LyVTcARnxm3pPwzuINj18xnDS6ZinNiWyiBfVWZApASRqfMP5fHXUXqB8dP%2FCOJwGqJQHQXItC7yPDnj6f3dThH6RIcgsCENCkx32tIoI74a%2FZfakIzqZf81r4vgvY%2BS8cw74fWhLSGpOI%2FtYHaMlUgWpv99yvKU%2FIn3fHScvojOBxU67eDcAOSIaOsJHyIriPKu9O9tHo1apXVg3vTdeBltjyMcc0pwnSuug7RmfEWYxdD0nVhZGNTXw%2FNr7jFHXdxvGgYwa%2BICNLcO3b8rlMcSUfwhp5wOd%2Bs9Je2KCBQeoOlhz%2Blo61gRCVtz2%2FDyb9F8S76og%2FQZCa4XUCeXqsVhcAu0FLOqXpzQTYm4YyMkOJTb3Ce%2FhLDTgDbh6jDrJdypDmkNC9u%2FAbowBhMtsMNuum8wGOqUBADGIkMRy7u41Ty%2BJIZZA8ZwZg%2FJgd8p4hHJi%2FqWk%2FiRMa1Zb%2BeGDk7zG8BSw5OjHYS6dcVLY%2BwZTb6%2Bz02SoAsEWtWcbq1etsza8K6qGEPV5AD%2FKRtGYqMR%2BK5UCAtFkINQgwnNFeI2BEDqKgKZUfUDkfmn735DGLqen1tML9efwcP3TIrEO9C4U8wPJMQjSJs6kNB8dsM0VJpHztIQbk%2F9v5iRq&X-Amz-Signature=76b999a4c92706114ac3a8a5deaaa2332b965667ea0aa88190e54395c87859a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







