



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673O3REYL%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T062455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9L9ivpIhNG3YUZ1fTtW8HZBIYVHf7PoOu74FnOO0V%2FwIgSv13MGM%2Fu1yRVdmnHscivu71pbwznEUzyL8%2FEVxM1%2Bwq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDI61MFsOQrj1syYJWCrcAws214x6aeFVsfXzhtPYLdh0p8o49q0ikCWpq4PkvoPqcWlLv21gtTA2pJk8dJWdm6L8AKES%2FsUAMZ0NEdhuimmT1KL8QkCQH%2BxCLX2MvFj3J07HSQebrXEc1J5ES%2FTC4us%2FU%2F6uWEdLK3c%2BwmWsDhlkIhLieJxwHQ9ygkeF2wKozUnKBocO8XRM%2BTnScCcUDtfj6%2BF%2FxcPJMji34qtVELhbTSSqCG%2BP36eOACW%2BYK4BP%2BkxmtBLT1PHUX%2FGJaiowwIkROFUEKoqpPDafF6BXtb8g6SZPnR6YDWcHh%2FMwiVIoyRPe%2FSIaiEWIxY01ImbY%2BNPHLCPQ5WKh4wMEbu0I%2Bk5VnCYNNtpm0GF53SkJfZSOOhpyzeaSw%2BgthxqmiG1AHCMCAhM3%2BSDsFNxAcXeYj06kTd20IvGUqoCt8vtFGc4oLLWRDpBPON7KDUVuQywT4KZ5r3z3nastf4qXkTzysb7yA7AenWMJHkfpeym6UN4omVTmU9UxxCxrZSToVlay29V6w%2FZAtuQFHbmbICQtM7T%2BzTpaBeqxhEjp0XMm%2BMpAfr975Aqf9NMUVfDs7IjiQ%2B1TnXLivGeKiC5KgOTyyykhKcuq60XNKR4quqTG1TG9D6WjtLkwINnq6QwMP3Yj8kGOqUBNGYXWztGHDMD576nQ6q%2FIGNYLscLNaj94FRWcVoUaS%2FKpQOPa%2Fw8S08qRJXHSLRwVf6Z59VHq6ZDTRUsYnN0OHwY1ENzxVloLOO84ZdKXQ7GVavydTvcVuclrChj%2B7b2piuqcdvGYh%2FuojO4qbkD9UMH60iy7r7yMvkU6fvYMdLHVy%2BACRSc1PKzw99XtB1dc%2FqMmfzWdbhOzTOP%2BU9kDtep4dgQ&X-Amz-Signature=613fd972230ae9f1ad55af9f68845890c8daca2fb3df18b76e2825d1ed06a56f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673O3REYL%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T062456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9L9ivpIhNG3YUZ1fTtW8HZBIYVHf7PoOu74FnOO0V%2FwIgSv13MGM%2Fu1yRVdmnHscivu71pbwznEUzyL8%2FEVxM1%2Bwq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDI61MFsOQrj1syYJWCrcAws214x6aeFVsfXzhtPYLdh0p8o49q0ikCWpq4PkvoPqcWlLv21gtTA2pJk8dJWdm6L8AKES%2FsUAMZ0NEdhuimmT1KL8QkCQH%2BxCLX2MvFj3J07HSQebrXEc1J5ES%2FTC4us%2FU%2F6uWEdLK3c%2BwmWsDhlkIhLieJxwHQ9ygkeF2wKozUnKBocO8XRM%2BTnScCcUDtfj6%2BF%2FxcPJMji34qtVELhbTSSqCG%2BP36eOACW%2BYK4BP%2BkxmtBLT1PHUX%2FGJaiowwIkROFUEKoqpPDafF6BXtb8g6SZPnR6YDWcHh%2FMwiVIoyRPe%2FSIaiEWIxY01ImbY%2BNPHLCPQ5WKh4wMEbu0I%2Bk5VnCYNNtpm0GF53SkJfZSOOhpyzeaSw%2BgthxqmiG1AHCMCAhM3%2BSDsFNxAcXeYj06kTd20IvGUqoCt8vtFGc4oLLWRDpBPON7KDUVuQywT4KZ5r3z3nastf4qXkTzysb7yA7AenWMJHkfpeym6UN4omVTmU9UxxCxrZSToVlay29V6w%2FZAtuQFHbmbICQtM7T%2BzTpaBeqxhEjp0XMm%2BMpAfr975Aqf9NMUVfDs7IjiQ%2B1TnXLivGeKiC5KgOTyyykhKcuq60XNKR4quqTG1TG9D6WjtLkwINnq6QwMP3Yj8kGOqUBNGYXWztGHDMD576nQ6q%2FIGNYLscLNaj94FRWcVoUaS%2FKpQOPa%2Fw8S08qRJXHSLRwVf6Z59VHq6ZDTRUsYnN0OHwY1ENzxVloLOO84ZdKXQ7GVavydTvcVuclrChj%2B7b2piuqcdvGYh%2FuojO4qbkD9UMH60iy7r7yMvkU6fvYMdLHVy%2BACRSc1PKzw99XtB1dc%2FqMmfzWdbhOzTOP%2BU9kDtep4dgQ&X-Amz-Signature=4b91666adbaf3cff8e3a62022b01de3c975aaf34d775d8c43032daa14090aa17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







