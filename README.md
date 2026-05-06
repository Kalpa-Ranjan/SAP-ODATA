



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJP635RJ%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T081741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoRSDgNvmDDoDEIvGNoVfFGcbMGCAr7mrymFlt1hgITAiEAuiVnGTkhxSzOhE4opm2VJFNwB91k9Ahi1HZWnFJLRjYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaLdp1AtfltNhHrkircA%2Bk4kafDe%2F7Qbxsx5OKeZdNFqmFh8mkr98JLEy6fxvi%2FCjQePy4A950gsFIPt1MM8Ico24eKW%2FoGN%2Fwscz3g0H8BrpSkMqVD%2BEpuJ%2FpjgMGo9G3rkntf7EsBDvWk7ecpGwMeMnXci7wF25ChpY0n3zAB%2B9TBGqjiMq1iPojuBY7WnEslN%2FqTGE9hwRFpO%2FxmVolFEXB1RjYA7T7VXS2U1ioSZzwE6odUP0kMrm3YOFzC8H4FOV476YoaOYyJcxt4juxBDbZhPFYnjU%2BXOMT4E03PzGQt%2Fsz9mFoP02diL4WnSlBG%2F1qQCxaYSIxxBruKZiCK6s%2BIOQ%2FTe2863iQCvyLv7DqZBiJ%2FVjtaR9zb03Y596sN2QN2x4DUw29vyZbYit%2FTI91QnaZg4ba%2FGQ5WSO0vOaHdk5RSNwS2OIpK1ycpvwmdBGharAJOb1GnqXisGFRU5Hdh5bYfjsFycDi11CsGxjPg7Nm4HFCScyxBwW6CXEuj%2FDKk7tC4jhPMuIA6AxWHDEHpUBVHKaMlLoxUBG21jmjx5iPaxX%2FOKNObU58fsIKZ6FLWqYWz75PQ8zdJyyfSpbp9AEHvX8cpxLCb38XNb9NnFdetjUyo1sFzParAeEx8KrcboiF%2FAq2gMJbg688GOqUBT%2BBlUr1Iav3KdJPb9dGIBiCmuvZWzj6ivDNSmiDPQ3Fhx6%2Fw017OUvcGGOU89Ly6E2NTIB%2BTnU4XoggWMNtPKnEiu0VfgcIdNVOXLvzhpAt32xQFfsp%2BHkMhUj63w5GyoFbv7us%2BeICynm4V3gf%2F%2FjLNaOL%2BF%2FqFmSvVTeYjanUkcyvWSKRaJYYX3ou57nlTRVAKZJRtRGs6X1aEEw%2BsUClTU6R2&X-Amz-Signature=fa05cdbb9fe84a769672cdf2f9cb2f20b46726c03050667e162644de644dc126&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJP635RJ%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T081741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoRSDgNvmDDoDEIvGNoVfFGcbMGCAr7mrymFlt1hgITAiEAuiVnGTkhxSzOhE4opm2VJFNwB91k9Ahi1HZWnFJLRjYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaLdp1AtfltNhHrkircA%2Bk4kafDe%2F7Qbxsx5OKeZdNFqmFh8mkr98JLEy6fxvi%2FCjQePy4A950gsFIPt1MM8Ico24eKW%2FoGN%2Fwscz3g0H8BrpSkMqVD%2BEpuJ%2FpjgMGo9G3rkntf7EsBDvWk7ecpGwMeMnXci7wF25ChpY0n3zAB%2B9TBGqjiMq1iPojuBY7WnEslN%2FqTGE9hwRFpO%2FxmVolFEXB1RjYA7T7VXS2U1ioSZzwE6odUP0kMrm3YOFzC8H4FOV476YoaOYyJcxt4juxBDbZhPFYnjU%2BXOMT4E03PzGQt%2Fsz9mFoP02diL4WnSlBG%2F1qQCxaYSIxxBruKZiCK6s%2BIOQ%2FTe2863iQCvyLv7DqZBiJ%2FVjtaR9zb03Y596sN2QN2x4DUw29vyZbYit%2FTI91QnaZg4ba%2FGQ5WSO0vOaHdk5RSNwS2OIpK1ycpvwmdBGharAJOb1GnqXisGFRU5Hdh5bYfjsFycDi11CsGxjPg7Nm4HFCScyxBwW6CXEuj%2FDKk7tC4jhPMuIA6AxWHDEHpUBVHKaMlLoxUBG21jmjx5iPaxX%2FOKNObU58fsIKZ6FLWqYWz75PQ8zdJyyfSpbp9AEHvX8cpxLCb38XNb9NnFdetjUyo1sFzParAeEx8KrcboiF%2FAq2gMJbg688GOqUBT%2BBlUr1Iav3KdJPb9dGIBiCmuvZWzj6ivDNSmiDPQ3Fhx6%2Fw017OUvcGGOU89Ly6E2NTIB%2BTnU4XoggWMNtPKnEiu0VfgcIdNVOXLvzhpAt32xQFfsp%2BHkMhUj63w5GyoFbv7us%2BeICynm4V3gf%2F%2FjLNaOL%2BF%2FqFmSvVTeYjanUkcyvWSKRaJYYX3ou57nlTRVAKZJRtRGs6X1aEEw%2BsUClTU6R2&X-Amz-Signature=896fb2a48382850b009a42f2181bb60971825e96751c340fe0d30149e2ea2f05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







