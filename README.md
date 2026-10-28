



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674OO5L2G%2F20261028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261028T060938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJIMEYCIQDstZ8uTKm6mjp0mBjhY1GHc9gB4TbDssigr06Hxqw1EwIhAK6FhswPiOTGLNRKSOwd4HeQYwdUVDl7rwOJGB6Fom6uKogECP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz40uvhnDd3ZxYzHxMq3AMtAFT9HgFk3gEuiiES9AWknhP8KiMNoXUHqfVs73O%2BPAMfnNdPE877iJ5RPK81PEhGaKfMqZVqq08ip575gfy2yQVZJ%2FnIsXK131eYq6PhxSoB35ZNYs5lhlPpmTqdlKvZBta%2Bjd3t20gVeL4HTrVxU6N7%2F%2F8LnTTp%2FPE3p8F6fXhhFNXAB9EK6lf7d5PkbReU4U9Gz3q47YuOnSZgCK6VcfuX8L7IGaoVd8ISj06CExFoSy02WahIXi%2BDtgeQ%2FpACNnbIkpdsTV7FjQaWXPAfZ3DoKNAqj6nmHWuwE8Bw408DI4Zu6P3hIwZRz45cVEOnoveK2C5qp6a3V2z0%2BTsHyjmaPUWSvQr1WNvIe%2F%2BWeunMFGjUnOmODFtW126fV9feOGUgSL%2F9STgk3zWoWCcUtrDkAIPz75vrSp3za6pJKveUw7faML32Ll1K2986AVTSxHHjBKh6TOZPoaz4DAbC9sONuGewgVmx6cGn1VyK7F8fMi6h9TTnQQPZOC54hzLg2QQxWlZsEiaCzBTSzi%2BE9SyfNsETUH%2FiBhiJtZYZI7Cc0E1e8tWqgSM%2FMounCIBD9jMXt6xQqlHYmsLRevDVnHvdtq%2BTJRBWLPH%2F0KteHYbwXDn8wFzrnPQeEDCLiIbXBjqkAeyh3Hu5Yz%2Fckb0qglMevToQh%2FeAyYUhV%2F46Yz3UPseSJi56bHnbd3jBg0iUDye3vzipANSG18OoWdmB4Cxuj8KwLsvXlOKBrGHu56E%2Bm4xEcfGCCAZRxyf8LMLulquqXvJZW%2Bg0v3pvsHPf74J%2FOE09rBLS4OQBmlG2NFxZKjZRYr%2BgM%2BQK9S4cJXUabxchnORgNywLwT%2Btnr9XLyr13tOB%2BfPb&X-Amz-Signature=fe3cbad348223a9c9b17749c7b7a2dd6f81c80b74d9a2fb687fd93c25bd1f671&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674OO5L2G%2F20261028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261028T060938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJIMEYCIQDstZ8uTKm6mjp0mBjhY1GHc9gB4TbDssigr06Hxqw1EwIhAK6FhswPiOTGLNRKSOwd4HeQYwdUVDl7rwOJGB6Fom6uKogECP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz40uvhnDd3ZxYzHxMq3AMtAFT9HgFk3gEuiiES9AWknhP8KiMNoXUHqfVs73O%2BPAMfnNdPE877iJ5RPK81PEhGaKfMqZVqq08ip575gfy2yQVZJ%2FnIsXK131eYq6PhxSoB35ZNYs5lhlPpmTqdlKvZBta%2Bjd3t20gVeL4HTrVxU6N7%2F%2F8LnTTp%2FPE3p8F6fXhhFNXAB9EK6lf7d5PkbReU4U9Gz3q47YuOnSZgCK6VcfuX8L7IGaoVd8ISj06CExFoSy02WahIXi%2BDtgeQ%2FpACNnbIkpdsTV7FjQaWXPAfZ3DoKNAqj6nmHWuwE8Bw408DI4Zu6P3hIwZRz45cVEOnoveK2C5qp6a3V2z0%2BTsHyjmaPUWSvQr1WNvIe%2F%2BWeunMFGjUnOmODFtW126fV9feOGUgSL%2F9STgk3zWoWCcUtrDkAIPz75vrSp3za6pJKveUw7faML32Ll1K2986AVTSxHHjBKh6TOZPoaz4DAbC9sONuGewgVmx6cGn1VyK7F8fMi6h9TTnQQPZOC54hzLg2QQxWlZsEiaCzBTSzi%2BE9SyfNsETUH%2FiBhiJtZYZI7Cc0E1e8tWqgSM%2FMounCIBD9jMXt6xQqlHYmsLRevDVnHvdtq%2BTJRBWLPH%2F0KteHYbwXDn8wFzrnPQeEDCLiIbXBjqkAeyh3Hu5Yz%2Fckb0qglMevToQh%2FeAyYUhV%2F46Yz3UPseSJi56bHnbd3jBg0iUDye3vzipANSG18OoWdmB4Cxuj8KwLsvXlOKBrGHu56E%2Bm4xEcfGCCAZRxyf8LMLulquqXvJZW%2Bg0v3pvsHPf74J%2FOE09rBLS4OQBmlG2NFxZKjZRYr%2BgM%2BQK9S4cJXUabxchnORgNywLwT%2Btnr9XLyr13tOB%2BfPb&X-Amz-Signature=e396ab5ab9d25b97a6c76f2fb8dc899605576677951e9a6b20389bad6d2c5f13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







