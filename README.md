



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667BALEX2%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T022927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHJYwjrbG4qi1yM089TeFgLsSy8TIAayU4Qyw5XOSlF%2FAiEAgDcQs%2FeVgIVhyqjzEl9FD%2FxmpDN%2BVQp%2BVJrknHyTtxkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2KAqT2b2ChhUMC%2FCrcA0Ac5ZJvkZsSFSqNd9mXaxK6EwZStq3O9BGmO%2FEmleeKZBvBjrx8hS2RBL9d%2BsnMvv1Mi05v%2FLTfKwGv3kWFe7E%2F%2B8xftncEypInn27xCdGfbCIdqm30u9tr8fVxY7HzRik%2FB2W9BE8yUKTk1P3Mxt6IXx%2FrxZzAa%2FF371wc2TT6aevv5iQ36KIVlyF5E2dWt060xpEYNnhXjTdwQVgoLZMaqwSXaAh1XvSfZcA7edSwYBv5f4qfh%2F9b88QUFCrf428%2BDoeKcNBH4OBInb4eqUe%2BYyF1F4AxckQpj%2By6L4Jh3XT46YY0l06%2BhXOzOy064EMe5hdGTa46JpZqMChKE3yjqBoGHvgyjj2CXmQYUwts1SL3TghHV5rMUtFoNZMyIRumvKfNHLBImVEbjUpA6VQWYfJsdc0kwpph6SonrE%2BjCAO6Ou6KRM4ekR%2BGySPY76hej5wK0rt5TGMVxy9h3DZkNP3kOnW7OF2pHRvggm%2Bs%2BAL%2FDVpxwRBwRBqTWyQGDtpEeXPpG6BddXjwk1oF%2FZ7HDz07dk47LRuY50pFuaVeW7C%2BwYYSjnJc2LnDsrTl8diNIHy22XddZgPg6OrrVnSWIJmHS19vbRx8idS1aIqu6AS9Ra4EMpgXegjtMPr%2F3dQGOqUBZ9zUgHOZ%2Fz7v%2BGDohdjWpBwOXZlNay%2F6CwSzL%2FXDLvmK11PNu6YZ7h0%2FBCLyIE3rIei6770EW6uNc%2BZTdX5nNyEY6XlK%2FGI7sb0pyEWoqs8G0fV70jIKThb3VXpb2WmlrQjXqppUlxFDJWlmi%2Fy6UUUxodbVQ9XZeAuyU9ULLFV5jKlkeIhl86WOuVGhgwlZVKSthptbn1MmHE9s2PdyC12IzdhP&X-Amz-Signature=e5dab5556f67bd7a2d3d46b5aeaeefcd0b361f2e9f9df85286e9f894de46a12a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667BALEX2%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T022927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHJYwjrbG4qi1yM089TeFgLsSy8TIAayU4Qyw5XOSlF%2FAiEAgDcQs%2FeVgIVhyqjzEl9FD%2FxmpDN%2BVQp%2BVJrknHyTtxkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2KAqT2b2ChhUMC%2FCrcA0Ac5ZJvkZsSFSqNd9mXaxK6EwZStq3O9BGmO%2FEmleeKZBvBjrx8hS2RBL9d%2BsnMvv1Mi05v%2FLTfKwGv3kWFe7E%2F%2B8xftncEypInn27xCdGfbCIdqm30u9tr8fVxY7HzRik%2FB2W9BE8yUKTk1P3Mxt6IXx%2FrxZzAa%2FF371wc2TT6aevv5iQ36KIVlyF5E2dWt060xpEYNnhXjTdwQVgoLZMaqwSXaAh1XvSfZcA7edSwYBv5f4qfh%2F9b88QUFCrf428%2BDoeKcNBH4OBInb4eqUe%2BYyF1F4AxckQpj%2By6L4Jh3XT46YY0l06%2BhXOzOy064EMe5hdGTa46JpZqMChKE3yjqBoGHvgyjj2CXmQYUwts1SL3TghHV5rMUtFoNZMyIRumvKfNHLBImVEbjUpA6VQWYfJsdc0kwpph6SonrE%2BjCAO6Ou6KRM4ekR%2BGySPY76hej5wK0rt5TGMVxy9h3DZkNP3kOnW7OF2pHRvggm%2Bs%2BAL%2FDVpxwRBwRBqTWyQGDtpEeXPpG6BddXjwk1oF%2FZ7HDz07dk47LRuY50pFuaVeW7C%2BwYYSjnJc2LnDsrTl8diNIHy22XddZgPg6OrrVnSWIJmHS19vbRx8idS1aIqu6AS9Ra4EMpgXegjtMPr%2F3dQGOqUBZ9zUgHOZ%2Fz7v%2BGDohdjWpBwOXZlNay%2F6CwSzL%2FXDLvmK11PNu6YZ7h0%2FBCLyIE3rIei6770EW6uNc%2BZTdX5nNyEY6XlK%2FGI7sb0pyEWoqs8G0fV70jIKThb3VXpb2WmlrQjXqppUlxFDJWlmi%2Fy6UUUxodbVQ9XZeAuyU9ULLFV5jKlkeIhl86WOuVGhgwlZVKSthptbn1MmHE9s2PdyC12IzdhP&X-Amz-Signature=a857575fe5b1d12e121418c6c7c8642e6b697cda1cf04b0402c63dbe5eddda59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







