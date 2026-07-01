



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGTQDCOD%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T194549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCb4bOssr8tmgOziiHchIUOZVEK5rSSSGQDEHrVdYfeugIhAOZUbprrooX0EBbuqxFQf8YVbhp1pSS6mE4ZOAb%2BnItsKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhbdcziVtZVE9VuXcq3ANIFHGTHVOM%2FvYNcm7ZccBkiqV6qQMuF6326s63WrxUb98a3LH%2BwYghRZAp0o9jgXev43zOp16%2BhEcohSo48Ane%2FocXC%2BvzIxW9TMygbWzQw1DCzvLITyzji7XHlFuKE9SkjqPeG9AH3QsvNUIISvE6nwHdqi1e35ffDe2RJj3kgXOlrcsKD0R4JBEUAOQ3T6qQKH0jdP9O4LcWVLw9nbfZor4%2BUJZusMKuSi3XQSkhWiqvxyLDAQizXDVavdsR%2F694NKoFdmuqVnYtYDhppiez9ZVwEpUFdPCzFhABioRlG4uTOr3EL7vlPs1d4wEkC%2Bz5lBM%2BYbj9%2B5y1taXlw8cH2npUJZI2PlJq99uz4wSWBjXQAPfm56zkBi5zNBSx5qf0gLLfJtDVsCiZoHdH%2BfcX3JhyI8glIvPqI%2BJ8rYRjj6NqgxHGuFDqJ9cdwRgKHGz%2BsIrKeOESMEpjr3xcyMXdB5%2BHHQoKBSTFynNBQlWI3BYC%2FkUwLnugrZQWMJze9HD9bQiQjnsGwU4pju6ptOv7JG8q3cio34US3BoLS9hB5a4XP83bd8qZsVYBNvz9NkfhydWzGifCf8UWXhkfZTXiVrd6XXbvo0I2OkHMyWvm%2Bdyakre5MefN7JqubTC%2F1JXSBjqkAXdsvPUgAKaBfGD6Ay3LFssUegOXfX%2FjJkfCZuHlkppA2P9LFkLwDAZ2fEcnPVu1LdKsPMxa8jpf%2BCWJpuDD6XVfre31LyQKI8X0Bh8eFqrPX4gTIlOfvIju0eI2PY5K7uPnEf%2BR3z%2B3A7qCbOsZUuXiqR3H40KSQI%2FMDTebxprOY3R5Tthkrzki5dAA%2BGVLEEOkpyb55lDUet373431wX2kuIxE&X-Amz-Signature=740cfe0a22080c54f4a6814e3908f1ebdb3b1f3465042a0b3c468900b92e5e6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGTQDCOD%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T194549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCb4bOssr8tmgOziiHchIUOZVEK5rSSSGQDEHrVdYfeugIhAOZUbprrooX0EBbuqxFQf8YVbhp1pSS6mE4ZOAb%2BnItsKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhbdcziVtZVE9VuXcq3ANIFHGTHVOM%2FvYNcm7ZccBkiqV6qQMuF6326s63WrxUb98a3LH%2BwYghRZAp0o9jgXev43zOp16%2BhEcohSo48Ane%2FocXC%2BvzIxW9TMygbWzQw1DCzvLITyzji7XHlFuKE9SkjqPeG9AH3QsvNUIISvE6nwHdqi1e35ffDe2RJj3kgXOlrcsKD0R4JBEUAOQ3T6qQKH0jdP9O4LcWVLw9nbfZor4%2BUJZusMKuSi3XQSkhWiqvxyLDAQizXDVavdsR%2F694NKoFdmuqVnYtYDhppiez9ZVwEpUFdPCzFhABioRlG4uTOr3EL7vlPs1d4wEkC%2Bz5lBM%2BYbj9%2B5y1taXlw8cH2npUJZI2PlJq99uz4wSWBjXQAPfm56zkBi5zNBSx5qf0gLLfJtDVsCiZoHdH%2BfcX3JhyI8glIvPqI%2BJ8rYRjj6NqgxHGuFDqJ9cdwRgKHGz%2BsIrKeOESMEpjr3xcyMXdB5%2BHHQoKBSTFynNBQlWI3BYC%2FkUwLnugrZQWMJze9HD9bQiQjnsGwU4pju6ptOv7JG8q3cio34US3BoLS9hB5a4XP83bd8qZsVYBNvz9NkfhydWzGifCf8UWXhkfZTXiVrd6XXbvo0I2OkHMyWvm%2Bdyakre5MefN7JqubTC%2F1JXSBjqkAXdsvPUgAKaBfGD6Ay3LFssUegOXfX%2FjJkfCZuHlkppA2P9LFkLwDAZ2fEcnPVu1LdKsPMxa8jpf%2BCWJpuDD6XVfre31LyQKI8X0Bh8eFqrPX4gTIlOfvIju0eI2PY5K7uPnEf%2BR3z%2B3A7qCbOsZUuXiqR3H40KSQI%2FMDTebxprOY3R5Tthkrzki5dAA%2BGVLEEOkpyb55lDUet373431wX2kuIxE&X-Amz-Signature=0d6ad3717f0a19bda36d2bed1274f7c7daf8745d27841ca052b2917dab623cae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







