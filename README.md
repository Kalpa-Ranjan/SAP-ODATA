



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ENI4GGU%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T015549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgjBtFj5zU7SNO7Rd2pl9Dt%2BWAnwXM7j7l0E8l1yySlwIhAL6RsbRQGQEuf%2FRxXQN%2BnSok8z5oniu2jNLshi%2B5OjlmKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtBekCW51orAtoTWsq3AP7tjnMoB7rXttrJ85BXea%2B0aHFPodNPpVmxNWvw8XtEM6K1J21GBPKdMcNWNLXaRr0o4nbSckatvNdXKXJRWBudbMJKLsbAuwJUaKwy6yzm7e6tQ%2FEdXfgbCnSywIirj7fhL2jLIBpovSyJvaycEbUba23ICrvLHBusELtdSR%2FYth5si9aPDl4y%2BEoZgrpt%2Bx1BY5dIua9uWvz7C3NViWqibROESzTP0iO4XgJnjc2teKhg%2F3coGq%2B0YiRoasmB3RUaA%2FDxFsXaxe7PGZYVWBcZAIhUElyRsnGW2cGWcTnN7k%2Fbbyeza6MfwwA6lygnt1dE0n3eWeOw3x4PCun%2FsTGhN0x%2BARjHYH49VkEdnyvNyFB%2FxiWFeIb5Q1vkW%2Bcg6FZnQjfG1WW%2Fu%2FK0pI5eZYd2uIDyCZcCGjdDqnDC5CztIW59VhLUpJHfZSa%2F%2BTUi9T%2FlILa%2Bfw%2FlXKEwROwfDK%2FzJlmBx5bOigEccKrVqB4bB4xOocIrUYESusB8BV0lolDlFKSvaxh6nKe9MHy05XHmQIzT4%2Fx%2BuanV%2FqsQ2aT6HysQ2%2FKjLj8z13UI6ut5czqrkGYkRzXKTgjlXhO9JD3oz4y0xlzXRnppdrmOatxphayvKZ8q2v9WHCzazC70pHOBjqkAVJ7fUHaA6%2F5y3e2uoxXaT9Hru4Wb4E9bS%2FGvPsgqPqgd6mlIEcaE34qxOVFaM7Nw%2FszgWWG%2Bh38ta8WxOS2EronVT2xMMSy6tFgYYHrZP%2FmGQ%2FggquUxlYQc4vZJEgLv%2B7g7SiBRBvb9YqeD6h21GSJmoT92N7adGQbOx40QKmsCVOa62v7ksXF68XLtOovMRTU%2BrbSXwB%2BftbUYuXzA1hxAINy&X-Amz-Signature=3453b2c490df26e2a4dffb6064f5b16940de895758d3cdb1430a529f6d2f4f60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ENI4GGU%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T015549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgjBtFj5zU7SNO7Rd2pl9Dt%2BWAnwXM7j7l0E8l1yySlwIhAL6RsbRQGQEuf%2FRxXQN%2BnSok8z5oniu2jNLshi%2B5OjlmKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtBekCW51orAtoTWsq3AP7tjnMoB7rXttrJ85BXea%2B0aHFPodNPpVmxNWvw8XtEM6K1J21GBPKdMcNWNLXaRr0o4nbSckatvNdXKXJRWBudbMJKLsbAuwJUaKwy6yzm7e6tQ%2FEdXfgbCnSywIirj7fhL2jLIBpovSyJvaycEbUba23ICrvLHBusELtdSR%2FYth5si9aPDl4y%2BEoZgrpt%2Bx1BY5dIua9uWvz7C3NViWqibROESzTP0iO4XgJnjc2teKhg%2F3coGq%2B0YiRoasmB3RUaA%2FDxFsXaxe7PGZYVWBcZAIhUElyRsnGW2cGWcTnN7k%2Fbbyeza6MfwwA6lygnt1dE0n3eWeOw3x4PCun%2FsTGhN0x%2BARjHYH49VkEdnyvNyFB%2FxiWFeIb5Q1vkW%2Bcg6FZnQjfG1WW%2Fu%2FK0pI5eZYd2uIDyCZcCGjdDqnDC5CztIW59VhLUpJHfZSa%2F%2BTUi9T%2FlILa%2Bfw%2FlXKEwROwfDK%2FzJlmBx5bOigEccKrVqB4bB4xOocIrUYESusB8BV0lolDlFKSvaxh6nKe9MHy05XHmQIzT4%2Fx%2BuanV%2FqsQ2aT6HysQ2%2FKjLj8z13UI6ut5czqrkGYkRzXKTgjlXhO9JD3oz4y0xlzXRnppdrmOatxphayvKZ8q2v9WHCzazC70pHOBjqkAVJ7fUHaA6%2F5y3e2uoxXaT9Hru4Wb4E9bS%2FGvPsgqPqgd6mlIEcaE34qxOVFaM7Nw%2FszgWWG%2Bh38ta8WxOS2EronVT2xMMSy6tFgYYHrZP%2FmGQ%2FggquUxlYQc4vZJEgLv%2B7g7SiBRBvb9YqeD6h21GSJmoT92N7adGQbOx40QKmsCVOa62v7ksXF68XLtOovMRTU%2BrbSXwB%2BftbUYuXzA1hxAINy&X-Amz-Signature=d3aef94d46dc2b6fd065c8c9c4bfb7cb8c580261f00bbb6560566df4e7a4a108&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







