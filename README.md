



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4SVSR6%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T063139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGm6KWKGUMyI5Gdy93sMlF6u2h0ucvOFQnIrAhwqZqgwIgZO3s%2Bb7wGrWoCKFoVqSwwUW2l1YnXtLF8CQ0OWrBZKIqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6g7guq6PnA8NFOLyrcA0%2FY0%2BFrN6HonTz%2FLsWssPB9t2WYbgQ0yjSRmcqUDXvRzpBWlbwH2%2FgPuJM%2F4H0md1ITv9%2By34jyZMejdau8ZFf%2BOeJLw2ZKj2dK6R5dKtJCZ9Jg5AwGgp5EMS0Sj%2F3i8mFztzPY6jacP%2BGF0iMJiV6Z%2B6kigN3a4qsd8LVYaA4b2BX6crwwRXOog17Ca0XgkyocmU0OR6lxMDYEjVY8QfIEJC64IRyT%2BdFsMvhUjG2aaiox4nbc4pcFe8jEP4Q930vz0OIzXDEG6cjXnrJXnC8SNSHpVRTpDvBkcC3p1Y705Mdx2yzt0%2BuXmd2y9EvrxFk7b5v6QdPf%2FTtVOnGh0ubG8EekSpd7FRkN442SRITik9Gw%2BvXEyI0OvFFInQ0Q8mAUp5Bqw8c7nQXCr8Wc9XFfp%2FhU4CaecgkKC0nT1AUTtp88PYkYSplJZWeS70bj0wBFV12voP2RXuxiF8VQmpM3fQrXsANRkjnU%2FHq0TTaI0VxAyU5dGQZxf%2BYk1rKcnxl%2FMLk%2F7yMyYunLVPk%2FkLdgmsj7lJtc%2Bi5Y1xz0oBLvkj5IzavJmn7zzK1d3WeoiMgqIG9HZyT2uU5Dvd%2BhAImT7gFd3m7QrFQgesBNLEqzhjmIV7MiIev5M4%2FuMPz5tssGOqUB0sExS9gKarPuDNtAZtwOQxULtgIcERPejwMrsFNCoZGLQeE2ccWKgs0%2F9bvLOQhgijndzti%2BT5aCy%2B%2BrqfdiQ6uD1Xv8XRpJUwqC4AL%2FeFebI%2BmthVWc5XLeSMYCs00RSDhowfEcH4pbxGIpqycyFBNvHK%2F7ZAr4cCwZhE28lyKZAlpXBWebmBNNeh6xrJnFRZ6He2GHo%2BAtBRzQKpgh3p1hkkwi&X-Amz-Signature=388f31e3fea187a20c062e452f9811ef2bfb0e1ef18f37233fe40644d476da55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG4SVSR6%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T063139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGm6KWKGUMyI5Gdy93sMlF6u2h0ucvOFQnIrAhwqZqgwIgZO3s%2Bb7wGrWoCKFoVqSwwUW2l1YnXtLF8CQ0OWrBZKIqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6g7guq6PnA8NFOLyrcA0%2FY0%2BFrN6HonTz%2FLsWssPB9t2WYbgQ0yjSRmcqUDXvRzpBWlbwH2%2FgPuJM%2F4H0md1ITv9%2By34jyZMejdau8ZFf%2BOeJLw2ZKj2dK6R5dKtJCZ9Jg5AwGgp5EMS0Sj%2F3i8mFztzPY6jacP%2BGF0iMJiV6Z%2B6kigN3a4qsd8LVYaA4b2BX6crwwRXOog17Ca0XgkyocmU0OR6lxMDYEjVY8QfIEJC64IRyT%2BdFsMvhUjG2aaiox4nbc4pcFe8jEP4Q930vz0OIzXDEG6cjXnrJXnC8SNSHpVRTpDvBkcC3p1Y705Mdx2yzt0%2BuXmd2y9EvrxFk7b5v6QdPf%2FTtVOnGh0ubG8EekSpd7FRkN442SRITik9Gw%2BvXEyI0OvFFInQ0Q8mAUp5Bqw8c7nQXCr8Wc9XFfp%2FhU4CaecgkKC0nT1AUTtp88PYkYSplJZWeS70bj0wBFV12voP2RXuxiF8VQmpM3fQrXsANRkjnU%2FHq0TTaI0VxAyU5dGQZxf%2BYk1rKcnxl%2FMLk%2F7yMyYunLVPk%2FkLdgmsj7lJtc%2Bi5Y1xz0oBLvkj5IzavJmn7zzK1d3WeoiMgqIG9HZyT2uU5Dvd%2BhAImT7gFd3m7QrFQgesBNLEqzhjmIV7MiIev5M4%2FuMPz5tssGOqUB0sExS9gKarPuDNtAZtwOQxULtgIcERPejwMrsFNCoZGLQeE2ccWKgs0%2F9bvLOQhgijndzti%2BT5aCy%2B%2BrqfdiQ6uD1Xv8XRpJUwqC4AL%2FeFebI%2BmthVWc5XLeSMYCs00RSDhowfEcH4pbxGIpqycyFBNvHK%2F7ZAr4cCwZhE28lyKZAlpXBWebmBNNeh6xrJnFRZ6He2GHo%2BAtBRzQKpgh3p1hkkwi&X-Amz-Signature=64e0b8053e2e9f52502edddeef22bf8b252b369dee6d9da0556e04ce86c87ca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







