



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPBZTM26%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T065709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFNolIns9XoqlFShUvvQ7EpEm3PbXUDudcsVBoqF4qksAiEA0U9Q%2Bt4sZLdhqWMhsDkyaaPmLbr8eNBbzDwLWyruvJYqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC12piBVjnqH%2BNaIBSrcA2xFNN%2B106n5s%2BdbEreJOUvP58cV7SrCFscm5Nnh1iV7SE4XomfDLgsuvue%2BWMQNkT%2FdjLDiILNS5pSXOzyCFfZXul5xNu4JQoJ%2B0bBjUcx8zatqQFx1IAyvknTu6W642f9Wa7MiCT9gmYLSFC2wYUqsD96Th%2B0UrCJaoCOhh8CVJuLTbfRW878ua9sogMFEpTF2j6NTg5HgdVjp%2F5cf76rP9CrlgXGNej5sO0fZbZpWiuZmBgWtPcRid1gdI6hzUEfvBOT2afmna32xkSVLAxh5w4Fzm2wdlz%2BPlsbv4G2hWNur5QdpWTlH7TW%2FdpwT%2BIaST0da0xu96nf4sOpRIb%2BBQimmDgpNdbluSgVj8pYuEeNEyyQEAJ8G8W5YubG4HU2fl02Jok4uhOMOpnIYUVmFNCpqMNpJ7yo5Wv8eib0WJos3MeqwTI8vDHs0VQf23uuYEoh4qdERnFdMglMgCNpBeMsk725VXbzIxLbofJMG4byUVmt7XejFcfLjjvHdpMeP%2BF7YZSOSZdccOYbciR8iKh%2Bll%2FIYzcGblE88v7XDqaJJEP3Vorrjj0GY9mTuJTr4%2BfAr6dPhl3kGGnCABCKz8QIj31z%2BWni7cv%2FnL0ZZjYCQ0f7c4PKnrv5WMLLQ6tMGOqUBpKmDS27YwAdoFliPMgy5haZtW1K66ImhdpqzwUDwijvbhaJd3NM5g%2FgCYj11F2krxbZ2UO23FACZsn8KWoPnMY9djh3L8tCnxIgPhnEB8QYTI6ifmO942rhNEFjzk9zkPZjiIbDqh9aMPZK0flAzkPGYQbkJHc6mRCjgPqLcoc4cLZWdgVDLRHj1lSR7nak0A%2FBfsWVosbO8d%2FO%2FpNtqMuMix%2FKY&X-Amz-Signature=f3f5b2906ceed529e1c05bda65936d7c84ce6d62c5558f863bb96084ef80282d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPBZTM26%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T065709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFNolIns9XoqlFShUvvQ7EpEm3PbXUDudcsVBoqF4qksAiEA0U9Q%2Bt4sZLdhqWMhsDkyaaPmLbr8eNBbzDwLWyruvJYqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC12piBVjnqH%2BNaIBSrcA2xFNN%2B106n5s%2BdbEreJOUvP58cV7SrCFscm5Nnh1iV7SE4XomfDLgsuvue%2BWMQNkT%2FdjLDiILNS5pSXOzyCFfZXul5xNu4JQoJ%2B0bBjUcx8zatqQFx1IAyvknTu6W642f9Wa7MiCT9gmYLSFC2wYUqsD96Th%2B0UrCJaoCOhh8CVJuLTbfRW878ua9sogMFEpTF2j6NTg5HgdVjp%2F5cf76rP9CrlgXGNej5sO0fZbZpWiuZmBgWtPcRid1gdI6hzUEfvBOT2afmna32xkSVLAxh5w4Fzm2wdlz%2BPlsbv4G2hWNur5QdpWTlH7TW%2FdpwT%2BIaST0da0xu96nf4sOpRIb%2BBQimmDgpNdbluSgVj8pYuEeNEyyQEAJ8G8W5YubG4HU2fl02Jok4uhOMOpnIYUVmFNCpqMNpJ7yo5Wv8eib0WJos3MeqwTI8vDHs0VQf23uuYEoh4qdERnFdMglMgCNpBeMsk725VXbzIxLbofJMG4byUVmt7XejFcfLjjvHdpMeP%2BF7YZSOSZdccOYbciR8iKh%2Bll%2FIYzcGblE88v7XDqaJJEP3Vorrjj0GY9mTuJTr4%2BfAr6dPhl3kGGnCABCKz8QIj31z%2BWni7cv%2FnL0ZZjYCQ0f7c4PKnrv5WMLLQ6tMGOqUBpKmDS27YwAdoFliPMgy5haZtW1K66ImhdpqzwUDwijvbhaJd3NM5g%2FgCYj11F2krxbZ2UO23FACZsn8KWoPnMY9djh3L8tCnxIgPhnEB8QYTI6ifmO942rhNEFjzk9zkPZjiIbDqh9aMPZK0flAzkPGYQbkJHc6mRCjgPqLcoc4cLZWdgVDLRHj1lSR7nak0A%2FBfsWVosbO8d%2FO%2FpNtqMuMix%2FKY&X-Amz-Signature=3c7987ae81f6cc2df5cd81b2ad4eaeeb72454083b5ac3d93ca6463927734d478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







