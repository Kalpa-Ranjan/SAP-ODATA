



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665COBMSLT%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T062444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtaYVrkwu6FbXta4BlmyAWZ0vRcIOUDpxQd90kEquptwIhALVonWpJ05GGO1DeWqYukljkjP8aOuwOO23E7QqNixXWKv8DCHUQABoMNjM3NDIzMTgzODA1Igyk2HZ%2FXQoEMuE%2FnHYq3APAjrETdc1jEbKE8vjv38s9z7QNy%2B5iWxLBz3lXaMDF26LeakBr2N9iGGO%2Bzyf45mTgHvBrcixn6F6FC5Js4kDMzAfPdUyH7mjnHBHgG8uEASLxXi%2BMhoHWYHaTiGlh5vG2PjBm09yQRVQGjclBRMH2LDDMC2W6EnqA5timkgFiMFwXx0V7HnNXNYJZunBaw%2FFS%2Fm4qYvpffaRDHm54lvS9tyPaP3V2EHtsuhm%2Fm%2FTfC8iGfmHITz1IqrD%2FBbVMAs3CeD99KsRWOSoWML6eEBEIROc8hcCOBp3yzfhGIK4yGGt64%2F0KDAolC5%2BL8gX0afJiNgXPWB3i2lDem%2BlPKadKK32MtKMbHt4Gcno6ZXzUjC1nOPSrEvDU%2BJtj0E8DbkStea2Jh0wnQmgwRHowwVvOM7R4iYA75mFEhmsZ0lj88MmstygCwMYn4CXay1TUSWwvjYxZTJPq8Mm9Wxnp%2F4t%2FtjCvqxIPWtg2ved9w4rflcpz0CGwt943UnfYyDBe8mWhaUfGByvPY00Yv3VkV02u8HgIpKcCTlE8ztCZybN2KURCPbfr8nSVrMPe8CimH6zeMe9Tz0XuwrSjFO6dS2Nu1DODXUxoLHkel29yYQYXyWfrRqXvsyJD8sTSezD1pbHLBjqkASBf1%2BGEGcumdcfc%2F8rHIRuRQ1fn7gDT%2BT8xNndm5ceW6fa5HG18RQqJEiu0Gxm0GN5xIksHdVmTyJ7NNc1tgRS9Npt%2FGguuhpGqru2x9gwzGDJ6zas0wbq00to0Ai4%2FkkNd35QFO91M1wRjRZXZWpp8FUurB1SxWeWhgQodX15DaEnHLSVwWGvzPQEYGdX9KPmMuxQrxM9AptmP%2BZEgbv7YPpiS&X-Amz-Signature=92395bb3acbbd225b34b1752437f174d082c33411e00c47977de38b178f1881a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665COBMSLT%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T062444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtaYVrkwu6FbXta4BlmyAWZ0vRcIOUDpxQd90kEquptwIhALVonWpJ05GGO1DeWqYukljkjP8aOuwOO23E7QqNixXWKv8DCHUQABoMNjM3NDIzMTgzODA1Igyk2HZ%2FXQoEMuE%2FnHYq3APAjrETdc1jEbKE8vjv38s9z7QNy%2B5iWxLBz3lXaMDF26LeakBr2N9iGGO%2Bzyf45mTgHvBrcixn6F6FC5Js4kDMzAfPdUyH7mjnHBHgG8uEASLxXi%2BMhoHWYHaTiGlh5vG2PjBm09yQRVQGjclBRMH2LDDMC2W6EnqA5timkgFiMFwXx0V7HnNXNYJZunBaw%2FFS%2Fm4qYvpffaRDHm54lvS9tyPaP3V2EHtsuhm%2Fm%2FTfC8iGfmHITz1IqrD%2FBbVMAs3CeD99KsRWOSoWML6eEBEIROc8hcCOBp3yzfhGIK4yGGt64%2F0KDAolC5%2BL8gX0afJiNgXPWB3i2lDem%2BlPKadKK32MtKMbHt4Gcno6ZXzUjC1nOPSrEvDU%2BJtj0E8DbkStea2Jh0wnQmgwRHowwVvOM7R4iYA75mFEhmsZ0lj88MmstygCwMYn4CXay1TUSWwvjYxZTJPq8Mm9Wxnp%2F4t%2FtjCvqxIPWtg2ved9w4rflcpz0CGwt943UnfYyDBe8mWhaUfGByvPY00Yv3VkV02u8HgIpKcCTlE8ztCZybN2KURCPbfr8nSVrMPe8CimH6zeMe9Tz0XuwrSjFO6dS2Nu1DODXUxoLHkel29yYQYXyWfrRqXvsyJD8sTSezD1pbHLBjqkASBf1%2BGEGcumdcfc%2F8rHIRuRQ1fn7gDT%2BT8xNndm5ceW6fa5HG18RQqJEiu0Gxm0GN5xIksHdVmTyJ7NNc1tgRS9Npt%2FGguuhpGqru2x9gwzGDJ6zas0wbq00to0Ai4%2FkkNd35QFO91M1wRjRZXZWpp8FUurB1SxWeWhgQodX15DaEnHLSVwWGvzPQEYGdX9KPmMuxQrxM9AptmP%2BZEgbv7YPpiS&X-Amz-Signature=364625b92ec0e20d1f0d1ee6112d72e92f42416869272db57e82bb9fb4d0d34e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







