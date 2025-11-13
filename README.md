



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRGGO2JG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T011310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCICZpHDL534KczBQhps%2Bd9%2BvRgixtW1vlplhafZGiaMnDAiEAuocF8QRiQboe7z5D2CjQESs5VZD9LpzJrxoKtRrtOVMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKPKrND9hyN7%2BskwVircA3%2FSmkfB250wzY%2BK9LjiAvBjcz8RuVnvPScN4Wtr1atK1iTMZuQ29JI4svm55jR3WenZ5C6b7Ngx91yTQQrZKD7ygrtIqrayenHvjUOcbXjsJglO2qNGpTYDc3QvrOvmTiZZGDox39O%2FAoqH93FWgWrawekejIrTJH4nyuA46hZ%2BnUGqXBRSgzf9fdAaQvmzaZHpOgGKEAELGOxw8SCZ%2F2ezzqZDqSF74%2BCCx4B55gJwgWH2yi61cbl93TgC69g%2FnJvX1KDI%2FaPQYQsw1y181hDpEoDIBJ%2F2vQMFp%2Fr6K5CRiH5UZhCem2HEJYyjE5MDRqsgi3GugM3STK1kL%2Bnc1TPNWLapxIRs6LHzJbTOMCq%2FqokvCZiD8%2FMz85DRQU%2BjbkxNOZriYW7Tjexmwz9Jm8%2FjI%2FuxWd05AIBw%2BBcrO0tfR2Mf%2F73JatiklEKQYKoXEMfSJA%2BIz73VEDHa7SSXwKmXM2aAVqztnqe6JyrRIrYb7L8HElPQ%2FyG%2FkiYIQr5IyBkHOCCFsXmsyTkUNFJzXvC23vtXhLOxXp6yVzwMmfxMDnIOOuZ9vhC1u2vh0BjT3XvNkq%2BCrTThM92xgpbxT0qUvI0g27ZJsFJcPIL%2F5I%2FpUYsoqWlbGiS%2BxFxGMN%2FO1MgGOqUBnCOdW3IKmrH2frAwtHBFXBQLdyfxv5LFjmTkOAOJ5ao1GqclTridf5D6MH8d2hfHkpCBHsz6%2BLrw6ng0ttzVTAJa27NzrwrtS%2FWKYZukihBHkTXMqIMA%2B9baj1md%2B%2FPoQ8q1Ahn2QBEiTefiM5NBxb%2FZRm6DHQUZmMK6kIs2X2VjOY9TCG2%2FuHzgibGU9B7oW3iGJ3QvKTo2XS5yhI6X%2FtFafGjc&X-Amz-Signature=b57615c003deca39a4e7d401dc8e7503b73203bc384110259b803372e04f8722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRGGO2JG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T011310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCICZpHDL534KczBQhps%2Bd9%2BvRgixtW1vlplhafZGiaMnDAiEAuocF8QRiQboe7z5D2CjQESs5VZD9LpzJrxoKtRrtOVMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKPKrND9hyN7%2BskwVircA3%2FSmkfB250wzY%2BK9LjiAvBjcz8RuVnvPScN4Wtr1atK1iTMZuQ29JI4svm55jR3WenZ5C6b7Ngx91yTQQrZKD7ygrtIqrayenHvjUOcbXjsJglO2qNGpTYDc3QvrOvmTiZZGDox39O%2FAoqH93FWgWrawekejIrTJH4nyuA46hZ%2BnUGqXBRSgzf9fdAaQvmzaZHpOgGKEAELGOxw8SCZ%2F2ezzqZDqSF74%2BCCx4B55gJwgWH2yi61cbl93TgC69g%2FnJvX1KDI%2FaPQYQsw1y181hDpEoDIBJ%2F2vQMFp%2Fr6K5CRiH5UZhCem2HEJYyjE5MDRqsgi3GugM3STK1kL%2Bnc1TPNWLapxIRs6LHzJbTOMCq%2FqokvCZiD8%2FMz85DRQU%2BjbkxNOZriYW7Tjexmwz9Jm8%2FjI%2FuxWd05AIBw%2BBcrO0tfR2Mf%2F73JatiklEKQYKoXEMfSJA%2BIz73VEDHa7SSXwKmXM2aAVqztnqe6JyrRIrYb7L8HElPQ%2FyG%2FkiYIQr5IyBkHOCCFsXmsyTkUNFJzXvC23vtXhLOxXp6yVzwMmfxMDnIOOuZ9vhC1u2vh0BjT3XvNkq%2BCrTThM92xgpbxT0qUvI0g27ZJsFJcPIL%2F5I%2FpUYsoqWlbGiS%2BxFxGMN%2FO1MgGOqUBnCOdW3IKmrH2frAwtHBFXBQLdyfxv5LFjmTkOAOJ5ao1GqclTridf5D6MH8d2hfHkpCBHsz6%2BLrw6ng0ttzVTAJa27NzrwrtS%2FWKYZukihBHkTXMqIMA%2B9baj1md%2B%2FPoQ8q1Ahn2QBEiTefiM5NBxb%2FZRm6DHQUZmMK6kIs2X2VjOY9TCG2%2FuHzgibGU9B7oW3iGJ3QvKTo2XS5yhI6X%2FtFafGjc&X-Amz-Signature=f58ced49d8fc1ac08dc1e02f2f8688cc9c643823a20d96a913ef9ea4d171a52a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







