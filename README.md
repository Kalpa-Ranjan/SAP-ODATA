



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CERJBLU%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T134139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCijDoa9UVcg7w3q8bFRp38jtiSAioqwV3ir0V%2F1IomMAIgOSSRZYApnQnMODIuxxd7Hx7aBVuG734kdQ2630SfRGgqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwwL7oUEnuRsm%2BOVCrcA3ovwoSbY%2B%2FsMfghMeSu472H6g9wSayYs6g%2B8lIecMxQPeIvichHlIIVDeZAsUm93tnN4hLgL%2FO5tOIIXKZKjCMJtAtz1Kvb7FRtDUVTqZp3P7ReFvaE1uQqpYA%2F6oY3nOm8NwLlwlkVTg3KR3GT6hfXIudtC8NOWxrZFM3s%2BiK%2BkkK7u%2BAUoCgYhfqJicALaotHN5rEcK1nBYz1tgN%2FJvxieoQghX22mGui6wNma40Uhy%2BqotbjegrKPGHqI3Lm2O9UAaaSoxS6LqkFn3Lb5T4n4EgHZec2iAxNDzvtnxWtOTkhAXHefmgk5Iohi0Tk9E7Q0vH%2BVLisqzCWpdo%2BSQCED0iefL%2Bw7%2FpUq96dZM0K29jz6cNih48HBE0gNX0ejkUg5b4iIXCYTyQDXQ9uDBwTBa1HVW4MS6ytXZK%2BibLwH55UyWFeTbUYxpf%2FxMNYxILi3H3XqeD5NFMkfcWMzw%2Bm7iXAar4%2FoksVXP1l4beiHQPBf47SAspPkdbf5mkdaVyoNS45r1OCwAlcxFtzy8JwGAuXpyVrAutmAxMMdLJbYhWE9iKjaxNzXM7u9Too3hatH1nB9V4sqlyqTo0ERAR%2FiD7c%2FonmNnKLR262U%2BRz3Rwxh1y%2B3KQesZM8MKP%2Bg9YGOqUBxKVJuyFEnGNpikSEOI7JG0PpTnkN5GPuBvMAshe9%2B4zBDeLIzTVD2zi9yIpasunnsyVoads1b2dTJYU8YkxjJ0ipMeyPw6xcUxfrAZ7T7tQrJ4gOm41o7eaGTSAO5KvMrqrNfvnZAbsjSiLk7dSO2QsSO8G2CQdpA7qGQ%2Fi7CeonDVgm%2FzTuQ3yvcb%2BTlX7WTZ5EKcv4FqNQ7RQZF%2BgHPQmcsJhx&X-Amz-Signature=3b0aae6810fa7d2c58c9e8bc9e34ed696ecea0fcfc9d4576c6c4adc6f997ff04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CERJBLU%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T134139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCijDoa9UVcg7w3q8bFRp38jtiSAioqwV3ir0V%2F1IomMAIgOSSRZYApnQnMODIuxxd7Hx7aBVuG734kdQ2630SfRGgqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMwwL7oUEnuRsm%2BOVCrcA3ovwoSbY%2B%2FsMfghMeSu472H6g9wSayYs6g%2B8lIecMxQPeIvichHlIIVDeZAsUm93tnN4hLgL%2FO5tOIIXKZKjCMJtAtz1Kvb7FRtDUVTqZp3P7ReFvaE1uQqpYA%2F6oY3nOm8NwLlwlkVTg3KR3GT6hfXIudtC8NOWxrZFM3s%2BiK%2BkkK7u%2BAUoCgYhfqJicALaotHN5rEcK1nBYz1tgN%2FJvxieoQghX22mGui6wNma40Uhy%2BqotbjegrKPGHqI3Lm2O9UAaaSoxS6LqkFn3Lb5T4n4EgHZec2iAxNDzvtnxWtOTkhAXHefmgk5Iohi0Tk9E7Q0vH%2BVLisqzCWpdo%2BSQCED0iefL%2Bw7%2FpUq96dZM0K29jz6cNih48HBE0gNX0ejkUg5b4iIXCYTyQDXQ9uDBwTBa1HVW4MS6ytXZK%2BibLwH55UyWFeTbUYxpf%2FxMNYxILi3H3XqeD5NFMkfcWMzw%2Bm7iXAar4%2FoksVXP1l4beiHQPBf47SAspPkdbf5mkdaVyoNS45r1OCwAlcxFtzy8JwGAuXpyVrAutmAxMMdLJbYhWE9iKjaxNzXM7u9Too3hatH1nB9V4sqlyqTo0ERAR%2FiD7c%2FonmNnKLR262U%2BRz3Rwxh1y%2B3KQesZM8MKP%2Bg9YGOqUBxKVJuyFEnGNpikSEOI7JG0PpTnkN5GPuBvMAshe9%2B4zBDeLIzTVD2zi9yIpasunnsyVoads1b2dTJYU8YkxjJ0ipMeyPw6xcUxfrAZ7T7tQrJ4gOm41o7eaGTSAO5KvMrqrNfvnZAbsjSiLk7dSO2QsSO8G2CQdpA7qGQ%2Fi7CeonDVgm%2FzTuQ3yvcb%2BTlX7WTZ5EKcv4FqNQ7RQZF%2BgHPQmcsJhx&X-Amz-Signature=2c5c9f26e8ea40ddb5f3917c8f54ce00a418c4fa08bfe00ff68f9e33ebeeeaf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







