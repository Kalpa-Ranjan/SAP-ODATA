



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMIWE4MQ%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T065837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCdHK%2FKRsy7gh4YngoRxVWU4UQATaonGZZrBiYA9CUpWQIgcphIeMQMKZG96M7iktN9eR1d%2Bk%2BE1k7dsXhLhmTEWc0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7m4znj1AEwzvae8SrcA1hec2GJkcRpBFuEmlsFKivqoO2vM2NI31gfqficJ%2FYFR49XGI1PiRBxm6oRefqL1LtJ2of%2B20PHBqHAaaZfIAgKyUSBNlyUs1IsgRXmcvu%2FfKwtXH7IjW9v0cCn3d5tREMq%2BwYyA1snd4h%2F9qf7evbJp4g8aqXoB%2BzHlcq7AqS8TLmWoci9QhrY2P5t%2B%2Fid%2BnpnADOQMf%2B2PEhN7zfSbqetJyxkshOisjXcDLinVBgNbKe%2BrAyEmneWeDtsI4VXjQCEOoutHrzpAMqnOtvcT6ERnG8YTpIGOjBnvoXPs7tQT9v5zH1Yeao3EcegCi7bWAXtLATo0Sk%2F%2FD4wvuK4kXvVXsOI%2FGYRf6w1mLDAoWD6xkovqKenat6MoXmD1xjk6uhMiC61a1%2BJ%2F2nuddmrS4jQ72kycEm2EqkOVCPY8wlj1O8FG336qiMSMUhNu5FCwt0DRaD%2FKuSnx4VYII7HBd5gqvx1K8su2pYk5FSadpBcasehaS7gp%2BvOxewM3EdGzVONsHtdZrpNSnnF0N9Cz9ybUlnbXKHWlWBe4E5YOZ6rD3OLfO4PxDqYFRrHztG%2BqqT6QURXpJTxjK2E2bTVXdY%2BiOIHw3HzxfpF2PfcpH%2B0%2Bug88uHNPAmfn7R9MJ%2FX78wGOqUBovkLClJOXOl%2Bh12CRZfPKoV6xUupyNIZ3pkfVgePnA4d2gEV0i4p67rR8EBWgVc5vpygzYXavQbRDQLWvIo7D6xVAGZayK655cE%2FAa5AsGZSvDysdih8r9olrfFmldtvapwxphxJr5lAlZ%2B3Zqcuo7%2FCPeDIjjrOIg4D%2F9Om331SU0LwEo3AneRAPzdph0cial%2BMGPJH6KdcTAohS3SQDZ2SzWQP&X-Amz-Signature=8749f1e5df7ae6f0c45762c2003a56180929db866539213053d31fc0d5dca3ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMIWE4MQ%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T065837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCdHK%2FKRsy7gh4YngoRxVWU4UQATaonGZZrBiYA9CUpWQIgcphIeMQMKZG96M7iktN9eR1d%2Bk%2BE1k7dsXhLhmTEWc0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7m4znj1AEwzvae8SrcA1hec2GJkcRpBFuEmlsFKivqoO2vM2NI31gfqficJ%2FYFR49XGI1PiRBxm6oRefqL1LtJ2of%2B20PHBqHAaaZfIAgKyUSBNlyUs1IsgRXmcvu%2FfKwtXH7IjW9v0cCn3d5tREMq%2BwYyA1snd4h%2F9qf7evbJp4g8aqXoB%2BzHlcq7AqS8TLmWoci9QhrY2P5t%2B%2Fid%2BnpnADOQMf%2B2PEhN7zfSbqetJyxkshOisjXcDLinVBgNbKe%2BrAyEmneWeDtsI4VXjQCEOoutHrzpAMqnOtvcT6ERnG8YTpIGOjBnvoXPs7tQT9v5zH1Yeao3EcegCi7bWAXtLATo0Sk%2F%2FD4wvuK4kXvVXsOI%2FGYRf6w1mLDAoWD6xkovqKenat6MoXmD1xjk6uhMiC61a1%2BJ%2F2nuddmrS4jQ72kycEm2EqkOVCPY8wlj1O8FG336qiMSMUhNu5FCwt0DRaD%2FKuSnx4VYII7HBd5gqvx1K8su2pYk5FSadpBcasehaS7gp%2BvOxewM3EdGzVONsHtdZrpNSnnF0N9Cz9ybUlnbXKHWlWBe4E5YOZ6rD3OLfO4PxDqYFRrHztG%2BqqT6QURXpJTxjK2E2bTVXdY%2BiOIHw3HzxfpF2PfcpH%2B0%2Bug88uHNPAmfn7R9MJ%2FX78wGOqUBovkLClJOXOl%2Bh12CRZfPKoV6xUupyNIZ3pkfVgePnA4d2gEV0i4p67rR8EBWgVc5vpygzYXavQbRDQLWvIo7D6xVAGZayK655cE%2FAa5AsGZSvDysdih8r9olrfFmldtvapwxphxJr5lAlZ%2B3Zqcuo7%2FCPeDIjjrOIg4D%2F9Om331SU0LwEo3AneRAPzdph0cial%2BMGPJH6KdcTAohS3SQDZ2SzWQP&X-Amz-Signature=9cf2218892c9b4163f1e4a3e778f872affb1f7a49d2e427316d37356e12fa83e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







