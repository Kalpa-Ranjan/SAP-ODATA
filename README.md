



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A7C2GK7%2F20261028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261028T180652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQD4W6ISStsSRbfZcfrgjDq0%2Bbow%2FUg%2FcH2yXoztgEWq7gIhAM69pEIrDE2yPc57aB6ymVM025k3a57%2F6Gh%2F3f9iTh1LKv8DCAoQABoMNjM3NDIzMTgzODA1Igz%2BFO2CqYs9id963HIq3AOMOVV9FIKPJUB6BkiWuQqN2pYcWpySCiY88ImfLWMXbXMbBjFfD68V3OmzxcaOPN25vw9%2FAoOHWSs1cqWavZ0SLH95Vydk2XwVlPvEUNTh8te239l9Jtkpt0k1e5AXWnUmPgIGoww54WQCBL1dJ8chyA%2BwkSCLOAKA8uhYNNTvDFNge64FgOpNfEFUw%2F2o%2BNaf6zs21kAWgfqcRcr7N3msglaKrDweyd5l0HJ3SQ2BoPFfMpSq%2Ff0uPT%2Bbk7WSAJQZdE1y24eQy4DDJAaTfiQ7yP9bght4xMnYWFcA9WyGkLAMpJpISkNB8MVMuyQFmFKEO5lrnzwaw91lPIZ7gn1xt7dR5M11Mbm2OGZsaJ5a4kx%2B1bIkiOUvVZ1PXJxv%2FSiGaZ%2Fx8awOwvSwzWRxtZQNWsXHigOMZSJ9Qrh0UpRU%2F1F8GMbFftFle0g%2BHzHHRWUxkWLRc3jG%2FoG%2Fsj1kCYsIlZSjopHr0YNHuapunpzpVlZwWRszPVbKB4ETLYfepwyMoe%2BCMsXNoIYwHOmVRmYPkh8toDYESqsv3le1uSQXpWu3DOq9vaZgzR1pXkrKOOPxF7eEPR4tKiHYeE9m75XWQn3Ex6fvI%2FYaFbAXwiCBfxg%2Bal6MaQKc0gUvbjD144jXBjqkAedQuzXIs0qGpdJ3KK1sAkuiMMH3Ml9ARQwSG5dHevSkl5KwwCkwJqbINI9rBEWhZq4XiVFsmeCOrruoQ7%2BqumkcYyIjvE58%2BToy23s5Aag8a8m8SLLet2wXWyysHf0Bx%2F6Nt4uu7iUnhTPtyGQjTo9EDKy82gVFrSEP12hkcXUusqxB4kTWATkN4zooiLUcFVy9B8qev44h%2BywG3zzuMMEdgyAT&X-Amz-Signature=964ebc848e9f4a4d7dc959d76cd1c430b238ac722b7e0f08b643de6cfb2912e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A7C2GK7%2F20261028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261028T180652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQD4W6ISStsSRbfZcfrgjDq0%2Bbow%2FUg%2FcH2yXoztgEWq7gIhAM69pEIrDE2yPc57aB6ymVM025k3a57%2F6Gh%2F3f9iTh1LKv8DCAoQABoMNjM3NDIzMTgzODA1Igz%2BFO2CqYs9id963HIq3AOMOVV9FIKPJUB6BkiWuQqN2pYcWpySCiY88ImfLWMXbXMbBjFfD68V3OmzxcaOPN25vw9%2FAoOHWSs1cqWavZ0SLH95Vydk2XwVlPvEUNTh8te239l9Jtkpt0k1e5AXWnUmPgIGoww54WQCBL1dJ8chyA%2BwkSCLOAKA8uhYNNTvDFNge64FgOpNfEFUw%2F2o%2BNaf6zs21kAWgfqcRcr7N3msglaKrDweyd5l0HJ3SQ2BoPFfMpSq%2Ff0uPT%2Bbk7WSAJQZdE1y24eQy4DDJAaTfiQ7yP9bght4xMnYWFcA9WyGkLAMpJpISkNB8MVMuyQFmFKEO5lrnzwaw91lPIZ7gn1xt7dR5M11Mbm2OGZsaJ5a4kx%2B1bIkiOUvVZ1PXJxv%2FSiGaZ%2Fx8awOwvSwzWRxtZQNWsXHigOMZSJ9Qrh0UpRU%2F1F8GMbFftFle0g%2BHzHHRWUxkWLRc3jG%2FoG%2Fsj1kCYsIlZSjopHr0YNHuapunpzpVlZwWRszPVbKB4ETLYfepwyMoe%2BCMsXNoIYwHOmVRmYPkh8toDYESqsv3le1uSQXpWu3DOq9vaZgzR1pXkrKOOPxF7eEPR4tKiHYeE9m75XWQn3Ex6fvI%2FYaFbAXwiCBfxg%2Bal6MaQKc0gUvbjD144jXBjqkAedQuzXIs0qGpdJ3KK1sAkuiMMH3Ml9ARQwSG5dHevSkl5KwwCkwJqbINI9rBEWhZq4XiVFsmeCOrruoQ7%2BqumkcYyIjvE58%2BToy23s5Aag8a8m8SLLet2wXWyysHf0Bx%2F6Nt4uu7iUnhTPtyGQjTo9EDKy82gVFrSEP12hkcXUusqxB4kTWATkN4zooiLUcFVy9B8qev44h%2BywG3zzuMMEdgyAT&X-Amz-Signature=32ed5a433bcd2151d8b21d3c58877ecaed51f78d44b52e79f34c80832857e589&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







