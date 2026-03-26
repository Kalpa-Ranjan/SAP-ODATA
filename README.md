



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GYVIX7X%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T070156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBRRTh6gz1oKEhjMNTTgMZB9%2Bh3zSxxtls5ZKKkd%2BRfAIhANYVKWOJHx4%2FCXPEDqkf%2F9SOyKEzZsAIcj7lsDtXXp%2F5KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B7cO6x053LaAd6roq3ANhtGWGMUWJmlSZ%2FBxf4CfIOU4tuWGhg5CsgSHV7NVSWwmheK0JL21gNbixuHU3%2FFFIWNuRhtvmPojJglbrZSy%2F%2Fidt1fUElhrOfMX%2FASxTMYfM6Ne7lgU%2BvIdAkzUeO5qg4e%2BHrh4W0iiwT4OcuEJjUyZrHBUPjR%2FZZWb57GtjogEJ2aTGBAuWdfJ6JdeQmoZRuA5R8oNyI2HvSn8wz7mbMBaB6WObJmeT4Q8Gu6KGnq61IZy%2BtStX%2BNJY5T2QXbJN2FQnIBczdZZthuJBQULa3MOtl%2Bwf6IslQCrEWuAmF61Bey6gT8wCGP%2F%2FeULprylTIBhKhzrXYfQnCwtCuMgw3%2Bh2zQARdMwDaMpOnZ4kY7A45F1Bki2%2B%2FOUxUtacvb%2BfkfGm5NlQk%2B6q411Gi%2BuCIXpcP1CzUZ4Dnnz6UVnzuCe%2Fp%2FNeLbKE%2FTlWHjpQduw0eop2mkiO6TE5728w9pRmkVd9pHVMJYCEwS4%2BWQNQlJEmDyy2xU4pZdDotHt2aoH3s%2Bztdf6fao7ZsfbS55jmNWd2n5dgoe0Z7S8aE%2Fu1K755OjAr92T84cCpQIcB2%2FtspxwV2ZaoeWYBaUTzfgyl1q3onfhw2nyw21UUlhi3DJ61ZDP8Upvyo8FqnTCAsZPOBjqkAZIEsRX7s01whcsXAXUGfkNPcclIGi3MEJiXQ3h3nSyEO4hoU1uMlT12IA20wNgO%2F5MxZj0nbG5Lgu4pOOYUI2rvduOjRnGyzLWkeSVdUUbaiTjSGf23ypwDhPrebVGaTB5%2FA21YCQvUaITxQyVjmaw495Tpkulnw3m%2BSDNr3ofDar7nbb0FotRVdvCuwZ9uZ%2FdfOvO0JlsVJuXeXiFKMBQ2niwP&X-Amz-Signature=85ce27e5a9cb33f24b24f9403b093779c04257b84e7e9af71b742a23270dbd39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GYVIX7X%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T070157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBRRTh6gz1oKEhjMNTTgMZB9%2Bh3zSxxtls5ZKKkd%2BRfAIhANYVKWOJHx4%2FCXPEDqkf%2F9SOyKEzZsAIcj7lsDtXXp%2F5KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2B7cO6x053LaAd6roq3ANhtGWGMUWJmlSZ%2FBxf4CfIOU4tuWGhg5CsgSHV7NVSWwmheK0JL21gNbixuHU3%2FFFIWNuRhtvmPojJglbrZSy%2F%2Fidt1fUElhrOfMX%2FASxTMYfM6Ne7lgU%2BvIdAkzUeO5qg4e%2BHrh4W0iiwT4OcuEJjUyZrHBUPjR%2FZZWb57GtjogEJ2aTGBAuWdfJ6JdeQmoZRuA5R8oNyI2HvSn8wz7mbMBaB6WObJmeT4Q8Gu6KGnq61IZy%2BtStX%2BNJY5T2QXbJN2FQnIBczdZZthuJBQULa3MOtl%2Bwf6IslQCrEWuAmF61Bey6gT8wCGP%2F%2FeULprylTIBhKhzrXYfQnCwtCuMgw3%2Bh2zQARdMwDaMpOnZ4kY7A45F1Bki2%2B%2FOUxUtacvb%2BfkfGm5NlQk%2B6q411Gi%2BuCIXpcP1CzUZ4Dnnz6UVnzuCe%2Fp%2FNeLbKE%2FTlWHjpQduw0eop2mkiO6TE5728w9pRmkVd9pHVMJYCEwS4%2BWQNQlJEmDyy2xU4pZdDotHt2aoH3s%2Bztdf6fao7ZsfbS55jmNWd2n5dgoe0Z7S8aE%2Fu1K755OjAr92T84cCpQIcB2%2FtspxwV2ZaoeWYBaUTzfgyl1q3onfhw2nyw21UUlhi3DJ61ZDP8Upvyo8FqnTCAsZPOBjqkAZIEsRX7s01whcsXAXUGfkNPcclIGi3MEJiXQ3h3nSyEO4hoU1uMlT12IA20wNgO%2F5MxZj0nbG5Lgu4pOOYUI2rvduOjRnGyzLWkeSVdUUbaiTjSGf23ypwDhPrebVGaTB5%2FA21YCQvUaITxQyVjmaw495Tpkulnw3m%2BSDNr3ofDar7nbb0FotRVdvCuwZ9uZ%2FdfOvO0JlsVJuXeXiFKMBQ2niwP&X-Amz-Signature=603a55456042ad2a4889ccb6112df18d314d40e260d5c401812e0b442dd49528&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







