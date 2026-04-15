



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BCKL5L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T020145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCw8R%2BcZRgrq64qYtSNIZkwoZf6alcyAJ8ir%2FWdvrZTsAIgY1Ak4moG31sfDdcGwQTojCy6KVB7XPjnmNpy9UimgeUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEVjlLF5JzIBjJ%2BjSrcA7IaBw4ljkrmJAEuHNzIwQijF4i91POU%2BOY9x%2FlE8s4rX1BbUMx1nR3LMETkX%2BGNgw6OeQoi%2BzIgp5T%2FK2jNqG7RzUoTx3%2BcnJ48z44%2Fzw%2FZBQ3R7DDKQRGyEXCiOxu5GxGL6UDWtum3Zmf90ECXcNa5nfJ5G0ja%2Fq8vUmgqXpqlZaUF5LrDuWyTucc9%2FClt7HChWVaBEE2rN52fC3idT6MLdMQMV6aUIOJP86wF3VnLwerLdi%2FYb3NzV4FadQkUq0tsdbvRZ54qxFQ707fDoXLvTfDdMnsPKFindONZ9R6KKJgjX6ABUqBOukWgP0PfayGxKdBNhO975ahfGre9apAOydv1AcuNl0SBkTjWlKrf1FQtjYlMMCvznxL2OUssF5EzqKVAqf%2F2y897mGLHop49zsYi6PvBFSCFX66ThAgEZhmU%2FiViKzsGIQX7HKXANyOV6KaCKY0d2GJgRWuyJdk5G5TP2EFE6KWRyt6H1wuvKCwzbNJpntuMuzRi6IQHn2h9SCY0C4qNL9b1mEKM%2Bkiq6wJ%2B1RcY2OVUwSgpi3Mx2j0taCplCQQSIEfwwTxqjYRfKU01wHr9ZIMARBTCkjIF7MNNzyaeJekXL2jiCUkOGb43xt0rWF%2F4Z%2B4GMObh%2B84GOqUBxNulN5i6nInmEMb4pGGx4AsQUCfYd71wNrX5r0t6C9Mgia3ceQVteGpYohlGc6c0m0pyK0F%2FgqIThGknwvWrnms80fhQbVtfYdE7Pu81p%2BWPS2qOszUuh4qknuck0MoDabkrirS7vhHKrQwQ71BstTkYZnAU%2BN1hYyoP5gOKCJywhrsCdd%2FmItsBnYPcTQVU99LfMXlGDs%2B2MiWW3zEdbyo2eE3R&X-Amz-Signature=902d0f873c00cd3d6f1bca60d3f4abb1418f141360a9abf35fd1dcc03f6aa1e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BCKL5L%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T020145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCw8R%2BcZRgrq64qYtSNIZkwoZf6alcyAJ8ir%2FWdvrZTsAIgY1Ak4moG31sfDdcGwQTojCy6KVB7XPjnmNpy9UimgeUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEVjlLF5JzIBjJ%2BjSrcA7IaBw4ljkrmJAEuHNzIwQijF4i91POU%2BOY9x%2FlE8s4rX1BbUMx1nR3LMETkX%2BGNgw6OeQoi%2BzIgp5T%2FK2jNqG7RzUoTx3%2BcnJ48z44%2Fzw%2FZBQ3R7DDKQRGyEXCiOxu5GxGL6UDWtum3Zmf90ECXcNa5nfJ5G0ja%2Fq8vUmgqXpqlZaUF5LrDuWyTucc9%2FClt7HChWVaBEE2rN52fC3idT6MLdMQMV6aUIOJP86wF3VnLwerLdi%2FYb3NzV4FadQkUq0tsdbvRZ54qxFQ707fDoXLvTfDdMnsPKFindONZ9R6KKJgjX6ABUqBOukWgP0PfayGxKdBNhO975ahfGre9apAOydv1AcuNl0SBkTjWlKrf1FQtjYlMMCvznxL2OUssF5EzqKVAqf%2F2y897mGLHop49zsYi6PvBFSCFX66ThAgEZhmU%2FiViKzsGIQX7HKXANyOV6KaCKY0d2GJgRWuyJdk5G5TP2EFE6KWRyt6H1wuvKCwzbNJpntuMuzRi6IQHn2h9SCY0C4qNL9b1mEKM%2Bkiq6wJ%2B1RcY2OVUwSgpi3Mx2j0taCplCQQSIEfwwTxqjYRfKU01wHr9ZIMARBTCkjIF7MNNzyaeJekXL2jiCUkOGb43xt0rWF%2F4Z%2B4GMObh%2B84GOqUBxNulN5i6nInmEMb4pGGx4AsQUCfYd71wNrX5r0t6C9Mgia3ceQVteGpYohlGc6c0m0pyK0F%2FgqIThGknwvWrnms80fhQbVtfYdE7Pu81p%2BWPS2qOszUuh4qknuck0MoDabkrirS7vhHKrQwQ71BstTkYZnAU%2BN1hYyoP5gOKCJywhrsCdd%2FmItsBnYPcTQVU99LfMXlGDs%2B2MiWW3zEdbyo2eE3R&X-Amz-Signature=64d5eedfd642cab0e5968b1bfdf5d3b71db72be9394579316d5b13867db19927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







