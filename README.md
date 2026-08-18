



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQCEX7P%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T063323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeYAvmREC%2Fde6F6Vcco1gFwbys56C2CoS5SbIe%2B6xlLAiEAk%2F3uNfarpol3EcMwjAAEonqvep%2Bt1xr8yoBUdNHUt%2Bwq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDP2e67yybujaxV3mpSrcAwsteWec%2Bru4zrJ66idf26vT%2BnlUBYEsHrhFg95gn9um1NYmhZ2S4bkdl6Rjn%2FESM7IETwGG9a6sd%2BdjbcXXO5CwI0MMEMKEK%2B3tro%2Ft5B%2BxvFCFqSlanJjW8G48hENRpD4pCdJuK2z8VRk6Swersq9KoZ4Lm8S7jIQnvQekxTZVANNnLNha8ivCkimTfYtalZNZ56IC0DaHsZuDIjfCiCakz9vrKEVNQUg2M%2BrJKijM%2FzwS6xe4dM0krgP4HO41WRAH%2F496Dl98%2BEHSZAG%2BqyjN9taGOgO9VqvBoaRBq6wk4ThsuB6DFEOs%2F4jvG1j3c%2B7NZUV1q2T%2B9WfIqGXHterT3e9hKf2Wz36XZCf%2FE3fpfjvyEm6NY3PJVG5pV3XOHv8xncz6ah4Q4pqmxmOkv7mfh7KKbqHontwgsCyUaAr3sMpfFT6ekc8P4jCL77o3qUPeUxPYiHgzHCAMu%2FwbFYa5cRbShy20xzerPojiTKDIOoHCD0hccQErp6xNtKrv%2FH65A%2F74VNgcrijzfpxeByugSxZUPSztfA0HAw7sVknm0N2nXX6fLsQllBGxYXgcaj%2B0y%2Fe2hyfhpZM%2Fy1hnmSWjgIdna8MIWwug%2BSRYGFJBXUjshijZBC2fTWDSMLCzj9QGOqUBIfPEDgFvSmx6rrNhHPAMo96VCROwl4sctlND4VKu7O0GX0dMCEJXAI8nuACnL%2FwkAmXQVDSypHglYv%2FXMrMSANGpkqf2lVhn3aF7sNSCIaVeLAGI0Vx9AHcPpGqQnDhm5OE0kNYCEsbElCWfuft4yfJ2QUEs95uuP16sUaLh2JOcQWu2xGK%2FTBmx6udtHtxy%2BGFBXTyDfdRdwV22IWxipUXp2BZ5&X-Amz-Signature=ed8583d73d2fe485f5b7471338144595459ca4ae658b64a40f7ef344e757e2ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQCEX7P%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T063323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICeYAvmREC%2Fde6F6Vcco1gFwbys56C2CoS5SbIe%2B6xlLAiEAk%2F3uNfarpol3EcMwjAAEonqvep%2Bt1xr8yoBUdNHUt%2Bwq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDP2e67yybujaxV3mpSrcAwsteWec%2Bru4zrJ66idf26vT%2BnlUBYEsHrhFg95gn9um1NYmhZ2S4bkdl6Rjn%2FESM7IETwGG9a6sd%2BdjbcXXO5CwI0MMEMKEK%2B3tro%2Ft5B%2BxvFCFqSlanJjW8G48hENRpD4pCdJuK2z8VRk6Swersq9KoZ4Lm8S7jIQnvQekxTZVANNnLNha8ivCkimTfYtalZNZ56IC0DaHsZuDIjfCiCakz9vrKEVNQUg2M%2BrJKijM%2FzwS6xe4dM0krgP4HO41WRAH%2F496Dl98%2BEHSZAG%2BqyjN9taGOgO9VqvBoaRBq6wk4ThsuB6DFEOs%2F4jvG1j3c%2B7NZUV1q2T%2B9WfIqGXHterT3e9hKf2Wz36XZCf%2FE3fpfjvyEm6NY3PJVG5pV3XOHv8xncz6ah4Q4pqmxmOkv7mfh7KKbqHontwgsCyUaAr3sMpfFT6ekc8P4jCL77o3qUPeUxPYiHgzHCAMu%2FwbFYa5cRbShy20xzerPojiTKDIOoHCD0hccQErp6xNtKrv%2FH65A%2F74VNgcrijzfpxeByugSxZUPSztfA0HAw7sVknm0N2nXX6fLsQllBGxYXgcaj%2B0y%2Fe2hyfhpZM%2Fy1hnmSWjgIdna8MIWwug%2BSRYGFJBXUjshijZBC2fTWDSMLCzj9QGOqUBIfPEDgFvSmx6rrNhHPAMo96VCROwl4sctlND4VKu7O0GX0dMCEJXAI8nuACnL%2FwkAmXQVDSypHglYv%2FXMrMSANGpkqf2lVhn3aF7sNSCIaVeLAGI0Vx9AHcPpGqQnDhm5OE0kNYCEsbElCWfuft4yfJ2QUEs95uuP16sUaLh2JOcQWu2xGK%2FTBmx6udtHtxy%2BGFBXTyDfdRdwV22IWxipUXp2BZ5&X-Amz-Signature=ba9930bc555bdaf0e276051ecdf182d8944a99c77cd9da07878123cd5de48ecf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







