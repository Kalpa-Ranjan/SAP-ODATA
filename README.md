



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZSH2W4Z%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T181953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQDksxrnkqPDaflwv%2F0RngZ8AcwXUvJU90%2Bte%2BHzXCfqSQIhAIe66bmXEkR173DaWCFt5uI1KeipBdMh3Sz%2F6O3OtkdLKv8DCBsQABoMNjM3NDIzMTgzODA1Igy86yb5%2ByenpVPwQkgq3ANloltAaGogmGbK9vXXnvUdkfHeZJ9Qs1%2BsS3Kkhaxqopf0sMVCDO2yIQIbInNTJXdw1pypyNkAndMxsbYMTx4T9eQzlSbVfRbTA69itI%2BNu0XmOMYe3ey3cccRmPKQVNIrhMxd99RXCj7Y3YBYEjBiCBhn1kQTN9RLWmt1mLLd7IYNOhiFfE3sjUOq9wTFln%2FUOEIc89AuzOgGYaBkOvn%2Fth4TUI3aSoPchNnK4NyZ%2BpUHdlMxfaolyL4v0%2BCin4CCUeavV2q8PMTUUG7jvsK7glbLwHlG%2B8hOtZvdYRu86Q4xihbQw10Eq8d4CL%2FBmRl1aTFCgMBENC3iWwm1wwgT%2F5zEIefuyyUNYoOyNt9Amx2D9bHnzhR5aCoicb9qs6b%2Fado0%2BsBzZXK2EsANl5aO6ETFiOI6GCgcwPJiOGHOYCYZqdaX74HJtrYwRgCG9cadR%2Bfezvc6WdziaOPpC3OhaBEgb7dR6%2F3ZDoPorjb1Cgeo4Fyk4%2BaqYqy07m0fJvELxnW7993I5zjwqO2LX8LoFuHStgF9vIEktIPsx7JqIIbEhvPZ71x3lb34B1ct3osN6iyacC5fvd6O%2B%2FabJeO0DjvVERiy3Tpv0C0LuVRJuXyiy3hV99Tv2J2jeDCayILUBjqkAfpf7%2F50hypq%2BEkZci9xWG7D7xZKb4LS%2FZ4MQjXFeBJusBlRx8yIrL6pxMvSat1FZ3%2Bxg4sbCkdmaKmfTT6%2BJ4PjXMh%2FnS4MZLTIZ%2Bj1JAG%2BwFBksnp7v3Acl5%2FGUWp6%2FG37OiDe%2FheftytY5%2F1LVsPu%2BH7ifI41jR8BQKeMM384VScykpjFVj%2FLjLCFMF2fItqtf4oo69erwkTy%2FmJG44ylCgMA&X-Amz-Signature=aa88aca66762e83a597ec2ea38341062e5dc1323de63f6f6d8ca3fd8c837443f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZSH2W4Z%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T181953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQDksxrnkqPDaflwv%2F0RngZ8AcwXUvJU90%2Bte%2BHzXCfqSQIhAIe66bmXEkR173DaWCFt5uI1KeipBdMh3Sz%2F6O3OtkdLKv8DCBsQABoMNjM3NDIzMTgzODA1Igy86yb5%2ByenpVPwQkgq3ANloltAaGogmGbK9vXXnvUdkfHeZJ9Qs1%2BsS3Kkhaxqopf0sMVCDO2yIQIbInNTJXdw1pypyNkAndMxsbYMTx4T9eQzlSbVfRbTA69itI%2BNu0XmOMYe3ey3cccRmPKQVNIrhMxd99RXCj7Y3YBYEjBiCBhn1kQTN9RLWmt1mLLd7IYNOhiFfE3sjUOq9wTFln%2FUOEIc89AuzOgGYaBkOvn%2Fth4TUI3aSoPchNnK4NyZ%2BpUHdlMxfaolyL4v0%2BCin4CCUeavV2q8PMTUUG7jvsK7glbLwHlG%2B8hOtZvdYRu86Q4xihbQw10Eq8d4CL%2FBmRl1aTFCgMBENC3iWwm1wwgT%2F5zEIefuyyUNYoOyNt9Amx2D9bHnzhR5aCoicb9qs6b%2Fado0%2BsBzZXK2EsANl5aO6ETFiOI6GCgcwPJiOGHOYCYZqdaX74HJtrYwRgCG9cadR%2Bfezvc6WdziaOPpC3OhaBEgb7dR6%2F3ZDoPorjb1Cgeo4Fyk4%2BaqYqy07m0fJvELxnW7993I5zjwqO2LX8LoFuHStgF9vIEktIPsx7JqIIbEhvPZ71x3lb34B1ct3osN6iyacC5fvd6O%2B%2FabJeO0DjvVERiy3Tpv0C0LuVRJuXyiy3hV99Tv2J2jeDCayILUBjqkAfpf7%2F50hypq%2BEkZci9xWG7D7xZKb4LS%2FZ4MQjXFeBJusBlRx8yIrL6pxMvSat1FZ3%2Bxg4sbCkdmaKmfTT6%2BJ4PjXMh%2FnS4MZLTIZ%2Bj1JAG%2BwFBksnp7v3Acl5%2FGUWp6%2FG37OiDe%2FheftytY5%2F1LVsPu%2BH7ifI41jR8BQKeMM384VScykpjFVj%2FLjLCFMF2fItqtf4oo69erwkTy%2FmJG44ylCgMA&X-Amz-Signature=dc87b300a223a37fd93cb0b501baaf6c7c87f908fc3efbabc6f7cffa7343966a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







