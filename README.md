



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVHP5D%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T183117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIG2E2Qgyizy8hZx0r0XIVkxtKznqK2sryjkfQhKzuIgoAiArF64%2BgiqR%2FTzNWuU4rTyG250HJ5t0yyV9W7KjGkJ2gCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMspzOWf01epB02dR2KtwDhL0yI6rZIef2Wy%2BNRXnyBxcSxsR2DIZUd42sP4EE0Yq37TDNASGyiqdJEjv5a5I6NzjVB7Yi6N%2B6OiFkWrUXQES8fb4UM5NTKvI98xuFlak7aIwtREa4igHE9VgHotYi80ZWGiN%2BCkLPJulRUjZlgoOHkigCAzRrXGeR7nF%2BGoZ5Q0ixIbo%2FGF7HEvAP8P6dfh0aBAaEuL5L1zIp5Mf4ZdVS8h8bjirTjupIHUkykXEfkzYSNcTXgU774o0eCbq3f%2BHx0VssXtAgHgfB3Sk40jfaQgCbyz%2FliMnsfXOveiiED9LpVzKR1lnBCU8v2bQZPGT8Wrc%2FsC6RyfrFZ9yKxZbAbaqylH9z8ldnwqbVO02ddo2nPtwP%2BPxiP4fZF3Wmg1FkVhdgaxolUNK9GxoipPTsw97lP%2B%2FKnlRvXQ31K%2F70KZgMdMXqy%2Fq3gP4A%2FT0tOJsRVZUzI8GZ5IHLpw46%2BxI%2BfG6GlPscGpST3i5SYMCJQVfwb8gU1BLqbUDmEOl8i87tSTvkR7HSf%2FriWkrePxy9dmOYWx5dLyQGbvjAo7K5DQdWojpmTYydwU67Jd5Sq6HAGfDZCm2fPZ3lREigU%2FaJRVEXeEajP70CKbMfQMJDDcG0TSu3c%2BiRqvcwxv2x1AY6pgG3wC%2BnUE0BTIssk9m7KE4NwxQsPhPJfKMzRgR20xVg9iYNbpM5wVX%2BYDKjO0s0aVq7IPoQP3vF%2BuvFX%2FtwLqFZ%2B6WH%2Fr3hGw5FyLWlnEQ96iO85O9jUV%2FdGI%2F%2B3zXCnsMr334uKj7TPonY%2Bv5qet%2BQX7sXKrpIPPCY7snLgA%2B1GNnFrTaSYirJ64wnb4YlT0jArtkn1nFHWPxFARE5ODfjjvLGHsvu&X-Amz-Signature=7d4c08940f9e7c237c120e54f8284aa973548ddb544adf8e6b591bae0065eac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEVHP5D%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T183117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIG2E2Qgyizy8hZx0r0XIVkxtKznqK2sryjkfQhKzuIgoAiArF64%2BgiqR%2FTzNWuU4rTyG250HJ5t0yyV9W7KjGkJ2gCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMspzOWf01epB02dR2KtwDhL0yI6rZIef2Wy%2BNRXnyBxcSxsR2DIZUd42sP4EE0Yq37TDNASGyiqdJEjv5a5I6NzjVB7Yi6N%2B6OiFkWrUXQES8fb4UM5NTKvI98xuFlak7aIwtREa4igHE9VgHotYi80ZWGiN%2BCkLPJulRUjZlgoOHkigCAzRrXGeR7nF%2BGoZ5Q0ixIbo%2FGF7HEvAP8P6dfh0aBAaEuL5L1zIp5Mf4ZdVS8h8bjirTjupIHUkykXEfkzYSNcTXgU774o0eCbq3f%2BHx0VssXtAgHgfB3Sk40jfaQgCbyz%2FliMnsfXOveiiED9LpVzKR1lnBCU8v2bQZPGT8Wrc%2FsC6RyfrFZ9yKxZbAbaqylH9z8ldnwqbVO02ddo2nPtwP%2BPxiP4fZF3Wmg1FkVhdgaxolUNK9GxoipPTsw97lP%2B%2FKnlRvXQ31K%2F70KZgMdMXqy%2Fq3gP4A%2FT0tOJsRVZUzI8GZ5IHLpw46%2BxI%2BfG6GlPscGpST3i5SYMCJQVfwb8gU1BLqbUDmEOl8i87tSTvkR7HSf%2FriWkrePxy9dmOYWx5dLyQGbvjAo7K5DQdWojpmTYydwU67Jd5Sq6HAGfDZCm2fPZ3lREigU%2FaJRVEXeEajP70CKbMfQMJDDcG0TSu3c%2BiRqvcwxv2x1AY6pgG3wC%2BnUE0BTIssk9m7KE4NwxQsPhPJfKMzRgR20xVg9iYNbpM5wVX%2BYDKjO0s0aVq7IPoQP3vF%2BuvFX%2FtwLqFZ%2B6WH%2Fr3hGw5FyLWlnEQ96iO85O9jUV%2FdGI%2F%2B3zXCnsMr334uKj7TPonY%2Bv5qet%2BQX7sXKrpIPPCY7snLgA%2B1GNnFrTaSYirJ64wnb4YlT0jArtkn1nFHWPxFARE5ODfjjvLGHsvu&X-Amz-Signature=647aa3872fed9a310ad286414c28eabd5ac512d3842f18729490361a77ad53ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







