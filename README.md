



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DJGR3F7%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T060801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDceq0D48PZUlHnilxQEgnE8kts%2F6pBDRyypgYnhaQVDwIhAK8s0KA%2Bc6aWxqjhhnKi3XV0BP2s7W9wO%2B1RgbK7ieXlKv8DCEsQABoMNjM3NDIzMTgzODA1Igw4f8eIWHClvS5gXI8q3ANjqn66lTzZFwmC5i%2Fso8gbzNHT05I9%2BxzNlNltE5XjS34bXXlK64zCK16BYMP1AcUQvN5SXvx7I1MwzkbpSn06NZ%2By%2FX9%2FwdR263hVBfAGvlx1Iq7wFQlirvDvUvFTvGjq9qzSgGVo0Ja9zpDx0QCSJGyMQ7tTR1F57o6%2BSzqSAc7INDK%2Fz3uU7z5hSgkSXVH7%2FMsMPgy7W2ck6bBUlrJEu42z1H9aNNmVsVE2U%2BgmzC%2FEEldsg%2FVmSxe9J2h6D3H7ualUPOldNyrG%2FSa7iDw3GepZHkayLI6PExP%2Flrl1l1ljbA5Litq7Dq6KdTZA4dLwG2IHOjfKTavR5bS2Xt0Fl%2Bbsk8%2ByCMiyGIqB2c4TF9BsqXv7zN3A37H%2B543hQvKEht5xOdqNsRMhGrJ7dXeiqL%2FAGT9jYmejDWV87T9nLNuIHCBXLd8haNV8z19bqh3yli62Uj6GuAkZrsEk%2B6SBq2opVMRb8WNk4T0US%2FIO6fV%2B0YWT3G6hx9XZSxl3ZoinRu0wEgxk4SPGfEblhvoSrMWFWzWi8Lxlyzl4pRBqHjOlitvYyEduw93fj2u80y0HPPn1oW9KqAku6uoaE%2Fh7NsKo89Bjfe4S4KMDB3bGtO%2B1W3tBvWFvqOHp5TDEnM%2FXBjqkARitLEFmBLQ%2FQdnWuSXSy0tBAIuiAutvf%2FFjYGi8FVRds%2B0FbYzNI18tiy5Mo916r14956H4M3NeEVNAS2v6BGsgvJpp2Gwn7x6rPzSTYYHd5vcbmMBRxXdZBdwe6i%2FoGTrk%2F7ck7OOREJac6EzSZj9JrIgPYtc0raDzu9jPKGHuUNaEjaB%2FHE0WcpDNSk%2FbqCPGAZSnZZFpsx%2FPnMsOlU04APUr&X-Amz-Signature=07e46a5c4cf653dffc59c5febc4b2d64e71174f58116cc680e629aa1783e83d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DJGR3F7%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T060802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDceq0D48PZUlHnilxQEgnE8kts%2F6pBDRyypgYnhaQVDwIhAK8s0KA%2Bc6aWxqjhhnKi3XV0BP2s7W9wO%2B1RgbK7ieXlKv8DCEsQABoMNjM3NDIzMTgzODA1Igw4f8eIWHClvS5gXI8q3ANjqn66lTzZFwmC5i%2Fso8gbzNHT05I9%2BxzNlNltE5XjS34bXXlK64zCK16BYMP1AcUQvN5SXvx7I1MwzkbpSn06NZ%2By%2FX9%2FwdR263hVBfAGvlx1Iq7wFQlirvDvUvFTvGjq9qzSgGVo0Ja9zpDx0QCSJGyMQ7tTR1F57o6%2BSzqSAc7INDK%2Fz3uU7z5hSgkSXVH7%2FMsMPgy7W2ck6bBUlrJEu42z1H9aNNmVsVE2U%2BgmzC%2FEEldsg%2FVmSxe9J2h6D3H7ualUPOldNyrG%2FSa7iDw3GepZHkayLI6PExP%2Flrl1l1ljbA5Litq7Dq6KdTZA4dLwG2IHOjfKTavR5bS2Xt0Fl%2Bbsk8%2ByCMiyGIqB2c4TF9BsqXv7zN3A37H%2B543hQvKEht5xOdqNsRMhGrJ7dXeiqL%2FAGT9jYmejDWV87T9nLNuIHCBXLd8haNV8z19bqh3yli62Uj6GuAkZrsEk%2B6SBq2opVMRb8WNk4T0US%2FIO6fV%2B0YWT3G6hx9XZSxl3ZoinRu0wEgxk4SPGfEblhvoSrMWFWzWi8Lxlyzl4pRBqHjOlitvYyEduw93fj2u80y0HPPn1oW9KqAku6uoaE%2Fh7NsKo89Bjfe4S4KMDB3bGtO%2B1W3tBvWFvqOHp5TDEnM%2FXBjqkARitLEFmBLQ%2FQdnWuSXSy0tBAIuiAutvf%2FFjYGi8FVRds%2B0FbYzNI18tiy5Mo916r14956H4M3NeEVNAS2v6BGsgvJpp2Gwn7x6rPzSTYYHd5vcbmMBRxXdZBdwe6i%2FoGTrk%2F7ck7OOREJac6EzSZj9JrIgPYtc0raDzu9jPKGHuUNaEjaB%2FHE0WcpDNSk%2FbqCPGAZSnZZFpsx%2FPnMsOlU04APUr&X-Amz-Signature=316d6d55227ca8947f697b3aa9ae90ea3daa2752aa07002a8784451d67368402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







