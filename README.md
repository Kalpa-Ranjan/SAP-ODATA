



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVMAOGUA%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T124546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHwFGJKR8Ti2p%2B1F4khMMPY7z0ymJ9SvkI6nphsQTNB5AiEAtnWC%2FlRZwh9lE6%2Fb9NdHGM2BUNrm8KRpIN2DkyUTLywq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDFe4E5PTQU6EiMDSXCrcAyqCXpUqpapmv5clgwl%2FrHwa0%2Fk%2Fb5oB0VM%2BCA7m95dYci%2FalV%2FUfI3%2FZ6vQxD7zPygxtldwHUFC5la6CVSVstI39i4mp41tpdwvKPZyoiDQPJ7RyJcjnq2dxK59p4Iy0qfgGmmxkiJz8r%2BQxs%2BXbvEFIBFa9BO3GaPlMW57qSorfNMJYfGIwnNotIkWm5lvVnT7HPKvnPsl1oXCmlVviVXoqQWXYTCUSEY3WR3bGBwOBOufjvtkgSYLB%2BvSn%2BW5Qpdx6Fg5w7FW302NBc4t2eF6uNDEV6LZQ2uNezv52GWDRkSnvEKPs2N%2Ffio67XszOYhQ0h9m%2FnXyfu4otea159SecyrX2RvEDye0tiDyFws6%2Beu%2FU6IXu1P0bc97TQmL1zMsd8uWU0MSS%2F2lc0r61D1bbsrXOKZ9Yn8Nqmf6OIrRs5MDBRh19sczmOCr7au0aiEU3FcXvcxZCn0kXKSULBFoEvHtlxvzkCpAjyEvMtoThWTtjZR2uiAskXyqrKQlW%2FHWEEKRrwdo%2FH0WQtPc1VaO64xxySSjgDoTH7L%2F3wQQ2BdSD4d0xFB194UiI2PA%2BTyKhHUlkBmF%2B5uLQrcPuqJJmYS99QmMYWZgNrKJfqxFt%2FJMs53XR4sZ%2B4v1MKPH6M4GOqUBsx1LG7rqs5OtzTzXU792uCauFpc2j3yWBUReyZ%2F1im709EpQe4X4OMlVT8Iedvv4lO%2FGwLEtybD2zPiV6sjbvO3I660sj5ryoAItVdhzyuykiLK2RXPeqKJxzvq5JrjxRo0qs3TmIACakHtDBgmutsLyL09bUoGmaCXKMsCLPpxBEDP%2FJlkEWmuIP6HxJ32Z8ykkniF8Q4bRbY4O3VZsv4Td6dPg&X-Amz-Signature=0927510881c6ce5f2a34b6f1b5a492c28dc3520f4702cff67d49daecbeaa626e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVMAOGUA%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T124546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHwFGJKR8Ti2p%2B1F4khMMPY7z0ymJ9SvkI6nphsQTNB5AiEAtnWC%2FlRZwh9lE6%2Fb9NdHGM2BUNrm8KRpIN2DkyUTLywq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDFe4E5PTQU6EiMDSXCrcAyqCXpUqpapmv5clgwl%2FrHwa0%2Fk%2Fb5oB0VM%2BCA7m95dYci%2FalV%2FUfI3%2FZ6vQxD7zPygxtldwHUFC5la6CVSVstI39i4mp41tpdwvKPZyoiDQPJ7RyJcjnq2dxK59p4Iy0qfgGmmxkiJz8r%2BQxs%2BXbvEFIBFa9BO3GaPlMW57qSorfNMJYfGIwnNotIkWm5lvVnT7HPKvnPsl1oXCmlVviVXoqQWXYTCUSEY3WR3bGBwOBOufjvtkgSYLB%2BvSn%2BW5Qpdx6Fg5w7FW302NBc4t2eF6uNDEV6LZQ2uNezv52GWDRkSnvEKPs2N%2Ffio67XszOYhQ0h9m%2FnXyfu4otea159SecyrX2RvEDye0tiDyFws6%2Beu%2FU6IXu1P0bc97TQmL1zMsd8uWU0MSS%2F2lc0r61D1bbsrXOKZ9Yn8Nqmf6OIrRs5MDBRh19sczmOCr7au0aiEU3FcXvcxZCn0kXKSULBFoEvHtlxvzkCpAjyEvMtoThWTtjZR2uiAskXyqrKQlW%2FHWEEKRrwdo%2FH0WQtPc1VaO64xxySSjgDoTH7L%2F3wQQ2BdSD4d0xFB194UiI2PA%2BTyKhHUlkBmF%2B5uLQrcPuqJJmYS99QmMYWZgNrKJfqxFt%2FJMs53XR4sZ%2B4v1MKPH6M4GOqUBsx1LG7rqs5OtzTzXU792uCauFpc2j3yWBUReyZ%2F1im709EpQe4X4OMlVT8Iedvv4lO%2FGwLEtybD2zPiV6sjbvO3I660sj5ryoAItVdhzyuykiLK2RXPeqKJxzvq5JrjxRo0qs3TmIACakHtDBgmutsLyL09bUoGmaCXKMsCLPpxBEDP%2FJlkEWmuIP6HxJ32Z8ykkniF8Q4bRbY4O3VZsv4Td6dPg&X-Amz-Signature=bcbbb10effc943f25bd992c17c85d0cda10ee8149068ba4852bd6d62c1a718d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







