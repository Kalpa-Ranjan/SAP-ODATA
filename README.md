



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6R7KWZC%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T124000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIG6O9ev3NvQjAaZlrSpnI8nepis3JtjL6P%2F5yyilLl5NAiBYb1U7zWzYy5ItcnaYhXRNJzzb0SXDz5pFswR3yQKPGSr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMJNqr4kXh%2BySMx2IwKtwDolX3z4YSGE9zy3aOXWCBXd1Y5bfGzFEcFH3ynAemD3ikofBCyF12VwvA3mtyjaUJpSfiWKWUqkM0gWtpcznc7wylQ8PcjiFvWhu9Qv%2FfAU%2B2iB6Yg06rls9Ur8SpmbT4yawYuX6ZOnJsjAifkfVEzzYJbIdP1KsNpjqXi3WN4R3yF%2FdjKAmDb4tcGIH%2BSKW8Le5Ez%2FQqvLAQ8c9w7azF34zLywjM2v54EBFQse%2BZ2d67a8mWW4sf%2F6Hclq2zpXz91PgikPG6wTBHMrhPNkCZC%2FYlKN3YRaFreZaPcb8uot2lZjhuEexCVjI%2FCFSu9H6XH779uDqLjTk8xQPSiMM9yPNGaDIPWBFiK7oBAEb5cD9iNjjy%2BqeeeL9hBz1Cr9MTJhPKwAaQkclNHUHgi5XHhJDAjHxUCaDt0%2BEuOFQs5t2%2BBhx6U8yK6MheXvjkXD0FcADdwJnNiFEeNwXpQiEd63WhUG5mwTlK5hhiZEjZIksUFa6sMrLSDOKb179npU0jneI%2FACd9TdGvMO9WaOqOmuVk8SVBJUqwQi%2BontiShhixy4JAYPhGk8Gzl4T6dwpzQAhA3HLFUhJ3vjNQ7BRq9EX2H3RlDQb9Bx68TeudnC4PEW0UYqebW60h8Rwwm6S71AY6pgEsRY%2BtZG1ZHlFSaTXf9mI8hnnPBOEDpxGLlU7huYwSpCRltmP6YAtyab88LBWbQtzsvc2tkq9fxqQXQOE7Oxjg%2BlXJDMA67H20qP6zDTrtF1JXjUFg1UIr%2BFu%2FEafao5FwLd29p4R%2FzNJUIaphTSdZhKmp%2BeICCXMXUU6ymRyWN5MXc6H3%2B2mQTOUcw61QS2K%2Bc0kZxOdrnepAbB%2F%2FTqyXQA%2FAay%2FA&X-Amz-Signature=d8c869c34d6a13c59c19cca82768af8d94ca8b5bd8bda86399af16b872d2aab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6R7KWZC%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T124000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIG6O9ev3NvQjAaZlrSpnI8nepis3JtjL6P%2F5yyilLl5NAiBYb1U7zWzYy5ItcnaYhXRNJzzb0SXDz5pFswR3yQKPGSr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMJNqr4kXh%2BySMx2IwKtwDolX3z4YSGE9zy3aOXWCBXd1Y5bfGzFEcFH3ynAemD3ikofBCyF12VwvA3mtyjaUJpSfiWKWUqkM0gWtpcznc7wylQ8PcjiFvWhu9Qv%2FfAU%2B2iB6Yg06rls9Ur8SpmbT4yawYuX6ZOnJsjAifkfVEzzYJbIdP1KsNpjqXi3WN4R3yF%2FdjKAmDb4tcGIH%2BSKW8Le5Ez%2FQqvLAQ8c9w7azF34zLywjM2v54EBFQse%2BZ2d67a8mWW4sf%2F6Hclq2zpXz91PgikPG6wTBHMrhPNkCZC%2FYlKN3YRaFreZaPcb8uot2lZjhuEexCVjI%2FCFSu9H6XH779uDqLjTk8xQPSiMM9yPNGaDIPWBFiK7oBAEb5cD9iNjjy%2BqeeeL9hBz1Cr9MTJhPKwAaQkclNHUHgi5XHhJDAjHxUCaDt0%2BEuOFQs5t2%2BBhx6U8yK6MheXvjkXD0FcADdwJnNiFEeNwXpQiEd63WhUG5mwTlK5hhiZEjZIksUFa6sMrLSDOKb179npU0jneI%2FACd9TdGvMO9WaOqOmuVk8SVBJUqwQi%2BontiShhixy4JAYPhGk8Gzl4T6dwpzQAhA3HLFUhJ3vjNQ7BRq9EX2H3RlDQb9Bx68TeudnC4PEW0UYqebW60h8Rwwm6S71AY6pgEsRY%2BtZG1ZHlFSaTXf9mI8hnnPBOEDpxGLlU7huYwSpCRltmP6YAtyab88LBWbQtzsvc2tkq9fxqQXQOE7Oxjg%2BlXJDMA67H20qP6zDTrtF1JXjUFg1UIr%2BFu%2FEafao5FwLd29p4R%2FzNJUIaphTSdZhKmp%2BeICCXMXUU6ymRyWN5MXc6H3%2B2mQTOUcw61QS2K%2Bc0kZxOdrnepAbB%2F%2FTqyXQA%2FAay%2FA&X-Amz-Signature=23baf3f88af914a1f9727d5b90e2cfd075a00c809395d239121a806945522594&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







