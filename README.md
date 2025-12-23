



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AD6Q755%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T062649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQC%2FvuqOq2OS5nbt4rmOVBVYlApseVbR2BAKDLx9nu8n3wIgTL7bZmnI8dB9Da2aIBVvIeCzNMWEbKqR3iPf8uPCWRwq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDIuqROKF%2FoPnczjKHircA3Bh4xPnTdJwEoppnarDRBVMkvAtBHRI0K30z%2FqVCezJXjEDOc67cd0XXF8STitoM68MkLectB67FDXaXrvRBaEe9VZaLeS7FDSgF6LJUN9IpDnge%2BE4JPUmGydem7frirhf3FDYHDQ1Cn7UoY17sjg%2BwDgJXFs34O3BnC9XFYztsmkVzItg1HP74%2BZ7LkTN2ISdpkKFdghUMjwXrqZi5EbqGJuYJjjLKWHpTf2%2FFMP1g6yPjQN%2FuHfsT4tgEolwGESUczZy%2FRgk0Msi%2FfdZKxKzPFR2UYD4zrDJQOjLpKFUaXmTzbjGorYJ0g5lNFsn0f1VPCsbEOrvv444FTj2YEcAIT8iMr8vhYSdxwqVJAhnXLTjUILIc%2F0QjmScqJFVE48m7e7o%2FyRbdSLMZ5Z0h1yh6GMB5OGD1C4RRlgrrJ07f8OR5UYlz8xm55a5olTDYi8aij3AW%2BueEdHHpWPzZkiexXTPwGC61c%2BEyMIOi1uY4Xd1ZusVfYSglk292asveqe%2BSOHYHEqMyHunAJdNBDaiHfzBMd%2FjVcSs72nmLwdcUUpzo9y9fpCxk5p26iZlxGgOkWKG3Xk2pbfDsyh0PXr4M9cRLmasFkg6yTIEmLqH7NYut7KhLLBJCilhMPHjqMoGOqUBBO0qRB6hU8JA1E%2Bbu69iTebMhyqthht9LC61K1b68MoTe0GiYLidU5m%2Ff0heOcp3SP7K2OH5i1MizaMSR38wBiVYDJTCXcTUnQxvB%2FAKPrACzpes%2FZ%2F7PF4migDAKbzgoeeKMmMN%2BPqgLqXxAuVkGHcQ1sayUKYUyAdKNrUU0vObD4Etnqq%2BL8HxGT7SYPw%2FpkUzZiAGaKPiLwfGymE2Ui5W%2BQpv&X-Amz-Signature=b243bb645f7d671cf12b90ac1c760119f32ca86c652aa12bdea7fb4da44b5b8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AD6Q755%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T062649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQC%2FvuqOq2OS5nbt4rmOVBVYlApseVbR2BAKDLx9nu8n3wIgTL7bZmnI8dB9Da2aIBVvIeCzNMWEbKqR3iPf8uPCWRwq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDIuqROKF%2FoPnczjKHircA3Bh4xPnTdJwEoppnarDRBVMkvAtBHRI0K30z%2FqVCezJXjEDOc67cd0XXF8STitoM68MkLectB67FDXaXrvRBaEe9VZaLeS7FDSgF6LJUN9IpDnge%2BE4JPUmGydem7frirhf3FDYHDQ1Cn7UoY17sjg%2BwDgJXFs34O3BnC9XFYztsmkVzItg1HP74%2BZ7LkTN2ISdpkKFdghUMjwXrqZi5EbqGJuYJjjLKWHpTf2%2FFMP1g6yPjQN%2FuHfsT4tgEolwGESUczZy%2FRgk0Msi%2FfdZKxKzPFR2UYD4zrDJQOjLpKFUaXmTzbjGorYJ0g5lNFsn0f1VPCsbEOrvv444FTj2YEcAIT8iMr8vhYSdxwqVJAhnXLTjUILIc%2F0QjmScqJFVE48m7e7o%2FyRbdSLMZ5Z0h1yh6GMB5OGD1C4RRlgrrJ07f8OR5UYlz8xm55a5olTDYi8aij3AW%2BueEdHHpWPzZkiexXTPwGC61c%2BEyMIOi1uY4Xd1ZusVfYSglk292asveqe%2BSOHYHEqMyHunAJdNBDaiHfzBMd%2FjVcSs72nmLwdcUUpzo9y9fpCxk5p26iZlxGgOkWKG3Xk2pbfDsyh0PXr4M9cRLmasFkg6yTIEmLqH7NYut7KhLLBJCilhMPHjqMoGOqUBBO0qRB6hU8JA1E%2Bbu69iTebMhyqthht9LC61K1b68MoTe0GiYLidU5m%2Ff0heOcp3SP7K2OH5i1MizaMSR38wBiVYDJTCXcTUnQxvB%2FAKPrACzpes%2FZ%2F7PF4migDAKbzgoeeKMmMN%2BPqgLqXxAuVkGHcQ1sayUKYUyAdKNrUU0vObD4Etnqq%2BL8HxGT7SYPw%2FpkUzZiAGaKPiLwfGymE2Ui5W%2BQpv&X-Amz-Signature=d2349d483e4b8eef39312ae22c1e279c3e29facac7b6cb649abf6b3f990cea50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







