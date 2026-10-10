



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXIMZU5H%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T061253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDYkoU3J79CY3zgey2iGswr%2BEuWE5sUrfmCe8i2eZ0mSAiEAqA%2Fa%2BDqUT6JQQxfwqVAsAHwhs%2BJFgYNk4fYKHf1KFnMq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDJzSCMLSV1rz1WnLcyrcA9dfqdp56CdCGrDbG8uXvxZki4TGwkDX8IzEewdtRDxWATLz1ggBFVedEzHKTrDt8cm83P0n9%2F0tDhf1Zu%2Fu7dg9s2%2F3J%2BOKY3746c%2BWcWC%2F2WJzA4Q5jYLn%2FXzCnWpyPO4yYpXD%2BTTgY905N3nkzzvfAlLNtZ2BD2oTtJZlfwJ8a0CBrJv7Tc%2B8bbaXkFRHqy3GS6UK6J89YrNxOklRLT9O5rMNaGCg1s4y5Gvdy0SPUoRxn9OjqzfQC0SCCGMh42T98V4J2rAKxKeVz5HnThOrFbhD3X9AgUHUlCfrokrC%2FYaUWHsBFGJBqs5nJJHZmRKbCbarVo6tmp3iGor1WT9bEvPLYrywP0qr9NOejmxYT5anM9XA1CRicWXSSMEaPVDFZ9eDm3%2F66%2FoZDSuXF8Rl%2BPWO5cjLXtOIK8eOqm3Hk7%2BZHElzWg6NOzEHCWBVdG15z3oExLqED3Qi3kPqd9zAHBxVNZhxMdts4%2FOw8JpKYHfRzf6cF0%2BI3wAGF5KvDqZuliwc14yBEdsTYFUIFz5KoNC7yAcQkuy4W2CEnBMaEP%2BZiiH%2FLBn8rfyLxlPW057OGPovJZ3LwwbiUfYvyIl39QPE63cWJU9Lzj1XCp%2FIvW%2BUNuplIKSvyN5QMJzhptYGOqUBidcPsumX6tzUJreU3%2BCu979v7KZY%2B%2Bg6qEUj%2FcO%2BFXObFBnVkUKqFDOHEsyZj7ILnsiIrJLt%2BVg1f7B%2B6RL%2Fi9TWXfzz2RBaCXzlHUpMkvSRkIFZcV5M2dNOrUurhXLcwx2IpbJ7UoQiuo%2BywEGz%2B43afPzHzmjC597lhFS%2BV2thYLd2xWyxZd4bcxWFMeuOTyXsLKDFJIsqiOU1Nns93DY7b2VE&X-Amz-Signature=92cd53cad3a1b168661a82e6ce4a1ec5d6de451cc4909e16eb1c1e5954f72476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXIMZU5H%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T061253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDYkoU3J79CY3zgey2iGswr%2BEuWE5sUrfmCe8i2eZ0mSAiEAqA%2Fa%2BDqUT6JQQxfwqVAsAHwhs%2BJFgYNk4fYKHf1KFnMq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDJzSCMLSV1rz1WnLcyrcA9dfqdp56CdCGrDbG8uXvxZki4TGwkDX8IzEewdtRDxWATLz1ggBFVedEzHKTrDt8cm83P0n9%2F0tDhf1Zu%2Fu7dg9s2%2F3J%2BOKY3746c%2BWcWC%2F2WJzA4Q5jYLn%2FXzCnWpyPO4yYpXD%2BTTgY905N3nkzzvfAlLNtZ2BD2oTtJZlfwJ8a0CBrJv7Tc%2B8bbaXkFRHqy3GS6UK6J89YrNxOklRLT9O5rMNaGCg1s4y5Gvdy0SPUoRxn9OjqzfQC0SCCGMh42T98V4J2rAKxKeVz5HnThOrFbhD3X9AgUHUlCfrokrC%2FYaUWHsBFGJBqs5nJJHZmRKbCbarVo6tmp3iGor1WT9bEvPLYrywP0qr9NOejmxYT5anM9XA1CRicWXSSMEaPVDFZ9eDm3%2F66%2FoZDSuXF8Rl%2BPWO5cjLXtOIK8eOqm3Hk7%2BZHElzWg6NOzEHCWBVdG15z3oExLqED3Qi3kPqd9zAHBxVNZhxMdts4%2FOw8JpKYHfRzf6cF0%2BI3wAGF5KvDqZuliwc14yBEdsTYFUIFz5KoNC7yAcQkuy4W2CEnBMaEP%2BZiiH%2FLBn8rfyLxlPW057OGPovJZ3LwwbiUfYvyIl39QPE63cWJU9Lzj1XCp%2FIvW%2BUNuplIKSvyN5QMJzhptYGOqUBidcPsumX6tzUJreU3%2BCu979v7KZY%2B%2Bg6qEUj%2FcO%2BFXObFBnVkUKqFDOHEsyZj7ILnsiIrJLt%2BVg1f7B%2B6RL%2Fi9TWXfzz2RBaCXzlHUpMkvSRkIFZcV5M2dNOrUurhXLcwx2IpbJ7UoQiuo%2BywEGz%2B43afPzHzmjC597lhFS%2BV2thYLd2xWyxZd4bcxWFMeuOTyXsLKDFJIsqiOU1Nns93DY7b2VE&X-Amz-Signature=cf66a3aef55cc6868d759fe7cda5cc36c82139c3d0dbb9c8cd0907dec64cf437&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







