



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FO6LR25%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T194709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEKsd8isFGr%2FmoxLmA91CLYfTASup%2B3Yh6y9vzxoautcAiA64k%2FTr9hLxfYgcxZjt81um9atMFpeWEvyq8TW3CJ5PSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMmt%2FtoLXJaBOChVEOKtwDqJCvoJtItIgNJIq0MEspqOyJ0aTS1FZfsl%2FLQV3xqdFdlMQnh%2BAtNSeTG6Bn2Ao%2B5WRr7vb8fOU7Xd%2FNGOOwa34ZR3VSUmFd%2FtHIuJEjwH5jI1oLSwiN6Y3JJaoIf%2Fz8Sqe5CLdJUIT13hcvEwrNIpQXSCTddhfqqsxQd%2BTyh3LOlbnlZDK0uwaoE9LboAFpjbgUP0zwtoh9rcqMRy12j3W0PGKldgiOwTWrBWPigk%2F0fx8QxT0UxDQ00J8%2FSfdoPQEKGBpWjORG3mLvXXA7dt%2Bh%2BUQjASQGvfGYjx2ygYiJrV3H%2BvpigC6P0HQpNojdABEST%2FxwXHTJRJ%2FXz908wGU4qv9uRZrJKu%2Fg9wyBaiKz7Nx5s6AZhtJMIdI00%2Fh8wptHqnOe0DxV72GvJ2bg%2FHoacHgv3QvWVe0RhetBf0kgRXIYMry%2BVoJBn4PdHu9MsrP8f0jZ2ywSb22SJ38B2ZT5uiL%2B%2BWxBCt64oehnogz2NC7dBRFMElFmTrWWpWUt3Aegge7PcqQH0%2Fw8en1wnpei%2Bp9ESWK%2BTJ%2BeOUnAYvmb6ZsGD9izkECKAuR4UMUdJYcZa1PE6UcC4nf495kvY3ZYcB1zRFcZNoNCZU7hQKdMSK9fxE%2FSpFDW1BcwlqKM0QY6pgHUqnIi81%2B6c%2FMmmshvXvbY9bFnl23kmbeMO5MPxBPmU1IydUnKOzGgaG%2B0AB%2B9gRkqH5J3yGIAKNFCC8bF6yWGwEOCGgyHBCcA8GGIaVU0ai4nIxm787Q1hiKd%2F6yFg0LB%2Bbyq0cVS2ANKSIqnlrsNrVpOtazGc8ryTIxRw7uq%2Fhy0H5%2B%2BLhWAHCvFK7mwaa%2B7mohAmxxVZz3gNjUsSgKXArbNN2S8&X-Amz-Signature=bcf92841c81b9aba1a426ea2b4daed6257db6eae5494c36437d0905df3fcc8dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FO6LR25%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T194709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEKsd8isFGr%2FmoxLmA91CLYfTASup%2B3Yh6y9vzxoautcAiA64k%2FTr9hLxfYgcxZjt81um9atMFpeWEvyq8TW3CJ5PSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMmt%2FtoLXJaBOChVEOKtwDqJCvoJtItIgNJIq0MEspqOyJ0aTS1FZfsl%2FLQV3xqdFdlMQnh%2BAtNSeTG6Bn2Ao%2B5WRr7vb8fOU7Xd%2FNGOOwa34ZR3VSUmFd%2FtHIuJEjwH5jI1oLSwiN6Y3JJaoIf%2Fz8Sqe5CLdJUIT13hcvEwrNIpQXSCTddhfqqsxQd%2BTyh3LOlbnlZDK0uwaoE9LboAFpjbgUP0zwtoh9rcqMRy12j3W0PGKldgiOwTWrBWPigk%2F0fx8QxT0UxDQ00J8%2FSfdoPQEKGBpWjORG3mLvXXA7dt%2Bh%2BUQjASQGvfGYjx2ygYiJrV3H%2BvpigC6P0HQpNojdABEST%2FxwXHTJRJ%2FXz908wGU4qv9uRZrJKu%2Fg9wyBaiKz7Nx5s6AZhtJMIdI00%2Fh8wptHqnOe0DxV72GvJ2bg%2FHoacHgv3QvWVe0RhetBf0kgRXIYMry%2BVoJBn4PdHu9MsrP8f0jZ2ywSb22SJ38B2ZT5uiL%2B%2BWxBCt64oehnogz2NC7dBRFMElFmTrWWpWUt3Aegge7PcqQH0%2Fw8en1wnpei%2Bp9ESWK%2BTJ%2BeOUnAYvmb6ZsGD9izkECKAuR4UMUdJYcZa1PE6UcC4nf495kvY3ZYcB1zRFcZNoNCZU7hQKdMSK9fxE%2FSpFDW1BcwlqKM0QY6pgHUqnIi81%2B6c%2FMmmshvXvbY9bFnl23kmbeMO5MPxBPmU1IydUnKOzGgaG%2B0AB%2B9gRkqH5J3yGIAKNFCC8bF6yWGwEOCGgyHBCcA8GGIaVU0ai4nIxm787Q1hiKd%2F6yFg0LB%2Bbyq0cVS2ANKSIqnlrsNrVpOtazGc8ryTIxRw7uq%2Fhy0H5%2B%2BLhWAHCvFK7mwaa%2B7mohAmxxVZz3gNjUsSgKXArbNN2S8&X-Amz-Signature=ca12925b9ea10b55e715b59e965907c06c4e7c5631b5f3cf635fe31df85756b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







