



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6S3RGOO%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T021314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIEXrzb1zIK315VOxIVD7Y3569A7zzVHXoFSaovn0%2BWOYAiEAndCDcDEGQU6ZJVmcl6oNYQWAOLF9APBsDhNQ0JVdqc0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwgHKp5t6aNlTdanCrcA%2BKfHXYpVk4mnsh2cvrReTMkiUIkzN9Y8y7wlqTdQ8be4AdemQxfdMnZ7cMXjfwpATBRsbonCdaUy6y7%2Bu3s%2FLDiQFUu0IPRXz5N9enbXH9eAHAqQnfKR2DLnKIHXcKk3e7zWhkY7PSUAYqWtqAgMm6vWS7H8axsMG9IRJnw7Ukq4ZIEsCH6EAzW8TcjOkvxhxpeP1H2MXs1cZB8JZhe0ZB1tMMF65Y1KKhTX7Xte%2FN4b5gpurRIDICHVa7GlgbTCauuM0%2BAA115EAAatKdmSQH67%2B8tpZBLbXkkSt%2FlEOClEstZahXGwNlQJxCc0DtYfQdB%2BFd2qdscGd2ohGKr7MWGoKWjFpYL2nPs93JnQO2t6RRmL2f6%2BtqDYRr3ObqRXZf%2F6bqWoCUSxxqwXCE9hiI0TvEJ%2FRE6VVn%2F0bX%2BqyLYEShL7FrLvXdeP%2BTBDP8At4pStPNG1kXw9mPxxiKBtSiysDrlVIMwjUu1ModyfUGsJDE7CaflvmeKgCM%2F4CVcqV5G9ujNLX8IzfQA85dTGSLJGXsgPKamKvTlCrfF1dHwDpe6Gs2qmu9kzFC6GFzyJdNoCrvHoF2lKIfV%2BprqM0WHE9Gxxc7UciCcFYG4f6r9TyXGsa%2F7%2BseDMKrMMMu80NIGOqUBlefluKCAtbJ57XAPefhzxjdg348MsMKp2YohScKBmpcgRNnMdnzTOyWfT1jJXE2Hxmcgl6RV8c1TD6XNBB3iuXiySWQXDEXED8B%2F0fyyRmE4hStDI3FpxCdIkAM1kNDGspIx1qfRzlHm8mvSkQ9qwCTBOB2jiQcxhWJdTAW5altO%2F6Bi2NCamujycAJsUaPQ4wlopur%2F11YqG38Bm4KgbGde00va&X-Amz-Signature=1783932a221c6a8fb294424db7bbf89aded83e08c761e24261c9e75b62e2ac1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6S3RGOO%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T021314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIEXrzb1zIK315VOxIVD7Y3569A7zzVHXoFSaovn0%2BWOYAiEAndCDcDEGQU6ZJVmcl6oNYQWAOLF9APBsDhNQ0JVdqc0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwgHKp5t6aNlTdanCrcA%2BKfHXYpVk4mnsh2cvrReTMkiUIkzN9Y8y7wlqTdQ8be4AdemQxfdMnZ7cMXjfwpATBRsbonCdaUy6y7%2Bu3s%2FLDiQFUu0IPRXz5N9enbXH9eAHAqQnfKR2DLnKIHXcKk3e7zWhkY7PSUAYqWtqAgMm6vWS7H8axsMG9IRJnw7Ukq4ZIEsCH6EAzW8TcjOkvxhxpeP1H2MXs1cZB8JZhe0ZB1tMMF65Y1KKhTX7Xte%2FN4b5gpurRIDICHVa7GlgbTCauuM0%2BAA115EAAatKdmSQH67%2B8tpZBLbXkkSt%2FlEOClEstZahXGwNlQJxCc0DtYfQdB%2BFd2qdscGd2ohGKr7MWGoKWjFpYL2nPs93JnQO2t6RRmL2f6%2BtqDYRr3ObqRXZf%2F6bqWoCUSxxqwXCE9hiI0TvEJ%2FRE6VVn%2F0bX%2BqyLYEShL7FrLvXdeP%2BTBDP8At4pStPNG1kXw9mPxxiKBtSiysDrlVIMwjUu1ModyfUGsJDE7CaflvmeKgCM%2F4CVcqV5G9ujNLX8IzfQA85dTGSLJGXsgPKamKvTlCrfF1dHwDpe6Gs2qmu9kzFC6GFzyJdNoCrvHoF2lKIfV%2BprqM0WHE9Gxxc7UciCcFYG4f6r9TyXGsa%2F7%2BseDMKrMMMu80NIGOqUBlefluKCAtbJ57XAPefhzxjdg348MsMKp2YohScKBmpcgRNnMdnzTOyWfT1jJXE2Hxmcgl6RV8c1TD6XNBB3iuXiySWQXDEXED8B%2F0fyyRmE4hStDI3FpxCdIkAM1kNDGspIx1qfRzlHm8mvSkQ9qwCTBOB2jiQcxhWJdTAW5altO%2F6Bi2NCamujycAJsUaPQ4wlopur%2F11YqG38Bm4KgbGde00va&X-Amz-Signature=6998e62515cc7307cb9aaa049e6c0d47df73b2ec41c653416f5b14b12ea094b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







