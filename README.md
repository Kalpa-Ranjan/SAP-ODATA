



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2Y7JZQJ%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T183653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAp85spQE7X4aywHiJej6m4eiiy7YaEHB1M%2Bigct4dMkAiAO%2BTH%2BiUo17qpi8BykIDzOaOQOcKeZBLNX0yhtq1l6XSqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7FeGx5f%2FQg1nF42SKtwDCfI%2F3kFM2OqYCiMzGKTTNL9sETUA1J9Kdm61HuBRtVinbC9Hn2TpSAaN59YIZD%2Bv1xGQtTfBwtxdYWPJEtlbroLJO3XUZvtZXFyJpkGtA%2BFbYUgETrXavpLji%2BxyzxNn2RXVZ57kqts4yUs3LXBy995kWjs2eKh53KlsvhMZ8gnst1u7saCEfgAGBPkPIx8y5ENTD1NIq%2Ff4bpPRzwWcbCfkB0cV3viCncAsUsfL4cShZG6KBSQuR56Ve7%2BM1EYFRcjI3kbdzEOnNVDQxpz4l%2FqnlWNkYuufvL6fbh%2BzZfZXq8SSvaDQ5DST0y5mGGDIXQ%2BYSHV5Jz0inr4Vc8oWRV2B%2B3cB0x3%2BtQSpmlSkgGvFVqu%2FMER7f5FGYzTeeOWL9UDVfcwgkQZRlyDLrOOA5NcLOldsscjEdKqeENv75JcvaFvjeIn%2BFW7dr5aVkKMFhK91%2FsmK5oJ3gNllgVHBGXWlGOLj%2BDUz%2B6nwW9aNeEzXcngqUFKyfNiv%2BmMwhHEzi6wHlZ3yeuEbNp8Nrc2rQzXODcw53D5AkcB2We1k%2BfuTy90T%2B7vI5rotKRWj1abgE51LoV2qfdbyfYdnj5hPqcJBqKTP703m6DB%2Bnh7NayCgroTo%2FSNjeLNXt5swk%2BjJzgY6pgGsE5jXy4kj4VbbB9NxUkyc%2BSOL1Qn4w%2Flq7Yc0J9cSkLcxXFKPwTk%2BPlcaXzoA2gwjR1PJH7VnYRy1xX%2FLUDaGlFEjQMxHHgBXXGh0lMZG8cRuh8pgHRxP50LxdMTybaB%2BbIMDYX1%2B3TSLCOM0xjb5F2pYQoyqxlm9fYuIEyOb8n9k%2BXkeFvxaMcr7dUqQlpQ0mXEpBqK0FtWoaIM9kx7A7fDlNXLV&X-Amz-Signature=2b78cfcd41586f5e0d6f6dab1d22e9815e78e94502203087b4806323ff07a4f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2Y7JZQJ%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T183653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAp85spQE7X4aywHiJej6m4eiiy7YaEHB1M%2Bigct4dMkAiAO%2BTH%2BiUo17qpi8BykIDzOaOQOcKeZBLNX0yhtq1l6XSqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7FeGx5f%2FQg1nF42SKtwDCfI%2F3kFM2OqYCiMzGKTTNL9sETUA1J9Kdm61HuBRtVinbC9Hn2TpSAaN59YIZD%2Bv1xGQtTfBwtxdYWPJEtlbroLJO3XUZvtZXFyJpkGtA%2BFbYUgETrXavpLji%2BxyzxNn2RXVZ57kqts4yUs3LXBy995kWjs2eKh53KlsvhMZ8gnst1u7saCEfgAGBPkPIx8y5ENTD1NIq%2Ff4bpPRzwWcbCfkB0cV3viCncAsUsfL4cShZG6KBSQuR56Ve7%2BM1EYFRcjI3kbdzEOnNVDQxpz4l%2FqnlWNkYuufvL6fbh%2BzZfZXq8SSvaDQ5DST0y5mGGDIXQ%2BYSHV5Jz0inr4Vc8oWRV2B%2B3cB0x3%2BtQSpmlSkgGvFVqu%2FMER7f5FGYzTeeOWL9UDVfcwgkQZRlyDLrOOA5NcLOldsscjEdKqeENv75JcvaFvjeIn%2BFW7dr5aVkKMFhK91%2FsmK5oJ3gNllgVHBGXWlGOLj%2BDUz%2B6nwW9aNeEzXcngqUFKyfNiv%2BmMwhHEzi6wHlZ3yeuEbNp8Nrc2rQzXODcw53D5AkcB2We1k%2BfuTy90T%2B7vI5rotKRWj1abgE51LoV2qfdbyfYdnj5hPqcJBqKTP703m6DB%2Bnh7NayCgroTo%2FSNjeLNXt5swk%2BjJzgY6pgGsE5jXy4kj4VbbB9NxUkyc%2BSOL1Qn4w%2Flq7Yc0J9cSkLcxXFKPwTk%2BPlcaXzoA2gwjR1PJH7VnYRy1xX%2FLUDaGlFEjQMxHHgBXXGh0lMZG8cRuh8pgHRxP50LxdMTybaB%2BbIMDYX1%2B3TSLCOM0xjb5F2pYQoyqxlm9fYuIEyOb8n9k%2BXkeFvxaMcr7dUqQlpQ0mXEpBqK0FtWoaIM9kx7A7fDlNXLV&X-Amz-Signature=c86edfcdd3b10bcf6ad73b76e5eb03707afea98b15c31b5884afdbd4b9626ba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







