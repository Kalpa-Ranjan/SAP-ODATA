



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZUAA6TD%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T020216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGU9ov1BBZJUHjw7zMttTfnIG7AmZc%2BLpnDdoXMwWIQ7AiEAjA9jBaizG8rL%2BKvCy9x35b1PAJeKgAI%2BMb3sCJRBGJ8qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2U3BTohP4lKllmISrcAy0EitGZp%2FnZf9sH3aNlCMSfOOEXHO6zgOmIJmxzS6JQveUzj1SzHArm9AokSwjPcO34Itn7rfI6rABA%2FP1qFa7IkhAaWQwLd7c0QJXpe2hx582%2Fqtfjn5dN4%2FZeuth%2B4PozNjGM9%2B3lUVhhthQJ3QnSIYzg8fcP3NZ%2BoLsN5rEkYpFusy%2FqvUPOZ8UFcxfqpbKnXZUFQnyk7aF6wWlQGkzKW%2BT0Ykyjd%2Bzf3eorM6uZ929B0aSCxeKjRjkiKIyTRCUCKZLqiC%2BV4lGXDrw37bMwEDEPzJuah5qm%2FsJSBkK8MpnotaVjlTX9OXbtzC%2BnSa%2B7bC8YW%2FcC6wZhESQ5NRx9s4q1wdw5GLyJkrqDPX2NwT6XwG6DYbhC9fmpye7ZJVKXv8dmtSH1VjXhelrL%2Fbge%2BWthpARlR6edFtxl7Zkgm9ANLhZ4GflTL1aUWKpZmKOKB66mem9naitDp7gER7YrvbylGb8pChcA4Tl4P99ySp2kr8zPZMzL1669jA6JnU%2FfMG4ItIojOtrC55JYq%2BoR%2BmCHkhN3k3c71UVCZMU4lcC74AvLq8Q%2BUrARCDPLppatkWulKPiepS4Z2hLYUcz39taAny0yZO7WS1mXmUQcBj%2BlHy%2BGWIqQPMUlMO2KzM4GOqUBOxNnmkEFPmeYd%2BZ0xX9%2FII9zt9dBHEzGuiubm4UM3EINithA%2F8pNqL5s5n%2FiQsw6LzfnAQCC8EeZRO4Zit0xryW9i5mHZYdqTPxKkkyBmn74B%2FB%2F7SbqFcUPMfsBok%2FSjBtyn3PnshuJjPgVcSgS6p39ZLXSicycX8chtsPoTpz17vkmSfdIePVXlKld75BcHC0ii4lhf54GGQaz9EphgG14%2BUUQ&X-Amz-Signature=c64ee5bb71831829a505e58a8f255c96db9ac930bc25ea5cde75286b02cdc97e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZUAA6TD%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T020217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGU9ov1BBZJUHjw7zMttTfnIG7AmZc%2BLpnDdoXMwWIQ7AiEAjA9jBaizG8rL%2BKvCy9x35b1PAJeKgAI%2BMb3sCJRBGJ8qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2U3BTohP4lKllmISrcAy0EitGZp%2FnZf9sH3aNlCMSfOOEXHO6zgOmIJmxzS6JQveUzj1SzHArm9AokSwjPcO34Itn7rfI6rABA%2FP1qFa7IkhAaWQwLd7c0QJXpe2hx582%2Fqtfjn5dN4%2FZeuth%2B4PozNjGM9%2B3lUVhhthQJ3QnSIYzg8fcP3NZ%2BoLsN5rEkYpFusy%2FqvUPOZ8UFcxfqpbKnXZUFQnyk7aF6wWlQGkzKW%2BT0Ykyjd%2Bzf3eorM6uZ929B0aSCxeKjRjkiKIyTRCUCKZLqiC%2BV4lGXDrw37bMwEDEPzJuah5qm%2FsJSBkK8MpnotaVjlTX9OXbtzC%2BnSa%2B7bC8YW%2FcC6wZhESQ5NRx9s4q1wdw5GLyJkrqDPX2NwT6XwG6DYbhC9fmpye7ZJVKXv8dmtSH1VjXhelrL%2Fbge%2BWthpARlR6edFtxl7Zkgm9ANLhZ4GflTL1aUWKpZmKOKB66mem9naitDp7gER7YrvbylGb8pChcA4Tl4P99ySp2kr8zPZMzL1669jA6JnU%2FfMG4ItIojOtrC55JYq%2BoR%2BmCHkhN3k3c71UVCZMU4lcC74AvLq8Q%2BUrARCDPLppatkWulKPiepS4Z2hLYUcz39taAny0yZO7WS1mXmUQcBj%2BlHy%2BGWIqQPMUlMO2KzM4GOqUBOxNnmkEFPmeYd%2BZ0xX9%2FII9zt9dBHEzGuiubm4UM3EINithA%2F8pNqL5s5n%2FiQsw6LzfnAQCC8EeZRO4Zit0xryW9i5mHZYdqTPxKkkyBmn74B%2FB%2F7SbqFcUPMfsBok%2FSjBtyn3PnshuJjPgVcSgS6p39ZLXSicycX8chtsPoTpz17vkmSfdIePVXlKld75BcHC0ii4lhf54GGQaz9EphgG14%2BUUQ&X-Amz-Signature=d0a2d4bd90398b0080ba624a177e1d0e3ca94433bbed91c0e525885c1befb266&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







