



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSYFVSWK%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCDayBI4dYLEgx7EjS3AlLfSBZ9oPy7gTTA5JBcrnpDGAIhANZF2aJET3NzMX0FvA1DqKmVO%2BalLOOsCy2uJQU0idKUKv8DCD8QABoMNjM3NDIzMTgzODA1IgwliYdNtHwBKE3GOesq3APry6spDTlS7EeihC2Trm6s8%2B%2F37DQSZ1VAoZcAKBIoswxuUXHa2xkeqPv02nG7Rv7oIXcxYRARnqynmu5kpjSaL4DV6elP6ZJCA1ilYz0%2FFVnuKmtWOxjOCO2if%2FGP3%2Fycezdyjg66bVaCNrtSthL%2FOoU5SNbuZek3SmSQjIXtAUKzRynO0ufisdbaBVnTOHvdTYsgOjG5mvmesVbpUYvbGxzMYcF%2BBjItg4TPBEn%2BOYwsT5XkBxt%2Fz0AQ%2FuBuighVhZ5oAlTLTn6CRblMUHp1w5sdcIgtsv72qLuAQvpbkLuxe1nmPXOBGMMrcbGrr8gNIG8FOZelhyOQ7v3R%2F%2Bphk9ndadDhVAp1BMxFnhDIJj1Fw7e4SWPZyQq44kV8nVGG9Wbqi%2BZDuXFY%2FZaiUKcKI77ZNbVVAKiKBdm2aLBr2kJ8mcMuppyJ5YQO5wJtfgvYE26GN9a7NQFLIB9bGrKDHYAy0L4gs3VdZYOnYSBeuYxZOkfllXhncjM5UISG3qiW3Wvd6njw7rfC76CyVhwHGE3VzVVo2O3yrqCiJ1PhhaEns5gOokRMYiUQnDi94e16wful53p2hI3RKxqqXuT9qhZ3kHZ50AN%2FqDq%2F533%2FzzEGgyBvWkc5YxrlujCt7JvIBjqkAXaD52wjC7VWZZjzsmi8eqoGnoObakvGbrYdtakrtBp0xL2Gm747N4mViVIPOCZQJc6kqF3bO%2FvVP98dEZrlKzCo%2F%2FUiY2JtQ6OJ2nLxI3OdMPAUlly%2F4fXDnOKIOncK%2FhDa6B8FMzo1PC9EMA4O0R5AxGJXB%2B5d3vlHX7enGyuTu1tJSSBARzoH1eMe2sgwaSm6oMbism8%2F6OK9dotnbK6MIwiE&X-Amz-Signature=de8b8f2e1f1846c195868d155d742c5ed78d319d8e79854067bda8e4b1ba437c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSYFVSWK%2F20251102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251102T062131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCDayBI4dYLEgx7EjS3AlLfSBZ9oPy7gTTA5JBcrnpDGAIhANZF2aJET3NzMX0FvA1DqKmVO%2BalLOOsCy2uJQU0idKUKv8DCD8QABoMNjM3NDIzMTgzODA1IgwliYdNtHwBKE3GOesq3APry6spDTlS7EeihC2Trm6s8%2B%2F37DQSZ1VAoZcAKBIoswxuUXHa2xkeqPv02nG7Rv7oIXcxYRARnqynmu5kpjSaL4DV6elP6ZJCA1ilYz0%2FFVnuKmtWOxjOCO2if%2FGP3%2Fycezdyjg66bVaCNrtSthL%2FOoU5SNbuZek3SmSQjIXtAUKzRynO0ufisdbaBVnTOHvdTYsgOjG5mvmesVbpUYvbGxzMYcF%2BBjItg4TPBEn%2BOYwsT5XkBxt%2Fz0AQ%2FuBuighVhZ5oAlTLTn6CRblMUHp1w5sdcIgtsv72qLuAQvpbkLuxe1nmPXOBGMMrcbGrr8gNIG8FOZelhyOQ7v3R%2F%2Bphk9ndadDhVAp1BMxFnhDIJj1Fw7e4SWPZyQq44kV8nVGG9Wbqi%2BZDuXFY%2FZaiUKcKI77ZNbVVAKiKBdm2aLBr2kJ8mcMuppyJ5YQO5wJtfgvYE26GN9a7NQFLIB9bGrKDHYAy0L4gs3VdZYOnYSBeuYxZOkfllXhncjM5UISG3qiW3Wvd6njw7rfC76CyVhwHGE3VzVVo2O3yrqCiJ1PhhaEns5gOokRMYiUQnDi94e16wful53p2hI3RKxqqXuT9qhZ3kHZ50AN%2FqDq%2F533%2FzzEGgyBvWkc5YxrlujCt7JvIBjqkAXaD52wjC7VWZZjzsmi8eqoGnoObakvGbrYdtakrtBp0xL2Gm747N4mViVIPOCZQJc6kqF3bO%2FvVP98dEZrlKzCo%2F%2FUiY2JtQ6OJ2nLxI3OdMPAUlly%2F4fXDnOKIOncK%2FhDa6B8FMzo1PC9EMA4O0R5AxGJXB%2B5d3vlHX7enGyuTu1tJSSBARzoH1eMe2sgwaSm6oMbism8%2F6OK9dotnbK6MIwiE&X-Amz-Signature=4b85bcdaffdc1cccfad02cfc71d7ff2ad838e2f2153141a23696b464e7633770&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







