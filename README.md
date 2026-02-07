



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PVOKNHM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T014031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2TvbWP7%2BRakL1JopYHQzuRoYnI00k8h5ixjZw%2FotC7gIhAL0b1jAVbPWnPaAY7Gbc%2Fhn1iA0TcclnB8MIaPB5kxlVKv8DCFIQABoMNjM3NDIzMTgzODA1Igyy2jhjp%2FJnIZFHKS4q3AN7FJP0GwLm046clOs%2FBi3WXCZoSWz3aMVwVQkRExMTmOeU3g%2Bo8JhcQmns72Yj22FvlLkVFWjs8x2bqL%2F%2B165u6nXK75%2FBdETroc35gs4%2BmRbJ2cR2WoE5yOKx1M%2FnTW4wN3mMJB3I0cHvDX6NK%2FSXq%2BbCx8f5U21tRd85ApLorzleTToWkQF6GyrmPTxJ4vLqJTysIbn%2B%2FwBT9ybJC13Rh83UfAnTop8cC1CTMjoAJ1wzQVKmRkF64hoaKbxNgtyLTKPpd%2FyN1JWHRqfHI2bubciGeDI61E6N79zzs3J%2FoN%2Fbc5yoSnXGZhgVzp%2BfvNJKzuLU19c4kL4aiuOjc2OF4FnJh1CHhtEJToiaZE8JptWeS5lhAeHyP8lqsB6WYXRk9ZaGG1jjsbgGeGu9OrPGX3BzBjeSJga2vG1LyXCfCNx%2BsNBvuK6pA5x%2BU85WYA1SQ3RbfkpCGHlhSjBFzAe7TZUec0u4YmJFxT8schqhYODZbjwqZW6gKi%2Fz1Q%2FyhHq4AAik%2F%2BqbQ%2Bu0Vfdi1DFsrLHQcoNLJB%2BMWE%2F0JcVUFWU%2BMN30hO0E7sc2aFhFcxiLhaUOQBV92iCN83D1nF3bm%2BCsCdwH0aIPuaG6x8JTvykTlNcSrGRHxJEWaTDhpZrMBjqkAXAbWn2nD%2Bjd%2FUqHZF04xg%2F80XToiKZznD9F7lLfnptPKNWR%2Bk9G72ZHj3fDEvu%2Bj%2BzhKLf1VIb9d6ywF2fkqgYhQ7CbOpen7GDjRwvejC77D3RaS4aQPtVnVGgXOP7fbNA9A5YfVD4K7WXER%2BulD%2FOuRGKh9nbc3kmjz6ixTSTOw9lXvehJaf6CqDww9E%2BZxtPJkSKvcwpLVQb1xL5wqG5%2FYeW%2F&X-Amz-Signature=e42c45c20bcafacd0cae815a7f3f4d0a63e7334a158d2d3234a3a60cd799e56a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PVOKNHM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T014031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2TvbWP7%2BRakL1JopYHQzuRoYnI00k8h5ixjZw%2FotC7gIhAL0b1jAVbPWnPaAY7Gbc%2Fhn1iA0TcclnB8MIaPB5kxlVKv8DCFIQABoMNjM3NDIzMTgzODA1Igyy2jhjp%2FJnIZFHKS4q3AN7FJP0GwLm046clOs%2FBi3WXCZoSWz3aMVwVQkRExMTmOeU3g%2Bo8JhcQmns72Yj22FvlLkVFWjs8x2bqL%2F%2B165u6nXK75%2FBdETroc35gs4%2BmRbJ2cR2WoE5yOKx1M%2FnTW4wN3mMJB3I0cHvDX6NK%2FSXq%2BbCx8f5U21tRd85ApLorzleTToWkQF6GyrmPTxJ4vLqJTysIbn%2B%2FwBT9ybJC13Rh83UfAnTop8cC1CTMjoAJ1wzQVKmRkF64hoaKbxNgtyLTKPpd%2FyN1JWHRqfHI2bubciGeDI61E6N79zzs3J%2FoN%2Fbc5yoSnXGZhgVzp%2BfvNJKzuLU19c4kL4aiuOjc2OF4FnJh1CHhtEJToiaZE8JptWeS5lhAeHyP8lqsB6WYXRk9ZaGG1jjsbgGeGu9OrPGX3BzBjeSJga2vG1LyXCfCNx%2BsNBvuK6pA5x%2BU85WYA1SQ3RbfkpCGHlhSjBFzAe7TZUec0u4YmJFxT8schqhYODZbjwqZW6gKi%2Fz1Q%2FyhHq4AAik%2F%2BqbQ%2Bu0Vfdi1DFsrLHQcoNLJB%2BMWE%2F0JcVUFWU%2BMN30hO0E7sc2aFhFcxiLhaUOQBV92iCN83D1nF3bm%2BCsCdwH0aIPuaG6x8JTvykTlNcSrGRHxJEWaTDhpZrMBjqkAXAbWn2nD%2Bjd%2FUqHZF04xg%2F80XToiKZznD9F7lLfnptPKNWR%2Bk9G72ZHj3fDEvu%2Bj%2BzhKLf1VIb9d6ywF2fkqgYhQ7CbOpen7GDjRwvejC77D3RaS4aQPtVnVGgXOP7fbNA9A5YfVD4K7WXER%2BulD%2FOuRGKh9nbc3kmjz6ixTSTOw9lXvehJaf6CqDww9E%2BZxtPJkSKvcwpLVQb1xL5wqG5%2FYeW%2F&X-Amz-Signature=caa31c730796e143dec17f779cc6a594460f2349062bb9d67cd683e1a6cd08da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







