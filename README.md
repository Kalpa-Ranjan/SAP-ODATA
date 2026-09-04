



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDHCJTNP%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T153733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGaK8JIvtx8TT67UiJDEqvF2228a6hgE1DQEiRaYSOFfAiEAjqUBEr4eEqpe4f2sm6nYFPLyXfpJl8HnIhC1YFLWNVkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVWm7ZX2Fvk6lXrHSrcA3hjikLuLOejVKMsyHtTtnBML9ocY5uCrQj0pQRltjsU%2Fxw6sjzJWCt22OmPo0DWVkdPWWGYzX%2Bau04lHpb1mu5lMyb%2ByGIDVrx4LOxi951gy4XJuhiqgGvm9N7Asxo9m7GrVIU2ogOk9ppgTRhBIscGS2V0kzHR4nEGIMFa8byyrZcnCrHA6oqSadCEHkG6N2hmyGIBAaWKugjBqv2%2Fti8%2BxgsZCmcIok8bnKxmw8uXqA5QQ1uN%2B%2FlkHH967%2FmwX6C4UxxGnddhyVN6rkowEL1bTRrtFuuCRfuYIhlEQGmbu0eAlzK8xf51ZpbKdshACQPmahe0hyoHhZ48RlkouvuvilcWCVh1%2F2By%2FhKUO9m8PeqYB42V5zuy%2BmC1Jzy5sv%2B30pMy0Vdb3yjpiACGVn4lw7ii6jpTivqZpdJMJGfhEoGY1E4qO0QGrO2X46uD%2FcyVyv4pB3iNVVswTGdm8hREu4sfcB91SjoFRbn8FDsci80aaC4vmQzbkBEimC0EckIdv2eA9mh9jo1ijWPqU7KMO%2BDy5W9SUjiNnX7vFdiOkRsXbsrnnOW3CvOrMbPhH%2Bo44PnVIo2tOMpoZInNY4gxdYP0cUZLRdj64Rj1nR%2BIMzFbywLIB8ycdl9qMOi269QGOqUBvpGdt9BK9b%2FoPF7LDLfHVV5iOAftHR4Z2latQHTq2%2B0%2FBHk1kOU9teQAcyuLmfQT2I7b1hQK%2FjGQIm0cXwIrEOmMqv5bSa79V4LlGcelXH%2BiTGwNkBUr9LA1fGqZDAjAsQDKQMom%2Bz2XB7jjytGPiHJGJRrBrLKPpJUU6QnwvT0xDWeRV94x8P8zDN54PMoLroZHEUQneoFeNbVqZsoxrljvzONa&X-Amz-Signature=d41ef92b19c5913df708eb8fb30ca9fc766f38240f9f32f6c4296f722581d5de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDHCJTNP%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T153733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGaK8JIvtx8TT67UiJDEqvF2228a6hgE1DQEiRaYSOFfAiEAjqUBEr4eEqpe4f2sm6nYFPLyXfpJl8HnIhC1YFLWNVkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVWm7ZX2Fvk6lXrHSrcA3hjikLuLOejVKMsyHtTtnBML9ocY5uCrQj0pQRltjsU%2Fxw6sjzJWCt22OmPo0DWVkdPWWGYzX%2Bau04lHpb1mu5lMyb%2ByGIDVrx4LOxi951gy4XJuhiqgGvm9N7Asxo9m7GrVIU2ogOk9ppgTRhBIscGS2V0kzHR4nEGIMFa8byyrZcnCrHA6oqSadCEHkG6N2hmyGIBAaWKugjBqv2%2Fti8%2BxgsZCmcIok8bnKxmw8uXqA5QQ1uN%2B%2FlkHH967%2FmwX6C4UxxGnddhyVN6rkowEL1bTRrtFuuCRfuYIhlEQGmbu0eAlzK8xf51ZpbKdshACQPmahe0hyoHhZ48RlkouvuvilcWCVh1%2F2By%2FhKUO9m8PeqYB42V5zuy%2BmC1Jzy5sv%2B30pMy0Vdb3yjpiACGVn4lw7ii6jpTivqZpdJMJGfhEoGY1E4qO0QGrO2X46uD%2FcyVyv4pB3iNVVswTGdm8hREu4sfcB91SjoFRbn8FDsci80aaC4vmQzbkBEimC0EckIdv2eA9mh9jo1ijWPqU7KMO%2BDy5W9SUjiNnX7vFdiOkRsXbsrnnOW3CvOrMbPhH%2Bo44PnVIo2tOMpoZInNY4gxdYP0cUZLRdj64Rj1nR%2BIMzFbywLIB8ycdl9qMOi269QGOqUBvpGdt9BK9b%2FoPF7LDLfHVV5iOAftHR4Z2latQHTq2%2B0%2FBHk1kOU9teQAcyuLmfQT2I7b1hQK%2FjGQIm0cXwIrEOmMqv5bSa79V4LlGcelXH%2BiTGwNkBUr9LA1fGqZDAjAsQDKQMom%2Bz2XB7jjytGPiHJGJRrBrLKPpJUU6QnwvT0xDWeRV94x8P8zDN54PMoLroZHEUQneoFeNbVqZsoxrljvzONa&X-Amz-Signature=b684adce9d7861442cc3d49827f3059df6c791ad6f478c016e0e2f132d416412&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







