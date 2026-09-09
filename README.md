



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663374OHDT%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T002102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8qCR%2BhD5nrR4Vav%2BEUT%2FGwGq4IGtbs01RWtSIjC9MVAiAw9A3zyxlHiqWgC6lW%2BRgT7mnZVRjX1if7A3etAKjkmyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMey2xpHVhlpOk7c1iKtwD%2B6Nt1UwocLwU5ySndEN5%2Beuqx09HyE2K7lL78189%2FnkEOnyIByid99Pnj4vWsGbmsTdmMxJj093HRhj7dMU%2F5hIudzTrQBxPQR7mNvECG40rBm8Gdn3jshGZvMSzCUMEwOlJY6TWwj0%2BY8mPCJy6DR%2BVdztu4rWeY0gkYf3AmwgNRcdZ01b1d%2FYwjyWqjbsc0Z2P68Fsar1HX4maVHBWk4zDmMho79t771eRHETWhGx3gwvUTep4qD8NwzY%2BpgJ0XskJyUXTDEVC3J23R1gLFQG24SKP2ZpCjAiqw4LBiQMHs4%2Bg01jSCwczQM7WfUdh9MSxMvTu1yci7O6NYfFyn6m7EmMZ8AmnfXvxbKBrzbVMw8BC1EI8Knrkfjq1DeS%2FYrWU9nD1vrt7YK6W9kNmUKoyasa84ao%2BI%2BhrGWr1424ej461%2Bj%2Fd8AxW%2F3hWqbpC18M67VZSSL%2FmqLqskCi39i5ce%2FIZ%2BSKPJV7nJJIDWT7fBsgFFAhGvDNzxtll9xFWUlVm%2FDVqwY%2BMSgeGFNxVhnQ42g1Mil0JhQytntpENTDMhxsQQ0nEWN1F5%2BujFff6d%2FR4TIs86RexWo%2FLUKbwsEHzFalvlO5LnxfcgJxcqe9sX2sfwyctQ3LeRZ0wvKaC1QY6pgHtEITVDX2kKE98dDARSIEBAHM7sevTJUYBhJv4d9u3EkwrbD1KgXT0WJDHtZgz4xY2FocoyBWwl2zJu430spSFdKPsLiYRcia1xvxsBmpWAtuFVCozvjCcq8SxcQ6JkR2cz3%2BSpqXwgcTyvq5IzPGV5hQwJeg%2BHQGuX8H5QNUnyH4sw2VdKp%2BjYczpZ4oJl2YVX%2BI0hXPGqQTwL23WKsR7pGKpQA2v&X-Amz-Signature=1b311451d8e1b96e12535b55a118f4f84ae9ec2e7c16647b49ca0e891505e123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663374OHDT%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T002102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8qCR%2BhD5nrR4Vav%2BEUT%2FGwGq4IGtbs01RWtSIjC9MVAiAw9A3zyxlHiqWgC6lW%2BRgT7mnZVRjX1if7A3etAKjkmyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMey2xpHVhlpOk7c1iKtwD%2B6Nt1UwocLwU5ySndEN5%2Beuqx09HyE2K7lL78189%2FnkEOnyIByid99Pnj4vWsGbmsTdmMxJj093HRhj7dMU%2F5hIudzTrQBxPQR7mNvECG40rBm8Gdn3jshGZvMSzCUMEwOlJY6TWwj0%2BY8mPCJy6DR%2BVdztu4rWeY0gkYf3AmwgNRcdZ01b1d%2FYwjyWqjbsc0Z2P68Fsar1HX4maVHBWk4zDmMho79t771eRHETWhGx3gwvUTep4qD8NwzY%2BpgJ0XskJyUXTDEVC3J23R1gLFQG24SKP2ZpCjAiqw4LBiQMHs4%2Bg01jSCwczQM7WfUdh9MSxMvTu1yci7O6NYfFyn6m7EmMZ8AmnfXvxbKBrzbVMw8BC1EI8Knrkfjq1DeS%2FYrWU9nD1vrt7YK6W9kNmUKoyasa84ao%2BI%2BhrGWr1424ej461%2Bj%2Fd8AxW%2F3hWqbpC18M67VZSSL%2FmqLqskCi39i5ce%2FIZ%2BSKPJV7nJJIDWT7fBsgFFAhGvDNzxtll9xFWUlVm%2FDVqwY%2BMSgeGFNxVhnQ42g1Mil0JhQytntpENTDMhxsQQ0nEWN1F5%2BujFff6d%2FR4TIs86RexWo%2FLUKbwsEHzFalvlO5LnxfcgJxcqe9sX2sfwyctQ3LeRZ0wvKaC1QY6pgHtEITVDX2kKE98dDARSIEBAHM7sevTJUYBhJv4d9u3EkwrbD1KgXT0WJDHtZgz4xY2FocoyBWwl2zJu430spSFdKPsLiYRcia1xvxsBmpWAtuFVCozvjCcq8SxcQ6JkR2cz3%2BSpqXwgcTyvq5IzPGV5hQwJeg%2BHQGuX8H5QNUnyH4sw2VdKp%2BjYczpZ4oJl2YVX%2BI0hXPGqQTwL23WKsR7pGKpQA2v&X-Amz-Signature=01fbc04ac5ae741808c9102cba5f61d97f40954cd6c95adcb2be656845202fb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







