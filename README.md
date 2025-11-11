



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ANFTX52%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T123147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIExmNapP82xp7Rm3osjVXv%2FtaeJecNeM3NvL%2Bt%2ByZoCyAiEA8gNBgyLCrWgzKF7cWaX70msmjjXzuESxc3twJOII5kEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDKFNkTkFtFnW635dmSrcAwaX36PY1IjnhC2JrB46j7DdafOsIehM4NAT2zrGEVRijdHwayYxUPMM0pGsEtiaQDmvPmObH28qbzuE9luWNrTQ7FcMASFx%2F4nS4c4K2eECAXOdbL%2FzMFQ3Q6wlXUelhyp4vu%2FxZCqVwVht4v%2Bv2BHPl%2Bhnpx1V44JabRZjKzd8iP9IXqiLZSxy1EhMVtVf9GvGracPKT9bMf7ylsTJNcWoO6UoxzDkNg2T9xxxCD%2BsdMjPnHPVeZVAEkhBcmvVJkLcOEWzSJx2NZH8ZeJ7uPLuBCiwd5p%2BnvK0MIiQHpWHmRVNTDzbCt0%2FTOOFentyDJpmKAO8jK4331jbvo0BGz9wXPeJkMK2MrtusZ24LhiyRQrST51TUouCvhLGUnw5GceyPqYbWkTe44hmFdB9Q2FPKHshgLCyzNYV4hbwoOXmL3Kvm8y%2BNdX%2FdG9kn5gyMUvfjfUg0n4Qtaxy7zVJmcD91TAIv0k6Os%2Fa%2BcaHI7CiGM3G%2F8UD5EWg%2BABQyXxPF8ZUS67TlzFDyM%2BHcB8JJaTtzc0U4wulA%2FgzgCCQAWcN%2BWxIointhBqQG4tnZYLLXLfu5PLotg1CdgLFAy%2BP3FzreY2HjwrahZ8mTa16xiVuKY3r6Oi1dSIe017WMI%2FLzMgGOqUBrcDQ3SLATzWRmlbkop1llrjtyZXC141QkY%2BjZ7%2B9DL%2BNfcq68yAvCZmoxwz5ooNdn5Hr%2F8bY%2Bql4Oc9JZqQ0jbs4DHVMvuvGjMY9Jvzv3kwFSkEmk2BZWUM2Q485x8s33pf6oX3g1UpSizUhUB4YZNvihC%2FriP7aXqMNxfKy3tZ161Xrc1v6SDup4nA9BiaZzuHwvV2lgjEeAj1nOHF7DLrMswYq&X-Amz-Signature=b84e12a29f3351bf8602e0fbf66ada44d72ae6086d9b53bf25b1223cbf58f0b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ANFTX52%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T123148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIExmNapP82xp7Rm3osjVXv%2FtaeJecNeM3NvL%2Bt%2ByZoCyAiEA8gNBgyLCrWgzKF7cWaX70msmjjXzuESxc3twJOII5kEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDKFNkTkFtFnW635dmSrcAwaX36PY1IjnhC2JrB46j7DdafOsIehM4NAT2zrGEVRijdHwayYxUPMM0pGsEtiaQDmvPmObH28qbzuE9luWNrTQ7FcMASFx%2F4nS4c4K2eECAXOdbL%2FzMFQ3Q6wlXUelhyp4vu%2FxZCqVwVht4v%2Bv2BHPl%2Bhnpx1V44JabRZjKzd8iP9IXqiLZSxy1EhMVtVf9GvGracPKT9bMf7ylsTJNcWoO6UoxzDkNg2T9xxxCD%2BsdMjPnHPVeZVAEkhBcmvVJkLcOEWzSJx2NZH8ZeJ7uPLuBCiwd5p%2BnvK0MIiQHpWHmRVNTDzbCt0%2FTOOFentyDJpmKAO8jK4331jbvo0BGz9wXPeJkMK2MrtusZ24LhiyRQrST51TUouCvhLGUnw5GceyPqYbWkTe44hmFdB9Q2FPKHshgLCyzNYV4hbwoOXmL3Kvm8y%2BNdX%2FdG9kn5gyMUvfjfUg0n4Qtaxy7zVJmcD91TAIv0k6Os%2Fa%2BcaHI7CiGM3G%2F8UD5EWg%2BABQyXxPF8ZUS67TlzFDyM%2BHcB8JJaTtzc0U4wulA%2FgzgCCQAWcN%2BWxIointhBqQG4tnZYLLXLfu5PLotg1CdgLFAy%2BP3FzreY2HjwrahZ8mTa16xiVuKY3r6Oi1dSIe017WMI%2FLzMgGOqUBrcDQ3SLATzWRmlbkop1llrjtyZXC141QkY%2BjZ7%2B9DL%2BNfcq68yAvCZmoxwz5ooNdn5Hr%2F8bY%2Bql4Oc9JZqQ0jbs4DHVMvuvGjMY9Jvzv3kwFSkEmk2BZWUM2Q485x8s33pf6oX3g1UpSizUhUB4YZNvihC%2FriP7aXqMNxfKy3tZ161Xrc1v6SDup4nA9BiaZzuHwvV2lgjEeAj1nOHF7DLrMswYq&X-Amz-Signature=0e51a9c6256b459a322149124a6de8f266ea89fddf9f432a75e51fb3fc6fdb2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







