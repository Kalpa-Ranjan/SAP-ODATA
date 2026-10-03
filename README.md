



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCCEWJUM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T183820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC40tmzHp3f%2FL%2FHWXTD0H%2FlXx3vPOJko7izdgnk%2FT13FAIgEqeD543V5Iuywd6dfSx8CIb3O52BQzO6whSdomSbFtEqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBKsUwOMsKLPqZyzUyrcA8Gh6rMS6U1zP6c%2BiNHeC6A4TlSyvkgjZ8X%2Fgn5sYeQw84p%2FmXzwZ2tm8TaklCyGRX5tCHNE3l9Sf2NsxmLjzszcLg9Gii6CQ%2BzpBj9QwdIWV3Uf8fZKJFmKdue86tG08MjmpVd7Oo8p2O8sqw6sj56Cs9OkXopx7aJEOgtb8V0Vmdgcc9azC%2Fp4HAb06YYA%2FSKqGnbwO2DKAiIsJuCRbpdM3d5XJaTPW6dOGNYrksWO8Zc3QRAYEnhARQ20L0jGRJhfuHz%2Bpp98rT84Mm%2FWNRjqeGxnIoPNIJ24XU58vQ8ojNOulXdmcJcEtfeRWbk7Qw%2B7WY53ibi82OOt3g6WsXCeEXf%2BBUFNhdLE2zIBtZryA3n1ucxjlFwul3TXfbdy2Q%2B7uo3Z3lhT18v50Zc8tZkSqGFV7K0I9PDNQeLtXjRInH102OXz%2B2XZqeDEpKOOIRFv48SlZA6hrTL698RFlzLrGtEUVEgOH%2FJtzg%2Feile8I0u7XHspaQBbTXUsm6%2FBfmSeRKjKMXnXgiZwBM4WsZwAGOWeqqV3R3Ez1nLigLGHrNWkKPGbPZEsKgu%2FXeYsijEH6ILX1qTIT8zXTYg8rj2%2F3iBX2P40KsOg9f7iGEkrEZKnH82T9vEGalBbMLf0hNYGOqUBt5%2Fq%2FF9TH1sc%2FcifDYSDm3IdCd5gQZcfzIw8f5bowvoXSEeGryk%2FDJxrslOWGZ%2F6JFhwXxpaejhJ4fGbIBUKh5xTJueLC4i4cMGoHgbxyIlgGcI6vC1ek4e5DCvpP3g2GtZc9h9zP06n9TUF8dr%2FgZBqRhJUB1f4wwfA6RXUScgzTMcqlLm0IdDyZwp%2BpeO2ljqKpaEYdiPHZknEtUE3pnxTpR7I&X-Amz-Signature=f93f404c6346021c43544deb114e2a0f4e462e3190012ef3453bbbab9f9208c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCCEWJUM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T183820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC40tmzHp3f%2FL%2FHWXTD0H%2FlXx3vPOJko7izdgnk%2FT13FAIgEqeD543V5Iuywd6dfSx8CIb3O52BQzO6whSdomSbFtEqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBKsUwOMsKLPqZyzUyrcA8Gh6rMS6U1zP6c%2BiNHeC6A4TlSyvkgjZ8X%2Fgn5sYeQw84p%2FmXzwZ2tm8TaklCyGRX5tCHNE3l9Sf2NsxmLjzszcLg9Gii6CQ%2BzpBj9QwdIWV3Uf8fZKJFmKdue86tG08MjmpVd7Oo8p2O8sqw6sj56Cs9OkXopx7aJEOgtb8V0Vmdgcc9azC%2Fp4HAb06YYA%2FSKqGnbwO2DKAiIsJuCRbpdM3d5XJaTPW6dOGNYrksWO8Zc3QRAYEnhARQ20L0jGRJhfuHz%2Bpp98rT84Mm%2FWNRjqeGxnIoPNIJ24XU58vQ8ojNOulXdmcJcEtfeRWbk7Qw%2B7WY53ibi82OOt3g6WsXCeEXf%2BBUFNhdLE2zIBtZryA3n1ucxjlFwul3TXfbdy2Q%2B7uo3Z3lhT18v50Zc8tZkSqGFV7K0I9PDNQeLtXjRInH102OXz%2B2XZqeDEpKOOIRFv48SlZA6hrTL698RFlzLrGtEUVEgOH%2FJtzg%2Feile8I0u7XHspaQBbTXUsm6%2FBfmSeRKjKMXnXgiZwBM4WsZwAGOWeqqV3R3Ez1nLigLGHrNWkKPGbPZEsKgu%2FXeYsijEH6ILX1qTIT8zXTYg8rj2%2F3iBX2P40KsOg9f7iGEkrEZKnH82T9vEGalBbMLf0hNYGOqUBt5%2Fq%2FF9TH1sc%2FcifDYSDm3IdCd5gQZcfzIw8f5bowvoXSEeGryk%2FDJxrslOWGZ%2F6JFhwXxpaejhJ4fGbIBUKh5xTJueLC4i4cMGoHgbxyIlgGcI6vC1ek4e5DCvpP3g2GtZc9h9zP06n9TUF8dr%2FgZBqRhJUB1f4wwfA6RXUScgzTMcqlLm0IdDyZwp%2BpeO2ljqKpaEYdiPHZknEtUE3pnxTpR7I&X-Amz-Signature=947935f9561c106f33e8518f194dde7ca0e85eeabda9f3b050e9229815a8b7f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







