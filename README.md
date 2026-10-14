



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E6DO3OT%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T061234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDTuG%2FKOSQ89KXe4LGZKWaDM9L7lDU6zb55IRNkxffT0AiEAr3NVCWY7wmB%2B9AxBOHyEBlifopPFrpb6SI6ysvVZc5AqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrOMsvjwAseRMI3KCrcA3%2Fsn%2FNd%2FrORdi41FkZ4P%2BZlNWBhWfjo4jYlAu9OVVYP0H1GQhu3enLH6OA2p6e6U5uo5KrYAGNoLq4dBR1SchEmo4tx%2BO%2Fsx4UUmb4%2BgmpZ09Ci%2BqN84m98%2FjYj8Kdv%2F97BArKuIAKWoInCgmRKZBdQiGHqKMqmhdjlOmlAnRyqJzQcf5oZvWy5DaGCNxl756V4AVsXAz1G61OMeRaqzau4FiXZWHPC9iJBiI2TBi8FcETkp8PHV7Di0AGY82QioT61%2FOzM5YQbaCWUH8Enq4mzB9%2BFWOe1ySRYI1pytvEPg%2FhdwsHoMMAXzYtSefAeIzpZU3iWswKURwMPmoGCrWYzH5YX5MuhhlzDGWkj71uvNcA6wwD%2BftzB27vEyHudtd%2FMIhAj1VFtPKQH9Eca%2BJcxxBHm%2FfWC%2FRMmclrXoJZ%2FLxxYDa%2BWsVRe2Q49jiljJBU7W%2FdO2L12h9RMP%2BtR4uP4CiJ9SiL%2FVGAcQqLUvvRfYLMDhgksUUouiFZXervcRv0YYWGhKnTS7lHcSxIKG2NzwJ9NQJjlPhMuopPKwRsY8AkujeVhnGcqoboqbYJvdjZHivImh4fIk8vSNc9qXrYIpkvEe2rUUdAbVhityVVGTeWx0Zew4wcQR0JFMKeSvNYGOqUBr00PFH0rycuA5FMWUdNo727V%2F5on5OIh%2BfpRo201NoEYSZgShnQlyMl%2BxKKfFbhX%2Br42moUS0995c%2BEP2hkK5wzf0nIx5Hmy1jQM9n7fhd4t2a7GN5hfEJ1zusUy4WkNUDyI5cCdT4uE1s4jd%2FZssKDinFdcHBdCnl9lKqgUJI9TfawaqYhwwiLjijD3Du%2FtFhbft%2FzrPorqjiVhA2oRcGgHc003&X-Amz-Signature=ca228cede043205224b770af48e6ee6a23bff51fd243176fb52988654e125482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E6DO3OT%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T061234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDTuG%2FKOSQ89KXe4LGZKWaDM9L7lDU6zb55IRNkxffT0AiEAr3NVCWY7wmB%2B9AxBOHyEBlifopPFrpb6SI6ysvVZc5AqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrOMsvjwAseRMI3KCrcA3%2Fsn%2FNd%2FrORdi41FkZ4P%2BZlNWBhWfjo4jYlAu9OVVYP0H1GQhu3enLH6OA2p6e6U5uo5KrYAGNoLq4dBR1SchEmo4tx%2BO%2Fsx4UUmb4%2BgmpZ09Ci%2BqN84m98%2FjYj8Kdv%2F97BArKuIAKWoInCgmRKZBdQiGHqKMqmhdjlOmlAnRyqJzQcf5oZvWy5DaGCNxl756V4AVsXAz1G61OMeRaqzau4FiXZWHPC9iJBiI2TBi8FcETkp8PHV7Di0AGY82QioT61%2FOzM5YQbaCWUH8Enq4mzB9%2BFWOe1ySRYI1pytvEPg%2FhdwsHoMMAXzYtSefAeIzpZU3iWswKURwMPmoGCrWYzH5YX5MuhhlzDGWkj71uvNcA6wwD%2BftzB27vEyHudtd%2FMIhAj1VFtPKQH9Eca%2BJcxxBHm%2FfWC%2FRMmclrXoJZ%2FLxxYDa%2BWsVRe2Q49jiljJBU7W%2FdO2L12h9RMP%2BtR4uP4CiJ9SiL%2FVGAcQqLUvvRfYLMDhgksUUouiFZXervcRv0YYWGhKnTS7lHcSxIKG2NzwJ9NQJjlPhMuopPKwRsY8AkujeVhnGcqoboqbYJvdjZHivImh4fIk8vSNc9qXrYIpkvEe2rUUdAbVhityVVGTeWx0Zew4wcQR0JFMKeSvNYGOqUBr00PFH0rycuA5FMWUdNo727V%2F5on5OIh%2BfpRo201NoEYSZgShnQlyMl%2BxKKfFbhX%2Br42moUS0995c%2BEP2hkK5wzf0nIx5Hmy1jQM9n7fhd4t2a7GN5hfEJ1zusUy4WkNUDyI5cCdT4uE1s4jd%2FZssKDinFdcHBdCnl9lKqgUJI9TfawaqYhwwiLjijD3Du%2FtFhbft%2FzrPorqjiVhA2oRcGgHc003&X-Amz-Signature=0ac60cfeef48c401fc78644b5861a3f2f7eaf85842909a7bbca78dea0299df05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







