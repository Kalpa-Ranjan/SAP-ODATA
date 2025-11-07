



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNXDHGUM%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTwfLK03uPcrnEIAkhfJL%2BJREufPA1grbRCgcWHDtC5AiEAxctNgJWy4bRRXnfbdFAW8hX2juWO3mR7xwmpcx4jkcMqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCivEhDffAMXjiDOVSrcA3YpLkym4uLYy3wFiimuB9QjapNvyQJVZVXmawX8lOCNoWKsOcXUpvvxwJmJtHUxiCZxBP1%2BdbYTQEetSQqPmsZss53hbv1zxIcRx2NDccZLvrxC%2By7cHBQRlDMvhm%2FVB5Ry8xaAsphIJd272r%2BMtPXIyFCLLvBtdyqzHJ0%2F3wpgiVRd%2F2PmiDC8kW%2F8q%2FdEzlGG4i3XLrWqq6Vf%2BGCJ4HDuzfdbpACNSqUvK6xjoITgBdIHoOjqjpgu9nxihjcIukPl%2BhBzzNyUNieUWT%2FBDNxoXcNPXPOMR4iDC%2ForXv4p7I10QynYQRn0%2FqpIrNoG4rsF2rItuxUzy65eI64TORD3qmdWOXKWmpzHZMzMZfCUhbslKQbRvFzCw%2F9mEkijWDUwbomXf14wev%2FDUpRmsYRNxjy0uR110PLtOm%2BJUr2DXFjSrnKe9BATrUSWkic%2BP3FzLNwwazsph7JgOT438Wm43c4LtyOOB%2F%2FwBdmMlqGXpxA4md%2BoIhXLEjJiFqXS91NE%2FPiCPh2MqApIsoVWutEYNc7YNT6pjpjb%2Fk2Dv25BG%2FcCHHkQUmBPpzxAH4B9d7uY%2BpW4wx4iyVCjYpSiMRF%2FlE6IXo%2F8dv5C0xZHsPK9xaziD2u9YFLrQ4J7MJv4tMgGOqUBExPJpcNgjKAXZbJ5FB10K%2Bbxl8QVizE4BK%2BHxYiVYhjcg48E2ba1XU4SdxFFrUwYhX8gqjB5ym7v7WNnQh4%2B7shvjFsMdG0rXa97ij0ojtqOZDE56maF%2Bzhi5P29UDHmydpz6XI0t9UoIaMD9WZmm5x0uUFzn8ZbGjVro4lOVdIMdo9KLw0%2FJU9mda5G5UuX3kAPlt%2BTVwsZYd6sCt%2BZM09X48vo&X-Amz-Signature=e1d47e572e0504d7e033a2ceb3def28e5f8b652c64611ce47b93f9640fb54fe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNXDHGUM%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHTwfLK03uPcrnEIAkhfJL%2BJREufPA1grbRCgcWHDtC5AiEAxctNgJWy4bRRXnfbdFAW8hX2juWO3mR7xwmpcx4jkcMqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCivEhDffAMXjiDOVSrcA3YpLkym4uLYy3wFiimuB9QjapNvyQJVZVXmawX8lOCNoWKsOcXUpvvxwJmJtHUxiCZxBP1%2BdbYTQEetSQqPmsZss53hbv1zxIcRx2NDccZLvrxC%2By7cHBQRlDMvhm%2FVB5Ry8xaAsphIJd272r%2BMtPXIyFCLLvBtdyqzHJ0%2F3wpgiVRd%2F2PmiDC8kW%2F8q%2FdEzlGG4i3XLrWqq6Vf%2BGCJ4HDuzfdbpACNSqUvK6xjoITgBdIHoOjqjpgu9nxihjcIukPl%2BhBzzNyUNieUWT%2FBDNxoXcNPXPOMR4iDC%2ForXv4p7I10QynYQRn0%2FqpIrNoG4rsF2rItuxUzy65eI64TORD3qmdWOXKWmpzHZMzMZfCUhbslKQbRvFzCw%2F9mEkijWDUwbomXf14wev%2FDUpRmsYRNxjy0uR110PLtOm%2BJUr2DXFjSrnKe9BATrUSWkic%2BP3FzLNwwazsph7JgOT438Wm43c4LtyOOB%2F%2FwBdmMlqGXpxA4md%2BoIhXLEjJiFqXS91NE%2FPiCPh2MqApIsoVWutEYNc7YNT6pjpjb%2Fk2Dv25BG%2FcCHHkQUmBPpzxAH4B9d7uY%2BpW4wx4iyVCjYpSiMRF%2FlE6IXo%2F8dv5C0xZHsPK9xaziD2u9YFLrQ4J7MJv4tMgGOqUBExPJpcNgjKAXZbJ5FB10K%2Bbxl8QVizE4BK%2BHxYiVYhjcg48E2ba1XU4SdxFFrUwYhX8gqjB5ym7v7WNnQh4%2B7shvjFsMdG0rXa97ij0ojtqOZDE56maF%2Bzhi5P29UDHmydpz6XI0t9UoIaMD9WZmm5x0uUFzn8ZbGjVro4lOVdIMdo9KLw0%2FJU9mda5G5UuX3kAPlt%2BTVwsZYd6sCt%2BZM09X48vo&X-Amz-Signature=d5f8bd5ce4867ce5c5c5c1b0087a11e560e26437e74a014525f0650b7677a74f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







