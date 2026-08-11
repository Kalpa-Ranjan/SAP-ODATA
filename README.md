



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HXEWNHS%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T011602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa2sphINyjoVncvpU8XFGRj%2FxgxbIWbUyV1hsBq1LmiwIgHCyKXmpn%2BYrdVRJA3NEQLF7WzsQ%2FhB0mzcvtNA1CaukqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1TcfvDiavzXbeBnircA7%2FHxqZkCQSGMHWT2mFeWKgvdUp%2B8XIpP1mPy8569hgQr%2BWa%2F2tsyWDjl3eIlsn2%2FbWFqiwcEu6bHgaaGePV46C0MIYBb8eHXnECoM0m83zFPrGVQ3V4u13vK7HqvHsA209NGU9rUHF39C3NdvUv%2Bze%2F1Jp9V2KwsVNFXwukLVcam9iwZm4oNjtU%2FjTaW66Q617O5IRxKyO6a26KiBtZNp8MrEhdGnIk7cbRn%2Bn60c9ptneOAr%2BDCpjoWPdFHju03zECodAkVK%2BkdIgB%2Br0sN1Hc%2F43Wxke%2BzFNOAuxv6bY3eh0lLwnYIhXpoM2QA3GmRhQeSBoWzd9UfYXNHehcvxK%2BjqLkJhvM14WNZARxIwM9Fe2vQBsPTPfcxD%2BE5PRCbgGEccLW8j1k5lbEjruUm50TAyBVj6ziXyICKfVT%2F0NomeK8lwdXMYGvbYJ6%2Bj1HfGAom9cr3UT%2BpIO4AcHzJFLha6dIAhcUf17ivhx9%2BRU8p8kCNBB5NJLontGvXBfjImnfcR%2BRthmZLZEfP0UksL1bFyQMZY9q5hxQZ%2FGdxY2fQ87c0Mu3Xca6NgcX2o1IaYDQhxNtFIv9NgK0vTE8w9b8j3wLYFDS8swKzubfB7gnjjGNgHVCVS%2B34GFHMO3b6dMGOqUBeKfXsFZVNSB03NDb9aSdqHViwdBZmJUt7%2FH1e%2FXAlp0SWWJtshXEEiXlyaQwFs39TCKfYOf6FKDTr0zP6BDOd4M9BEaT699jFvhzncBtXm%2BTm4tbStC0H%2BZJCynIn%2BOMM%2Byqj%2BFmH1KmHfzRgmyNdY7xfdHcNDWhXOqDj15CLjZM2ANDy%2FtxLuJ9nX%2BD%2BGOBUL8LkrXyO0YewORvQxy6rA83BzcV&X-Amz-Signature=fe7d7e1efc6c7c6451035c7ff1258871ff7c3088acb574e59683f551dd4901ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HXEWNHS%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T011603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa2sphINyjoVncvpU8XFGRj%2FxgxbIWbUyV1hsBq1LmiwIgHCyKXmpn%2BYrdVRJA3NEQLF7WzsQ%2FhB0mzcvtNA1CaukqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1TcfvDiavzXbeBnircA7%2FHxqZkCQSGMHWT2mFeWKgvdUp%2B8XIpP1mPy8569hgQr%2BWa%2F2tsyWDjl3eIlsn2%2FbWFqiwcEu6bHgaaGePV46C0MIYBb8eHXnECoM0m83zFPrGVQ3V4u13vK7HqvHsA209NGU9rUHF39C3NdvUv%2Bze%2F1Jp9V2KwsVNFXwukLVcam9iwZm4oNjtU%2FjTaW66Q617O5IRxKyO6a26KiBtZNp8MrEhdGnIk7cbRn%2Bn60c9ptneOAr%2BDCpjoWPdFHju03zECodAkVK%2BkdIgB%2Br0sN1Hc%2F43Wxke%2BzFNOAuxv6bY3eh0lLwnYIhXpoM2QA3GmRhQeSBoWzd9UfYXNHehcvxK%2BjqLkJhvM14WNZARxIwM9Fe2vQBsPTPfcxD%2BE5PRCbgGEccLW8j1k5lbEjruUm50TAyBVj6ziXyICKfVT%2F0NomeK8lwdXMYGvbYJ6%2Bj1HfGAom9cr3UT%2BpIO4AcHzJFLha6dIAhcUf17ivhx9%2BRU8p8kCNBB5NJLontGvXBfjImnfcR%2BRthmZLZEfP0UksL1bFyQMZY9q5hxQZ%2FGdxY2fQ87c0Mu3Xca6NgcX2o1IaYDQhxNtFIv9NgK0vTE8w9b8j3wLYFDS8swKzubfB7gnjjGNgHVCVS%2B34GFHMO3b6dMGOqUBeKfXsFZVNSB03NDb9aSdqHViwdBZmJUt7%2FH1e%2FXAlp0SWWJtshXEEiXlyaQwFs39TCKfYOf6FKDTr0zP6BDOd4M9BEaT699jFvhzncBtXm%2BTm4tbStC0H%2BZJCynIn%2BOMM%2Byqj%2BFmH1KmHfzRgmyNdY7xfdHcNDWhXOqDj15CLjZM2ANDy%2FtxLuJ9nX%2BD%2BGOBUL8LkrXyO0YewORvQxy6rA83BzcV&X-Amz-Signature=7d80fc336936475504edaa220ac856e1beb31dc9c9cf1fb3c58ff42f01b11fc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







