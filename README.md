



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UJACSTS%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T002119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCLh9W%2FeIkhLzV6TKpiPqmVPq89R8VohhMp4B%2Fst%2FpvjwIhAIR7g%2BmR7dSz%2FWAweMyrIGBgkKZmwd80jAdyoKaZCv7GKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2F8LS8pcsHN7mgD4q3AM%2BbC00oL5hJlkANrzKQPs6PuoAdCua3R63wEtP0sje93K2MbZt6F3unu9lbw85qajQWilO22pof%2Bzo0I%2FboerLxCNq6w%2BercMNoM19oh6NWuy6E3vfFEt4sr1bCRDJ6su3KQbhRkGwFlkPtrySHfOuHhh8umcseymdPMhDUuInA6Q6AxFTpHAeFtZx74G1mfJd1V1hCBRmdlMMNJ3Ca%2B9sR6Hm3hPPltoC4IynbgpDAOXl5SYH93ahJfqF0iGAPQHvr47I6FRJ4ELxWn%2BIrkBdYhyMg5g26ucqWmRVNSqDHzAisEHSvKTNtoIML%2BcUTGoOsG2c0s2tCwV2MMqfLxc0mkY%2BZZBMbbBxDFBM1MdVIg5IpA6nQItvC%2BYyueDmYYcUlhQlR8gCDITJWcIvqvg3LhX%2By5hR5BUKDEdbByCBy6UKiCIajS1a2SVVTZPkmcybV4aXzLRxGfVN2bsDB3XXm3zbiP5ofnUJMYC78Eg3JSHM9SofX%2BTvV%2FP%2BVgL5b%2F8UFGbQeVJm10wFLboEUcyGqSV7uQ9ww5KIaIjdKx3a18GvBa%2F%2BMzkOlL7D4uMwxiNCzwtydH1%2BuTGeHkP5g%2B97vEDai4%2B6p5d4uU1W0UsUjv9UU%2BD6ZA2lAZfAjTDC0tbVBjqkAXouC4UOR%2Bh1sisWGxnEPaE6HgCW%2FGlMaGE82NQ57P45M%2FnlV5EGn8ZsvBJxiedtiyd5y5yVurHA%2BlE%2FixWzpVnB7qejsSu4YrHuAfIshpdDz7TowUKMLzaxukG0RLq8stEmLrQnhaApD5oEbuPAWbkf6fVaFp8K17WpYqkAxihY2HSbrTQ8%2Fm7iEcwRijQRDpJb05WgYW%2Be6BkIruLVeCKiH0MT&X-Amz-Signature=a7a901c6c2e8e6a0a147e353a6e6b84d72bb0e5cfbdf8c570ac6c43b5ecd7216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UJACSTS%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T002119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCLh9W%2FeIkhLzV6TKpiPqmVPq89R8VohhMp4B%2Fst%2FpvjwIhAIR7g%2BmR7dSz%2FWAweMyrIGBgkKZmwd80jAdyoKaZCv7GKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2F8LS8pcsHN7mgD4q3AM%2BbC00oL5hJlkANrzKQPs6PuoAdCua3R63wEtP0sje93K2MbZt6F3unu9lbw85qajQWilO22pof%2Bzo0I%2FboerLxCNq6w%2BercMNoM19oh6NWuy6E3vfFEt4sr1bCRDJ6su3KQbhRkGwFlkPtrySHfOuHhh8umcseymdPMhDUuInA6Q6AxFTpHAeFtZx74G1mfJd1V1hCBRmdlMMNJ3Ca%2B9sR6Hm3hPPltoC4IynbgpDAOXl5SYH93ahJfqF0iGAPQHvr47I6FRJ4ELxWn%2BIrkBdYhyMg5g26ucqWmRVNSqDHzAisEHSvKTNtoIML%2BcUTGoOsG2c0s2tCwV2MMqfLxc0mkY%2BZZBMbbBxDFBM1MdVIg5IpA6nQItvC%2BYyueDmYYcUlhQlR8gCDITJWcIvqvg3LhX%2By5hR5BUKDEdbByCBy6UKiCIajS1a2SVVTZPkmcybV4aXzLRxGfVN2bsDB3XXm3zbiP5ofnUJMYC78Eg3JSHM9SofX%2BTvV%2FP%2BVgL5b%2F8UFGbQeVJm10wFLboEUcyGqSV7uQ9ww5KIaIjdKx3a18GvBa%2F%2BMzkOlL7D4uMwxiNCzwtydH1%2BuTGeHkP5g%2B97vEDai4%2B6p5d4uU1W0UsUjv9UU%2BD6ZA2lAZfAjTDC0tbVBjqkAXouC4UOR%2Bh1sisWGxnEPaE6HgCW%2FGlMaGE82NQ57P45M%2FnlV5EGn8ZsvBJxiedtiyd5y5yVurHA%2BlE%2FixWzpVnB7qejsSu4YrHuAfIshpdDz7TowUKMLzaxukG0RLq8stEmLrQnhaApD5oEbuPAWbkf6fVaFp8K17WpYqkAxihY2HSbrTQ8%2Fm7iEcwRijQRDpJb05WgYW%2Be6BkIruLVeCKiH0MT&X-Amz-Signature=367f1902053e362bb1e56500f9e59034dfbd9e40e4af45d1769edda1daa1de71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







