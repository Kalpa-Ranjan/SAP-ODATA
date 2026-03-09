



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE3HKNQA%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T065541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIQDd3U5U5oeipWsGqOpsTGcLYfIvV7H8wAovec3ni9YsHwIgdMRY5oJiUOuGsKLQ1K16GSOnCk8RMCfsfoQT9IkXaLMq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMYCMRnMB%2BH8rXCfkyrcAx5%2Fz9ZpNxHoJ2TDILW0jksf4Cm1NOwyn9mX6jggKBseoPi%2FSUJC0RUA5ZuSJvR2jcaSQe2bG1bjMj%2FB1YhEAv9xIcjmJylqa7fxdSxtSBHvpODCqxlemeUwH8I5Jb2BMIZvAccQsME55byJ7R4oHAKVadFdlBlWJj%2BWHIMpC%2BYDVsATeNMAsd1AAY8JRqgFkrfZOfqW7yvaZRnPn%2FK6j1VSqr4hXfkAhomrx4XY816aCGHX%2Faoz5rTLZj%2BXCkK8WLgafRjdvIRQSYChZdcKwxkG6IF0Fzhkh8IrQxxYh8201lKMfaOVky1SGXm0fHneNqLpR2hhO3XIpMZv2EtHoMbr%2FGoFnSRjZYUI%2FzgERvUgUI0x57f%2FPw%2FZgVAOKy%2BQX%2FyZj8kjqyEu9TTAbB9aZ9Y4TGS8UYR%2BObYPus5KqJZHN3PhIkN%2FxtNIbaBsS2QqK80PbqHHc5tC7GpQ3WWjprfwXGMDOJcO9mWf5X0vathjEBdQWMvbfb9eRPXgVY%2BTzmk3tSPBw7gGMiK7SM4rLHBKrDLYoecstc5mx%2BHjeawnNpwMs3EbfksP9i1ETDd4y6RMmaHYrlcTCyM0QVwmOsTTlJBQBtqs11maaKARnaoet4Kest3lLb1BALijMI%2FHuc0GOqUBaaTj8Y88pRMZgfvxy2j5z0%2FfD5NlU%2FCHxRdmgvrzNuyQquvX55FWBjv3KLKs6TX7u%2BE2%2BlQDsf5IJKxDOU4gMJzNw8V%2B3B880Ejdj36kTm8y2S2S25Ose9LIT44CL8JaTToZoV1SaGcWCCTxwgiTeti5EBmruL6VbZ2WAam7QxWVqrcw4%2BWKrKG8mdKmicO5w8zoNHyCQ92jUkDLkPGOYzhBcV9N&X-Amz-Signature=feac376ce4d8cd62b11b7b0be39f9f6e9f318964a7a409169a2ee9d71654b684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE3HKNQA%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T065542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIQDd3U5U5oeipWsGqOpsTGcLYfIvV7H8wAovec3ni9YsHwIgdMRY5oJiUOuGsKLQ1K16GSOnCk8RMCfsfoQT9IkXaLMq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMYCMRnMB%2BH8rXCfkyrcAx5%2Fz9ZpNxHoJ2TDILW0jksf4Cm1NOwyn9mX6jggKBseoPi%2FSUJC0RUA5ZuSJvR2jcaSQe2bG1bjMj%2FB1YhEAv9xIcjmJylqa7fxdSxtSBHvpODCqxlemeUwH8I5Jb2BMIZvAccQsME55byJ7R4oHAKVadFdlBlWJj%2BWHIMpC%2BYDVsATeNMAsd1AAY8JRqgFkrfZOfqW7yvaZRnPn%2FK6j1VSqr4hXfkAhomrx4XY816aCGHX%2Faoz5rTLZj%2BXCkK8WLgafRjdvIRQSYChZdcKwxkG6IF0Fzhkh8IrQxxYh8201lKMfaOVky1SGXm0fHneNqLpR2hhO3XIpMZv2EtHoMbr%2FGoFnSRjZYUI%2FzgERvUgUI0x57f%2FPw%2FZgVAOKy%2BQX%2FyZj8kjqyEu9TTAbB9aZ9Y4TGS8UYR%2BObYPus5KqJZHN3PhIkN%2FxtNIbaBsS2QqK80PbqHHc5tC7GpQ3WWjprfwXGMDOJcO9mWf5X0vathjEBdQWMvbfb9eRPXgVY%2BTzmk3tSPBw7gGMiK7SM4rLHBKrDLYoecstc5mx%2BHjeawnNpwMs3EbfksP9i1ETDd4y6RMmaHYrlcTCyM0QVwmOsTTlJBQBtqs11maaKARnaoet4Kest3lLb1BALijMI%2FHuc0GOqUBaaTj8Y88pRMZgfvxy2j5z0%2FfD5NlU%2FCHxRdmgvrzNuyQquvX55FWBjv3KLKs6TX7u%2BE2%2BlQDsf5IJKxDOU4gMJzNw8V%2B3B880Ejdj36kTm8y2S2S25Ose9LIT44CL8JaTToZoV1SaGcWCCTxwgiTeti5EBmruL6VbZ2WAam7QxWVqrcw4%2BWKrKG8mdKmicO5w8zoNHyCQ92jUkDLkPGOYzhBcV9N&X-Amz-Signature=6c4676a59e84f1bc99992b4acce775c59e36ea1d3001d6c6fd611bb4da671103&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







