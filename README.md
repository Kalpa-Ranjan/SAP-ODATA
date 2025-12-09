



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUC5HIXJ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T011415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCu0gpBqFwC5m3Sy9549RrVZz%2FKzEL0u8A7MHNRhgEhAiAuhASrzy2PPiyWfWCcZKjNha6wFeve4CGhTMYuugAmeCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgrgfEjQea6am52iZKtwD8KDQjhBAwZgXpOCLkf75xqQH2bccohsE%2FUMJDPJFN66IiSCnExUBHGqN1%2BrCJtNqprIhdG%2F0GqTVXLBuQ7Nv%2Bo15g7O12nKmHKuVG1aLhGbR6NvsmIbJ0MXtvScvrlHWGC4N7T7XwgykDvv%2FV5yCoXNNrB4bMekaT8n75h69KNSdfLRkRCpoUYhFWsizzzN4aPtw0VG8%2FOcHhDvF7VfMXuxzXRYKtarIWxgjXHh0Nu1bR%2BE%2FX22%2BW%2BbFE0uJJrGPQ2%2FpvPSAYrqeYftDaJ8MtdxmzvQi7sbccrk3tvvRckvFbcyGsK6ZIrFqVzOg80FZMWxbue3Wu5LYxNS9CBblg7FfmaFKUoaCwvuIG1gg2X0%2Fpzg%2BCwtN3XWnzBrtdK%2FyVuv4mLx6tvZ1QtfM2FSn6GoNciXaG3iAvrP7jxUhGvJtqJlCtOpvyFfDfMtUqVbIGQhoXXa7emJR9lMHA4x4d5L4MEEu5q1MSBmUMoN1P%2FB5tjgT4eMfTLO%2BtwR%2F3wmiznfjV1wG6sJ%2B8FO5KFBFxr6WNzSpN1vymhsz6N1WvC9QNcLGI0F19kpIyiGY0FY1SXppZvEG3WoJPSSzcYeMEp5qsD3F3LiDqAAq%2BP6s%2BX6Wa%2BGQyaaywzqQhhYw3OndyQY6pgFzRfjRy%2BY62a%2BuAC7MSttGaoMweqd0df8rHDnw6CphSXlqx7pCET5Y55su%2BFpKTCCNmaWDoIxq9xRq164T3%2BpyOac%2Byhh7jXjWicY5UpKjpGkxQuav8UI9m6rAxrGO7gSjBEPvaMSsSCc3t6dBay8Qoq6oYCUmX2aNgGEF4vfIwSibNIHGhszSMKYqoq2O1fXm2bZDPuBZtJKmzJvRuXXUr34K1Z%2Fg&X-Amz-Signature=b9a7d7fdc29184e7d88b802bae1afc964802909ce0e6ff8a9e16dfc2dd694a1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUC5HIXJ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T011416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCu0gpBqFwC5m3Sy9549RrVZz%2FKzEL0u8A7MHNRhgEhAiAuhASrzy2PPiyWfWCcZKjNha6wFeve4CGhTMYuugAmeCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgrgfEjQea6am52iZKtwD8KDQjhBAwZgXpOCLkf75xqQH2bccohsE%2FUMJDPJFN66IiSCnExUBHGqN1%2BrCJtNqprIhdG%2F0GqTVXLBuQ7Nv%2Bo15g7O12nKmHKuVG1aLhGbR6NvsmIbJ0MXtvScvrlHWGC4N7T7XwgykDvv%2FV5yCoXNNrB4bMekaT8n75h69KNSdfLRkRCpoUYhFWsizzzN4aPtw0VG8%2FOcHhDvF7VfMXuxzXRYKtarIWxgjXHh0Nu1bR%2BE%2FX22%2BW%2BbFE0uJJrGPQ2%2FpvPSAYrqeYftDaJ8MtdxmzvQi7sbccrk3tvvRckvFbcyGsK6ZIrFqVzOg80FZMWxbue3Wu5LYxNS9CBblg7FfmaFKUoaCwvuIG1gg2X0%2Fpzg%2BCwtN3XWnzBrtdK%2FyVuv4mLx6tvZ1QtfM2FSn6GoNciXaG3iAvrP7jxUhGvJtqJlCtOpvyFfDfMtUqVbIGQhoXXa7emJR9lMHA4x4d5L4MEEu5q1MSBmUMoN1P%2FB5tjgT4eMfTLO%2BtwR%2F3wmiznfjV1wG6sJ%2B8FO5KFBFxr6WNzSpN1vymhsz6N1WvC9QNcLGI0F19kpIyiGY0FY1SXppZvEG3WoJPSSzcYeMEp5qsD3F3LiDqAAq%2BP6s%2BX6Wa%2BGQyaaywzqQhhYw3OndyQY6pgFzRfjRy%2BY62a%2BuAC7MSttGaoMweqd0df8rHDnw6CphSXlqx7pCET5Y55su%2BFpKTCCNmaWDoIxq9xRq164T3%2BpyOac%2Byhh7jXjWicY5UpKjpGkxQuav8UI9m6rAxrGO7gSjBEPvaMSsSCc3t6dBay8Qoq6oYCUmX2aNgGEF4vfIwSibNIHGhszSMKYqoq2O1fXm2bZDPuBZtJKmzJvRuXXUr34K1Z%2Fg&X-Amz-Signature=c2d83f2e84e49eb6c1ffae7dacd20057ad440528e1b1c1f5798d4d471911fb41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







