



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5R6TZ62%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T182603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIGIFLhhvhNQ4a0AwYjZwE7QL1qqRG39JgtssYCE3lEOAAiAArQsywJlO7whFMGOJvDUgIj1xR377r13SSE7pDN6jnCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMZ2S7byvYTytyRvfQKtwDysB1KdCK5d9SKcTy19YgvsnYNdpF0aWe%2Fs8Y9b0Tddanh%2BqYG%2FBXq1hOQOLr9C3J7pI9pRlB%2BpARZdCd%2FZTv9ptdcgKp0JFR5SIGqKYOaEKcuZMgWeUozVqvl3fgJjNIlrs4b1iDfhTHGGRA6BENX5pcoCp%2FrMdODfbHOctuSUAK71BX3xuNrhX8Gy8EKQhxHUDC%2BZ6wpdMSVh8orsD76z9SBFbvFM4V6WM1tCcBNaZQe4iZzlOdc%2BxO%2Bqap5ey50A26ztgFC2q2elsAcMsKfNgtmhZOp2e8ApLyRYeNt4nny0LyEOB3NYD3NwDYaGCyKyV61CYoXwizLJnIR3z6a5HePCzEXlmn%2BupcUDWyHPCKsCJT9jQy3Ki5vxb4emkl6l1aTwV%2F7s0vtzPIdewXUAiYpPjI1dA5RuRAFNF1ba8Md7yi1KSdD51o8tTP%2BiQJ%2B%2B5x17plr1it3D1eSZvPr%2Fzlim5Lv5H7l9E2eWUIHevH81kClNKZiYCJqsiip%2FGRyBYYtPqp82ax9BC8HSryhGf%2F2c%2Bd8rxMmOlGhEQGUGbp%2BzL7QPwKYWblWMImgHqphWwFkWA42qf2UnulcLeq0X5zx7zp1Wu5PxmmGOo2C1tFs%2Feaj8GimFEBOs8wp4vvygY6pgEWSp86qaOfc%2F7BecW1BXwNBBgjw8ptjNlgP2R4stF6jhScZjHHAiOgxOXb%2Fx9mFbTMng3vUJj%2B%2BZPNu4z3SRzrT%2F9g72sybJUqvqGe2qb1g%2BRrIxH%2FkDPtwNB0SHrDlqcDC4vhTkLf1g0CcuIs5n7A%2Bh7DzHn%2BsRSNVi7KPqE4E4%2FQGLIh%2Bk1olMMeIMxF%2Bbfl1gFJ25NqAmsclUHw3U46DTdiavRX&X-Amz-Signature=8602ee4c58d9630d02b1bbc4a2d46ce1c27dc7247de9e38dbfbfb02c77044e7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5R6TZ62%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T182604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIGIFLhhvhNQ4a0AwYjZwE7QL1qqRG39JgtssYCE3lEOAAiAArQsywJlO7whFMGOJvDUgIj1xR377r13SSE7pDN6jnCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMZ2S7byvYTytyRvfQKtwDysB1KdCK5d9SKcTy19YgvsnYNdpF0aWe%2Fs8Y9b0Tddanh%2BqYG%2FBXq1hOQOLr9C3J7pI9pRlB%2BpARZdCd%2FZTv9ptdcgKp0JFR5SIGqKYOaEKcuZMgWeUozVqvl3fgJjNIlrs4b1iDfhTHGGRA6BENX5pcoCp%2FrMdODfbHOctuSUAK71BX3xuNrhX8Gy8EKQhxHUDC%2BZ6wpdMSVh8orsD76z9SBFbvFM4V6WM1tCcBNaZQe4iZzlOdc%2BxO%2Bqap5ey50A26ztgFC2q2elsAcMsKfNgtmhZOp2e8ApLyRYeNt4nny0LyEOB3NYD3NwDYaGCyKyV61CYoXwizLJnIR3z6a5HePCzEXlmn%2BupcUDWyHPCKsCJT9jQy3Ki5vxb4emkl6l1aTwV%2F7s0vtzPIdewXUAiYpPjI1dA5RuRAFNF1ba8Md7yi1KSdD51o8tTP%2BiQJ%2B%2B5x17plr1it3D1eSZvPr%2Fzlim5Lv5H7l9E2eWUIHevH81kClNKZiYCJqsiip%2FGRyBYYtPqp82ax9BC8HSryhGf%2F2c%2Bd8rxMmOlGhEQGUGbp%2BzL7QPwKYWblWMImgHqphWwFkWA42qf2UnulcLeq0X5zx7zp1Wu5PxmmGOo2C1tFs%2Feaj8GimFEBOs8wp4vvygY6pgEWSp86qaOfc%2F7BecW1BXwNBBgjw8ptjNlgP2R4stF6jhScZjHHAiOgxOXb%2Fx9mFbTMng3vUJj%2B%2BZPNu4z3SRzrT%2F9g72sybJUqvqGe2qb1g%2BRrIxH%2FkDPtwNB0SHrDlqcDC4vhTkLf1g0CcuIs5n7A%2Bh7DzHn%2BsRSNVi7KPqE4E4%2FQGLIh%2Bk1olMMeIMxF%2Bbfl1gFJ25NqAmsclUHw3U46DTdiavRX&X-Amz-Signature=b14531f8ddbe1b2f48e7e9056b98b3c65225f8c62a6346ec87c24ad9fb602ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







