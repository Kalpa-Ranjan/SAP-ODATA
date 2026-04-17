



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653H573G4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T020539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGDTDT8UCinQ91kFl0PxoSVB7MrFTL5TtucjvrBxoPGwIgMB9TV%2FXHaw%2Fa5ZojeXYTln4a%2FwgDI5pBKADPm60n0GwqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5yOUTch5YCfaL%2FrSrcAxNFTxsoSeP2oDC4h92VTIaQiyWpJ4pJoUXgOgkht%2B%2BXTpj13%2Bj047cvpPrb3F7iU%2F0wmpAayL1Al2fVrQdNugNJN28YZyHLBwAvIXVX2cahc508clcnpmb2PE8mGHYFADj0GMcS3maFTx0uCTcWUIbdveHyjChYpumK60VskgRzKJT8xDiPND6v%2BauvaePnlMytzIWPsS1NnUmPuGh7AsPq6wLCUlcSbjQP5%2B0A%2FEAnUm85ZMRmZDs2BdyxniO8Zt4eDlObiBx08%2FtV%2B60tMUQnPwF1six1KIkcQMeXZ%2B9FmSpEcttJD%2FTo%2F2wfF8TndefCo96%2B%2F3SHDA4SBq6xHNUS1IXIGPxkxJBYdthl0TiRC8qf2TgSTFiwv1CRqKIqP3Ae5IPZeT%2FYN6nDbab2kDwJzoFmDRUXxog5KXIG8hPaCDgwmW%2FbfxSL4s7qgQ9UjFCFrpVrFJpuQEl8VvEHIOS7aDzi0nqe3fHw%2FwifW0L15Kk8nTGGyv3paZxtWge80s0ThoCGoX5%2Fk0W1JxIBB4tXgzW5ds2XBSyjeObCkTX4CjRrbI7H6vCFvKRjjAt4bA9JSAv9dUD4ViHqc6eBuxy7%2BX5NR4VsayL87LRPBzqempB7GKXz7P73qzrGMPbZhc8GOqUBp2Tm5pTZDyh3txO8CUuxYFgKnDiTTR8ENZocdcph9mtuzGlwVS26oKgtohpObRqoNnBaEscm2w1hLRY6%2BWX0zGbDaq3XyGndjFJhS2sRy9mbtB91ohS7GpTjYSj%2Bihyv2zdxI4kg73K7H%2BLt5T%2FQ0J7NjUtZFFEqH9ccEXRqk4sUTuTP%2FZTFjXhd4GW0bhB0g5R4vNxKhtlPPnleMqlLRlumPNQb&X-Amz-Signature=77d199e8df457607c1c694d96c1917d3e3d9beb0ad4391f25aa7dfdcce51ebba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653H573G4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T020539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGDTDT8UCinQ91kFl0PxoSVB7MrFTL5TtucjvrBxoPGwIgMB9TV%2FXHaw%2Fa5ZojeXYTln4a%2FwgDI5pBKADPm60n0GwqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5yOUTch5YCfaL%2FrSrcAxNFTxsoSeP2oDC4h92VTIaQiyWpJ4pJoUXgOgkht%2B%2BXTpj13%2Bj047cvpPrb3F7iU%2F0wmpAayL1Al2fVrQdNugNJN28YZyHLBwAvIXVX2cahc508clcnpmb2PE8mGHYFADj0GMcS3maFTx0uCTcWUIbdveHyjChYpumK60VskgRzKJT8xDiPND6v%2BauvaePnlMytzIWPsS1NnUmPuGh7AsPq6wLCUlcSbjQP5%2B0A%2FEAnUm85ZMRmZDs2BdyxniO8Zt4eDlObiBx08%2FtV%2B60tMUQnPwF1six1KIkcQMeXZ%2B9FmSpEcttJD%2FTo%2F2wfF8TndefCo96%2B%2F3SHDA4SBq6xHNUS1IXIGPxkxJBYdthl0TiRC8qf2TgSTFiwv1CRqKIqP3Ae5IPZeT%2FYN6nDbab2kDwJzoFmDRUXxog5KXIG8hPaCDgwmW%2FbfxSL4s7qgQ9UjFCFrpVrFJpuQEl8VvEHIOS7aDzi0nqe3fHw%2FwifW0L15Kk8nTGGyv3paZxtWge80s0ThoCGoX5%2Fk0W1JxIBB4tXgzW5ds2XBSyjeObCkTX4CjRrbI7H6vCFvKRjjAt4bA9JSAv9dUD4ViHqc6eBuxy7%2BX5NR4VsayL87LRPBzqempB7GKXz7P73qzrGMPbZhc8GOqUBp2Tm5pTZDyh3txO8CUuxYFgKnDiTTR8ENZocdcph9mtuzGlwVS26oKgtohpObRqoNnBaEscm2w1hLRY6%2BWX0zGbDaq3XyGndjFJhS2sRy9mbtB91ohS7GpTjYSj%2Bihyv2zdxI4kg73K7H%2BLt5T%2FQ0J7NjUtZFFEqH9ccEXRqk4sUTuTP%2FZTFjXhd4GW0bhB0g5R4vNxKhtlPPnleMqlLRlumPNQb&X-Amz-Signature=1d67bd791922e204f4e3dda47c806165618d7eaffa2a5375ec1167decdc9d713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







