



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSR3CG4Q%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T062036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIQD4PTmvYUyecYVuGCkzY%2Bd%2B1tsOnTEznNHshwhH40qo5AIgPaYmL2oBNekLbmCHmUYhpdsBTMEPw1ZG%2BPdoyVNwBVIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDn00tKKijVDmlX22SrcA941BJlxGtVUaAiFYymTCLZXfMkBED%2F5ctsTQ%2F57xkuWU3O33BeTXFc652gQNLldmoMgHTNUa%2FBTK6FReDCEKBbIXu5quwPmLmZTGCmisDT7IjcyOLp1hLEXKcsJzGqidnOiGcqVzZ88bPf8cm6%2BMWTaGzyBpjXHz%2FmrbguwNjhiTu0WZujDEMF38ozEcf%2F5mB75BOSStPg81dDb9C0XOY%2FNCI6JUb%2Fd%2FCxK7SaERXOi4De%2BIonNEHJr%2BnYmM53tk36dXeF0L5oLRt0TaEkjHKnGNukvuYoW1AYcqUbYFSDrcJFXAyDsZ6sMT7%2FrlJZcjnl3GB26eggIIbw4n4i2SUvHjK7dwQJtvcl3ova4of9owMWFH%2Fr9LxUQFLvFSUztvyLxp%2BTpyxKWA%2F7Xc4%2Fe6LZHgQRaUfodvFQLM%2B1LMivIJBlLtpbtdVfmkBeFzgrS4F0a9g7lzbz1J%2FNbQ6LMOKkQtBu8%2FgSu5W97YlLswy9coBHStBtkvB62RtW%2FB2%2BnNREX9xm%2BfXN1fQPsqbR3z5O1gBr3b4pDsxNN%2FXnwMa83uNLmZan%2F5%2FJCd5289HjdZMYQgZWpW3ETMtKYzNhsA3SC9Ky80k1jvNGLMGHiRuip%2Bk0Dva9pVyvszgrQMJvElsgGOqUBcvQP5IipB%2Bn1NOdJuzPoJSEL6EdWM24%2FWby68axJljBFncANNxSJyv4niM4bR2ioXsaFS2aiQU6CggBmOvl1h%2BrjjwD%2FYZRyhSK8JOzDlVJBuB%2F5REtBO79DMxHbmMSy7I64JrthPB6XZmS2wr92wN7h6wOhlX68ksqGPZOLykc5a%2BfqkBssMu1O4vdjDfs7lkOBhEMuMO5d6cAMbEs5XqtHXUPH&X-Amz-Signature=33a3c696ba097058e3e6af02bf960b63593de54d61ec77f9a0f4b6dd6382b87c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSR3CG4Q%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T062037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIQD4PTmvYUyecYVuGCkzY%2Bd%2B1tsOnTEznNHshwhH40qo5AIgPaYmL2oBNekLbmCHmUYhpdsBTMEPw1ZG%2BPdoyVNwBVIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDn00tKKijVDmlX22SrcA941BJlxGtVUaAiFYymTCLZXfMkBED%2F5ctsTQ%2F57xkuWU3O33BeTXFc652gQNLldmoMgHTNUa%2FBTK6FReDCEKBbIXu5quwPmLmZTGCmisDT7IjcyOLp1hLEXKcsJzGqidnOiGcqVzZ88bPf8cm6%2BMWTaGzyBpjXHz%2FmrbguwNjhiTu0WZujDEMF38ozEcf%2F5mB75BOSStPg81dDb9C0XOY%2FNCI6JUb%2Fd%2FCxK7SaERXOi4De%2BIonNEHJr%2BnYmM53tk36dXeF0L5oLRt0TaEkjHKnGNukvuYoW1AYcqUbYFSDrcJFXAyDsZ6sMT7%2FrlJZcjnl3GB26eggIIbw4n4i2SUvHjK7dwQJtvcl3ova4of9owMWFH%2Fr9LxUQFLvFSUztvyLxp%2BTpyxKWA%2F7Xc4%2Fe6LZHgQRaUfodvFQLM%2B1LMivIJBlLtpbtdVfmkBeFzgrS4F0a9g7lzbz1J%2FNbQ6LMOKkQtBu8%2FgSu5W97YlLswy9coBHStBtkvB62RtW%2FB2%2BnNREX9xm%2BfXN1fQPsqbR3z5O1gBr3b4pDsxNN%2FXnwMa83uNLmZan%2F5%2FJCd5289HjdZMYQgZWpW3ETMtKYzNhsA3SC9Ky80k1jvNGLMGHiRuip%2Bk0Dva9pVyvszgrQMJvElsgGOqUBcvQP5IipB%2Bn1NOdJuzPoJSEL6EdWM24%2FWby68axJljBFncANNxSJyv4niM4bR2ioXsaFS2aiQU6CggBmOvl1h%2BrjjwD%2FYZRyhSK8JOzDlVJBuB%2F5REtBO79DMxHbmMSy7I64JrthPB6XZmS2wr92wN7h6wOhlX68ksqGPZOLykc5a%2BfqkBssMu1O4vdjDfs7lkOBhEMuMO5d6cAMbEs5XqtHXUPH&X-Amz-Signature=ef4d2c50adafb1b83846ebb277ca8628805ed21a22c51dafbecf125461f74809&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







