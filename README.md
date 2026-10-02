



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZMHT4XY%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T061345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP6qPOJeOUmmm5fqdTGv7pW4RRhjGsTDlS58sk66YceAiAB12D%2BVZBEHmczAiXJnpflx3X%2BkZiuaDpJwZVTYzY9vSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKD4d8oEi2sMMioLKtwD%2BN3uvp4O9Zp2xdQBqX4plGrRDX1OogK4Av6AsIToS1sJQIKvBt7n%2Bj7gnrAB2K8%2Frq8MT9fpj%2BlC5tZ%2FS2kVJp%2F16aH8rQjlrpPCAFIZAGbKrIiAxNKRbWAmQw5yl2Hicq7EJsWYGRDSkeSCW1PQiWrA%2FdSAfMWExygX5i8ed8pKyHQdz53jKkM88U4THmYKBPUsA6KxEBO3ZjW50coyPQ%2FM61S5ie%2FiC8jHyOsftK9WWxNGq0K0B6twBAfP1NgkLXHEvtFzzweZ3VZ%2Br5E2cUaKRkZQR5r2I%2FN%2BQIoY3Qn59KoxDs6oqgw3c3xBl7%2BfYujsB582Ul2u3uUBjA9Wi64Gas5CNfw3z7qivx7tFBLbzA0Whpon9Cfk7%2FyQjowkcEndRvQS8BTwVqQ3Em6IOwccavPsFWuTVWEuJyKs034ybAovOJDOTM4AhedIXHET2tYuonVDysf4WUygMvTaF6YMT9PZye5r0cvVFoWYcz51qqUJ4ZlkLTwVUK2FIAMZKHeMqA47Z3dcIVv%2F18iqEE7GRl%2Blthu5CWdZG5OI2zrIL%2Fl0lJuokkB9DoZXo7OyRXastzYryGlDLsF1D34ESuHHs5BOZmtMPr92AEyUZ6GyQotmPUxxc2GSq0gwrPL81QY6pgFXeUm%2BYS8PmpjtCF9GjI7tnPyh4MKG6p14yBVP7odcS27f1zsUUDwJ%2FgSejy%2FIFDY1lYU94GGSZRJrODbM%2FhA2qfiqRJdxk05zlNWoPkZDKw4vMHHlu%2FJAyLWBH1lJMvbMoG4X6cMWQVfV6rhR2D6e6ORqI%2BYaSLq2vhtHAJ40EBQZouOGiUCbQPHNAZlFP6AhFA%2F723MXOmgCiF9pcAig5qRbdaOr&X-Amz-Signature=9ed94a3c5ffae2e516bb484c8739254fa64b463fc3a545b712d69177e81307e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZMHT4XY%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T061345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP6qPOJeOUmmm5fqdTGv7pW4RRhjGsTDlS58sk66YceAiAB12D%2BVZBEHmczAiXJnpflx3X%2BkZiuaDpJwZVTYzY9vSqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKD4d8oEi2sMMioLKtwD%2BN3uvp4O9Zp2xdQBqX4plGrRDX1OogK4Av6AsIToS1sJQIKvBt7n%2Bj7gnrAB2K8%2Frq8MT9fpj%2BlC5tZ%2FS2kVJp%2F16aH8rQjlrpPCAFIZAGbKrIiAxNKRbWAmQw5yl2Hicq7EJsWYGRDSkeSCW1PQiWrA%2FdSAfMWExygX5i8ed8pKyHQdz53jKkM88U4THmYKBPUsA6KxEBO3ZjW50coyPQ%2FM61S5ie%2FiC8jHyOsftK9WWxNGq0K0B6twBAfP1NgkLXHEvtFzzweZ3VZ%2Br5E2cUaKRkZQR5r2I%2FN%2BQIoY3Qn59KoxDs6oqgw3c3xBl7%2BfYujsB582Ul2u3uUBjA9Wi64Gas5CNfw3z7qivx7tFBLbzA0Whpon9Cfk7%2FyQjowkcEndRvQS8BTwVqQ3Em6IOwccavPsFWuTVWEuJyKs034ybAovOJDOTM4AhedIXHET2tYuonVDysf4WUygMvTaF6YMT9PZye5r0cvVFoWYcz51qqUJ4ZlkLTwVUK2FIAMZKHeMqA47Z3dcIVv%2F18iqEE7GRl%2Blthu5CWdZG5OI2zrIL%2Fl0lJuokkB9DoZXo7OyRXastzYryGlDLsF1D34ESuHHs5BOZmtMPr92AEyUZ6GyQotmPUxxc2GSq0gwrPL81QY6pgFXeUm%2BYS8PmpjtCF9GjI7tnPyh4MKG6p14yBVP7odcS27f1zsUUDwJ%2FgSejy%2FIFDY1lYU94GGSZRJrODbM%2FhA2qfiqRJdxk05zlNWoPkZDKw4vMHHlu%2FJAyLWBH1lJMvbMoG4X6cMWQVfV6rhR2D6e6ORqI%2BYaSLq2vhtHAJ40EBQZouOGiUCbQPHNAZlFP6AhFA%2F723MXOmgCiF9pcAig5qRbdaOr&X-Amz-Signature=d00fdecf3d2bebecb42a32a78195530b165cc1f299671792d16e2261768c5b09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







