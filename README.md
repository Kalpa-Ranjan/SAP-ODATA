



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XXWBSI6%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T191235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqHWNxk16uAGroEJs2dkjHkl9N8VLnxCMTuqi%2BMNlyzgIgENMy4C%2B7g8wq00senY%2FKVUkDGRzUR7qI3h97XBe0YbEqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5%2FdN8v4Mes69IiRyrcAzP63cCfdYgD0W9bL8ZSFwpTXLfbYJlDph7tEWlsREwNHTUtTf6%2FR%2F%2FzvoC0JoUzXo3iTnZuc6cXoLtOuSHM%2B4%2Bej9zAixu6SZt3BjW0OuGX%2Bl5UdUOkPbl4KRVhwK5rvykI25NqG5aj17VYv%2FVCUDJM7mI1oPAlih2zmXRa7PWqrn6SiTOefPv7Z2Np1e2zm1BTxuFeX8xbl0Ota15f8Nc4Txv1vNW5DzYjlSySab2jU%2FdScJrXMwefLZh3YTeBMtK14OCsKYvKlrCUI5TW%2Fm%2FZCIIchjMe36Ysl6DKYiDBV9fs8TQY8V7JauE2NCt1kRu%2B2uKYUSGbbz%2F0k82uVVyLZNQxHe9kA2V4QnBX2F3gwAVwAKQ2CopaFbKjAcOGjHaM9ezHA%2Bum9PNAIot9epmydc824TEzgzV4SE5SjjTAyIgw%2FSbM0tvJygCLeVZQbyM2kcqKahYZcPen%2F9bltGjhv0amSHyjeXnU1CMCvGCmdPIzVWMKzFm83396o%2FW0D90bwqhOp0FUporHYaNtLJHcbqHF%2BGbD1d2zROUHu3rppJfrSQE6t8br5k9iO88IVEHYLBx0HmbipC4nReQBkp9MmLZM63Yr93%2BF00BsDGaYnBkKJjhQOGaxkXzlMMeZgNIGOqUBs0R4PQYhTkcrGMDFpslW18oCDRR6PoLjzdnId02DM6n2iTF%2BzitD4Y5RamRkQ%2FFIX7YIDbR1ZTCwloHNoxs0EVkYTbA5esGwHMjrDA1f5Ddi2DGL9P6415TKoqMK3qSglBo0OoO2FUhAmQ7V7VvAk3ICd9%2Fmz8Ob%2Fu4RwlaNXO%2FBoWj6awUPM6ues2fXWUV%2Bf2QNJhmwuxQ%2Bg7rycaD0OTtw53LA&X-Amz-Signature=27b15b09da61cf37266cfae3e05be2cbb6360214b2d8b602ee805b2220efb699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XXWBSI6%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T191236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqHWNxk16uAGroEJs2dkjHkl9N8VLnxCMTuqi%2BMNlyzgIgENMy4C%2B7g8wq00senY%2FKVUkDGRzUR7qI3h97XBe0YbEqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5%2FdN8v4Mes69IiRyrcAzP63cCfdYgD0W9bL8ZSFwpTXLfbYJlDph7tEWlsREwNHTUtTf6%2FR%2F%2FzvoC0JoUzXo3iTnZuc6cXoLtOuSHM%2B4%2Bej9zAixu6SZt3BjW0OuGX%2Bl5UdUOkPbl4KRVhwK5rvykI25NqG5aj17VYv%2FVCUDJM7mI1oPAlih2zmXRa7PWqrn6SiTOefPv7Z2Np1e2zm1BTxuFeX8xbl0Ota15f8Nc4Txv1vNW5DzYjlSySab2jU%2FdScJrXMwefLZh3YTeBMtK14OCsKYvKlrCUI5TW%2Fm%2FZCIIchjMe36Ysl6DKYiDBV9fs8TQY8V7JauE2NCt1kRu%2B2uKYUSGbbz%2F0k82uVVyLZNQxHe9kA2V4QnBX2F3gwAVwAKQ2CopaFbKjAcOGjHaM9ezHA%2Bum9PNAIot9epmydc824TEzgzV4SE5SjjTAyIgw%2FSbM0tvJygCLeVZQbyM2kcqKahYZcPen%2F9bltGjhv0amSHyjeXnU1CMCvGCmdPIzVWMKzFm83396o%2FW0D90bwqhOp0FUporHYaNtLJHcbqHF%2BGbD1d2zROUHu3rppJfrSQE6t8br5k9iO88IVEHYLBx0HmbipC4nReQBkp9MmLZM63Yr93%2BF00BsDGaYnBkKJjhQOGaxkXzlMMeZgNIGOqUBs0R4PQYhTkcrGMDFpslW18oCDRR6PoLjzdnId02DM6n2iTF%2BzitD4Y5RamRkQ%2FFIX7YIDbR1ZTCwloHNoxs0EVkYTbA5esGwHMjrDA1f5Ddi2DGL9P6415TKoqMK3qSglBo0OoO2FUhAmQ7V7VvAk3ICd9%2Fmz8Ob%2Fu4RwlaNXO%2FBoWj6awUPM6ues2fXWUV%2Bf2QNJhmwuxQ%2Bg7rycaD0OTtw53LA&X-Amz-Signature=c29ef5852128fb5cace4bfd5bb9bef28b3d48532ba1620b6cad922402bb9a7b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







