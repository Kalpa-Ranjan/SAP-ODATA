



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HTRIRB%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T123126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCICYbD8Z%2BvHh4CwEgUFmbfGOc389g68RX0XU2H8EnZV04AiEAgmLY3kINCXaXM%2BmXqwC%2BBt5OrOouQkSEks9ASx1EF7kq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDHTTo1sEFsUm8Noz6CrcA7DYHKEuNtBpHoT13kCzVmVhX9oJ%2BxcBDTQTrgb0CtyNi1mL%2BZxm1EGn7q3X8zsPk2cte49p%2FSlIGxRacb4HCZh7qrbf9HcGDrfEsGYRVNcRwDs0%2Fjk04HYm94ad2WxeouZuzn4Rv%2BaBZsSSzfYijSaDKNUgAHt%2FSbDHuJL0o6A9TcRcaHJJ7DY92EKU90iRMDetlDAVCMAyFo%2BkuhppoBpJswuRUWEnqXJA116UVxR8RZxNdAeRX0XAx1OjLV%2BltNIz5pvlBWrPVFCltx5bZxK%2FppPqgapnmvs3GBp5vjDlemuERxb3WBcjZFecrQcbg6AL%2BD3E7s%2Fu9fY%2F1%2BDHRCPNwq%2FeG3guv4rQs0LpcrqFKeeilbet4sCEH3DfWpGKsKUp8PVrzig8F%2FL8crbCnYCYVCjK3QTREMz5PSFm8WONCjMjZK6PuVV1%2B6TD1RTTQ%2FCAcf1zbzkSHUgNI5%2Bf8K%2FQJ6DSJrUACkvYy3Mt5pOs0UgUCr2LDqCdrqMvOkUz1maL3Ot9COZ03g46iFS2Ulj5yP0mm75enoXcztZk4g5ZDBsf4XXRwEDgI%2FzT6o2KIk5CARM7AHoprbwwn%2FidKToUDcfmEgJ0iljGhwonSuNwqAEoWRCSPHfjbsQ0MJCw6coGOqUBjLOR%2BuJDnOZ%2BQTl%2F5z5g3kSyHcXB3DQy4XQyy3bMFTKMI2dKNQ5ivE%2BQ9fkAryHrgNpd2baILXFDNMB5uRLCmjD9NpBuT9VXP0Daar1ueTPFqB2D3qnmB0qD9FmmFiR03SjCgRCmU%2BwJn%2B%2FuMppgi4OoaQvIFoYRCqvYpHoTue8DAHYStQTJuFyRFCJOz4rDw9%2B2%2B9eFHDWM8HnBq6h10gsGeque&X-Amz-Signature=53bb633acffd6833c240084c08a9f841b97b7816d24bfb11d08b0c0704750d9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5HTRIRB%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T123127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCICYbD8Z%2BvHh4CwEgUFmbfGOc389g68RX0XU2H8EnZV04AiEAgmLY3kINCXaXM%2BmXqwC%2BBt5OrOouQkSEks9ASx1EF7kq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDHTTo1sEFsUm8Noz6CrcA7DYHKEuNtBpHoT13kCzVmVhX9oJ%2BxcBDTQTrgb0CtyNi1mL%2BZxm1EGn7q3X8zsPk2cte49p%2FSlIGxRacb4HCZh7qrbf9HcGDrfEsGYRVNcRwDs0%2Fjk04HYm94ad2WxeouZuzn4Rv%2BaBZsSSzfYijSaDKNUgAHt%2FSbDHuJL0o6A9TcRcaHJJ7DY92EKU90iRMDetlDAVCMAyFo%2BkuhppoBpJswuRUWEnqXJA116UVxR8RZxNdAeRX0XAx1OjLV%2BltNIz5pvlBWrPVFCltx5bZxK%2FppPqgapnmvs3GBp5vjDlemuERxb3WBcjZFecrQcbg6AL%2BD3E7s%2Fu9fY%2F1%2BDHRCPNwq%2FeG3guv4rQs0LpcrqFKeeilbet4sCEH3DfWpGKsKUp8PVrzig8F%2FL8crbCnYCYVCjK3QTREMz5PSFm8WONCjMjZK6PuVV1%2B6TD1RTTQ%2FCAcf1zbzkSHUgNI5%2Bf8K%2FQJ6DSJrUACkvYy3Mt5pOs0UgUCr2LDqCdrqMvOkUz1maL3Ot9COZ03g46iFS2Ulj5yP0mm75enoXcztZk4g5ZDBsf4XXRwEDgI%2FzT6o2KIk5CARM7AHoprbwwn%2FidKToUDcfmEgJ0iljGhwonSuNwqAEoWRCSPHfjbsQ0MJCw6coGOqUBjLOR%2BuJDnOZ%2BQTl%2F5z5g3kSyHcXB3DQy4XQyy3bMFTKMI2dKNQ5ivE%2BQ9fkAryHrgNpd2baILXFDNMB5uRLCmjD9NpBuT9VXP0Daar1ueTPFqB2D3qnmB0qD9FmmFiR03SjCgRCmU%2BwJn%2B%2FuMppgi4OoaQvIFoYRCqvYpHoTue8DAHYStQTJuFyRFCJOz4rDw9%2B2%2B9eFHDWM8HnBq6h10gsGeque&X-Amz-Signature=1fd4dba1efb2b558e74c9a20285e5cbbbe8ffbcb82fdf2d738a925cb07c1164f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







