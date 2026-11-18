



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M4NLF6H%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T180516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQC%2BLxYnheg32QBs7jjQuJjlYlikhbczn3PwmFJ3kuVMMQIhAL4XWXxEEOSTeJzLGWW%2FA4HYWeRLPPr2mxeR6X6JuExQKv8DCAIQABoMNjM3NDIzMTgzODA1IgwRs55%2BuhVX0UfnoGcq3AMlrXgWhkxR53xMN5Z31bFCrS2ZXlNONz8w40AJfvWTFURhMUlay59VcXdsuHakNYV59a6uB8r%2Bq0yZqgUho3XUyccBWRAsHHrd%2BphS7FEsy6xRWuGbf8z8%2BO0bJM2slJkquB74Z7nZoBWgqFuUGGR3hcvT4b4eB8Z35BRmdmnYC84vyipcO%2FpIPaTzZWypCDzOM%2BYBLa1rUoeKNv%2FPtoqdrMvU6gMoCpH9xEEAHGHk80Az7tN8IDFD%2FA9H1yQw0AwplJ%2FQ7I1pCvMrmul0dPfXNF%2FZVlZU7qkW7B%2F8MEIOejZjcOvuS3DbahkQ9MbsgBwYcIqBGpAy2v2jBxKe84I1NYOlDksGDCAB3wIB8iqlaTUQJVIMTvON412d4t0ZvWHmqZyfgtR49appQjGlgyVSnk1MEzGwMzx6wVe12d9CzYhmO8Ql0IRc2KyJFDpMbEOdzv%2FeXBjK8ICd0eYPItZoP0TD6z6Q93REYrW1BQI006OQnb2zVsTUtUty9s7wMEVUTMQdZbnc%2F4ZVPYuqpI5fPqX13QbTJc07o%2BeTK7YPViG8umZDt%2Bc%2FULL9sdAbkS3SDvluls2ku6neug%2BU92liy%2F6Yy7PN5cn46L6kkPFSMRQxeMXSot6QSDKCojDyzPfXBjqkAcbvmRA%2BZz99gS9%2FoC8PZ%2FIC4W%2Fpz%2FO38GgwC1PhinZv0jNIqmFpwd2T%2BwlDcf4aqjdSsT2%2B2KaKvhzug5fHKqBWcXWdqBaa6UfylgX7zoCOPXB8TYU0v6%2BjfN8z%2FlvXKRyvM%2FOSNTJf2osxSGjxPnFV3PvMel6JZ4x6Zf8XXeBxeCJ8JwYVkWZKTpYOehlYA9up%2Fx8Ufw4wgBZhugAVQ8YtvOQs&X-Amz-Signature=3cd8638821b966900798fde31d70942d56ca50cf3386119fa86fbdf2173a3e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M4NLF6H%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T180516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQC%2BLxYnheg32QBs7jjQuJjlYlikhbczn3PwmFJ3kuVMMQIhAL4XWXxEEOSTeJzLGWW%2FA4HYWeRLPPr2mxeR6X6JuExQKv8DCAIQABoMNjM3NDIzMTgzODA1IgwRs55%2BuhVX0UfnoGcq3AMlrXgWhkxR53xMN5Z31bFCrS2ZXlNONz8w40AJfvWTFURhMUlay59VcXdsuHakNYV59a6uB8r%2Bq0yZqgUho3XUyccBWRAsHHrd%2BphS7FEsy6xRWuGbf8z8%2BO0bJM2slJkquB74Z7nZoBWgqFuUGGR3hcvT4b4eB8Z35BRmdmnYC84vyipcO%2FpIPaTzZWypCDzOM%2BYBLa1rUoeKNv%2FPtoqdrMvU6gMoCpH9xEEAHGHk80Az7tN8IDFD%2FA9H1yQw0AwplJ%2FQ7I1pCvMrmul0dPfXNF%2FZVlZU7qkW7B%2F8MEIOejZjcOvuS3DbahkQ9MbsgBwYcIqBGpAy2v2jBxKe84I1NYOlDksGDCAB3wIB8iqlaTUQJVIMTvON412d4t0ZvWHmqZyfgtR49appQjGlgyVSnk1MEzGwMzx6wVe12d9CzYhmO8Ql0IRc2KyJFDpMbEOdzv%2FeXBjK8ICd0eYPItZoP0TD6z6Q93REYrW1BQI006OQnb2zVsTUtUty9s7wMEVUTMQdZbnc%2F4ZVPYuqpI5fPqX13QbTJc07o%2BeTK7YPViG8umZDt%2Bc%2FULL9sdAbkS3SDvluls2ku6neug%2BU92liy%2F6Yy7PN5cn46L6kkPFSMRQxeMXSot6QSDKCojDyzPfXBjqkAcbvmRA%2BZz99gS9%2FoC8PZ%2FIC4W%2Fpz%2FO38GgwC1PhinZv0jNIqmFpwd2T%2BwlDcf4aqjdSsT2%2B2KaKvhzug5fHKqBWcXWdqBaa6UfylgX7zoCOPXB8TYU0v6%2BjfN8z%2FlvXKRyvM%2FOSNTJf2osxSGjxPnFV3PvMel6JZ4x6Zf8XXeBxeCJ8JwYVkWZKTpYOehlYA9up%2Fx8Ufw4wgBZhugAVQ8YtvOQs&X-Amz-Signature=e991c8c7f1e103e0dface4a16ec015e8eb3aba02aa048886ab6ee7b3308bead7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







