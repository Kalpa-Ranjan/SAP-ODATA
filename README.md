



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSBTPSVH%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T123318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIEFIhngWKOH9uClWDm2JQQ0N5fSv%2F4YFau6HYSW%2B25xZAiAGGAdyEtJgq9qf647yyEchYJXP3p0MUA1LRNYmAnBwiSqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMztg5pglPQiGBc5ViKtwDiNup17%2FxafBug5uL1s0K%2BzvfsZSBgi9UJRbuBciRUmj8abVC3%2F%2B6DSPo5rBIWFZ6JYz3NQF7xPt1pmd%2FM26mu1phdhNT7RMRYrO3oaplro9wj0byjgwvLwTJ%2BS6jaGhLgLIiVRoo2DOovtYkZONXMmRtPSKPKt6m9ggdULreialxyjbqYpkdTW5NBrfQMTkuY93dYRaDssBI%2FhiSWZFGkKb5JrOfB78nx%2F3RNookVBFhMdKjMgTt6xuwl%2F9dmp7AfQlYPafSX62HejtzsT0pCb61qF043tIo6RH1hWJUHrBPELFq2btayaZ%2BGXLEEXAx7kshoCZ7OTiHJ7sbV4xCGFElC3gNp%2BJYiS6bbUeDpb99%2FB%2FRQvBrzdxfHghxXSwYI1rSYuomKul1HapTCvVt4nnAZd%2FRjqQg1WzEE2hzVqbQr%2FSl%2FhjAzYJrm95CB4Vqx11aFtdFS7jJ3yOUEZXa7PUFoIRoOu6WRtkjoAX5mZ59kWucR4HIH5x03Tkmg3CTw6LsQ4xC27hvK%2BlnJd3H4XlhJpIFd35Dvf9kncy49cHD1gSee4XJXCAgvoJN%2Bq3ZW4SgEbc%2Fdg0sFm6HmeTfOEyfnaG4RdjDVvAD3M2JIv7wbPJRx4VMfSUuAuow1er2yAY6pgFmLSBTdTaB%2B1xaEfSya9jX8A0tuwCrq0zy2ltJJEssF6dXz9iW%2F6w7RZxW0FZtAlU2p66cZ3qMvdVBAGoxUF11WQ28oc5zMBXtkdGYk2IA%2FelM2bjKMYgfcRfzclvfzMoSH7uFOvfk9egLGuNsOgSdxGFUwEPpYz8sRRkm5lFf8k4LzddUtdhZ2pak96uJdWz495cCV2zjMuAzia2wjGMc%2FJF5%2BsKJ&X-Amz-Signature=d912509faaa208ec3720a2635d60c4c18b67dd74db5074ea42cb07ee1668c3d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSBTPSVH%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T123318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIEFIhngWKOH9uClWDm2JQQ0N5fSv%2F4YFau6HYSW%2B25xZAiAGGAdyEtJgq9qf647yyEchYJXP3p0MUA1LRNYmAnBwiSqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMztg5pglPQiGBc5ViKtwDiNup17%2FxafBug5uL1s0K%2BzvfsZSBgi9UJRbuBciRUmj8abVC3%2F%2B6DSPo5rBIWFZ6JYz3NQF7xPt1pmd%2FM26mu1phdhNT7RMRYrO3oaplro9wj0byjgwvLwTJ%2BS6jaGhLgLIiVRoo2DOovtYkZONXMmRtPSKPKt6m9ggdULreialxyjbqYpkdTW5NBrfQMTkuY93dYRaDssBI%2FhiSWZFGkKb5JrOfB78nx%2F3RNookVBFhMdKjMgTt6xuwl%2F9dmp7AfQlYPafSX62HejtzsT0pCb61qF043tIo6RH1hWJUHrBPELFq2btayaZ%2BGXLEEXAx7kshoCZ7OTiHJ7sbV4xCGFElC3gNp%2BJYiS6bbUeDpb99%2FB%2FRQvBrzdxfHghxXSwYI1rSYuomKul1HapTCvVt4nnAZd%2FRjqQg1WzEE2hzVqbQr%2FSl%2FhjAzYJrm95CB4Vqx11aFtdFS7jJ3yOUEZXa7PUFoIRoOu6WRtkjoAX5mZ59kWucR4HIH5x03Tkmg3CTw6LsQ4xC27hvK%2BlnJd3H4XlhJpIFd35Dvf9kncy49cHD1gSee4XJXCAgvoJN%2Bq3ZW4SgEbc%2Fdg0sFm6HmeTfOEyfnaG4RdjDVvAD3M2JIv7wbPJRx4VMfSUuAuow1er2yAY6pgFmLSBTdTaB%2B1xaEfSya9jX8A0tuwCrq0zy2ltJJEssF6dXz9iW%2F6w7RZxW0FZtAlU2p66cZ3qMvdVBAGoxUF11WQ28oc5zMBXtkdGYk2IA%2FelM2bjKMYgfcRfzclvfzMoSH7uFOvfk9egLGuNsOgSdxGFUwEPpYz8sRRkm5lFf8k4LzddUtdhZ2pak96uJdWz495cCV2zjMuAzia2wjGMc%2FJF5%2BsKJ&X-Amz-Signature=29b598658c0e684b0615401333863fe85952cf3f2fbf1f44c0b1bb4422886a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







