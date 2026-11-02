



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KAHPUD6%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T061054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICSj%2Bj6xCbjrNUfXoWikW0qWTSmLEr%2FG9ok71bQuQyFCAiA57uCmgIQfoJVEYGk%2FS2w5v7B81A%2B6ugUAIcFDd4MEaSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIM3KaZjHR3vP%2FTc%2FLTKtwDB5KrCCYeYqbNk%2Bae%2F3%2FA4oPOocQdI%2FPtzsNm9mqpZwvkOn%2FTyBhv935MbLRmAhFq6MGJEgP0iD67KNeevRFc7I8CQUjOu06erNeqvDAKnmBsu4m1ZIfmzW6V%2Fg7OzBWbzhRHvH15rq6qapZLmnIfUU6vHUmo9y9s7hnj6q0D1eVEvW9Y3h%2BFjRdl%2FRrlgwZDJ3e9dr4aGRqtO0BguuIOSI3%2BGynq9uuRZytG3aqpE1corioSjCVamX0Dwlt13EDys7Rqo0d1xDe7RN8BL23jottvzo%2FLJmYhtwCs1lHYAcq05uBmTcFtFqYn4kIF%2FarG9%2FwygFq4VpIDHOmtxuDFJGcR93q3NbR%2FiNglZzGc7Sp6P8SMWX%2FCtbpdxIxRA24ruSH25gqvuTgWa5fWbqO6i8tgMkiSLDbk0%2BuU34y7ebYtBVdIzyslzZ5a1i0y4Tq4I8%2BEe7zX9qG7z2PRSeLnEKvRJionRaPD0z9m1zvHNuSKX5voowpQwv0jfWzgVhp5QrvkbqdF9c9aQ%2FLfa0qQ6%2BeskEY%2F1fGLn9H4Pec8QKm8Yxtui05JZGWSidLTBvs6DEk%2FOklnC%2FUFYlWjxfCXo8TpZQGd9gMK7nTw0QZzywBPswYCXe8PHM5LPRwwgpWg1wY6pgHCeKBCFRHfoisNL7TG0HmqJDWmX7f8Eg6cRZyPfL9TCPYfduhpIFm1bGhRDQ%2FpepSaX%2F2%2FIyXi8ia10V1KSmS77lvl1FbZC4FrCzF1urOyVU2QH5N7bZBIckt0BxUSnxRoCznb9MRP6ZOJMQz0gEwixjbX90nK9zqjFMpz8q93nWugNU9KUVFvDOIQ6krW%2Fhz2xj7y4v%2BryLPIZXj2ViUg5ryo%2BYRm&X-Amz-Signature=0b3d1f5e3803fdfa39206d5b4cb927a68ad6618ec8c5b49a3ef44be7a2bed0d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KAHPUD6%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T061054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICSj%2Bj6xCbjrNUfXoWikW0qWTSmLEr%2FG9ok71bQuQyFCAiA57uCmgIQfoJVEYGk%2FS2w5v7B81A%2B6ugUAIcFDd4MEaSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIM3KaZjHR3vP%2FTc%2FLTKtwDB5KrCCYeYqbNk%2Bae%2F3%2FA4oPOocQdI%2FPtzsNm9mqpZwvkOn%2FTyBhv935MbLRmAhFq6MGJEgP0iD67KNeevRFc7I8CQUjOu06erNeqvDAKnmBsu4m1ZIfmzW6V%2Fg7OzBWbzhRHvH15rq6qapZLmnIfUU6vHUmo9y9s7hnj6q0D1eVEvW9Y3h%2BFjRdl%2FRrlgwZDJ3e9dr4aGRqtO0BguuIOSI3%2BGynq9uuRZytG3aqpE1corioSjCVamX0Dwlt13EDys7Rqo0d1xDe7RN8BL23jottvzo%2FLJmYhtwCs1lHYAcq05uBmTcFtFqYn4kIF%2FarG9%2FwygFq4VpIDHOmtxuDFJGcR93q3NbR%2FiNglZzGc7Sp6P8SMWX%2FCtbpdxIxRA24ruSH25gqvuTgWa5fWbqO6i8tgMkiSLDbk0%2BuU34y7ebYtBVdIzyslzZ5a1i0y4Tq4I8%2BEe7zX9qG7z2PRSeLnEKvRJionRaPD0z9m1zvHNuSKX5voowpQwv0jfWzgVhp5QrvkbqdF9c9aQ%2FLfa0qQ6%2BeskEY%2F1fGLn9H4Pec8QKm8Yxtui05JZGWSidLTBvs6DEk%2FOklnC%2FUFYlWjxfCXo8TpZQGd9gMK7nTw0QZzywBPswYCXe8PHM5LPRwwgpWg1wY6pgHCeKBCFRHfoisNL7TG0HmqJDWmX7f8Eg6cRZyPfL9TCPYfduhpIFm1bGhRDQ%2FpepSaX%2F2%2FIyXi8ia10V1KSmS77lvl1FbZC4FrCzF1urOyVU2QH5N7bZBIckt0BxUSnxRoCznb9MRP6ZOJMQz0gEwixjbX90nK9zqjFMpz8q93nWugNU9KUVFvDOIQ6krW%2Fhz2xj7y4v%2BryLPIZXj2ViUg5ryo%2BYRm&X-Amz-Signature=470cec5503776fd0423bed418610c7796829829ea9beb42f0bf0ae7cad8ed01a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







