



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RE226L2%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T112148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCICbRDnY9sMy6dwzm%2FoIxBD1xnMTpiJomlU%2B58amF1kMgAiAFlbp2%2Fz%2F7DJbF0B2UgZH%2FM6hT3hq5IQTkeBe8oqPD4yr%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMslkcq6CjuE39%2FvcSKtwDRh%2FNhM2Ky70QL%2BjSuFjYtJTBrk6KcNSC5hcK6JOfyhS4M0sBIOocA%2BWMKqPFpvgXjPuK9WajHpAIGIcGQnOrMk5M5UCxIdecv0PgaHVIDvAB%2B3W20eTvJmNqC3YfGK4UgOXMaNOzHosK98AefFKqaoP4BnkaUV24tUNDZbcFEnXlZs77okVhLaiGSATs48Z6HCQ1QWxcmfJNmAsv1ijpKpmrPV5EcJdoCM04kTiuWauH7ZjtCBSBnUai0cIq2ayryjR8FVzxZWW0Mo1uQpLDtV2zud4J%2FRKd6csfoLug%2BgAC0aTpg3ut4VVgjLvYCQBxmP0nTLc8HD%2FAYrqs5M%2BlRoC32oyUvmJGkGspDCw57%2BJTaczaiNNjdRH5kb0whjenK5zC5TGQ0iDQG9YmeFUQ38oIgh4eybNyqNoWWF0QFi60bIx9Ht%2BOeaydgQYwuTOzYFwwnCN86PbaVPWHHOgGYDTnaV7lgIlNn%2Bt1UDpXUulJk%2BGGoHc4K9eSqJpAwnG5Oep2QV1K0aMI01cV2suDSL5hsAPok6XXjgEPbEbIrgO10HjJyCXZ7UUdGUWefvReYZpfYPKCDlkRQCov46FyRXIY2vjhi%2FGXVOB4SOzuMzLbMAkxdlf4Vvwlsc8w1MH00AY6pgGlcGly61dqkQAgJwfT8bZZfovAN9thUvKIcJ9BMFVH2kG%2BrAah9W%2Bl9VffN53fwCzrBtu8q0CKAessOrZQbhW3EbzW7eSeyg2dQXoa1bJfx6p5U9ghnIMY%2BUDcUFPoOtu6b6N1Ts7qLTmTwTrQ4oXLYf5%2Ff7hb6p6vKqr6owJ9lfRTsQD5iKdB5QhrxPuyN6lJG%2Fz61IjkE3%2F5tCqlmlA1HdGP9pQc&X-Amz-Signature=cbc1ea1b646294f7821242f8a9463c17ececb513ae4ee1803910d3c33bbea685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RE226L2%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T112148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCICbRDnY9sMy6dwzm%2FoIxBD1xnMTpiJomlU%2B58amF1kMgAiAFlbp2%2Fz%2F7DJbF0B2UgZH%2FM6hT3hq5IQTkeBe8oqPD4yr%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMslkcq6CjuE39%2FvcSKtwDRh%2FNhM2Ky70QL%2BjSuFjYtJTBrk6KcNSC5hcK6JOfyhS4M0sBIOocA%2BWMKqPFpvgXjPuK9WajHpAIGIcGQnOrMk5M5UCxIdecv0PgaHVIDvAB%2B3W20eTvJmNqC3YfGK4UgOXMaNOzHosK98AefFKqaoP4BnkaUV24tUNDZbcFEnXlZs77okVhLaiGSATs48Z6HCQ1QWxcmfJNmAsv1ijpKpmrPV5EcJdoCM04kTiuWauH7ZjtCBSBnUai0cIq2ayryjR8FVzxZWW0Mo1uQpLDtV2zud4J%2FRKd6csfoLug%2BgAC0aTpg3ut4VVgjLvYCQBxmP0nTLc8HD%2FAYrqs5M%2BlRoC32oyUvmJGkGspDCw57%2BJTaczaiNNjdRH5kb0whjenK5zC5TGQ0iDQG9YmeFUQ38oIgh4eybNyqNoWWF0QFi60bIx9Ht%2BOeaydgQYwuTOzYFwwnCN86PbaVPWHHOgGYDTnaV7lgIlNn%2Bt1UDpXUulJk%2BGGoHc4K9eSqJpAwnG5Oep2QV1K0aMI01cV2suDSL5hsAPok6XXjgEPbEbIrgO10HjJyCXZ7UUdGUWefvReYZpfYPKCDlkRQCov46FyRXIY2vjhi%2FGXVOB4SOzuMzLbMAkxdlf4Vvwlsc8w1MH00AY6pgGlcGly61dqkQAgJwfT8bZZfovAN9thUvKIcJ9BMFVH2kG%2BrAah9W%2Bl9VffN53fwCzrBtu8q0CKAessOrZQbhW3EbzW7eSeyg2dQXoa1bJfx6p5U9ghnIMY%2BUDcUFPoOtu6b6N1Ts7qLTmTwTrQ4oXLYf5%2Ff7hb6p6vKqr6owJ9lfRTsQD5iKdB5QhrxPuyN6lJG%2Fz61IjkE3%2F5tCqlmlA1HdGP9pQc&X-Amz-Signature=c1f82a32906e9db9b7f001ac855c7118eb503ece4d0c4c8649ce5d984c1b344c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







