



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF52ADW5%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T124118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5dJHlQclI7b4vUV2zzY%2B0i7J0vKJ89s6uVgLcEh46bwIhAKnlzNwV21rV%2BpROVYekVlPvnnqIQQkdT5mvey096MbvKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVLAt%2BhlUOktaksnUq3AP6YX0zLDs1AehmAZXTpTdpqWdv6oiASEw1yxnH9qpExhcyelmYXmAPZ4UPlkk2Mu9yXKXYJQKG63BFrjuPoRTfHMzu9v9iApbR372L%2BsIrz%2FZX2ozU9mLhCDIDCF5hP6EtQK0ej65dkPUQ1t7Heloy%2FxJg9uGdhNkR7NtRb2goG0QWq59rUYYd3A7FbcPdeK%2FeSNfjMpcRRn3dgNbB4E0QgMF4HM%2F1BlLWM4L6B%2FDYOm2EbpM500j2qa3bQeROrXnZ48MfG6ETo5GXhye%2Bup5Raa%2FriNzIxxfuE%2FhQYbTeC1PQv%2F45vJJmhGqGYn04oGS1GO1U6A2RpSCak9thGUrn9CpdmM7XqOvR1%2B4vOKJO27QVWP75QiuH19MuNJe23BelvQTejJtZTxpOSvRKbt1Xdfzl%2F8EyBxb2ijOQBi%2FIidLYiWfilXrTnYzPXT0fnC6s6HJdMqlM20FIPgFw6tyN0fic8uykAKdm%2BM8X6mwo19wA3ZMWnjMDtV9BGOCq2IYqF0P96cI%2Ba4xd6%2FH%2BhhDpRagzXbHfSf6QVDpEAuWbyZdabayNWcF9EvRWplo2zDewqhDyofKUHWRX3CBK9zw8hygE67Khyf2IrFHSRci9kM7p4it%2FLiR6gHhr9zDx3dnNBjqkAW%2BFRPLbpCRSSHZbvsJ8NQgQKaPhK72PwyKvW6972h44jl0LLCT98kksLe%2FCuaYUsAALSxOA8CrXRyPj6Zsj4Aq6Y99w%2FVPX0tZKaIdrXhMwtOm5jb6Wz%2B4YCCFh41qZqPaVyWTqCfBKMVHnO9VL6AqAhTxm2JpT%2Bxp5mgbBJdU1NnMrZ6fer%2FDeEacHifowl%2BA%2BFt%2FkJDJ0EzEwKNaaPf9D6zQ7&X-Amz-Signature=be61de0d6391aea69a65f877f347175fec0d212ae079dfb6ec1b54f21edcdb91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF52ADW5%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T124118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5dJHlQclI7b4vUV2zzY%2B0i7J0vKJ89s6uVgLcEh46bwIhAKnlzNwV21rV%2BpROVYekVlPvnnqIQQkdT5mvey096MbvKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVLAt%2BhlUOktaksnUq3AP6YX0zLDs1AehmAZXTpTdpqWdv6oiASEw1yxnH9qpExhcyelmYXmAPZ4UPlkk2Mu9yXKXYJQKG63BFrjuPoRTfHMzu9v9iApbR372L%2BsIrz%2FZX2ozU9mLhCDIDCF5hP6EtQK0ej65dkPUQ1t7Heloy%2FxJg9uGdhNkR7NtRb2goG0QWq59rUYYd3A7FbcPdeK%2FeSNfjMpcRRn3dgNbB4E0QgMF4HM%2F1BlLWM4L6B%2FDYOm2EbpM500j2qa3bQeROrXnZ48MfG6ETo5GXhye%2Bup5Raa%2FriNzIxxfuE%2FhQYbTeC1PQv%2F45vJJmhGqGYn04oGS1GO1U6A2RpSCak9thGUrn9CpdmM7XqOvR1%2B4vOKJO27QVWP75QiuH19MuNJe23BelvQTejJtZTxpOSvRKbt1Xdfzl%2F8EyBxb2ijOQBi%2FIidLYiWfilXrTnYzPXT0fnC6s6HJdMqlM20FIPgFw6tyN0fic8uykAKdm%2BM8X6mwo19wA3ZMWnjMDtV9BGOCq2IYqF0P96cI%2Ba4xd6%2FH%2BhhDpRagzXbHfSf6QVDpEAuWbyZdabayNWcF9EvRWplo2zDewqhDyofKUHWRX3CBK9zw8hygE67Khyf2IrFHSRci9kM7p4it%2FLiR6gHhr9zDx3dnNBjqkAW%2BFRPLbpCRSSHZbvsJ8NQgQKaPhK72PwyKvW6972h44jl0LLCT98kksLe%2FCuaYUsAALSxOA8CrXRyPj6Zsj4Aq6Y99w%2FVPX0tZKaIdrXhMwtOm5jb6Wz%2B4YCCFh41qZqPaVyWTqCfBKMVHnO9VL6AqAhTxm2JpT%2Bxp5mgbBJdU1NnMrZ6fer%2FDeEacHifowl%2BA%2BFt%2FkJDJ0EzEwKNaaPf9D6zQ7&X-Amz-Signature=2f231bfe07a4c5040056d7f8bdf74c392046865ed39308c3bb82e7653efa988a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







