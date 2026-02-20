



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOXPYDM6%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T014435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0eMWaSQ7ZxJiOWGRfGLkJfIEzvwLDkS16fvOQ%2FjYw6AiAzAO3niSLiSzLa3TCG%2BbxZPITgrYMcygVAG1s54jINECqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtRlddvF98l8%2BYKbnKtwD7013y8T5gQHZPAadg7BRCmv48TBKHlCO429I3EgD2gsPsgt%2F%2FSFBkwnV6C7W4XwMo41EMXd0ab20W07bP4UGmIzu%2FEhxMjvd7rVYFazwQzcIFL%2FvOr5Y8sSMB11F%2B9ggOWPAev7suvA2uorqMf%2Fkw%2BNXiJpyarQp8eK601uYQBEcO5Q5VQTDm0NRuuGsCYEVLZbpgE907sdXgGAi7XRpqDVRcf4Cow%2FDEenBz2Isrh179c4HbdDdUYrNYUPbAY7j4uu6WDXDLgg3dNB8mqQ6PV77eh%2FG6SwSSyVqqPusmY2kWNwkqLUgovOdyvV79xZWquzZeGQU7deUWbWVxFZ89GN8IqyH0BWaz5FShiWKbHC6JITyE6wjVtGxHmeN%2BZmo5NBTgt0kxZs2bQlk%2F5IbxIkEkBBSuucU86PX0oNvaBX3HYm1QnPO1xudoXhSUVB%2BhytfLCSaBWPMmIw%2FTrVo%2FtC3juMlldKtmWt5ntLB9oIV2yy1RnTXe3lFHYm3W30kIxzajwz4SN2MeTmXmdFfFz%2BFd1rOn4pRRsWyi2txPMZeDUANFY%2BALV876Oz22y1gXD36XoWdp5hg3JEKYFPEB5M6VQ8S4%2Fdu2vQOEZyfcpClNYNGUA3oA%2BN90rgw2%2BfezAY6pgGctGdkEpe%2Fw7WZUKyGnfNhWzyL2BVSgd8W%2BLXnl%2BZB00Up8aaSuABt0XKflCi2x62JIScE3jFMPj15Ec9Yj6tgX6YXgl77AFjGB3hjXv97nw4x%2FijMnGoS5xr%2BOIxe4yQBLZ%2FdObgmBFKhedzIm%2BqdX4K2Aa6KOwM0I56wrg0nvzNm%2BqVTalim1MXSNx9jyJkkNNASVZiLWvBM5yv0Z2pnusB5%2B2XJ&X-Amz-Signature=65df4ace627097dc56af87128a166d8da7ff4f0d83e7ab7601c6673ebceab0cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOXPYDM6%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T014436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0eMWaSQ7ZxJiOWGRfGLkJfIEzvwLDkS16fvOQ%2FjYw6AiAzAO3niSLiSzLa3TCG%2BbxZPITgrYMcygVAG1s54jINECqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtRlddvF98l8%2BYKbnKtwD7013y8T5gQHZPAadg7BRCmv48TBKHlCO429I3EgD2gsPsgt%2F%2FSFBkwnV6C7W4XwMo41EMXd0ab20W07bP4UGmIzu%2FEhxMjvd7rVYFazwQzcIFL%2FvOr5Y8sSMB11F%2B9ggOWPAev7suvA2uorqMf%2Fkw%2BNXiJpyarQp8eK601uYQBEcO5Q5VQTDm0NRuuGsCYEVLZbpgE907sdXgGAi7XRpqDVRcf4Cow%2FDEenBz2Isrh179c4HbdDdUYrNYUPbAY7j4uu6WDXDLgg3dNB8mqQ6PV77eh%2FG6SwSSyVqqPusmY2kWNwkqLUgovOdyvV79xZWquzZeGQU7deUWbWVxFZ89GN8IqyH0BWaz5FShiWKbHC6JITyE6wjVtGxHmeN%2BZmo5NBTgt0kxZs2bQlk%2F5IbxIkEkBBSuucU86PX0oNvaBX3HYm1QnPO1xudoXhSUVB%2BhytfLCSaBWPMmIw%2FTrVo%2FtC3juMlldKtmWt5ntLB9oIV2yy1RnTXe3lFHYm3W30kIxzajwz4SN2MeTmXmdFfFz%2BFd1rOn4pRRsWyi2txPMZeDUANFY%2BALV876Oz22y1gXD36XoWdp5hg3JEKYFPEB5M6VQ8S4%2Fdu2vQOEZyfcpClNYNGUA3oA%2BN90rgw2%2BfezAY6pgGctGdkEpe%2Fw7WZUKyGnfNhWzyL2BVSgd8W%2BLXnl%2BZB00Up8aaSuABt0XKflCi2x62JIScE3jFMPj15Ec9Yj6tgX6YXgl77AFjGB3hjXv97nw4x%2FijMnGoS5xr%2BOIxe4yQBLZ%2FdObgmBFKhedzIm%2BqdX4K2Aa6KOwM0I56wrg0nvzNm%2BqVTalim1MXSNx9jyJkkNNASVZiLWvBM5yv0Z2pnusB5%2B2XJ&X-Amz-Signature=7a9944898a5b753e785ec4490c23d9e6b5740c6964bc2c63f591ffaf05aa92e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







