



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4BNDTZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T122951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQDpgbD3SWeWDFN%2BiZA8Ble%2Bughd8lsJM%2BnJaGBb4tnrVgIgbyN%2FvJG7qB6n0KGLu3vpSVdsFbGqI3dALvG2B7qJlN4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDP0wQ0gLqv%2B939a7pCrcA9nmEyA7rd7SIK3D24fwsH42NnmhyYaqeFk6hHRkhu731rlggEz5Mwd4zVVP19cmuSK6%2BgNcAGxMTVB9A2T%2FdPLy29SyGl3OH5ExR5J753KkRuc8S%2BvAbZrd6nYQZ%2B45%2BNQTVO3YSX1Lh8MwEQcGUSdTUSUMHgFz9sNuO0PpVC30jak%2BR4KQc8y69ZdXOt3kPUCO6r4bGeTrow8IihY36cb9YAegds%2Bj7O1VMtswev2kacMRZswm0QakvhB61QFhtsHhlGq7dPUSgTbo1B1NKWbSE4ML2DZ95SJeDp6uYshRnA%2BiOL3fWh2LkajCiJCZSOyrztQdvGZr4BuqAotq7zLS%2B%2F7RnrMU6Ik6acoxKz3vYLZ%2B2xi%2FNpZd%2FOgYPsBKI44Aq6EPIwtZa3Xrr2wYImidCorBRm1BSIMggbaKjWJ9GOVkglOllGXVu5O5YKhAs%2BaVhwFDoRU884PWe6ofZzdTFivnwbTQVm0%2F7uPgYM9uE2dTF%2BxOZ3xe6o4Wi2IUhnsALm%2Bzv0l0c1CJ70BNTo6OHIIRZwYwHZ6lrrbMqD1aZ1MTqxywB0b0XQnHLmDr7aDZyRHJ71rwU2sNXlQmZ7kApsOxDJ0sNrXKtVQ0Xn%2FZmeOkqg6kk8jLCDr7MPqY9ckGOqUBokubC%2FoAgb47%2BsclkWqUI6uMFc6%2BaPRYeU98ANK2CDdrLTYi%2BKftju4iVFrCSKq8ycEpgryGzKGUF6PLEr89hx3q0VJz2Ndxi7QX302WrV1j82o%2BhnAyfCsQQ6q65ehloKJPlDEbDJgwzl%2FQspOyZg6Okp7oWWEzoaS9ChOsUyyX0NTmoKI86DbKyFYEr0plB9qcwmmk0Ac35GrTtmbbQrAPOyKF&X-Amz-Signature=61d2968c02b98496bd5f2f14398fe9426ffd01f28bfc9c85a52cc65f1ffee951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4BNDTZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T122952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQDpgbD3SWeWDFN%2BiZA8Ble%2Bughd8lsJM%2BnJaGBb4tnrVgIgbyN%2FvJG7qB6n0KGLu3vpSVdsFbGqI3dALvG2B7qJlN4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDP0wQ0gLqv%2B939a7pCrcA9nmEyA7rd7SIK3D24fwsH42NnmhyYaqeFk6hHRkhu731rlggEz5Mwd4zVVP19cmuSK6%2BgNcAGxMTVB9A2T%2FdPLy29SyGl3OH5ExR5J753KkRuc8S%2BvAbZrd6nYQZ%2B45%2BNQTVO3YSX1Lh8MwEQcGUSdTUSUMHgFz9sNuO0PpVC30jak%2BR4KQc8y69ZdXOt3kPUCO6r4bGeTrow8IihY36cb9YAegds%2Bj7O1VMtswev2kacMRZswm0QakvhB61QFhtsHhlGq7dPUSgTbo1B1NKWbSE4ML2DZ95SJeDp6uYshRnA%2BiOL3fWh2LkajCiJCZSOyrztQdvGZr4BuqAotq7zLS%2B%2F7RnrMU6Ik6acoxKz3vYLZ%2B2xi%2FNpZd%2FOgYPsBKI44Aq6EPIwtZa3Xrr2wYImidCorBRm1BSIMggbaKjWJ9GOVkglOllGXVu5O5YKhAs%2BaVhwFDoRU884PWe6ofZzdTFivnwbTQVm0%2F7uPgYM9uE2dTF%2BxOZ3xe6o4Wi2IUhnsALm%2Bzv0l0c1CJ70BNTo6OHIIRZwYwHZ6lrrbMqD1aZ1MTqxywB0b0XQnHLmDr7aDZyRHJ71rwU2sNXlQmZ7kApsOxDJ0sNrXKtVQ0Xn%2FZmeOkqg6kk8jLCDr7MPqY9ckGOqUBokubC%2FoAgb47%2BsclkWqUI6uMFc6%2BaPRYeU98ANK2CDdrLTYi%2BKftju4iVFrCSKq8ycEpgryGzKGUF6PLEr89hx3q0VJz2Ndxi7QX302WrV1j82o%2BhnAyfCsQQ6q65ehloKJPlDEbDJgwzl%2FQspOyZg6Okp7oWWEzoaS9ChOsUyyX0NTmoKI86DbKyFYEr0plB9qcwmmk0Ac35GrTtmbbQrAPOyKF&X-Amz-Signature=98071832777289e403d97c997f75b29442ede3faa6f26465a1289440e29b7913&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







