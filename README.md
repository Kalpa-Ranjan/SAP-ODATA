



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THSXNX2A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T014844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOWEIRkn6sccMxYoCvzMDqQ54syZ7tfh0poY6f7w3z3AiEAzZpH9C0hVtiO1Q5Qtbto%2FECvt%2B40%2FP2kIeLflu1t4%2Fcq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDOus%2FI%2B%2BUpB%2FKSDxeircA2wwLEB%2BCbWWcVuy2nVGufATIguJJMKjv3K7jymxCUOAItMBEZ7%2F24lak5itnTVZTE6aoMHLQNZiKOXnseSjsSRPdSq4xkVAN1vSYS6KlU3QV4MRG09hU62pDjoZl51UZdv4T0AHP7B1O2SlQU2PCrxTXIZHepZjH%2BNO%2FjefwpDo8vJMElwfKU0%2FCE1miLV9hgZS5u8Uq4TMF15x5kpFE5Ro0WtuiWP2fmM3gWeAcj3OsCWqZ1K44OdVnGVkLCfVgrJuHGMAz0hwt1M5xAM7iS7PhwxT9%2BLS3hNJ7NBEk0%2FL8%2F6n%2FDPxmGtIyVZTxgmwCI69l5kt7xGXt1Hjtpkg4FpWF1evUUMb1aD9KmbV9PjIoEEwYCyHYfHLZFM5fDHAqfRxyj6sbtd91WWqCH3c4dNWgKLr5aUboArp1yllll56YxGNkNy9IFQpe8PPQTBwowBvuYf5dIFwOclGZBXcMtKEr0stsvZSVBj84b8xin1l8HwwjJSE3XJcShBrmRmnWZwQsPqBlgTcBq4gOYHNL2mR6Dw%2BTiS%2BVz4MJISH1iZ5UaxohyyOICXab8P6TAxvFxlTDAZJ2wUdom6UNcee5VIUYAUZkHDWqa2%2BPhjvPQOpvfetu2uL5F0KXr2%2BMITF2cwGOqUBZ%2B4G9ea%2BSy9iqatJF3Cd17HLTaOo7PpxC7wUcgR5PWY4OVBdNNpg%2F7t9NjFpuH8jH3j%2FfCht8pbKLsU0w9usx8tc8ybjcurBDesa%2F47GhcdBlRmB8034ANbCl4YYfEY6god3VkgpDIgS%2FHeGJIbSL6bTIOcp%2FW09FJCybLBUzStIgY%2F0NDzr%2FnEakdIgTYXokszS4BENTY4rqEs3zu4IVgsERN1r&X-Amz-Signature=639573efeac414e14214d2d28be446c5d9a3bbf87561529041da54151d0185f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THSXNX2A%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T014844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAOWEIRkn6sccMxYoCvzMDqQ54syZ7tfh0poY6f7w3z3AiEAzZpH9C0hVtiO1Q5Qtbto%2FECvt%2B40%2FP2kIeLflu1t4%2Fcq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDOus%2FI%2B%2BUpB%2FKSDxeircA2wwLEB%2BCbWWcVuy2nVGufATIguJJMKjv3K7jymxCUOAItMBEZ7%2F24lak5itnTVZTE6aoMHLQNZiKOXnseSjsSRPdSq4xkVAN1vSYS6KlU3QV4MRG09hU62pDjoZl51UZdv4T0AHP7B1O2SlQU2PCrxTXIZHepZjH%2BNO%2FjefwpDo8vJMElwfKU0%2FCE1miLV9hgZS5u8Uq4TMF15x5kpFE5Ro0WtuiWP2fmM3gWeAcj3OsCWqZ1K44OdVnGVkLCfVgrJuHGMAz0hwt1M5xAM7iS7PhwxT9%2BLS3hNJ7NBEk0%2FL8%2F6n%2FDPxmGtIyVZTxgmwCI69l5kt7xGXt1Hjtpkg4FpWF1evUUMb1aD9KmbV9PjIoEEwYCyHYfHLZFM5fDHAqfRxyj6sbtd91WWqCH3c4dNWgKLr5aUboArp1yllll56YxGNkNy9IFQpe8PPQTBwowBvuYf5dIFwOclGZBXcMtKEr0stsvZSVBj84b8xin1l8HwwjJSE3XJcShBrmRmnWZwQsPqBlgTcBq4gOYHNL2mR6Dw%2BTiS%2BVz4MJISH1iZ5UaxohyyOICXab8P6TAxvFxlTDAZJ2wUdom6UNcee5VIUYAUZkHDWqa2%2BPhjvPQOpvfetu2uL5F0KXr2%2BMITF2cwGOqUBZ%2B4G9ea%2BSy9iqatJF3Cd17HLTaOo7PpxC7wUcgR5PWY4OVBdNNpg%2F7t9NjFpuH8jH3j%2FfCht8pbKLsU0w9usx8tc8ybjcurBDesa%2F47GhcdBlRmB8034ANbCl4YYfEY6god3VkgpDIgS%2FHeGJIbSL6bTIOcp%2FW09FJCybLBUzStIgY%2F0NDzr%2FnEakdIgTYXokszS4BENTY4rqEs3zu4IVgsERN1r&X-Amz-Signature=b6fc054f57d7c6d35c243583eeeae3db296411e94497661e9a1651b7f83e8ed5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







