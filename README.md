



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GSECIAG%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T065824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKevb37uLqbP%2FpdkLOnY5HgeiQhPkJKBM7zDXK0IlcCAiEAl1eqzLmDXBEL0aRnEO2uerOR0JsLyNzIda7YTyen7dsqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcioX1Ei9C4gOsVvircA%2BY2wlQmftbzWwNAkTtsGPN%2FU0jlLjMVtAcCLOzPviWFPSDfwFTRTWbHk4yLztqoDvbFJVmOb0y53JpjwQY7aV3OYrM519h1ErGavac%2Bkb%2F5I%2BX1wIYNP3PPSRRu9IlbgknMT%2B0xYJeflaWL9Ufst%2FWLRj19Z3QzMYFYJPKfYcylHefwqTnPnRkcagKURuZXpUPgPs3uxt7ucKG%2BB9p6CQ3YKD8uXM8B3Lt3I8uKycChHMIEuAwiQGEBVCK2s%2Ffzhzuc3%2FCWlFH1BVvHwTpCaXq0g3tXJ66tyj1baZrE%2FUGZgcNzABS2FXnvTgbxIyIBWmw%2Fue5FrRP6Dbhra7voaTHFhLg6VOQpRmnmMng3bbbnv4C2oyqkZ17YA%2B7Sk6PwZezsKLoUVZWQrvHJHajsG%2FcSz8m%2FlXkwHegZoIQPgBbyqcOSPLsg9FtnkKEAGG0eiEPKdrwX%2B5sHfDPm9TFW3A683X60555SfYsd%2F2iTeX%2F3nMRMf5u9jCdhTaZgufl%2BG1oh76NoF4AkkjykWaG%2F2%2Bls7QIfaeIFYCQT44rsuYHaVFdHp8AQV3HmajNO95R%2By%2BxCct4e1MF3BYqpXA1elGuaZokFuzVGoQxEfwABzYDt7Uvtq1NVj6aTiYxYMOfpiM4GOqUB0%2FqPqLTWXBRQ8VuRpOlXYWQIfXIrGSWgsb6JU3GQ8%2B170ZIglULjU741uiMm6ETVk6Tu853NVQ8AupYUHBzDf6P%2FWODLqL9Dor%2FR8p9C0f2FRnHqORkJn5VHaVJo%2BksPgJMsJj6PC5HyGV0%2BGLpMN%2BwDkzX6gfiw0EYDVP5OdIvbynMgKtioyI7aEmfIq%2B83bWqWYY7MFoYJHc19LIQljDhzHVJ3&X-Amz-Signature=aa88164a513c624f8af1f0b22199abdd32a1cd1621070be9b68b32c907f42855&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GSECIAG%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T065824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKevb37uLqbP%2FpdkLOnY5HgeiQhPkJKBM7zDXK0IlcCAiEAl1eqzLmDXBEL0aRnEO2uerOR0JsLyNzIda7YTyen7dsqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcioX1Ei9C4gOsVvircA%2BY2wlQmftbzWwNAkTtsGPN%2FU0jlLjMVtAcCLOzPviWFPSDfwFTRTWbHk4yLztqoDvbFJVmOb0y53JpjwQY7aV3OYrM519h1ErGavac%2Bkb%2F5I%2BX1wIYNP3PPSRRu9IlbgknMT%2B0xYJeflaWL9Ufst%2FWLRj19Z3QzMYFYJPKfYcylHefwqTnPnRkcagKURuZXpUPgPs3uxt7ucKG%2BB9p6CQ3YKD8uXM8B3Lt3I8uKycChHMIEuAwiQGEBVCK2s%2Ffzhzuc3%2FCWlFH1BVvHwTpCaXq0g3tXJ66tyj1baZrE%2FUGZgcNzABS2FXnvTgbxIyIBWmw%2Fue5FrRP6Dbhra7voaTHFhLg6VOQpRmnmMng3bbbnv4C2oyqkZ17YA%2B7Sk6PwZezsKLoUVZWQrvHJHajsG%2FcSz8m%2FlXkwHegZoIQPgBbyqcOSPLsg9FtnkKEAGG0eiEPKdrwX%2B5sHfDPm9TFW3A683X60555SfYsd%2F2iTeX%2F3nMRMf5u9jCdhTaZgufl%2BG1oh76NoF4AkkjykWaG%2F2%2Bls7QIfaeIFYCQT44rsuYHaVFdHp8AQV3HmajNO95R%2By%2BxCct4e1MF3BYqpXA1elGuaZokFuzVGoQxEfwABzYDt7Uvtq1NVj6aTiYxYMOfpiM4GOqUB0%2FqPqLTWXBRQ8VuRpOlXYWQIfXIrGSWgsb6JU3GQ8%2B170ZIglULjU741uiMm6ETVk6Tu853NVQ8AupYUHBzDf6P%2FWODLqL9Dor%2FR8p9C0f2FRnHqORkJn5VHaVJo%2BksPgJMsJj6PC5HyGV0%2BGLpMN%2BwDkzX6gfiw0EYDVP5OdIvbynMgKtioyI7aEmfIq%2B83bWqWYY7MFoYJHc19LIQljDhzHVJ3&X-Amz-Signature=abe55d6803add6636d3d63fbaa191bcc91296c5c63a10aa1e7e959dfc9c89395&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







