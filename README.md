



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYKZVSO2%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T011734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaWk2%2Byv5xUVTg4JcxnIQXifK8YLqXt7VKym8cS%2Btg1wIhAM4BIBrXBiUh7saJyXXl0RTke2QI64UjE1M9l6f3LbOWKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxi2TU2U4vsjPZBeTMq3AP1CHlHcyguGcy2eHO4ygQUkMTCtM20IqqtpLyaUkfx3ZvUmLxjJj%2BN5ZYS2FEOMbVafhuA3ma9y%2BM%2Fi5bUWKMPI8qcAJLJ7FdIDNTRmcFzp%2BxNhQcD%2FdPqRQfEEo%2Bq14CdrR7a%2FK63B%2FqYbrNzlAuLjtb7LK%2BCFItw9UZ1O8t%2B5r%2FTsCP4vtmEAqYFiYzZlAEa%2FDveM2ndUm%2BsJCjGU4ym6HZ0RF0B9%2Fnj%2F8qAjNQS%2F3sR7UY3bk4wq%2FopA3WVewIxxo%2BxpmABjZVBY04MAsKhiysdUPgVaOVhAh%2BxSOMqkDeWj5PzqHc%2B0%2B70UyD9bgLFNmLAK8hteBCv25lL5O6dMHrYJurfZgYVi8AJ7olG14XJ799m5BSRRI2j39iwtp7iNdkwIQtsowipxIfdIwB0juE8FjI8FYrwBxP5Ygo908LGt0rXp1pVHiE4W3Lg0%2BiSdh%2BFxVqgKGlHdZCRt%2FXYxw4XLczqjgehgRTwmRyeVnU9dIpqshZ7XdxTLCqP4C3cth4nxisdfgo2yzUGBgZ0cHZMHhQNlyzC4JJpnpVrNLwWMginUOiP%2FTs604I3bNN6RM%2FMhMYau%2BqRlRN431OI4UjEOQ7kGzg8fDKKRfa2g4zga28CZ0Z9nV%2FwdTD2reTTBjqkAZX%2Bnv6YCHc8lZH7tfCXD6YC7tGLg1FfG%2F%2BLXFhKIdLBc7sGf1AdcokPOni0rlHbWSnmBtiQ3Rfy9iAPdTaUTh4WcY%2FfGqtxpg5GVQ55dbCqQm32Z5bPpygRYPgRY1AuKfKoXh%2BElhfi6mchfUFosCoHPJurcPgRvTlFSy%2FMeXqQEh9oobSMiVaN%2FykNOfqVKCPW65I1TGUbLMuUl7ge24fidvgV&X-Amz-Signature=8aaa91194ec687ee6a32336a58e09a401ad1b9bf7bb6db85ec7079fd5c80c852&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYKZVSO2%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T011734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaWk2%2Byv5xUVTg4JcxnIQXifK8YLqXt7VKym8cS%2Btg1wIhAM4BIBrXBiUh7saJyXXl0RTke2QI64UjE1M9l6f3LbOWKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxi2TU2U4vsjPZBeTMq3AP1CHlHcyguGcy2eHO4ygQUkMTCtM20IqqtpLyaUkfx3ZvUmLxjJj%2BN5ZYS2FEOMbVafhuA3ma9y%2BM%2Fi5bUWKMPI8qcAJLJ7FdIDNTRmcFzp%2BxNhQcD%2FdPqRQfEEo%2Bq14CdrR7a%2FK63B%2FqYbrNzlAuLjtb7LK%2BCFItw9UZ1O8t%2B5r%2FTsCP4vtmEAqYFiYzZlAEa%2FDveM2ndUm%2BsJCjGU4ym6HZ0RF0B9%2Fnj%2F8qAjNQS%2F3sR7UY3bk4wq%2FopA3WVewIxxo%2BxpmABjZVBY04MAsKhiysdUPgVaOVhAh%2BxSOMqkDeWj5PzqHc%2B0%2B70UyD9bgLFNmLAK8hteBCv25lL5O6dMHrYJurfZgYVi8AJ7olG14XJ799m5BSRRI2j39iwtp7iNdkwIQtsowipxIfdIwB0juE8FjI8FYrwBxP5Ygo908LGt0rXp1pVHiE4W3Lg0%2BiSdh%2BFxVqgKGlHdZCRt%2FXYxw4XLczqjgehgRTwmRyeVnU9dIpqshZ7XdxTLCqP4C3cth4nxisdfgo2yzUGBgZ0cHZMHhQNlyzC4JJpnpVrNLwWMginUOiP%2FTs604I3bNN6RM%2FMhMYau%2BqRlRN431OI4UjEOQ7kGzg8fDKKRfa2g4zga28CZ0Z9nV%2FwdTD2reTTBjqkAZX%2Bnv6YCHc8lZH7tfCXD6YC7tGLg1FfG%2F%2BLXFhKIdLBc7sGf1AdcokPOni0rlHbWSnmBtiQ3Rfy9iAPdTaUTh4WcY%2FfGqtxpg5GVQ55dbCqQm32Z5bPpygRYPgRY1AuKfKoXh%2BElhfi6mchfUFosCoHPJurcPgRvTlFSy%2FMeXqQEh9oobSMiVaN%2FykNOfqVKCPW65I1TGUbLMuUl7ge24fidvgV&X-Amz-Signature=30db5620d4343815f6ef16ca477e42d7c57c55c3f02eb4a9d5e96c250d89074d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







