



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DNVR3N%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T060706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIG%2Fx5tXJ%2FTKjg10%2B9Usq3sw5aHE1AD6eTVGB%2FsCnRrjXAiBuWpxJ6LyXOZ8un8d5BKgXLAXMSK5x3ZYWtkbhnlr7wSqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqJ2MI19TZfaetRKUKtwDrCIJjevwNS3%2BsWWdIAsbXMiOR5fJhJn%2FCQ871t15p5UGs%2FgeWc%2BT%2B6GCXMO75eC6OAHWB0bBZ7Ib8K0uHFiJvwhoAUbYYPJ5x%2FI4XGUzjZSBnqu%2FV9RpIoGelpVW1WJobNLtVuY3DbjuzrSo%2BoVS0ogukIIzOA35uk3q0krY8nIRljZrPA3JfHF06%2BNNgHxmuTvVQOaqMLq8vDuC7mvBoAsh9cRYEIV9kUyy1jI9U7BY2OPVNjv6GePIzK0uYlfVQHutPSqvAa4e1%2B9%2BGsvvBG9EEPdsvPazvVr83cBUkaHKv%2F%2FWzW852Kug9zvHjZghNspt7AxILZm4X7IfeBqBhPEO0JIN%2BptHyW%2Boni8uqklhtoJxB8fSH8mhrgZoU38cpbK%2Bt9tMHBF1Ax6%2FTZoLtnWtP1x5jelW%2BbLtMjJ1nQ09YOboATzYGxy6%2FWrs2fTOoSsEwTnDJDg1hWSJx22H2YWBR4mGkM5lTYC3uhsobJ0jcT%2Br4%2BFvhkoolNh1Cii9B1hY0C%2BtOG2t0Xa4NP8wNck3RnKhHLggepxHTZpjX9kOGruMT0Rclla8y2bf2hhOy38%2F8Q%2FeZSQtlK9qM6%2BayMX%2FCW4%2BJGWjsYhVawxWkkEOph8wWv4ArKozJmgw2e%2B61wY6pgH57e4joBR%2FlQC0S109idPyNwRxrJKadscMvzeo%2FPXNw1RgRKV4JMiFCGR64R29Lt6c0kYKPdH%2BK0WK%2BNpjvK7duXAhnvWf6Ic%2BTBQNrcz02KIP5nChaxBmmfLTCsp4g7FD9wsr9GFBlKObCw9ntBgGuNCnYyKtR1Lb04vss49S%2FJCCu8gN8BHPIItXCAiBHjFnWjtIGAW%2F2zWhu1CRiCNra%2B3NZ2KQ&X-Amz-Signature=d32b7a8bd75663f6899f438a5b5e840d41e0ea24f49788bd0a37dccfa2e81516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DNVR3N%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T060706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIG%2Fx5tXJ%2FTKjg10%2B9Usq3sw5aHE1AD6eTVGB%2FsCnRrjXAiBuWpxJ6LyXOZ8un8d5BKgXLAXMSK5x3ZYWtkbhnlr7wSqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqJ2MI19TZfaetRKUKtwDrCIJjevwNS3%2BsWWdIAsbXMiOR5fJhJn%2FCQ871t15p5UGs%2FgeWc%2BT%2B6GCXMO75eC6OAHWB0bBZ7Ib8K0uHFiJvwhoAUbYYPJ5x%2FI4XGUzjZSBnqu%2FV9RpIoGelpVW1WJobNLtVuY3DbjuzrSo%2BoVS0ogukIIzOA35uk3q0krY8nIRljZrPA3JfHF06%2BNNgHxmuTvVQOaqMLq8vDuC7mvBoAsh9cRYEIV9kUyy1jI9U7BY2OPVNjv6GePIzK0uYlfVQHutPSqvAa4e1%2B9%2BGsvvBG9EEPdsvPazvVr83cBUkaHKv%2F%2FWzW852Kug9zvHjZghNspt7AxILZm4X7IfeBqBhPEO0JIN%2BptHyW%2Boni8uqklhtoJxB8fSH8mhrgZoU38cpbK%2Bt9tMHBF1Ax6%2FTZoLtnWtP1x5jelW%2BbLtMjJ1nQ09YOboATzYGxy6%2FWrs2fTOoSsEwTnDJDg1hWSJx22H2YWBR4mGkM5lTYC3uhsobJ0jcT%2Br4%2BFvhkoolNh1Cii9B1hY0C%2BtOG2t0Xa4NP8wNck3RnKhHLggepxHTZpjX9kOGruMT0Rclla8y2bf2hhOy38%2F8Q%2FeZSQtlK9qM6%2BayMX%2FCW4%2BJGWjsYhVawxWkkEOph8wWv4ArKozJmgw2e%2B61wY6pgH57e4joBR%2FlQC0S109idPyNwRxrJKadscMvzeo%2FPXNw1RgRKV4JMiFCGR64R29Lt6c0kYKPdH%2BK0WK%2BNpjvK7duXAhnvWf6Ic%2BTBQNrcz02KIP5nChaxBmmfLTCsp4g7FD9wsr9GFBlKObCw9ntBgGuNCnYyKtR1Lb04vss49S%2FJCCu8gN8BHPIItXCAiBHjFnWjtIGAW%2F2zWhu1CRiCNra%2B3NZ2KQ&X-Amz-Signature=8a86274333d40dfb66f97c354c44fd85ef45b1f20752bfa525b33f94f88ee1b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







