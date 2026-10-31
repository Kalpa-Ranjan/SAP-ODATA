



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5XHQHMM%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T180501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBV4UjeHrzdnM4QMn%2BwtX7FfBWcWh2ImAUFdasaIywtgAiEAnXm0AOORuQb1nWD4%2FtgqYP4aupV4qWK6wB2DubEl1U8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDD7V1xyxIVtA%2FggAxCrcA4OgoyRXp97v%2Fqr1rBqADcX5Jo4%2B9KIGdblX%2FqBla7M6TAgtlG2QduaZi4GMiUgeQK81jusu%2BF0pI%2BmH1qxbjFUtaVULDUCHTvQT25fozaVMvUDfWgmutebnVvabnMhOMI2xj%2F7%2BvfxCcp36n8PhnD4CZDGT%2BlKsvjrSaFtvZFRS06TRK7QtIViFBa%2F9ULwIYKD7K3x5bpRP97Kw0zJR8mDmEYvr19zth6UQJGRitrrInSjlBUkPvRL%2Fcx5sh1JyZXMmj7JdXPB0fAyczyiaIZrFxn2RB%2FSu8EaJfKZhyQVHGQF5gknrl0cQuA2VGaYpvBwrdRTYn0WmkkYqoa6U58k3O7GPo6SgvWFQ04rYRii%2FF3OFbi91y%2BH60KZ9EL0tSuNUlx5mqedNUha4Nu8OiPRKAxni%2FgVtKyJNkMs8hrI6OLh3XNpKbLbw%2BWoO3fn4jcYFNJLAIxFKbnVjo3PbN6asEZyWhVueE9rMtbkzfQffYZxsl951sxpK4ieBvV58Cwcd6%2B3diTBBKzdEA32rqXdHvw%2FfZ%2FvYUkxaLswZb4hNaZdS3VXJ3mWownAiDfA31uH6Mut5gRw32hTzOAsPdrWWGh%2FCRUW7JzqWzXCwx0l8S6vnEHE119Hm6RjVMPuqmNcGOqUBDJwwkKycy08J%2B0OlsV1d7e%2FSGxmgylrE9nLap2%2FZgcb0U6V0nPYLE81Ukedy6MJTiBIzChGrdtxdRNlxD4Sm9p91T8KtaJXUjeriKnRX7ABd4%2BFMEH7Irj4%2Bvgf4l5GbKEr4f%2B37A2TGyXH%2FmwyULu3lpv92nFNMGQivKzGeAAvOln199IypGSacowE7MHzagHD8s69Hc%2Bev8NnU%2Bl9Pyl6k1JCg&X-Amz-Signature=5677cfa8b3af7571a803b1e8bb76d21347137f829e716c3b4d8ae6e258e14d21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5XHQHMM%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T180501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBV4UjeHrzdnM4QMn%2BwtX7FfBWcWh2ImAUFdasaIywtgAiEAnXm0AOORuQb1nWD4%2FtgqYP4aupV4qWK6wB2DubEl1U8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDD7V1xyxIVtA%2FggAxCrcA4OgoyRXp97v%2Fqr1rBqADcX5Jo4%2B9KIGdblX%2FqBla7M6TAgtlG2QduaZi4GMiUgeQK81jusu%2BF0pI%2BmH1qxbjFUtaVULDUCHTvQT25fozaVMvUDfWgmutebnVvabnMhOMI2xj%2F7%2BvfxCcp36n8PhnD4CZDGT%2BlKsvjrSaFtvZFRS06TRK7QtIViFBa%2F9ULwIYKD7K3x5bpRP97Kw0zJR8mDmEYvr19zth6UQJGRitrrInSjlBUkPvRL%2Fcx5sh1JyZXMmj7JdXPB0fAyczyiaIZrFxn2RB%2FSu8EaJfKZhyQVHGQF5gknrl0cQuA2VGaYpvBwrdRTYn0WmkkYqoa6U58k3O7GPo6SgvWFQ04rYRii%2FF3OFbi91y%2BH60KZ9EL0tSuNUlx5mqedNUha4Nu8OiPRKAxni%2FgVtKyJNkMs8hrI6OLh3XNpKbLbw%2BWoO3fn4jcYFNJLAIxFKbnVjo3PbN6asEZyWhVueE9rMtbkzfQffYZxsl951sxpK4ieBvV58Cwcd6%2B3diTBBKzdEA32rqXdHvw%2FfZ%2FvYUkxaLswZb4hNaZdS3VXJ3mWownAiDfA31uH6Mut5gRw32hTzOAsPdrWWGh%2FCRUW7JzqWzXCwx0l8S6vnEHE119Hm6RjVMPuqmNcGOqUBDJwwkKycy08J%2B0OlsV1d7e%2FSGxmgylrE9nLap2%2FZgcb0U6V0nPYLE81Ukedy6MJTiBIzChGrdtxdRNlxD4Sm9p91T8KtaJXUjeriKnRX7ABd4%2BFMEH7Irj4%2Bvgf4l5GbKEr4f%2B37A2TGyXH%2FmwyULu3lpv92nFNMGQivKzGeAAvOln199IypGSacowE7MHzagHD8s69Hc%2Bev8NnU%2Bl9Pyl6k1JCg&X-Amz-Signature=dfd46fb0398c93b9ab5cdd81fb0d122ac30cd04498ff1f6639cea51135d6a1d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







