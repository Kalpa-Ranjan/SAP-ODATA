



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q22MUR7P%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T061132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChb7RzcHR9sqRRa5%2By1Xad1vpTRZ5RUL3%2B4L7A5YfOrQIgcd6jGFQnIxTWCZS%2FaUNj9tlxvtJshDMgi4OR3XjSZmkqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO2aMzrpIw9gLFfDsyrcAznLC1B5FyPilHdyJcaxHvgc93zvm0TA5SN%2Blwl9NopcaTpUqmTZ216IlghGfPt93kGcUUkukw%2Ff3VWFd5oycZrzsYr5FMdzcNOVvGXFf%2B2p0Kox6dG9o3gGX9GjfZ%2F1C32wssmEsyEI5KM6ob%2BPnY88Tt7vGTYd7FkKSU89mAgeDSDx8sW2F%2BVLEJIetT0MjCry4eJ3oF2VGk3hFObYYiaIQAdqDaeAu85TrNFy07306aha4d7oJBvdeTRhYZlYd5eFYmW9Rh19aO5zdJ0vVWlLoIUpn9XwYeK6xJ1GJqztZOrol53xMPO%2Fc8rK0bmrZOKSE6sLJ1BzPb5VcdS%2FnOmrZhuKJk14US1xkpQH3hmuwq2LQFu9MG%2B8vgqX60sUfooR2dbj0HmAG7mJcJsR%2BGeuqB0qyQItCQgcFHkJKp2rHHeLocpy3KHSs7G533k%2FyC2%2BVXStlF9zoJCuaIn2p3kExCdIbZhv5xGDnOabxFUUFxkFww%2FZjNCMwzhLv4d1Rp4sjoD44iqOmpwCGvYtd1IWFvWnL%2F9q56QjUXXuOaBIR5QjlUXpPq5vsMgFrRta8n6O0SUlgJtyXi3ZSKjQXeZMWnKlvm6PUyNRDH5vCWlQ%2BCx8swPue9ci%2B8DQMLGxk9UGOqUBtZwRMk6SY86l26k%2FP5IUcAX8%2BTcZYSJh5fZAwRMWQMCLqSqcfdIC5KtNsTjSuctGs%2F23sbxGuCr7QzY%2B4qYpBLeqJCJ2Dey%2FZw3yvyzP1rmWdOJEAb%2FBBuMYx2wwu0Ro2MtCO%2B5Ju6v56jYp%2FUxq8c81XcvtBAQvBc6PXr10G0pKJwZi5bwXFojjgfskhrHbdyd%2FW6%2BB5Y9F68NI%2FNEY%2FFOZONXj&X-Amz-Signature=002bbff74a048bfa226adf26f311082726dd4ac1982de0e10a7f883f65ae09c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q22MUR7P%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T061132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChb7RzcHR9sqRRa5%2By1Xad1vpTRZ5RUL3%2B4L7A5YfOrQIgcd6jGFQnIxTWCZS%2FaUNj9tlxvtJshDMgi4OR3XjSZmkqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO2aMzrpIw9gLFfDsyrcAznLC1B5FyPilHdyJcaxHvgc93zvm0TA5SN%2Blwl9NopcaTpUqmTZ216IlghGfPt93kGcUUkukw%2Ff3VWFd5oycZrzsYr5FMdzcNOVvGXFf%2B2p0Kox6dG9o3gGX9GjfZ%2F1C32wssmEsyEI5KM6ob%2BPnY88Tt7vGTYd7FkKSU89mAgeDSDx8sW2F%2BVLEJIetT0MjCry4eJ3oF2VGk3hFObYYiaIQAdqDaeAu85TrNFy07306aha4d7oJBvdeTRhYZlYd5eFYmW9Rh19aO5zdJ0vVWlLoIUpn9XwYeK6xJ1GJqztZOrol53xMPO%2Fc8rK0bmrZOKSE6sLJ1BzPb5VcdS%2FnOmrZhuKJk14US1xkpQH3hmuwq2LQFu9MG%2B8vgqX60sUfooR2dbj0HmAG7mJcJsR%2BGeuqB0qyQItCQgcFHkJKp2rHHeLocpy3KHSs7G533k%2FyC2%2BVXStlF9zoJCuaIn2p3kExCdIbZhv5xGDnOabxFUUFxkFww%2FZjNCMwzhLv4d1Rp4sjoD44iqOmpwCGvYtd1IWFvWnL%2F9q56QjUXXuOaBIR5QjlUXpPq5vsMgFrRta8n6O0SUlgJtyXi3ZSKjQXeZMWnKlvm6PUyNRDH5vCWlQ%2BCx8swPue9ci%2B8DQMLGxk9UGOqUBtZwRMk6SY86l26k%2FP5IUcAX8%2BTcZYSJh5fZAwRMWQMCLqSqcfdIC5KtNsTjSuctGs%2F23sbxGuCr7QzY%2B4qYpBLeqJCJ2Dey%2FZw3yvyzP1rmWdOJEAb%2FBBuMYx2wwu0Ro2MtCO%2B5Ju6v56jYp%2FUxq8c81XcvtBAQvBc6PXr10G0pKJwZi5bwXFojjgfskhrHbdyd%2FW6%2BB5Y9F68NI%2FNEY%2FFOZONXj&X-Amz-Signature=589539cc98bfe9a6c72caf335570060c69043c24cbb7effd1ca74078a64059cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







