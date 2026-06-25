



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6Z3D3TR%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T085233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxBeTAZHMDn%2BKyB3IHL1aVL%2FAowxoCWza6SzoYhDA7jAiEAmF4VRq56CcaPD5YH6CWK2dBXYiA0X6WH52onvhjdiZUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGAbE18hsOdYscOhaSrcA7d1irdxjAprvq4I07dA2Yz68IhARhmCwfuf65g5gjhHq%2FEedn4ONhYgyyW3D%2BJBCQMZ3O%2Fm3RjKY1pVkprS5xq7Gs6oc229qRRONq22913YWYHrOaE5ShqPk9ah0rFcCogiIQ%2F4JZPiEqDIsulMdBoCyjMS7HnEMUXoIRjeiOGMCZy%2BCfvvICunZyt48SIjZMkNDxfknpBtC9mNyPIdeXVOm%2FFieAKCvGxkVVnCPPVlVsAedcdTFMFdmM3gBfE1IR1NXDuEozKL7L8dgxzuVrHG0Z8i38miZ1IMtlrr4quDddchfTuIAL7bC1tcdHwAtCHp8%2FRV7sYTSJDMlvmRWOCif9f2CXo9OGxRLxZnys2uXWr06Fw8QPEHOCeSiQt4puzRxpMn95VKJmephJ9gU8%2FnjVlKsakj181VAyEJBqObo7qjtXeCLx60UJWh655QjIz8%2FZoK1ZxSevqwMw6fTQmU18RWcY8%2BwImzHB8z4FaC4DpiiDJM3AOp0uc3YH2dk5BReT3WeWADmQfS4WlYCT%2F8LcSvL2FjlpXIUpNP8ipy4CTobq%2BpDIZeTFzXcbP23AfvOWaEpqFmt5KnxkvkG3HM%2BwCGJejcXWY8v6IM6cfblDzviyOPgp32BfJ4MNXO89EGOqUBV6bagchUd7gmq%2FNV3xs91YkNT9W5R8O0LGavv0VToy7Z1Z0NwB9abdDiQQft1o5aDRHxC6M2npg8a1WMQ%2FWe%2BeZkfGkJg9zMvBCBTtoyigK4ZwAEpcPpr2e6JZx%2BSagy21RMyQg8l4zvSs0SRIMv1O3ziGORXKcIlkyuV%2FG9MRiGtZ3JFom0Jntwaw2OH2wkLt65LpC34fRcLYvOwSbx6HNTGNG8&X-Amz-Signature=f2650b6ab1c56ed3dbb8e1f47fba11f0664ed303051873e3391498387a7e4ac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6Z3D3TR%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T085233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHxBeTAZHMDn%2BKyB3IHL1aVL%2FAowxoCWza6SzoYhDA7jAiEAmF4VRq56CcaPD5YH6CWK2dBXYiA0X6WH52onvhjdiZUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGAbE18hsOdYscOhaSrcA7d1irdxjAprvq4I07dA2Yz68IhARhmCwfuf65g5gjhHq%2FEedn4ONhYgyyW3D%2BJBCQMZ3O%2Fm3RjKY1pVkprS5xq7Gs6oc229qRRONq22913YWYHrOaE5ShqPk9ah0rFcCogiIQ%2F4JZPiEqDIsulMdBoCyjMS7HnEMUXoIRjeiOGMCZy%2BCfvvICunZyt48SIjZMkNDxfknpBtC9mNyPIdeXVOm%2FFieAKCvGxkVVnCPPVlVsAedcdTFMFdmM3gBfE1IR1NXDuEozKL7L8dgxzuVrHG0Z8i38miZ1IMtlrr4quDddchfTuIAL7bC1tcdHwAtCHp8%2FRV7sYTSJDMlvmRWOCif9f2CXo9OGxRLxZnys2uXWr06Fw8QPEHOCeSiQt4puzRxpMn95VKJmephJ9gU8%2FnjVlKsakj181VAyEJBqObo7qjtXeCLx60UJWh655QjIz8%2FZoK1ZxSevqwMw6fTQmU18RWcY8%2BwImzHB8z4FaC4DpiiDJM3AOp0uc3YH2dk5BReT3WeWADmQfS4WlYCT%2F8LcSvL2FjlpXIUpNP8ipy4CTobq%2BpDIZeTFzXcbP23AfvOWaEpqFmt5KnxkvkG3HM%2BwCGJejcXWY8v6IM6cfblDzviyOPgp32BfJ4MNXO89EGOqUBV6bagchUd7gmq%2FNV3xs91YkNT9W5R8O0LGavv0VToy7Z1Z0NwB9abdDiQQft1o5aDRHxC6M2npg8a1WMQ%2FWe%2BeZkfGkJg9zMvBCBTtoyigK4ZwAEpcPpr2e6JZx%2BSagy21RMyQg8l4zvSs0SRIMv1O3ziGORXKcIlkyuV%2FG9MRiGtZ3JFom0Jntwaw2OH2wkLt65LpC34fRcLYvOwSbx6HNTGNG8&X-Amz-Signature=827c3af28cff426727a26e2f84f755e33cd0495cf4dedec2476ee66052eb2a7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







