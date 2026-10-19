



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOVAULXF%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T002138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQCJmJaq%2F2VJhx95eIB4Bxk5%2B0MVGepB98HEiVdgjfQRswIhAIIS8pjBwZyJdcOvZ4Ns6dPo6XTN0AmXil6zuEs6Yy84Kv8DCCAQABoMNjM3NDIzMTgzODA1IgzhWPimhQ1RzzQ7lDYq3AM%2FTgBj%2FMufyYOMNuRZrA97GzWV6iwfyw7sH9VZbqpV%2BQc6Fp8HDIGJbVskp9KD2EI%2FMYKgtCAdO5FWuk0OeIBSwqXp%2FYDcSvCBFWMxm60rpwi094z7FKOYrmv8ucOZhcr0O4XgkBpHFUVyhKmflzuyiV2%2FKsj4hkdIJNpdszGN58VRmi9E0a1WyPz3kP1NMoS0DuQavp9v7Ffhj0LNMEnrGtBzvb2jI9KoAiOah7HoJ%2F5nl0wUX7rnfDQKZ%2FVKkUzD7C%2FeaNvJgbq8dXPsc%2B62jDJ5e7UD8ay7ebkju7tw4eXslUJOMHwqJ%2F6jpCMbPBWLxJA15EjXLVXKfGZg8wGNqmVyLr3ZbfhNoYKttUTNtodMx2QDvXbuRMkAlN8Dw%2FMg9DSfjCFcudhuinyvy4jNbbfpwrYxWY5Bjx6kieV37A7HSpTbR3eitme3pIdvhp6wCpYsciNb5DurTNhjYT7uS9PB%2BwiVfy5feAhw4oP2B%2BJ526qo16ZCJhdmxr0LIdY2xfNBHgF3XAd6PYIH4%2BcAWy4d%2B%2F0JzthPgumtz3qN9a8AjlWYts9D%2FdnBoUczy17IDgVbMBuXww2zTXr2UPUChBVF4YY%2Btx5BPwh9IhiO5oMQ8vLnGzu6YlPUGDC3pdXWBjqkAbTkrZk5pAdMPX4j1qJIx6FhUSb1%2FV9LnCMtnpa1FJ%2BrwkPjp9xhtCwnCdBB3EhmtZ91bliFogCSe1ddzhT8YhMB9pKv7QTorTo4ee7VXsZuKMKcYf3eBdsxJxal%2FaQcUmWjPs%2FRMTBMN%2FL1KGMruW2xf2svslodl0MYJCcWC3kf342tleylRTGzd%2FCiepwsmeUhfCKmd%2BK6I1j2Vbki5Lv5m1E%2F&X-Amz-Signature=3b06f5b1635e17d4f7b24cc4e5da345d3dca2321b9c8d65dbcabe80b80320502&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOVAULXF%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T002138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQCJmJaq%2F2VJhx95eIB4Bxk5%2B0MVGepB98HEiVdgjfQRswIhAIIS8pjBwZyJdcOvZ4Ns6dPo6XTN0AmXil6zuEs6Yy84Kv8DCCAQABoMNjM3NDIzMTgzODA1IgzhWPimhQ1RzzQ7lDYq3AM%2FTgBj%2FMufyYOMNuRZrA97GzWV6iwfyw7sH9VZbqpV%2BQc6Fp8HDIGJbVskp9KD2EI%2FMYKgtCAdO5FWuk0OeIBSwqXp%2FYDcSvCBFWMxm60rpwi094z7FKOYrmv8ucOZhcr0O4XgkBpHFUVyhKmflzuyiV2%2FKsj4hkdIJNpdszGN58VRmi9E0a1WyPz3kP1NMoS0DuQavp9v7Ffhj0LNMEnrGtBzvb2jI9KoAiOah7HoJ%2F5nl0wUX7rnfDQKZ%2FVKkUzD7C%2FeaNvJgbq8dXPsc%2B62jDJ5e7UD8ay7ebkju7tw4eXslUJOMHwqJ%2F6jpCMbPBWLxJA15EjXLVXKfGZg8wGNqmVyLr3ZbfhNoYKttUTNtodMx2QDvXbuRMkAlN8Dw%2FMg9DSfjCFcudhuinyvy4jNbbfpwrYxWY5Bjx6kieV37A7HSpTbR3eitme3pIdvhp6wCpYsciNb5DurTNhjYT7uS9PB%2BwiVfy5feAhw4oP2B%2BJ526qo16ZCJhdmxr0LIdY2xfNBHgF3XAd6PYIH4%2BcAWy4d%2B%2F0JzthPgumtz3qN9a8AjlWYts9D%2FdnBoUczy17IDgVbMBuXww2zTXr2UPUChBVF4YY%2Btx5BPwh9IhiO5oMQ8vLnGzu6YlPUGDC3pdXWBjqkAbTkrZk5pAdMPX4j1qJIx6FhUSb1%2FV9LnCMtnpa1FJ%2BrwkPjp9xhtCwnCdBB3EhmtZ91bliFogCSe1ddzhT8YhMB9pKv7QTorTo4ee7VXsZuKMKcYf3eBdsxJxal%2FaQcUmWjPs%2FRMTBMN%2FL1KGMruW2xf2svslodl0MYJCcWC3kf342tleylRTGzd%2FCiepwsmeUhfCKmd%2BK6I1j2Vbki5Lv5m1E%2F&X-Amz-Signature=bf28ef57a65a209ca01331c9ae6ffd053bdd8cc3f793a1344ca170e840ab632e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







