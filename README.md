



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTGVXAJ%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T102656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaJrBc0k%2FNF6A7jO5JRaQaBy8y52x2lY8pd8hR3kd9qwIgKtdF6SsX6g76sqYZ%2F3XMr6fvhhjybbeM2duB8iOSUJsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBXDQbcjyfc1e3rpSrcA1XbNaWfBFdaHFiRa9JOM8dGboku1UiR6tpJfl434zKyAPDke0oA5ODxqYuWRHXzkgQheoMFyturcmIg3j0V8TdGnp5jF1eWJ9SrSbhAiLdq5wQzsJe8CafyanQd2ey5eb2YVNrwXvCJKzCkDCkiAM83q2giZMUI%2FeRpB84VnPsOKGcfQ6cUyqpiY5rbo3IRjQgiEq6BXqZxl3AcJhFgVu89BU9sQEnI%2B4olXW172sdgTClCvBMJUPJoU56QbU993J9w9Qmal%2BZBxDoz3QQFo8LMzGjJ%2FEZcM04CX8JDfG8tlSujCfiNPfCY8BR82VRgtJGs9wYq%2FWUvBnekhMDHw4oCnFn%2Bwl7lohfxUM1P5bQT9vKvsv00W28su77qYg1PrG2YcUKxtgO4Yu%2Bct8cBup%2BshsnWWQJcIJRr6jo0JoBAHYRVeI8azr3CJWSMJxgyhpj1gGwvuRRKjQWh8aKRhuvrVlLpq6nPwrpak95c4xMhQEpODiS7L5VQhXQ7TINGN3eO6IaU1mQcU9TuSAuf%2Bx%2FMfqFKGdeVSxebB3rNJKeV4wFQUZhV372gqvRN36zTGnHUJVxwL3%2BMdXsegVencNl1aFZZ8ZfErsvaGZO6BMUIhuyvCuMu4jkeiDQpMKmLmtEGOqUBfBDXXRWdudDpHLBCHIQkOqxNWoWgyfkpNarOnyDs98VtMvr4Au7WZd00XWLtVugqNK4pnklD2iPHzkNtjK8bs69QwOe7Fc1Kv3Gbe7u2bN7heYWs877VfljiUnhO23mtl%2FLU8RnM55rYdmzgr5Kp9IzvgxI%2FsIn5NVWrLTWuDMieZQ0yGOxXEks8k63eT0xbq4tnk8VBBvVyImawNGWjqzmUUfdv&X-Amz-Signature=d36c1157dee51b8468ea034c724ca7e077c19e93ca6535438a6e5ac36e713fa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTGVXAJ%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T102656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaJrBc0k%2FNF6A7jO5JRaQaBy8y52x2lY8pd8hR3kd9qwIgKtdF6SsX6g76sqYZ%2F3XMr6fvhhjybbeM2duB8iOSUJsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBXDQbcjyfc1e3rpSrcA1XbNaWfBFdaHFiRa9JOM8dGboku1UiR6tpJfl434zKyAPDke0oA5ODxqYuWRHXzkgQheoMFyturcmIg3j0V8TdGnp5jF1eWJ9SrSbhAiLdq5wQzsJe8CafyanQd2ey5eb2YVNrwXvCJKzCkDCkiAM83q2giZMUI%2FeRpB84VnPsOKGcfQ6cUyqpiY5rbo3IRjQgiEq6BXqZxl3AcJhFgVu89BU9sQEnI%2B4olXW172sdgTClCvBMJUPJoU56QbU993J9w9Qmal%2BZBxDoz3QQFo8LMzGjJ%2FEZcM04CX8JDfG8tlSujCfiNPfCY8BR82VRgtJGs9wYq%2FWUvBnekhMDHw4oCnFn%2Bwl7lohfxUM1P5bQT9vKvsv00W28su77qYg1PrG2YcUKxtgO4Yu%2Bct8cBup%2BshsnWWQJcIJRr6jo0JoBAHYRVeI8azr3CJWSMJxgyhpj1gGwvuRRKjQWh8aKRhuvrVlLpq6nPwrpak95c4xMhQEpODiS7L5VQhXQ7TINGN3eO6IaU1mQcU9TuSAuf%2Bx%2FMfqFKGdeVSxebB3rNJKeV4wFQUZhV372gqvRN36zTGnHUJVxwL3%2BMdXsegVencNl1aFZZ8ZfErsvaGZO6BMUIhuyvCuMu4jkeiDQpMKmLmtEGOqUBfBDXXRWdudDpHLBCHIQkOqxNWoWgyfkpNarOnyDs98VtMvr4Au7WZd00XWLtVugqNK4pnklD2iPHzkNtjK8bs69QwOe7Fc1Kv3Gbe7u2bN7heYWs877VfljiUnhO23mtl%2FLU8RnM55rYdmzgr5Kp9IzvgxI%2FsIn5NVWrLTWuDMieZQ0yGOxXEks8k63eT0xbq4tnk8VBBvVyImawNGWjqzmUUfdv&X-Amz-Signature=d1f3665506f297d44e96310a408073a473dafe263abaddd62ea27758dcc1260e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







