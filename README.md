



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVIFMRPO%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T135713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZQBc0TCpjomlqxVaGY66ZSuOUpQiIhO9k9gO%2FN%2Fnn5AiA8VuYwMhlDE2QAiMkEwMwaVji3FpeWIM1UKSUOuSuISir%2FAwheEAAaDDYzNzQyMzE4MzgwNSIM5wwTx2N8xAU%2BHIb4KtwDbpxKF2GclqTV0d3ERT4QxkLwbCTv42inhfp2kTXHAM7bdw3vHu7HA1GNtu4fSogbG%2FA%2BozNKTo8i4phIr9zime16aQ9R2XtNd0voGD%2FTeJVXA4gD3fNROyxAsSw8pm%2FjjS3iMInfkCUqBxu0Pej3MYkbFzuSEaY5N5FDjtmuWTNJd4QufeTlvh61wKJEwh7MGIlt1mYIIuXldJZybC97XNSY2ZaTMYFdOuLS5ndctw%2FWIMBdaaH9ARpP%2FDWj7e2R4bT15Dg1MvMNDiFOa1SpK0iZDk8Zq%2BvfQhZ8b6CakehZKjFVUTCVImXx9P0K7tOazwXjrw7XTsCEh9f%2BbL%2BJ3Nt8fLHYyQrenzh8FdXnKeOuSPJqAyWGHk%2B95G8PohJwZC%2BTglPY5A%2Fst0t8%2BZcPNNqMfMjJE1GRoE3CEP8R1LxCZMalCCHl4VgmAniuDlumluD%2BFZuOPs3gilXn2pPa4zyU%2FsU5v9V39FwaJlF9ja%2FqvBgxTzONSVPx1TeOg%2Ftt62ULT%2FMTsTOwXgVUVydcVvizRtLCCjs%2Fh22e1TCLeZrVEn4c%2FzB4GQHtRHTJi0vR6a20YcdsNOzFQRRLFi8KSFpqo2ElnXQ0EoIyiCUl9pFbDIHcjEH66VmqwVswm4CX0AY6pgHYs7R7cI7nO2MF%2FaJtDqeqJK15NE9IC7bneg6faSMxs5EACRXF3%2B2nydGTWLH4sTaugOR64%2BE5hb1IdMPl1ARbK4XgdsxBUZLjXVurFk7rOr4wjUkJxhwtBk3StpyaIp85lTfqkcg1ucKhgWqCYuJYz0Ax%2BzvIerzXkhLeVW1Etfbu90Eh9LD1BhYNqmDe%2FE3sF1a%2FoCIwFVFFVo0pJmwjI4oLMmk8&X-Amz-Signature=2bbfd8945fc78cf2cc8f2c556087da5ad0efc188ca16441a4302948c378cfef6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVIFMRPO%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T135713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDZQBc0TCpjomlqxVaGY66ZSuOUpQiIhO9k9gO%2FN%2Fnn5AiA8VuYwMhlDE2QAiMkEwMwaVji3FpeWIM1UKSUOuSuISir%2FAwheEAAaDDYzNzQyMzE4MzgwNSIM5wwTx2N8xAU%2BHIb4KtwDbpxKF2GclqTV0d3ERT4QxkLwbCTv42inhfp2kTXHAM7bdw3vHu7HA1GNtu4fSogbG%2FA%2BozNKTo8i4phIr9zime16aQ9R2XtNd0voGD%2FTeJVXA4gD3fNROyxAsSw8pm%2FjjS3iMInfkCUqBxu0Pej3MYkbFzuSEaY5N5FDjtmuWTNJd4QufeTlvh61wKJEwh7MGIlt1mYIIuXldJZybC97XNSY2ZaTMYFdOuLS5ndctw%2FWIMBdaaH9ARpP%2FDWj7e2R4bT15Dg1MvMNDiFOa1SpK0iZDk8Zq%2BvfQhZ8b6CakehZKjFVUTCVImXx9P0K7tOazwXjrw7XTsCEh9f%2BbL%2BJ3Nt8fLHYyQrenzh8FdXnKeOuSPJqAyWGHk%2B95G8PohJwZC%2BTglPY5A%2Fst0t8%2BZcPNNqMfMjJE1GRoE3CEP8R1LxCZMalCCHl4VgmAniuDlumluD%2BFZuOPs3gilXn2pPa4zyU%2FsU5v9V39FwaJlF9ja%2FqvBgxTzONSVPx1TeOg%2Ftt62ULT%2FMTsTOwXgVUVydcVvizRtLCCjs%2Fh22e1TCLeZrVEn4c%2FzB4GQHtRHTJi0vR6a20YcdsNOzFQRRLFi8KSFpqo2ElnXQ0EoIyiCUl9pFbDIHcjEH66VmqwVswm4CX0AY6pgHYs7R7cI7nO2MF%2FaJtDqeqJK15NE9IC7bneg6faSMxs5EACRXF3%2B2nydGTWLH4sTaugOR64%2BE5hb1IdMPl1ARbK4XgdsxBUZLjXVurFk7rOr4wjUkJxhwtBk3StpyaIp85lTfqkcg1ucKhgWqCYuJYz0Ax%2BzvIerzXkhLeVW1Etfbu90Eh9LD1BhYNqmDe%2FE3sF1a%2FoCIwFVFFVo0pJmwjI4oLMmk8&X-Amz-Signature=97564d609ec4932cfaf2f5c1db4d56d9c5813e0ce1d2657fa2464acf308e1a7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







