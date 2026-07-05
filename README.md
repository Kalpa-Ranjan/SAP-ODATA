



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW76TZQO%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T190839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFgPP5BVcUQ4sLJ%2BsUsS9BWCTruHNMTfQTnux0kNZJnjAiEAymxoJ509%2BSJPFXzEJyW%2F0I03q3WeaPLuh3FPz7x1jWEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNuPcdhDS89VD8S7iircA%2Fn7ODxe8zzqJEYYmySxzmEWYVPDJ%2F4ssn74pln1GH9oQSNy8KbRK%2FL7nT2Uao%2BlT77oKDW49AYlZVDA4arKhBzXd9Q%2F36hu8Up4WCmOdpojwVYTnFLO5S1TwlR21%2F1hj4VRUvbhYPjiIylIpqwgiPl%2Bc3jwEqCiPR8XRYOc7GzH%2BVy%2FqtwHcelJM%2BHBwJrZguptawhL8MR8Qzwsh8QSKhZrx8D37gjClAi%2BA4OJVZoeSbtsozxb4Ck%2F48qXVzyHkg22IWj%2FLDmrvI41N6iaTlzICP64iQt0iA8NTj6QHbqIVM8e9siZtyrLWc5CpHwDXgOeUU0R%2FGTVOaf4voF47n34rHYvm2NPE0p632gEiVeIBWGtFWBKL5LJgNurmOpjARW%2FjeZxI4MK481AdMvhZfy5yJL5KshwapQCAAUGXBVJwC6a5ftUP%2BwKhdbV7fFb4kzudr5UnETm6BpLVQOQ1WXHfLtQy7Qt9h5JYWjzxFSU1D7AgA%2FqLAtODSPaIX2w9TvoQ2wAGqv3OerO5UTCQrs0dV7fpg%2FpeISRUYIdhIP8sB%2FDYQWIr5cV5PJzKN1NRriF6pfNy7xpvzaoyJjzKQx2Esf9US8wbjqiZMrlbkTOCrxe1tu5a7iDHTuXMI7SqtIGOqUBdiuOcbk9kr9xNpxixKv7cFiHIZfAyGDWb5I2eZTqcjSN2ZbBuS%2BLPfCNIvACXUvFr5DmmPeFpd7oJl1oAw4AJQS5cDlZ5kIX7ucbT4bb2Ef9yIFnP8bkXuSQ0FuQI0jREClUjBm4hu793DAXPe0ktkwfGiQK%2F5HbL7zApEu%2FTcqQA9MpwhCpE3L0Ni3R6GE2Vyv9G%2FszH6xXUUdEKfKUQZqTIt6c&X-Amz-Signature=f2fa3fd4ccba1564d3260ad4c844b3a945e6238be71265c55ec5cda81fb057fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW76TZQO%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T190839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFgPP5BVcUQ4sLJ%2BsUsS9BWCTruHNMTfQTnux0kNZJnjAiEAymxoJ509%2BSJPFXzEJyW%2F0I03q3WeaPLuh3FPz7x1jWEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNuPcdhDS89VD8S7iircA%2Fn7ODxe8zzqJEYYmySxzmEWYVPDJ%2F4ssn74pln1GH9oQSNy8KbRK%2FL7nT2Uao%2BlT77oKDW49AYlZVDA4arKhBzXd9Q%2F36hu8Up4WCmOdpojwVYTnFLO5S1TwlR21%2F1hj4VRUvbhYPjiIylIpqwgiPl%2Bc3jwEqCiPR8XRYOc7GzH%2BVy%2FqtwHcelJM%2BHBwJrZguptawhL8MR8Qzwsh8QSKhZrx8D37gjClAi%2BA4OJVZoeSbtsozxb4Ck%2F48qXVzyHkg22IWj%2FLDmrvI41N6iaTlzICP64iQt0iA8NTj6QHbqIVM8e9siZtyrLWc5CpHwDXgOeUU0R%2FGTVOaf4voF47n34rHYvm2NPE0p632gEiVeIBWGtFWBKL5LJgNurmOpjARW%2FjeZxI4MK481AdMvhZfy5yJL5KshwapQCAAUGXBVJwC6a5ftUP%2BwKhdbV7fFb4kzudr5UnETm6BpLVQOQ1WXHfLtQy7Qt9h5JYWjzxFSU1D7AgA%2FqLAtODSPaIX2w9TvoQ2wAGqv3OerO5UTCQrs0dV7fpg%2FpeISRUYIdhIP8sB%2FDYQWIr5cV5PJzKN1NRriF6pfNy7xpvzaoyJjzKQx2Esf9US8wbjqiZMrlbkTOCrxe1tu5a7iDHTuXMI7SqtIGOqUBdiuOcbk9kr9xNpxixKv7cFiHIZfAyGDWb5I2eZTqcjSN2ZbBuS%2BLPfCNIvACXUvFr5DmmPeFpd7oJl1oAw4AJQS5cDlZ5kIX7ucbT4bb2Ef9yIFnP8bkXuSQ0FuQI0jREClUjBm4hu793DAXPe0ktkwfGiQK%2F5HbL7zApEu%2FTcqQA9MpwhCpE3L0Ni3R6GE2Vyv9G%2FszH6xXUUdEKfKUQZqTIt6c&X-Amz-Signature=4e55b761892ad0da79ab127acc4a2544b01d63257588564580f7b810284b8c06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







