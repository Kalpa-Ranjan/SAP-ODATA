



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX4ZBTRE%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T015726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIGsblsYE65F%2FM1E3wGEYRe4Dy0%2FfrIgS%2BuxTmg%2FiSuMmAiBTE1hw%2FUhqR1UR4QMmcCRVJztZqokBYjss%2Ft3cqoQ%2F5yr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMeg7WoScCOHK1VDc6KtwDY9AcqBJWte3Xk%2BKIXEGdUwJfd94OvFHCOg3t0CMNOTGmGDV8iEXTZ4bqH9gVqieisWmvnpctGoVn8G2oEMxKs%2FHwlzMEexirftreav8IY82dsYhm05tds5Q3kiT6SMXeoGL4x3QVubfXRmCAyEm9tL53EyJe3156CniGbHwli%2F4cUN5vhfVJUuJoyFel5BLVJRxdAClOVEzE7ywY5CFAeRHvRxNudCRWM2A8TuBKLjZJj3P8V80Z18tqFvtC0J5V6DCLvRLkPUOtN72iKFUp%2BB7L9U2oTvqKWMprkj5DQgghOw%2Fhtxcd5h4GSRZswQ2QP1LWspTzUu7jHCrekXpWBbqrl9fTHKLXJgd1ayyICPW7xkec1zog52C0h3niFuyJw%2BX3axpjaksGT%2FOtGl586QDvSEf8cW%2FjEqZaJ9thfNiOXaiL9LEVcdNeM6%2Bi1u9qTduAzNBvhqryOPcmKxjPLPmdfbNaqTj8pM8FoDKDg%2B%2FZCM085nTyUKjC6SxeuzQ5DPSm98XG02SIyUEDtQpXim5wBDhjSYN8JvllIzZjC0%2FkhWhm%2BqFv4dT1DKHmFltLq%2Biocb%2Fiihc%2BFrqr4vxZlFeq6AX1Xm8we87lw7EKHlOLzNwYcVVU4gQ0Yg4w0MCszgY6pgFL6wnbjknxFjzrK02febK1lTsDVRxFOJDxzz91tOgLXEt7zDsvAjhlXVOVzgmmo8XQpcI6PQLQjuPabR6D3NqcfWoOAQUEDkgdIVZvdwna%2Bu87sfRoy5oQJKRloYENaO4vvb7tQijEPhTT6LPunw%2F282M%2FmBphBQnrwrrDAXVX0ibswxT%2F8uXpheZh6%2FkuT1EiCbO3EHJPXNdRQP%2B%2F8zJKLP%2FFVuBK&X-Amz-Signature=699173528560c5e98fb7e406fbdf2655f03d7db083014de9f3c67163d9b3507f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX4ZBTRE%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T015727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIGsblsYE65F%2FM1E3wGEYRe4Dy0%2FfrIgS%2BuxTmg%2FiSuMmAiBTE1hw%2FUhqR1UR4QMmcCRVJztZqokBYjss%2Ft3cqoQ%2F5yr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMeg7WoScCOHK1VDc6KtwDY9AcqBJWte3Xk%2BKIXEGdUwJfd94OvFHCOg3t0CMNOTGmGDV8iEXTZ4bqH9gVqieisWmvnpctGoVn8G2oEMxKs%2FHwlzMEexirftreav8IY82dsYhm05tds5Q3kiT6SMXeoGL4x3QVubfXRmCAyEm9tL53EyJe3156CniGbHwli%2F4cUN5vhfVJUuJoyFel5BLVJRxdAClOVEzE7ywY5CFAeRHvRxNudCRWM2A8TuBKLjZJj3P8V80Z18tqFvtC0J5V6DCLvRLkPUOtN72iKFUp%2BB7L9U2oTvqKWMprkj5DQgghOw%2Fhtxcd5h4GSRZswQ2QP1LWspTzUu7jHCrekXpWBbqrl9fTHKLXJgd1ayyICPW7xkec1zog52C0h3niFuyJw%2BX3axpjaksGT%2FOtGl586QDvSEf8cW%2FjEqZaJ9thfNiOXaiL9LEVcdNeM6%2Bi1u9qTduAzNBvhqryOPcmKxjPLPmdfbNaqTj8pM8FoDKDg%2B%2FZCM085nTyUKjC6SxeuzQ5DPSm98XG02SIyUEDtQpXim5wBDhjSYN8JvllIzZjC0%2FkhWhm%2BqFv4dT1DKHmFltLq%2Biocb%2Fiihc%2BFrqr4vxZlFeq6AX1Xm8we87lw7EKHlOLzNwYcVVU4gQ0Yg4w0MCszgY6pgFL6wnbjknxFjzrK02febK1lTsDVRxFOJDxzz91tOgLXEt7zDsvAjhlXVOVzgmmo8XQpcI6PQLQjuPabR6D3NqcfWoOAQUEDkgdIVZvdwna%2Bu87sfRoy5oQJKRloYENaO4vvb7tQijEPhTT6LPunw%2F282M%2FmBphBQnrwrrDAXVX0ibswxT%2F8uXpheZh6%2FkuT1EiCbO3EHJPXNdRQP%2B%2F8zJKLP%2FFVuBK&X-Amz-Signature=9542a191a720f8b9f132108b32ab9b867a3ce6a79c0aa5eecf6c98a45a8dc4db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







