



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBHHQXI4%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T123341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDIxgEnqXtrLENedpdJjQG6JLRq7PN%2BCXhyjAFtSXHvEAiABMc5fDJUIgBt1StsjKIm7EwUedBddsm7I8006f8U5LCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaSu9P8QnX3gzeYq7KtwDFCh3nLNev9kXD9VwW53s%2F3S4OOl3iBRSwVStazb8Jvdk9M0qWx7iAF1VJm1ki4tL66JB19Q55%2BRGRRS%2B99%2FGt19It%2FYixWKASALcS51ug9VknZ31ZyVzWm4GRTPp4BeTTutAoJ9DZHkcFVsa4X5axcVsp8FLAPJjWvMlzKzB%2BU4QwXK4NX6bdzTxaeMWh%2B0ZE08TSUlAcCtKUVhBI7YK72IQPFlBJxrvok%2BmOGPmnNLEjRY3MOt7M7za8FoxBUA3sSwwwRp5rjzIUG7xKjETvNU24wDX1lp5XvAwqmedAwnMx40JXf6bI3L33PnaWV2%2BXnM2%2Fbfyyz583u6XfMGV8iNqIQNJrfFAQ%2FwhKmu%2BrQTZ%2BsaWP3yeOD2nGZR5CXMQE8n5uQjp5vt1zvrlFcViTjlXlCufLxY%2BzEes%2Bto7nBBp5a4c2FH92R5RrmL8qi2eoa2m%2BWOUGZQHhIV%2FMACKBO5jluwGvpNUy9c29a6Z%2FDl5nUvYAZzPGYrIWLIdiyQuNPNI3xqu%2FuM5lMLLyHI5Md%2FKYjIGFFIV2nFCUy5DDdsvLc%2BHFPHZpUsQq2E0eFf24ByX8z%2FnqefeQIvzapSm1vGQqJqvSUtgOhep0CkXZJpxh13XivR5WrnUcwsw592byQY6pgEEpl6YdMiKbenbf9pQLCCDoQtoBv3kBFS9WRTBgX1n3C7HUZ4dU4kTEIlGcV%2FGMsE3GHTzjOg%2Bye%2BG6P9wZ3uv1isSKoYpLfjUxPNsdnmACyi6HAIqRsJmyhpksTQeivhvnsO30Htl%2BoexTJfXwkDbJVtkGndF7eppk5kA%2FQG4g6DwyTIU%2BKAsowCVG6dfo02QZ6%2Ftz9l0wejarXkuxHxHGztJjpTH&X-Amz-Signature=06b87bcce398eaa2578964d4f1a3ee9e9246a9498a5a1859870ff333c71afd1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBHHQXI4%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T123341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDIxgEnqXtrLENedpdJjQG6JLRq7PN%2BCXhyjAFtSXHvEAiABMc5fDJUIgBt1StsjKIm7EwUedBddsm7I8006f8U5LCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaSu9P8QnX3gzeYq7KtwDFCh3nLNev9kXD9VwW53s%2F3S4OOl3iBRSwVStazb8Jvdk9M0qWx7iAF1VJm1ki4tL66JB19Q55%2BRGRRS%2B99%2FGt19It%2FYixWKASALcS51ug9VknZ31ZyVzWm4GRTPp4BeTTutAoJ9DZHkcFVsa4X5axcVsp8FLAPJjWvMlzKzB%2BU4QwXK4NX6bdzTxaeMWh%2B0ZE08TSUlAcCtKUVhBI7YK72IQPFlBJxrvok%2BmOGPmnNLEjRY3MOt7M7za8FoxBUA3sSwwwRp5rjzIUG7xKjETvNU24wDX1lp5XvAwqmedAwnMx40JXf6bI3L33PnaWV2%2BXnM2%2Fbfyyz583u6XfMGV8iNqIQNJrfFAQ%2FwhKmu%2BrQTZ%2BsaWP3yeOD2nGZR5CXMQE8n5uQjp5vt1zvrlFcViTjlXlCufLxY%2BzEes%2Bto7nBBp5a4c2FH92R5RrmL8qi2eoa2m%2BWOUGZQHhIV%2FMACKBO5jluwGvpNUy9c29a6Z%2FDl5nUvYAZzPGYrIWLIdiyQuNPNI3xqu%2FuM5lMLLyHI5Md%2FKYjIGFFIV2nFCUy5DDdsvLc%2BHFPHZpUsQq2E0eFf24ByX8z%2FnqefeQIvzapSm1vGQqJqvSUtgOhep0CkXZJpxh13XivR5WrnUcwsw592byQY6pgEEpl6YdMiKbenbf9pQLCCDoQtoBv3kBFS9WRTBgX1n3C7HUZ4dU4kTEIlGcV%2FGMsE3GHTzjOg%2Bye%2BG6P9wZ3uv1isSKoYpLfjUxPNsdnmACyi6HAIqRsJmyhpksTQeivhvnsO30Htl%2BoexTJfXwkDbJVtkGndF7eppk5kA%2FQG4g6DwyTIU%2BKAsowCVG6dfo02QZ6%2Ftz9l0wejarXkuxHxHGztJjpTH&X-Amz-Signature=08e5fec299ace4244456bee527c62937ece2a0f3c80699e6c90bcaceb2b5f319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







