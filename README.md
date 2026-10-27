



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6ZEQURR%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T121156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIAJlC7Jul5qKjukaPOI5Hd4yrC6uo6Cdpf0t%2FLXPUdB4AiEA293kcHdAmvurBTF9XEKvPLqNEevmHE5Su%2BDe3o%2F5y7kqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZWSVFfHrw0wPxaICrcA%2B9t0cjlepk8Dda8EPZq7NMtdUy57ntAk2Myqim4dy8tHXFXMWUj6h77TtJuawci4KObDJqrqNqnJEGAtW5V5SGT6k1aCz2Td8ihaB8rwwkzwdQHIR40NZU%2FuuPYMB1N87P8alc5kE2wyG06W98qvF8W0X%2FS5GOn98m7QtlR6hGBDwB8dEIBzEkHhLZ7kJOpTGDGOj9q9HiL0UzE8s%2BOq62yxGTlOq0ZKAcZ0AmOTzPcXXnFfJvwVwhDJgH4wNdZ4Y5uWfY4sZnQfB9XI7uoc2RUdP5%2FFPNW1fyBJXT77LWxLZtSO5Aq3cDodKobdcEXCzkAuZ8PXXgJCOaPffgVaup%2F%2BL0MYc03RLRq2OLcfC6xb5fE%2FAb%2BV5%2FwMl3e92F2eATNWPbUbdZCSODwupHCjEujljuYxM46blkENeJYcyG3BOeWGuMiDyaXzdyp%2B8q4X%2FnA0Q2lBhWj6svsNaiKgox4nxG%2FyVUjREczNgdEBNUFhApUNUGStbqmMJYkZPmiXjvSdnECd2S6ogwZXaSmrKBzFvxTY9UKi%2FPnQ%2Bz6YOzU2Lr%2BEA1dZhQR%2BvseTA9fHx68jchqEGy8D1g0eMnAuXJMvODMVKQspub0jZk2%2BiMCUzMWCMh%2BfAo9AXveMJCKgtcGOqUBMtivr9v32Lelu7FuqJn%2FsOwfsf3V8bxB8XEKo8OD3hqH4SLn%2FOwSCCyKG9v6rsIttEgtvvY3pk51HwIJxkFYDzSxvUq70V%2FtWhnb7ihNao0MLCFocqIp6daPWZIZQCjM%2Buze2NExAg6YdonC20rwRt95FGLgtmHbZraq60yUIEow7%2BZs3WxvQFfP1A9yUFgrbixps%2Ba3b6b6Ho4oQX6lLZK5pma1&X-Amz-Signature=4067faa6d879e3fec0dbb466b0aded611cded332f935c172df1fa60f9c547e5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6ZEQURR%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T121156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIAJlC7Jul5qKjukaPOI5Hd4yrC6uo6Cdpf0t%2FLXPUdB4AiEA293kcHdAmvurBTF9XEKvPLqNEevmHE5Su%2BDe3o%2F5y7kqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZWSVFfHrw0wPxaICrcA%2B9t0cjlepk8Dda8EPZq7NMtdUy57ntAk2Myqim4dy8tHXFXMWUj6h77TtJuawci4KObDJqrqNqnJEGAtW5V5SGT6k1aCz2Td8ihaB8rwwkzwdQHIR40NZU%2FuuPYMB1N87P8alc5kE2wyG06W98qvF8W0X%2FS5GOn98m7QtlR6hGBDwB8dEIBzEkHhLZ7kJOpTGDGOj9q9HiL0UzE8s%2BOq62yxGTlOq0ZKAcZ0AmOTzPcXXnFfJvwVwhDJgH4wNdZ4Y5uWfY4sZnQfB9XI7uoc2RUdP5%2FFPNW1fyBJXT77LWxLZtSO5Aq3cDodKobdcEXCzkAuZ8PXXgJCOaPffgVaup%2F%2BL0MYc03RLRq2OLcfC6xb5fE%2FAb%2BV5%2FwMl3e92F2eATNWPbUbdZCSODwupHCjEujljuYxM46blkENeJYcyG3BOeWGuMiDyaXzdyp%2B8q4X%2FnA0Q2lBhWj6svsNaiKgox4nxG%2FyVUjREczNgdEBNUFhApUNUGStbqmMJYkZPmiXjvSdnECd2S6ogwZXaSmrKBzFvxTY9UKi%2FPnQ%2Bz6YOzU2Lr%2BEA1dZhQR%2BvseTA9fHx68jchqEGy8D1g0eMnAuXJMvODMVKQspub0jZk2%2BiMCUzMWCMh%2BfAo9AXveMJCKgtcGOqUBMtivr9v32Lelu7FuqJn%2FsOwfsf3V8bxB8XEKo8OD3hqH4SLn%2FOwSCCyKG9v6rsIttEgtvvY3pk51HwIJxkFYDzSxvUq70V%2FtWhnb7ihNao0MLCFocqIp6daPWZIZQCjM%2Buze2NExAg6YdonC20rwRt95FGLgtmHbZraq60yUIEow7%2BZs3WxvQFfP1A9yUFgrbixps%2Ba3b6b6Ho4oQX6lLZK5pma1&X-Amz-Signature=e924bc64022334a4102d3227f371a5c89e8b0d8959df7de2be6f0ce03d4cd2fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







