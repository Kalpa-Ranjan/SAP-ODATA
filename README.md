



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTB3R7P%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxc3w1DlHOivjIVrgqT0aTB7SJPMISkataq%2BmzH7CWZgIgBuPzipkmPfMPEIIR7GMRicmgNpaVTXC1MGV%2BhDZopzkqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJiK9ug7vBkdglE%2FwSrcAwR8NvuLFDW%2FKf6tnN3G48UC2ioZDznb1AWgkBxM%2BwAdI4dCkRkdiHp8yygeRRQV9NqWcQBafw35PT4glTbR8u6LN7fRKn%2FFr12duHPtMXYrwHGFjaqXmvtwz3PPz3ucjMumlhaaULJkb75DPvsuBx%2Br4LbW%2FEa0bmV6Mcjo%2B16NaFnvnMyD7d0ZOKSoNMMxJogbzEEk0Qa23g8zti6BTLnTPCPoKHwQ%2FDxPDYlSooayOhnD7KfV%2BYyyqeQvBKoAUhEtuiM%2Fxb8gJHHakShZ9PyPM3JDFZacWY4lIf7SOnPV1PIc60rz2T4ZKgijqIz2bWLzyOY31%2B7KPggb3AbGVRFuITB4Q1gWbcF5yrMi7Ji%2BBPu7ZlH%2FQw9HLMORocPldoT6ZNESQkV9rJryu4TuNd7wjoz7uhnC2nVUQyxfSats8azZDmvKxYjyhhWa8CQrfCGl6JfQrzjiOUhfeRyYSG3pcETvvW%2B6i6v%2Fkk8yTw8XaP3BuQK2OVwhOsIsTAuSdSbGi3vcWM4jCG4qNwqNyufivAFqiPK6MUXg3UooEe131QfC6AAHhwqlPnMjIeFRCXvhGbsMrOpVHyKwkvi%2FJV9w0tZWzfKWD05HX62pkvEdsGK4Dc8%2F%2BzoIAblfMKX1pMwGOqUBCHTsz1SkpLNCHNI5wFD%2FNsFIz4OJWPfV%2FBwVj6g1q05FV3GtAWHvIwTQ0LRWi2kl5jstVXid7w4WRYoJw9pC6sIlSZeZ%2BNlyUrZNI2vgIiegPgdnwXXOt1JHkNbrCo%2BX3d%2BnP%2F0zlDs1Lry6KmSzkMeScwnMNkHzBzwHeARBeXJBiMm6FIArSJYETQsUjeukRyDrCPqANTzm5hc%2FXFB%2BC372wI8b&X-Amz-Signature=4a3e8e40d4c1c631b444276d474063d3b6059686b7173d814553e2a3d7020782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MTB3R7P%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T015026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxc3w1DlHOivjIVrgqT0aTB7SJPMISkataq%2BmzH7CWZgIgBuPzipkmPfMPEIIR7GMRicmgNpaVTXC1MGV%2BhDZopzkqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJiK9ug7vBkdglE%2FwSrcAwR8NvuLFDW%2FKf6tnN3G48UC2ioZDznb1AWgkBxM%2BwAdI4dCkRkdiHp8yygeRRQV9NqWcQBafw35PT4glTbR8u6LN7fRKn%2FFr12duHPtMXYrwHGFjaqXmvtwz3PPz3ucjMumlhaaULJkb75DPvsuBx%2Br4LbW%2FEa0bmV6Mcjo%2B16NaFnvnMyD7d0ZOKSoNMMxJogbzEEk0Qa23g8zti6BTLnTPCPoKHwQ%2FDxPDYlSooayOhnD7KfV%2BYyyqeQvBKoAUhEtuiM%2Fxb8gJHHakShZ9PyPM3JDFZacWY4lIf7SOnPV1PIc60rz2T4ZKgijqIz2bWLzyOY31%2B7KPggb3AbGVRFuITB4Q1gWbcF5yrMi7Ji%2BBPu7ZlH%2FQw9HLMORocPldoT6ZNESQkV9rJryu4TuNd7wjoz7uhnC2nVUQyxfSats8azZDmvKxYjyhhWa8CQrfCGl6JfQrzjiOUhfeRyYSG3pcETvvW%2B6i6v%2Fkk8yTw8XaP3BuQK2OVwhOsIsTAuSdSbGi3vcWM4jCG4qNwqNyufivAFqiPK6MUXg3UooEe131QfC6AAHhwqlPnMjIeFRCXvhGbsMrOpVHyKwkvi%2FJV9w0tZWzfKWD05HX62pkvEdsGK4Dc8%2F%2BzoIAblfMKX1pMwGOqUBCHTsz1SkpLNCHNI5wFD%2FNsFIz4OJWPfV%2FBwVj6g1q05FV3GtAWHvIwTQ0LRWi2kl5jstVXid7w4WRYoJw9pC6sIlSZeZ%2BNlyUrZNI2vgIiegPgdnwXXOt1JHkNbrCo%2BX3d%2BnP%2F0zlDs1Lry6KmSzkMeScwnMNkHzBzwHeARBeXJBiMm6FIArSJYETQsUjeukRyDrCPqANTzm5hc%2FXFB%2BC372wI8b&X-Amz-Signature=7432f4cd0449a4bd6d2e60c98b8ab581d15f0736b11e66445800fbd7ac9d24a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







