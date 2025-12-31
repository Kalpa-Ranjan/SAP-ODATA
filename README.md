



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LNPFD2W%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T011824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnef2SA29jwNBmjWnj%2BpnZvVbfdAz9sXnKvqNEPZmMvwIhAJfZdHGBwpcj0ovGiMf66nEoU5ahgL1kRbnOAxS2MCpPKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytLlYnVLTEgW0wYxQq3AObM9HoyN1rEUueuiEDrcbOJO3qQHCfXevADqTpyrgc4OByex2IEAMxRvN32JyvbPvcRpr2JXRH2rdwznMXO%2B8mM57Aeqs6bK9Dg6QVwhLDN4d1U9w0XU1GQoG4PCDflD%2FBGAbT9%2BGuhnFmc6mOTGWLMxrZwJ2bs11nlBI152d2BQUqUnUIF7BRJR4gazQWy4McUW9uPmtOAyLMGIgTztF4H7dfcB7n6ziI0rGmVkEu1SKFNNN52W%2FJwVxjTS0uicBUSN3nnB8t0t5BdJ%2FDHaiLId97egyGjch0Guvf0jrj1alIhH%2BZx7MKW7EjulUGzzGX16iqdIMizDdb1aPeMIEHhZm0GXv1liWn2ItKcgIbm2rURRJIbbV4tVXB5uLx%2Fj9aelhsogTJrRQUqbghUpmmWh7OrrXrQ7MhMwJrRbfHdox%2FX%2FVpJuZ8ynqcmu6HO9PFUzXutzZhIZdxG09FHg1hjSHGEbSzx9trnXFdqWuTQGVj%2FQK0E2pWnufP7dnDdAtJWiIJC1Lv7u7HxbkVEqBgfEPQu6lPDTVfTkG9rL8x30dNgxrse3l5qWQPmAGKqjWohTOFWYV%2BLIyR4i74PiaIbOYY%2FN8jtck8Im3qrP26KN2xShpRRCQ6K0%2FyHDD31dDKBjqkAb0ecwj1wigpnfKsZq%2Fq1IE75p0JsbFkw8rnf7MuNABDj8mYmNqAGMncO6R7uLiYQAhYu5IhxDFzujTntkkH0PGruvQHwRDufzU7J8uGaoUu%2Fl%2FBPE9s9QMm%2FaMLGTNrnVoTaxcF2gcFzOUaV6hcqiazq79Gdks%2B9LT6p9KZS2MWE288BY5d%2FzikrhbjYjCtF6JHDdu0qJFVxuqPclgnjVXx55Vw&X-Amz-Signature=4ff360c0f31034b0179404932120c9128cbf96f3cfb50679f89a49eb59b15bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LNPFD2W%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T011825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnef2SA29jwNBmjWnj%2BpnZvVbfdAz9sXnKvqNEPZmMvwIhAJfZdHGBwpcj0ovGiMf66nEoU5ahgL1kRbnOAxS2MCpPKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytLlYnVLTEgW0wYxQq3AObM9HoyN1rEUueuiEDrcbOJO3qQHCfXevADqTpyrgc4OByex2IEAMxRvN32JyvbPvcRpr2JXRH2rdwznMXO%2B8mM57Aeqs6bK9Dg6QVwhLDN4d1U9w0XU1GQoG4PCDflD%2FBGAbT9%2BGuhnFmc6mOTGWLMxrZwJ2bs11nlBI152d2BQUqUnUIF7BRJR4gazQWy4McUW9uPmtOAyLMGIgTztF4H7dfcB7n6ziI0rGmVkEu1SKFNNN52W%2FJwVxjTS0uicBUSN3nnB8t0t5BdJ%2FDHaiLId97egyGjch0Guvf0jrj1alIhH%2BZx7MKW7EjulUGzzGX16iqdIMizDdb1aPeMIEHhZm0GXv1liWn2ItKcgIbm2rURRJIbbV4tVXB5uLx%2Fj9aelhsogTJrRQUqbghUpmmWh7OrrXrQ7MhMwJrRbfHdox%2FX%2FVpJuZ8ynqcmu6HO9PFUzXutzZhIZdxG09FHg1hjSHGEbSzx9trnXFdqWuTQGVj%2FQK0E2pWnufP7dnDdAtJWiIJC1Lv7u7HxbkVEqBgfEPQu6lPDTVfTkG9rL8x30dNgxrse3l5qWQPmAGKqjWohTOFWYV%2BLIyR4i74PiaIbOYY%2FN8jtck8Im3qrP26KN2xShpRRCQ6K0%2FyHDD31dDKBjqkAb0ecwj1wigpnfKsZq%2Fq1IE75p0JsbFkw8rnf7MuNABDj8mYmNqAGMncO6R7uLiYQAhYu5IhxDFzujTntkkH0PGruvQHwRDufzU7J8uGaoUu%2Fl%2FBPE9s9QMm%2FaMLGTNrnVoTaxcF2gcFzOUaV6hcqiazq79Gdks%2B9LT6p9KZS2MWE288BY5d%2FzikrhbjYjCtF6JHDdu0qJFVxuqPclgnjVXx55Vw&X-Amz-Signature=6a357f8a4c7d2f3e0fb09d3dde4770f693a2e36a0887e4bacb806d46b94a4f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







