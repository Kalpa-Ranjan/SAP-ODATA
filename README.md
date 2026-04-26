



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN3K5F65%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T125605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQGcOLy1YWFIeuwTU6preSqAXaMeKPmOln0lkauoBaEAiA%2FStVP86dez88h4Yv7H0d5DLgw8XCDHt9zJDoBFej8JyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLFaw3Tpnlcy1IPgKtwD9b%2FlVrI1BgcQjTw6bgsEO1wgEPpGYcLlNiDvWIA2pK%2Fx5IJ2hPqTdYvxNj06p7H1EGbBcS4dW8LYQM3hnLNLCr7LeGR1%2B7n5cW3WhW4jDpUnbHt%2FwM%2B14T7lnqsOlYYP2MRKqXij2U0QUHEvMYsPrv5vJMO2lHDYdRe7BBgiG0B5bhrcV0ddXezp6JmHQXndIlmCw8BE1kzkv%2BZFpQHYiPiUZcDZkB3RcAw0kY39onTVihNBmOw4V1s04SX7pgKMUZnKYx1WpBSHah7rs980N7%2FudEQlGj1zqKUpSN9V9%2F13ZoRXVm52ovXnDW5j5rE%2B40ztH92i%2FEd1pbwoKMAU%2F0610PMalUDL3LibkzQTZ6D5PegLItN2b%2FUDY0sPtFiEgdArRxkTUpDf2pFJgtIAxAnCE083ZH%2BEH2IXaYyeKERrrn9gFrk5KpZYrniKKt%2FDlaOf%2FUSLX1pPrwbvdKH%2F5H8rEq7pzhQ53ABgAfN0iWckMd9smlWV5cJbLaoZZlmw0IfW4BTaR3hmSZYqdfe%2FvEFYJgIKAQS0ZOGtJNGA4gJRmTOCBflq2%2BMKC9win2KbbG9zWPWYsfOt6jjTds7%2B8QzXD%2FuOIyzTRXytZ%2Bf2cu5EwWso7XBf%2B7F5Qt4wuvS2zwY6pgGuT9s214iAM0HEVucRzGuqkXNdULHUZpHDZ28oFWVBXvfP9%2FhPaxKBFDRvgBz0fCstwIzhmBJEYR1hcL50rOHw4v%2BWZ5LqK7aKve615S14JBEE3pTYKubcf4JW%2FO68SioKiVe8xgnr%2FCpK9GKQYrudZKfZDjcJyYXmMrmXRBwv1dwbSS7p6y3%2FjDJpqVJrSksXvWpgU26xDkdKkUpd5XOqWTWMVQfq&X-Amz-Signature=33266d1364e1f78d67eb3e8aad59238c63a02c52bf35895308b425b713e5e775&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN3K5F65%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T125605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQGcOLy1YWFIeuwTU6preSqAXaMeKPmOln0lkauoBaEAiA%2FStVP86dez88h4Yv7H0d5DLgw8XCDHt9zJDoBFej8JyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLFaw3Tpnlcy1IPgKtwD9b%2FlVrI1BgcQjTw6bgsEO1wgEPpGYcLlNiDvWIA2pK%2Fx5IJ2hPqTdYvxNj06p7H1EGbBcS4dW8LYQM3hnLNLCr7LeGR1%2B7n5cW3WhW4jDpUnbHt%2FwM%2B14T7lnqsOlYYP2MRKqXij2U0QUHEvMYsPrv5vJMO2lHDYdRe7BBgiG0B5bhrcV0ddXezp6JmHQXndIlmCw8BE1kzkv%2BZFpQHYiPiUZcDZkB3RcAw0kY39onTVihNBmOw4V1s04SX7pgKMUZnKYx1WpBSHah7rs980N7%2FudEQlGj1zqKUpSN9V9%2F13ZoRXVm52ovXnDW5j5rE%2B40ztH92i%2FEd1pbwoKMAU%2F0610PMalUDL3LibkzQTZ6D5PegLItN2b%2FUDY0sPtFiEgdArRxkTUpDf2pFJgtIAxAnCE083ZH%2BEH2IXaYyeKERrrn9gFrk5KpZYrniKKt%2FDlaOf%2FUSLX1pPrwbvdKH%2F5H8rEq7pzhQ53ABgAfN0iWckMd9smlWV5cJbLaoZZlmw0IfW4BTaR3hmSZYqdfe%2FvEFYJgIKAQS0ZOGtJNGA4gJRmTOCBflq2%2BMKC9win2KbbG9zWPWYsfOt6jjTds7%2B8QzXD%2FuOIyzTRXytZ%2Bf2cu5EwWso7XBf%2B7F5Qt4wuvS2zwY6pgGuT9s214iAM0HEVucRzGuqkXNdULHUZpHDZ28oFWVBXvfP9%2FhPaxKBFDRvgBz0fCstwIzhmBJEYR1hcL50rOHw4v%2BWZ5LqK7aKve615S14JBEE3pTYKubcf4JW%2FO68SioKiVe8xgnr%2FCpK9GKQYrudZKfZDjcJyYXmMrmXRBwv1dwbSS7p6y3%2FjDJpqVJrSksXvWpgU26xDkdKkUpd5XOqWTWMVQfq&X-Amz-Signature=a7e6285de4013e2331e454a8905b52ef9e2e744cfb17b202279da690a7347732&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







