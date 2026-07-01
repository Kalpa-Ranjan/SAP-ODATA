



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4IOJMOD%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T142338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDha%2BsD1olDv10iCb%2BpnOm8rGUIUHtFBQtnJ%2BAJrj%2FQVQIhAMZpYvEIQC4SGN7gBgY9IPsGsfC%2FPqk038m5V%2FRMarV%2FKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfebjtJEcGh86kzGsq3ANUBl2m23g%2ByQk%2FC6bXmLlY3As%2FCgQAx8CzweGj4OWF7mYYV2LVtAqiWe7YsyHPHbJ6f0XTs0drH9NXHqEnntwD9lH5AsOci%2F%2B6mmAHN%2BVan90pIyHHpkEDa78Gx1Jeb%2BCGaJbH5CVa302m4RC5suxagR6C2ebxM566jIGHvjcDF7KfkQM5a7W84tM4wNvCrEeydzNbQSJfRlx6hXmnXppkRWkKVA%2FoIKi91VCY%2BJI7DSdaCUtNWu1fJ2E0dEbcm0IAnS5Kfyc9geISf03E7Bf9MTZV5UoVbVDxdV3ajwV4JF2FGbAkijj9DTlMLL%2BZRixKyqfm9sw2hZK4bIDrgekcxR4Nra3STdXSwzxtRUzOcpWtK7XPTxyn7K%2BqC7XaDWaaoEpxMUqT2Xid9FclpMoaTU%2FETRkLxJ8rLhxwrHHFoL9otqgqmp4d2pVQvxnZyiQQUpSvgWNbFOQ%2BORUHqN4OoY6Y0ZnoqRn9KVnbAxpwWNUXmHzmjfKpE%2B2O3%2FiquGakU3bLNC%2FW9nZgARd3XCWPqYU4ImtYeoj3%2FglFHC8B2ni1GPmX9MesfVRR2uJCZmGFRozgbl9GcPVPJNOe4gj7vgweQXAx9frLYFfVWMgEVOILO2loXF%2BQdUZWYTDNr5PSBjqkAbaUd9mDmwAoGGThxKaZ2TQNsHwHFbKog%2F7aA2lVQpps3nbXwT7sFORKnknOVfTybQgsrRxygU0WkfOM8whq7MpBx%2BYD0MsuoBcKBgBFSiB5jeR2m%2Fm4AQ%2FSNOcSkVh%2BGYOilC0ee24WFGCvLqbnKAUR5lLEm%2BCwLaZ5h151tDPpkPqpnbZyFuhbUZYsieufqBiq285QiyuVqUzeeuXnKSB78Je4&X-Amz-Signature=bcd8761cd51e3089742faf6942935e497c2f21807e42575ccd9ad8ba6b7b6265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4IOJMOD%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T142338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDha%2BsD1olDv10iCb%2BpnOm8rGUIUHtFBQtnJ%2BAJrj%2FQVQIhAMZpYvEIQC4SGN7gBgY9IPsGsfC%2FPqk038m5V%2FRMarV%2FKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfebjtJEcGh86kzGsq3ANUBl2m23g%2ByQk%2FC6bXmLlY3As%2FCgQAx8CzweGj4OWF7mYYV2LVtAqiWe7YsyHPHbJ6f0XTs0drH9NXHqEnntwD9lH5AsOci%2F%2B6mmAHN%2BVan90pIyHHpkEDa78Gx1Jeb%2BCGaJbH5CVa302m4RC5suxagR6C2ebxM566jIGHvjcDF7KfkQM5a7W84tM4wNvCrEeydzNbQSJfRlx6hXmnXppkRWkKVA%2FoIKi91VCY%2BJI7DSdaCUtNWu1fJ2E0dEbcm0IAnS5Kfyc9geISf03E7Bf9MTZV5UoVbVDxdV3ajwV4JF2FGbAkijj9DTlMLL%2BZRixKyqfm9sw2hZK4bIDrgekcxR4Nra3STdXSwzxtRUzOcpWtK7XPTxyn7K%2BqC7XaDWaaoEpxMUqT2Xid9FclpMoaTU%2FETRkLxJ8rLhxwrHHFoL9otqgqmp4d2pVQvxnZyiQQUpSvgWNbFOQ%2BORUHqN4OoY6Y0ZnoqRn9KVnbAxpwWNUXmHzmjfKpE%2B2O3%2FiquGakU3bLNC%2FW9nZgARd3XCWPqYU4ImtYeoj3%2FglFHC8B2ni1GPmX9MesfVRR2uJCZmGFRozgbl9GcPVPJNOe4gj7vgweQXAx9frLYFfVWMgEVOILO2loXF%2BQdUZWYTDNr5PSBjqkAbaUd9mDmwAoGGThxKaZ2TQNsHwHFbKog%2F7aA2lVQpps3nbXwT7sFORKnknOVfTybQgsrRxygU0WkfOM8whq7MpBx%2BYD0MsuoBcKBgBFSiB5jeR2m%2Fm4AQ%2FSNOcSkVh%2BGYOilC0ee24WFGCvLqbnKAUR5lLEm%2BCwLaZ5h151tDPpkPqpnbZyFuhbUZYsieufqBiq285QiyuVqUzeeuXnKSB78Je4&X-Amz-Signature=7d55410fcaea7ac2b996d18265d5625ea84e8474f0aca00d3c00085316b4bcb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







