



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6TQK3PW%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T065900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHWlrqhvd3Du%2FBt39xxqVLg7juwgHRd0gCvpk7rIeTmQIgMO46axbLSZ3bvJMEAWo%2FCwq9EO85kaDJeK%2BddaBAfpcqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfUGQvLKhq9rCPpiCrcA%2BgGmG%2FWokn%2FgoU7s4xpe%2FkQ67aMDEMKceiDuV9LZ0sPunbqS8bkcxzWeYIFbI7c1%2F%2BV8JWO%2BV7XqGZ6Re6sUy3Dp424BI2Uv8BFqHLhLNJz1yzOmZhGJra%2BEim%2Fh%2BpGuCZDoCacGuEsHRw6Vki7ob597YPny0NpWug8kImSsSal2t92%2F9YYTyHvSoIzGgWt7D6ZbWPdoUKgsyjYZ69WgVTpqd8s02m4pwADVBNwOyKAoR%2FVw9av4L9pU5EbPaJQ5AZDHTLpkmHkjIbeNJe%2FgnwIJ3y6XiF35XakDfK%2FBDhdlRCTx%2FZpYUh5sHNYjKKZDUOXfOfvGyE6IgFi%2BVtPE8EhkkB%2Bi9eva5YvTdxz8AJJKZlApuoO4PabnVO%2FwXbdvaxzuo3FjUM%2BS0ZXgA3Y%2F%2F2ZOJzcFVSinZuQhyWbjXZUR9z%2BdUvrN1fWezriW6IOUsF6QCkzPPL9W%2FeGLFR7H8A6dx2nlP2cShQWd8lB6VK30dponP3c%2FNwDRb3StjiavSVsGpMgGYvgc3EVMrUNA4162UAXgbNrvscaAt3e9l1MoH056XLJyn1L10s3%2Fp3Esj7hotCkBbRbcR6uo0KoHbgDmSAh4aFK%2B1Npd8XIqxqfj2oHCC8Db9DVHd%2FrMIfLx84GOqUBtCh0%2B18Gd31mtvXIKnijJ7CqIxx0qDQn7jYz%2FYst2bWFlN3bXLOMA8ESYtPY0%2BHLB5DuoWkDo1kYSED%2BWBipDtcblX4PzkvWNuwDBteZ8CXhk3ogoZFd4s2HeVuhdD%2FRLxoXd65nd7ItDv2EU2zGrjSsgai6YqOvnECXG9lH53cWJEfGRL3MNcTx2YE20Q3twiJAYq%2BOV2l4%2BBze7CGlgcNJIKKw&X-Amz-Signature=6bdfe7efe29d233e189783eb1667f841a02ab9930098d6ba65dc077f1e411030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6TQK3PW%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T065900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHWlrqhvd3Du%2FBt39xxqVLg7juwgHRd0gCvpk7rIeTmQIgMO46axbLSZ3bvJMEAWo%2FCwq9EO85kaDJeK%2BddaBAfpcqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfUGQvLKhq9rCPpiCrcA%2BgGmG%2FWokn%2FgoU7s4xpe%2FkQ67aMDEMKceiDuV9LZ0sPunbqS8bkcxzWeYIFbI7c1%2F%2BV8JWO%2BV7XqGZ6Re6sUy3Dp424BI2Uv8BFqHLhLNJz1yzOmZhGJra%2BEim%2Fh%2BpGuCZDoCacGuEsHRw6Vki7ob597YPny0NpWug8kImSsSal2t92%2F9YYTyHvSoIzGgWt7D6ZbWPdoUKgsyjYZ69WgVTpqd8s02m4pwADVBNwOyKAoR%2FVw9av4L9pU5EbPaJQ5AZDHTLpkmHkjIbeNJe%2FgnwIJ3y6XiF35XakDfK%2FBDhdlRCTx%2FZpYUh5sHNYjKKZDUOXfOfvGyE6IgFi%2BVtPE8EhkkB%2Bi9eva5YvTdxz8AJJKZlApuoO4PabnVO%2FwXbdvaxzuo3FjUM%2BS0ZXgA3Y%2F%2F2ZOJzcFVSinZuQhyWbjXZUR9z%2BdUvrN1fWezriW6IOUsF6QCkzPPL9W%2FeGLFR7H8A6dx2nlP2cShQWd8lB6VK30dponP3c%2FNwDRb3StjiavSVsGpMgGYvgc3EVMrUNA4162UAXgbNrvscaAt3e9l1MoH056XLJyn1L10s3%2Fp3Esj7hotCkBbRbcR6uo0KoHbgDmSAh4aFK%2B1Npd8XIqxqfj2oHCC8Db9DVHd%2FrMIfLx84GOqUBtCh0%2B18Gd31mtvXIKnijJ7CqIxx0qDQn7jYz%2FYst2bWFlN3bXLOMA8ESYtPY0%2BHLB5DuoWkDo1kYSED%2BWBipDtcblX4PzkvWNuwDBteZ8CXhk3ogoZFd4s2HeVuhdD%2FRLxoXd65nd7ItDv2EU2zGrjSsgai6YqOvnECXG9lH53cWJEfGRL3MNcTx2YE20Q3twiJAYq%2BOV2l4%2BBze7CGlgcNJIKKw&X-Amz-Signature=b01cd4b51a838ca42beecf766939f0838847468cd6c696a70b873886ea91c22a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







