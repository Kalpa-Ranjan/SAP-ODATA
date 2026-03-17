



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T23EMLR6%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T185502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCeE9zoUT7TRR64Xj2j4lBcSk744W7iUlqlzoGBxfewhQIgXqaiGGRXvOZps%2FEfWlQMrAumAzGNaOqJY%2F%2BDx6ztN9MqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe8XU%2Bq27333wAukCrcAzaNoSicqNul%2FcSblXf14Vg5a%2B5mfJZBUqWHRuwQUgHWsjMBLnhE0MgRhwRzjXwbuRBrZrUkUkFwMzN5eccevyUCJqN6YQ8hJsbLZgE8OkjML6ED5q5UgAv2D%2Brcs8j4hlMwAaUyQ3nWjE1UoQFzMBtB4MgluXCxfKIOBKRhZjUfHOUzX9p8r559h4K0BPQh8U90AqTm10ioZcLX35EL0Z%2BTxNBao%2FM92fVl9AI4CiFAmsqDzbHgF4IrFzKbE2Ih4OOxAyJp%2BBq1ZuPbyGf5oG8KBLIF%2BECKcoYn8UMJj6nyZOt9Vz7oVt3wz14PBEJWytktOwe5FXZ3ejPrsk1EfJ40pGsjaRWsUMbjeTmKvZ6kc4iz9zJpIJygVDCNDfvVqH%2BUecdoguVaGD6Ci7xrcq9WmNdlTT9OOThtmH4cM3wkiWWaSOxKDNFWBUm4CKwOFrJO71%2B4jFxiiL1Wg%2FkXsDEOSovJM1VxqTY6qqrSJ4g%2B4ZqDkmMfaY7NrReaALpoPB1V9AKNgmL9G4I1tuPtKXUw%2Bm5R9zYnor3Oe3kCQnQGKk1tN56tdUmnwm0BdEdOxoq3DA9D9hwUowR5QQVjFHqcwiRfrqoWmUH5cW28%2FDkGdbf%2FMOx9ASwLClLIMNjF5s0GOqUB6b9KKw0KrQVEuWcEWrBUjiKe1wx9F0WJgtUE8AR%2FEBmVG6AJJDQQ9%2BIu4TdhkoUb3UxGH13BZ%2FXU7Cvk0t2b7wjtliRJ3%2BtczKNJjgw7YNDK%2FIuSLskrEKHXuyOatNF87EOwiT8JOOXtPnobBS55F2%2BQcm0Ys%2B6W1iQkWqXY7SjwJW9YgyljJ%2FOCKr2pW4DZObrC7w8ZtuvOUzDsrop9dqVcmIck&X-Amz-Signature=065840af5bbf3224b68cdacca7db669b7e3a6987cffe8e342b83449d39e5541b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T23EMLR6%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T185502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCeE9zoUT7TRR64Xj2j4lBcSk744W7iUlqlzoGBxfewhQIgXqaiGGRXvOZps%2FEfWlQMrAumAzGNaOqJY%2F%2BDx6ztN9MqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe8XU%2Bq27333wAukCrcAzaNoSicqNul%2FcSblXf14Vg5a%2B5mfJZBUqWHRuwQUgHWsjMBLnhE0MgRhwRzjXwbuRBrZrUkUkFwMzN5eccevyUCJqN6YQ8hJsbLZgE8OkjML6ED5q5UgAv2D%2Brcs8j4hlMwAaUyQ3nWjE1UoQFzMBtB4MgluXCxfKIOBKRhZjUfHOUzX9p8r559h4K0BPQh8U90AqTm10ioZcLX35EL0Z%2BTxNBao%2FM92fVl9AI4CiFAmsqDzbHgF4IrFzKbE2Ih4OOxAyJp%2BBq1ZuPbyGf5oG8KBLIF%2BECKcoYn8UMJj6nyZOt9Vz7oVt3wz14PBEJWytktOwe5FXZ3ejPrsk1EfJ40pGsjaRWsUMbjeTmKvZ6kc4iz9zJpIJygVDCNDfvVqH%2BUecdoguVaGD6Ci7xrcq9WmNdlTT9OOThtmH4cM3wkiWWaSOxKDNFWBUm4CKwOFrJO71%2B4jFxiiL1Wg%2FkXsDEOSovJM1VxqTY6qqrSJ4g%2B4ZqDkmMfaY7NrReaALpoPB1V9AKNgmL9G4I1tuPtKXUw%2Bm5R9zYnor3Oe3kCQnQGKk1tN56tdUmnwm0BdEdOxoq3DA9D9hwUowR5QQVjFHqcwiRfrqoWmUH5cW28%2FDkGdbf%2FMOx9ASwLClLIMNjF5s0GOqUB6b9KKw0KrQVEuWcEWrBUjiKe1wx9F0WJgtUE8AR%2FEBmVG6AJJDQQ9%2BIu4TdhkoUb3UxGH13BZ%2FXU7Cvk0t2b7wjtliRJ3%2BtczKNJjgw7YNDK%2FIuSLskrEKHXuyOatNF87EOwiT8JOOXtPnobBS55F2%2BQcm0Ys%2B6W1iQkWqXY7SjwJW9YgyljJ%2FOCKr2pW4DZObrC7w8ZtuvOUzDsrop9dqVcmIck&X-Amz-Signature=4494b5b9637ba4bcad06c4e865db2b7c79bbe81282fb94bb406d6b554747adb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







