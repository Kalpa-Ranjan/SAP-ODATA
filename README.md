



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFEBTEV%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T020134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQD5O%2Bj7T0pjZ0ljXGfZlkPDymBHCPrlHloaQgW7BtfhKQIgOLuUSU%2Ftk4P4dcw3u7RMyRn8qCQmMNCkAf3wv3BnMCsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDIlBRco92xKhslwjdSrcAzT4lKT2tWYeDjNn3uy9irRIt9vT8Cu9jrgJfmp03jt0MhSTIQxHWCaUAo1y7cq7%2FXAYDs9gzJYmsyheNBG8%2B4OKyqYHPVuyStYDQoZqTRKIh%2BnL6K0D0c%2FZba4wek9XOJ09ZC3IKChNAmW8fBpQipOg%2F8175IkIL5FLkQtHiz%2F%2FkxIUFlyTPv4qaRnWXmgO%2B50LXlfGzxPMcUFynPsqV0foN9JaUstkQhjWl4Kgi%2BMW2OI4Zdo9UNzbH0IIfSS%2FL602QwOmZxTK8%2BPagqr6k%2BxkOKBA%2BhV6QsUf8LYxZIHytpbPDdnhEPdb5oLR%2F9In4beI%2B6A2hJXeQwmUBZpzhvtkNlsPa0tJXK0utbCRbolMiL0D8NZPcWsuPZmFrrFksO4cZLAyPhYCX1yZOOUMWP6LVZNj6JOrQEehtckCwA81ZdplwriTozD1lHvRyuhnzfAZxjJQLqFhaasaMh4mi5225cziJE9l20J6OQiPbyOQbUMB6QOQj3BR0GZ892QW%2BJyCiGKDvWXWQhwiHx2VYplTSpvdZYjLnuejUbmJzUpElA9W3VQZW6WJmJQKqV5hTbkujEHAaXQanwV%2BrrDUjBCgJat5ux2yScOTAK2FIEjOGnfVG7aLe1XK6RtGMLynp84GOqUBIPLhGr8p5cMGKhGbWbR7v7o4D31WNiHelFKm3A7dn5EzevIWP2JBBSMa7mOtSTLGC%2BRvN6%2Bxrd9rNy%2BWVtjHExl1h3K6DwzHO%2BoTM11g9i8Bt%2FX%2BXTMxoMR8PxrKppT9XgVcRFPjOOV6h3U9XwqccHDgbJKd9v58WK0lrIxDuzUnPNDs6jdezhMehurv3Xr76JhHLMejhwtQtlaQxrMA62lZ%2BL9T&X-Amz-Signature=df320ad8a786418d7f1a6ad4c986057836f3bd949cc48b4a990b0c102139f49e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KFEBTEV%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T020134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQD5O%2Bj7T0pjZ0ljXGfZlkPDymBHCPrlHloaQgW7BtfhKQIgOLuUSU%2Ftk4P4dcw3u7RMyRn8qCQmMNCkAf3wv3BnMCsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDIlBRco92xKhslwjdSrcAzT4lKT2tWYeDjNn3uy9irRIt9vT8Cu9jrgJfmp03jt0MhSTIQxHWCaUAo1y7cq7%2FXAYDs9gzJYmsyheNBG8%2B4OKyqYHPVuyStYDQoZqTRKIh%2BnL6K0D0c%2FZba4wek9XOJ09ZC3IKChNAmW8fBpQipOg%2F8175IkIL5FLkQtHiz%2F%2FkxIUFlyTPv4qaRnWXmgO%2B50LXlfGzxPMcUFynPsqV0foN9JaUstkQhjWl4Kgi%2BMW2OI4Zdo9UNzbH0IIfSS%2FL602QwOmZxTK8%2BPagqr6k%2BxkOKBA%2BhV6QsUf8LYxZIHytpbPDdnhEPdb5oLR%2F9In4beI%2B6A2hJXeQwmUBZpzhvtkNlsPa0tJXK0utbCRbolMiL0D8NZPcWsuPZmFrrFksO4cZLAyPhYCX1yZOOUMWP6LVZNj6JOrQEehtckCwA81ZdplwriTozD1lHvRyuhnzfAZxjJQLqFhaasaMh4mi5225cziJE9l20J6OQiPbyOQbUMB6QOQj3BR0GZ892QW%2BJyCiGKDvWXWQhwiHx2VYplTSpvdZYjLnuejUbmJzUpElA9W3VQZW6WJmJQKqV5hTbkujEHAaXQanwV%2BrrDUjBCgJat5ux2yScOTAK2FIEjOGnfVG7aLe1XK6RtGMLynp84GOqUBIPLhGr8p5cMGKhGbWbR7v7o4D31WNiHelFKm3A7dn5EzevIWP2JBBSMa7mOtSTLGC%2BRvN6%2Bxrd9rNy%2BWVtjHExl1h3K6DwzHO%2BoTM11g9i8Bt%2FX%2BXTMxoMR8PxrKppT9XgVcRFPjOOV6h3U9XwqccHDgbJKd9v58WK0lrIxDuzUnPNDs6jdezhMehurv3Xr76JhHLMejhwtQtlaQxrMA62lZ%2BL9T&X-Amz-Signature=903aed901f7d721ccfbefe44b85a2de4a04e5afcc206ac8d0b281503de05fadb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







