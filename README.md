



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY565KJG%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T190845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQD7kKhfoiTmRxLNwLXODjgkNzn8WKsjK7hUGRsY41%2BFWQIgCn%2BXhLT61VkSy0CenQBRBHKSzcuBIzy19pSN23qEOJ0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDCuv4YHCKSAsWQyFKircA%2FB6v3qo6nn872QbNOL1fXhFImxhprApyshWLsnO4TmQf1KUhYC7Nv3HO7WTWYPbZahJrBoRIRfS5WhJuACfXxQ7xBoiXXS9QNmrLJ%2B9IhIA%2BEMBzxUPuxD7EcG21NAloLHXddgmterdTFR5LdVRVtnPCjwDzVWEmu%2FdE4GFat3pyi%2FeoNviUXKf8cOtOxKpDwZAk8MjlFPAfdkJoDybZalZjG70AnRSBLdDSaCvBQasOyOvZWjdlXq6S%2F46FGwf90ClsJGoKNkm6JpA%2FAWRtmcOz4gFbDRmWH%2F3xXHJLeLL3yjs81Uk9JHLfECyrPHqTi8OkzRTfo%2BNBiT8UjwojIL8rzI7TP7SCm%2F2sTo1w7GrbBt3RbwbEgFCa1XuqYxoZ4otBG5ArFPrPX6SoHHh8N2qzCukcdZx%2BZJDEGcDF%2FbMvvsX%2B9Z%2Fv%2BCcZ0G20veORGJSiPtn6ZqplNc3YrDS0yL%2BcE619PyxOmyNq21iSS%2FJoXZwUgYXkkY2h8%2B4l958WkKK2OBVofR%2Ft13trFnjQy36CQzwwdHVchzYkRFFgwU2ZoGUmgzKP5Sx5RUA2%2BUOXWHtxKuRcHaEl2toGqfCIxo%2FJdso3C3EIdEito2l4kvptfo0nOrmYcF53NLBMObI2s4GOqUB8rtCyRUek0hot6HWyVUgcr3BxhPVnedUs4iCcSlcbiBV%2Fl0s76zeMNLLumGPB%2F3dkYe9S8A5cul53Xbz25lYRo8RMPwA3%2B%2FGcNYlebaIZgSltwXJuNqiCIVextWLpQtoOarSildNlTZjp4V3jg8nJGbrd88N5QX%2FseyBrXw6EK2O7hkMhBGooMKMeegQiN13PDGsFfMLplNRpqzhLlmvhtRvYPr5&X-Amz-Signature=c74f06fac5f93ccdd576453668c48fed1fc14bbe216c0642db0d34701de06644&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY565KJG%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T190845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQD7kKhfoiTmRxLNwLXODjgkNzn8WKsjK7hUGRsY41%2BFWQIgCn%2BXhLT61VkSy0CenQBRBHKSzcuBIzy19pSN23qEOJ0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDCuv4YHCKSAsWQyFKircA%2FB6v3qo6nn872QbNOL1fXhFImxhprApyshWLsnO4TmQf1KUhYC7Nv3HO7WTWYPbZahJrBoRIRfS5WhJuACfXxQ7xBoiXXS9QNmrLJ%2B9IhIA%2BEMBzxUPuxD7EcG21NAloLHXddgmterdTFR5LdVRVtnPCjwDzVWEmu%2FdE4GFat3pyi%2FeoNviUXKf8cOtOxKpDwZAk8MjlFPAfdkJoDybZalZjG70AnRSBLdDSaCvBQasOyOvZWjdlXq6S%2F46FGwf90ClsJGoKNkm6JpA%2FAWRtmcOz4gFbDRmWH%2F3xXHJLeLL3yjs81Uk9JHLfECyrPHqTi8OkzRTfo%2BNBiT8UjwojIL8rzI7TP7SCm%2F2sTo1w7GrbBt3RbwbEgFCa1XuqYxoZ4otBG5ArFPrPX6SoHHh8N2qzCukcdZx%2BZJDEGcDF%2FbMvvsX%2B9Z%2Fv%2BCcZ0G20veORGJSiPtn6ZqplNc3YrDS0yL%2BcE619PyxOmyNq21iSS%2FJoXZwUgYXkkY2h8%2B4l958WkKK2OBVofR%2Ft13trFnjQy36CQzwwdHVchzYkRFFgwU2ZoGUmgzKP5Sx5RUA2%2BUOXWHtxKuRcHaEl2toGqfCIxo%2FJdso3C3EIdEito2l4kvptfo0nOrmYcF53NLBMObI2s4GOqUB8rtCyRUek0hot6HWyVUgcr3BxhPVnedUs4iCcSlcbiBV%2Fl0s76zeMNLLumGPB%2F3dkYe9S8A5cul53Xbz25lYRo8RMPwA3%2B%2FGcNYlebaIZgSltwXJuNqiCIVextWLpQtoOarSildNlTZjp4V3jg8nJGbrd88N5QX%2FseyBrXw6EK2O7hkMhBGooMKMeegQiN13PDGsFfMLplNRpqzhLlmvhtRvYPr5&X-Amz-Signature=196a68066138d17f7a25b8e591a8147654054dfb144396c4f9f068372a9e1a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







