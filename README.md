



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR2IOST%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T133832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQC2Rmjwba881tp%2ByGHCCvUGSjURTjDq1%2FrzJ6FDURQzegIhAII46vkibPUe%2BE5SDP2pj7DdDMkpKw1KGSKIfCZ8pkGcKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyyf4mzPeYlBDAUffsq3AOkHq3tSWGmqlPOI%2FTiCxEYLofq5zDr4Lh9H8Ux%2F7WA3z53dEmZaYUif%2BamNcSJZi2eFcZbzRTDhxwJkYoFDU4lKd1XBauyCh0ROz3TPjAIsMtMWgOQWXYn2HhqqZSa7VTJIel8ZvyWF1IW1V%2FQK0lcIj%2FRaXiG3wca35quv7%2FsogtULnKRBZMewczCNnfg4ckTIbctkYpd8p6Zl7i3RtfpCwsmg2Wvs85ExSMcYFGKCRZcdBpYeJFtjE0uEt4nHzzd%2BdzR2MaPqtQyeQZA7djg5b1WEle%2F%2BD%2Bgjnn7Sc9ijtZ5YcP7IqjEp5P1FfYWaVfBR2gUKzU%2Bl40%2FKzH7xmS%2Bxz%2BXzMMd6jX%2FOwKD%2F0Qw6dtQY3TnJGzW4Bm7k%2BFU70%2FTOajBQCpJjncUzEogVUgt4lHKO44R6xPuNLHa60D2Eu1LAYbB0y73w4LDByYKbrOfmJDKVgwd6Bgu7%2Bn8dEMJO%2F3D45YEG5ToR8FNMfKqmOz1SCYTCtRYf3pNZJmLr6WaGo0H2FygtDNSf6zfqqrPhLTqgfcacn%2BvpXv%2BCYBeGTsrSkIPoqDX0QJGrE207G49vtRz%2Bh2JyeToFwGytlfN3LvqA%2FYD0IsuIDK0iDq22HGyaeF8nONE1ni%2FTjDG5ILTBjqkAbfroyUoTI4H4veiXbkABS6ld%2BOmHN9%2FUt4pVsY6yzIbt5l3%2F3nz3kj8ooQht3WIyCzZs61vDHlPgBIonJTUc6GNc4EwxaIZtytGQPf%2FwTCUzR%2FuY57IhCoMlNCHzzUSnm6oESx25g0pwrHYwgi4r7bAkoCE2H%2BBBDomz6cQccuH121ILbEe1i55VLmu%2BgSCGpGPaoBm1WvM0XLw5PjhUHyO57pG&X-Amz-Signature=0e10f17245daef8aebb4224b4aa1c8217b25ed9c87eae83bed3e624bfa5ab79a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR2IOST%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T133832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQC2Rmjwba881tp%2ByGHCCvUGSjURTjDq1%2FrzJ6FDURQzegIhAII46vkibPUe%2BE5SDP2pj7DdDMkpKw1KGSKIfCZ8pkGcKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyyf4mzPeYlBDAUffsq3AOkHq3tSWGmqlPOI%2FTiCxEYLofq5zDr4Lh9H8Ux%2F7WA3z53dEmZaYUif%2BamNcSJZi2eFcZbzRTDhxwJkYoFDU4lKd1XBauyCh0ROz3TPjAIsMtMWgOQWXYn2HhqqZSa7VTJIel8ZvyWF1IW1V%2FQK0lcIj%2FRaXiG3wca35quv7%2FsogtULnKRBZMewczCNnfg4ckTIbctkYpd8p6Zl7i3RtfpCwsmg2Wvs85ExSMcYFGKCRZcdBpYeJFtjE0uEt4nHzzd%2BdzR2MaPqtQyeQZA7djg5b1WEle%2F%2BD%2Bgjnn7Sc9ijtZ5YcP7IqjEp5P1FfYWaVfBR2gUKzU%2Bl40%2FKzH7xmS%2Bxz%2BXzMMd6jX%2FOwKD%2F0Qw6dtQY3TnJGzW4Bm7k%2BFU70%2FTOajBQCpJjncUzEogVUgt4lHKO44R6xPuNLHa60D2Eu1LAYbB0y73w4LDByYKbrOfmJDKVgwd6Bgu7%2Bn8dEMJO%2F3D45YEG5ToR8FNMfKqmOz1SCYTCtRYf3pNZJmLr6WaGo0H2FygtDNSf6zfqqrPhLTqgfcacn%2BvpXv%2BCYBeGTsrSkIPoqDX0QJGrE207G49vtRz%2Bh2JyeToFwGytlfN3LvqA%2FYD0IsuIDK0iDq22HGyaeF8nONE1ni%2FTjDG5ILTBjqkAbfroyUoTI4H4veiXbkABS6ld%2BOmHN9%2FUt4pVsY6yzIbt5l3%2F3nz3kj8ooQht3WIyCzZs61vDHlPgBIonJTUc6GNc4EwxaIZtytGQPf%2FwTCUzR%2FuY57IhCoMlNCHzzUSnm6oESx25g0pwrHYwgi4r7bAkoCE2H%2BBBDomz6cQccuH121ILbEe1i55VLmu%2BgSCGpGPaoBm1WvM0XLw5PjhUHyO57pG&X-Amz-Signature=a4967605332ef42ac3f8aaa208e809e3509758eb362c3e54095858ac34c6048f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







