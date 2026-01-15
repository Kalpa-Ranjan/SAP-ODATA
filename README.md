



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664I2Q37XJ%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T183022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIEEjLNlzwg1oJLTp%2B9CVWUbQ2zM4%2FORAYRMSmJdsrb8pAiBJADJuoJROrUEeMyy4HcANWb6vQdEr%2F3NJ7ifQL%2FzEjir%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMgLYwqEa4gmXX5XIcKtwD6r3FcwMhnEFWJ8RILuN3HgN39gXPQKAUVRVePWO2M40eiMOIM3lhrR9QXrPfO9RZbanXA0uHTtlf%2FaSU0z2qWEgT3XGKti4br6dnLxJqBJZvb4MTOKRpRBawd%2B8ypRQ295z3XPoGDZ6Z79JLPzZFIQFu%2BaN13dO6pb3qxnj0kEsTOOWslfMdMhQHMuisyGQq8YVnw%2FpFSyk6omKqw3kDyAxuR5433zOZnW1O6pHsdcvO9YiTyuw2sfS3t61CKkmutgYdqONHOVYYkmS%2FWwKbv2wRblSve8D4B4YDvI6u1DSHQw1cFUpeLU36tlHAADwoGyVY7YTIblB0AI6fw9yd9sh2bFHYAARoJV%2B8iIqGAbeeP4M5FctUobpUTpjqHibQ3YF1qhTbHz7h%2BKXwlj6iuzrhSgj8xaDxeHcHpYoztkwXLtF9INT3%2F5cQf80jKEv0KvrXYaOeGvK3C5boh3hSr1Qe%2Fzd3ELaZuyI4BsfZdsEhHsmaEoHh%2BHVbPR7nDJz4GZgzSHAiWIQZeO4oIGzcIAZcC7OfYKHOA5HWdeysh7uYlfEhD0j%2BUdTpdzT56o1QS56XO6yxYQnCwj9gh6Hf670rSTDY4GWqpWMKy4%2FsJ4afQjGDiL7pi7jPc34wl9GkywY6pgG8frUH7Dkz0rfVhnf5jOEUyFyW%2FH%2FAhdZVkS317d15V%2Fwb2gF3PDrrumGQXBEAR%2FV%2F0rif22I4PJczKouhIW40A6X9VDefjhnJe2TUb8ToO%2FkEd1GIyCkpDEDN90Zf5UNBpixEPqDnx0Qt9LU%2B2Pa4HV%2F5qVxf9bwsEiehTEIvkisGeMm7Ku3M1d201tQ%2BfbTgW28mHW01G4QeU70pzplIuwWFaEtK&X-Amz-Signature=bf7786c5c501837cc0f41e0ca462a9c5c9fd2b3d45c449d52ce13d3de5b28327&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664I2Q37XJ%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T183022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIEEjLNlzwg1oJLTp%2B9CVWUbQ2zM4%2FORAYRMSmJdsrb8pAiBJADJuoJROrUEeMyy4HcANWb6vQdEr%2F3NJ7ifQL%2FzEjir%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMgLYwqEa4gmXX5XIcKtwD6r3FcwMhnEFWJ8RILuN3HgN39gXPQKAUVRVePWO2M40eiMOIM3lhrR9QXrPfO9RZbanXA0uHTtlf%2FaSU0z2qWEgT3XGKti4br6dnLxJqBJZvb4MTOKRpRBawd%2B8ypRQ295z3XPoGDZ6Z79JLPzZFIQFu%2BaN13dO6pb3qxnj0kEsTOOWslfMdMhQHMuisyGQq8YVnw%2FpFSyk6omKqw3kDyAxuR5433zOZnW1O6pHsdcvO9YiTyuw2sfS3t61CKkmutgYdqONHOVYYkmS%2FWwKbv2wRblSve8D4B4YDvI6u1DSHQw1cFUpeLU36tlHAADwoGyVY7YTIblB0AI6fw9yd9sh2bFHYAARoJV%2B8iIqGAbeeP4M5FctUobpUTpjqHibQ3YF1qhTbHz7h%2BKXwlj6iuzrhSgj8xaDxeHcHpYoztkwXLtF9INT3%2F5cQf80jKEv0KvrXYaOeGvK3C5boh3hSr1Qe%2Fzd3ELaZuyI4BsfZdsEhHsmaEoHh%2BHVbPR7nDJz4GZgzSHAiWIQZeO4oIGzcIAZcC7OfYKHOA5HWdeysh7uYlfEhD0j%2BUdTpdzT56o1QS56XO6yxYQnCwj9gh6Hf670rSTDY4GWqpWMKy4%2FsJ4afQjGDiL7pi7jPc34wl9GkywY6pgG8frUH7Dkz0rfVhnf5jOEUyFyW%2FH%2FAhdZVkS317d15V%2Fwb2gF3PDrrumGQXBEAR%2FV%2F0rif22I4PJczKouhIW40A6X9VDefjhnJe2TUb8ToO%2FkEd1GIyCkpDEDN90Zf5UNBpixEPqDnx0Qt9LU%2B2Pa4HV%2F5qVxf9bwsEiehTEIvkisGeMm7Ku3M1d201tQ%2BfbTgW28mHW01G4QeU70pzplIuwWFaEtK&X-Amz-Signature=d45bf2215daf05e73a8c581e330d4ceadb0f6f6c36867b8c6df76c08a5daceb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







