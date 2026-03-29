



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AADQ4FE%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T183503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCpJu4lnhA6UrDXT%2FOWUuzzoxS0MNik8zHBoBIlVJ%2FgpgIhAP8srsuN9QXgwXyxHDRqjwQmcJn5r9IgxBqE8EezNrgoKv8DCBMQABoMNjM3NDIzMTgzODA1Igw5%2FjN9V%2BValEXi%2FQgq3APj9APGemP5pPvthbIAFKOceCNovHcxXgIxuLivhX%2FUOiKGG44Y6afjojsb%2BN2BaVeTbBcqdjE7Of8MOrOHroF%2Fq%2Bjl72XPDYFsk6zs7I1HV8znQtBGzFjAyNW4suD%2BGrDyuKKuF9okGf5WO74KM1p2rnIm9V7dgok%2FtrTHj%2F9UQ4P9mBkGX633YqM%2BFI%2Biwr0hbCiDvntBYgo0%2FTGFxLzyd0Xj5vm4SfIcjH3YXvZxGPzl38vlGnw2pULK00fXSQVmAwEqTSGsNdiWM8K0AraXCf5L0D7yeGcWQOM1A4si29o0AQeaj08uEbf3LF%2B9PfEAR%2FB1%2BB6eZ7JkKAvNOvZYLABOMK0G1%2BZ4N1izZJLGzUN49uME5kkhlGLmB7aBoZfM0fbIpdLs9%2BTTHutsgniaoTnXqHauXnJw61HTuVc1sOrCVKxGBv59ikc%2B1qM5OjA5VaNatUfl8ezAgOa%2Bk6NbVwAhCW0TwwMio4EUDWLKJNXmGVts%2FpBqX8RdxVU3n38YTR4OEbMKK7fz3O2JbK%2BRKRUz6pYlfvSunl6ZYUp8%2FyzVSChf3Xak8LcOh5TS0yN884pH5MxI3uPHt61c0BbcCBdIPCWiTUPvowdPD8%2BXz1CdfMepVpd5eAVo4TDh2qXOBjqkAWEgDZzMyuZGZSMDogrcUJKymFVY1N0LuYSUMHyju8QTBD0G78uKOhD%2BRD8k9sDdDbFwKbi7pSIAY0o2AK0zeBmGDrYg0HCBDWbai60tw9J2UiQm6TlRBzpNnHwhrd0PdGp%2BbNYQ12nHO26gFgqp6Ec6vpaOYrMVrw4FH77%2BVHgPBbao3q%2BiGS1foPXm0ykYI%2FlL4o0JCkJ2Ir5KmcO8C8Dyr%2F5g&X-Amz-Signature=2b15a58d2500d74482ccbc8ea38c050f31257cf98b98a527f766e006792c914d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AADQ4FE%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T183503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCpJu4lnhA6UrDXT%2FOWUuzzoxS0MNik8zHBoBIlVJ%2FgpgIhAP8srsuN9QXgwXyxHDRqjwQmcJn5r9IgxBqE8EezNrgoKv8DCBMQABoMNjM3NDIzMTgzODA1Igw5%2FjN9V%2BValEXi%2FQgq3APj9APGemP5pPvthbIAFKOceCNovHcxXgIxuLivhX%2FUOiKGG44Y6afjojsb%2BN2BaVeTbBcqdjE7Of8MOrOHroF%2Fq%2Bjl72XPDYFsk6zs7I1HV8znQtBGzFjAyNW4suD%2BGrDyuKKuF9okGf5WO74KM1p2rnIm9V7dgok%2FtrTHj%2F9UQ4P9mBkGX633YqM%2BFI%2Biwr0hbCiDvntBYgo0%2FTGFxLzyd0Xj5vm4SfIcjH3YXvZxGPzl38vlGnw2pULK00fXSQVmAwEqTSGsNdiWM8K0AraXCf5L0D7yeGcWQOM1A4si29o0AQeaj08uEbf3LF%2B9PfEAR%2FB1%2BB6eZ7JkKAvNOvZYLABOMK0G1%2BZ4N1izZJLGzUN49uME5kkhlGLmB7aBoZfM0fbIpdLs9%2BTTHutsgniaoTnXqHauXnJw61HTuVc1sOrCVKxGBv59ikc%2B1qM5OjA5VaNatUfl8ezAgOa%2Bk6NbVwAhCW0TwwMio4EUDWLKJNXmGVts%2FpBqX8RdxVU3n38YTR4OEbMKK7fz3O2JbK%2BRKRUz6pYlfvSunl6ZYUp8%2FyzVSChf3Xak8LcOh5TS0yN884pH5MxI3uPHt61c0BbcCBdIPCWiTUPvowdPD8%2BXz1CdfMepVpd5eAVo4TDh2qXOBjqkAWEgDZzMyuZGZSMDogrcUJKymFVY1N0LuYSUMHyju8QTBD0G78uKOhD%2BRD8k9sDdDbFwKbi7pSIAY0o2AK0zeBmGDrYg0HCBDWbai60tw9J2UiQm6TlRBzpNnHwhrd0PdGp%2BbNYQ12nHO26gFgqp6Ec6vpaOYrMVrw4FH77%2BVHgPBbao3q%2BiGS1foPXm0ykYI%2FlL4o0JCkJ2Ir5KmcO8C8Dyr%2F5g&X-Amz-Signature=f4e1dcc60a074c12402ee64bad01fa52e326cfacd55dce306b284258da016ae5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







