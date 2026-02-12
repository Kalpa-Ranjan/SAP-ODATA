



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NNCAWX6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T185628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDAsrvu6tHZUbQm1%2BOkmn4sFbI6dT8Kz58NibmzZ8gtaQIhANF4W%2BM3J%2BmZm7Cgg6JfqkKu07LMBIHLKE4SqMxuID%2BWKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6078Jm3ZR4uQpOGQq3AMJkemL7IbPHFbIPA148ntSYIvT11rDlhHSpKe8OY5ffJ3EGtVNIjz7KeQyvqkJV7EKs4vTeZL6JJyato9i2oNO1JFSGX4oiVyuUPevdFDLOvguJ5Bv1EZ0RUmYgnZ5Ix9RvA%2BFyW5Sa8ygwjE1IfiNQpjN6rJG7zdLgKvwX%2FOFqcFkwe1koRyfhABNTXyyAboqU5rE2p1%2FZLs7Z3JE8%2BAcuz1ZCVzhStpvBboIh2fBCd18hawzyprr7F9tBAnvY%2Bz3lKGhq2c9FV5lFGKN4pD8PuhUaQEutAYkWS0UShMDMKZ33jpn5eVTfbwvJ%2B%2FTz8kclhoS3YAiolrFFHN%2FCuhgWTExsjCt0aMpo%2F2NuEBTmMoE%2FItVAg9bYUc2nTNiTB%2BCy8KKE5CCQPjk32vxZSlruNZ5g6nzH9qe0qX%2BX3VJ0deCGt9va4s%2FXMsnIt1FdTvXVDVmk53WYDROHQmD265oncsq%2FVcG17YNt2iPIRa4n%2FsvMjrS6NyV%2FX%2BOedcxI%2FJ7pLZZnmHVoV5NUq6q%2Bz80CyNwoPFXKGeH%2B58gO4GBsE86JV5rpJpn1BrtvhtHUJZnkpX4LY4m2Itjk7ozQvb6x4lYf4I1eZz0e1V2rQXFlRfJ2CTVJ7HheGpBVTDdqrjMBjqkAZnDNbpZIB6gFXSULrRetgsWOPmYn0IN%2BCrfXgC79RFeN628Eal1TBrw%2FsB6mOOVhv%2FKwo1sfyP7jXMx0GvrxMM6eC8H5oLyh03bWUyflQX3J2xLiTC5MuhhN4wYwgRAOVG5xOnUbzv9rS4SC4Ot97U%2B8p84yHk1g%2FuRfissaGwM0Ni%2FszmIKfnJXUwP2%2BxIeLwfY6M%2FnZGkEzrHKeXEE5P7G6IF&X-Amz-Signature=fb8eadc20f382836845b49670bdca31cbc218cd3d5f98bf8007a41efbc4b3729&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NNCAWX6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T185628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDAsrvu6tHZUbQm1%2BOkmn4sFbI6dT8Kz58NibmzZ8gtaQIhANF4W%2BM3J%2BmZm7Cgg6JfqkKu07LMBIHLKE4SqMxuID%2BWKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6078Jm3ZR4uQpOGQq3AMJkemL7IbPHFbIPA148ntSYIvT11rDlhHSpKe8OY5ffJ3EGtVNIjz7KeQyvqkJV7EKs4vTeZL6JJyato9i2oNO1JFSGX4oiVyuUPevdFDLOvguJ5Bv1EZ0RUmYgnZ5Ix9RvA%2BFyW5Sa8ygwjE1IfiNQpjN6rJG7zdLgKvwX%2FOFqcFkwe1koRyfhABNTXyyAboqU5rE2p1%2FZLs7Z3JE8%2BAcuz1ZCVzhStpvBboIh2fBCd18hawzyprr7F9tBAnvY%2Bz3lKGhq2c9FV5lFGKN4pD8PuhUaQEutAYkWS0UShMDMKZ33jpn5eVTfbwvJ%2B%2FTz8kclhoS3YAiolrFFHN%2FCuhgWTExsjCt0aMpo%2F2NuEBTmMoE%2FItVAg9bYUc2nTNiTB%2BCy8KKE5CCQPjk32vxZSlruNZ5g6nzH9qe0qX%2BX3VJ0deCGt9va4s%2FXMsnIt1FdTvXVDVmk53WYDROHQmD265oncsq%2FVcG17YNt2iPIRa4n%2FsvMjrS6NyV%2FX%2BOedcxI%2FJ7pLZZnmHVoV5NUq6q%2Bz80CyNwoPFXKGeH%2B58gO4GBsE86JV5rpJpn1BrtvhtHUJZnkpX4LY4m2Itjk7ozQvb6x4lYf4I1eZz0e1V2rQXFlRfJ2CTVJ7HheGpBVTDdqrjMBjqkAZnDNbpZIB6gFXSULrRetgsWOPmYn0IN%2BCrfXgC79RFeN628Eal1TBrw%2FsB6mOOVhv%2FKwo1sfyP7jXMx0GvrxMM6eC8H5oLyh03bWUyflQX3J2xLiTC5MuhhN4wYwgRAOVG5xOnUbzv9rS4SC4Ot97U%2B8p84yHk1g%2FuRfissaGwM0Ni%2FszmIKfnJXUwP2%2BxIeLwfY6M%2FnZGkEzrHKeXEE5P7G6IF&X-Amz-Signature=ce5e3ea4e037cc99d01efa4681b8642b6c0664fed0c18f1f423bb2fe4f3014f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







