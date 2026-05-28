



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GKBIMU3%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T024151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC69Tc5Y5FmX1Hd2b50Bva4C88LnCMKLAmKseK7ijidugIgTujIYiW%2BVybgLVN6Gb97WlCQnBeeIEOdPxAHRoZernMqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPGn9Le7EfmGpCEGXyrcA1sd9t1m55Sf0CksutzEAqRb0QwCGNgQqMTJ2Xaz2S%2BNzAW7%2BtuNfPqsdvpYiUXPkIfsWkHSe86i%2ByCG%2FisR4rk3E1m2KnA%2FFWjHRfXcomd8oVM%2BAhGhY4pduumR3pds3p%2FufdIUVDq9OST0JzRgFCMtJFaWN%2F0PK5PjYYuLCn9H9zSAC7qa5p3mwZy2SY1smrkfaV63FOSiujX%2BFiMs67EbA2mJtE3hOMmmdXo1FpSGj1l4jAmKyeevitmWIXXMqWJS0liGIRiOkuuSAMv%2FgXf81QVp39I6jV%2B%2FoJG21N0LVrLNq7X8X9vY5SaDA36aG9od%2F7SnmQb6xCG3fJAFFi1jsxyISzpevr1OcPEkUzEshWk7wdk5evjT9uhJYeOTRe8%2F7f12WvAJJbTuB3nVUkC2ed%2FpA55gg4aUfP7Wu%2B8BAH4HqraXcczbcw%2FTd61PbMGp8UTU47IgtVfB1dUGQQN2L95yBTDd27CxXHNYw2VdU2g%2BW95rERMiEoAKVePk5QBh1ycL2rFFZe4B2R9iUwA8Ziuh1yvCXEHTsd6nNsMdTepz2E6qOCuhi8QT7KrA0ofNpKra1vonJvoIKkYqYQs2%2FWtEeT4cAySKbu%2BDOHQ50jfOujr0zrKDKB%2FwMKC%2B3tAGOqUBj6GbvTFhQgA5NNqIwsBz4I3Q44PjHMFbME334Xjnpm7PriW0LW7f7cXHYDfkT4JEVa75fmqEMsCaN4dAz1qer72%2Frkg6uFq7yPAs8AZVEmGOHIlChTdBD1qUH16S4k7ILVdy%2FyTS7Y7gL9%2BB0xch0kJxpLkhfp124NiVdqydCoKACRDnUTNT8Ot9uCB4X69GgzB70U0qu%2FhOaAY%2FKnOyWEUmtCfV&X-Amz-Signature=87bea9a192c1658a797d32ea21becaedb830410e7c8733aad9e24892e44a8b4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GKBIMU3%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T024151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC69Tc5Y5FmX1Hd2b50Bva4C88LnCMKLAmKseK7ijidugIgTujIYiW%2BVybgLVN6Gb97WlCQnBeeIEOdPxAHRoZernMqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPGn9Le7EfmGpCEGXyrcA1sd9t1m55Sf0CksutzEAqRb0QwCGNgQqMTJ2Xaz2S%2BNzAW7%2BtuNfPqsdvpYiUXPkIfsWkHSe86i%2ByCG%2FisR4rk3E1m2KnA%2FFWjHRfXcomd8oVM%2BAhGhY4pduumR3pds3p%2FufdIUVDq9OST0JzRgFCMtJFaWN%2F0PK5PjYYuLCn9H9zSAC7qa5p3mwZy2SY1smrkfaV63FOSiujX%2BFiMs67EbA2mJtE3hOMmmdXo1FpSGj1l4jAmKyeevitmWIXXMqWJS0liGIRiOkuuSAMv%2FgXf81QVp39I6jV%2B%2FoJG21N0LVrLNq7X8X9vY5SaDA36aG9od%2F7SnmQb6xCG3fJAFFi1jsxyISzpevr1OcPEkUzEshWk7wdk5evjT9uhJYeOTRe8%2F7f12WvAJJbTuB3nVUkC2ed%2FpA55gg4aUfP7Wu%2B8BAH4HqraXcczbcw%2FTd61PbMGp8UTU47IgtVfB1dUGQQN2L95yBTDd27CxXHNYw2VdU2g%2BW95rERMiEoAKVePk5QBh1ycL2rFFZe4B2R9iUwA8Ziuh1yvCXEHTsd6nNsMdTepz2E6qOCuhi8QT7KrA0ofNpKra1vonJvoIKkYqYQs2%2FWtEeT4cAySKbu%2BDOHQ50jfOujr0zrKDKB%2FwMKC%2B3tAGOqUBj6GbvTFhQgA5NNqIwsBz4I3Q44PjHMFbME334Xjnpm7PriW0LW7f7cXHYDfkT4JEVa75fmqEMsCaN4dAz1qer72%2Frkg6uFq7yPAs8AZVEmGOHIlChTdBD1qUH16S4k7ILVdy%2FyTS7Y7gL9%2BB0xch0kJxpLkhfp124NiVdqydCoKACRDnUTNT8Ot9uCB4X69GgzB70U0qu%2FhOaAY%2FKnOyWEUmtCfV&X-Amz-Signature=b59a325235bffe949316d901f28a9cf8993da6a6d26a1e133a8b5a7a834d47d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







