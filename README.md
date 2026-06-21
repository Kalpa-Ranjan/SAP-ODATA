



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLIQLEHY%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T033621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEJiNHDF6WSt9L6nVdVDF%2FsQL8pcCWoValFzmqPX4H%2BCAiADuGZ%2BUQQ%2BwIGxxjNEyMFGjxNLpAmB7sujITBqWMTGMCqIBAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkHjubpx9y7b%2BqdHmKtwD1Dooin1s4pJGTzhrU3m70Pkk4mggfG228TDH4sxujH0gFjYPHA5Wfmf1H2DTSmlWSvkuH44LONQaEZTTJ8pLH8as1HgZv90Qu3XACZqx7mBn3CMj9oFULBFuuLmV5OqhNyCi%2BUChm%2FraUs6gQ3AwzWaQhgtk2CUnkZKrufSMiUmB52NEC9ooy12kR81DAFhKkdqwyPJhuK7GxcGiYdKQ6oOg89QjuX6cPIObreCFLN36cnFa2djPwip3EsFX4Xcum9QQSnA24avKHjibi3ElD%2FUjPa2HDgBzxTosdf7Lpf8qDKM4MD5BEXdfVKg7d1rA9bZVuchgu2iXR4SuFiGtl2ljRHg7cgU6Q%2FLM1gA5XLU2V%2F1XdGrWEt41RqiHjf6XDpW6faRr0KuJk0FhtPHFJrmKB91y4owtIKUr78Oxh08sqwTAwtNrSrd1ubiO6o7JHqbZ%2BuTkEBn2B5CEWz7X6dLhSmkX1oSsU1j6TQQrVQMmp%2BQV7agHacB%2FLvqcP1Nsv0q4sMw1tim968H%2BycWmXBvzhevPi94BbitVUqUW40q5jdfcyySXuAfDx2zP8plXROjVk1XAVEew6Ke7LPSx8x1Uru2PfNvFdKtWpPxHjvZbDRiFZYi%2BDuzrNK0wuK%2Fc0QY6pgFT0go8INMe8QFt0tJVNPLnozoK3BfZhJA4klDpQFAkNQIV6RJBqcb3P4Ha2YCcH2DFJt5tsBLnf5bH7FfV%2F%2BaxXzwJbsQ13zvdt5w4oYhSEwlicUx1YeQyfVY09L6C7IuWskyGyV0lZN31VGOU4FMQwMeHUeKO3%2B9iEIZYUKIs9lU7ApjuSTjzTBiN60VGqMkDWTYAJpH8sYZBQSargf5XeyDXGhiW&X-Amz-Signature=800297b88f33eae2a245988141307571bee69ef5cf1a9857d4253af40f43e600&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLIQLEHY%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T033621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIEJiNHDF6WSt9L6nVdVDF%2FsQL8pcCWoValFzmqPX4H%2BCAiADuGZ%2BUQQ%2BwIGxxjNEyMFGjxNLpAmB7sujITBqWMTGMCqIBAjg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkHjubpx9y7b%2BqdHmKtwD1Dooin1s4pJGTzhrU3m70Pkk4mggfG228TDH4sxujH0gFjYPHA5Wfmf1H2DTSmlWSvkuH44LONQaEZTTJ8pLH8as1HgZv90Qu3XACZqx7mBn3CMj9oFULBFuuLmV5OqhNyCi%2BUChm%2FraUs6gQ3AwzWaQhgtk2CUnkZKrufSMiUmB52NEC9ooy12kR81DAFhKkdqwyPJhuK7GxcGiYdKQ6oOg89QjuX6cPIObreCFLN36cnFa2djPwip3EsFX4Xcum9QQSnA24avKHjibi3ElD%2FUjPa2HDgBzxTosdf7Lpf8qDKM4MD5BEXdfVKg7d1rA9bZVuchgu2iXR4SuFiGtl2ljRHg7cgU6Q%2FLM1gA5XLU2V%2F1XdGrWEt41RqiHjf6XDpW6faRr0KuJk0FhtPHFJrmKB91y4owtIKUr78Oxh08sqwTAwtNrSrd1ubiO6o7JHqbZ%2BuTkEBn2B5CEWz7X6dLhSmkX1oSsU1j6TQQrVQMmp%2BQV7agHacB%2FLvqcP1Nsv0q4sMw1tim968H%2BycWmXBvzhevPi94BbitVUqUW40q5jdfcyySXuAfDx2zP8plXROjVk1XAVEew6Ke7LPSx8x1Uru2PfNvFdKtWpPxHjvZbDRiFZYi%2BDuzrNK0wuK%2Fc0QY6pgFT0go8INMe8QFt0tJVNPLnozoK3BfZhJA4klDpQFAkNQIV6RJBqcb3P4Ha2YCcH2DFJt5tsBLnf5bH7FfV%2F%2BaxXzwJbsQ13zvdt5w4oYhSEwlicUx1YeQyfVY09L6C7IuWskyGyV0lZN31VGOU4FMQwMeHUeKO3%2B9iEIZYUKIs9lU7ApjuSTjzTBiN60VGqMkDWTYAJpH8sYZBQSargf5XeyDXGhiW&X-Amz-Signature=e59d8cd6e3b8e2aad2d06d07ea2709d3e5acf185939d681064e1fa76e1474e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







