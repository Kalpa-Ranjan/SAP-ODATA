



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5HCXIJN%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2F1fPXcn1Bo2Lo3X05wXi4obDJ4bY5T6NgBnOhrUt2SAiABDl4cbzrTzvwAy4%2BSWjVnwX07K1q0%2FbDhf9ia8n7FcSr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMTyQvA6u%2Bp2eYoSDNKtwD0yEWqJCu7IBPCP13sEMp6TEp3gxCgxhMKjD2qaHwGII%2FJr4c3coTRU%2B7R7%2BzinNWBdsrlwsdeMRNgoH1vNZMs6cMbCqb2YlkoBILOtw7xzmL1WFLBc4Db1kqlqOntaKA1DYCZxdRHjFsy4%2Fr06tuoIsIZIYdYgRvnAxvX5HMPlXR9tXrTnvxsrp4eagZFlme%2FD1Js%2FDkIa8KSKlXLR9QykdenW%2BW%2BxUr1b246B19uOWgMBwC66VNyztKzERFhxYWyi2JgNNxEiCVbphfXOD6eWo6mgKfnoUkGPnMpY3qnc8o3IqYjxrVHSstUTPb2Ul%2BVE4tc5DxpaCCN6gNVeld7qqJj9KwPn47EFyf3g03YzfCad9lbSPR6NnQzS2ivY5nvBCsP9G55b3wI6Z%2Bd1AzVKlw%2FKAUmIy4mL2ku6glhM7fVA0Y1BUtTPPAlqnLfs4NtvYZvSv66TDqTuqz%2BOdqqAbZG6lmYCdU7hFKjiOzv%2F%2BWjvFCR8IDx912MbyVr6OFfoONrUJlexWzDgRHPwbkPqoYvNNne87G8cGmVNAhwb75gGdw6Zc7MyxvtGJENAuS11BC%2B8ec%2FPtl4UHvm7NF2EtHOV7iAiNhHi9dQa4QbJpLO7Yo%2F5LePmqZN7kwjoOzzgY6pgHedWYOeOJiFo%2BOKFpMS9L4jR1W4I8qcG7%2FQW34LRptE%2BZ5Q2RE4rC0Qpsd9ut%2BI%2BVVpHWaHb0JZefb1I0MTFeBeeIHSZYlFyR1%2FE2Yxpy6Y6H2QWeQwEIu%2BvkAJMq1CU9wAYeoiy%2BB7N1YaAA6lRZ2nHLdBri9ho5cpa3u1iCHzqh8WVy4LwdqL2GXIEBiosxUDCOxV5hrzhsEvb2X79i8FZXyA8AK&X-Amz-Signature=26e2d9b21385b91554876958843a1dccee24fb7edee482a1622aef1a01220e7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5HCXIJN%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2F1fPXcn1Bo2Lo3X05wXi4obDJ4bY5T6NgBnOhrUt2SAiABDl4cbzrTzvwAy4%2BSWjVnwX07K1q0%2FbDhf9ia8n7FcSr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMTyQvA6u%2Bp2eYoSDNKtwD0yEWqJCu7IBPCP13sEMp6TEp3gxCgxhMKjD2qaHwGII%2FJr4c3coTRU%2B7R7%2BzinNWBdsrlwsdeMRNgoH1vNZMs6cMbCqb2YlkoBILOtw7xzmL1WFLBc4Db1kqlqOntaKA1DYCZxdRHjFsy4%2Fr06tuoIsIZIYdYgRvnAxvX5HMPlXR9tXrTnvxsrp4eagZFlme%2FD1Js%2FDkIa8KSKlXLR9QykdenW%2BW%2BxUr1b246B19uOWgMBwC66VNyztKzERFhxYWyi2JgNNxEiCVbphfXOD6eWo6mgKfnoUkGPnMpY3qnc8o3IqYjxrVHSstUTPb2Ul%2BVE4tc5DxpaCCN6gNVeld7qqJj9KwPn47EFyf3g03YzfCad9lbSPR6NnQzS2ivY5nvBCsP9G55b3wI6Z%2Bd1AzVKlw%2FKAUmIy4mL2ku6glhM7fVA0Y1BUtTPPAlqnLfs4NtvYZvSv66TDqTuqz%2BOdqqAbZG6lmYCdU7hFKjiOzv%2F%2BWjvFCR8IDx912MbyVr6OFfoONrUJlexWzDgRHPwbkPqoYvNNne87G8cGmVNAhwb75gGdw6Zc7MyxvtGJENAuS11BC%2B8ec%2FPtl4UHvm7NF2EtHOV7iAiNhHi9dQa4QbJpLO7Yo%2F5LePmqZN7kwjoOzzgY6pgHedWYOeOJiFo%2BOKFpMS9L4jR1W4I8qcG7%2FQW34LRptE%2BZ5Q2RE4rC0Qpsd9ut%2BI%2BVVpHWaHb0JZefb1I0MTFeBeeIHSZYlFyR1%2FE2Yxpy6Y6H2QWeQwEIu%2BvkAJMq1CU9wAYeoiy%2BB7N1YaAA6lRZ2nHLdBri9ho5cpa3u1iCHzqh8WVy4LwdqL2GXIEBiosxUDCOxV5hrzhsEvb2X79i8FZXyA8AK&X-Amz-Signature=3d9ee446e0beb16f2fc1369a54b841ee6263001562351ab907becd8d0244112f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







