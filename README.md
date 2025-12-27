



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653TWASD7%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T062418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHsMF6Ca4FS9QsKnnhHgpPHYzqZSKKRS71cGkUtMUuXAiEA2aC%2Bt2EwFz%2B4E4atYkSBmoQivySdDc6I3JfW5K4mWIQq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBrcdtHPMqc08zm2PCrcA15mioc0x4X5F1FKvy7UXtXvmw9MIr040BeLWJvLjP3f%2BBaJ%2F910Ch%2Fqdrk%2BbVS92g4lfLFflCy5jj8K4AzL5jlG75AhcRpcEacLo8YGzQiHDRq9HWklcYALTzCznXq2kujo7eI7P%2FRJ64VDgRYcooHJeExXhaYji66BT0BDAv0WIoy0lTqMgTOx0Um1cIzkRnYGScKUM0waaa%2F4YhrjMap6QmEkpkGpsUg3DgUwhSxv5I5S3KdB0naZ5XUr6Q930EAzDKk4wwT25wqA9b0TlzimwFKfTjJL%2F8Uxobu2KVjHSytsTNutQm%2FVkk3hk2QUN%2BYttMcK8mgLBZR4TUBSjoZ3twpP55NaDzGT9npD0MZeN%2BHRaKud62cBuUoJf7GUkenCszlHjJhb0Wc95lxwG%2FG3pPxPREEVG1zeZU%2FAOOceCZ2UwnaDzBPUj5295G%2Fv%2FIz7bT7xNLaHcsmY0KcdwRLVLoBms1wHoLO9W6FLwVHSOvbd92P4dQ8VV590QjHwex66ngHRgeM9k6ZzRcKdvQ12Qg8ICJFEYns3wIYIH4NHI3c%2FB71jULgNqWDpI3OTOIBrS5NzTyvKgl5qAQejP1AixleE8T91ubL75K5Oz0SLGwOIUX0PDKm5Wv39MMflvMoGOqUBL5W50yCVc9SuFd9Wdo0%2BfN2iUenUeQYDTr%2BhX7Uzr3i4As%2BHZLLbD49EVgTxXt0R1CTNrLryT%2BjSmks3gl2E7QtxFSGKf1977V9BPqElXmupS3J2BzNqsLvL3ZzUCv8V2n66lAXm1sQQQ4WovZCmV%2BsGCqu2iZTe6lRhKkSjj4jk%2BECAeoTkGMUFXJ1fXay9OaCFQaOAcaKDpiq5INJ2MZ43YK9A&X-Amz-Signature=8c0f8c132f297532f11575afc0b0eb303b472d230e8940753a39b5ff09e66155&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653TWASD7%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T062418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHsMF6Ca4FS9QsKnnhHgpPHYzqZSKKRS71cGkUtMUuXAiEA2aC%2Bt2EwFz%2B4E4atYkSBmoQivySdDc6I3JfW5K4mWIQq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBrcdtHPMqc08zm2PCrcA15mioc0x4X5F1FKvy7UXtXvmw9MIr040BeLWJvLjP3f%2BBaJ%2F910Ch%2Fqdrk%2BbVS92g4lfLFflCy5jj8K4AzL5jlG75AhcRpcEacLo8YGzQiHDRq9HWklcYALTzCznXq2kujo7eI7P%2FRJ64VDgRYcooHJeExXhaYji66BT0BDAv0WIoy0lTqMgTOx0Um1cIzkRnYGScKUM0waaa%2F4YhrjMap6QmEkpkGpsUg3DgUwhSxv5I5S3KdB0naZ5XUr6Q930EAzDKk4wwT25wqA9b0TlzimwFKfTjJL%2F8Uxobu2KVjHSytsTNutQm%2FVkk3hk2QUN%2BYttMcK8mgLBZR4TUBSjoZ3twpP55NaDzGT9npD0MZeN%2BHRaKud62cBuUoJf7GUkenCszlHjJhb0Wc95lxwG%2FG3pPxPREEVG1zeZU%2FAOOceCZ2UwnaDzBPUj5295G%2Fv%2FIz7bT7xNLaHcsmY0KcdwRLVLoBms1wHoLO9W6FLwVHSOvbd92P4dQ8VV590QjHwex66ngHRgeM9k6ZzRcKdvQ12Qg8ICJFEYns3wIYIH4NHI3c%2FB71jULgNqWDpI3OTOIBrS5NzTyvKgl5qAQejP1AixleE8T91ubL75K5Oz0SLGwOIUX0PDKm5Wv39MMflvMoGOqUBL5W50yCVc9SuFd9Wdo0%2BfN2iUenUeQYDTr%2BhX7Uzr3i4As%2BHZLLbD49EVgTxXt0R1CTNrLryT%2BjSmks3gl2E7QtxFSGKf1977V9BPqElXmupS3J2BzNqsLvL3ZzUCv8V2n66lAXm1sQQQ4WovZCmV%2BsGCqu2iZTe6lRhKkSjj4jk%2BECAeoTkGMUFXJ1fXay9OaCFQaOAcaKDpiq5INJ2MZ43YK9A&X-Amz-Signature=dbe66bf7c43d778310f4135d5200bd7efd5a73e277c0f49cdbb406c1cb796615&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







