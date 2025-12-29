



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOTQIRJ%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T062806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyc%2FnkTaWk9k7o2NHJX2gwtpZd0P%2BNfwIo3vBN9NR2zQIgAd7o9gt9Z6F81CpPLRvP1DisHUvKXO5yoqFDxpa1X6QqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXPqjK0eVXXGrSLCircA7GRdDGvmDY28gG1pPjqY%2BK%2BSSEzt6kWWvynN1JYemVISH8v58qhIjSHJ2Twgnlqsi74z4ys2d0sR0CzTARazDwLvSrDiwKDwT7%2FELddyTQqcppx%2F5FcFJNB1XORiOYLVBLCKV5xVEJLu9lCx5%2BVv%2FOs%2FHCpUDIghzb%2BUiZORYQrOiURuReHnn2a79gdnT1sJfgH0tzX1QuzFDDjZZhy0tc%2FedxNMhhRzSpF2DSA1WvGgTf0RueFabAOHzEzOxcxKlbTudj9rBtZ9ScFkQRehhouZhs6AtgmzUrUtRMJY39xZpXGz%2BQ9Uh1%2FRe9W0zQYoGlUF5Cvui%2FUGAso4E5ndgiLSxodbefTAUA8TbSR28cBXVy7gF90Rbywm2tFonj7DEit3ZoWioXz3l%2B0y%2BgrXhWF3YLSDt2vkWzaHRVWOxNHMlod3sAfpuSbN0f1pujSFwLEy6%2Bd8%2BbG96BfAXIpQyQa22OXhmSkXafvY0Q092EfMDyrkJPACRbn47ires7T0ZXh8t4dz3DSka2R2lcD5hVZL9xAMf0woCw0%2Fy9gfMAZfr37ibp1rKa2tnq%2BmUp%2Fs7utZt%2BSHYpXeULo39caWEet836uywK3fVFyIxMlG5Rtd1OEbmcc4CBwWSsGMJqbx8oGOqUBYo%2FnR3TJHxO1TlK9UOQjXfcBW1kW2mmBJx9%2F38OzYo70Nywk%2FCmuMm0TeA%2FMAucHh04JxmFJtn8MTp5p3GOErj68Bv8YJx4izp3ssoc0mRoCb6ZLNjIZqSOGowZoS40fSgLW6lEiNGOSS%2FKAZgrKxVu%2BZdJsov8HxPnv50nKsYitDoDgzkJZ4UjWaSSN0EefAz54jkGJQtbEwPogQwPpILvQ4KAI&X-Amz-Signature=6ce66c777e824736aa7dd8380b6b1136fdc6eab04f83bc9714209a48096120cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOTQIRJ%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T062807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyc%2FnkTaWk9k7o2NHJX2gwtpZd0P%2BNfwIo3vBN9NR2zQIgAd7o9gt9Z6F81CpPLRvP1DisHUvKXO5yoqFDxpa1X6QqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXPqjK0eVXXGrSLCircA7GRdDGvmDY28gG1pPjqY%2BK%2BSSEzt6kWWvynN1JYemVISH8v58qhIjSHJ2Twgnlqsi74z4ys2d0sR0CzTARazDwLvSrDiwKDwT7%2FELddyTQqcppx%2F5FcFJNB1XORiOYLVBLCKV5xVEJLu9lCx5%2BVv%2FOs%2FHCpUDIghzb%2BUiZORYQrOiURuReHnn2a79gdnT1sJfgH0tzX1QuzFDDjZZhy0tc%2FedxNMhhRzSpF2DSA1WvGgTf0RueFabAOHzEzOxcxKlbTudj9rBtZ9ScFkQRehhouZhs6AtgmzUrUtRMJY39xZpXGz%2BQ9Uh1%2FRe9W0zQYoGlUF5Cvui%2FUGAso4E5ndgiLSxodbefTAUA8TbSR28cBXVy7gF90Rbywm2tFonj7DEit3ZoWioXz3l%2B0y%2BgrXhWF3YLSDt2vkWzaHRVWOxNHMlod3sAfpuSbN0f1pujSFwLEy6%2Bd8%2BbG96BfAXIpQyQa22OXhmSkXafvY0Q092EfMDyrkJPACRbn47ires7T0ZXh8t4dz3DSka2R2lcD5hVZL9xAMf0woCw0%2Fy9gfMAZfr37ibp1rKa2tnq%2BmUp%2Fs7utZt%2BSHYpXeULo39caWEet836uywK3fVFyIxMlG5Rtd1OEbmcc4CBwWSsGMJqbx8oGOqUBYo%2FnR3TJHxO1TlK9UOQjXfcBW1kW2mmBJx9%2F38OzYo70Nywk%2FCmuMm0TeA%2FMAucHh04JxmFJtn8MTp5p3GOErj68Bv8YJx4izp3ssoc0mRoCb6ZLNjIZqSOGowZoS40fSgLW6lEiNGOSS%2FKAZgrKxVu%2BZdJsov8HxPnv50nKsYitDoDgzkJZ4UjWaSSN0EefAz54jkGJQtbEwPogQwPpILvQ4KAI&X-Amz-Signature=2ec91790da7ec61177e3a1d71e937719f8ce0c74c0a9330a41d4f8321e94b919&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







