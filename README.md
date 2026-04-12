



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDCF3MMQ%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T183934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAa8XIMh3ez3ng%2FFLtrkJMfZ9zdrD5najNi9nZcHwf%2BKAiEA5%2BWauR%2Bk9IaZ5wKb5bQt6kXqjuxSoWLzTH%2FZ6agCfu0q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDI24WGPyymWFfv%2FyAyrcAwUp3TRMHHeieB2sh%2FyBspfZtARbT10m01iwcZTYKVRVmpctTeOOJJcSCl4euIr1VX2xCQM5jjUOgT1U%2FcrYssN%2FDbhIHAa6zGX3JJ%2B4IzEIDOTWN0%2B7AMJ9j4MYpiYNcAymtssOYdgdVbfOVZ5RWsTkrH7IV6oIf86hqe8m2F02VLYoBxNKJKwK1AMuhlNid8RwkjzqT8162%2BYsCEGxv2UNIh5yB%2BxS%2ByT%2FKfxnT1VdUCa0PBiI32MsHOEj0USCRCw1nPIhxVcRIthYw%2BFy4D5BZAFaqS1qbd%2F9QreWDfehqXU7dROA1eXeLrUDM38MfonaX3gtNog3%2BNwQIhyTNOIr6CWSsBYA6ShLxEi3Yh2LlPKh%2BRr0H9c79y%2Fujun3PSWN%2FCbf1t98fiENR16WB9KzA4eq4KZDXFJRFVskly72NPin0Uokjp8gq8OKry4Brr8DQqLr%2BMl7hTmFYQ7%2Fr4DSdWFH5ygAdMGFpko14jijxEBGIr9OIboUhDeD7GwZvlUKp20ssKE7aJBJhpe3Ggxu%2BOesH3UXKwMM3vQd3vDTC0IyuivU27hA%2FjaT8s8CM1hVLBY3ylofrarGC8RzSc5%2FszzW1BiJsDjCrjXI1ebKMTtAvmDo31w2RKksMNfH784GOqUBy0n%2FqoKrmsJI1WX88AAxs%2BqSMAmG3q%2FmUS%2BwbMu4tE4BDWU%2FdAim8NkPjpg1EFH0E%2BP%2FbPJu%2B7%2BM%2BPGUasI6FZbKH1t7bIlfzu%2FQov7o180rraQYZLlkXnvIYeviIbgYqjMF%2FwyO7zfk4n9LTJBpNT%2Fdl0jZIGEeSy90bzpDvkM7mwetG3wbqxSagIj4r2A3k1QoGLsfaTOaNNb%2BqmAi0L0ekQJo&X-Amz-Signature=06ee68e1632edc382399fa4cb7699a9f87aa84287f33e671e20cef54af2cc669&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDCF3MMQ%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T183934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAa8XIMh3ez3ng%2FFLtrkJMfZ9zdrD5najNi9nZcHwf%2BKAiEA5%2BWauR%2Bk9IaZ5wKb5bQt6kXqjuxSoWLzTH%2FZ6agCfu0q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDI24WGPyymWFfv%2FyAyrcAwUp3TRMHHeieB2sh%2FyBspfZtARbT10m01iwcZTYKVRVmpctTeOOJJcSCl4euIr1VX2xCQM5jjUOgT1U%2FcrYssN%2FDbhIHAa6zGX3JJ%2B4IzEIDOTWN0%2B7AMJ9j4MYpiYNcAymtssOYdgdVbfOVZ5RWsTkrH7IV6oIf86hqe8m2F02VLYoBxNKJKwK1AMuhlNid8RwkjzqT8162%2BYsCEGxv2UNIh5yB%2BxS%2ByT%2FKfxnT1VdUCa0PBiI32MsHOEj0USCRCw1nPIhxVcRIthYw%2BFy4D5BZAFaqS1qbd%2F9QreWDfehqXU7dROA1eXeLrUDM38MfonaX3gtNog3%2BNwQIhyTNOIr6CWSsBYA6ShLxEi3Yh2LlPKh%2BRr0H9c79y%2Fujun3PSWN%2FCbf1t98fiENR16WB9KzA4eq4KZDXFJRFVskly72NPin0Uokjp8gq8OKry4Brr8DQqLr%2BMl7hTmFYQ7%2Fr4DSdWFH5ygAdMGFpko14jijxEBGIr9OIboUhDeD7GwZvlUKp20ssKE7aJBJhpe3Ggxu%2BOesH3UXKwMM3vQd3vDTC0IyuivU27hA%2FjaT8s8CM1hVLBY3ylofrarGC8RzSc5%2FszzW1BiJsDjCrjXI1ebKMTtAvmDo31w2RKksMNfH784GOqUBy0n%2FqoKrmsJI1WX88AAxs%2BqSMAmG3q%2FmUS%2BwbMu4tE4BDWU%2FdAim8NkPjpg1EFH0E%2BP%2FbPJu%2B7%2BM%2BPGUasI6FZbKH1t7bIlfzu%2FQov7o180rraQYZLlkXnvIYeviIbgYqjMF%2FwyO7zfk4n9LTJBpNT%2Fdl0jZIGEeSy90bzpDvkM7mwetG3wbqxSagIj4r2A3k1QoGLsfaTOaNNb%2BqmAi0L0ekQJo&X-Amz-Signature=7f635c43f0e0c160bba993ad52c3f969aad7e768a73164ac4f8cc385af40e3c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







