



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z72MR5A%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T063408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFh%2FL1Nb68I6gdZaN7b4GC1Y9CuZ1DEbHFyA7ZllTV6yAiEApFCjBFRiUnyq3QynjzxhV6I4D%2BlLwbDrasdgOxcaCRQq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHHgrtRuqcpbNGR%2B%2ByrcAxgfmEGEVSqvLm67uKyl7ZdTbpf%2BrlGTUG7lBKA3FZicbV8LtCmEvIJdV%2BOD280lBQ9W%2FirNfUw9Ca%2B6RH8%2BWFoM9F8iQ7gHp%2FUKAcn0myWTfm33anVL6nY2UvBi%2BkCsmhIxeKytH%2BCpknmC%2FNiB5dR2sbj%2Fx0V3iAVX%2FQHVSFlX6ePtEnwZwvwX7Zf%2BLIFn2DPhkSsQIkBvce%2BlpWKYFLVW%2FoPNCfnRNz5ME2Y3ghC0jhuYC9k7X2lD3K2uQ%2BM3rM5A4y7Xgw8gjzVDcXP0CdQyQPfEcIw2t%2Fki%2Fl%2BQ5lxNmC3E5yQXdSO6ITjR27hzc48tshPV1QCvTgvxa3LcfQ2IwI8KO%2FS2%2FPzrsaeYtjKwMt%2FFFk%2BiPPzybr1biJocNjLPFpEPARF5MIhgRw%2B2T%2FQ1kzW0gLYFuKZ0liU8R3ZTMd2lGyfefsvDLolS340xzWQGHMwyw6xy%2BQo%2BRK8yMs0wGQSj8ISLvkncO%2F54MOKegYpYwiyFgsaOqn8xMz4rL9XqhbubxBSMTSZBMg4ywGr6hBvTIPu%2BQLNKXgRrNwADx7OT8f7X%2F%2BrE6fC9ZhoIBZK0neAVRxrucXqH3ida9840bc27q9hnSZpymfGXeYLpD45om0Qx3BUe5jD2MP%2FclNQGOqUBf3sguFbAFB%2FyvvTHJNG53XhBWsApHRcjRwl2%2FjVxNnTDvAax8jNWti3P4xjbgy8EvRxSBiN4wXkL86zTxA2YDrNz26lC9j1E0te1Zrcjd2tDHQRKi5GeJ1TITpu6yCrXpqEuNo9p7W8cZ6HSYYiXvGeEiVv0Ms1xgDriLRZR%2BBzV9k%2FSACFpm3oXWW9eyCb1JE4CmYDOpir8JpH2Hc1ScUibV%2BDH&X-Amz-Signature=47d5ef3a568941ae0fe52868fb886c63fc90438cfd4d22383df581f7cf91cbb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z72MR5A%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T063408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFh%2FL1Nb68I6gdZaN7b4GC1Y9CuZ1DEbHFyA7ZllTV6yAiEApFCjBFRiUnyq3QynjzxhV6I4D%2BlLwbDrasdgOxcaCRQq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHHgrtRuqcpbNGR%2B%2ByrcAxgfmEGEVSqvLm67uKyl7ZdTbpf%2BrlGTUG7lBKA3FZicbV8LtCmEvIJdV%2BOD280lBQ9W%2FirNfUw9Ca%2B6RH8%2BWFoM9F8iQ7gHp%2FUKAcn0myWTfm33anVL6nY2UvBi%2BkCsmhIxeKytH%2BCpknmC%2FNiB5dR2sbj%2Fx0V3iAVX%2FQHVSFlX6ePtEnwZwvwX7Zf%2BLIFn2DPhkSsQIkBvce%2BlpWKYFLVW%2FoPNCfnRNz5ME2Y3ghC0jhuYC9k7X2lD3K2uQ%2BM3rM5A4y7Xgw8gjzVDcXP0CdQyQPfEcIw2t%2Fki%2Fl%2BQ5lxNmC3E5yQXdSO6ITjR27hzc48tshPV1QCvTgvxa3LcfQ2IwI8KO%2FS2%2FPzrsaeYtjKwMt%2FFFk%2BiPPzybr1biJocNjLPFpEPARF5MIhgRw%2B2T%2FQ1kzW0gLYFuKZ0liU8R3ZTMd2lGyfefsvDLolS340xzWQGHMwyw6xy%2BQo%2BRK8yMs0wGQSj8ISLvkncO%2F54MOKegYpYwiyFgsaOqn8xMz4rL9XqhbubxBSMTSZBMg4ywGr6hBvTIPu%2BQLNKXgRrNwADx7OT8f7X%2F%2BrE6fC9ZhoIBZK0neAVRxrucXqH3ida9840bc27q9hnSZpymfGXeYLpD45om0Qx3BUe5jD2MP%2FclNQGOqUBf3sguFbAFB%2FyvvTHJNG53XhBWsApHRcjRwl2%2FjVxNnTDvAax8jNWti3P4xjbgy8EvRxSBiN4wXkL86zTxA2YDrNz26lC9j1E0te1Zrcjd2tDHQRKi5GeJ1TITpu6yCrXpqEuNo9p7W8cZ6HSYYiXvGeEiVv0Ms1xgDriLRZR%2BBzV9k%2FSACFpm3oXWW9eyCb1JE4CmYDOpir8JpH2Hc1ScUibV%2BDH&X-Amz-Signature=5a359d0827db7dd70f1b946ec7566361fe8b4effb5a9d029496f51c9fd116d72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







