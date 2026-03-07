



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJGZMGA3%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T063329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIDw3MctBjPQdWgxEGiEF289yorz%2FDqyJkTOzxs%2F4zl61AiB4fMaO0YPMKFhZ3C33n45%2Bw3PsSs1kU6xW1ZweOIRWqCqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FvhW1W5DWAE8veSIKtwDESduxtom9BPiwawjFF6w4x57z%2BNjjff2xAr8FgXBpho62cuj09T56wLu9VEUv7mV%2F6Nhw7gut9gHIyslxDKPwoIpm2Z88cwUduhkxnN3VWLlwLJ%2B8c2%2BvkcvS8xEDOmQugcDXqmwX2MRS5vylQ2BSBZpN950c%2FEnh4n%2Bd2caOOBdcYHLp1Q90uaKMJmG6JeuG6T%2F2fFv6wAJus8ScW0CnSiO5LjhxZ4scLgmu96wCPkZ5a338lVmV8SbHPcuwYSGrg%2BQO%2BoF4157RuKyooogTNhIezOwvBdAuOq5Hyf1OR3YcH2u4IQzlIrcp9t94vbldaxwE9s0EDrgc6vpVb%2Fehz0Mi%2FANzDwVqqaENCt09LO2PSGombcZeZhXbD%2FqiFnk%2FFUCarHqD4K4uCaW7mLm690q8wOr%2FQBwlCRBT7VuETLJFDBt3dWHKLQ2UnjpC%2FjsSYFOHbk0AUY16UMCiI5zD490cJbNRk25meM7nlJAfqGunIGTx6jb3lxP7j9dHpm6W0jZj9QoWxhbiQ6JxWUQyu7Xqi1gRsavKPetnTg%2BFTIl%2BkP17SVnyOGLxSYzj5Gh1n4iS9NdAVg9T7Vpzt9qpGqY8ih2JAD%2FcFoi0F0YXl3jsCsdK5%2FJxaXtJ5cw6%2FiuzQY6pgFez9dl%2BxYrkfhymHYa44K2VqbQw9X30re15LqKui%2BVnoD5ZJFS8pLoVhmZ4GCLnPx5hqKv0CFB52NSLevmGGOP2HsnYr8nnteUL3U%2BONSIBxuqeGscwMNSUEYJboC9%2Bya9Wqyc2%2BXDhXBOrBkSpkggUh5lY7L3vOwKuur0ZGek7cKHZ4HZn4aaILxmIkP66CnGz30jdO%2F%2Be1nkTX%2Bj9%2BpLAdrW8ZJC&X-Amz-Signature=31ee118cbb5a9275c5ec5bc2c954b7e6b908c9f01a0d359558e64ab600ee3e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJGZMGA3%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T063329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIDw3MctBjPQdWgxEGiEF289yorz%2FDqyJkTOzxs%2F4zl61AiB4fMaO0YPMKFhZ3C33n45%2Bw3PsSs1kU6xW1ZweOIRWqCqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FvhW1W5DWAE8veSIKtwDESduxtom9BPiwawjFF6w4x57z%2BNjjff2xAr8FgXBpho62cuj09T56wLu9VEUv7mV%2F6Nhw7gut9gHIyslxDKPwoIpm2Z88cwUduhkxnN3VWLlwLJ%2B8c2%2BvkcvS8xEDOmQugcDXqmwX2MRS5vylQ2BSBZpN950c%2FEnh4n%2Bd2caOOBdcYHLp1Q90uaKMJmG6JeuG6T%2F2fFv6wAJus8ScW0CnSiO5LjhxZ4scLgmu96wCPkZ5a338lVmV8SbHPcuwYSGrg%2BQO%2BoF4157RuKyooogTNhIezOwvBdAuOq5Hyf1OR3YcH2u4IQzlIrcp9t94vbldaxwE9s0EDrgc6vpVb%2Fehz0Mi%2FANzDwVqqaENCt09LO2PSGombcZeZhXbD%2FqiFnk%2FFUCarHqD4K4uCaW7mLm690q8wOr%2FQBwlCRBT7VuETLJFDBt3dWHKLQ2UnjpC%2FjsSYFOHbk0AUY16UMCiI5zD490cJbNRk25meM7nlJAfqGunIGTx6jb3lxP7j9dHpm6W0jZj9QoWxhbiQ6JxWUQyu7Xqi1gRsavKPetnTg%2BFTIl%2BkP17SVnyOGLxSYzj5Gh1n4iS9NdAVg9T7Vpzt9qpGqY8ih2JAD%2FcFoi0F0YXl3jsCsdK5%2FJxaXtJ5cw6%2FiuzQY6pgFez9dl%2BxYrkfhymHYa44K2VqbQw9X30re15LqKui%2BVnoD5ZJFS8pLoVhmZ4GCLnPx5hqKv0CFB52NSLevmGGOP2HsnYr8nnteUL3U%2BONSIBxuqeGscwMNSUEYJboC9%2Bya9Wqyc2%2BXDhXBOrBkSpkggUh5lY7L3vOwKuur0ZGek7cKHZ4HZn4aaILxmIkP66CnGz30jdO%2F%2Be1nkTX%2Bj9%2BpLAdrW8ZJC&X-Amz-Signature=00e0dfcad52d2f6924ec9880290c728e55822d4523ef5cd20c95bcdac9dc8f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







