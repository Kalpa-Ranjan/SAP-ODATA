



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGSSLTWG%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDHhWqB%2B3zbd7v%2FJSrdmjLe69OiSq7x1ztkAyewc3Ep2wIgCBh1UPLw%2F4GNuzo6vhz1lJbwYCkJBYrnMRh%2F%2FANGlh8qiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcfV3addI6Uun%2B0XyrcA8N3zktfmWAFO%2BdiYQfiG5cxn1SoGX4uyFf7uCJL2XHSL4mHAfB3jYXnxULz02JpS5xDjJIvGXbP879gemub%2F4v3z%2BxGDRuPaN2mSmBBfnmXcPpnOHRCH7EAUODhUAuNlboz7vAossPWcCfzrTg%2FavamSzmJqB5m6Z%2F1fJa%2Fd3GQ%2FsHPygQBxP%2B3JjygzhV7HN2HvKTvM8L7TfjURiwH%2B8Z7DQESzBPh9S1Q509KmuhXDPfIt6zOd%2FKdcx2ElPDIraaFtqFsat8vZT6fVN%2BjaXA%2B7NaRVKiPZnAGxhuc1oCVQgPbLJpbQbg9rpAul9lzCcVKcvlP6OQv7VrzAEZtYr3qvJbGr6%2BvffGFho4gM2CsZN%2FAveKivqvaXZFI5N04WAv2plbUFrFQ793cuTAbWtPenvRDT7dKcWJkGRr0rjuG1CQJMNi5aHxHNT8GugHtu8czJ9myhSMAedPNb%2F48IN%2BpYMPVMThg5TATjfveC244Np1SIMxQfdlMMAlG7KIj8gF5gyY0CKGx1XCapEQwuGkgdlbK5LS0h0DwoGW%2B%2FIb8DY8VkfBzbAig4zIxd0It8Yl%2F3IaiWkwogrG76QU45qz96THY46Xy1ge6jQKMT9oErPtH4y3Xxhy%2BfpScMMXGj8gGOqUBJxFVtnYpuiMgD%2FHaCXP3AbnIm7hCeGpL99lR%2FYgT%2FElej9bWCClbTjONcxF1FcLtKGOi09aEbJ3nfvk%2FMIguzP0aZYa5RNmzCAdu%2B7z7W%2BVkY5%2BWBGHtPDvJ4er6osXgy0H5UWEdEDGwtY%2FgT4wOhUO9Hsk7Yib%2FvwK7lmHkJB28LWanC7xs11PfdwyS%2BOmh%2BmIk9jKS%2FOTBFE1dteHQ45ExUvW5&X-Amz-Signature=b005d3069dfe77819ce2a5ef25b0781f1cb6953df91efc3098ac631bbd341804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGSSLTWG%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDHhWqB%2B3zbd7v%2FJSrdmjLe69OiSq7x1ztkAyewc3Ep2wIgCBh1UPLw%2F4GNuzo6vhz1lJbwYCkJBYrnMRh%2F%2FANGlh8qiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcfV3addI6Uun%2B0XyrcA8N3zktfmWAFO%2BdiYQfiG5cxn1SoGX4uyFf7uCJL2XHSL4mHAfB3jYXnxULz02JpS5xDjJIvGXbP879gemub%2F4v3z%2BxGDRuPaN2mSmBBfnmXcPpnOHRCH7EAUODhUAuNlboz7vAossPWcCfzrTg%2FavamSzmJqB5m6Z%2F1fJa%2Fd3GQ%2FsHPygQBxP%2B3JjygzhV7HN2HvKTvM8L7TfjURiwH%2B8Z7DQESzBPh9S1Q509KmuhXDPfIt6zOd%2FKdcx2ElPDIraaFtqFsat8vZT6fVN%2BjaXA%2B7NaRVKiPZnAGxhuc1oCVQgPbLJpbQbg9rpAul9lzCcVKcvlP6OQv7VrzAEZtYr3qvJbGr6%2BvffGFho4gM2CsZN%2FAveKivqvaXZFI5N04WAv2plbUFrFQ793cuTAbWtPenvRDT7dKcWJkGRr0rjuG1CQJMNi5aHxHNT8GugHtu8czJ9myhSMAedPNb%2F48IN%2BpYMPVMThg5TATjfveC244Np1SIMxQfdlMMAlG7KIj8gF5gyY0CKGx1XCapEQwuGkgdlbK5LS0h0DwoGW%2B%2FIb8DY8VkfBzbAig4zIxd0It8Yl%2F3IaiWkwogrG76QU45qz96THY46Xy1ge6jQKMT9oErPtH4y3Xxhy%2BfpScMMXGj8gGOqUBJxFVtnYpuiMgD%2FHaCXP3AbnIm7hCeGpL99lR%2FYgT%2FElej9bWCClbTjONcxF1FcLtKGOi09aEbJ3nfvk%2FMIguzP0aZYa5RNmzCAdu%2B7z7W%2BVkY5%2BWBGHtPDvJ4er6osXgy0H5UWEdEDGwtY%2FgT4wOhUO9Hsk7Yib%2FvwK7lmHkJB28LWanC7xs11PfdwyS%2BOmh%2BmIk9jKS%2FOTBFE1dteHQ45ExUvW5&X-Amz-Signature=065dfbffc46e79b2435cc1846e71ffe686fa72c463efc4c45209abf72292576e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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





Test Github-Notion synch



