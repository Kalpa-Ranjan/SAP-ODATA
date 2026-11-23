



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KEQBVMH%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T120731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7w5z0XpeuV6JMVf%2Bfgh9ckHLu%2F4UhCZr2iZ8sPxf63gIgAXQBKP5eKufKE4Xw%2FRlimNBhMjMdY3oOdwqWJR9zxzYq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDM7ibYAdG7NVKq08DircA%2Bfptfs%2FC0s1aneF9IQptwMksePhDyzQ0DIwk2lqeQABhkcb%2FoYAVufUsyAPk32HoDcLZcJRib5lHiswZPn337%2BonAYF4jJETgAy74NCLBOsx4j5bQaudDzsl5ACbPIX7OAl75hqO8iON2gpgfmMVMr06iwpXs4Ur1ppwCVdBg6mQ0QNzcyCWOwj9ujfqzlgE64GVIm%2BDSARsKs3Id4jOhv1D2GcRjTH0PepofoLtFZmOZ8Ty63ndDkcRkGpSOlt2N0q%2FHy28GKmqwkUCrZoed4rF%2BFCiw1kSfGZQijzyAkk5GpBu%2FBWdjKekQ3%2FkN6n5%2FQqMCeAtrvlYT%2F%2F8aycvijh%2B6m8nD4Ll45xXlIJ%2BSTKzFSSGDJ%2F31xRTIFuv3HbbAQGaohkYFS8zEmwkK4rZ27VDBCFPsjR0ZWEYRrLx49f8bq0dJhMegktgFavfeIWHUrnCj089KLUhJRNrY2whKKWywP6baj5rSHBLRxPtkdS%2FDG2imqpqDuinCzf8ATUEQT4fxn%2FXMIOh7u9Ba7pk0d7h077W7%2BIhtgxs7qVBNA3Tfj0bBy8A2ktOBjx2TPQRuQUYuqvtRk6sQ6M9T9YXrk3TrxMwVf8kKGeWCAJrNYE0%2Bn8DvCyvGZ2hlwiMMrDkNgGOqUBms8M5ZE%2BnsiQ%2FCxiE%2BflxZRHK5qdvo1PtxTpW1wlTib8XHL0quwcytmcEIfHiFw03LIwjX5jCM6cvaZr38wyv2%2BVNYDCNzoO4tRKusyTU%2BdETRerNSnQvfnb861Us3q3qoSEIUGn91KCcVwS0IKXfp26%2B0PrK5x0sc528Uhe8jyMhLjTgZdeQk98BooQDsABKEFELU6EFKygNWIcpa0KeA9bmOVl&X-Amz-Signature=e7f29a05e2bd0e9668e3500b92db66ded8e97b3b1b3e07cb159b1db36ccee95f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KEQBVMH%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T120731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7w5z0XpeuV6JMVf%2Bfgh9ckHLu%2F4UhCZr2iZ8sPxf63gIgAXQBKP5eKufKE4Xw%2FRlimNBhMjMdY3oOdwqWJR9zxzYq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDM7ibYAdG7NVKq08DircA%2Bfptfs%2FC0s1aneF9IQptwMksePhDyzQ0DIwk2lqeQABhkcb%2FoYAVufUsyAPk32HoDcLZcJRib5lHiswZPn337%2BonAYF4jJETgAy74NCLBOsx4j5bQaudDzsl5ACbPIX7OAl75hqO8iON2gpgfmMVMr06iwpXs4Ur1ppwCVdBg6mQ0QNzcyCWOwj9ujfqzlgE64GVIm%2BDSARsKs3Id4jOhv1D2GcRjTH0PepofoLtFZmOZ8Ty63ndDkcRkGpSOlt2N0q%2FHy28GKmqwkUCrZoed4rF%2BFCiw1kSfGZQijzyAkk5GpBu%2FBWdjKekQ3%2FkN6n5%2FQqMCeAtrvlYT%2F%2F8aycvijh%2B6m8nD4Ll45xXlIJ%2BSTKzFSSGDJ%2F31xRTIFuv3HbbAQGaohkYFS8zEmwkK4rZ27VDBCFPsjR0ZWEYRrLx49f8bq0dJhMegktgFavfeIWHUrnCj089KLUhJRNrY2whKKWywP6baj5rSHBLRxPtkdS%2FDG2imqpqDuinCzf8ATUEQT4fxn%2FXMIOh7u9Ba7pk0d7h077W7%2BIhtgxs7qVBNA3Tfj0bBy8A2ktOBjx2TPQRuQUYuqvtRk6sQ6M9T9YXrk3TrxMwVf8kKGeWCAJrNYE0%2Bn8DvCyvGZ2hlwiMMrDkNgGOqUBms8M5ZE%2BnsiQ%2FCxiE%2BflxZRHK5qdvo1PtxTpW1wlTib8XHL0quwcytmcEIfHiFw03LIwjX5jCM6cvaZr38wyv2%2BVNYDCNzoO4tRKusyTU%2BdETRerNSnQvfnb861Us3q3qoSEIUGn91KCcVwS0IKXfp26%2B0PrK5x0sc528Uhe8jyMhLjTgZdeQk98BooQDsABKEFELU6EFKygNWIcpa0KeA9bmOVl&X-Amz-Signature=0e499f64d99e4a58aba6f85f3bd7896382d61258e1bb0cc5920346282084a6ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







