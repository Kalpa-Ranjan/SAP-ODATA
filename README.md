



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRUFSOEB%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T021007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICcyDwOuNrqZFKkIwZ6F7kzjxkAFVm%2B%2BN2Tte%2B%2BQvf%2FOAiEA1CgGQdSt3C8%2BIzgyOWvzCJJHlSeBe5PRsX0q57xeulsq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDBiW4Kp%2BFBSYVzqiOCrcA8E5Uxs%2FVMg%2FIdYSmHtqOwK%2F6Nodh%2FbPnMfzH7Am2C5uXtPczuuwXSRNKrgUeKSZDbwINDS9Rj9VV7jXD7ZlmAY6mIxtkg5%2BCR83YjXMlSzfroD9oF7KVqwLsVyD1njaHYMZw9EJPjf%2BgVkm%2Bcz4EsziiLUtNk7zdClEfoTMP0BbO9FLaPY13Bb6hMNS7Ac0GKHvnPLaW2uihBM7yhy%2FP0vURdDIbAeQSViyQi58tCuEddKa%2Bkl4NM%2B5yATHEBiKZQoScoKJn0kOxadf5UK3jxG651wsr7vRTEPmOu8Moacn%2FaTiSDliZPbyHvPHcbjS%2F9i86peTVk0KsvUxbtTRQDXDlOSFhlPvV5bluZ1Vf4oVOUUVeOSqE6I6dYgI44roN6B9uzLaGwN2ritPVWtHl4676lT2Iad1cWqOt315bKWS0nIOw7UlIieIBVMYabn0Jy060D7E3BorXdUp88Q%2F1cjsbw5enZgcJ6r0NK4dJ4%2BxoURgeybfFmW9ZOGrEQfXDfTV%2FLsYDH3ttYRElhLGm1mQyCpJWdInNeCEmrNJgWcQbPPIxilRki1%2FDxzT0y5P%2FJN5%2Fky7uJ6Vyh2aN30K8h4nkxbuvEhDqZcgqo0ZK4H2Vzsb1MFD8hn%2BBH0FMNPrlc8GOqUBY8y3YHRHt0FrIx%2BRcGYwAl6EjPoOX%2FDQdb8lJoTTXFumJrsSuErFmK1otmPpHQ9lS3oq4g2WFGimUMWqblxcajnnSDrKoI0zxj9q4R6tfhWb0a4krHT0LXNfR80FdN86e8UorGyb4P81xVGhXbOg4HEj6L2GzHroo62JjmLUeM38d2XMGwdlu62KroDIZSvGWWd9%2Bz4%2BuCjFlTbd8z6oCNRLKw2p&X-Amz-Signature=6cdb5e564aac974e0c83bdabf75e5cf6416b3b17ec98b66653c80d26da9c13c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRUFSOEB%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T021007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCICcyDwOuNrqZFKkIwZ6F7kzjxkAFVm%2B%2BN2Tte%2B%2BQvf%2FOAiEA1CgGQdSt3C8%2BIzgyOWvzCJJHlSeBe5PRsX0q57xeulsq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDBiW4Kp%2BFBSYVzqiOCrcA8E5Uxs%2FVMg%2FIdYSmHtqOwK%2F6Nodh%2FbPnMfzH7Am2C5uXtPczuuwXSRNKrgUeKSZDbwINDS9Rj9VV7jXD7ZlmAY6mIxtkg5%2BCR83YjXMlSzfroD9oF7KVqwLsVyD1njaHYMZw9EJPjf%2BgVkm%2Bcz4EsziiLUtNk7zdClEfoTMP0BbO9FLaPY13Bb6hMNS7Ac0GKHvnPLaW2uihBM7yhy%2FP0vURdDIbAeQSViyQi58tCuEddKa%2Bkl4NM%2B5yATHEBiKZQoScoKJn0kOxadf5UK3jxG651wsr7vRTEPmOu8Moacn%2FaTiSDliZPbyHvPHcbjS%2F9i86peTVk0KsvUxbtTRQDXDlOSFhlPvV5bluZ1Vf4oVOUUVeOSqE6I6dYgI44roN6B9uzLaGwN2ritPVWtHl4676lT2Iad1cWqOt315bKWS0nIOw7UlIieIBVMYabn0Jy060D7E3BorXdUp88Q%2F1cjsbw5enZgcJ6r0NK4dJ4%2BxoURgeybfFmW9ZOGrEQfXDfTV%2FLsYDH3ttYRElhLGm1mQyCpJWdInNeCEmrNJgWcQbPPIxilRki1%2FDxzT0y5P%2FJN5%2Fky7uJ6Vyh2aN30K8h4nkxbuvEhDqZcgqo0ZK4H2Vzsb1MFD8hn%2BBH0FMNPrlc8GOqUBY8y3YHRHt0FrIx%2BRcGYwAl6EjPoOX%2FDQdb8lJoTTXFumJrsSuErFmK1otmPpHQ9lS3oq4g2WFGimUMWqblxcajnnSDrKoI0zxj9q4R6tfhWb0a4krHT0LXNfR80FdN86e8UorGyb4P81xVGhXbOg4HEj6L2GzHroo62JjmLUeM38d2XMGwdlu62KroDIZSvGWWd9%2Bz4%2BuCjFlTbd8z6oCNRLKw2p&X-Amz-Signature=8cde4cf453ac878a6726d463aafedbd3adf5bb54f8e2b67b3045bfd74e59c36d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







