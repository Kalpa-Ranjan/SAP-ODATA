



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JUPI4Y3%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T062913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0P%2BhDxhHN%2FHgUO2f0OhaSDWtGlQz0ynY%2BSrjTKV6WuAiBJSBRuznbF7ClMIz0WtVuVhhSePrEgiw2G2%2FBnYftBHCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUkpq3mDe9fu4wv4tKtwDe%2FopHKERhH4QGrbegWfLpyW73kkvZSbHVewQnDI2elSb4qVAyn6LA7Kr3uAVIZJodP10HngxnKfWKuHvqHHLBhGJ73o51YICdsj%2FYCeyjk8ZjgYNi%2Fnyit8qFMx0q4eL5i%2F%2FAuko1D2uFekq9DzBmwfVwMytPK9TwkIrRClNb8rp22BiOI7c9C82MfuPkiBdlC%2Bz2N0h2eaXvr2NyWMkN5IEVMa0ChMc98hjKzoChglgE1Cc0%2FXY6WxVHla2JDJZccUUltiKoanT6QdHJ6O87CXWuh5bwmG1gPhx%2BEAH0nR4BXvQBwKNlb0%2BxXfLNQdbPGcx9FoYXRsVD%2B3dq2KW64gLFHuR8n2XoK6HwoXc1EZv2ldkTqj0ikOjXBsELX5%2FUlCzHowyn7HrJ%2BkmPJ0ZjJeSwBMyRBDUIYxf0TtAeGdrrB037yQkG70GK%2FEduoHqg4m%2FtMNxKN0OGi9Awjnuanwet2x3%2FlHirzq5Xo92Y43yQlJCSw9s86k3D43yshWT5yYgOofDnkwCiLKiq4nQsvAgEJIsCnT4tqXlvl%2BU327GwOFTBWY%2FhORZ9t%2FEiJoMa69nWuYPxKgpWyiJ7Zav%2BaXE2SzVB5X%2B1oAhSGeIjhJSp4mevVitcpBYOH8wzre8ywY6pgEwkrDmXl4QPHWVg4aR%2FYkTFHiVQkTFNfSDHM9uoFdT7E%2BqcVDZYLEWZu6M3j9xiJZ72FQfZ73IScJexxC%2FuLSZMQ38QziXalupxbkF75OsKfJX8bd6sNjjy7ZCIwVHILopYTLvLNwEBcbDI05zJNLlpsd9LBBN8IziDZAUvTMFdHKYTCVeX7myGbaWWx2OyLSlCXAdaMpUSEPYYoT9O7jvELfCOla3&X-Amz-Signature=4d1f96f1d19ddbdc5c7a780275d558ad35ca9871f9e2be02d0ecad77be0056c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JUPI4Y3%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T062913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0P%2BhDxhHN%2FHgUO2f0OhaSDWtGlQz0ynY%2BSrjTKV6WuAiBJSBRuznbF7ClMIz0WtVuVhhSePrEgiw2G2%2FBnYftBHCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUkpq3mDe9fu4wv4tKtwDe%2FopHKERhH4QGrbegWfLpyW73kkvZSbHVewQnDI2elSb4qVAyn6LA7Kr3uAVIZJodP10HngxnKfWKuHvqHHLBhGJ73o51YICdsj%2FYCeyjk8ZjgYNi%2Fnyit8qFMx0q4eL5i%2F%2FAuko1D2uFekq9DzBmwfVwMytPK9TwkIrRClNb8rp22BiOI7c9C82MfuPkiBdlC%2Bz2N0h2eaXvr2NyWMkN5IEVMa0ChMc98hjKzoChglgE1Cc0%2FXY6WxVHla2JDJZccUUltiKoanT6QdHJ6O87CXWuh5bwmG1gPhx%2BEAH0nR4BXvQBwKNlb0%2BxXfLNQdbPGcx9FoYXRsVD%2B3dq2KW64gLFHuR8n2XoK6HwoXc1EZv2ldkTqj0ikOjXBsELX5%2FUlCzHowyn7HrJ%2BkmPJ0ZjJeSwBMyRBDUIYxf0TtAeGdrrB037yQkG70GK%2FEduoHqg4m%2FtMNxKN0OGi9Awjnuanwet2x3%2FlHirzq5Xo92Y43yQlJCSw9s86k3D43yshWT5yYgOofDnkwCiLKiq4nQsvAgEJIsCnT4tqXlvl%2BU327GwOFTBWY%2FhORZ9t%2FEiJoMa69nWuYPxKgpWyiJ7Zav%2BaXE2SzVB5X%2B1oAhSGeIjhJSp4mevVitcpBYOH8wzre8ywY6pgEwkrDmXl4QPHWVg4aR%2FYkTFHiVQkTFNfSDHM9uoFdT7E%2BqcVDZYLEWZu6M3j9xiJZ72FQfZ73IScJexxC%2FuLSZMQ38QziXalupxbkF75OsKfJX8bd6sNjjy7ZCIwVHILopYTLvLNwEBcbDI05zJNLlpsd9LBBN8IziDZAUvTMFdHKYTCVeX7myGbaWWx2OyLSlCXAdaMpUSEPYYoT9O7jvELfCOla3&X-Amz-Signature=2dc023c3e8af50ef98063a16b90ee99d64d9fa24b48afc87354ef0557dd10f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







