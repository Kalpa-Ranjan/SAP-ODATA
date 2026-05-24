



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NI32DJO%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T024639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEw6GHJbxqlSKiPPkdX16zrqPaiTSR7b3yMhg%2B9gDt4rAiBWVeKvukMoVxiEj1OyBkMUgLJX2mnGeJPd94vaRvSI5yr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMQ5KkvjVWxn7MnRXpKtwDNMSlDv6Mfc%2BzB8LboKZ9YyZIKnvQ%2BEAst%2FJtQcYQie%2FrbgjeMPV%2Bm7bLVYpy1xwhieBkSWJp1wiXhZeL2JVAipUoJj8%2B7BaD3Xnp8KYClN0BAAOCdNIOG5VDMNBVHev4LCUT1qfAcqwdO5Lgr5e5upbM5enoZab4VXXTCqs9RIPcixE74D8Q1b3FD2lxoZ7h3jbPhKjycz3tmcv9sOi9KUHEAb0FhhDdpl9qhFyMYZqZuqBtInqKU3tD%2F%2Fi6maoIwr6vax%2FHLNpRdYOWFsNVe%2FYnCAv1ZIxw6Ij3KaE%2B%2F32En1VMd4LWJ9gbXDYfQCH0k3iAf9RNgm2jTWwowGvYuNA%2FVdsjhrru2YmuX0VK%2BpdfgQc%2F4BY4jD5xFOH9g3GPLcyEpCQ1cHAMvMcwUcKuGRSr5HUcuNo2AyPEtWFaIcaXcd4bcCGhE4XmGWzTOoy%2FyHD%2BD8YW%2FXDrMV3ME2F6VKwP2yEz3SlnrI8lJPMptZhM4ekgTiWQp6bBsMB8SPz8PmANdZRnqfFApZ2sMw4j8RRhJFFoiRB8cg%2Fkr1CVG18I5HbrGFqon2upHisuZFAYtmeKOrLRVms2oQr%2FLdLphYMiNe4uT0uv7I2tgypSbbiwZaBvbQclUhIrQ8cwhsjJ0AY6pgG1KcHwpzefrBDtq11dDLxgiMyMvjkTiRKG%2FR6qJWXY8SiFj16QneyJxLSatUU4FvvMyVWGYMa0Cf0bgaQC2IteHpHMA%2BoJVYuxUyeHWCN%2B5t%2FNGXrzr5KdTpeU%2FvR8RxjNeMcnVnzlc3q1tecN6d4TvP4FNfFKWTvKv0sChd%2B4tWwbjwXz2OUmOVnklinsJ2W4V111N2AxGxwAa1Tec6hB9a3GeJKa&X-Amz-Signature=088558bc1b8dc225ecf546a82919ea488164bf8fd4a509c0851b110a9ece8f39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NI32DJO%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T024639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEw6GHJbxqlSKiPPkdX16zrqPaiTSR7b3yMhg%2B9gDt4rAiBWVeKvukMoVxiEj1OyBkMUgLJX2mnGeJPd94vaRvSI5yr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMQ5KkvjVWxn7MnRXpKtwDNMSlDv6Mfc%2BzB8LboKZ9YyZIKnvQ%2BEAst%2FJtQcYQie%2FrbgjeMPV%2Bm7bLVYpy1xwhieBkSWJp1wiXhZeL2JVAipUoJj8%2B7BaD3Xnp8KYClN0BAAOCdNIOG5VDMNBVHev4LCUT1qfAcqwdO5Lgr5e5upbM5enoZab4VXXTCqs9RIPcixE74D8Q1b3FD2lxoZ7h3jbPhKjycz3tmcv9sOi9KUHEAb0FhhDdpl9qhFyMYZqZuqBtInqKU3tD%2F%2Fi6maoIwr6vax%2FHLNpRdYOWFsNVe%2FYnCAv1ZIxw6Ij3KaE%2B%2F32En1VMd4LWJ9gbXDYfQCH0k3iAf9RNgm2jTWwowGvYuNA%2FVdsjhrru2YmuX0VK%2BpdfgQc%2F4BY4jD5xFOH9g3GPLcyEpCQ1cHAMvMcwUcKuGRSr5HUcuNo2AyPEtWFaIcaXcd4bcCGhE4XmGWzTOoy%2FyHD%2BD8YW%2FXDrMV3ME2F6VKwP2yEz3SlnrI8lJPMptZhM4ekgTiWQp6bBsMB8SPz8PmANdZRnqfFApZ2sMw4j8RRhJFFoiRB8cg%2Fkr1CVG18I5HbrGFqon2upHisuZFAYtmeKOrLRVms2oQr%2FLdLphYMiNe4uT0uv7I2tgypSbbiwZaBvbQclUhIrQ8cwhsjJ0AY6pgG1KcHwpzefrBDtq11dDLxgiMyMvjkTiRKG%2FR6qJWXY8SiFj16QneyJxLSatUU4FvvMyVWGYMa0Cf0bgaQC2IteHpHMA%2BoJVYuxUyeHWCN%2B5t%2FNGXrzr5KdTpeU%2FvR8RxjNeMcnVnzlc3q1tecN6d4TvP4FNfFKWTvKv0sChd%2B4tWwbjwXz2OUmOVnklinsJ2W4V111N2AxGxwAa1Tec6hB9a3GeJKa&X-Amz-Signature=e7c12a8e0a6dff86395b7a1060c95bcd8fcd1d51be40959d5ff8d198da59b760&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







