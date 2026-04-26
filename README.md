



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHWJZR4V%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T184316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcclSsEhzwSlo4s%2BHeeM%2Fss%2Fvo8sN7368k4QP0ltl%2B4AiBR%2FFsZgJfrvfmZ9dTkj6SO1Z9ve%2FCoqnA%2Fp5iipa85AiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2XL%2FbAgbOxtBgGXZKtwDLY40umJIhIG54zDoPwWlAWbmdEa7LE0w5FHh02cPS8m4npZB8AuNVEBxGhADcwvSxd5XlOrtP3pRRtjACwGuTzEY1XOY7TNZgQLVceqiOu7BblYN38ax8wDD%2BiDigoIc1Hu75fZzv8vIG5ZFT8IxMC8Q4a5R4M%2FlHcrywkWNHMgVxYT4BUCmkuxI9ut0qKlC325%2Bjn6Hc%2Bx78L6vHL8NMltzVz3ZtRCLs%2BiX1hsPk4bhc2hjxWlfi9cG5d7Nw%2BxbY%2Bw%2ButxHhPHkIgx4UlFV3L1wP2KblvyRvNtsfsuYufxIKq99HkZZ%2FHo8mYyccgWzM1zcfVFiH0ulCxJcx03ARCmYzU2DL8xHeYrBjedVIfpKAEs8C9T%2BCfLBLomDL5LhqPOV%2Bxro9iHhjQfLmWJWbcTbb2Lc3ks%2BVR0HrlkJx7uMWvIhWcLC9WOx%2BYdS2gT7kEaCvRl7TlzywmxHXdxLkHiPleCcbCjcKpuWiRYsdBmwBNEfsj2moLdzj8yESeWhnmOIckHTxWwiLak1sPp4HSluTk7WFBeSGGh0xO32TYfGmB8ZuNmLVDva%2BCJiA%2FLr2Hkf9eSZ5LjYuOrEzOeORKavkfti358f%2FeL2W%2BC%2BDpak15XJWAVAdXPnJ2Iw9pO4zwY6pgFazG5gyVHxH5HQKLBU77nFAoEax6Uw0A%2BpofjhbmNxf6F9KRELX6vEptMj6j4dcV9tet2WztpBidfXEPAzjwW9dMYCZSUWoNbvjCNeeQ9JyDNn72BEvBHQIPnq0qKzdLYgdVVCV%2B4Upu1RaSV8aUmExygbXRIV3csz%2BYj31z%2BOjxSeGItLq4eNf0T6M1at3c3ks%2FQb8Lbl6hmP8657Qhs01E77OFZt&X-Amz-Signature=5efcf87d4600a2eb8687cbc54e13cc22fad0142aca22f679cf4eefc5f183c8e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHWJZR4V%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T184317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcclSsEhzwSlo4s%2BHeeM%2Fss%2Fvo8sN7368k4QP0ltl%2B4AiBR%2FFsZgJfrvfmZ9dTkj6SO1Z9ve%2FCoqnA%2Fp5iipa85AiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2XL%2FbAgbOxtBgGXZKtwDLY40umJIhIG54zDoPwWlAWbmdEa7LE0w5FHh02cPS8m4npZB8AuNVEBxGhADcwvSxd5XlOrtP3pRRtjACwGuTzEY1XOY7TNZgQLVceqiOu7BblYN38ax8wDD%2BiDigoIc1Hu75fZzv8vIG5ZFT8IxMC8Q4a5R4M%2FlHcrywkWNHMgVxYT4BUCmkuxI9ut0qKlC325%2Bjn6Hc%2Bx78L6vHL8NMltzVz3ZtRCLs%2BiX1hsPk4bhc2hjxWlfi9cG5d7Nw%2BxbY%2Bw%2ButxHhPHkIgx4UlFV3L1wP2KblvyRvNtsfsuYufxIKq99HkZZ%2FHo8mYyccgWzM1zcfVFiH0ulCxJcx03ARCmYzU2DL8xHeYrBjedVIfpKAEs8C9T%2BCfLBLomDL5LhqPOV%2Bxro9iHhjQfLmWJWbcTbb2Lc3ks%2BVR0HrlkJx7uMWvIhWcLC9WOx%2BYdS2gT7kEaCvRl7TlzywmxHXdxLkHiPleCcbCjcKpuWiRYsdBmwBNEfsj2moLdzj8yESeWhnmOIckHTxWwiLak1sPp4HSluTk7WFBeSGGh0xO32TYfGmB8ZuNmLVDva%2BCJiA%2FLr2Hkf9eSZ5LjYuOrEzOeORKavkfti358f%2FeL2W%2BC%2BDpak15XJWAVAdXPnJ2Iw9pO4zwY6pgFazG5gyVHxH5HQKLBU77nFAoEax6Uw0A%2BpofjhbmNxf6F9KRELX6vEptMj6j4dcV9tet2WztpBidfXEPAzjwW9dMYCZSUWoNbvjCNeeQ9JyDNn72BEvBHQIPnq0qKzdLYgdVVCV%2B4Upu1RaSV8aUmExygbXRIV3csz%2BYj31z%2BOjxSeGItLq4eNf0T6M1at3c3ks%2FQb8Lbl6hmP8657Qhs01E77OFZt&X-Amz-Signature=f9fc41267fe98a174bfd4ae0d9fa16ed8b2820dbc7c901776003ce73c0696200&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







