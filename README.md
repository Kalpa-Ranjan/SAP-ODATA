



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URF6XBUX%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T011728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMdhW%2BjG54tI4saGr6r6VYak%2F4Lzy0ygj8zmqSzL%2F%2FPAiEA1vdXmSRxv8hD7JsbjJ5%2FckIXMzgESjBT6LmUyqCZzlwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDNyvOui0zCYpmXl3pircAzW4PgOhv6fBQ3tNupXOq7raOnwFlICDaTTIoE3aPpyH4%2BI%2FCSWYQMlpxrROcPq4jG84MPbbor3gSYyVjzLoxLogZlGjgKqy9CvPHQAXhkn5cC%2BqXfesA66GAx628zTYRz2wiPtMnG6l9hsDdpQM69yVk8D%2FZEIqp5c10QdnzqTA0mfqBXGxzV87kn6%2BNmg0v1t31%2BVDX4PEHYAH5Qhapw9UuPYPqsuQyPWIQ6rZPs3p0LLhv6jvEFVQsk1381vZLiImi8mQJiNSxZ0unOgtGYc5Vn0bcNcKy2%2FS7OVlaSYDC91eefZoWM9GqIvEfjLdp49EPN4249TU7a3RnMry9EX6FNZCGdOI4ki1dAAJayUm20UPer9WaGy0%2BtxwS4QYsG0sLqEcY2IOhGSmjnIfXR3sitVK16pS3zLdgaw2E5njHPYlxN90vJLdrG4qucT8Wpxzw9Wq5zUZ7lg4c7YwhbARO3YOZyKgLSl%2B1VVSlBsGzV34r23QGNl7SJj6crgsTFNdtm5JjSA18UPBSOTIiSmSCk2MhAvK7BWWOHJrD5GRHb5SgumHdrZg0wTAd5M7MPTcFCnwBqzuWXZA2WWnpUThuWP1YCiw%2FQ5p8xtBpO7y4Zx8edWSBhy1sejIMKPLgsoGOqUBEYCbiF0dlzorYwxgkz1soUmudx%2BTllp4R%2FDR2v%2FlHTTH03yZSPfeyBaqRSQ7ioBU6JVdVGAGn2YnBhObb0U%2BBohNvKjmlu8IfZKi7u1hpACOxr8%2F4mPMMdXgzump5nqh0%2B27kZcxKQ3pMUgELYwzHaeuA0WFtP4kPGWYzLyqeu3yWcUfj20aFmcGZb%2F%2BfUf8PH6VB0kipyl8Pmkwf9ZiMxBs6S%2F1&X-Amz-Signature=453cdeed700659d502ad601e61e5d40d20d62ffec89b3063316d620b76c71242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URF6XBUX%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T011728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMdhW%2BjG54tI4saGr6r6VYak%2F4Lzy0ygj8zmqSzL%2F%2FPAiEA1vdXmSRxv8hD7JsbjJ5%2FckIXMzgESjBT6LmUyqCZzlwq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDNyvOui0zCYpmXl3pircAzW4PgOhv6fBQ3tNupXOq7raOnwFlICDaTTIoE3aPpyH4%2BI%2FCSWYQMlpxrROcPq4jG84MPbbor3gSYyVjzLoxLogZlGjgKqy9CvPHQAXhkn5cC%2BqXfesA66GAx628zTYRz2wiPtMnG6l9hsDdpQM69yVk8D%2FZEIqp5c10QdnzqTA0mfqBXGxzV87kn6%2BNmg0v1t31%2BVDX4PEHYAH5Qhapw9UuPYPqsuQyPWIQ6rZPs3p0LLhv6jvEFVQsk1381vZLiImi8mQJiNSxZ0unOgtGYc5Vn0bcNcKy2%2FS7OVlaSYDC91eefZoWM9GqIvEfjLdp49EPN4249TU7a3RnMry9EX6FNZCGdOI4ki1dAAJayUm20UPer9WaGy0%2BtxwS4QYsG0sLqEcY2IOhGSmjnIfXR3sitVK16pS3zLdgaw2E5njHPYlxN90vJLdrG4qucT8Wpxzw9Wq5zUZ7lg4c7YwhbARO3YOZyKgLSl%2B1VVSlBsGzV34r23QGNl7SJj6crgsTFNdtm5JjSA18UPBSOTIiSmSCk2MhAvK7BWWOHJrD5GRHb5SgumHdrZg0wTAd5M7MPTcFCnwBqzuWXZA2WWnpUThuWP1YCiw%2FQ5p8xtBpO7y4Zx8edWSBhy1sejIMKPLgsoGOqUBEYCbiF0dlzorYwxgkz1soUmudx%2BTllp4R%2FDR2v%2FlHTTH03yZSPfeyBaqRSQ7ioBU6JVdVGAGn2YnBhObb0U%2BBohNvKjmlu8IfZKi7u1hpACOxr8%2F4mPMMdXgzump5nqh0%2B27kZcxKQ3pMUgELYwzHaeuA0WFtP4kPGWYzLyqeu3yWcUfj20aFmcGZb%2F%2BfUf8PH6VB0kipyl8Pmkwf9ZiMxBs6S%2F1&X-Amz-Signature=0e0329d98488f7d4b9200210fd946c0e41fd338fb82e0c5ae27e433f504c20bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







