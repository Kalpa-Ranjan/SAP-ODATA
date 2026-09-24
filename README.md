



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676VKDO2B%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T180934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIE2t0wpQ5fjHAPacR16iUwQj4MmvCvi%2BXtda%2F2J5q6PRAiAeKQQtp%2FqjTO7Rov3aspAvhg030NnQcZ7u8hdyhYA9giqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMt9DLNCxNMTylNTpoKtwDopeXMlngX6lLkAFQmDP66eczW2AIn0Rw4KG0A6QTgpeVnNhOmN9Z7VImqVlba3RqtoitdkCb1%2F%2B2oR%2BMQ%2BCepAF6jzoB7HtgASCmddINLohAZxVJqINgrfa4sYBKlsw7Mo8cOTQvWzfv3A6Ywv6cDI%2FqMl8dG0IxgqDmn0i0yZ6AwnEkzOnO4Afm4ke1uJZQ4FHNo1d7w9Mc5fNpEjJV2k0vl7xA10UyE44dkIVHv75SpndZfLjeW6kSg44Thx9NoqHROchZYLGtV5Go%2BiqyMKNXgv2466JdoaX9k6HWndViU3oNv7lAr8cl6UZr0On2F5VeRpUUy%2F2NQ5VXnxj0gRRI1Kn7fG%2F2u3y8FubGYTpaH8%2Fkxi2qqjejloI7ojSQtGgcRLftR5WmUQuNB79zxBuiiDrybuiTPba0qEjQo3J%2FHUlNp0tJU%2By1Wq6trvM1N2%2BdCA5qQM0uvPZjWU2bkgjMPmtDiUr0J4v%2BpNLYN6NPAEksNkAHFaB40CD1prWDrCQfvQLMhRl%2BdpKYUPQhjN3Va%2BS84Hafjx0zr%2FvBO%2BHBFO94KWodRJ0Zd%2Bz7Z2fFtOAbT4ZbtW1JIHN3EU7nzHPx1lA0nvZxssqT0m6H2eoOTrdsYCZ%2FFn1dzHkwlqjV1QY6pgEqdJz%2FQ%2BjGRgi4XZ%2BqwoZihuvIhbwu3L15r37fycZDSd10WN3wfB8mkAHOO6%2Bcu%2FdQj7kY%2FlDwfx2xq1bBT2nwBGIAhE6A1cTlvmg5vVba0kVHMWbSizsXXFFLY4RBD2k3cRmTizy4pePMvaLfUvnuCaftpPhhtcAV3DTwc%2FVufqNK0SHPypxiHUcRC02iSKwvAr0mH%2Blg42I22pWVkJP3DzxnjGYi&X-Amz-Signature=fc3534e4c754a59dfc7678970737a37c47d2fbf32c5d61e07aabd10f8dbb57df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676VKDO2B%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T180934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIE2t0wpQ5fjHAPacR16iUwQj4MmvCvi%2BXtda%2F2J5q6PRAiAeKQQtp%2FqjTO7Rov3aspAvhg030NnQcZ7u8hdyhYA9giqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMt9DLNCxNMTylNTpoKtwDopeXMlngX6lLkAFQmDP66eczW2AIn0Rw4KG0A6QTgpeVnNhOmN9Z7VImqVlba3RqtoitdkCb1%2F%2B2oR%2BMQ%2BCepAF6jzoB7HtgASCmddINLohAZxVJqINgrfa4sYBKlsw7Mo8cOTQvWzfv3A6Ywv6cDI%2FqMl8dG0IxgqDmn0i0yZ6AwnEkzOnO4Afm4ke1uJZQ4FHNo1d7w9Mc5fNpEjJV2k0vl7xA10UyE44dkIVHv75SpndZfLjeW6kSg44Thx9NoqHROchZYLGtV5Go%2BiqyMKNXgv2466JdoaX9k6HWndViU3oNv7lAr8cl6UZr0On2F5VeRpUUy%2F2NQ5VXnxj0gRRI1Kn7fG%2F2u3y8FubGYTpaH8%2Fkxi2qqjejloI7ojSQtGgcRLftR5WmUQuNB79zxBuiiDrybuiTPba0qEjQo3J%2FHUlNp0tJU%2By1Wq6trvM1N2%2BdCA5qQM0uvPZjWU2bkgjMPmtDiUr0J4v%2BpNLYN6NPAEksNkAHFaB40CD1prWDrCQfvQLMhRl%2BdpKYUPQhjN3Va%2BS84Hafjx0zr%2FvBO%2BHBFO94KWodRJ0Zd%2Bz7Z2fFtOAbT4ZbtW1JIHN3EU7nzHPx1lA0nvZxssqT0m6H2eoOTrdsYCZ%2FFn1dzHkwlqjV1QY6pgEqdJz%2FQ%2BjGRgi4XZ%2BqwoZihuvIhbwu3L15r37fycZDSd10WN3wfB8mkAHOO6%2Bcu%2FdQj7kY%2FlDwfx2xq1bBT2nwBGIAhE6A1cTlvmg5vVba0kVHMWbSizsXXFFLY4RBD2k3cRmTizy4pePMvaLfUvnuCaftpPhhtcAV3DTwc%2FVufqNK0SHPypxiHUcRC02iSKwvAr0mH%2Blg42I22pWVkJP3DzxnjGYi&X-Amz-Signature=d44cbc2d9b69c40d0710e4fc98c5fe292e9691b40d1584c6b308086273568275&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







