



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3L4GJRZ%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T011535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIGW%2Fz4VKYObho8JP53SCniBg0IU6yJp1YkraoDX9cdamAiEAi0cWH9odhixM%2FzWoXQtx6V5PXKLMw7vTRYkCdCQAyTsq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOaIq4BCgnaXod%2B%2FSyrcA%2BPliS7jh7yAv7mifblvbjdXxuNzni7kYE6DNxPBGnXQ7hiki3qAm5RN6oq7NIhLlC9y%2Fx5e9uaLQqj2hgDnpWnSavpbvgUUkjHq%2Fw5RMFgBHzVFuO%2Ftp14pmInrVZCam2FYNEljIOTQ92Z6GfdfZW%2F9JFz49Q9cjrHUrkfiPA1Bb4152h7kOUEkFuJ3UclVtsoj7TYZ0OrIna1aXM5OGDT%2FtsUZZylaOUJ6AYYWkV51C6mLNuTgVnk9puXcRPw9sZNvT22WQxpUfDjl0AO1FwP4suRjoQdPfBXYKVKqin2LvMYRgx9sP%2BKD982BfyzDuI8pJKdz6x1SnpxUZC2yHmsY0WS3uJmMnX4Z1hAqadfGKrF7XwTfTK%2B1omfPTY0ASKYI4ehc7h1KkZn7F4BcNBc0djX5KaxNFacADy%2FdLKGzbb4htQ0jxqZleWNAiktrVuEowZaOX%2FGYkAHa%2FT7svKRg5S61hkDvQ62HJFQpkdc4BbtjrL7QYelsUedrpP7bpeKn4IZSuLyvAqmNBbcLwGTHuek1m8p30d%2B8LgZR09U%2FRXwAoEI6I6pXjZmD4JcxEbtugGd3HvhcCwaoVeYLAxbowHKIGVa9spP4BQp%2BzlOziazUe5mBhwIYwp5%2BMOPYmcgGOqUB1KbJJt%2BfFM35Eqb1kI3hQJsH5LYmOY6KLt8N6f8IrgmdRJRE74fGn9nQop4FP7bAc%2Bs668Ie7Z1yS4PQyPu40rHwD5F350k6qei5VzGfJ%2BzGeRwy4mc4lkGLb%2B8veTd1p0hkZ%2BVgcwBxVKuboAC%2F6aAd3%2B1HxoCDAr%2BW%2BL2T%2FvTJznqEUaVB7IXAVTrt1xoJNTIfqTtxd7hxL5TvagyA%2BXtcSRcE&X-Amz-Signature=9f5850d8ea98b84ac6cfe85e0a0cce03826837804ef1b5d86304bc5ac0df98d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3L4GJRZ%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T011535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIGW%2Fz4VKYObho8JP53SCniBg0IU6yJp1YkraoDX9cdamAiEAi0cWH9odhixM%2FzWoXQtx6V5PXKLMw7vTRYkCdCQAyTsq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDOaIq4BCgnaXod%2B%2FSyrcA%2BPliS7jh7yAv7mifblvbjdXxuNzni7kYE6DNxPBGnXQ7hiki3qAm5RN6oq7NIhLlC9y%2Fx5e9uaLQqj2hgDnpWnSavpbvgUUkjHq%2Fw5RMFgBHzVFuO%2Ftp14pmInrVZCam2FYNEljIOTQ92Z6GfdfZW%2F9JFz49Q9cjrHUrkfiPA1Bb4152h7kOUEkFuJ3UclVtsoj7TYZ0OrIna1aXM5OGDT%2FtsUZZylaOUJ6AYYWkV51C6mLNuTgVnk9puXcRPw9sZNvT22WQxpUfDjl0AO1FwP4suRjoQdPfBXYKVKqin2LvMYRgx9sP%2BKD982BfyzDuI8pJKdz6x1SnpxUZC2yHmsY0WS3uJmMnX4Z1hAqadfGKrF7XwTfTK%2B1omfPTY0ASKYI4ehc7h1KkZn7F4BcNBc0djX5KaxNFacADy%2FdLKGzbb4htQ0jxqZleWNAiktrVuEowZaOX%2FGYkAHa%2FT7svKRg5S61hkDvQ62HJFQpkdc4BbtjrL7QYelsUedrpP7bpeKn4IZSuLyvAqmNBbcLwGTHuek1m8p30d%2B8LgZR09U%2FRXwAoEI6I6pXjZmD4JcxEbtugGd3HvhcCwaoVeYLAxbowHKIGVa9spP4BQp%2BzlOziazUe5mBhwIYwp5%2BMOPYmcgGOqUB1KbJJt%2BfFM35Eqb1kI3hQJsH5LYmOY6KLt8N6f8IrgmdRJRE74fGn9nQop4FP7bAc%2Bs668Ie7Z1yS4PQyPu40rHwD5F350k6qei5VzGfJ%2BzGeRwy4mc4lkGLb%2B8veTd1p0hkZ%2BVgcwBxVKuboAC%2F6aAd3%2B1HxoCDAr%2BW%2BL2T%2FvTJznqEUaVB7IXAVTrt1xoJNTIfqTtxd7hxL5TvagyA%2BXtcSRcE&X-Amz-Signature=fd7325610fdcfebd2a5bbc679fc262fdda7d868950d230ecca3cbfd2e8b9a2d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







