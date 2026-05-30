



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA2GCP3%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T023836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDo5%2BTQyKwrvlx9tnvI%2FMvPbdnMqkahRHhDTMuk%2Ba92FAIhALcnDCnTguLIanq6NgXOtZ4BioPkGUSOIQGye282QIHPKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwBVS4oI7C97XOILO0q3AMovFO7t5%2Fef1fHwi0nTghIZ8xAO1wR1VmjpS0Voo1OwCNCH4fz650vhZn0Bo%2BCTH%2BKR7c4LzCwr0l5hrZ78oTuCwHpMvmZ6eOFvRX65AzBBJPdRvILliqxZFDAYGAVJl54cKnLE06I9GN7e2RoaVnVEBwLdhlvFWNZ%2B%2BzrsRtnCHbxlL2Un5kUdNQyayn%2FszAaojo5QwVqeCXQ9J5HL3%2FCLFILeROuRxQUHyI6nO8Y4W501gGn9J%2BHZMN%2FuHdFvJm07hY%2FkjYZnYzglerpVj1%2BdgH4UAggOCHRGD30TLTYvGX2PUKUOQ%2BljVyL0HGHDqhHZHyQF9e3fZ9znDKYG0hYTGCUc05LNGAJmEdpLXCyOiEiDUP7T7eslzFH4nJVYslq%2BOF0tMN53XMbMBEhp947YYoGfrRgizxAg%2BJbiiL%2FbyzNV9JiRVSUkzr7QxV6ekGrKJGl0aJvp%2F7Sp1Eg%2B9SOiRZUHes8fhGhOQS494DLJVd0YsluYwiIYt%2BaIwnYRnwiD19IUY3W6ERyRo07ievIZWD6gd0sn7PF0ki0eZmmM2TXwbqBiMeM31Qx9PH6uCRQyt38vdcZxZcVpGRpqzIvOsW50wazNCMGWTXw7gYhgKX3CtSsuNIo9eGUeTCC%2FOjQBjqkAShfBonkhWVvXzgOf%2ByargPjmP9J1UmMnlQgXnKOQoPeAdgPuYgIEqxJRa6ymKIKMPTSmW8PpNzZAV98NPRoOx4ln3zaDWt5sNQXRkIqbSUfU%2FHyZUY6FqCy1kwFjTQzdU4dvT2WjpXkJg2VdKg2WWXA0lkgMO6Q8OYKzvHGOYUxb1NzFqPvPquZyS2gwRl0lhKSGg8JA9Hv%2BWfu0JWuCd%2FEP9Nv&X-Amz-Signature=ead7d4a10d80eb9141fa79428d6317628fceab1b7b31a818517a99c784ba42f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA2GCP3%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T023837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDo5%2BTQyKwrvlx9tnvI%2FMvPbdnMqkahRHhDTMuk%2Ba92FAIhALcnDCnTguLIanq6NgXOtZ4BioPkGUSOIQGye282QIHPKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwBVS4oI7C97XOILO0q3AMovFO7t5%2Fef1fHwi0nTghIZ8xAO1wR1VmjpS0Voo1OwCNCH4fz650vhZn0Bo%2BCTH%2BKR7c4LzCwr0l5hrZ78oTuCwHpMvmZ6eOFvRX65AzBBJPdRvILliqxZFDAYGAVJl54cKnLE06I9GN7e2RoaVnVEBwLdhlvFWNZ%2B%2BzrsRtnCHbxlL2Un5kUdNQyayn%2FszAaojo5QwVqeCXQ9J5HL3%2FCLFILeROuRxQUHyI6nO8Y4W501gGn9J%2BHZMN%2FuHdFvJm07hY%2FkjYZnYzglerpVj1%2BdgH4UAggOCHRGD30TLTYvGX2PUKUOQ%2BljVyL0HGHDqhHZHyQF9e3fZ9znDKYG0hYTGCUc05LNGAJmEdpLXCyOiEiDUP7T7eslzFH4nJVYslq%2BOF0tMN53XMbMBEhp947YYoGfrRgizxAg%2BJbiiL%2FbyzNV9JiRVSUkzr7QxV6ekGrKJGl0aJvp%2F7Sp1Eg%2B9SOiRZUHes8fhGhOQS494DLJVd0YsluYwiIYt%2BaIwnYRnwiD19IUY3W6ERyRo07ievIZWD6gd0sn7PF0ki0eZmmM2TXwbqBiMeM31Qx9PH6uCRQyt38vdcZxZcVpGRpqzIvOsW50wazNCMGWTXw7gYhgKX3CtSsuNIo9eGUeTCC%2FOjQBjqkAShfBonkhWVvXzgOf%2ByargPjmP9J1UmMnlQgXnKOQoPeAdgPuYgIEqxJRa6ymKIKMPTSmW8PpNzZAV98NPRoOx4ln3zaDWt5sNQXRkIqbSUfU%2FHyZUY6FqCy1kwFjTQzdU4dvT2WjpXkJg2VdKg2WWXA0lkgMO6Q8OYKzvHGOYUxb1NzFqPvPquZyS2gwRl0lhKSGg8JA9Hv%2BWfu0JWuCd%2FEP9Nv&X-Amz-Signature=bd9daa51c6dcd0c3d46e8eeb9edf1d6b3907a21baeb52445a2c75c8a03ebbc15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







