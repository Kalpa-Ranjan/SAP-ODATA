



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOVE4OOE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T125909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCswAkyAW03pUqiJ2b2Fc%2BO7MfgxwgxMt4YUXmoOBf2QQIhAPo1ir8mio7GL2YrOQ6Yj1qdrNJKXIeDmtT76p53b4vqKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxthyFuUQU6Zhv8%2BIkq3APtgBq7hHfVZIMvsZlMMzi6Xs3zT8bVfZc3%2B%2FuscD%2BalLQWGrQxHyI1W7eM0WT2LUVHthvbO%2Bgq3eG91SIRzQPO%2BvHh4hx3H4YItw10tB96wR1%2FZdGY3Y347YIPKFoMqlJbFyGDAYQKAuedImgBN5ItjXhiqURR9eVmUDw8xKfkHUCWmjmnvoXSZisAg4pqzXG%2Bc2iGssSu6og%2B%2FAqv9%2FJ6FoVVZIgEB6OmCgqwB0QCGocu3oDxEKURmp4L%2FsCp5YEyjLO4N7d2HojGWE5XIlupApv8%2Bm8JVyEpLdx0SDQLwELxWX5PXlk6dpoQeGsm0VpiagKRsP%2FDpUhoaGHQws%2F6LC8g9j4OTme46dEMskCZfgH1m%2Fh7Ri08gQzR19mPpaxLIQ3K5WWQHbta345EclQ%2BDTbBxvx%2F9IEFVmKHxZKAWZIOC0Has9b3GYoCdQCuVs0n5nXoNRe1jO8V4%2B1C2nQia%2BtTl2K%2F4FQGNpntrnssRizhxIMghBjiW1AUA%2BWd5B8MnIkAsUrHg1urRcqMp0meorULiWlR6t8yd%2Fw3rz9vbsJBlcO0TTt5EVPGeWyh86yiYl9bGHfcuslm7mzdwhFJvmFWmEcNYcb9ooFGgZFPDClEW%2B3i88jmTM%2BGUjCLys7OBjqkAcsA%2FhH18U7Czb%2Bv5paMTc%2FEe7PqmXil%2B1d6fg%2FpfPDA8XMezfYs89RmI3Wo%2FAGdxje8HGyhFIhd7w93JV7Oh1z%2BAGd2dh6q6Nw%2BKCwvUa8tQCl%2BiUjQBEaf6sS9W8zawNo%2B8PWYDPX9IlLyTFl94nTy0tEX3Tv5tSlmkKwJrJCrVxGMi9PIEcELuupIt61wtwUBhxsvlSE4hiLuWygfsVt5k0Mx&X-Amz-Signature=c2dbe55c2e2e0d51e32a8386bfb20e782fdd2b95fc14adcbd1b04dc6b562f9f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOVE4OOE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T125910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCswAkyAW03pUqiJ2b2Fc%2BO7MfgxwgxMt4YUXmoOBf2QQIhAPo1ir8mio7GL2YrOQ6Yj1qdrNJKXIeDmtT76p53b4vqKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxthyFuUQU6Zhv8%2BIkq3APtgBq7hHfVZIMvsZlMMzi6Xs3zT8bVfZc3%2B%2FuscD%2BalLQWGrQxHyI1W7eM0WT2LUVHthvbO%2Bgq3eG91SIRzQPO%2BvHh4hx3H4YItw10tB96wR1%2FZdGY3Y347YIPKFoMqlJbFyGDAYQKAuedImgBN5ItjXhiqURR9eVmUDw8xKfkHUCWmjmnvoXSZisAg4pqzXG%2Bc2iGssSu6og%2B%2FAqv9%2FJ6FoVVZIgEB6OmCgqwB0QCGocu3oDxEKURmp4L%2FsCp5YEyjLO4N7d2HojGWE5XIlupApv8%2Bm8JVyEpLdx0SDQLwELxWX5PXlk6dpoQeGsm0VpiagKRsP%2FDpUhoaGHQws%2F6LC8g9j4OTme46dEMskCZfgH1m%2Fh7Ri08gQzR19mPpaxLIQ3K5WWQHbta345EclQ%2BDTbBxvx%2F9IEFVmKHxZKAWZIOC0Has9b3GYoCdQCuVs0n5nXoNRe1jO8V4%2B1C2nQia%2BtTl2K%2F4FQGNpntrnssRizhxIMghBjiW1AUA%2BWd5B8MnIkAsUrHg1urRcqMp0meorULiWlR6t8yd%2Fw3rz9vbsJBlcO0TTt5EVPGeWyh86yiYl9bGHfcuslm7mzdwhFJvmFWmEcNYcb9ooFGgZFPDClEW%2B3i88jmTM%2BGUjCLys7OBjqkAcsA%2FhH18U7Czb%2Bv5paMTc%2FEe7PqmXil%2B1d6fg%2FpfPDA8XMezfYs89RmI3Wo%2FAGdxje8HGyhFIhd7w93JV7Oh1z%2BAGd2dh6q6Nw%2BKCwvUa8tQCl%2BiUjQBEaf6sS9W8zawNo%2B8PWYDPX9IlLyTFl94nTy0tEX3Tv5tSlmkKwJrJCrVxGMi9PIEcELuupIt61wtwUBhxsvlSE4hiLuWygfsVt5k0Mx&X-Amz-Signature=f433b766c5edbad15ea05a7ea3db5b6d5e86b6a737d58e4c18b65d9dc461a03f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







