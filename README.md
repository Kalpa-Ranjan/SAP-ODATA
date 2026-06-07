



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGQRWN4H%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T191403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjQMx%2Fjk7Gf4HQXrjBPKCMrg1dqkFFnLW%2BGOiARAl1GQIgTi4OwRxVrDbUtT04jS5e7jHPV8nfP93mMVRkBVjQ5TYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAimjiUyh0kdj0PLACrcAySVfhJy%2F%2B83THR6jqO%2BbUjhGlfj1ElKcWHK3YvHtLK0JNUM3FCFQgEdTUAUHa%2BcrQLm0FTFHSdEvFnVwyYkcEhnHV0CL2v0PSdMmh7Zif55cZkzfiYDGG4M0XAA5p1xo%2FdVQm9IwlnPzgF8k3kYP2qd7sILMss7Qk8dgvOECQobQs%2FP5zOscqKe%2BomNHduuEdeoHK31IzrE9f9K%2BlSEC67zuY07rpV8hzke8yLYWBznnpCzsycO%2Bny9PaIW4%2Fkos6Mb%2FS4V8Zey%2Br8Wg2Zzg4WO75s03wtOZrhbou6YkqEMO%2Fc6kv%2BxzIZMqsYLMr2DL%2FVE10C%2BOQcHe3kc6tTyPGSZtdGzdVTrDdJTn0h6WvVHBBMxXncKshk5c9moc%2FXXRjGh1vbbZ060Qr%2FF0PGxI7Vdpzvts7yq0sVlrFJdhl1Y%2FgVyYmXnDGGEmFJO0CWBQbtQGiRJX7kdgFtFzqxwKxPxh8OdNOiRGScfy%2B1VC9IKmY5eEv%2FGm8M%2F7FxCzpNaDdYm5xnr21AWXQog34RNhMyVKs0hjIRmUyW6YPDPZxmGUEixvGOV4Pgr2%2BepatUDOYQqybc0pWZrRhl4%2FikT5zBlr7Bg06vH4fQHc5dWadV0sKCm4czftZ2H7yznML%2FgltEGOqUBjK3wIjElA1%2FOuJQT%2FXdFuxaycNvR9ppCt7Gb2Gezj5TFygEEiRJwlAgnpvNi9RQVyJ8DqryH9KHsYUeNc9%2FHuKtF8vv1oqM%2FSZ3OSGDTz2Sgp05IyLqOLjBCUM%2BOht6poH78SlgOC%2FQ%2BXLj4YpMnS%2BZrr0xBXpKRxmv2WDdUqTu%2FyzL1QTuO5W8OjKTQcK1hSQwgFPoerAU7iABUDiyTr7TdgqIk&X-Amz-Signature=b05a6fc1cdcc87d7d4362468eaec70e62d5712701b8dd21e249895cc78adbb71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGQRWN4H%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T191403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjQMx%2Fjk7Gf4HQXrjBPKCMrg1dqkFFnLW%2BGOiARAl1GQIgTi4OwRxVrDbUtT04jS5e7jHPV8nfP93mMVRkBVjQ5TYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAimjiUyh0kdj0PLACrcAySVfhJy%2F%2B83THR6jqO%2BbUjhGlfj1ElKcWHK3YvHtLK0JNUM3FCFQgEdTUAUHa%2BcrQLm0FTFHSdEvFnVwyYkcEhnHV0CL2v0PSdMmh7Zif55cZkzfiYDGG4M0XAA5p1xo%2FdVQm9IwlnPzgF8k3kYP2qd7sILMss7Qk8dgvOECQobQs%2FP5zOscqKe%2BomNHduuEdeoHK31IzrE9f9K%2BlSEC67zuY07rpV8hzke8yLYWBznnpCzsycO%2Bny9PaIW4%2Fkos6Mb%2FS4V8Zey%2Br8Wg2Zzg4WO75s03wtOZrhbou6YkqEMO%2Fc6kv%2BxzIZMqsYLMr2DL%2FVE10C%2BOQcHe3kc6tTyPGSZtdGzdVTrDdJTn0h6WvVHBBMxXncKshk5c9moc%2FXXRjGh1vbbZ060Qr%2FF0PGxI7Vdpzvts7yq0sVlrFJdhl1Y%2FgVyYmXnDGGEmFJO0CWBQbtQGiRJX7kdgFtFzqxwKxPxh8OdNOiRGScfy%2B1VC9IKmY5eEv%2FGm8M%2F7FxCzpNaDdYm5xnr21AWXQog34RNhMyVKs0hjIRmUyW6YPDPZxmGUEixvGOV4Pgr2%2BepatUDOYQqybc0pWZrRhl4%2FikT5zBlr7Bg06vH4fQHc5dWadV0sKCm4czftZ2H7yznML%2FgltEGOqUBjK3wIjElA1%2FOuJQT%2FXdFuxaycNvR9ppCt7Gb2Gezj5TFygEEiRJwlAgnpvNi9RQVyJ8DqryH9KHsYUeNc9%2FHuKtF8vv1oqM%2FSZ3OSGDTz2Sgp05IyLqOLjBCUM%2BOht6poH78SlgOC%2FQ%2BXLj4YpMnS%2BZrr0xBXpKRxmv2WDdUqTu%2FyzL1QTuO5W8OjKTQcK1hSQwgFPoerAU7iABUDiyTr7TdgqIk&X-Amz-Signature=0e61b60ba4221ccb3e1fc105bef83543f572620627977732b39c4c518ae1ab80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







