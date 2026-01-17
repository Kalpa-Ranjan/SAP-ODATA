



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCKXH2O%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T011554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBi3H9LORJk%2Ft%2FKm%2B3rxvOo%2BbXUihgky9XaLmXbkj2jwAiAv%2FURPIGE5E1aiNfmizBUvjtGruQ8Fu5XMy2a7rTL8iSr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMwSX0UxfMRoR2IfU3KtwDwQ8HRMVsS49X5Im8RFq%2FdPpv0x63VqxzilrZFj8Nus7JjepVKULHwMDckMwZI5XbGlryhl4T%2BhmKWi21%2BBYN4G1bxsIL90PZ6cA4aUF38JkUV8y8bm6Hta4Befqg0wiiXOeXQRhhmsYXTycbXKLkoGGKySl66kp8TOOkp5yl6gfRALMxoLHNt5zsMxNxM8pcV25UBqBKc6EZA7vVHgG3a6IohoiZyYsInn1kykZ8YrBxxwNz%2F8tGhmTEO7r4gwjNcA%2BFqKTCu3pTlD%2Fkd0NmIKtiy%2Fao4xBoPgp6om%2FHlEh%2FUh26%2BMherQ0i0gAlhrS0kCGTPy3dPWP6fAsSEhJTUp0ag3NcKR12ok1RpnoXbqjbga49YC1j75V5IjidSn3nRNeE4dnGiGPLv2t6wAe11RXMt8RRQHywRXBvHC7KiGdTScmAoH1wwRZv1j6r2n%2BSAjjWREIsFBTwysW8qVfeBlJcNPtJ6FFsuWyoUF9fHNCajjW%2BPa7iLQWNtXatjDobi64v0hsURsWJoQP%2BuZm8A%2FSd%2BEQIPBTzbgKtjKvYnPwO%2BoFAqWlnYR2lDkoNsuDgdjvyv%2BzWDsWeaf3P7Zxcy73s9gMgJpMhu1tgumUoKky93RI4rXCblUn%2FJD0wmK%2BrywY6pgHu3fGXm4KGVbv0gHs%2B5Emh12xIYujg6iCihnxuGw22JEM9i7T4M4YmsAN128nXvYt9G%2FPPKcS0IlFwUHRcSzvUbIvUHGr6BJ%2BWiQvyXPtp3XQCKePlTMJuHbOY1We%2FpmXQL0NJT%2BODSdrwZpStSzKxwj3%2BbQ2210vsmDFsvYW3zkRXUmh1qIv6BkxonC9AdtYlfuUeAk0uFy8WUyl5cw8%2BIV1booOY&X-Amz-Signature=801d602f9afcd9aea7a802b74ad9ef68676cd5e5ddde8c49cc02dd0c0ac25f72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCKXH2O%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T011554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBi3H9LORJk%2Ft%2FKm%2B3rxvOo%2BbXUihgky9XaLmXbkj2jwAiAv%2FURPIGE5E1aiNfmizBUvjtGruQ8Fu5XMy2a7rTL8iSr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMwSX0UxfMRoR2IfU3KtwDwQ8HRMVsS49X5Im8RFq%2FdPpv0x63VqxzilrZFj8Nus7JjepVKULHwMDckMwZI5XbGlryhl4T%2BhmKWi21%2BBYN4G1bxsIL90PZ6cA4aUF38JkUV8y8bm6Hta4Befqg0wiiXOeXQRhhmsYXTycbXKLkoGGKySl66kp8TOOkp5yl6gfRALMxoLHNt5zsMxNxM8pcV25UBqBKc6EZA7vVHgG3a6IohoiZyYsInn1kykZ8YrBxxwNz%2F8tGhmTEO7r4gwjNcA%2BFqKTCu3pTlD%2Fkd0NmIKtiy%2Fao4xBoPgp6om%2FHlEh%2FUh26%2BMherQ0i0gAlhrS0kCGTPy3dPWP6fAsSEhJTUp0ag3NcKR12ok1RpnoXbqjbga49YC1j75V5IjidSn3nRNeE4dnGiGPLv2t6wAe11RXMt8RRQHywRXBvHC7KiGdTScmAoH1wwRZv1j6r2n%2BSAjjWREIsFBTwysW8qVfeBlJcNPtJ6FFsuWyoUF9fHNCajjW%2BPa7iLQWNtXatjDobi64v0hsURsWJoQP%2BuZm8A%2FSd%2BEQIPBTzbgKtjKvYnPwO%2BoFAqWlnYR2lDkoNsuDgdjvyv%2BzWDsWeaf3P7Zxcy73s9gMgJpMhu1tgumUoKky93RI4rXCblUn%2FJD0wmK%2BrywY6pgHu3fGXm4KGVbv0gHs%2B5Emh12xIYujg6iCihnxuGw22JEM9i7T4M4YmsAN128nXvYt9G%2FPPKcS0IlFwUHRcSzvUbIvUHGr6BJ%2BWiQvyXPtp3XQCKePlTMJuHbOY1We%2FpmXQL0NJT%2BODSdrwZpStSzKxwj3%2BbQ2210vsmDFsvYW3zkRXUmh1qIv6BkxonC9AdtYlfuUeAk0uFy8WUyl5cw8%2BIV1booOY&X-Amz-Signature=926368e188b7bad7d1173da573cc5bd5e1b1e340a93ddedf18353d24e15961e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







