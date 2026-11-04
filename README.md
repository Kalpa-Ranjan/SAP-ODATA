



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CM2WQY4%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T060801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAclCJEBgJq8WSjzT%2FVV%2BOzUY4RaW67nzOTprb8xWIdPAiEA2rVRcBLyDpBzb%2BUshZgtSsnRlyYDDdFpQsOhBGSLMnYqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFBVMWT0h1oNsrYLSrcA%2B8P%2BNS9RvML6VxIEvT7ja5CvJKMXRnWb89LGpOr50irbqcx4Q30tYn6axpqwdXj5lWaCa17N90PMLTp4%2FI9ERIjCAYQxU0On0W0hQ7Xs%2BBaMd5wTfmUzF2YVFHF6c3oDg2suUrzYlVzrj2Nk%2F9p9ZJDP5XuOZNp1vSmo72yh7A3RMa3JoTa033UwpeAiNP6VWWssG8j96R3sCmyK7T%2BvwcTEIcuDogop7jUHhWKrhaX31FtxsP6I1kRq%2BbZSMKBES%2FV3NrdL1qWHoJWkPp4CQtPbHQC61Ibd2tf3xs2tEqS9vUs%2BQh09kVtNqOYrsuwBp6%2BZeVfuQ8zaPc9B9r9Gb0N5Xw%2BIFc%2Bzl3go2GcWaJ3zJzAzkZRAB4ZDZaU96GbNpPEPNzemIS1pOOKg9DZKB3Koa8%2FpP0Gg94v7KnvRtDmTm3K%2B7zXJ9U%2FVx%2FHOh%2BE1MYqNPB9Kbqylf6QKJwJWpYLsqdaY3kB7S3WP%2BkAOak9FFJrNk4N0lu0IldV3s3iPtH5%2FMeumwR1%2FsYR%2FyUDVLSLzwPvkxltcFpDy1XIgajclPSzSABZ8gy%2FZ5O1cEce0G8T%2B7WmD5yNC94t7GBNsB9fcOYSwhDD1XM9PtMlnEPmEQDIrY27eHiMgeJoMOKOq9cGOqUB6LPpV%2Boyy9knF%2BLcuGar47d99jPDj1JMo%2BZtonLif%2BT%2B4eq9%2BSuC%2Bi1tKP1qrqvuOkKt0jMbhgoGCx5LD%2B3C4vHtnb7fvoOaTkCUQxLyacq02x5qsgt0cuZqzaFUDzdEok3ajrDUfOe5ZVZRSD5amEI4eKPiRF2uvLXxkG%2BWJSR8a9fL4joxrxbqB4xGrCmKLfz3ZCd6ifpwyKnwDQWV6QcnHaSz&X-Amz-Signature=1d98d7c8a3e3051103880fd1d6339b403dae1a6fbac05e857426857f9fb65514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CM2WQY4%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T060801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAclCJEBgJq8WSjzT%2FVV%2BOzUY4RaW67nzOTprb8xWIdPAiEA2rVRcBLyDpBzb%2BUshZgtSsnRlyYDDdFpQsOhBGSLMnYqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFBVMWT0h1oNsrYLSrcA%2B8P%2BNS9RvML6VxIEvT7ja5CvJKMXRnWb89LGpOr50irbqcx4Q30tYn6axpqwdXj5lWaCa17N90PMLTp4%2FI9ERIjCAYQxU0On0W0hQ7Xs%2BBaMd5wTfmUzF2YVFHF6c3oDg2suUrzYlVzrj2Nk%2F9p9ZJDP5XuOZNp1vSmo72yh7A3RMa3JoTa033UwpeAiNP6VWWssG8j96R3sCmyK7T%2BvwcTEIcuDogop7jUHhWKrhaX31FtxsP6I1kRq%2BbZSMKBES%2FV3NrdL1qWHoJWkPp4CQtPbHQC61Ibd2tf3xs2tEqS9vUs%2BQh09kVtNqOYrsuwBp6%2BZeVfuQ8zaPc9B9r9Gb0N5Xw%2BIFc%2Bzl3go2GcWaJ3zJzAzkZRAB4ZDZaU96GbNpPEPNzemIS1pOOKg9DZKB3Koa8%2FpP0Gg94v7KnvRtDmTm3K%2B7zXJ9U%2FVx%2FHOh%2BE1MYqNPB9Kbqylf6QKJwJWpYLsqdaY3kB7S3WP%2BkAOak9FFJrNk4N0lu0IldV3s3iPtH5%2FMeumwR1%2FsYR%2FyUDVLSLzwPvkxltcFpDy1XIgajclPSzSABZ8gy%2FZ5O1cEce0G8T%2B7WmD5yNC94t7GBNsB9fcOYSwhDD1XM9PtMlnEPmEQDIrY27eHiMgeJoMOKOq9cGOqUB6LPpV%2Boyy9knF%2BLcuGar47d99jPDj1JMo%2BZtonLif%2BT%2B4eq9%2BSuC%2Bi1tKP1qrqvuOkKt0jMbhgoGCx5LD%2B3C4vHtnb7fvoOaTkCUQxLyacq02x5qsgt0cuZqzaFUDzdEok3ajrDUfOe5ZVZRSD5amEI4eKPiRF2uvLXxkG%2BWJSR8a9fL4joxrxbqB4xGrCmKLfz3ZCd6ifpwyKnwDQWV6QcnHaSz&X-Amz-Signature=4f217b9a60ed802ab531cee85cd885aad20a9ea41ccd75cfe2ce4388a3238f0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







