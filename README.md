



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPFOB6CN%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T062227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEEdUBDZOnjFKGs8cI5359nUu7LDzeq7ipO5RtXLj%2FK8AiEA9zYciMoPCdWpx9RvDDV7x%2BYPM5kb6DD9RdWlApOWdFEqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUksY3GwannkK8hxSrcA3dqy1bH414Lg1tMDOKma394juQlJRLzfxP20zFkdQwGxV%2BSM7HjbQSXjPfvNf04aM0KUBHYsoitxmfJzWyOuV8st2CN%2Ff6AJJQmhC31D5H9Ys8QcT%2BAKw3aDRQl4d8AxyDI1uOOF7RDL9YtjRuHCump%2BLg9Flz3GuzxZd3bIT8WZx50%2BOlruUMDcv0njq3VzHZxl7s6%2FAmSAyQW8Z1%2BrDkdlqD4qtaG7BrAg2imfXpjdFx7fCL2rTa9dMOxPmutDQO%2BlYSBV6LVJGQCHKueXaq%2BRn7TUr3D3rX6%2BLsnDUiBrtV3QfkxqEalKfoNo4tRhskx1VBHToAi4e70G7N%2BErr67TI6f%2FrwjQ0Vdv4bzfYSxpq7FQNcaklr0ghHkvMpAfOjkkYVlbVbAX1138Gemasj%2BnamJAyfCEslUPoYD1T%2B01ZPxyr14ZmbVUKPVxY6Kk34ko6GUO4gRa3bV0xbEUX%2FsG7Uc%2BKaKTy5YUN9U8m98dZIdcFFdobG1S3c1Hi912YVTBchMNfpF0UQbUYXAa0bOtfVgKe%2Fg%2F77vkdiwyABBb6Pzr07VPSvv%2FzRFChteqBLuc6uI4M%2Bf8C5KUHWMarNJf0xfVWJYkdx8Cb8nFWaxi9mpjkzFYLyksLvMLTbjNYGOqUBeJdCjAOM7Fs7P4PwqJfXUz8onDOs0BzoOsTh9qfw64%2FPQOx%2BjptDJjiqCtdacdLcwjYOZA88pyhOrVbkdYgVMInoIKNH115VVIdbDD62lyt7%2ByOKc7sT5kskPO9wmcy97AYs7ORu45VB0WCpNYQu%2F5%2BFDogR8pyKQSVL2qI9Ne%2FU8DU4U8iN7plHbLCLif3jH5X8GQr%2FeLMhLi%2BtN2ozU0a4i7IL&X-Amz-Signature=22800467915407948f313e2ef8013b9eb4e813e89527cf70eaacb4061c61c8da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPFOB6CN%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T062227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIEEdUBDZOnjFKGs8cI5359nUu7LDzeq7ipO5RtXLj%2FK8AiEA9zYciMoPCdWpx9RvDDV7x%2BYPM5kb6DD9RdWlApOWdFEqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUksY3GwannkK8hxSrcA3dqy1bH414Lg1tMDOKma394juQlJRLzfxP20zFkdQwGxV%2BSM7HjbQSXjPfvNf04aM0KUBHYsoitxmfJzWyOuV8st2CN%2Ff6AJJQmhC31D5H9Ys8QcT%2BAKw3aDRQl4d8AxyDI1uOOF7RDL9YtjRuHCump%2BLg9Flz3GuzxZd3bIT8WZx50%2BOlruUMDcv0njq3VzHZxl7s6%2FAmSAyQW8Z1%2BrDkdlqD4qtaG7BrAg2imfXpjdFx7fCL2rTa9dMOxPmutDQO%2BlYSBV6LVJGQCHKueXaq%2BRn7TUr3D3rX6%2BLsnDUiBrtV3QfkxqEalKfoNo4tRhskx1VBHToAi4e70G7N%2BErr67TI6f%2FrwjQ0Vdv4bzfYSxpq7FQNcaklr0ghHkvMpAfOjkkYVlbVbAX1138Gemasj%2BnamJAyfCEslUPoYD1T%2B01ZPxyr14ZmbVUKPVxY6Kk34ko6GUO4gRa3bV0xbEUX%2FsG7Uc%2BKaKTy5YUN9U8m98dZIdcFFdobG1S3c1Hi912YVTBchMNfpF0UQbUYXAa0bOtfVgKe%2Fg%2F77vkdiwyABBb6Pzr07VPSvv%2FzRFChteqBLuc6uI4M%2Bf8C5KUHWMarNJf0xfVWJYkdx8Cb8nFWaxi9mpjkzFYLyksLvMLTbjNYGOqUBeJdCjAOM7Fs7P4PwqJfXUz8onDOs0BzoOsTh9qfw64%2FPQOx%2BjptDJjiqCtdacdLcwjYOZA88pyhOrVbkdYgVMInoIKNH115VVIdbDD62lyt7%2ByOKc7sT5kskPO9wmcy97AYs7ORu45VB0WCpNYQu%2F5%2BFDogR8pyKQSVL2qI9Ne%2FU8DU4U8iN7plHbLCLif3jH5X8GQr%2FeLMhLi%2BtN2ozU0a4i7IL&X-Amz-Signature=e310df0f565432272081bccaa9435c3b2ef994da32a8f5a899ff6b93c36522b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







