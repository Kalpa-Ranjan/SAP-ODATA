



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FF76YLU%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T072003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6i9SJZmjzxvDjMuL0Hx0JAf0pcr3WzEKjk6Ef4mZ3jQIgaEqqm6JBJQ6R4FWt6xuyVa8qT57pweIcEFegeTn08hoqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKS9U4GbRZio5ZqrQircA96Xl%2BI1kaLWAjmklfkcDXRRr9iOi53UDCsOAIJmoH6SbqG%2BwnSeeiFg4ByhZNOSico2R5dsy9XbHIN%2BuydqWMOznRL%2FYQSK4DinI8tVrsdChgMJamF4Srud00%2BMdIB3%2BElL83Fz1z4%2Fuq4Poba%2Bvm1kuP%2FrAHbDPnezj0XjLFvKR5q%2BjZAytt6f%2F4e90HE3iny6QHcOhbSb6HIjHPxMyGHeOPQgp%2FsR8ox751Vc89z3gcnAXe7qE8xBdwvNcIYdvcA2eCl5hLPE9efrzjub%2FhGhn192Tci1vH%2F2D59TS2kVCx5zGxKqjKKBYf6c0Ef4CYO52%2B0Xbpmsa%2FmGyMINdwYNrVjReLxBIHYz%2Bg83E4FsTTTA%2F8ghF32aV0HA%2Fa%2Bsqn3%2FQ0pkmUpoJyOhOv5YDOuMi5w8OslOjsKrGh40uuU9VasrNdHnH73ZvMu48Gu%2Fe7CkkCz2qCNaTv43DPB0hrFWejX57QHfmTxvHy9ntbPCn4EW0VZuA0p4yN9%2FC18TjwCESzyi8oygJYzVP9MVZ0EC6jYDmbF2qcs9NAn2qQAUepAhiCm0pZWlhx4QyCCR37vHL%2FqN21G9aohdoLk%2BJWRbBsp%2BaUJ7rXfPSlL70hKoisqO8YifS6t3yMogMJfs5dMGOqUBGDn3fxwMVBG7zj3AmkfaT3rM1gtseNN5OWEFeu3HRw6nAOYPXDJMtYHMVeAhomlocHXgKH6UsUXgJjVT17E%2Fkq5sNA0RZCFhBEo%2FsH4B2FQfFYsyF1492KbJh4oEOgvq3bJEsGY1Tj7H9lkt3Sp7l4cq8%2BgT6tuGE4ZLnVY0nUxfT3qA7aZQbMkWeVv%2BPhH%2F540%2FTUpAZniml2xsFk2OnX8j%2Fe0R&X-Amz-Signature=852637a641e8f5b7f3249e1b61c6c3999ec37379c1055cac0bdab0dc8f9279f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FF76YLU%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T072003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6i9SJZmjzxvDjMuL0Hx0JAf0pcr3WzEKjk6Ef4mZ3jQIgaEqqm6JBJQ6R4FWt6xuyVa8qT57pweIcEFegeTn08hoqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKS9U4GbRZio5ZqrQircA96Xl%2BI1kaLWAjmklfkcDXRRr9iOi53UDCsOAIJmoH6SbqG%2BwnSeeiFg4ByhZNOSico2R5dsy9XbHIN%2BuydqWMOznRL%2FYQSK4DinI8tVrsdChgMJamF4Srud00%2BMdIB3%2BElL83Fz1z4%2Fuq4Poba%2Bvm1kuP%2FrAHbDPnezj0XjLFvKR5q%2BjZAytt6f%2F4e90HE3iny6QHcOhbSb6HIjHPxMyGHeOPQgp%2FsR8ox751Vc89z3gcnAXe7qE8xBdwvNcIYdvcA2eCl5hLPE9efrzjub%2FhGhn192Tci1vH%2F2D59TS2kVCx5zGxKqjKKBYf6c0Ef4CYO52%2B0Xbpmsa%2FmGyMINdwYNrVjReLxBIHYz%2Bg83E4FsTTTA%2F8ghF32aV0HA%2Fa%2Bsqn3%2FQ0pkmUpoJyOhOv5YDOuMi5w8OslOjsKrGh40uuU9VasrNdHnH73ZvMu48Gu%2Fe7CkkCz2qCNaTv43DPB0hrFWejX57QHfmTxvHy9ntbPCn4EW0VZuA0p4yN9%2FC18TjwCESzyi8oygJYzVP9MVZ0EC6jYDmbF2qcs9NAn2qQAUepAhiCm0pZWlhx4QyCCR37vHL%2FqN21G9aohdoLk%2BJWRbBsp%2BaUJ7rXfPSlL70hKoisqO8YifS6t3yMogMJfs5dMGOqUBGDn3fxwMVBG7zj3AmkfaT3rM1gtseNN5OWEFeu3HRw6nAOYPXDJMtYHMVeAhomlocHXgKH6UsUXgJjVT17E%2Fkq5sNA0RZCFhBEo%2FsH4B2FQfFYsyF1492KbJh4oEOgvq3bJEsGY1Tj7H9lkt3Sp7l4cq8%2BgT6tuGE4ZLnVY0nUxfT3qA7aZQbMkWeVv%2BPhH%2F540%2FTUpAZniml2xsFk2OnX8j%2Fe0R&X-Amz-Signature=e162aaaf85a659cc1fee56bc1da097035824ff42b7d2930cd128794a76b0b811&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







