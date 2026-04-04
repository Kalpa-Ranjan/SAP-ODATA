



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4YLAPX4%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T014832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBC86PT6mfA6AEAQzIlWkyjd33ji4ajeF1tM%2BDS%2FiPYqAiEA0pKXKEala0GCM98g%2FXW8jiELDxvQmqFqB%2FOVJ88vIccqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfwOIMXL67F7z2eHCrcA%2BAin4oaGzAwgxULi8fJDcGg2XFOvMv6yRub3IxspBT6G9L7uYEYVSZTM2dEdcSz02NSNNJaavzKD9Hs4xroZFgvjIVYcvtmhoKYBjfF3hOoGVcMmguO8U3mAzki%2F%2FL4gcdGOu%2FOJTew%2BCQKpq1Etd2OvpmdEPUJZwEftmPt1OWPJZhPK3HnS7K3RBSqw9lKM4i5w41pNvPlKM5wmvZc5GdR2efyOigqi%2BvkqzgKVSY0C8GOhdWYDkQBZFiUdz9k6%2FtKv3fG%2Fwq7lkXH3kzfW0JXtR1i%2F8YshJ95oyo%2F0yzqhT8Cun3h4GpTI1%2FiJ6ygFaldLj6S3QRDujRBUOfuRLh6Uh1lq6ey3SRCxwdscvTYB4RrZ907qxoTgS%2FZKwEx2mGZuQpGUjYG43udvBzgw12Es0aiG0zNvQG6fnrVU0Gz1CrB6ojYwZYxS3yKgYhp9wsgQ9%2FYSzn3ShaAJ2o5SaLCZwJUvbrTqaPgNSq0hp0z7RcLbacD8zG3gzGJr0Jm8OGZHPBimzYCwoAyQw2wnZ7186IPGFmk%2F6EHMjtLvCLuHu%2Bkvc%2FOPyjvBPPluuYVGGyqxdSOuXfGLv9GEPuCNPX56IRbi%2Feq6Ve9UtoR%2BVfRTIE%2Bw2PxNYAqsTfrMJy7wc4GOqUBGE9VDj5q9Outge3yRXzZYgy5zH7jr2AMJYTzgRTtW54qRpP4wQ2rVAlceCnAw%2B0H6lKZq%2FnHKo7256ahqkO%2FgIhpAzl3Ecs2%2BJl3d7mSXMbpZn3I%2F0SwQFiA%2FdLTVEQYEHbnVkeVP%2Bs5RXcBO0LvhSIqke4e1C2GrDK4Ij5QtyM2E%2F7eszJn3ie0NHx3g1dL6TmlRjzovD2tdLm8M9qSO2aoZ6eg&X-Amz-Signature=ac306713bd7a573328d67872c3a984489bea2ea309885da46c67f50e1c910e69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4YLAPX4%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T014832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBC86PT6mfA6AEAQzIlWkyjd33ji4ajeF1tM%2BDS%2FiPYqAiEA0pKXKEala0GCM98g%2FXW8jiELDxvQmqFqB%2FOVJ88vIccqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfwOIMXL67F7z2eHCrcA%2BAin4oaGzAwgxULi8fJDcGg2XFOvMv6yRub3IxspBT6G9L7uYEYVSZTM2dEdcSz02NSNNJaavzKD9Hs4xroZFgvjIVYcvtmhoKYBjfF3hOoGVcMmguO8U3mAzki%2F%2FL4gcdGOu%2FOJTew%2BCQKpq1Etd2OvpmdEPUJZwEftmPt1OWPJZhPK3HnS7K3RBSqw9lKM4i5w41pNvPlKM5wmvZc5GdR2efyOigqi%2BvkqzgKVSY0C8GOhdWYDkQBZFiUdz9k6%2FtKv3fG%2Fwq7lkXH3kzfW0JXtR1i%2F8YshJ95oyo%2F0yzqhT8Cun3h4GpTI1%2FiJ6ygFaldLj6S3QRDujRBUOfuRLh6Uh1lq6ey3SRCxwdscvTYB4RrZ907qxoTgS%2FZKwEx2mGZuQpGUjYG43udvBzgw12Es0aiG0zNvQG6fnrVU0Gz1CrB6ojYwZYxS3yKgYhp9wsgQ9%2FYSzn3ShaAJ2o5SaLCZwJUvbrTqaPgNSq0hp0z7RcLbacD8zG3gzGJr0Jm8OGZHPBimzYCwoAyQw2wnZ7186IPGFmk%2F6EHMjtLvCLuHu%2Bkvc%2FOPyjvBPPluuYVGGyqxdSOuXfGLv9GEPuCNPX56IRbi%2Feq6Ve9UtoR%2BVfRTIE%2Bw2PxNYAqsTfrMJy7wc4GOqUBGE9VDj5q9Outge3yRXzZYgy5zH7jr2AMJYTzgRTtW54qRpP4wQ2rVAlceCnAw%2B0H6lKZq%2FnHKo7256ahqkO%2FgIhpAzl3Ecs2%2BJl3d7mSXMbpZn3I%2F0SwQFiA%2FdLTVEQYEHbnVkeVP%2Bs5RXcBO0LvhSIqke4e1C2GrDK4Ij5QtyM2E%2F7eszJn3ie0NHx3g1dL6TmlRjzovD2tdLm8M9qSO2aoZ6eg&X-Amz-Signature=aaefc8a274400e74c3c6d545c040840168b04a1363e29a6d299e2590c012e0a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







