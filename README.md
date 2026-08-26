



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTFG5W53%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T194042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCyTuQUT38Jp5%2BttejdnAbJ9BCWOsVJPol7K%2BTnH4JEsAIhAMRP4otclkdbD1hITP5QnEC40KIDUYCtCRPoh8xWdz06Kv8DCCIQABoMNjM3NDIzMTgzODA1Igzvn00go0SZi9Vwqpkq3APtWH4DgPJpAjWOzzHneUcnPrZxqkFOoDCkFgWfRS3HEVrveLnk%2F5o8x37wWBbL862f7zDoYJjhPvkMOPlJxX86Cdae0Rrr1LAUEPPn3DUhsw2CEn%2FHUD5Ui6qYF5mpTTQK0%2F5CQnoYa3zMWuPfJekiIodMlkyjIt9KHxkJQOtYWmhP7VwkuQbMtZENbWDK%2BR9AVeAxmlDmQ%2FgU8HEgRGnGpgBOvb4IX8JowRXMSQoWgZPG7XSXKp27zS0Ox9m%2B0F6TujWi0bqQWkju8kgQYdgOmqEGasGe43BuUpLaah7852TPNFGGeb2o%2FilgYA8RVdmVNFtVY6rIbVKaezqUSPxIvWzYFaQzy9zlikntQlvDme6KmYjzSuUPk83%2BsdfNkUcFsBClvTjQuNNlE90QJ1PYInuG4L3sW08Hwx4MNtKMGEZQFF5glh1azohsgfHj3NQv2AlVSTv8bbrtGgQniJnWHaSWBcvjzk4O3kvXy9k%2BQoqCQcGtUbOkClxTLiy6b0mHzG%2Fqx2WS7l0hsOQJD3Na6Fx%2F9QF8x%2BMJrua1QF%2FVbPxBwfqrthgDv6Jx%2FrxG0o8Ff0J6eUnOKrRG%2B2vzPmHin4Ppnfpc6F4QcCSMLOMnVFIYgEdIYqGVzE%2FVODCZt7zUBjqkAUF%2Fug2%2FuMLEs9hSb9OMWarDmCe67UArqgaQnQu7x%2BSlu6WJjfvHg0bQdOoHOgBPm7Pm8fm4i4i9yysJkndJCnkvU%2FhrzgV6D6%2FAmCdL9OcSPj34qhpAYaDWuesFQX9pMM%2FHt8FKKNeFnrEGoEzCt0YxeXAAQDDmgn7rbvtOaR2aqP8JxZ%2BAg0n%2FyKpnGshPP69f%2B67eStcP9gOspluyr7ENzzt0&X-Amz-Signature=8c7ef85076eb32775e0080874807f08d9d63a390e031c478a6bfdd17d8f49ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTFG5W53%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T194042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCyTuQUT38Jp5%2BttejdnAbJ9BCWOsVJPol7K%2BTnH4JEsAIhAMRP4otclkdbD1hITP5QnEC40KIDUYCtCRPoh8xWdz06Kv8DCCIQABoMNjM3NDIzMTgzODA1Igzvn00go0SZi9Vwqpkq3APtWH4DgPJpAjWOzzHneUcnPrZxqkFOoDCkFgWfRS3HEVrveLnk%2F5o8x37wWBbL862f7zDoYJjhPvkMOPlJxX86Cdae0Rrr1LAUEPPn3DUhsw2CEn%2FHUD5Ui6qYF5mpTTQK0%2F5CQnoYa3zMWuPfJekiIodMlkyjIt9KHxkJQOtYWmhP7VwkuQbMtZENbWDK%2BR9AVeAxmlDmQ%2FgU8HEgRGnGpgBOvb4IX8JowRXMSQoWgZPG7XSXKp27zS0Ox9m%2B0F6TujWi0bqQWkju8kgQYdgOmqEGasGe43BuUpLaah7852TPNFGGeb2o%2FilgYA8RVdmVNFtVY6rIbVKaezqUSPxIvWzYFaQzy9zlikntQlvDme6KmYjzSuUPk83%2BsdfNkUcFsBClvTjQuNNlE90QJ1PYInuG4L3sW08Hwx4MNtKMGEZQFF5glh1azohsgfHj3NQv2AlVSTv8bbrtGgQniJnWHaSWBcvjzk4O3kvXy9k%2BQoqCQcGtUbOkClxTLiy6b0mHzG%2Fqx2WS7l0hsOQJD3Na6Fx%2F9QF8x%2BMJrua1QF%2FVbPxBwfqrthgDv6Jx%2FrxG0o8Ff0J6eUnOKrRG%2B2vzPmHin4Ppnfpc6F4QcCSMLOMnVFIYgEdIYqGVzE%2FVODCZt7zUBjqkAUF%2Fug2%2FuMLEs9hSb9OMWarDmCe67UArqgaQnQu7x%2BSlu6WJjfvHg0bQdOoHOgBPm7Pm8fm4i4i9yysJkndJCnkvU%2FhrzgV6D6%2FAmCdL9OcSPj34qhpAYaDWuesFQX9pMM%2FHt8FKKNeFnrEGoEzCt0YxeXAAQDDmgn7rbvtOaR2aqP8JxZ%2BAg0n%2FyKpnGshPP69f%2B67eStcP9gOspluyr7ENzzt0&X-Amz-Signature=371e69e02a1439b3ba8b7c1bdcbdd32365bfc050e0ba6047a37e09c55688f5a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







