



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FCVSERN%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T151400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZuQR71Xob%2Foht%2Bl2KCO3%2B1N7f%2Fa1lymNszfR%2BXcjPwAIhAP88kfha7NONe5s50fU1v42jxHLQhYjI2EmRRdEn9tK6KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNLnxcon2zjh9gbpsq3AP9RaqXYF9TNvFsmIjdbb4gIigJIx5hcm6JIiuqUIxcQ8SaAbQR%2BqsH40aH4YrwFaiUdekSuZTUB5UwI2gR9yrvNNP8N7Sp%2FYbUEwXyygkxUBnmE7jTLToTNW15P0d84vP5AxyrVdd7ySRaUemF3crGu81H9kHWHZy1tKPkHEeUNdtcQd%2BSYvikDXmw2MKtYg4qOoOfQY6gzJo8vQldXyCxQ8z1y%2BV1u7Zx4WpXWKJluhdz%2Fssa%2Fhad1uXmGYThgzfQxJk3mX8C6%2Fx%2F9cQyq2yJhuEcZaMw4hnOOyNNn2Q%2FdaUe3IXgk4Qq5w9bHYewRKDr7ngU%2FF2TS5xmYnji94DWK8wklU73CynougjLDDXSrD%2BbiTB%2FLbz6z99VEHZjeI2StJjn0ghjPu63%2BFUu%2Fj1Fwgxc7gJfA2ULNjqcnJvCFxeiRYODxbdr10Ne3m5%2Fgujt6FnUEFzXaC6ZviGfIpfNmexRuuJJcOLRb76XkYwkR%2Bb74FP0WIXQIcYvAVnHciyGWNSEZY3lUuf4xYMzHA84AV8efI75fMzNDMvEqB81RoVL5ssYfPX2Sq70VethmGNcAB5u7bZZ6GBfAAfxX0vvWcFb0O4kewG53un0fP4yoHLouXCDvIBB0PL7PTD22MrRBjqkASNZ%2F%2BCnUupSEEWSxPcaET0SrKo%2F0CMDVFp6Jv7E3jMZLOyFiWxC2A0%2Bkuee9E3WDzYXmVymnC4eMQa%2Fq%2B6hg%2B%2FKbr9KzU97r1lHFevbsrCSPBe7XN%2FiEZtxFQqsiihkvjR5h6igKOWxmMk531uc1z7t2plwNsZRK%2B0e%2Byu5bWSSIKxM6LmvswUuB8KBV2Kc9%2BKHmz4qB6xxmlMbM7RcEqIvv7Or&X-Amz-Signature=c4cb3561ad1243266cc2d2c3afc6c76c92f4ec83e2ceaa293db81db886e6ff8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FCVSERN%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T151400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZuQR71Xob%2Foht%2Bl2KCO3%2B1N7f%2Fa1lymNszfR%2BXcjPwAIhAP88kfha7NONe5s50fU1v42jxHLQhYjI2EmRRdEn9tK6KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNLnxcon2zjh9gbpsq3AP9RaqXYF9TNvFsmIjdbb4gIigJIx5hcm6JIiuqUIxcQ8SaAbQR%2BqsH40aH4YrwFaiUdekSuZTUB5UwI2gR9yrvNNP8N7Sp%2FYbUEwXyygkxUBnmE7jTLToTNW15P0d84vP5AxyrVdd7ySRaUemF3crGu81H9kHWHZy1tKPkHEeUNdtcQd%2BSYvikDXmw2MKtYg4qOoOfQY6gzJo8vQldXyCxQ8z1y%2BV1u7Zx4WpXWKJluhdz%2Fssa%2Fhad1uXmGYThgzfQxJk3mX8C6%2Fx%2F9cQyq2yJhuEcZaMw4hnOOyNNn2Q%2FdaUe3IXgk4Qq5w9bHYewRKDr7ngU%2FF2TS5xmYnji94DWK8wklU73CynougjLDDXSrD%2BbiTB%2FLbz6z99VEHZjeI2StJjn0ghjPu63%2BFUu%2Fj1Fwgxc7gJfA2ULNjqcnJvCFxeiRYODxbdr10Ne3m5%2Fgujt6FnUEFzXaC6ZviGfIpfNmexRuuJJcOLRb76XkYwkR%2Bb74FP0WIXQIcYvAVnHciyGWNSEZY3lUuf4xYMzHA84AV8efI75fMzNDMvEqB81RoVL5ssYfPX2Sq70VethmGNcAB5u7bZZ6GBfAAfxX0vvWcFb0O4kewG53un0fP4yoHLouXCDvIBB0PL7PTD22MrRBjqkASNZ%2F%2BCnUupSEEWSxPcaET0SrKo%2F0CMDVFp6Jv7E3jMZLOyFiWxC2A0%2Bkuee9E3WDzYXmVymnC4eMQa%2Fq%2B6hg%2B%2FKbr9KzU97r1lHFevbsrCSPBe7XN%2FiEZtxFQqsiihkvjR5h6igKOWxmMk531uc1z7t2plwNsZRK%2B0e%2Byu5bWSSIKxM6LmvswUuB8KBV2Kc9%2BKHmz4qB6xxmlMbM7RcEqIvv7Or&X-Amz-Signature=f65849611d45e59da08082377457ede4293f440f0f8c34f5cc2236f35fa62c66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







