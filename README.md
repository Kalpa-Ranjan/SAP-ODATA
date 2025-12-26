



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QP6VEN%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBjj0eVuqJ6Zhchf59nY3FavC4N2DojiWjEGebc2%2FMJQIhAI4OTCNAEYYNTFsazBpiXEZofa6jsDHqRwr%2BjF%2BdeeO4Kv8DCEsQABoMNjM3NDIzMTgzODA1IgxvRCSMkmkufDRG%2FGUq3AP5OWfDlJ0s1nIJn1aaF5oDougxruE%2F8LUesRuFxKOLZtFlFN6hjG6K9CcdVIcvEnntnJTzrYpDBsCPVOmH%2FDkI1Y9VQfZBYB8%2BZBqnOx95jwVIrQ42yfipTCi0e02NHcHzyFJy%2BJl%2Bc%2BOkiL7FYDA7t5QFXxtvHVTMa4WnhJPTanrSHcmThif6COaS5SYSKRpoqEji3whV%2BovTJqoP9W881fEDw6hZZvBerlEg8TCDoOFBUAeQksAi%2FJYdGRQH72xRUchukxF6OUGRZnyYEiOcN64WfyrJhdoQOpnCfMaYP5rlzGgDiHe%2B%2FxwiWeXeQ5Vognwg40ehkfmGCmeQ6Nt3ZtpRhXq9jV7Gi%2BhxElTgk1vEYRE4reBH9bZuwl6ZE8JB5skhf2sf8pUW%2BQDlOJ4LJMHQ3zgGk6f4BRT3xnbgVS%2B0Z%2BJSZJOplww6JMVSSYc3R8WF%2F4zxJFXMD7aom0uTp199qdP6%2FWaLOUkx320UOd%2BcYr81loVoYvlzfWw4M488MMGqDg%2B8uWGRHOPnFFW3VGoFMY%2FnPsldCPwgq%2B%2BgVY6V3sMnYlo0d8FiWYH7mTfehslTtR8IgaDylW1edGKm8rvye22FZcdojN2celMLX6SzodOokGuVLnodMzDaybfKBjqkATqOJqvvrF89k%2B%2BaCOkh688qhHGopGKS87H%2FrvPaP4bUFWg3qqLqonGJy1T4pDC3Sh3yWXfiJQifA6PTnn87212CToxwBBAjpGxjPLOs8xlWFYhJRSy5dq93UbeEzHHng7SzM5o1yz3XS5s0c1VuWW2vzKJSYTOJv4cCH5y0MgTaM%2B2xoLTPxhu2NatGpL37k1KmyUzy7aoxmkDTmgz2dTidEPaz&X-Amz-Signature=ffe3a701165656813a3aabac46e596925875424c0697c896ec3a0e26b4248424&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QP6VEN%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBjj0eVuqJ6Zhchf59nY3FavC4N2DojiWjEGebc2%2FMJQIhAI4OTCNAEYYNTFsazBpiXEZofa6jsDHqRwr%2BjF%2BdeeO4Kv8DCEsQABoMNjM3NDIzMTgzODA1IgxvRCSMkmkufDRG%2FGUq3AP5OWfDlJ0s1nIJn1aaF5oDougxruE%2F8LUesRuFxKOLZtFlFN6hjG6K9CcdVIcvEnntnJTzrYpDBsCPVOmH%2FDkI1Y9VQfZBYB8%2BZBqnOx95jwVIrQ42yfipTCi0e02NHcHzyFJy%2BJl%2Bc%2BOkiL7FYDA7t5QFXxtvHVTMa4WnhJPTanrSHcmThif6COaS5SYSKRpoqEji3whV%2BovTJqoP9W881fEDw6hZZvBerlEg8TCDoOFBUAeQksAi%2FJYdGRQH72xRUchukxF6OUGRZnyYEiOcN64WfyrJhdoQOpnCfMaYP5rlzGgDiHe%2B%2FxwiWeXeQ5Vognwg40ehkfmGCmeQ6Nt3ZtpRhXq9jV7Gi%2BhxElTgk1vEYRE4reBH9bZuwl6ZE8JB5skhf2sf8pUW%2BQDlOJ4LJMHQ3zgGk6f4BRT3xnbgVS%2B0Z%2BJSZJOplww6JMVSSYc3R8WF%2F4zxJFXMD7aom0uTp199qdP6%2FWaLOUkx320UOd%2BcYr81loVoYvlzfWw4M488MMGqDg%2B8uWGRHOPnFFW3VGoFMY%2FnPsldCPwgq%2B%2BgVY6V3sMnYlo0d8FiWYH7mTfehslTtR8IgaDylW1edGKm8rvye22FZcdojN2celMLX6SzodOokGuVLnodMzDaybfKBjqkATqOJqvvrF89k%2B%2BaCOkh688qhHGopGKS87H%2FrvPaP4bUFWg3qqLqonGJy1T4pDC3Sh3yWXfiJQifA6PTnn87212CToxwBBAjpGxjPLOs8xlWFYhJRSy5dq93UbeEzHHng7SzM5o1yz3XS5s0c1VuWW2vzKJSYTOJv4cCH5y0MgTaM%2B2xoLTPxhu2NatGpL37k1KmyUzy7aoxmkDTmgz2dTidEPaz&X-Amz-Signature=8dbe40b35e03f902bd54667d783e5b3df8e74514ae2823106fcdd21d6ce9fd37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







