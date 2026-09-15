



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N27QBNN%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T002120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIH02%2B7YQMO%2FHBFXDO3e0ILOaSexX7Y%2FQrrX7wYELFcx3AiBf5miUrccpfQ2tqyVxlWVf3dQy28YUEOYe%2B653iT%2FY7yqIBAjw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9u%2F3NpcJmvVIyEfnKtwDZuMPnHsPyBM4JE4UGGAvNRwqWYb%2FMGL5KTEgEjnuKVIQPKC7DOpaAlREeKbtmdgc4JWLE5M0iZgsZ1At9cJoykG4gJY67Vv%2FJ8YGXysQbPxs9UwEP%2Bk6Z1k1U7nBQZjdy9ofzeGvpQPaR829wvf5OOV9zeicvo1MBygTlx9nCbwrSr4Lw%2FVqWd%2B8rJPucJdRB3E39EsFdCHmdK1jE3HAfgdJSLpeSlOobDsM1mMMwGbcZv%2BQYIWQNcgYBkMUTma7iqTdeJbMWV3zcferDFZEFm8ewC%2FiXs3cSDL2k3J%2FjnvaZMv7AiGxxAwfXax5rCytMaI0%2F9bV3bPJKzMvQ0bjeDDS5uQFkXJEgRfM%2FPbH1nD8RTQHE6kLsfVqhNFwrE4pzs7eEJjs8Zk5%2BpDCyUqB6LtEIfdMjEwH%2B9R23S7iUppKAJIlFjVE0oAxNFSoG4goPVo199olB7CubW6Q9MUa6d92YVtnRvw0klIyuIXpnfS0jdWHu3%2BRL5Fb3v79dyy3kSSSdQ775oRwNtVT%2FqtrtPrGntyUc8oMh2Z6O4ASi13v06bLZhg12GMJzFyJXilwyGSNtl6FC41L6txdIdtBpnfy%2BZFVNENxjNmPz2M0re83SxwaFM%2Boxjvj080w%2Ffyh1QY6pgFgGx%2F8fzl7sabhY5WS4jG9vy9F7q8Bk8e%2Fp5fX%2BS%2FGB63pBajx1xrnhIJYsW%2BB0UhobrbkhzcU4hHGNg%2F%2BaVP6PuQeVxqrPLE4%2FpZycQK3jkAyHWsK8S2XWvFlnGt2jEe5VqH0gwQ1ZIjG3I6ebcmvoMmnoIIp%2FqBZRZA%2FXLm1K31hEPAfFwZgg%2BxVlctl6DH1qq7Qpu5FTXDLLdkHoLlMWHNGk%2But&X-Amz-Signature=7794e32fd143b64bc1e3e5f73c86e30159c9f24f6564506c60a6e045cda54476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N27QBNN%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T002120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIH02%2B7YQMO%2FHBFXDO3e0ILOaSexX7Y%2FQrrX7wYELFcx3AiBf5miUrccpfQ2tqyVxlWVf3dQy28YUEOYe%2B653iT%2FY7yqIBAjw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9u%2F3NpcJmvVIyEfnKtwDZuMPnHsPyBM4JE4UGGAvNRwqWYb%2FMGL5KTEgEjnuKVIQPKC7DOpaAlREeKbtmdgc4JWLE5M0iZgsZ1At9cJoykG4gJY67Vv%2FJ8YGXysQbPxs9UwEP%2Bk6Z1k1U7nBQZjdy9ofzeGvpQPaR829wvf5OOV9zeicvo1MBygTlx9nCbwrSr4Lw%2FVqWd%2B8rJPucJdRB3E39EsFdCHmdK1jE3HAfgdJSLpeSlOobDsM1mMMwGbcZv%2BQYIWQNcgYBkMUTma7iqTdeJbMWV3zcferDFZEFm8ewC%2FiXs3cSDL2k3J%2FjnvaZMv7AiGxxAwfXax5rCytMaI0%2F9bV3bPJKzMvQ0bjeDDS5uQFkXJEgRfM%2FPbH1nD8RTQHE6kLsfVqhNFwrE4pzs7eEJjs8Zk5%2BpDCyUqB6LtEIfdMjEwH%2B9R23S7iUppKAJIlFjVE0oAxNFSoG4goPVo199olB7CubW6Q9MUa6d92YVtnRvw0klIyuIXpnfS0jdWHu3%2BRL5Fb3v79dyy3kSSSdQ775oRwNtVT%2FqtrtPrGntyUc8oMh2Z6O4ASi13v06bLZhg12GMJzFyJXilwyGSNtl6FC41L6txdIdtBpnfy%2BZFVNENxjNmPz2M0re83SxwaFM%2Boxjvj080w%2Ffyh1QY6pgFgGx%2F8fzl7sabhY5WS4jG9vy9F7q8Bk8e%2Fp5fX%2BS%2FGB63pBajx1xrnhIJYsW%2BB0UhobrbkhzcU4hHGNg%2F%2BaVP6PuQeVxqrPLE4%2FpZycQK3jkAyHWsK8S2XWvFlnGt2jEe5VqH0gwQ1ZIjG3I6ebcmvoMmnoIIp%2FqBZRZA%2FXLm1K31hEPAfFwZgg%2BxVlctl6DH1qq7Qpu5FTXDLLdkHoLlMWHNGk%2But&X-Amz-Signature=3c6081ac999b39801fb47acb9aba2029a27a737a26f9cb4ad54f438b321027ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







