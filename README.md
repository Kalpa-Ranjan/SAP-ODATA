



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWOLTTNC%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T191218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIHxS1r%2Bn1m%2BK5CzCakRpUM6ibXtV9iWeDZmd9%2B%2BKzQpQAiBmiZ0NdmFVgMOtOCAAKEsAnQ%2BEf4VTJgMzd44JTRW1fSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMSV7fFISwiQXIpZ6qKtwDRG8V0cpeeKoTqGbmhXBv9oQ3OgHtEBR2Hd1xZKF2eDKpi5fTKw1bj9nzSIXZIkgXkRHeUbvA%2FDGH9vQPiTacy%2FMG1DPRIBl6hQlbEoDuS%2Bk60p6fPWKVUYgtU7K2aKZNsz%2FNDtCQ%2FIxFaBXK3cO1tVPMNB2YquzVrmz3YAulGEbVOW%2FXIVa0igBHNy9AQDafGh1tv0iYeyQzpQ3DGNi77BbsBhmBrUInv8hTt1bR7%2BzUH5Tm1BlOvxsoJ7LG6NH4p0wajtFcCKXuVzOhKS5SdMQsUlGogWxyHdG%2FGbfIIYaN2WAbiHlNY2o8NQp62F8ITHgWoRrxkl2SsNxqpzYGsigRD2mVx2kv1yD0lPk%2FiFS9jae7Cfa48h8zEyB0nzCbB3cJb%2FxxWxkQkf%2FoiIp9Qu%2FLS40nOZPXlPNXqcDDjFJN3BKjCbO%2B1ru43Q8Gs2dsIupJY99xJ3VJBjAzgdYYar4Swl42n3LE8bY71RNxo%2Br%2Fw21JiyS%2FzgCC2DB6BVmbFjo5ou9GawNUR4OVOcOfG2DEJLLKtUrGtyAsY5epf%2B7eKHa2buSLS%2BX7HMgbWr%2Bfj4fZ6eJGJG8QgRBXZoRbDic56jpkoCuXRl1LEbJzCKdAFcEL90FC9WmS3jowsbjOzwY6pgFe4tAMZW70xUV%2BVih%2BN1FBuRtevu0F7cGook4CRkT55WKQxaxfEFIEmmWKqg%2Fix%2BUxp%2FyS4a2MMCyPVFQg50XL1Uy8MSND697EkQguIJLebQkIJXyyKc0iluwTynO6ekINtHatvd0IHN3zIJF8ZQzl8HttHBg5vHamie8MfdV7uM4HD7audJIAgCs7rcMkzaUokBwYCsR%2FUXiuDGGtle5oQlcX3aQp&X-Amz-Signature=b5da4b657c66907578f28e3a0392771927cdeabb9500dafb9e41d6979240130b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWOLTTNC%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T191218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIHxS1r%2Bn1m%2BK5CzCakRpUM6ibXtV9iWeDZmd9%2B%2BKzQpQAiBmiZ0NdmFVgMOtOCAAKEsAnQ%2BEf4VTJgMzd44JTRW1fSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMSV7fFISwiQXIpZ6qKtwDRG8V0cpeeKoTqGbmhXBv9oQ3OgHtEBR2Hd1xZKF2eDKpi5fTKw1bj9nzSIXZIkgXkRHeUbvA%2FDGH9vQPiTacy%2FMG1DPRIBl6hQlbEoDuS%2Bk60p6fPWKVUYgtU7K2aKZNsz%2FNDtCQ%2FIxFaBXK3cO1tVPMNB2YquzVrmz3YAulGEbVOW%2FXIVa0igBHNy9AQDafGh1tv0iYeyQzpQ3DGNi77BbsBhmBrUInv8hTt1bR7%2BzUH5Tm1BlOvxsoJ7LG6NH4p0wajtFcCKXuVzOhKS5SdMQsUlGogWxyHdG%2FGbfIIYaN2WAbiHlNY2o8NQp62F8ITHgWoRrxkl2SsNxqpzYGsigRD2mVx2kv1yD0lPk%2FiFS9jae7Cfa48h8zEyB0nzCbB3cJb%2FxxWxkQkf%2FoiIp9Qu%2FLS40nOZPXlPNXqcDDjFJN3BKjCbO%2B1ru43Q8Gs2dsIupJY99xJ3VJBjAzgdYYar4Swl42n3LE8bY71RNxo%2Br%2Fw21JiyS%2FzgCC2DB6BVmbFjo5ou9GawNUR4OVOcOfG2DEJLLKtUrGtyAsY5epf%2B7eKHa2buSLS%2BX7HMgbWr%2Bfj4fZ6eJGJG8QgRBXZoRbDic56jpkoCuXRl1LEbJzCKdAFcEL90FC9WmS3jowsbjOzwY6pgFe4tAMZW70xUV%2BVih%2BN1FBuRtevu0F7cGook4CRkT55WKQxaxfEFIEmmWKqg%2Fix%2BUxp%2FyS4a2MMCyPVFQg50XL1Uy8MSND697EkQguIJLebQkIJXyyKc0iluwTynO6ekINtHatvd0IHN3zIJF8ZQzl8HttHBg5vHamie8MfdV7uM4HD7audJIAgCs7rcMkzaUokBwYCsR%2FUXiuDGGtle5oQlcX3aQp&X-Amz-Signature=226a1d42f921d72ebee4b4a39a15227abc23dcb4882f8552705711b5c3a14b32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







