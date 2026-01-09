



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4UY5BH%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T011914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpoukG7zN1ba88PFatWymQZ%2Fb9dlhyUfhHRQ4sVWZd7AiBlItALZ%2Bg8NDwwxoxfUMYZA3JKcygbRHpnZhAkQ1%2FXqSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMymqfn4Ke9A2yRCzlKtwDJ9O31mHmV6lBFzQr%2B4PaAPQtHmOaM8ukb8umjbE3GqH%2F05I5aes82dmeV8BYI4PY%2Fyr%2BLujwMpS62%2BWWPn%2Fdo1U41YL0FITksyJRqzXrVxX12NB7Rfc6BQ4UsrZMqTZcRdHgJhXZCagrhT3YAXEfn4nAxdMSnEovkRtNoHIfnmJNNLA3Dc46CyXt6XlCMHUcfuNuzyB0O7fJLmcw7%2Fow3T0njv6pLzEI7o5XtN28UpR6Bvj%2FBsqO5v%2F3sM7A%2BK5MLbSy9I7qidMt3HKxySNo5secnSNM%2BKiWwV3DPWFI7%2Ba6%2BivexnghDmGlXbhZL%2Fm4xZ7YdJAXfCdlDxbpcwmOuJFqhA%2Bay2kR0cJZDqWhD81MwBCx981ZnugOdBeAssshZ4m39G72YtQiGXY5BujqBzhWo1hktgPOG90zAw3gE24wC3xVfHRT1aCjeyo%2FGysJq%2F39fSBF1gRYzkoU8ieIwuslwHWvzuvJtnDQuLK9bPcgaso%2BaV0Rips69maBOHN%2FVdv0swJ2wyos6CmQxDOFftuJnYWZIHM1vn7MXjvE%2BBWlEVO%2B5u%2BedkNVz68DVI9Lg46iABOkxFYZLncSIftT2qv9gbIK8H%2BbAomWSNCFmtO2tMMao5JmDkoLLKswlaSBywY6pgG3z8uJ0K%2FrfGN2Pcb5FLhHU%2BrMvCfYGv7mn6UlPL%2Be83fZYvRII2aLwFYDH1lOZfpNnVzFtOtycrpH1MXjj9IZzoVM2siyNfTsV7mPKHofoUbiPQGDtcLw3RwwxEYHiwMfbjx%2Fqw%2F4kX0U8W6jlUqAYq1E5hkkddXFoR%2Fnk9B9%2F6o3ISnJGP0yMNKdgxr0tlo%2Bptm0O71i4a%2BO5LxzBVdZni6qSplg&X-Amz-Signature=3bcdb9dd9b498eef26994878db27ac4afdcc8a0034075cdf53924d7741072ce7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4UY5BH%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T011914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpoukG7zN1ba88PFatWymQZ%2Fb9dlhyUfhHRQ4sVWZd7AiBlItALZ%2Bg8NDwwxoxfUMYZA3JKcygbRHpnZhAkQ1%2FXqSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMymqfn4Ke9A2yRCzlKtwDJ9O31mHmV6lBFzQr%2B4PaAPQtHmOaM8ukb8umjbE3GqH%2F05I5aes82dmeV8BYI4PY%2Fyr%2BLujwMpS62%2BWWPn%2Fdo1U41YL0FITksyJRqzXrVxX12NB7Rfc6BQ4UsrZMqTZcRdHgJhXZCagrhT3YAXEfn4nAxdMSnEovkRtNoHIfnmJNNLA3Dc46CyXt6XlCMHUcfuNuzyB0O7fJLmcw7%2Fow3T0njv6pLzEI7o5XtN28UpR6Bvj%2FBsqO5v%2F3sM7A%2BK5MLbSy9I7qidMt3HKxySNo5secnSNM%2BKiWwV3DPWFI7%2Ba6%2BivexnghDmGlXbhZL%2Fm4xZ7YdJAXfCdlDxbpcwmOuJFqhA%2Bay2kR0cJZDqWhD81MwBCx981ZnugOdBeAssshZ4m39G72YtQiGXY5BujqBzhWo1hktgPOG90zAw3gE24wC3xVfHRT1aCjeyo%2FGysJq%2F39fSBF1gRYzkoU8ieIwuslwHWvzuvJtnDQuLK9bPcgaso%2BaV0Rips69maBOHN%2FVdv0swJ2wyos6CmQxDOFftuJnYWZIHM1vn7MXjvE%2BBWlEVO%2B5u%2BedkNVz68DVI9Lg46iABOkxFYZLncSIftT2qv9gbIK8H%2BbAomWSNCFmtO2tMMao5JmDkoLLKswlaSBywY6pgG3z8uJ0K%2FrfGN2Pcb5FLhHU%2BrMvCfYGv7mn6UlPL%2Be83fZYvRII2aLwFYDH1lOZfpNnVzFtOtycrpH1MXjj9IZzoVM2siyNfTsV7mPKHofoUbiPQGDtcLw3RwwxEYHiwMfbjx%2Fqw%2F4kX0U8W6jlUqAYq1E5hkkddXFoR%2Fnk9B9%2F6o3ISnJGP0yMNKdgxr0tlo%2Bptm0O71i4a%2BO5LxzBVdZni6qSplg&X-Amz-Signature=17da071b58f0ab9676a34a5122640bf5fbcf336404e31f05102f6db9dbb26e50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







