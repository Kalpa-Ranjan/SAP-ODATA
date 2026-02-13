



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKQGF6S%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T015205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCSn2EU9h%2B8ySJzrwDdott%2FZKmy3naApVet5IQncO6EZQIgAttEP7CJxQXmJT9WVZmT4IkOJPjO91IqEWsSRxlhqP4qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFG%2BZjCXh1H3EJR2SrcA2su3krRtEdzRgOZKKmqFLb1h8lCK5%2FYnpcEDGzy1013VWPI%2FGgRIF9WApRZkMxpSAFUrtjB2ckAEy1fYA5aPT8qvqMOqZI6NgAe0FrnJzujBgMtjSvEuxif3mVfqaLxykVHYfNg%2FbgxR%2F7rYCUYvB%2B1uh4HfP646thl3oDGLYkmWp5OsdWhhTO2n1c02IXFYUVYoVJyOxQdWU1FBalXjMtAz4ImVqTr7pTAI9dgO6xV2Kkza3BDfZ%2F7S6iUSBjy1ilHWTvDDLFoyCDh30LWbKfPDMsGDOyM9iDS5PeUn2g3ex7tDk7iy%2F3T9Tz5EIjhpZCe36wZPVUz1OtSbSQQRTQrpr18m8iLbvzZgjt7POjcNgvymBoleP7jWIA7DVSG%2BkAxZIf2Hjct9hT1ViPzoVloO6dyS6MP%2BWnP4OesTvxkGzMR74lnQB6gvH2lTQLPloRSqRQ5wIPiDzIFTaRdz2%2F2u4OpbLcbE8NZkjZbmmMscI671%2B%2BB0WRtTFBVhtI5H0z%2BmPVMTtAxMNEKkHCce9hIaWdd91UiJSyC0v%2FLMAeuGNFLKNcX9OhMDtBGKszINz%2FoNRtkNljzqJ0B09%2BR%2F8HWBeTi162LqXpsd7WPRbshRAlMwM9xscHnmDDsMOrsucwGOqUBN%2FDhzvklHlx%2B9%2Bkx%2BY%2BHPdZbpstGcq8C1Cx1YU6O%2BIfyvzfPawFvTsjjqUSimbn1qdMlGFhJW4njTqjFw0gNNqGjhwRHFjWoKm512e4M5joJc7fj8djFc%2Bp8NFZM0w%2BADAYcb%2FsnvvPis3QG2adoFAXE5pU1aaMnucC70y048%2BPS1YKrWB9EEzdXTaoBbDTUAIZo1k%2BqS2Zlkn6WnhZUt%2FMV1ejH&X-Amz-Signature=e154fa25d53df2a86c7961a79969af63fcf731952156670ec026c3b0960810a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKQGF6S%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T015205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCSn2EU9h%2B8ySJzrwDdott%2FZKmy3naApVet5IQncO6EZQIgAttEP7CJxQXmJT9WVZmT4IkOJPjO91IqEWsSRxlhqP4qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFG%2BZjCXh1H3EJR2SrcA2su3krRtEdzRgOZKKmqFLb1h8lCK5%2FYnpcEDGzy1013VWPI%2FGgRIF9WApRZkMxpSAFUrtjB2ckAEy1fYA5aPT8qvqMOqZI6NgAe0FrnJzujBgMtjSvEuxif3mVfqaLxykVHYfNg%2FbgxR%2F7rYCUYvB%2B1uh4HfP646thl3oDGLYkmWp5OsdWhhTO2n1c02IXFYUVYoVJyOxQdWU1FBalXjMtAz4ImVqTr7pTAI9dgO6xV2Kkza3BDfZ%2F7S6iUSBjy1ilHWTvDDLFoyCDh30LWbKfPDMsGDOyM9iDS5PeUn2g3ex7tDk7iy%2F3T9Tz5EIjhpZCe36wZPVUz1OtSbSQQRTQrpr18m8iLbvzZgjt7POjcNgvymBoleP7jWIA7DVSG%2BkAxZIf2Hjct9hT1ViPzoVloO6dyS6MP%2BWnP4OesTvxkGzMR74lnQB6gvH2lTQLPloRSqRQ5wIPiDzIFTaRdz2%2F2u4OpbLcbE8NZkjZbmmMscI671%2B%2BB0WRtTFBVhtI5H0z%2BmPVMTtAxMNEKkHCce9hIaWdd91UiJSyC0v%2FLMAeuGNFLKNcX9OhMDtBGKszINz%2FoNRtkNljzqJ0B09%2BR%2F8HWBeTi162LqXpsd7WPRbshRAlMwM9xscHnmDDsMOrsucwGOqUBN%2FDhzvklHlx%2B9%2Bkx%2BY%2BHPdZbpstGcq8C1Cx1YU6O%2BIfyvzfPawFvTsjjqUSimbn1qdMlGFhJW4njTqjFw0gNNqGjhwRHFjWoKm512e4M5joJc7fj8djFc%2Bp8NFZM0w%2BADAYcb%2FsnvvPis3QG2adoFAXE5pU1aaMnucC70y048%2BPS1YKrWB9EEzdXTaoBbDTUAIZo1k%2BqS2Zlkn6WnhZUt%2FMV1ejH&X-Amz-Signature=aaaf1f2d3896007548b464c2b0aa2b4235eb9465665a0eb296a88046f2ac0f11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







