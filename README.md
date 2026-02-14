



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466545ISZZR%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T063822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIQCWW3oHnTTv%2FEM0RajflRgS3NVqNTrXuoNLIGdKluRqzAIgNkm5AmVhOsxVV%2Fd5FJ54fcl2IZ52j0lnKL%2BdiGKlikAqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4015ER8i%2FHNRoe1ircA8ddeOLDIAfTaIR%2BekJDQTpRSw5hw7RIk2X26ziEGkENe%2B6vvgXG5TbbNqDi2%2BnpRjW1kCFBjuJr0QtjSP4AFrb52ucw6zNny%2FpjPeAZXrIOF7PLJ0hspXpuzb0%2FU1CqTaXRE57OCpEpLFcSiDvZlWOXBpJALDe1hyJMmjbYccqJ30H%2B7X8DXvldfAY6eK65gL%2B51qiOrC%2FO33r1lzYwCyiyodmGN7DXEBuH3bXDQihXJkoTDKPmUfetwNEvoa%2FCKPpLqzVHTzNgN4VydSuXWhCyT65EoHAybAeZyaaPdA9AgHBNpl1WKY2BDP01kZHH8LayN0%2F1kaNaE1PsNkObicvkJ9puEO2uLDrZJwGqywPxtnvazLEbVE1uRgBpaRDfyAq5FUCKmOJpFOuMaKyrdX6NpduRuYwJI93DVeqTkJ3zdQBqcZ9KNf0Pvf7%2BW1bM%2B7Y8879%2Bx%2F15edrdhgJUXPSO8PgtkSWHSz1GNmJtZnOy8gZPkW9Pqxoq6uycCERrIrtOqGjEkCiUlvPvma0jZ%2BH1pcvhOSGtNjF5Y85SpkeXXTsh%2Fhy1x1CJuVW7iG6do%2BGVlsroq5x%2B2gJe%2Fg%2Fl8LFfXs6e3JBhvxPGXOzWrZiAwwKszEhP1oJzkVWgMJ2TwMwGOqUBpZzWWPwo19Y0omZy8Oib9YhdOXnPOlxDxJz7tRC6SgAl1z6qBbv%2FiAkIG94fQqU2BU3vZQWWPSxPI1en3Z1FNWa8Nq6QWhE1atIxZYszzmT%2Br0sRo7wzmGkmWoUVAm5gGpUv5LMiB0nL5mSmHqhwFR%2FhWmqRu1WyzNCI0sCWHtEWS%2FLMZo479ZU3FkC8uqEAkHjizSKtliAtC6wuz9%2F9avPLdYLy&X-Amz-Signature=724ed617b4dd2a23fab5d9909e31876f4033f0519cd16d90dcdd5115a36ab5fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466545ISZZR%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T063825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIQCWW3oHnTTv%2FEM0RajflRgS3NVqNTrXuoNLIGdKluRqzAIgNkm5AmVhOsxVV%2Fd5FJ54fcl2IZ52j0lnKL%2BdiGKlikAqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4015ER8i%2FHNRoe1ircA8ddeOLDIAfTaIR%2BekJDQTpRSw5hw7RIk2X26ziEGkENe%2B6vvgXG5TbbNqDi2%2BnpRjW1kCFBjuJr0QtjSP4AFrb52ucw6zNny%2FpjPeAZXrIOF7PLJ0hspXpuzb0%2FU1CqTaXRE57OCpEpLFcSiDvZlWOXBpJALDe1hyJMmjbYccqJ30H%2B7X8DXvldfAY6eK65gL%2B51qiOrC%2FO33r1lzYwCyiyodmGN7DXEBuH3bXDQihXJkoTDKPmUfetwNEvoa%2FCKPpLqzVHTzNgN4VydSuXWhCyT65EoHAybAeZyaaPdA9AgHBNpl1WKY2BDP01kZHH8LayN0%2F1kaNaE1PsNkObicvkJ9puEO2uLDrZJwGqywPxtnvazLEbVE1uRgBpaRDfyAq5FUCKmOJpFOuMaKyrdX6NpduRuYwJI93DVeqTkJ3zdQBqcZ9KNf0Pvf7%2BW1bM%2B7Y8879%2Bx%2F15edrdhgJUXPSO8PgtkSWHSz1GNmJtZnOy8gZPkW9Pqxoq6uycCERrIrtOqGjEkCiUlvPvma0jZ%2BH1pcvhOSGtNjF5Y85SpkeXXTsh%2Fhy1x1CJuVW7iG6do%2BGVlsroq5x%2B2gJe%2Fg%2Fl8LFfXs6e3JBhvxPGXOzWrZiAwwKszEhP1oJzkVWgMJ2TwMwGOqUBpZzWWPwo19Y0omZy8Oib9YhdOXnPOlxDxJz7tRC6SgAl1z6qBbv%2FiAkIG94fQqU2BU3vZQWWPSxPI1en3Z1FNWa8Nq6QWhE1atIxZYszzmT%2Br0sRo7wzmGkmWoUVAm5gGpUv5LMiB0nL5mSmHqhwFR%2FhWmqRu1WyzNCI0sCWHtEWS%2FLMZo479ZU3FkC8uqEAkHjizSKtliAtC6wuz9%2F9avPLdYLy&X-Amz-Signature=45a0628d98a56adfc429de6dca01aed5f5476756a4af9f51a68c55f1d51c8c30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







