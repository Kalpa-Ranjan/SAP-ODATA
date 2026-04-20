



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IEAI3NZ%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T132005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQCc3YLYKpeU7aCJxsgKCD5iIUrVuV%2Bt7L4zFTwN6IGXiAIhAOVUxG5bgxHWpOGZ%2FVpzdEV1D4xH0n4XVdNZsERo26IlKv8DCB0QABoMNjM3NDIzMTgzODA1Igz2EMlrxgymnz295jEq3AMLBKMrFVFdSePDmi%2F3DBqdalFVFOVr2ujNFurlTVQMv0kkwEy29EsItfY6ZPbHx4MPIVTf77sZ3f0hCjxvEXZiv%2BhEB1NG2h2aMiHAHzB2nczWk1IU05mymLELYU1DGw0zgfFcURYX3abrl9Hb4YM4%2FW8mu1qI%2F71wXxfivOh3aC68teVzZvqYE%2F6mMnboXtyniSQQnCPCMGw8XsxYpPo6Bzp5YALE3sr72Qm%2Bk%2B6An8c8slvKwagEroOjr9zMtDF1oX7f%2Fpm01J%2FCfAqyZG4Tp5PbCRVBS%2FH9HpkQ6z0XIV36A%2FwaHf44L9uFh1xVwBuQ6xhtINeCYAmP6KtZ887aDzMK7b%2FFcFE%2FrcmX3zQa6%2FiAqg2m%2FnfD5EItusktnwJB2PCYtB4ka%2FghUZy3WYtB5T7Fm9WNcaGq%2BOer5FKHTi7JOCv1yUOqgACaPe9D6BWLudzRvmIsOYZ04bgpC30%2BDaUBGqduWSgqgjB4cnUW0rKDDv3OW%2Faii7Eu0xksRC%2BUz4vsZjLVWc7OePsOpmixx8AqE8%2Bp0GOzI2CqnOMrkMCQv0%2B3e7LOzrXy6JE9A93aOO0C4j8pMDrHiMYtXJKmHAsZlOqs2C8b%2B3GgZEzKrNP6Xi4l0yv2nhPIQDC3spjPBjqkATcENyMPBMGZhabWkN5521Thy3iR1Mha1JHLuCNzKxgt8RJXGdUHnIxeKi71YWmANt9cgU%2Fpi3VPXe84rePSusK1C3KC2u38yjVBaxXPPYtlPE6uE%2BokTiRP7EZ3iwkhs0k%2FC9TJWo%2FpF03O91iJjDRII8dTgpOYhKhDTYkIxOHCYoPa%2B1fgUPyx0rE7BIlD%2FfHsU3xghF4MxVmk9YzlRwO1GG%2Bo&X-Amz-Signature=6b4c0333a2424be0a2809e225fba0df127783fbfaf7c4de6321a817cc8dc4569&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IEAI3NZ%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T132005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQCc3YLYKpeU7aCJxsgKCD5iIUrVuV%2Bt7L4zFTwN6IGXiAIhAOVUxG5bgxHWpOGZ%2FVpzdEV1D4xH0n4XVdNZsERo26IlKv8DCB0QABoMNjM3NDIzMTgzODA1Igz2EMlrxgymnz295jEq3AMLBKMrFVFdSePDmi%2F3DBqdalFVFOVr2ujNFurlTVQMv0kkwEy29EsItfY6ZPbHx4MPIVTf77sZ3f0hCjxvEXZiv%2BhEB1NG2h2aMiHAHzB2nczWk1IU05mymLELYU1DGw0zgfFcURYX3abrl9Hb4YM4%2FW8mu1qI%2F71wXxfivOh3aC68teVzZvqYE%2F6mMnboXtyniSQQnCPCMGw8XsxYpPo6Bzp5YALE3sr72Qm%2Bk%2B6An8c8slvKwagEroOjr9zMtDF1oX7f%2Fpm01J%2FCfAqyZG4Tp5PbCRVBS%2FH9HpkQ6z0XIV36A%2FwaHf44L9uFh1xVwBuQ6xhtINeCYAmP6KtZ887aDzMK7b%2FFcFE%2FrcmX3zQa6%2FiAqg2m%2FnfD5EItusktnwJB2PCYtB4ka%2FghUZy3WYtB5T7Fm9WNcaGq%2BOer5FKHTi7JOCv1yUOqgACaPe9D6BWLudzRvmIsOYZ04bgpC30%2BDaUBGqduWSgqgjB4cnUW0rKDDv3OW%2Faii7Eu0xksRC%2BUz4vsZjLVWc7OePsOpmixx8AqE8%2Bp0GOzI2CqnOMrkMCQv0%2B3e7LOzrXy6JE9A93aOO0C4j8pMDrHiMYtXJKmHAsZlOqs2C8b%2B3GgZEzKrNP6Xi4l0yv2nhPIQDC3spjPBjqkATcENyMPBMGZhabWkN5521Thy3iR1Mha1JHLuCNzKxgt8RJXGdUHnIxeKi71YWmANt9cgU%2Fpi3VPXe84rePSusK1C3KC2u38yjVBaxXPPYtlPE6uE%2BokTiRP7EZ3iwkhs0k%2FC9TJWo%2FpF03O91iJjDRII8dTgpOYhKhDTYkIxOHCYoPa%2B1fgUPyx0rE7BIlD%2FfHsU3xghF4MxVmk9YzlRwO1GG%2Bo&X-Amz-Signature=9a2d110d3fcc212b475e7d9ad9ebb91d5a9a7f267becd6f162285e811489683a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







