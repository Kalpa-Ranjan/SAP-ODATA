



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6PZKBP%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T130651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGUge3SnIn6FcL8PtRl%2FSIFKDkct4F0qU0JZmmbBUETkAiEAzbByme9d1P0GsSC3AHZU1DPMm8lwyQvRpk7cE01ENYMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNZ%2F9DyafcPjdNJmircA1RWSCKzH8QG0BOhVG5hcRGjb8UVgi04gQ5Zvi1j1%2Bx51j51hFUkYO2zgagq2CpJkGbpMzH4EXINEJtqSEBWM2K%2Fn0JfuC7DhvJzQ%2FX7T7uSDsRSpVF%2BnHWDAeAk7H2aQfm1ow%2BHqqexCidzJjCr7QEAn5roOwH5PU6Fq3xPw0wYPn8lIDa6i%2BZaz0X8T312zzcifZehnx%2BWw3oMOmdaOOCMY7A8jICjfXARwaUYm6%2Fu%2BZKeYNhDs3ksEem2JnV1bFXcIfYPEcI9YzPfOmZxjySEd2ykZxowBSmbpATgvUzJ0DE3tLX8HEwfRuDx4V79tKK%2B1VN4XEptF04NjLu4EZCwnieN9urf0M0K8bukHtQcPVIIPhCQzoiU9acRVwGQpeM%2Bo9LRVfNuYK6i75iOeMz8O7mM8WGQWNd0GdNTyl6zyRAXuh8sDiG4e5fi%2BzzaiCBTWodPY5e6vnSMN%2Fm82KC%2FDtQlcoiVETTR6FZJ%2F%2FdUI%2B5oQAEdmjctAdKOK0pEiB1de%2Fel03ku7SwRJYXOenFx6DEZWE20q6elSM2b20v%2FFv%2F8%2Bk5uI1b%2BhCTCJlczvJWtEKOBp2zQ9eKBkV0Djs3IJk3m%2FS5K4KjztZ2EmLRbE1Qr5vcDYchzN9K5MJSxgdAGOqUBAnRC1u8FgPdn42ugf86%2FkFKvoUQq11VyeCJlNJbQIMBvTlA6g2W4E6AmOq6nD0KCPVnuDyOTDzFvwJmRfNOJBAm3yVfxUz7wu%2FBWRcGokEOJ7452rW4U2uo7Ej0L50X5es8p2raKTcOYMeiuYpHheCOGRmkpV4g9du8IVx8gpf8Lbil8uDKNbYQTavhmYARbPnfmTI6sMtmyNjm%2FZb8kaeFwoZHk&X-Amz-Signature=aaedc77ae45ed2d83ddae88e7d038dcac777077bd7f89ff9a13912408c797c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6PZKBP%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T130651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGUge3SnIn6FcL8PtRl%2FSIFKDkct4F0qU0JZmmbBUETkAiEAzbByme9d1P0GsSC3AHZU1DPMm8lwyQvRpk7cE01ENYMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNZ%2F9DyafcPjdNJmircA1RWSCKzH8QG0BOhVG5hcRGjb8UVgi04gQ5Zvi1j1%2Bx51j51hFUkYO2zgagq2CpJkGbpMzH4EXINEJtqSEBWM2K%2Fn0JfuC7DhvJzQ%2FX7T7uSDsRSpVF%2BnHWDAeAk7H2aQfm1ow%2BHqqexCidzJjCr7QEAn5roOwH5PU6Fq3xPw0wYPn8lIDa6i%2BZaz0X8T312zzcifZehnx%2BWw3oMOmdaOOCMY7A8jICjfXARwaUYm6%2Fu%2BZKeYNhDs3ksEem2JnV1bFXcIfYPEcI9YzPfOmZxjySEd2ykZxowBSmbpATgvUzJ0DE3tLX8HEwfRuDx4V79tKK%2B1VN4XEptF04NjLu4EZCwnieN9urf0M0K8bukHtQcPVIIPhCQzoiU9acRVwGQpeM%2Bo9LRVfNuYK6i75iOeMz8O7mM8WGQWNd0GdNTyl6zyRAXuh8sDiG4e5fi%2BzzaiCBTWodPY5e6vnSMN%2Fm82KC%2FDtQlcoiVETTR6FZJ%2F%2FdUI%2B5oQAEdmjctAdKOK0pEiB1de%2Fel03ku7SwRJYXOenFx6DEZWE20q6elSM2b20v%2FFv%2F8%2Bk5uI1b%2BhCTCJlczvJWtEKOBp2zQ9eKBkV0Djs3IJk3m%2FS5K4KjztZ2EmLRbE1Qr5vcDYchzN9K5MJSxgdAGOqUBAnRC1u8FgPdn42ugf86%2FkFKvoUQq11VyeCJlNJbQIMBvTlA6g2W4E6AmOq6nD0KCPVnuDyOTDzFvwJmRfNOJBAm3yVfxUz7wu%2FBWRcGokEOJ7452rW4U2uo7Ej0L50X5es8p2raKTcOYMeiuYpHheCOGRmkpV4g9du8IVx8gpf8Lbil8uDKNbYQTavhmYARbPnfmTI6sMtmyNjm%2FZb8kaeFwoZHk&X-Amz-Signature=53557f6c58213b045aee16649db71f79c9a6937210305940f77ff819101080ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







