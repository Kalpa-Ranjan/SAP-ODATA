



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFLCQP6E%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T180849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOTkevj925H4vHrAHRWzz0uz45BtUo10yiUYNPVc8grAIhALfDzislU2qhn%2FgueWUrF1eIdPC%2BGWHzwBit7nDSk7hyKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkrWIPpad%2B%2BFbsUmEq3APP6SLT8RPJGC4ULUhdnw2TJrXll3uz8fISv65PDaqW48NV9ToSnpFV0nSj4NiCdxLPgD4YOiv6ikN6vAOc3ElLKJq2kmJsX5zOio5nKuBZv16cklXDRSFoZMjnVfy6142oC72jdFYu4phkKWmbtqVG9Lpsa%2B8NB2Ysc1w4BX%2FtJa9tcBwJT4SLa%2FIGJiZXU%2B2gpDkvvMPCJBwy3GhfzlWUuQuC50h5GGfQAls8exd2uYoMkbhvjt%2BNgwEJn7OWIhRlqP9cGvQ04B0dTPCbbRNCginMwHSkGsKTHSEYfI6e5OxRltIVBGVW5QwiMgDSeV%2BURIwblhSPH0%2BjKVUUpjoOzxUA13if7jQhvHJngMDenkNze3zcm4hCKSzN9dgEeyz22jFTHygZucTZTAbPAlyCcQDkgTSwzwPFNOtclOgxKkcu7yT7d%2F3PJka3S5npainIgT%2B%2B7gKyb6Tw6rdgsnkf%2FMeNZrVCLlk6ZDpoFf5P4%2FUv0ZjSYlPIBdOHxvMgnMzXjozzNqqxZG%2BWIdsQJWIErH0oyfN4xmBAe8EmEBq1Yz22bA%2FDLa%2BI37tR5t3uADNkxa%2Bu1XTVrzITUGviT7PC4JaHMINDZHzCEqIMWfXor44hxf%2BEcJQNw%2Fo9PTDJme7WBjqkAdWjbFSWDbIFkfge3RcrMhSNhyf0%2Bi4pkJAajrNQnfKa3%2BqfGQMDNkVDBj9SYSWsMRGGFk3g4uS4CSvSSwiL196jnZm98Vv2bbOP%2Fh0ep2BZjv3XA5GYjdvIiDfED7JV5lqj41vIMB7qNZswGh%2BW2Fn5b5j3vhFc7PL2JyDoMTMorFpyP4TXr0j1TyUN2%2BFicH88GFEa7Xfn%2BBJDEg1T3B6xucmW&X-Amz-Signature=446810f21c6a3e04c7b3a5060b0df6a020bafa1db5a7be5fde71479678c0d86c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFLCQP6E%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T180849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOTkevj925H4vHrAHRWzz0uz45BtUo10yiUYNPVc8grAIhALfDzislU2qhn%2FgueWUrF1eIdPC%2BGWHzwBit7nDSk7hyKogECJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkrWIPpad%2B%2BFbsUmEq3APP6SLT8RPJGC4ULUhdnw2TJrXll3uz8fISv65PDaqW48NV9ToSnpFV0nSj4NiCdxLPgD4YOiv6ikN6vAOc3ElLKJq2kmJsX5zOio5nKuBZv16cklXDRSFoZMjnVfy6142oC72jdFYu4phkKWmbtqVG9Lpsa%2B8NB2Ysc1w4BX%2FtJa9tcBwJT4SLa%2FIGJiZXU%2B2gpDkvvMPCJBwy3GhfzlWUuQuC50h5GGfQAls8exd2uYoMkbhvjt%2BNgwEJn7OWIhRlqP9cGvQ04B0dTPCbbRNCginMwHSkGsKTHSEYfI6e5OxRltIVBGVW5QwiMgDSeV%2BURIwblhSPH0%2BjKVUUpjoOzxUA13if7jQhvHJngMDenkNze3zcm4hCKSzN9dgEeyz22jFTHygZucTZTAbPAlyCcQDkgTSwzwPFNOtclOgxKkcu7yT7d%2F3PJka3S5npainIgT%2B%2B7gKyb6Tw6rdgsnkf%2FMeNZrVCLlk6ZDpoFf5P4%2FUv0ZjSYlPIBdOHxvMgnMzXjozzNqqxZG%2BWIdsQJWIErH0oyfN4xmBAe8EmEBq1Yz22bA%2FDLa%2BI37tR5t3uADNkxa%2Bu1XTVrzITUGviT7PC4JaHMINDZHzCEqIMWfXor44hxf%2BEcJQNw%2Fo9PTDJme7WBjqkAdWjbFSWDbIFkfge3RcrMhSNhyf0%2Bi4pkJAajrNQnfKa3%2BqfGQMDNkVDBj9SYSWsMRGGFk3g4uS4CSvSSwiL196jnZm98Vv2bbOP%2Fh0ep2BZjv3XA5GYjdvIiDfED7JV5lqj41vIMB7qNZswGh%2BW2Fn5b5j3vhFc7PL2JyDoMTMorFpyP4TXr0j1TyUN2%2BFicH88GFEa7Xfn%2BBJDEg1T3B6xucmW&X-Amz-Signature=466c0a7bbed39afe6c766d944483766a2f0ba9bdecc0d109fef0da4401b14a09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







