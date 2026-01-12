



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXVCQERJ%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T123738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQDfSFNIMhdLJ7bbeFX9u3Y%2FGQvC2YnFqvf02LXL4O71DwIhALTngXK09ZB0jiyJq4kYbKBvQcNJwzF3wpp0E7W%2BlwVQKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYYCw7oMArI9sBnQIq3AN%2BFv8sALHcZmeiK10B3f8dAbA2hxxRP%2FS4wJp0b3W7%2BMfsRloU3373FzD%2FGTeKiR9axkBuQSR2OIU0MVyDdVb854fbxc4aGM2CISQ3FY%2B%2BbLbzJNwkCJib1GkIXs7puS3gJFvMcRXRWUNjGIeYLCgEt3HCsswH9XlZnjTvHaRYDJ8s%2Bh6umBXSxlMGyxxz7G6IylZwUFddjye4FNpCOLKbLHdg%2Fh4v1QlYrKusbuJ9yazepT%2FtqXPxvSmLiAGIKXzQL16O%2FRgJrxam36aLnM5T%2By1Ft4B2W21iFlTziTZOEuYu9doaGd%2F9%2Bt6VWVOgZbjfny%2B%2BONLDzQGh%2BGEvEIxYEvGq%2Fa2MPZ1lAuE2WpHRNMTkQmU2J0LFZf6XDfcXKbgxG33fIxTvPGg67XOWcUv5Py6A%2BPwfXU1%2FD2bAiAMiPpKnoGd9Cpv2UFuVyg8O3rnXgiYinInxL6cK0vgFG6gWjJU4qvv56QFZRtVYHUFBGn6QV5mJIB%2FlRSv4VHXWp16xA35dQFgF6m1tX16%2Fa51O1iJ9CO2Kmd05T2uVFlKSEXUfE3LqUvXCGdPJyHK6Xg0FBOV%2FXiOKLlershovjWAZLqLnNZISbxSWpJziMo8UfYPnU8u4Ff8iyaPiaTDbvJPLBjqkAcDwA7PGdlDvlV8G39oJ8L%2B75mD4qD13rMb%2FpWYwiFHJl1DKsavZAcj3IWvpW4VXgOhhhtK%2BiL1MsStsuNGC13rkk2F5ZbMUfMB5yi8md5BnpC3ohi5jvuMEe8qDc64lwK9gYouafdyi0Z6A%2BxHe3O0D49TKs3bhYWe1LC95AKQGfb9MX91w4BKfUCf2jcJhf%2FExcaBuqmUrTfy3FZ%2FqtHIAXpo3&X-Amz-Signature=87f8539982ca7ec748b4d67515d9288a9bddd515e90e2d7dccde5da96fd164cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXVCQERJ%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T123738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQDfSFNIMhdLJ7bbeFX9u3Y%2FGQvC2YnFqvf02LXL4O71DwIhALTngXK09ZB0jiyJq4kYbKBvQcNJwzF3wpp0E7W%2BlwVQKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYYCw7oMArI9sBnQIq3AN%2BFv8sALHcZmeiK10B3f8dAbA2hxxRP%2FS4wJp0b3W7%2BMfsRloU3373FzD%2FGTeKiR9axkBuQSR2OIU0MVyDdVb854fbxc4aGM2CISQ3FY%2B%2BbLbzJNwkCJib1GkIXs7puS3gJFvMcRXRWUNjGIeYLCgEt3HCsswH9XlZnjTvHaRYDJ8s%2Bh6umBXSxlMGyxxz7G6IylZwUFddjye4FNpCOLKbLHdg%2Fh4v1QlYrKusbuJ9yazepT%2FtqXPxvSmLiAGIKXzQL16O%2FRgJrxam36aLnM5T%2By1Ft4B2W21iFlTziTZOEuYu9doaGd%2F9%2Bt6VWVOgZbjfny%2B%2BONLDzQGh%2BGEvEIxYEvGq%2Fa2MPZ1lAuE2WpHRNMTkQmU2J0LFZf6XDfcXKbgxG33fIxTvPGg67XOWcUv5Py6A%2BPwfXU1%2FD2bAiAMiPpKnoGd9Cpv2UFuVyg8O3rnXgiYinInxL6cK0vgFG6gWjJU4qvv56QFZRtVYHUFBGn6QV5mJIB%2FlRSv4VHXWp16xA35dQFgF6m1tX16%2Fa51O1iJ9CO2Kmd05T2uVFlKSEXUfE3LqUvXCGdPJyHK6Xg0FBOV%2FXiOKLlershovjWAZLqLnNZISbxSWpJziMo8UfYPnU8u4Ff8iyaPiaTDbvJPLBjqkAcDwA7PGdlDvlV8G39oJ8L%2B75mD4qD13rMb%2FpWYwiFHJl1DKsavZAcj3IWvpW4VXgOhhhtK%2BiL1MsStsuNGC13rkk2F5ZbMUfMB5yi8md5BnpC3ohi5jvuMEe8qDc64lwK9gYouafdyi0Z6A%2BxHe3O0D49TKs3bhYWe1LC95AKQGfb9MX91w4BKfUCf2jcJhf%2FExcaBuqmUrTfy3FZ%2FqtHIAXpo3&X-Amz-Signature=6cab92a684bfe065ba84311d7915550d22fea37ef189237c9317440f9a440015&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







