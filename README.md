



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H663VHZ%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T120857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO41Fro6bYeX0%2BSrhe700iTDkAmjLcJ81%2B73U1JNwc1gIhAL8y6VTCHtlBFoROd%2FU3ZeZtiA0kb1fE2sQjrgt1bNFeKv8DCGQQABoMNjM3NDIzMTgzODA1IgxpXIghzW5JY4KhgZIq3APfWGN4K4todtUoKu8WRRrK99DniTVBTPynS6P%2BTxIR3ech1nunGrjFJiJST6FcgqM0h8vVlqStILWjkphiXALwDExMMvkjufaM4sU6JyPktw9VxAy%2Bo7ypguXZg%2FF3n6RizfaWGR%2BXbRCefF8%2BiYTcr6C08KpBAWKy0V%2FU5oKDtpWAlx%2FGVr2N7YcI71uAJjQ0ZYiBayFa4Hq%2BM5f0t1ZtiQG1N6Mr4j3R0wslQ8bp5NQPHRYSXYt9wiOfuXG4oF20Un3TUFCYnLsePciGcz80dk3uDdmdN%2FxwqjOd%2Fa06VDT%2B2NxoXbUvMc4CdvEoga6nvp5H5%2BXw9A3cyYUEmhUOJijRcGmpf2Z%2FTe%2BTYeG99%2B6osVzrliF6HFZ8QvI67hUvnzLsOTrUlraaBWXZ7Ct7h5h5qpUznsYc8XuZ7CDRlwA07ZdwN8PDyKuMyZ8nVNGlCN7JyXmZrfTbEBDVS7PIgHWoQV5M%2BBwUA9v4d8GXuyhRm%2BReE7qxYAfOkFQkw79GviUbkWe3FA8k6pEwSLb8PcmeAGT1bdtPKxRa5CrVaO5TRBz6I4exj6m%2FZdZg1AJlbK4Zzmi0bGcOkwMtWrz7E2OMaIS3pkkiCNWdAc8mNwRMDw85ip%2Fs4M2U8zCa%2FMrUBjqkAR6Avrg%2FOzdJTLMobY4wgQI0ps4d4HY%2B8F4OCpDdO8EQUyVZwZS8%2BOZ4YJrMKtmbTaOJJq601MThxs12jTJZihlNFNqqP0UPXL%2F6mZ5sZDziSYrHTtAAC2sVbXDgTPAlRnzqXbboXbIumrW87306d5gM306FicdJlM%2BqKlwT6IxGnxTcZ4IC1u14r8Xow6my%2Bz2nLiHd%2FQC%2Bd%2FNfN8EB0GgpLIlG&X-Amz-Signature=85a8d37821fe55da1cc42a1839c57956afbdf511aa690bc01335f840ae779b1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H663VHZ%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T120858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO41Fro6bYeX0%2BSrhe700iTDkAmjLcJ81%2B73U1JNwc1gIhAL8y6VTCHtlBFoROd%2FU3ZeZtiA0kb1fE2sQjrgt1bNFeKv8DCGQQABoMNjM3NDIzMTgzODA1IgxpXIghzW5JY4KhgZIq3APfWGN4K4todtUoKu8WRRrK99DniTVBTPynS6P%2BTxIR3ech1nunGrjFJiJST6FcgqM0h8vVlqStILWjkphiXALwDExMMvkjufaM4sU6JyPktw9VxAy%2Bo7ypguXZg%2FF3n6RizfaWGR%2BXbRCefF8%2BiYTcr6C08KpBAWKy0V%2FU5oKDtpWAlx%2FGVr2N7YcI71uAJjQ0ZYiBayFa4Hq%2BM5f0t1ZtiQG1N6Mr4j3R0wslQ8bp5NQPHRYSXYt9wiOfuXG4oF20Un3TUFCYnLsePciGcz80dk3uDdmdN%2FxwqjOd%2Fa06VDT%2B2NxoXbUvMc4CdvEoga6nvp5H5%2BXw9A3cyYUEmhUOJijRcGmpf2Z%2FTe%2BTYeG99%2B6osVzrliF6HFZ8QvI67hUvnzLsOTrUlraaBWXZ7Ct7h5h5qpUznsYc8XuZ7CDRlwA07ZdwN8PDyKuMyZ8nVNGlCN7JyXmZrfTbEBDVS7PIgHWoQV5M%2BBwUA9v4d8GXuyhRm%2BReE7qxYAfOkFQkw79GviUbkWe3FA8k6pEwSLb8PcmeAGT1bdtPKxRa5CrVaO5TRBz6I4exj6m%2FZdZg1AJlbK4Zzmi0bGcOkwMtWrz7E2OMaIS3pkkiCNWdAc8mNwRMDw85ip%2Fs4M2U8zCa%2FMrUBjqkAR6Avrg%2FOzdJTLMobY4wgQI0ps4d4HY%2B8F4OCpDdO8EQUyVZwZS8%2BOZ4YJrMKtmbTaOJJq601MThxs12jTJZihlNFNqqP0UPXL%2F6mZ5sZDziSYrHTtAAC2sVbXDgTPAlRnzqXbboXbIumrW87306d5gM306FicdJlM%2BqKlwT6IxGnxTcZ4IC1u14r8Xow6my%2Bz2nLiHd%2FQC%2Bd%2FNfN8EB0GgpLIlG&X-Amz-Signature=d91959d1c5f928300272d997b1ad97bbbfa2b79e703f44fd635a2a0870287917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







