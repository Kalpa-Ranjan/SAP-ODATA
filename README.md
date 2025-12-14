



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHF6K5NT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T123005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIHZrh9dUczh0PxGF%2FEKY1pQYqpB0dPUkTmR%2F3zkXjGZ%2BAiB6FigXKjPttMZdwL3J0%2FjRscmQ%2BgksMDfK4y6vPOTEdSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMjgfLybyajBlSV0PSKtwDF3zvf9yYAWHqltCZED%2B1Mp4OyeqLku8Tl9QPUACpCW4UF7eH9hiXFto%2B4q2xwo1iyDX5TQvccfW07PEXAB4mq6kjXi91srgodsH7%2B5rtQe4icAZfJcPjJ%2Ff%2BLIxQkogC%2FV%2FqnuFd0luJFG6GrIOSPKoKlLWuTnItHl8Q2JE2AZ4LjA%2F1UPvFNYckffQXis6VUwrj7lrSvItYEcKhU6CSJjcCdAOYEO6z7AQlsRbtaGG8j%2B8bY1PknpZVS%2BOg9BB7ZHAKjubgtjsQjoUVt9BYPSvpuINmuohiEVpiQNNdYqtrkre1kamV4LX0Feo%2B%2F0ap8ac0FKunDppyNFWB3InpTNTi7azsySmdj2oojbIHC26MKVY0DPpwqKfhv67lisrDnD3AdJkFI2c5%2BigqjwrK29tA81TG5JvzXQV2zL0ql2PO5m%2BRucl6OGawXr7z2vkz9L%2FZpVvvXf9ctTm%2Fd8Sa%2FNP7wUkqO0XptxFLSnxeEfnsGWssyIvk14VWbFTb%2FpTJeEexU020DAwTq6SKeDTgshZt%2FlLaDiGjYEaJ5uLehlKJ7hwrfWh5uY3pjt%2BQy4oiEY3%2FRfKi1nEoXTR4eVvSZup6az2gzvEIuj4CJwajq%2FNHIwqIM3Y50ra9ACowjtD5yQY6pgEnXXWNZFtGLh%2BBcRMBJJuw%2BLxozUtNySj9KLTHR8fxzndJmDzZ88FSt%2FFjK6E4zQ4LFvX315r1P5uVrvWKJIa%2Fe14mopxYxyUBxlsQQvH3hkf%2B6a8XsF%2FcKj5QR9yCL8wBBZYgdLZInO6ApOE328YqjtCde8LED%2B4FBxohPbYGozZtW2c%2F%2BFnUh3eg3HsnXYD0b0iQT%2BctLM4TjBN0Eh9fbYyvVk2u&X-Amz-Signature=640e948e388018e0af11a168a643d1bcd3fa3ab719bafd4210a24ecfd51d57e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHF6K5NT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T123005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIHZrh9dUczh0PxGF%2FEKY1pQYqpB0dPUkTmR%2F3zkXjGZ%2BAiB6FigXKjPttMZdwL3J0%2FjRscmQ%2BgksMDfK4y6vPOTEdSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMjgfLybyajBlSV0PSKtwDF3zvf9yYAWHqltCZED%2B1Mp4OyeqLku8Tl9QPUACpCW4UF7eH9hiXFto%2B4q2xwo1iyDX5TQvccfW07PEXAB4mq6kjXi91srgodsH7%2B5rtQe4icAZfJcPjJ%2Ff%2BLIxQkogC%2FV%2FqnuFd0luJFG6GrIOSPKoKlLWuTnItHl8Q2JE2AZ4LjA%2F1UPvFNYckffQXis6VUwrj7lrSvItYEcKhU6CSJjcCdAOYEO6z7AQlsRbtaGG8j%2B8bY1PknpZVS%2BOg9BB7ZHAKjubgtjsQjoUVt9BYPSvpuINmuohiEVpiQNNdYqtrkre1kamV4LX0Feo%2B%2F0ap8ac0FKunDppyNFWB3InpTNTi7azsySmdj2oojbIHC26MKVY0DPpwqKfhv67lisrDnD3AdJkFI2c5%2BigqjwrK29tA81TG5JvzXQV2zL0ql2PO5m%2BRucl6OGawXr7z2vkz9L%2FZpVvvXf9ctTm%2Fd8Sa%2FNP7wUkqO0XptxFLSnxeEfnsGWssyIvk14VWbFTb%2FpTJeEexU020DAwTq6SKeDTgshZt%2FlLaDiGjYEaJ5uLehlKJ7hwrfWh5uY3pjt%2BQy4oiEY3%2FRfKi1nEoXTR4eVvSZup6az2gzvEIuj4CJwajq%2FNHIwqIM3Y50ra9ACowjtD5yQY6pgEnXXWNZFtGLh%2BBcRMBJJuw%2BLxozUtNySj9KLTHR8fxzndJmDzZ88FSt%2FFjK6E4zQ4LFvX315r1P5uVrvWKJIa%2Fe14mopxYxyUBxlsQQvH3hkf%2B6a8XsF%2FcKj5QR9yCL8wBBZYgdLZInO6ApOE328YqjtCde8LED%2B4FBxohPbYGozZtW2c%2F%2BFnUh3eg3HsnXYD0b0iQT%2BctLM4TjBN0Eh9fbYyvVk2u&X-Amz-Signature=f1acb58b72b0a6e25d1054e5ed0e3197862892a191f80e3b25433e47f294f910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







