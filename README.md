



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHVRXC7C%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T190136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIDWCIlI%2FVGl2uN8oXuBuKnqkaZ%2BvZgvFkVDyyQ3qg6KPAiBAtbdsSyZFvfQTR6P3Pymcn2IUph47z7VTLk4qzEVkcCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMm3SPUa1TXjF7SSO2KtwDqBlqGwzTzQa4KhMQYPOnEZW9CLXHNLNmtwfjaF48BtUPu5VIu%2BWwGdRXEVKvan8YwnONNWY8A0AG9M5539eL6kdOsLyLe58VA4AwjB6X9CbN0qaMLL0qtoEcRd6j5QyEFz6sVhGLkRjplDINYncxzKZ30CHiR4gYGQAItIKYe6Dyo8AgGle8F3ZlsvDHwxHOvup4KOexdYyN%2Ft5mfBbkHGvMJgvu7O7TqvepXHUwuOrPJWofBuxzNz9L5kjqQwLK9QP1mS10CGKo1HfDQ0Pek0t8y4JTJoUrONx50Jmnx51e4L80cQiitSNanQtlb4KY4zJL4tFDHBuW5wFeHKTHIMy5t5HzuM3G3NKed3x0YZPRjNS9YAvX%2FnHvCn%2FNVVoKGhlGdO3oLZGTwqrAMGBuJPFARWe7rJJIZe983aBjIfcYfTuw1wSzUfV8Riui5Gat9lIJE9aYUuFv1PLuxE%2BX3XkuRL9To8euEkWXiIqbPu4maeMyvM%2BPsahj5oT3k0RkcLfg9StRhnOICfkUS7Ub9yc61aloNHV%2BCvnAd8OG9%2FD3zjJcd7VZsbvRa4tP9a40AyEtMNx12YeENzXrm%2BLck4xa85hBFpz4J1K%2FcBrhRwm4FlgBNAoq5bmOQ9QwmsHj0gY6pgG1PBSaA1jE1f6v0aquCnRMWGJPHJYq%2Fs2GQHRKGyJaurhBkuKFV9rgK%2BifUs7ONVlnPNZ8Ftw9UKwnymQmvyXvB6TjhkTO%2FSgMwDaYSUjHWbf%2F3Q4BAtuyvFiKt7wTeL7qD4vr%2BgleDZ%2FJYKf8f6vCOfKH1hD0DbbOFbJTQwZRG0IT049jp1fCIO%2BAWyDD52CckFUidK5FpjZhPnhxyVAwTQyyqknl&X-Amz-Signature=54c00d54dfd74b4529444b5c96dc04ffd2b3d776f38322c12678e22b26542035&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHVRXC7C%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T190136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIDWCIlI%2FVGl2uN8oXuBuKnqkaZ%2BvZgvFkVDyyQ3qg6KPAiBAtbdsSyZFvfQTR6P3Pymcn2IUph47z7VTLk4qzEVkcCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMm3SPUa1TXjF7SSO2KtwDqBlqGwzTzQa4KhMQYPOnEZW9CLXHNLNmtwfjaF48BtUPu5VIu%2BWwGdRXEVKvan8YwnONNWY8A0AG9M5539eL6kdOsLyLe58VA4AwjB6X9CbN0qaMLL0qtoEcRd6j5QyEFz6sVhGLkRjplDINYncxzKZ30CHiR4gYGQAItIKYe6Dyo8AgGle8F3ZlsvDHwxHOvup4KOexdYyN%2Ft5mfBbkHGvMJgvu7O7TqvepXHUwuOrPJWofBuxzNz9L5kjqQwLK9QP1mS10CGKo1HfDQ0Pek0t8y4JTJoUrONx50Jmnx51e4L80cQiitSNanQtlb4KY4zJL4tFDHBuW5wFeHKTHIMy5t5HzuM3G3NKed3x0YZPRjNS9YAvX%2FnHvCn%2FNVVoKGhlGdO3oLZGTwqrAMGBuJPFARWe7rJJIZe983aBjIfcYfTuw1wSzUfV8Riui5Gat9lIJE9aYUuFv1PLuxE%2BX3XkuRL9To8euEkWXiIqbPu4maeMyvM%2BPsahj5oT3k0RkcLfg9StRhnOICfkUS7Ub9yc61aloNHV%2BCvnAd8OG9%2FD3zjJcd7VZsbvRa4tP9a40AyEtMNx12YeENzXrm%2BLck4xa85hBFpz4J1K%2FcBrhRwm4FlgBNAoq5bmOQ9QwmsHj0gY6pgG1PBSaA1jE1f6v0aquCnRMWGJPHJYq%2Fs2GQHRKGyJaurhBkuKFV9rgK%2BifUs7ONVlnPNZ8Ftw9UKwnymQmvyXvB6TjhkTO%2FSgMwDaYSUjHWbf%2F3Q4BAtuyvFiKt7wTeL7qD4vr%2BgleDZ%2FJYKf8f6vCOfKH1hD0DbbOFbJTQwZRG0IT049jp1fCIO%2BAWyDD52CckFUidK5FpjZhPnhxyVAwTQyyqknl&X-Amz-Signature=f28cf4c63167fefb1f9f6fff1c6ea188cc50fb70d2cc8dc030a5b1e3dad6903a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







