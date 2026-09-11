



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TIIABOR%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T180830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAYvgjrRuaEHu0%2FIBvsOXv%2BMgHO8aNLkRwi9GkPAbhE8AiBelu9kTDmE4g0TFvFbxAIkVlkKCceKKyX425JF%2B16FwSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5S5XotqGWosLeZimKtwD615rZ8VRSNX6mwCuco5TZYVKOUIVENzXXqBvN1CxHSBt4EMNwe9pfFJM09GHNJRW5WUwBEUh8LdzeRDs9BqgrUaUIWuS6oT8HOdVYv9poJHEhD3At8ku08c2VKZ%2F5JzL7htQ334F9o%2BNqqMw0BZYEJaAzXaj%2FD%2BKcZcnDq9AWGxfV25oC1zu0lWseQihS5gr7gcmXQ94A4HH%2B9TfGA%2FqNXykAQRlTAyyI3sZnS2yzOdhj2GLGmXqSMrNIedX5RSvEsqCREgZursGU58YYEp70NhHYL81W9nFPHZF3d%2BEET%2F0Eybq8elB13VUsnLtIhVI19%2Fqc856yP0M8nPDsPLmuQT5VVh35qpkIzmaMlupOkN7g29zUTqlWOzTE7JoOMJDWytB2dVq8jqzcfJ5capBJxWbd4uS3y8oB1UkatSwbguAsZ0FZ1xH7ohdlrLRb9sQEjw2GxiLw0UKf7oFXcV5lH2z0MHVzpPX%2F6aOlm8Mv2mPJzzC6dYoi7nYVlzx5MfkMyZZqtQ3C8eu00yDPjbgAQ%2BVtKezbJdZeubrme8jaoNtBEsPk5sCb1OACK1dpDGa1sBNEnA00o82cn4htOw0U9JmO%2FReIJjysV%2BhNMIPU3YH9F1AGuWjldEVorgw5YKR1QY6pgGOIoZ8bioCSYIYNmlyK484inOnDeMDgnL13w89kY4Pqk1F2BJPIdJonbCpT5g94wF2MBfPGOh51YpCXx5DP3nBginLu2p0uHJ3c%2FKjZeLOMZXeOOHZQHNj6YcG3dw9vJQUjhDp4C1mLuqNPWTocgPKbMGECWx02bww5IdBH4%2FNpin1lAjWjA8sxTO4LSYvV80jAQETcJ28cBnr%2Fts8%2BE7B6yiJgMpj&X-Amz-Signature=99b5092a7da25f34494dc15f85a2115f962d69a033cfe75b55b27af15983c521&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TIIABOR%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T180830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAYvgjrRuaEHu0%2FIBvsOXv%2BMgHO8aNLkRwi9GkPAbhE8AiBelu9kTDmE4g0TFvFbxAIkVlkKCceKKyX425JF%2B16FwSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5S5XotqGWosLeZimKtwD615rZ8VRSNX6mwCuco5TZYVKOUIVENzXXqBvN1CxHSBt4EMNwe9pfFJM09GHNJRW5WUwBEUh8LdzeRDs9BqgrUaUIWuS6oT8HOdVYv9poJHEhD3At8ku08c2VKZ%2F5JzL7htQ334F9o%2BNqqMw0BZYEJaAzXaj%2FD%2BKcZcnDq9AWGxfV25oC1zu0lWseQihS5gr7gcmXQ94A4HH%2B9TfGA%2FqNXykAQRlTAyyI3sZnS2yzOdhj2GLGmXqSMrNIedX5RSvEsqCREgZursGU58YYEp70NhHYL81W9nFPHZF3d%2BEET%2F0Eybq8elB13VUsnLtIhVI19%2Fqc856yP0M8nPDsPLmuQT5VVh35qpkIzmaMlupOkN7g29zUTqlWOzTE7JoOMJDWytB2dVq8jqzcfJ5capBJxWbd4uS3y8oB1UkatSwbguAsZ0FZ1xH7ohdlrLRb9sQEjw2GxiLw0UKf7oFXcV5lH2z0MHVzpPX%2F6aOlm8Mv2mPJzzC6dYoi7nYVlzx5MfkMyZZqtQ3C8eu00yDPjbgAQ%2BVtKezbJdZeubrme8jaoNtBEsPk5sCb1OACK1dpDGa1sBNEnA00o82cn4htOw0U9JmO%2FReIJjysV%2BhNMIPU3YH9F1AGuWjldEVorgw5YKR1QY6pgGOIoZ8bioCSYIYNmlyK484inOnDeMDgnL13w89kY4Pqk1F2BJPIdJonbCpT5g94wF2MBfPGOh51YpCXx5DP3nBginLu2p0uHJ3c%2FKjZeLOMZXeOOHZQHNj6YcG3dw9vJQUjhDp4C1mLuqNPWTocgPKbMGECWx02bww5IdBH4%2FNpin1lAjWjA8sxTO4LSYvV80jAQETcJ28cBnr%2Fts8%2BE7B6yiJgMpj&X-Amz-Signature=b3297b4755edde8ef453abd49884b6a291112d36ddfeb219a4cc842d39724491&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







