



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOMQJ62%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T062507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCOBWnOgpJ0319LBkegIHViK5hhsNbNrRYCWv5oBMc79QIhAO1jLmOFBTsa51dcB3frrNfadOXDF1Qy94JDsyMLhQ6RKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmQgzkebvks4Ll3tsq3AM7sdU8%2FhcsZZ%2BVuGgePuLj5mZZdj2nTdMjnULCr%2FraBoCGv3oGaKw3pNnp6BMnds8l%2Bs0rQJSJcUaGq%2FPc4VAN6JvPrlbfRo3sIbmgwQCUwoO%2FB3ks7QmYTWcgbX8OolcbrTspRWPvwNM3N1KkYQCv0RjYrTjZeR229irSHWzYGCuRTS4bluzA1E8yqXQqeganBCDgOiYvrsW5PL74LcTlx358%2FYcOgv9%2BxsbzRqi3cemqjD0EFwqswIejDliu93mHeBw0yDW5dNHsk2kPnCfmxSrj437rCY%2FAhtLDR4yLzUpthYmOXu0OwIOtes5sbyukoagNBEm%2BumRqNHuPAvH4HyN8mhkkgzlEj70fuMZW7VHgqOQeVfbOF%2BjYEn2rjk1KEgs56sfkXGvMQqoFuNnW4iaLEdfPfbr5ODwvb%2BVq%2BNW0brqxpWHPRjEq4FY8HqZgTuqp5jUS0%2Fhi0vjDs0Z%2BRfiq%2F6BdwZepfKzf8cUK5PQKaosir%2BEvNTX7rqfBeWsnsTI5WGAMEbWApgHy7mR6d1BZLRFkx6tt3TlqWqAl62lezp3H0D6yIjECdWSm1OZlEiL1JhovCnpqUtZ0%2BBVdVdfeJ15kX96Mf0%2FOUxNZxqoiIY93RxlNRUYW1TD224zLBjqkAdk8JhgS01JZwlInFv4DwRwQBOXoCzp5FOspqHPvB09DWtwcCVbb6nAYwcY8%2FUvTUae2uxF8%2BEvc0%2BTV2FDxr%2BOLeo5lVqVbhI4lm2eMRNmRRbYWiEyxta2Sek3rtQvf01oVcx3diaXoIDMyGjLjHbV5BmQlApRdou8NYJ6aGfeF33r5XBtxYouRDX74Z1D%2Bla%2FNZl%2FVjZ8mdeuUM8XF4BD5sGTy&X-Amz-Signature=3d3a67343b30b471eec6b997889a1894b7a3674a427e1d6832323c66ba826fbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOMQJ62%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T062507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCOBWnOgpJ0319LBkegIHViK5hhsNbNrRYCWv5oBMc79QIhAO1jLmOFBTsa51dcB3frrNfadOXDF1Qy94JDsyMLhQ6RKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmQgzkebvks4Ll3tsq3AM7sdU8%2FhcsZZ%2BVuGgePuLj5mZZdj2nTdMjnULCr%2FraBoCGv3oGaKw3pNnp6BMnds8l%2Bs0rQJSJcUaGq%2FPc4VAN6JvPrlbfRo3sIbmgwQCUwoO%2FB3ks7QmYTWcgbX8OolcbrTspRWPvwNM3N1KkYQCv0RjYrTjZeR229irSHWzYGCuRTS4bluzA1E8yqXQqeganBCDgOiYvrsW5PL74LcTlx358%2FYcOgv9%2BxsbzRqi3cemqjD0EFwqswIejDliu93mHeBw0yDW5dNHsk2kPnCfmxSrj437rCY%2FAhtLDR4yLzUpthYmOXu0OwIOtes5sbyukoagNBEm%2BumRqNHuPAvH4HyN8mhkkgzlEj70fuMZW7VHgqOQeVfbOF%2BjYEn2rjk1KEgs56sfkXGvMQqoFuNnW4iaLEdfPfbr5ODwvb%2BVq%2BNW0brqxpWHPRjEq4FY8HqZgTuqp5jUS0%2Fhi0vjDs0Z%2BRfiq%2F6BdwZepfKzf8cUK5PQKaosir%2BEvNTX7rqfBeWsnsTI5WGAMEbWApgHy7mR6d1BZLRFkx6tt3TlqWqAl62lezp3H0D6yIjECdWSm1OZlEiL1JhovCnpqUtZ0%2BBVdVdfeJ15kX96Mf0%2FOUxNZxqoiIY93RxlNRUYW1TD224zLBjqkAdk8JhgS01JZwlInFv4DwRwQBOXoCzp5FOspqHPvB09DWtwcCVbb6nAYwcY8%2FUvTUae2uxF8%2BEvc0%2BTV2FDxr%2BOLeo5lVqVbhI4lm2eMRNmRRbYWiEyxta2Sek3rtQvf01oVcx3diaXoIDMyGjLjHbV5BmQlApRdou8NYJ6aGfeF33r5XBtxYouRDX74Z1D%2Bla%2FNZl%2FVjZ8mdeuUM8XF4BD5sGTy&X-Amz-Signature=36178031137d6c5be60faa3e0dc61db63fe5b0cc8c7a8fc789737f62d04adcf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







