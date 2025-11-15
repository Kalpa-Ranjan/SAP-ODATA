



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEFIBX7%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T122800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJJB9v8FxnVUXFttvhQ5uFVm5hoLhGJQajv0YZf8rlWQIgWL7sjE9nF1inSsEHrRJ0C4AbYhfHRS2EgeZyvKFESckq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDOAAwFh3tjtRXqLQ4ircA6usw8m2MU%2BrlQxL3SL1%2Frr9luqKXPZ7rAMnaozchVcwsERegNaZx6XV%2BsMz5tAUiJMnfc93mBIxeRcbvFLKPy26EG%2Fjo0mf3H4VAiyUZkDLNSX9%2BrovETl9nlL5WVGDCRBFwxFMy%2FpBSQuQMPNOT%2B0fC5hsLhicAs5kYmAn%2FHsW19Vi224tcfrAvkCYCalFQz5FnY5XZ9wbQnrU6ny6%2B%2Fr2E9UgrLrhvhlPf%2FWoJpPah%2FjlSkm5U8MZ688q9jDRZziDEJQ6Ei16Awjv7jYRs%2BuUmboasNh8t8yhoq4RRBsLK9o%2BV88tm73CpFEs1MogGtEkvQQi1I9a0ADKRyDg5zTyDXR6hFiAkeTCrxPQy3L5oHtQZUMH2CBI3naJulefHRTi2cK1Z9KbFc%2Bq4OFiP%2BTnkSLXIt2ys1PfrzRMwKVT77e9dGk1GhYzR7zPDMi%2B0RYYOZDbKzOQZGG83HC%2FbMICqx%2BJbVOLTqa8DPe1urdxyJXgUcaAja7j784NlSKUhzGp3e4d9I6acTklVKGHJImQIaYt9BuXXPCch33dBR9dOdN15Rs3RUzkFuUbg2eK0tX1uNm4WT3Ark6wYrPvayTnOLE%2BLRRT9JZJlpXVQLFulfCvsT62a3Qki%2BNoMPSV4cgGOqUBqfvny4RdxIBwdTqqIrdb%2FE3J2gG1qjLkLt0epJGKedcZiagxQb056O3mUGM3a5Xo6VYKP48Lk%2F%2FSROHH43b%2B5%2BZZEfr%2F90vE92XJZgCDywr%2B1aLfvybnR3c1Qc6A%2BtZ98Es9RSPuWq%2FrYWa2OCrb9MLbyp4N1s9WWwoBadZ%2BuzWc7bTyhosyMH975gNjXMyS%2BXtNH58JgDHH62VRX8CAdWzbq1lH&X-Amz-Signature=6dd3a023b525668b8f62764655b0859de4e8f6b3c7b4514776a9829594aaba0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEFIBX7%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T122800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJJB9v8FxnVUXFttvhQ5uFVm5hoLhGJQajv0YZf8rlWQIgWL7sjE9nF1inSsEHrRJ0C4AbYhfHRS2EgeZyvKFESckq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDOAAwFh3tjtRXqLQ4ircA6usw8m2MU%2BrlQxL3SL1%2Frr9luqKXPZ7rAMnaozchVcwsERegNaZx6XV%2BsMz5tAUiJMnfc93mBIxeRcbvFLKPy26EG%2Fjo0mf3H4VAiyUZkDLNSX9%2BrovETl9nlL5WVGDCRBFwxFMy%2FpBSQuQMPNOT%2B0fC5hsLhicAs5kYmAn%2FHsW19Vi224tcfrAvkCYCalFQz5FnY5XZ9wbQnrU6ny6%2B%2Fr2E9UgrLrhvhlPf%2FWoJpPah%2FjlSkm5U8MZ688q9jDRZziDEJQ6Ei16Awjv7jYRs%2BuUmboasNh8t8yhoq4RRBsLK9o%2BV88tm73CpFEs1MogGtEkvQQi1I9a0ADKRyDg5zTyDXR6hFiAkeTCrxPQy3L5oHtQZUMH2CBI3naJulefHRTi2cK1Z9KbFc%2Bq4OFiP%2BTnkSLXIt2ys1PfrzRMwKVT77e9dGk1GhYzR7zPDMi%2B0RYYOZDbKzOQZGG83HC%2FbMICqx%2BJbVOLTqa8DPe1urdxyJXgUcaAja7j784NlSKUhzGp3e4d9I6acTklVKGHJImQIaYt9BuXXPCch33dBR9dOdN15Rs3RUzkFuUbg2eK0tX1uNm4WT3Ark6wYrPvayTnOLE%2BLRRT9JZJlpXVQLFulfCvsT62a3Qki%2BNoMPSV4cgGOqUBqfvny4RdxIBwdTqqIrdb%2FE3J2gG1qjLkLt0epJGKedcZiagxQb056O3mUGM3a5Xo6VYKP48Lk%2F%2FSROHH43b%2B5%2BZZEfr%2F90vE92XJZgCDywr%2B1aLfvybnR3c1Qc6A%2BtZ98Es9RSPuWq%2FrYWa2OCrb9MLbyp4N1s9WWwoBadZ%2BuzWc7bTyhosyMH975gNjXMyS%2BXtNH58JgDHH62VRX8CAdWzbq1lH&X-Amz-Signature=22bc9226a15332c5a31a2d2b0114988a4c5714418ce37d1939890503a1467c98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







