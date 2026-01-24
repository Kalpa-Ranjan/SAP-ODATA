



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJYLRRR3%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T062519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDJGqTUscQWsF6VP4PpRlgtPPxPqoQWUPqbuiLB%2FM%2BL3gIhALpwNcObk5m2aj9JaoPw%2BKFWgcxwWmpgOUXhtRmzoGH7Kv8DCAcQABoMNjM3NDIzMTgzODA1Igwfz2vuAeJXBoU9vB8q3AOH5AXYSj39q3TYe6r4bHHli3mPgiFie22Ue2Y8QANdl%2BZLUageHQBojt4zIqJHExs2kwnxwhreIlyKRc0Vhzee2qWRuY2XiUoiSo1rTFIjXhm2AMzWxbLuKFQeNLAYYLhqxCGTT1%2B%2BK0gA%2F%2BYQNFDA2Ld47uFxbCkfBXWPv7LD%2BbPOhmpuLcIkcqGaM%2FuqgmRBos%2BB2dPAftq8LBJhfk4PXiGKgqyuuvPIrIoM3CmMwZpYEVhfpj5%2Bu4znFbGx67nNq7kbzWXNHHKDp4UONHdPF4yVHj2fht0ViRkH00KknUf0yNCJikBHl6O1kdXBn7lEXBRnjdmIEwXkbC4XrKt0IPCeH1iyOW5jE2F3M19SpmAxIWHOeG8lO9ifhiX3fEK1YdARMHnngxi17cP8t4Q3nSqkTfNdIfidH2y26FWDn9hJQYTEGPi6Bhx%2FNdMhGyVBahU9veAZkJR968YyoEBqFtMyVqIOkqFmHjVysycyAegOdRuer2r20OH0qcfJ2Nigkd2ViFy6wGfR68nV9c32XzB4XeoJvuTUFYAdt9WeDrT%2FDKYQXIt4xeeS2gFwcjgyLCUXtvQC2u0xnw9rmZV8Qm1UCSoggD2WVqRX9Y37JMPiL62JQinJGCc6fzDNxNHLBjqkAfRCosoGw4MHMbsHbJEnJPdiSNn7zqRYyDK7mqHSJdCU60v9e4ttvIpfOEFFHvFko%2FljZEkpBiDM7s6pXE%2FMuDpCKz7XAZKQX9yKBB4QSi4doyEUokuKUH2OLMGO3PQ49%2B2JmqsFZzW6eSrsfW90Pi5c6vD5K2l%2BO9jYXuDCpm2Nd09hHsrucr7%2FQH18WvLu%2Ba87f8x0wqjDkrf8d%2BnvwlRqJQTq&X-Amz-Signature=3bff630e305d668436b905ef9e321132d5c47c6c1720904e215d55c2662b77f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJYLRRR3%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T062520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDJGqTUscQWsF6VP4PpRlgtPPxPqoQWUPqbuiLB%2FM%2BL3gIhALpwNcObk5m2aj9JaoPw%2BKFWgcxwWmpgOUXhtRmzoGH7Kv8DCAcQABoMNjM3NDIzMTgzODA1Igwfz2vuAeJXBoU9vB8q3AOH5AXYSj39q3TYe6r4bHHli3mPgiFie22Ue2Y8QANdl%2BZLUageHQBojt4zIqJHExs2kwnxwhreIlyKRc0Vhzee2qWRuY2XiUoiSo1rTFIjXhm2AMzWxbLuKFQeNLAYYLhqxCGTT1%2B%2BK0gA%2F%2BYQNFDA2Ld47uFxbCkfBXWPv7LD%2BbPOhmpuLcIkcqGaM%2FuqgmRBos%2BB2dPAftq8LBJhfk4PXiGKgqyuuvPIrIoM3CmMwZpYEVhfpj5%2Bu4znFbGx67nNq7kbzWXNHHKDp4UONHdPF4yVHj2fht0ViRkH00KknUf0yNCJikBHl6O1kdXBn7lEXBRnjdmIEwXkbC4XrKt0IPCeH1iyOW5jE2F3M19SpmAxIWHOeG8lO9ifhiX3fEK1YdARMHnngxi17cP8t4Q3nSqkTfNdIfidH2y26FWDn9hJQYTEGPi6Bhx%2FNdMhGyVBahU9veAZkJR968YyoEBqFtMyVqIOkqFmHjVysycyAegOdRuer2r20OH0qcfJ2Nigkd2ViFy6wGfR68nV9c32XzB4XeoJvuTUFYAdt9WeDrT%2FDKYQXIt4xeeS2gFwcjgyLCUXtvQC2u0xnw9rmZV8Qm1UCSoggD2WVqRX9Y37JMPiL62JQinJGCc6fzDNxNHLBjqkAfRCosoGw4MHMbsHbJEnJPdiSNn7zqRYyDK7mqHSJdCU60v9e4ttvIpfOEFFHvFko%2FljZEkpBiDM7s6pXE%2FMuDpCKz7XAZKQX9yKBB4QSi4doyEUokuKUH2OLMGO3PQ49%2B2JmqsFZzW6eSrsfW90Pi5c6vD5K2l%2BO9jYXuDCpm2Nd09hHsrucr7%2FQH18WvLu%2Ba87f8x0wqjDkrf8d%2BnvwlRqJQTq&X-Amz-Signature=e62c4f803ee56cb4d265e29af428d3177e88c59adb6ae83308253a77f1f8f026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







