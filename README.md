



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIFEEKAI%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T182738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7EbWyZ3rVwNT5araTMQZoSvDpM02Sz1Xvdk%2FFRsQJZQIhAM1569ZHZMAXl9YqW6jCDGnpXP0VAsrQ2jGBUyCXzDy3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUSq4q4jnF%2Bqi1A9Yq3AOBn9eBeEtxORl3aFFFYM7Eb9l0TvQX4M%2FVeEGTVMuAi5%2FPhuX32pMUPJ6%2FZbJGaqo3%2F5FXWGwQjQF6yNpmU1tPT9mwiXgsc4XQcfTEQuaUF80ea2dMmBfiexWc%2FGvKvSUr7ns%2BCoOQwFfSmcJuWlp5NsdGF7Aw6Bvr1op4c5k%2BWO34uAiEnVLAvI45KXCN5an4RUDi52gCpqzR91llGYuuI%2BVSEKkIq0PzqbvssPATkv2ZbgKW16NFQPAW1VUIKT0HweY8cXcJPwk0rz4T9RrnCQtQszmUubtKsmyrBC4OJsRa7Ko3rIed08ZE6j%2BWn4ySo%2B3NeSusUuQTGn7KpNzFipkJMq7bopWwS4B2Ai%2F0oFx4O9wAzdP3eI6yWEwhrZKmchccC%2FvKvr8Ui47Bl6ECFNMroZrSpuk8FUvm6rkP1Z9b7fDTWWhLHuvffv8rBIpPjPmjGw%2B6wL3ZL0KdPQ9Oe0yFXOrrdY%2FAUhtmwE61%2BHOgaBHN7Hzdrth%2FLNY6NCsYQu%2Br2pefctP970HjwlBv5IqDmTue4x%2BzaECDD2DldUPuW34RZxaK%2FaQ7Ii4WuaKCpz8sH9RLYbMuzS0WeXPbkeP3zF1vb%2BC8O%2FmEvJJw7CF%2B%2Br%2FYmTbROCvBxDDT1ubMBjqkAV%2BNb5uNorG5puvT7jm%2FQ0y9JcYdEbKLIHuF72JmToUcWcrPdnpK2lfIW3EABzOs4Sp%2F673tEK0erKDm%2FdwoJqXdQivAq%2BA9UEE34m%2B2%2FJw5ibvNe4N1QeGjii3WjY%2FcuUn%2BknuKFwT4xlENxd7GNfdhGEKHMMtG5UvlZb34RNYB9nLz6opH0VNAhp2CdFyhOPYBL2Z8y84h%2B%2BgHPUxqZBMlth%2BY&X-Amz-Signature=e43e9db0b476d6bf6279ec888eb554c5bc114869a3dd93fea42e5af6a5f0cf55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIFEEKAI%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T182738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7EbWyZ3rVwNT5araTMQZoSvDpM02Sz1Xvdk%2FFRsQJZQIhAM1569ZHZMAXl9YqW6jCDGnpXP0VAsrQ2jGBUyCXzDy3KogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUSq4q4jnF%2Bqi1A9Yq3AOBn9eBeEtxORl3aFFFYM7Eb9l0TvQX4M%2FVeEGTVMuAi5%2FPhuX32pMUPJ6%2FZbJGaqo3%2F5FXWGwQjQF6yNpmU1tPT9mwiXgsc4XQcfTEQuaUF80ea2dMmBfiexWc%2FGvKvSUr7ns%2BCoOQwFfSmcJuWlp5NsdGF7Aw6Bvr1op4c5k%2BWO34uAiEnVLAvI45KXCN5an4RUDi52gCpqzR91llGYuuI%2BVSEKkIq0PzqbvssPATkv2ZbgKW16NFQPAW1VUIKT0HweY8cXcJPwk0rz4T9RrnCQtQszmUubtKsmyrBC4OJsRa7Ko3rIed08ZE6j%2BWn4ySo%2B3NeSusUuQTGn7KpNzFipkJMq7bopWwS4B2Ai%2F0oFx4O9wAzdP3eI6yWEwhrZKmchccC%2FvKvr8Ui47Bl6ECFNMroZrSpuk8FUvm6rkP1Z9b7fDTWWhLHuvffv8rBIpPjPmjGw%2B6wL3ZL0KdPQ9Oe0yFXOrrdY%2FAUhtmwE61%2BHOgaBHN7Hzdrth%2FLNY6NCsYQu%2Br2pefctP970HjwlBv5IqDmTue4x%2BzaECDD2DldUPuW34RZxaK%2FaQ7Ii4WuaKCpz8sH9RLYbMuzS0WeXPbkeP3zF1vb%2BC8O%2FmEvJJw7CF%2B%2Br%2FYmTbROCvBxDDT1ubMBjqkAV%2BNb5uNorG5puvT7jm%2FQ0y9JcYdEbKLIHuF72JmToUcWcrPdnpK2lfIW3EABzOs4Sp%2F673tEK0erKDm%2FdwoJqXdQivAq%2BA9UEE34m%2B2%2FJw5ibvNe4N1QeGjii3WjY%2FcuUn%2BknuKFwT4xlENxd7GNfdhGEKHMMtG5UvlZb34RNYB9nLz6opH0VNAhp2CdFyhOPYBL2Z8y84h%2B%2BgHPUxqZBMlth%2BY&X-Amz-Signature=84c2d0b5cda5b88c2158e6628fc362075ce17131c517ad973aa80ecdcea6465e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







