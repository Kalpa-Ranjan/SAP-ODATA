



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ42M3WH%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T020747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcZYu%2F20I022E12%2BCQPdXjnmJAMjSZ5KjadVf0CpxTSgIhANNUPbnmv%2FCXe9bCtnoPSiwlxXezAdJwHMORtOUVr1u7KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUIdKbJZHi4rkspo0q3AM7hk4CJkFSHVB%2BYo16BuR3%2FK%2BXd6LuaGcfKq%2F9N9IKqj7iQPqNERnb0FU3c7qGz%2Fgm3kU0l24AiuMJAQUXjgSx%2FIPVFmGWheXOQtJlOvXQ%2Bfz7NJQXlSC6j60gDsz8ZP1fWst9DnZpMs%2BJIBcW5LtMPDN855aJ8xtxCsi5fDxIspIYi7Zacbywa0RTjpSZjKd8uOMg5LAD5l7SRISX1lO2tys%2BO9W2TWLUaD17CLR8Zt8T2xzjifAY3EAfKXGi3P9kDZjMBoVRLC03Yj4zH8Z7rqvxbyhOB7iFbQVP79TUuNAmPTMqyZKUWPpa66IAvuAHIUzabJULnn7l%2FH5efaBBWwnDpJ24RopgSzfZu0ft37gLz2Tk67LBp3cruyeau7HMAy9wgQkd5VdbHwbO%2Fc0d6JpS1XB%2FjFUZd016pS5OMKT%2FMvvKa%2FHDDmKGvlWYrjRpfXzrjeTOcnryv0CO4WjVUY82hsUsT%2BmrBhj4T0bVxwhwVq5CdBBvkmiURkqzn4tLH7%2BYO3MOYFeAPI1150yDGO9qAqQxAHjHI7jmdlZRMl4z9ybjG2I40akyUU0JR1WBqfn%2B4nhLxqqVjObx8EFQLl0rt7qoEBVe074N8db8eoeKsA1ax8NGOaiLDDDg0cXSBjqkAfeNuBGj%2F%2B8GzcBfkhyfCv73RWVP9XxiRO8%2BWANze%2BpxChJsudmS6KAUUvy3ir3%2FqkaWVhiOBhNyAZ6I46P%2BvyvdA4aHDyPjxBCBF2aVp5eY5hU5%2Fz3Ei4ufMK4%2Fl7Llkuuvhf037DtuQ%2B5pMZTr7DgNCxttAirDnICtBvcB9MFPRf3oICIpRWFLQGfTAhngxktibz0ESH0j6KqmJJ2MxF%2BoMbKo&X-Amz-Signature=03ad08f988a8aeba790caa55db05e447b5947fd567b9ddfbc63ae749aa86dd03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ42M3WH%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T020748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcZYu%2F20I022E12%2BCQPdXjnmJAMjSZ5KjadVf0CpxTSgIhANNUPbnmv%2FCXe9bCtnoPSiwlxXezAdJwHMORtOUVr1u7KogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUIdKbJZHi4rkspo0q3AM7hk4CJkFSHVB%2BYo16BuR3%2FK%2BXd6LuaGcfKq%2F9N9IKqj7iQPqNERnb0FU3c7qGz%2Fgm3kU0l24AiuMJAQUXjgSx%2FIPVFmGWheXOQtJlOvXQ%2Bfz7NJQXlSC6j60gDsz8ZP1fWst9DnZpMs%2BJIBcW5LtMPDN855aJ8xtxCsi5fDxIspIYi7Zacbywa0RTjpSZjKd8uOMg5LAD5l7SRISX1lO2tys%2BO9W2TWLUaD17CLR8Zt8T2xzjifAY3EAfKXGi3P9kDZjMBoVRLC03Yj4zH8Z7rqvxbyhOB7iFbQVP79TUuNAmPTMqyZKUWPpa66IAvuAHIUzabJULnn7l%2FH5efaBBWwnDpJ24RopgSzfZu0ft37gLz2Tk67LBp3cruyeau7HMAy9wgQkd5VdbHwbO%2Fc0d6JpS1XB%2FjFUZd016pS5OMKT%2FMvvKa%2FHDDmKGvlWYrjRpfXzrjeTOcnryv0CO4WjVUY82hsUsT%2BmrBhj4T0bVxwhwVq5CdBBvkmiURkqzn4tLH7%2BYO3MOYFeAPI1150yDGO9qAqQxAHjHI7jmdlZRMl4z9ybjG2I40akyUU0JR1WBqfn%2B4nhLxqqVjObx8EFQLl0rt7qoEBVe074N8db8eoeKsA1ax8NGOaiLDDDg0cXSBjqkAfeNuBGj%2F%2B8GzcBfkhyfCv73RWVP9XxiRO8%2BWANze%2BpxChJsudmS6KAUUvy3ir3%2FqkaWVhiOBhNyAZ6I46P%2BvyvdA4aHDyPjxBCBF2aVp5eY5hU5%2Fz3Ei4ufMK4%2Fl7Llkuuvhf037DtuQ%2B5pMZTr7DgNCxttAirDnICtBvcB9MFPRf3oICIpRWFLQGfTAhngxktibz0ESH0j6KqmJJ2MxF%2BoMbKo&X-Amz-Signature=8bbb9c452fb6844b1a18000d97192e115ee46e89a1957fa3384dcc4e829defc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







