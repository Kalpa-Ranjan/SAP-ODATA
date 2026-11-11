



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFM27BRV%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T001245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD92Qhe%2BIprCAGJzYua5cNNQoN0kb0UoRX2xkvBZVyp9wIgXHfCslQiZAVA%2FYF5W7Drn2l%2FUrjmBmiJrDkNVYHDddwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDOuxJcku0osGBHS8ZircA2D1CRkeCYWbNLG%2BLZ9L7RiBIbAt4R196J9dlKBNBVCSoT6ZxHQYytOsLZgktGBGtVM3bKe0g4pm9FtCjIfLoor6G6n1m8UWo%2BxWHOLGTowUKLkD3xfqOvNJt9u4tXFoiPtz5e72KeWlhuuFMNpjUYC9vlCPp0ZRIvXWp2vOTOZB9X7qU%2Bchhtb2C9pxhjn%2FE0g%2BWg5jmqcauCoQarGSZTbuH9f0xYmUgdTNO7kPffzyhoiLkDGuyaFEdjdkAyP77a9m5QD2u0BBO4e85OHZMwUqCyAQQsfTGX6o4dc%2BkdJh15NtmjgKM5XL7K8Da4oLNsB0G8CGkhvRm5qtKFpKv4r%2Fd3J7Y%2F%2BJzx22X4srxMcCoWOMul2Gfn2%2F4kvVmzEu2QL4yBaR2aF%2BmLYkQ%2FijHKwBPx5%2BsL0dR06IV4xAFjbLdogp9%2F%2F7TIKiHGaJjRg9WGnavetKzIt1%2FPsuZHXM4A6LKe4%2Fn7qKWeKXXpi1Z1xO2yEQOifi%2BxjOf33y5vvadFHAfRfp8XarPJ9wtuXGzLYTCbuiG16zljLS%2FEkFRXHR0M%2FZIHF8fRLXa2GmOoIbFGOkcti4Bvw05CR0ZYqTdVrN9kFHtevxPnun7M3fLvhXocpV47%2FG2adG0mUUMJTVztcGOqUBLEivjR31r3PJmhZHomVChvYOfk0nEK%2BLPTU6bRdU6Lfab9qxfYRGmPyVeFXBI80r%2FHTEIvwFXF0Ss6E7K3S7lcnH%2FsZeCME648%2Bmmrzx0GJ47hyOC61WQPyc53PNDZ1%2FxLifkd%2FHIVgh5bXuwZSnkeY7IdR%2F5WRgjZdraPhA%2BKfwULVs7r8%2B470qmkddXf39jWVZ%2BxHqTd2Jc%2FgY1H74mAoNQxiz&X-Amz-Signature=9a27ff5a5aa71e2bc35f96a22f6b54656983f5f05fb04234cb890f4b8a86276e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFM27BRV%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T001245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD92Qhe%2BIprCAGJzYua5cNNQoN0kb0UoRX2xkvBZVyp9wIgXHfCslQiZAVA%2FYF5W7Drn2l%2FUrjmBmiJrDkNVYHDddwq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDOuxJcku0osGBHS8ZircA2D1CRkeCYWbNLG%2BLZ9L7RiBIbAt4R196J9dlKBNBVCSoT6ZxHQYytOsLZgktGBGtVM3bKe0g4pm9FtCjIfLoor6G6n1m8UWo%2BxWHOLGTowUKLkD3xfqOvNJt9u4tXFoiPtz5e72KeWlhuuFMNpjUYC9vlCPp0ZRIvXWp2vOTOZB9X7qU%2Bchhtb2C9pxhjn%2FE0g%2BWg5jmqcauCoQarGSZTbuH9f0xYmUgdTNO7kPffzyhoiLkDGuyaFEdjdkAyP77a9m5QD2u0BBO4e85OHZMwUqCyAQQsfTGX6o4dc%2BkdJh15NtmjgKM5XL7K8Da4oLNsB0G8CGkhvRm5qtKFpKv4r%2Fd3J7Y%2F%2BJzx22X4srxMcCoWOMul2Gfn2%2F4kvVmzEu2QL4yBaR2aF%2BmLYkQ%2FijHKwBPx5%2BsL0dR06IV4xAFjbLdogp9%2F%2F7TIKiHGaJjRg9WGnavetKzIt1%2FPsuZHXM4A6LKe4%2Fn7qKWeKXXpi1Z1xO2yEQOifi%2BxjOf33y5vvadFHAfRfp8XarPJ9wtuXGzLYTCbuiG16zljLS%2FEkFRXHR0M%2FZIHF8fRLXa2GmOoIbFGOkcti4Bvw05CR0ZYqTdVrN9kFHtevxPnun7M3fLvhXocpV47%2FG2adG0mUUMJTVztcGOqUBLEivjR31r3PJmhZHomVChvYOfk0nEK%2BLPTU6bRdU6Lfab9qxfYRGmPyVeFXBI80r%2FHTEIvwFXF0Ss6E7K3S7lcnH%2FsZeCME648%2Bmmrzx0GJ47hyOC61WQPyc53PNDZ1%2FxLifkd%2FHIVgh5bXuwZSnkeY7IdR%2F5WRgjZdraPhA%2BKfwULVs7r8%2B470qmkddXf39jWVZ%2BxHqTd2Jc%2FgY1H74mAoNQxiz&X-Amz-Signature=94584dd17fb7f0143cfa71482ccd61366e7f3568ef4401c1abda34f1f55d4571&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







