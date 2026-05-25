



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CA56JB7%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T144425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxv9VAOOZcQQnKb1L180CJq%2B28HzYmcEXKC1%2FdF6aNTAiEAmmTws6WS7%2F7AEChESiZIST9NUST%2B%2BIblsv2mQqiEglsq%2FwMIZxAAGgw2Mzc0MjMxODM4MDUiDKbxDTu5eQZxb7r1lSrcAxwtmpK59h3M96k03YUDOQ%2Bz%2FQLZo%2FYVDS1FQOs2pxxsWuikM%2FE9vtn%2FI4lh1rk8CGVqKDEYQydlYqDwhpx9OeTxLAWjnxxNXeJ66HwhaJjkc560jEUwWSvD9ooyger1Ftq6Aofj%2Fu%2BCw2n40kksnD%2BRaJdxQP1hOStcN%2F5ytxLOu8dvMRYl8yG7Kz7FIhg0Lii697dbcz8xE2%2FxvRCnY5xLJnBYvflqrOzhZgs%2FH30YsHdYSCIYDvUF2u1m5p5kPAraKwV%2Bx4xMoN5xOjqyIfstZE4eKvK3VpsvTXGvzdfA%2B8Rn4k%2FDyeypEkBoYqr1uFPvDBSMzwnAu5qzT5XJ25aK5hxnpJHfYpU4TzVMZBll4EHClM7NomOwAhIJI0dPghsaFiWZ6vamgUEhuun%2FoE6OTG7OPhZcNqhIpdQ%2BuKtND4gMAmqBlP8lmoBJpv1pXMrxAooWMJ3d9mfsLybtVlXh0TNRklDiR9sMt%2F2WOI5zcpelp1hOWbA33BBuobWpm%2Fwwv2%2BVntjhw4DvtaviLWzgTnfwNnVxGGGQn1Vi6JT00FbOjvWgV8n1BBjKiT4x8mrC1qnyAfHXu%2BGaiiIzxBuWaJ8UsZNbJNI173Pc1xL0lPJ%2FXPbYBuB97quQMPG10dAGOqUBu6%2BG5e9PmSUGkOzxYosOAs5QuHr%2BwBPvvmo6LQpIjwaGtfrJT0bTs0vpc0X3l1l9m8u2JqyC4NF55fV6qc1qZR2EQO%2Bpj71mlbjakpaZ%2BYPuvqfSQv5udF9kbZNT3DX030kcunJWls8qep%2BQ1wB5uJdAcZGxwrLJaVC74gVq%2F0PR%2Fhxs0SOAGqARm5ZeEypOU%2BEN6gaqRwLKdJ7%2FTq17NlDaoe32&X-Amz-Signature=edfebc9eb420ee6809b0b4e5413409b2409c9e547249d21bb69e584b6c5bb8be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CA56JB7%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T144425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxv9VAOOZcQQnKb1L180CJq%2B28HzYmcEXKC1%2FdF6aNTAiEAmmTws6WS7%2F7AEChESiZIST9NUST%2B%2BIblsv2mQqiEglsq%2FwMIZxAAGgw2Mzc0MjMxODM4MDUiDKbxDTu5eQZxb7r1lSrcAxwtmpK59h3M96k03YUDOQ%2Bz%2FQLZo%2FYVDS1FQOs2pxxsWuikM%2FE9vtn%2FI4lh1rk8CGVqKDEYQydlYqDwhpx9OeTxLAWjnxxNXeJ66HwhaJjkc560jEUwWSvD9ooyger1Ftq6Aofj%2Fu%2BCw2n40kksnD%2BRaJdxQP1hOStcN%2F5ytxLOu8dvMRYl8yG7Kz7FIhg0Lii697dbcz8xE2%2FxvRCnY5xLJnBYvflqrOzhZgs%2FH30YsHdYSCIYDvUF2u1m5p5kPAraKwV%2Bx4xMoN5xOjqyIfstZE4eKvK3VpsvTXGvzdfA%2B8Rn4k%2FDyeypEkBoYqr1uFPvDBSMzwnAu5qzT5XJ25aK5hxnpJHfYpU4TzVMZBll4EHClM7NomOwAhIJI0dPghsaFiWZ6vamgUEhuun%2FoE6OTG7OPhZcNqhIpdQ%2BuKtND4gMAmqBlP8lmoBJpv1pXMrxAooWMJ3d9mfsLybtVlXh0TNRklDiR9sMt%2F2WOI5zcpelp1hOWbA33BBuobWpm%2Fwwv2%2BVntjhw4DvtaviLWzgTnfwNnVxGGGQn1Vi6JT00FbOjvWgV8n1BBjKiT4x8mrC1qnyAfHXu%2BGaiiIzxBuWaJ8UsZNbJNI173Pc1xL0lPJ%2FXPbYBuB97quQMPG10dAGOqUBu6%2BG5e9PmSUGkOzxYosOAs5QuHr%2BwBPvvmo6LQpIjwaGtfrJT0bTs0vpc0X3l1l9m8u2JqyC4NF55fV6qc1qZR2EQO%2Bpj71mlbjakpaZ%2BYPuvqfSQv5udF9kbZNT3DX030kcunJWls8qep%2BQ1wB5uJdAcZGxwrLJaVC74gVq%2F0PR%2Fhxs0SOAGqARm5ZeEypOU%2BEN6gaqRwLKdJ7%2FTq17NlDaoe32&X-Amz-Signature=5aac8cdbd0c2c045dc5367d88a47d792d7e8ef5e32af4dc6e04a714521349a86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







