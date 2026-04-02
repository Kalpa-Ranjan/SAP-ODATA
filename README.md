



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657DN2G77%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T185029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkvgRTkjf4xrQJT2UEMKmnp%2BwSZjQqVVfdw4fOzlwqywIhANQvl6xvfUS12yNeNkVUecl5hAxiniNMIBaDy5MdbS6BKv8DCHQQABoMNjM3NDIzMTgzODA1IgzfX9aF7F43ZZBq4WYq3AObNH7ZehEVAGqK4Cjnrqm6ncz7YHYPRoDdtXG%2BJbliefVPWnfCQnSa2FHOaq6tzQISg6Zer4gJwfaWHMSEaPgj%2FdYp9zBsxumfvNstDa%2Fl6%2FDAJXLXKe6oey1fXXqyHHm%2B8C6qURhpEHCZVfiwc996xk0U%2BAQvKH%2F0Lb5mbGDP%2F%2FsKML0phDXzIGpIhjLLH%2Ffwt%2FTht0c1oLb9OI%2BUZnlI87vPr2e0wVuzz2pVSgVaGTndFGXkBJKP9Hd4kwFYze3hw1Ek59TfMTvSE1hSUJxwpGuVCgzNusKHkNFeSY%2FRy%2Fy8I3sh2YhKW71sD9uBRyRnOoLuuJd1ZPJcHV9vs7%2FKNpb9iVCCzABvXvkBPzaSY3WrSUkY1ztaColWI8bPd82J4EL6V9sTqP90he6u%2BqWwZEdoG3%2FrVCkF4rzkWFfxYlrBRXptdBC24s5KEwVcPl0ERAANbrbMCsxMXiFQ4tkrTDM%2BrZd4FcbNbEat27qv1jq6LYz79Js%2B3unaGE2ZBAk9jYeRwLtz9IMeoLgmtWsDVtPoIdwantgb7Bj23lAOYL3Q9LZ%2FCi0%2BOoyKEsEljUNh8iMnpgwg04QZ%2BznMuKRi%2BjwNt5F2%2BBOpnjXxLU9GCJ5Lq2aHqR%2BProEQrTDo77rOBjqkAXGWllEyeu9PvYKTBy9IbkGHVbJ2pYaRFZaUzecEMLmtHw7Fukm%2B%2Ff1R0qTlzfU45ZJciJNzrk7mBtThmje%2FkW2zxWTOE4tEIMgCLsBQF7eFjq%2BV669H4ioNP4gi4qxfHxZtKBdlyZf%2F5MQeKcyVOgNwX37Xhd3POf5vqLMRGC7dZMVgDpC0PPUJzyZSdcoeq8q%2BHK3hendZf%2FiWJg5Vyw%2BcS6hm&X-Amz-Signature=9db1d501ec7a3ae9ac1f1dfe4c730c2c7726132a8f6b7c755cfcaa37a688df21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657DN2G77%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T185029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkvgRTkjf4xrQJT2UEMKmnp%2BwSZjQqVVfdw4fOzlwqywIhANQvl6xvfUS12yNeNkVUecl5hAxiniNMIBaDy5MdbS6BKv8DCHQQABoMNjM3NDIzMTgzODA1IgzfX9aF7F43ZZBq4WYq3AObNH7ZehEVAGqK4Cjnrqm6ncz7YHYPRoDdtXG%2BJbliefVPWnfCQnSa2FHOaq6tzQISg6Zer4gJwfaWHMSEaPgj%2FdYp9zBsxumfvNstDa%2Fl6%2FDAJXLXKe6oey1fXXqyHHm%2B8C6qURhpEHCZVfiwc996xk0U%2BAQvKH%2F0Lb5mbGDP%2F%2FsKML0phDXzIGpIhjLLH%2Ffwt%2FTht0c1oLb9OI%2BUZnlI87vPr2e0wVuzz2pVSgVaGTndFGXkBJKP9Hd4kwFYze3hw1Ek59TfMTvSE1hSUJxwpGuVCgzNusKHkNFeSY%2FRy%2Fy8I3sh2YhKW71sD9uBRyRnOoLuuJd1ZPJcHV9vs7%2FKNpb9iVCCzABvXvkBPzaSY3WrSUkY1ztaColWI8bPd82J4EL6V9sTqP90he6u%2BqWwZEdoG3%2FrVCkF4rzkWFfxYlrBRXptdBC24s5KEwVcPl0ERAANbrbMCsxMXiFQ4tkrTDM%2BrZd4FcbNbEat27qv1jq6LYz79Js%2B3unaGE2ZBAk9jYeRwLtz9IMeoLgmtWsDVtPoIdwantgb7Bj23lAOYL3Q9LZ%2FCi0%2BOoyKEsEljUNh8iMnpgwg04QZ%2BznMuKRi%2BjwNt5F2%2BBOpnjXxLU9GCJ5Lq2aHqR%2BProEQrTDo77rOBjqkAXGWllEyeu9PvYKTBy9IbkGHVbJ2pYaRFZaUzecEMLmtHw7Fukm%2B%2Ff1R0qTlzfU45ZJciJNzrk7mBtThmje%2FkW2zxWTOE4tEIMgCLsBQF7eFjq%2BV669H4ioNP4gi4qxfHxZtKBdlyZf%2F5MQeKcyVOgNwX37Xhd3POf5vqLMRGC7dZMVgDpC0PPUJzyZSdcoeq8q%2BHK3hendZf%2FiWJg5Vyw%2BcS6hm&X-Amz-Signature=eee12cd09ab955e66825b3f8fe72e2f7e0dbac968de6539becb85b5f4edd6817&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







