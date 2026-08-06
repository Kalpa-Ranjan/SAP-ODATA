



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM36G3SD%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T235302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIDMpK9DSTkUhRVEOkPWwHzndqwY0%2FmxaY%2FdlDKbisUu1AiEA6z44SnsMGPPNBmh%2BB3sPwcSngkvuyRw9C9vV2G86cLQq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDLn1pcUYvlkNynLDeCrcA6EhsoBGtkg4Y6sGInmnxGARST9beOxD%2FnfLzk50WlMaFROq8W7TKNQWXOtvMoVXDuo8g7fAGtQGO2WuAoDJtgqzeskIJPifgCqcazjVq7QbQOncFewklMer%2FKNnBYvXd5JhpP8nM%2FJUGdVuI5qE0mDcKymCF2js1k0ITWiPNNErnE%2Fr8BpeyVfXxl77jPL6hJJHI2%2FBhzuFu%2BEZSRllmOae5pIW0k0kvOPbbhC4bO1%2BF9XFr9TQafOc81av2KhDaudyPTmaUQ3782eo4VxXkjJKD%2BU8E7ecLuaHA7h5ehgl%2F9l2MEa%2BPqtjEuJF0oUtBaKtAeV%2Bp932ABUZQxXKsfSu6nf4%2BxL%2BzQou75WZkcXmrR8TOvPNRj9rTLLI%2F5vlKsAou3rz3R8TDQa76XcCQod5g6ROVuIBdRelqmhvrXmMz5YwtvardCKS9PmOOGWp7%2Bj2gLLiC1tMMdRpZo1AhyBxyoHSgD0iqZJVJXNuCdG%2FhAS6DDwmv25mXS%2Fb2bC7Fmm9IOeoN1OI5j1TOIXL4gNPb2jVv7sIesY87LI6VssMfRbc2OHWtXp4JjK00c9WOdDitLLnI7LsnijhoHFoY9uATgtX36sVF9Wynv5pmwgAdOnLPZ15CY%2F5f8SXMLep1NMGOqUBjIewB5HD26sVscGu6%2F%2FoaQvAyJpfnBRL2dEVPHQJ7yh4fAXyYmSzJK24EvEBgc8HSAadPw2Hf%2FQGH3Q6H1vnrGIbPSDqfnZAVCZj8pzyys3B6M36coqGY2gMUMxKe69XM90Y3Aj3dMadBSevyrGDQ6Z6z8psp51IOPXiyr%2BuwUVwqNFyacJh7Rtvnds7OgSSUQH8lWVp7W%2FNYPsDWqSxZRgR5F5m&X-Amz-Signature=ed8b55526fc33e3b01a139478d8fcd1e22018c56da7c8f0e3b368ab4e0b70731&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XM36G3SD%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T235302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIDMpK9DSTkUhRVEOkPWwHzndqwY0%2FmxaY%2FdlDKbisUu1AiEA6z44SnsMGPPNBmh%2BB3sPwcSngkvuyRw9C9vV2G86cLQq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDLn1pcUYvlkNynLDeCrcA6EhsoBGtkg4Y6sGInmnxGARST9beOxD%2FnfLzk50WlMaFROq8W7TKNQWXOtvMoVXDuo8g7fAGtQGO2WuAoDJtgqzeskIJPifgCqcazjVq7QbQOncFewklMer%2FKNnBYvXd5JhpP8nM%2FJUGdVuI5qE0mDcKymCF2js1k0ITWiPNNErnE%2Fr8BpeyVfXxl77jPL6hJJHI2%2FBhzuFu%2BEZSRllmOae5pIW0k0kvOPbbhC4bO1%2BF9XFr9TQafOc81av2KhDaudyPTmaUQ3782eo4VxXkjJKD%2BU8E7ecLuaHA7h5ehgl%2F9l2MEa%2BPqtjEuJF0oUtBaKtAeV%2Bp932ABUZQxXKsfSu6nf4%2BxL%2BzQou75WZkcXmrR8TOvPNRj9rTLLI%2F5vlKsAou3rz3R8TDQa76XcCQod5g6ROVuIBdRelqmhvrXmMz5YwtvardCKS9PmOOGWp7%2Bj2gLLiC1tMMdRpZo1AhyBxyoHSgD0iqZJVJXNuCdG%2FhAS6DDwmv25mXS%2Fb2bC7Fmm9IOeoN1OI5j1TOIXL4gNPb2jVv7sIesY87LI6VssMfRbc2OHWtXp4JjK00c9WOdDitLLnI7LsnijhoHFoY9uATgtX36sVF9Wynv5pmwgAdOnLPZ15CY%2F5f8SXMLep1NMGOqUBjIewB5HD26sVscGu6%2F%2FoaQvAyJpfnBRL2dEVPHQJ7yh4fAXyYmSzJK24EvEBgc8HSAadPw2Hf%2FQGH3Q6H1vnrGIbPSDqfnZAVCZj8pzyys3B6M36coqGY2gMUMxKe69XM90Y3Aj3dMadBSevyrGDQ6Z6z8psp51IOPXiyr%2BuwUVwqNFyacJh7Rtvnds7OgSSUQH8lWVp7W%2FNYPsDWqSxZRgR5F5m&X-Amz-Signature=dc9faa26aa9c4e12d97bc0871b4a94b3f317f81f5be6ef0c8545c576857d27d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







