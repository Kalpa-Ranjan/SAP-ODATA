



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRDRMZPN%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T182517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCICPX1%2F%2FdPDoRRILiaWFdOEiZ9HVRmiTR8sGDejGM3HsSAiAdBc7nuzbnomf07oltpseUh9U99rMyDZCztCDKydoTSir%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMY2xvEQzWDfwc3F2%2FKtwDrdbQ6p%2F5%2BNGtV3%2FjHFLkjcJ7KIAk6ajZSwzV7%2BNn5Ll%2B8%2BCUIQbS%2FP6cbkWzoUO8TqQ0HiJL9h%2BUAiuZXKv10X3K0d7mUba7Da5ZByFYZD0PmaAnZWjSqqM%2F7BMtWYa%2BA0fRhSkS%2Fi6nkKhBxbLbZbOcbtC5J%2BunfZqsZaxvum7FRv%2FqpqjIXdchX02QtobTK3c2QjxrceLAZsK9S579T%2FZGsVe5o5te37otfu0CBScbPmiz03zgxfMqLPwCQb4kxGcLtt0RwuJv8lsy%2FliXs0k%2FrffllOpxfcD2yJrM0w5KWnI7%2FqSD3L4%2B3vN42Cntaw0y8A77K%2BxlZ0PCVwPHqUABmOVQ4VzkGe35%2BOywPI6uO4mbBO6hSr0WCffBAWT9nS%2BLc8eDJbPy228Sg0LWgmoPcgzuelOxbMpaGj03AdHxctuMn3PJ3vhZBqGYzCu65uei9ca4agNGDM2C2HiJ9ZqbP1kBHUtqvVNJi%2FreMGbcaPTRrSx68NK0OOLnVvA51WRFiU28Ug0O6i5QmN10Ab2V70bH92ITVp%2BgsK3Uhhh48WK81mxwYTRo84CVyiQvKB8NwtBpqUOuDKOIoJqx3OlQyLk4wSX1skD9IgOGDmQV5ogcfZSy3b%2FIuvYw5qjxyQY6pgENu4o5%2BWukZyjMr2dl7AG%2FEsEGOXmojPZVhs1Ny72TUaqRH%2FvXWgq9Ml442M4me9ErmrDzlv9mshNKQBkWlIujiLmdIGEb%2FCfVAaE324ge5TSUGI96yL4x18YtBRbgCe4KYYoEJZldcWliXAMxwp2WH8D%2B%2FOKkylAG%2FP09woZC4V22ddkdZCG2Ylv1ZdOF8Tc16%2BWbeqGgvi%2FlXiGbaQ%2B7B90WdRx5&X-Amz-Signature=7c03801a19e57182147d5c7102e7862bb964ce252413e850433901c14e66d011&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRDRMZPN%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T182517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCICPX1%2F%2FdPDoRRILiaWFdOEiZ9HVRmiTR8sGDejGM3HsSAiAdBc7nuzbnomf07oltpseUh9U99rMyDZCztCDKydoTSir%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMY2xvEQzWDfwc3F2%2FKtwDrdbQ6p%2F5%2BNGtV3%2FjHFLkjcJ7KIAk6ajZSwzV7%2BNn5Ll%2B8%2BCUIQbS%2FP6cbkWzoUO8TqQ0HiJL9h%2BUAiuZXKv10X3K0d7mUba7Da5ZByFYZD0PmaAnZWjSqqM%2F7BMtWYa%2BA0fRhSkS%2Fi6nkKhBxbLbZbOcbtC5J%2BunfZqsZaxvum7FRv%2FqpqjIXdchX02QtobTK3c2QjxrceLAZsK9S579T%2FZGsVe5o5te37otfu0CBScbPmiz03zgxfMqLPwCQb4kxGcLtt0RwuJv8lsy%2FliXs0k%2FrffllOpxfcD2yJrM0w5KWnI7%2FqSD3L4%2B3vN42Cntaw0y8A77K%2BxlZ0PCVwPHqUABmOVQ4VzkGe35%2BOywPI6uO4mbBO6hSr0WCffBAWT9nS%2BLc8eDJbPy228Sg0LWgmoPcgzuelOxbMpaGj03AdHxctuMn3PJ3vhZBqGYzCu65uei9ca4agNGDM2C2HiJ9ZqbP1kBHUtqvVNJi%2FreMGbcaPTRrSx68NK0OOLnVvA51WRFiU28Ug0O6i5QmN10Ab2V70bH92ITVp%2BgsK3Uhhh48WK81mxwYTRo84CVyiQvKB8NwtBpqUOuDKOIoJqx3OlQyLk4wSX1skD9IgOGDmQV5ogcfZSy3b%2FIuvYw5qjxyQY6pgENu4o5%2BWukZyjMr2dl7AG%2FEsEGOXmojPZVhs1Ny72TUaqRH%2FvXWgq9Ml442M4me9ErmrDzlv9mshNKQBkWlIujiLmdIGEb%2FCfVAaE324ge5TSUGI96yL4x18YtBRbgCe4KYYoEJZldcWliXAMxwp2WH8D%2B%2FOKkylAG%2FP09woZC4V22ddkdZCG2Ylv1ZdOF8Tc16%2BWbeqGgvi%2FlXiGbaQ%2B7B90WdRx5&X-Amz-Signature=5b607687095d77e18be2165734e48281d8e2227976e95fbb09dc08ac98368f5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







