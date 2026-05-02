



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBQUSHCN%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T021238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCdOGSlfb8smIk4tBzPyQjLo5JuFPSULw4%2Ba7OYvs%2FdywIhAP0QphO8n985NSe%2FRwUVEiEA82akypJjVsXTk2pYxB7XKv8DCDMQABoMNjM3NDIzMTgzODA1Igzv4VI%2FR3n9RSE1pFoq3APwuw63ntnpvMXixs5%2BBVE5S6mEegD6ZsFtVpht4Eb0dk%2BXg%2BewKsPI%2Fuyp7C7ppbHkkX%2BAkioBQZs0W9n%2FrBwISUUQWtcqRMlonC723GQ63cSETesaEOwakKvvYFyR9634xxz8IR%2FFO0vQsOjMP0duyTH9qeXacQGPicD%2FkY7kMwNQlWkjScwZer8amI8cGtAFbMkCQnWglUOZKdSuMd7RNzNgGOhMXM5LwkIMWhNvzrbPcf7d28SD7ziadBxT%2FFChlAxG9yjADFXI1m59PhGlj6yApiP0nt4xvpA0H85lWvWOgsiZoEkv61p662uDLJPQ0A6PzPhcxDFgTX7Je1ToR7MzmgaYUzkSbAWxQ9XZXphnVEn3bjgcTsQ9D94C1uB4oTalAnaHq3ash2hOlRlxQLWTgQa83iogtUFdcWmK%2Fjr8lKyRBQp7EqigBENkNsBtPzwFYZU8J%2Biz3JFI2yxHBWyA%2FULs2zVi2aS8QRJaoHr9xTiBrHhWKtkFDJN46%2F5cXsgN1yPk5STUn5gBh8TsSIItRvNifNtrAe3xtBJw%2FnThbXFktaZn4OgOF9mgxGjlKupOd6735F3dHqhrWzZyTaSD0Q6yuhbkGaJZuE90ZZ5MSjUMbDqrLxDywjCgqNXPBjqkATMb9jXfWSwsr%2BvIWWh8TAy3z%2B8K6PJgOs2DMWriC8dxAKy1KPvReDLIXkBZijMRqsUYibqVm61jmO2e4GhNeMnRM7GNM7flYrMax5zN0EytZIApT366QJY9HSCyVzFgaS5%2BMyc%2BkfclLwbnjbK%2FE7VA%2BizR0Yq5%2B2byCJaqKUF3GpSFgiBvRkJ9gpAchjEUTs%2FLj9TGgVYJk8Tn%2FNMjZRxUCmpD&X-Amz-Signature=3dc4ca2ec6c18f2f2fbf79c6ffb093cbbf8c3b99ee376861b49dd7ad76913aed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBQUSHCN%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T021239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCdOGSlfb8smIk4tBzPyQjLo5JuFPSULw4%2Ba7OYvs%2FdywIhAP0QphO8n985NSe%2FRwUVEiEA82akypJjVsXTk2pYxB7XKv8DCDMQABoMNjM3NDIzMTgzODA1Igzv4VI%2FR3n9RSE1pFoq3APwuw63ntnpvMXixs5%2BBVE5S6mEegD6ZsFtVpht4Eb0dk%2BXg%2BewKsPI%2Fuyp7C7ppbHkkX%2BAkioBQZs0W9n%2FrBwISUUQWtcqRMlonC723GQ63cSETesaEOwakKvvYFyR9634xxz8IR%2FFO0vQsOjMP0duyTH9qeXacQGPicD%2FkY7kMwNQlWkjScwZer8amI8cGtAFbMkCQnWglUOZKdSuMd7RNzNgGOhMXM5LwkIMWhNvzrbPcf7d28SD7ziadBxT%2FFChlAxG9yjADFXI1m59PhGlj6yApiP0nt4xvpA0H85lWvWOgsiZoEkv61p662uDLJPQ0A6PzPhcxDFgTX7Je1ToR7MzmgaYUzkSbAWxQ9XZXphnVEn3bjgcTsQ9D94C1uB4oTalAnaHq3ash2hOlRlxQLWTgQa83iogtUFdcWmK%2Fjr8lKyRBQp7EqigBENkNsBtPzwFYZU8J%2Biz3JFI2yxHBWyA%2FULs2zVi2aS8QRJaoHr9xTiBrHhWKtkFDJN46%2F5cXsgN1yPk5STUn5gBh8TsSIItRvNifNtrAe3xtBJw%2FnThbXFktaZn4OgOF9mgxGjlKupOd6735F3dHqhrWzZyTaSD0Q6yuhbkGaJZuE90ZZ5MSjUMbDqrLxDywjCgqNXPBjqkATMb9jXfWSwsr%2BvIWWh8TAy3z%2B8K6PJgOs2DMWriC8dxAKy1KPvReDLIXkBZijMRqsUYibqVm61jmO2e4GhNeMnRM7GNM7flYrMax5zN0EytZIApT366QJY9HSCyVzFgaS5%2BMyc%2BkfclLwbnjbK%2FE7VA%2BizR0Yq5%2B2byCJaqKUF3GpSFgiBvRkJ9gpAchjEUTs%2FLj9TGgVYJk8Tn%2FNMjZRxUCmpD&X-Amz-Signature=36d7ad84f1ab4edeb24fc0a94af75f69f0a720c2050f054fe87281269547da3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







