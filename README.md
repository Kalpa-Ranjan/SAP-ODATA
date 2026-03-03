



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJSAPHD4%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T184022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAodxjChs4FvdboDzr7AuFxX1TW0lcQNW4eIGggw7MGQIgPOwcFOnvNQs%2BD37zNbGsWaOZcyuONyKpqkk577xv%2BZUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEojXL36JohwCWiGUyrcA63Z%2FLdLHS8koEpdffFk7MNVFxsiGCxJbgRaUfuU0lzJvgSiXMdn2Xm815iovkw3DoFyu0%2Ff77DzYbb57jXWR%2BijHVpBROhq%2BFmqRO4IQXxdu6C%2BX%2F%2FhYjAtBUhhSm2B4waZPUhnhD3hKJUCJVgvrlot73MvWp3wowFCPCgSkGz42zxxPcvaOOjDcTuCWZPIn%2FhbhB63nMtKM%2BRZvHOIvZ3DiAlzAerGDbmM%2Bu6ieZu91%2F67edyVKDjescgFx7%2FGPYJSz3LW%2BGpup9w0yhcMx%2FiOc5ugTETyFC8FvWbMWxf67Qk2zhXuBpefoauVvmGfqpmizhgSNqOzXYFVe8EDeyjxPz6q3EsnyyUFk0HPUhr2%2FKjbRiOUQh2ck1Axexj0PrX%2Ft%2FQp7fT2siXTy3dSbWpimfUNHfk8jfPsmhAu1QsyEnZhLDnWwjQ2lpSf3ANiSlEr%2BDtvAN8yxZ01CkKf81kTVDKYAgCBgQL13J4a8lcvbxOvDuHD6j7syvUxjLbzaxy68%2BHZRRiqDaePX9%2BdUlL50yRz6iOlUpnAX64YDZUVZjclvmtEYTsC13KDo5GXe2uZ%2B5ePiwEGB%2B7Q4cUDD74zL2%2BrWvX3PnbDFuT4Eep6F0a4B3xlcSDfHQ8LMNTOnM0GOqUBVLFSLM9fVpQTnpBYQzrQN331LTLyKR1Y6eHAY90b%2FBdOWa2gZq1Z1LsiYdLp0QTyuEHZIb%2F4nmc3H9XCff6ilzGdFYDmglizh7BcMvf0oYQ25YFbaG9E8O4OMieCowvWyaP9No%2FkYKwrDz4lt%2BUjxnxTRxKlu5P8h%2FevgEOeIcuHEJmxWXMGN96yrWbVuW7zmgK%2BCDwje4yE17hoBuoUmZDm1dYM&X-Amz-Signature=cf73e1ad148c25d3331367708039aa1927ef0cd371b70fbff2df622e0a0725c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJSAPHD4%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T184022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAodxjChs4FvdboDzr7AuFxX1TW0lcQNW4eIGggw7MGQIgPOwcFOnvNQs%2BD37zNbGsWaOZcyuONyKpqkk577xv%2BZUqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEojXL36JohwCWiGUyrcA63Z%2FLdLHS8koEpdffFk7MNVFxsiGCxJbgRaUfuU0lzJvgSiXMdn2Xm815iovkw3DoFyu0%2Ff77DzYbb57jXWR%2BijHVpBROhq%2BFmqRO4IQXxdu6C%2BX%2F%2FhYjAtBUhhSm2B4waZPUhnhD3hKJUCJVgvrlot73MvWp3wowFCPCgSkGz42zxxPcvaOOjDcTuCWZPIn%2FhbhB63nMtKM%2BRZvHOIvZ3DiAlzAerGDbmM%2Bu6ieZu91%2F67edyVKDjescgFx7%2FGPYJSz3LW%2BGpup9w0yhcMx%2FiOc5ugTETyFC8FvWbMWxf67Qk2zhXuBpefoauVvmGfqpmizhgSNqOzXYFVe8EDeyjxPz6q3EsnyyUFk0HPUhr2%2FKjbRiOUQh2ck1Axexj0PrX%2Ft%2FQp7fT2siXTy3dSbWpimfUNHfk8jfPsmhAu1QsyEnZhLDnWwjQ2lpSf3ANiSlEr%2BDtvAN8yxZ01CkKf81kTVDKYAgCBgQL13J4a8lcvbxOvDuHD6j7syvUxjLbzaxy68%2BHZRRiqDaePX9%2BdUlL50yRz6iOlUpnAX64YDZUVZjclvmtEYTsC13KDo5GXe2uZ%2B5ePiwEGB%2B7Q4cUDD74zL2%2BrWvX3PnbDFuT4Eep6F0a4B3xlcSDfHQ8LMNTOnM0GOqUBVLFSLM9fVpQTnpBYQzrQN331LTLyKR1Y6eHAY90b%2FBdOWa2gZq1Z1LsiYdLp0QTyuEHZIb%2F4nmc3H9XCff6ilzGdFYDmglizh7BcMvf0oYQ25YFbaG9E8O4OMieCowvWyaP9No%2FkYKwrDz4lt%2BUjxnxTRxKlu5P8h%2FevgEOeIcuHEJmxWXMGN96yrWbVuW7zmgK%2BCDwje4yE17hoBuoUmZDm1dYM&X-Amz-Signature=5044a468433c5e426d78cb924380937996a0af589e43bd03ef984c25af29791e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







