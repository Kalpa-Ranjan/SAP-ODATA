



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZRPNMZG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T062407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDmgVfreun4ucbWem5kx%2FGGyMvlOLwaPeTsPwOORwOyAgIhAMuDhOvTLDZj3jq7sC%2F8L6WoUOHBt%2BgcXudf2paPqoeGKv8DCC8QABoMNjM3NDIzMTgzODA1IgxB94qO0Mbv2uR4wBIq3APud2vF2mO2Op7usS70Ycih9rnD2pT%2Fj6jJycGiksQkj3A6O%2BNH41ehQ2E26rinXulL%2Flc4wjp5BlhyUM1NPNqH5o%2F56Apg8Vl80hXsApHCS38V5g0K8lYscW%2F08Dzr5p5AE5gkxiSnRdQMB2CMNKdMc5iQlIL3PcyEvZu5j9mEMexYu71%2FSjUkewW2xWcEIme%2BAW4G%2F35h%2F554w3ny1NmlD6IWtg%2BoyfBzcO88kjb6wiFy5ThQgXcAQpo60AsPQex0DYM4FAuDZD%2B6eaAVNpVJl5brHLgUTGRKC0qcCWfRxRAMo8HC3B68BwA%2BSp0zghAxmSIekZb7fPL5AbfWWhPfGCFACt8%2F6PmL1fR2malg%2BmKZ3949mhwI6LVu0QMDD2esKIxboQVdv6XMitw%2B7CVFuhNXWa28G5PLnmskGScdaQlfcOHB8TBDiD6EdT%2BYH8CMmq6HPxJm%2FLfqh%2FD6xmkRoSg%2BO6ZfHVCA6Tt8oePPZ2h%2FF7cNgYeaLUuiHpMguFC8TM75%2BTiL4P0IjFND2tADzyAJjruUf0olbwPvRPM1up6zcKSJK2QdUEm6J3TMDOnKxGALRFwWh%2BGeeYDh03iQSnE0SCe%2BNSCQ0v84ahi1uH4mg1azl4U0DpsIMTD3x9DIBjqkAZL5Qi7hW5zEJxMjx1krcyywOl1JSlBZ%2B5unxsp5poO2ZBoUeuLq5ZQxHXtQ%2FjGh59vibRM0fDn2JPsUdlIw5FdME80vZApl9RnRPmKlBGOdfepg6HOaFv1udvFXRojkC6SEOI680v5lDPEzmxRwFtTSKx6myRxu1mKAcX%2BLTAwMODnQQss4MlH%2BGZtiFlpm5QoobWF7Cv4%2BpKL%2BmcG5niwRJ0Da&X-Amz-Signature=4895e482dadc108c29eaf275f7f3eb75e40fc07c715146a7ddfc3a347dbe54d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZRPNMZG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T062407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDmgVfreun4ucbWem5kx%2FGGyMvlOLwaPeTsPwOORwOyAgIhAMuDhOvTLDZj3jq7sC%2F8L6WoUOHBt%2BgcXudf2paPqoeGKv8DCC8QABoMNjM3NDIzMTgzODA1IgxB94qO0Mbv2uR4wBIq3APud2vF2mO2Op7usS70Ycih9rnD2pT%2Fj6jJycGiksQkj3A6O%2BNH41ehQ2E26rinXulL%2Flc4wjp5BlhyUM1NPNqH5o%2F56Apg8Vl80hXsApHCS38V5g0K8lYscW%2F08Dzr5p5AE5gkxiSnRdQMB2CMNKdMc5iQlIL3PcyEvZu5j9mEMexYu71%2FSjUkewW2xWcEIme%2BAW4G%2F35h%2F554w3ny1NmlD6IWtg%2BoyfBzcO88kjb6wiFy5ThQgXcAQpo60AsPQex0DYM4FAuDZD%2B6eaAVNpVJl5brHLgUTGRKC0qcCWfRxRAMo8HC3B68BwA%2BSp0zghAxmSIekZb7fPL5AbfWWhPfGCFACt8%2F6PmL1fR2malg%2BmKZ3949mhwI6LVu0QMDD2esKIxboQVdv6XMitw%2B7CVFuhNXWa28G5PLnmskGScdaQlfcOHB8TBDiD6EdT%2BYH8CMmq6HPxJm%2FLfqh%2FD6xmkRoSg%2BO6ZfHVCA6Tt8oePPZ2h%2FF7cNgYeaLUuiHpMguFC8TM75%2BTiL4P0IjFND2tADzyAJjruUf0olbwPvRPM1up6zcKSJK2QdUEm6J3TMDOnKxGALRFwWh%2BGeeYDh03iQSnE0SCe%2BNSCQ0v84ahi1uH4mg1azl4U0DpsIMTD3x9DIBjqkAZL5Qi7hW5zEJxMjx1krcyywOl1JSlBZ%2B5unxsp5poO2ZBoUeuLq5ZQxHXtQ%2FjGh59vibRM0fDn2JPsUdlIw5FdME80vZApl9RnRPmKlBGOdfepg6HOaFv1udvFXRojkC6SEOI680v5lDPEzmxRwFtTSKx6myRxu1mKAcX%2BLTAwMODnQQss4MlH%2BGZtiFlpm5QoobWF7Cv4%2BpKL%2BmcG5niwRJ0Da&X-Amz-Signature=7717c53d824d447db871b63127dd6bc8521597b217efab62b5f8fc3ac276f6ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







