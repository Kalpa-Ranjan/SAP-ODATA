



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIYQZDWM%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T121113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLqDTBNeO0545x6EcdaTycZMktCd932F6PuEg7yXBAvgIgL9InVwNn69RNxYc1nkAZLOdNAycdTiLgzk5%2FC6FOGDYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfUED6wx%2FYcr12JtSrcAyXcQCpeQcacPPdFfBXPJGP3DForkiuRjAIOIhTLha%2FY1rt0v8emNcedBpUF9CY5LrqUyufe8ncmctvVS9xdwsPhQ6pYR2%2BXUBas2VA2dz90VF%2Bw7q%2B3MB6NeTEpaXx2l4uQv7rEA1orHJJx%2FBVcAJvgrU%2B3dcYaPnBZP1bTrx%2FpEhSh1LSdxGndH8r8hHyn5RZTiWZjLm7Z8DJYQ1hA8vFNPnu1nAbnSkIkajnkI%2FGqvmlsptKiLy3MyBLNKokJ20pyeue0nbzjqVm%2FgH87aksf%2FM1o%2FPTpaxoZZJFPJok9j9tLS%2FOUXu4Ys7jvAW7CmwuGn%2FkQ5lgQ7myC7UHqu0Qdw9UXT2QEKrgmDcSW2E%2FeuvNMkk9ZWyqSdFO2dy8t9Pdc2z2dxTHe2G%2F3VPDe%2BQ54OrPt8nxHgSk8cHs3Pia0YkpZi5yGqvOnvgPLqEfeCgK0FXUwZbwb87qNDiMDEJ%2BWo2pNcWEYbA8%2Bny0dC6uFF1jrmP11NQh6p7gI2%2B2iurcAp9bNIt39dcP%2Bsa1VIVCUHnP8fLnIgByCUo%2FLUnPRrwYumc18e3SDxJzREVMG4Mis%2FhPqJZJ6CDiR5128d6q3tFAr9esY3TunaC%2BuTwg705jcaFKkclEHvErFMI%2BhitUGOqUBzH39n4D4UQ1D6s0ZD90DrxZEptOj9KYa4wOo8eCkPI4pu6SqRL18iHEASrVQIPkoH7QXvb1iOvKoP%2Ft4s7htFDxrmK84bckob30yp3YeYIK%2BnfsRidS3Uyag%2BzcLNFKaPporf0XeJ%2Fniqm05IFkbeWpdd59JLWjTIPnkvk5y9POmJna%2FNxOMtW3eEiDn4eBqu24wYSp6DaHy2oJ722IEJasOfDPA&X-Amz-Signature=df15031656201bb89291fd28c674c460a9431930dc25c7848aa2663dc01d488a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIYQZDWM%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T121113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLqDTBNeO0545x6EcdaTycZMktCd932F6PuEg7yXBAvgIgL9InVwNn69RNxYc1nkAZLOdNAycdTiLgzk5%2FC6FOGDYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfUED6wx%2FYcr12JtSrcAyXcQCpeQcacPPdFfBXPJGP3DForkiuRjAIOIhTLha%2FY1rt0v8emNcedBpUF9CY5LrqUyufe8ncmctvVS9xdwsPhQ6pYR2%2BXUBas2VA2dz90VF%2Bw7q%2B3MB6NeTEpaXx2l4uQv7rEA1orHJJx%2FBVcAJvgrU%2B3dcYaPnBZP1bTrx%2FpEhSh1LSdxGndH8r8hHyn5RZTiWZjLm7Z8DJYQ1hA8vFNPnu1nAbnSkIkajnkI%2FGqvmlsptKiLy3MyBLNKokJ20pyeue0nbzjqVm%2FgH87aksf%2FM1o%2FPTpaxoZZJFPJok9j9tLS%2FOUXu4Ys7jvAW7CmwuGn%2FkQ5lgQ7myC7UHqu0Qdw9UXT2QEKrgmDcSW2E%2FeuvNMkk9ZWyqSdFO2dy8t9Pdc2z2dxTHe2G%2F3VPDe%2BQ54OrPt8nxHgSk8cHs3Pia0YkpZi5yGqvOnvgPLqEfeCgK0FXUwZbwb87qNDiMDEJ%2BWo2pNcWEYbA8%2Bny0dC6uFF1jrmP11NQh6p7gI2%2B2iurcAp9bNIt39dcP%2Bsa1VIVCUHnP8fLnIgByCUo%2FLUnPRrwYumc18e3SDxJzREVMG4Mis%2FhPqJZJ6CDiR5128d6q3tFAr9esY3TunaC%2BuTwg705jcaFKkclEHvErFMI%2BhitUGOqUBzH39n4D4UQ1D6s0ZD90DrxZEptOj9KYa4wOo8eCkPI4pu6SqRL18iHEASrVQIPkoH7QXvb1iOvKoP%2Ft4s7htFDxrmK84bckob30yp3YeYIK%2BnfsRidS3Uyag%2BzcLNFKaPporf0XeJ%2Fniqm05IFkbeWpdd59JLWjTIPnkvk5y9POmJna%2FNxOMtW3eEiDn4eBqu24wYSp6DaHy2oJ722IEJasOfDPA&X-Amz-Signature=58afc89f858da4afa431aee2946607570192c43b0c5a8fa31f219e4debc022e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







