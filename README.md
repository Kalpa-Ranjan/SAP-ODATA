



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBKJ2FYF%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T060706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIHCLYm5MhFoLu33eSkNYieE2jQaAuUozt5O21OgIcZ2gAiEA%2BShL4pbUNpToA0EtYzTBfE8xg4ADZjTIIMoD%2BbT%2Bzk8q%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDAIQ85LeM1L%2FoIDbhSrcA0ot83ct1DXhTC2fZYAPSX401p1zD5OgfFV5ZZ1%2BB84YbOOYXSXvB4KR935a90teKulRlkcez5%2FCwxb3uIsy5vtA50sjXBNnFHBVexqOEJaUwOpdByyj8dsl964%2FOWJ%2FL8jEwUQX3snLfCCtY64FNNmXr63xu%2BaaxILJetZAlM2eJh6pwHGdU5jI69%2F8AxG2907WlQwKvrZzfpX%2BZ9z75S6bNiwDqOUbAB%2B56NJirfZ3Dz38S8G64kUvgVunkSvo9tt78xnN1%2FD%2B10drYjDz645EUotDk2E%2F7harufp14DENGtgZgPJkAeHEKohUjZbwttxlmUOTJyUV0MD7VXzEIN%2FPbF4XLQuwIg1Njzhq%2F3gEyTaa5g9iKR6tA58O%2F%2Fp3P142f7hucaWQEdGRfBWVPNSPy2UXr2UvBA2zN3iJ5ElZf12zjK4r5fMIkYrlaPDUTES7%2F%2F%2BdQ%2BE6vV80Psl0fVjY8QMklllQBWZTi14wsLgLECxi9s74D5lKzHkBBVymZNELygKmd4M32RYal5QabjhHYZU%2BsmgaD2yV6ShRR7tIAO81FtIIZu4xItrwySUg6pCvEGMBmS%2Fb5CxdFVpSXYNUUp7y5eThrxld6Y5t8Cz78qTAMb20YhvgeXXNMPPnldcGOqUB1cF3zZfpWe2d%2Fs%2F%2FrmBScwZv%2B0fbMn8jI6tmYT5XbPNJ%2FCW1Z%2BzQ%2Bl4KYauPoXMGGbwyY%2B%2FMxyyCe7V6qwSPNxHdzqyWKIIhbVWMV3DfYM5ovBbuL0%2BmFbDgq1gq0evC2Flk%2B8dUSOefiOjJ9p3RrMU16Dy0nkfAcDNt0vSIAC7W3AtVcjCOkHpLKEYjgR1DOetgH6D8yZAY6bQjKm8GRLhISKE3&X-Amz-Signature=491a9b0600219e8ff8d3e4ea03e3c429894d1574790734fae572d9743762c47f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBKJ2FYF%2F20261031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261031T060706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIHCLYm5MhFoLu33eSkNYieE2jQaAuUozt5O21OgIcZ2gAiEA%2BShL4pbUNpToA0EtYzTBfE8xg4ADZjTIIMoD%2BbT%2Bzk8q%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDAIQ85LeM1L%2FoIDbhSrcA0ot83ct1DXhTC2fZYAPSX401p1zD5OgfFV5ZZ1%2BB84YbOOYXSXvB4KR935a90teKulRlkcez5%2FCwxb3uIsy5vtA50sjXBNnFHBVexqOEJaUwOpdByyj8dsl964%2FOWJ%2FL8jEwUQX3snLfCCtY64FNNmXr63xu%2BaaxILJetZAlM2eJh6pwHGdU5jI69%2F8AxG2907WlQwKvrZzfpX%2BZ9z75S6bNiwDqOUbAB%2B56NJirfZ3Dz38S8G64kUvgVunkSvo9tt78xnN1%2FD%2B10drYjDz645EUotDk2E%2F7harufp14DENGtgZgPJkAeHEKohUjZbwttxlmUOTJyUV0MD7VXzEIN%2FPbF4XLQuwIg1Njzhq%2F3gEyTaa5g9iKR6tA58O%2F%2Fp3P142f7hucaWQEdGRfBWVPNSPy2UXr2UvBA2zN3iJ5ElZf12zjK4r5fMIkYrlaPDUTES7%2F%2F%2BdQ%2BE6vV80Psl0fVjY8QMklllQBWZTi14wsLgLECxi9s74D5lKzHkBBVymZNELygKmd4M32RYal5QabjhHYZU%2BsmgaD2yV6ShRR7tIAO81FtIIZu4xItrwySUg6pCvEGMBmS%2Fb5CxdFVpSXYNUUp7y5eThrxld6Y5t8Cz78qTAMb20YhvgeXXNMPPnldcGOqUB1cF3zZfpWe2d%2Fs%2F%2FrmBScwZv%2B0fbMn8jI6tmYT5XbPNJ%2FCW1Z%2BzQ%2Bl4KYauPoXMGGbwyY%2B%2FMxyyCe7V6qwSPNxHdzqyWKIIhbVWMV3DfYM5ovBbuL0%2BmFbDgq1gq0evC2Flk%2B8dUSOefiOjJ9p3RrMU16Dy0nkfAcDNt0vSIAC7W3AtVcjCOkHpLKEYjgR1DOetgH6D8yZAY6bQjKm8GRLhISKE3&X-Amz-Signature=88c409c17511f4e780e38729208613270ac1bca8b6c741906a8c0c0cdd8caab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







