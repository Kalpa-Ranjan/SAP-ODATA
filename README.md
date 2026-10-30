



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBIBTQDB%2F20261030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T060936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIQDVoxnKNncJ%2F%2B%2BPsUXBrl8JFgUDhFq%2BNWk4KsYj0FnyJQIgU5G3mxLSfPBwxN5p8jlenBDJ%2F2vnI4CN9UpBbhS%2BKxIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDD4Z5zJXSV0It%2FrlgyrcA9V10P0lxMB2EvA7J0WlVC5XY0vUJ4VzyxYmrjx3%2FRbjmsVAIrnVf61kkw2qc4XzXCtzrDPD9m1Rl3L8W%2FGaJ84MtCWPb3sPhffncxHGB%2FQOz9VPCOXxgvWSBlEj7pZG0D5Ti8MGyE4GrNuqr2NHMhqdJ49iJBVrnTmKrdM6IJJYDS7QVHro1inB9p2PrIKC%2BSPz4uKEvzHv8wzlokWjXPzpC8kwBq9eUftWSc%2B6twhSBEgBTRVdKGRm%2FTKKGLzTESLxXNKNLsjpTnJUhNRSfc1Aw987xEY2bkslGBvcJ40Uv91As6%2F9107alsQ%2Bo2xClWV9eP40KIZF4Krnm0nUqIHa%2BQ%2BBsL1urvEN7ihxsl7wsQE%2FJJkg281es4CfcN0qWGjlJMka5iN7xCZLwtOhhlM4YK%2B6WzKLArHvRanW6ypkNEeyXW6AZJB51nfEzQQSnCL7hQXtTKvugGhZ5z9x7MJbYKYd5KcyFu78P46eKKFDBNlJiU0w63Z3dG6qZ9Kc%2F1p6VSwMis%2Bttj1JAn8rVnM6xGatXxjLvNm8fVmPUmn0FZiZ8nhCxng3EW0IkyrH8qBvnH81Auw9lsu9ZnrMguRw4Pl3%2Fu78tclmPxKq1TVmNONf2beull2vn1paMJG1kNcGOqUBlR%2F%2F%2BE%2BhwTAOJfT5JYYE2cW7WCoKaAEzAKfz6%2BhQvGHqfWlT%2BHMretdHhBbF7ScCGCu4mlnrfZYRSEkEEyoyCDprTO8HoJz4%2FgSsV7ZeFvOBwAnezQ2rGx7feOlQxFG%2FTAD%2FQwD1ls7kJf%2FS2R4f5scakuHvgZS%2BpsWckQt45%2FAmalin7j4D25rUwpM5ghq%2B2L9B%2BIz2D4%2BggKR9x76wWloxgfCu&X-Amz-Signature=55b1cf03baa9f3c73853acd348186b8e2284f1b8e67fc738f45ea545a2e250a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBIBTQDB%2F20261030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T060936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIQDVoxnKNncJ%2F%2B%2BPsUXBrl8JFgUDhFq%2BNWk4KsYj0FnyJQIgU5G3mxLSfPBwxN5p8jlenBDJ%2F2vnI4CN9UpBbhS%2BKxIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDD4Z5zJXSV0It%2FrlgyrcA9V10P0lxMB2EvA7J0WlVC5XY0vUJ4VzyxYmrjx3%2FRbjmsVAIrnVf61kkw2qc4XzXCtzrDPD9m1Rl3L8W%2FGaJ84MtCWPb3sPhffncxHGB%2FQOz9VPCOXxgvWSBlEj7pZG0D5Ti8MGyE4GrNuqr2NHMhqdJ49iJBVrnTmKrdM6IJJYDS7QVHro1inB9p2PrIKC%2BSPz4uKEvzHv8wzlokWjXPzpC8kwBq9eUftWSc%2B6twhSBEgBTRVdKGRm%2FTKKGLzTESLxXNKNLsjpTnJUhNRSfc1Aw987xEY2bkslGBvcJ40Uv91As6%2F9107alsQ%2Bo2xClWV9eP40KIZF4Krnm0nUqIHa%2BQ%2BBsL1urvEN7ihxsl7wsQE%2FJJkg281es4CfcN0qWGjlJMka5iN7xCZLwtOhhlM4YK%2B6WzKLArHvRanW6ypkNEeyXW6AZJB51nfEzQQSnCL7hQXtTKvugGhZ5z9x7MJbYKYd5KcyFu78P46eKKFDBNlJiU0w63Z3dG6qZ9Kc%2F1p6VSwMis%2Bttj1JAn8rVnM6xGatXxjLvNm8fVmPUmn0FZiZ8nhCxng3EW0IkyrH8qBvnH81Auw9lsu9ZnrMguRw4Pl3%2Fu78tclmPxKq1TVmNONf2beull2vn1paMJG1kNcGOqUBlR%2F%2F%2BE%2BhwTAOJfT5JYYE2cW7WCoKaAEzAKfz6%2BhQvGHqfWlT%2BHMretdHhBbF7ScCGCu4mlnrfZYRSEkEEyoyCDprTO8HoJz4%2FgSsV7ZeFvOBwAnezQ2rGx7feOlQxFG%2FTAD%2FQwD1ls7kJf%2FS2R4f5scakuHvgZS%2BpsWckQt45%2FAmalin7j4D25rUwpM5ghq%2B2L9B%2BIz2D4%2BggKR9x76wWloxgfCu&X-Amz-Signature=db5e27c9b448c7ea313be9b5c715965d3bd760c7e6e4bf77a6d9d11f3ee74f04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







