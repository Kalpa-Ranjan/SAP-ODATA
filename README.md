



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636FYJEI6%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T182328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDW0qWAqlmBs6rH%2Fasmc6Y4UuL7cPi%2FDwgdY%2BEn9HAcggIgMliH5FBWNhQh5E7j5M5dcescngzV2%2F4L51AAcFvJY3MqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2B8F6wOxqqe4J0OUircA57YAiSVtTV%2F47XmAK2kji6zsh34rXgpltXQuoH1IXP4RItjmdz5JkIXYT5kMH4vwm059gaVtPVn9T0mFUZ0wcR5il9K1w9%2BZ2V6TyTlXDf0apXROBLwptgVUyLfoZ%2Ba0kOutUZ5uJqwEEC7SP1QiTsSY2Ngj6p7%2BrPmz7lSFc3FwXPqciExmEkDUFjf1MdA8%2FIaLpxO%2FtsIykmEgRXCTv1n2yn7ztj5NaECA3waBIef%2B28Ieozeu36QHxmN4AkcKmRy2aweM9ZP61PyncOvQJXA8VTFRHZgMDm%2BR8pe%2FeAt0x8ScHOf75Mc5cnhCSbrFoyOwdK%2B4bOJ7P%2FYSs7vGDZlETIXXrz9yBaf4xbAE1gGWFe1elV5kh2jlzZsZ9TOzyEpmvF9cbRnDN%2BmFI0X3JEhVRf1SoTb6arYthzx12enL4UxrSDk8i%2Frjq8Ec1GtMNYG4yJ2D%2FyvTwWaMoFXxRF6bKX4mVsYvxDoRvOvTANnL31EqSpHz8F2t2QRm9Beqg0NF5YqG5mbTuVPPaYI3jrL%2Fmimr%2Bd4ESR4CazSq9F7TPhKI6NgDrYthMOL5UsgLFntYxKc5Sf6eA93dY2T18wqVvNuWFqTvL8N6QiypXo2q1UbfbiquIv%2FXW3HMJaplsoGOqUBOFXCXHJg19DR%2BHxTMY3HJAANsl9pu%2FsDRqby8nMMHq%2BgIv1v4nzftCTIWvohhp10c2JP5xsMPAELfNS5rRA1bqHuSXkAWCR4zb4shtikfcXy1vfHJwJEwh%2Fvm4SGVSHpuKyG3cjUoXzjqGSzFB0aVWwp28ZSzMXv2CmnG%2F5KRsUVlQVn4N2iLc6TEb17Kp1qFYXcEpgChRM95p0grWVMLePepYXG&X-Amz-Signature=a4496495abfeb9be0c6b70f03d536ceaa1b8e3d9e632fe52db2b9dad2130b2bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636FYJEI6%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T182329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDW0qWAqlmBs6rH%2Fasmc6Y4UuL7cPi%2FDwgdY%2BEn9HAcggIgMliH5FBWNhQh5E7j5M5dcescngzV2%2F4L51AAcFvJY3MqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2B8F6wOxqqe4J0OUircA57YAiSVtTV%2F47XmAK2kji6zsh34rXgpltXQuoH1IXP4RItjmdz5JkIXYT5kMH4vwm059gaVtPVn9T0mFUZ0wcR5il9K1w9%2BZ2V6TyTlXDf0apXROBLwptgVUyLfoZ%2Ba0kOutUZ5uJqwEEC7SP1QiTsSY2Ngj6p7%2BrPmz7lSFc3FwXPqciExmEkDUFjf1MdA8%2FIaLpxO%2FtsIykmEgRXCTv1n2yn7ztj5NaECA3waBIef%2B28Ieozeu36QHxmN4AkcKmRy2aweM9ZP61PyncOvQJXA8VTFRHZgMDm%2BR8pe%2FeAt0x8ScHOf75Mc5cnhCSbrFoyOwdK%2B4bOJ7P%2FYSs7vGDZlETIXXrz9yBaf4xbAE1gGWFe1elV5kh2jlzZsZ9TOzyEpmvF9cbRnDN%2BmFI0X3JEhVRf1SoTb6arYthzx12enL4UxrSDk8i%2Frjq8Ec1GtMNYG4yJ2D%2FyvTwWaMoFXxRF6bKX4mVsYvxDoRvOvTANnL31EqSpHz8F2t2QRm9Beqg0NF5YqG5mbTuVPPaYI3jrL%2Fmimr%2Bd4ESR4CazSq9F7TPhKI6NgDrYthMOL5UsgLFntYxKc5Sf6eA93dY2T18wqVvNuWFqTvL8N6QiypXo2q1UbfbiquIv%2FXW3HMJaplsoGOqUBOFXCXHJg19DR%2BHxTMY3HJAANsl9pu%2FsDRqby8nMMHq%2BgIv1v4nzftCTIWvohhp10c2JP5xsMPAELfNS5rRA1bqHuSXkAWCR4zb4shtikfcXy1vfHJwJEwh%2Fvm4SGVSHpuKyG3cjUoXzjqGSzFB0aVWwp28ZSzMXv2CmnG%2F5KRsUVlQVn4N2iLc6TEb17Kp1qFYXcEpgChRM95p0grWVMLePepYXG&X-Amz-Signature=5b763d1edd9f8950a057e439921e42717f6fda70cf295c11c8f82d987b109748&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







