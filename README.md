



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZHYMVQ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T123229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDOtZe0b8Ov5Kxywp5nF1o6qkpxM3ny%2BBzxpHfX%2FDYJWwIgHpRa07jwO2DU6%2BWv6uEzVt2dQbEiLx5opONj4ic%2F0E8q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDHKn9YhhVjMM0sS6oircA4uvVFx83sUWyMOsXTS7pP5CPpniT9iHfYUGeUp68dbgI9Vtffli5XqAqoCcjEFjTbBoU270c8kzrBI%2BEV46w9pmN3u5tVhKOdlIIFOsKxR8BMs4aPb1pMGHrHk%2B4KxetIEfxNca492WS0qTTHLqNWlKYG0RDrXIBExAUhEnHaDVBQnfriAEL8XiHPcppfXsmFYkjGMseBeXwXQfsVvzWoxFfqKTC803ghNsPvmPaiJImB7jgIpGwhVik332YDBR%2FFoxTDFHgDpch%2BoYMsPJlDHyTcfFbzZ5MZwMup%2Bsf%2B742rcGXkPrzTOihZPHbapj5XXQvkOn8LKydNCLi65iXyA0xIuvO7l%2BhEfvRHoW4OxGGpa6ey832rHSmKn%2FK0S55qbRp%2BuUzCJJ6aB0DMbzcuOYiqNyPulxw006lyoJPXE4HEC1%2Bbu3LhDWvQiBQseKfzm%2FqxOw85KwR23kmF%2FvIuRKGH%2BUZFBadehIiis%2Fkyq%2BvbMqMCcEf8orXzRi%2FHN2%2FJBXduK96XEFpGSGkRju3kBqG%2FysD%2FzkqIvADZb9lLpxwMS37PhO1aRr%2FJ8OU%2By9FyAVFs1r8IF5pElXyQbDYu58bxTOVPX8MEkmihT5X86FTPzWixvxmK92fjhrMOmhx8gGOqUBnyBRl9XMllcVjopeMyAdxHIn1qrsoYzvCv7jt%2BfLw1JWa6PGS6YyLZcljImkQ1ACKyy62BkLcyoxoUvMRfieRWUxlDrPkV0ohNAQZfRQvEks%2Fp9ZUnklWYWhcEMDThitcypHvYyi3RAxLEVQcagiEon3tkhcNPtZLiKc7oXpY9dDjNcG1pES2mLua7PtdtPsFGvlCX7o3A5M67esbgRoc3hy9GLU&X-Amz-Signature=c036f906d5da076da4ede01cd7d35ad82ed061e626fefa04a64b917a6d1e8ec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZHYMVQ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T123229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDOtZe0b8Ov5Kxywp5nF1o6qkpxM3ny%2BBzxpHfX%2FDYJWwIgHpRa07jwO2DU6%2BWv6uEzVt2dQbEiLx5opONj4ic%2F0E8q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDHKn9YhhVjMM0sS6oircA4uvVFx83sUWyMOsXTS7pP5CPpniT9iHfYUGeUp68dbgI9Vtffli5XqAqoCcjEFjTbBoU270c8kzrBI%2BEV46w9pmN3u5tVhKOdlIIFOsKxR8BMs4aPb1pMGHrHk%2B4KxetIEfxNca492WS0qTTHLqNWlKYG0RDrXIBExAUhEnHaDVBQnfriAEL8XiHPcppfXsmFYkjGMseBeXwXQfsVvzWoxFfqKTC803ghNsPvmPaiJImB7jgIpGwhVik332YDBR%2FFoxTDFHgDpch%2BoYMsPJlDHyTcfFbzZ5MZwMup%2Bsf%2B742rcGXkPrzTOihZPHbapj5XXQvkOn8LKydNCLi65iXyA0xIuvO7l%2BhEfvRHoW4OxGGpa6ey832rHSmKn%2FK0S55qbRp%2BuUzCJJ6aB0DMbzcuOYiqNyPulxw006lyoJPXE4HEC1%2Bbu3LhDWvQiBQseKfzm%2FqxOw85KwR23kmF%2FvIuRKGH%2BUZFBadehIiis%2Fkyq%2BvbMqMCcEf8orXzRi%2FHN2%2FJBXduK96XEFpGSGkRju3kBqG%2FysD%2FzkqIvADZb9lLpxwMS37PhO1aRr%2FJ8OU%2By9FyAVFs1r8IF5pElXyQbDYu58bxTOVPX8MEkmihT5X86FTPzWixvxmK92fjhrMOmhx8gGOqUBnyBRl9XMllcVjopeMyAdxHIn1qrsoYzvCv7jt%2BfLw1JWa6PGS6YyLZcljImkQ1ACKyy62BkLcyoxoUvMRfieRWUxlDrPkV0ohNAQZfRQvEks%2Fp9ZUnklWYWhcEMDThitcypHvYyi3RAxLEVQcagiEon3tkhcNPtZLiKc7oXpY9dDjNcG1pES2mLua7PtdtPsFGvlCX7o3A5M67esbgRoc3hy9GLU&X-Amz-Signature=44244c1fd236b023707c638cd54f3b76e59395feb2ecd83a420100220e99ee66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







