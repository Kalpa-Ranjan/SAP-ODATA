



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFNSXOYJ%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T123137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLP5natGvRMe7kqQKJQykmrtJM9VuZjSH%2Bs8nftcQ%2F4AIgJDUGXz3zCa1OApIOojjc7O9K6dUCsQtntCgZTDvSoBAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYxC%2B3feALujIgrkSrcA0mviRdmth9QlaOMIRSQnl1BZCIt6M51FBZKy%2BWE3SD4efEZodbn93DeJljdxa3D67B42aXsYDvX1%2BoDMyiARnpA5R9N3QH3NCbbiihj9JKfRh9ScHxX5v9cUGNIL9xnvHt2MCw8hIoMqnoBwRpR%2B43QuhxQmyOvkSr1%2FXaefbr5VKzdjyYgE6w2MbPIJ3BEJfI3dWIOecHCtIhNi%2F%2F0BCn2WKfAaJFM%2B2izLnEgDpMFUQwv4Ovd%2BWZqPJZvLZY7m09A%2FeNPLlVbEBSw6quEevUkuKKWD8lwMliPfBMKp89OU7XA%2FtdbwGFXo9jLUwzo2q%2FV8qAi0OcLNWkQmkHYUiMCQKrAVT%2FkNSzs3FDj9ZIfrGXwI1pAfZJtpp7TqobUaY%2FY9%2F5eIC4sGe0Q%2FkV8d7HwXWgCDCSjNoiFJBooxmOARfsML%2BBhQBXKJFHktbhloX%2FmWV6RyUIhYIAqisNWsZdfb8h%2FjNq5YDXvChQy7wzUZFRNKxE8C7AQ8gbU1Lfym2X3HF%2FZ%2BMuVHyA2ShW6izKYkH46BXaEIoVUb93QfV0et1evh%2BIbnlfOoYnCJnQjv6xYAPg6L%2BvbkKacyU93aDuA3CHKm5cPlPrO2DsUsNwZkZGYg6DfY1u3zL6%2FMP%2BvxMoGOqUBfkdvEmdblGQNb%2F7iDd78CVxsqgynKoJpeuwPzjiP1ENw2qEj7gboAPk8wgTBkc2zCQcOPhNTGKZF8YPKcdM0A6UPtTm6Z4%2Bbg6P0iUXxXLKR3WO8WOW%2BER9W%2FzqZci7DAkMvSYsAiAAr97UKxYBVOtsFBhhGDujaHpFBgtfRgR0RVcjUA4aboZKOjyvUGNi%2FswUu3Gg8cnnqTFKf4oUBUxfj1Wzs&X-Amz-Signature=aee652ec9b3f77ebc61a08189a0805a91708991298b3a3d68892aee92567b9d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFNSXOYJ%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T123138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLP5natGvRMe7kqQKJQykmrtJM9VuZjSH%2Bs8nftcQ%2F4AIgJDUGXz3zCa1OApIOojjc7O9K6dUCsQtntCgZTDvSoBAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYxC%2B3feALujIgrkSrcA0mviRdmth9QlaOMIRSQnl1BZCIt6M51FBZKy%2BWE3SD4efEZodbn93DeJljdxa3D67B42aXsYDvX1%2BoDMyiARnpA5R9N3QH3NCbbiihj9JKfRh9ScHxX5v9cUGNIL9xnvHt2MCw8hIoMqnoBwRpR%2B43QuhxQmyOvkSr1%2FXaefbr5VKzdjyYgE6w2MbPIJ3BEJfI3dWIOecHCtIhNi%2F%2F0BCn2WKfAaJFM%2B2izLnEgDpMFUQwv4Ovd%2BWZqPJZvLZY7m09A%2FeNPLlVbEBSw6quEevUkuKKWD8lwMliPfBMKp89OU7XA%2FtdbwGFXo9jLUwzo2q%2FV8qAi0OcLNWkQmkHYUiMCQKrAVT%2FkNSzs3FDj9ZIfrGXwI1pAfZJtpp7TqobUaY%2FY9%2F5eIC4sGe0Q%2FkV8d7HwXWgCDCSjNoiFJBooxmOARfsML%2BBhQBXKJFHktbhloX%2FmWV6RyUIhYIAqisNWsZdfb8h%2FjNq5YDXvChQy7wzUZFRNKxE8C7AQ8gbU1Lfym2X3HF%2FZ%2BMuVHyA2ShW6izKYkH46BXaEIoVUb93QfV0et1evh%2BIbnlfOoYnCJnQjv6xYAPg6L%2BvbkKacyU93aDuA3CHKm5cPlPrO2DsUsNwZkZGYg6DfY1u3zL6%2FMP%2BvxMoGOqUBfkdvEmdblGQNb%2F7iDd78CVxsqgynKoJpeuwPzjiP1ENw2qEj7gboAPk8wgTBkc2zCQcOPhNTGKZF8YPKcdM0A6UPtTm6Z4%2Bbg6P0iUXxXLKR3WO8WOW%2BER9W%2FzqZci7DAkMvSYsAiAAr97UKxYBVOtsFBhhGDujaHpFBgtfRgR0RVcjUA4aboZKOjyvUGNi%2FswUu3Gg8cnnqTFKf4oUBUxfj1Wzs&X-Amz-Signature=1c402025341ac2912a94fe9d6696e5ab9aa97228394ada404f3e7d4f24112687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







