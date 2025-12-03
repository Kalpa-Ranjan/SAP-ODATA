



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZHW4PQK%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T011431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIDmlZIZoS3NPraiO%2FsyaD1RYxoK9btLL53HJjBihbROWAiBrhRk6MdSwWAmWYb%2B0wNUoSEFPDiSTnL9pju7cjdGSAir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMBoJvXjWJxX4vGB2AKtwDTPs9QTuZm6t5UNK1en%2Bh1jPACdV4QdNEZ%2BRe376Mpqj5ZuzoLsJZNMwlG6Iu84ZOUJiSKXs7KJ7Ak1YLeDLSZmVO98FgMuIA%2BqQIy3%2BolT3bYtrP0xaNENKLuePX4lHEuH1ed1NUmxzZ72Um%2B775RpNwew%2Fm5bwBtMDHQGUUy7TT7u2NlAiidrNewpYtbcjsnHD0pzpNlrje9V9kFejiPirruIsmmV60oGoUJOZJFNOuj%2BeYdKJPNfipxVgSE%2BLOBxoY%2FzA%2B2%2BWgt3jjyY0GZ%2FkgxIUlu2yitmZTNN9xNWM%2FiB9NH1t0YHWwovzynD9m63oNyoyX6gXKEjPJIpN2ZD906AWFwnB3DdO%2Fj2AegZ7ZAucfVWteYatx6KHuRB2VZwIvGcY3lkt%2FNUcgcQufD0hy6%2BXERyt%2BDhpP%2FUGgSfWwScHwNe5lmmfwoIKX2rt0Luk3nDsqNpcuS7F3lOUOEmkMF4NlI7Pb54YrTiDBBRKnXDaexoq2w%2B%2BwlA4Fk%2FdRnL%2Fsvjcc1fwUPgpWjxaZ1HgswfBYnt2GPWpiWEpkkebvYMSoU%2B3s5RD%2BN9Tqfm2wDLvQk0FY9LcWtvgtamwWvq17CDsD68xIQxWU8mkZplHnyhljkj9u7wcXr00w75S%2ByQY6pgHl28UAMHVTia0%2BKk7tPx0%2Fl6OVhC9kfR2RUkFyIi7MupM7iw5ohrihkb2QtcOZ%2FcDVrVTGm0MZGtp0YH4DVI8JnsIxRH4UxjbO3ahsYOv7lAz0M%2BsuN%2FuSZ%2BtVjKMqg7yd%2BRPQ77zD6H3EcJL%2F8iyUblqSLmnXspL04qRQZQOxZEyaYGkGR6U4vbgHbws0F%2BaM6brjZuCYMRnBDpFJF%2B6x3vJvcxqn&X-Amz-Signature=5951d7c970e980c41f1ea7b56ce3305f9f3e9b9d68fc504b71538fa2f7d306ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZHW4PQK%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T011431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIDmlZIZoS3NPraiO%2FsyaD1RYxoK9btLL53HJjBihbROWAiBrhRk6MdSwWAmWYb%2B0wNUoSEFPDiSTnL9pju7cjdGSAir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMBoJvXjWJxX4vGB2AKtwDTPs9QTuZm6t5UNK1en%2Bh1jPACdV4QdNEZ%2BRe376Mpqj5ZuzoLsJZNMwlG6Iu84ZOUJiSKXs7KJ7Ak1YLeDLSZmVO98FgMuIA%2BqQIy3%2BolT3bYtrP0xaNENKLuePX4lHEuH1ed1NUmxzZ72Um%2B775RpNwew%2Fm5bwBtMDHQGUUy7TT7u2NlAiidrNewpYtbcjsnHD0pzpNlrje9V9kFejiPirruIsmmV60oGoUJOZJFNOuj%2BeYdKJPNfipxVgSE%2BLOBxoY%2FzA%2B2%2BWgt3jjyY0GZ%2FkgxIUlu2yitmZTNN9xNWM%2FiB9NH1t0YHWwovzynD9m63oNyoyX6gXKEjPJIpN2ZD906AWFwnB3DdO%2Fj2AegZ7ZAucfVWteYatx6KHuRB2VZwIvGcY3lkt%2FNUcgcQufD0hy6%2BXERyt%2BDhpP%2FUGgSfWwScHwNe5lmmfwoIKX2rt0Luk3nDsqNpcuS7F3lOUOEmkMF4NlI7Pb54YrTiDBBRKnXDaexoq2w%2B%2BwlA4Fk%2FdRnL%2Fsvjcc1fwUPgpWjxaZ1HgswfBYnt2GPWpiWEpkkebvYMSoU%2B3s5RD%2BN9Tqfm2wDLvQk0FY9LcWtvgtamwWvq17CDsD68xIQxWU8mkZplHnyhljkj9u7wcXr00w75S%2ByQY6pgHl28UAMHVTia0%2BKk7tPx0%2Fl6OVhC9kfR2RUkFyIi7MupM7iw5ohrihkb2QtcOZ%2FcDVrVTGm0MZGtp0YH4DVI8JnsIxRH4UxjbO3ahsYOv7lAz0M%2BsuN%2FuSZ%2BtVjKMqg7yd%2BRPQ77zD6H3EcJL%2F8iyUblqSLmnXspL04qRQZQOxZEyaYGkGR6U4vbgHbws0F%2BaM6brjZuCYMRnBDpFJF%2B6x3vJvcxqn&X-Amz-Signature=2c293e95487f1f4d3323d79f7e24d40c0d84eb2b061d3661ff2cef18875b03f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







