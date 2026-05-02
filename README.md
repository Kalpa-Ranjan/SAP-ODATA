



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKSGD7XN%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T072510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICg9Mxif8J8sgbiEh5JtPrWcJeXiyVRDmsbaq8dHLcJkAiBuAaQMIlU0T%2FkEmV2jM6%2Bjx7EXJRNP4qr3SaSYxCsB4Sr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMldRPZM8B1n%2BVmRNhKtwD4w9RN8AF8qWT5DUgNQeCsETchkAY5Oc3u9myTzhSg1quR7%2FeQrBndsS0eVxuXLE%2B8raKajjEZH45HH9%2FWix%2Fy%2BjxJUdDBldsxL6QV%2Fako2GEAUj438APH3VyXWmqEIWbQUc8NhobOQI8Y9lWizX1lfvJlodaSD5gDZOih2Aj3t%2BAimVWyD6mWmd%2FSDad3ZEn2j%2FDONvQbfgIoomchFRYriyLnI9N7qQwZyUUeKP8KtpQQqJ7j3u20MfoVifLfbJxl8Wgsf3NK8Qul4Vr8S6SVoRdWIe9z%2Bb%2Bfyi06E7IveAO%2BbYqe6b9subjhTEjWD4zKS5%2FvprgJjha85GkU%2FPf29%2BmpOL2FYrOY6Is3%2BdFR9P9XSePXAmfic55acYkEbKRWlDmhHl9wJTIg39E8Gku2tFIhNZBr%2BqySXuZigd%2F9OwqyLwcDrfBc48%2Blw%2B%2BEtBwyp98kFdWcRhABzxpMzDJFmj7%2F6vq65q9agaunKgz1KrX%2BfWPKYfUWQEUYTTa4Lwr5FI8wLc43MORFDaYukv0qgyxLDiw1XT6ryRJWekaZbUjbhfILn8yZXACMZVLatZPcWHvij78aGQfBpwGP5ygu1Fw%2B%2FuYgn0deQkPeg%2BQ0UgdXgOvQc%2FAJJghtUcw%2FMfWzwY6pgGlbWXBlM%2BzzV3h8h6lZeluP0Q3KsvNCSsVc2soUdpDPAzJbYVwiofLOA4BDEZmaFAcn8v7din0mM1lBhiJGSCmev5qyMJYKv1Cptb2Qs6C0V7WKDnsefrLkYSPytHcW0Rk%2FcsgHWkNSFArJF5e5mbTiU8M%2FvAx8JhDZcVqM4J0BMFzpoQMrfzwypjqGRfRoGTS42ogWXTO4AompmUK7AfxNNG5cFos&X-Amz-Signature=38acf0e0ea6daa775a3ddbdfda94bb5432e1bd86c613a6812667539839fbdd4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKSGD7XN%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T072510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCICg9Mxif8J8sgbiEh5JtPrWcJeXiyVRDmsbaq8dHLcJkAiBuAaQMIlU0T%2FkEmV2jM6%2Bjx7EXJRNP4qr3SaSYxCsB4Sr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMldRPZM8B1n%2BVmRNhKtwD4w9RN8AF8qWT5DUgNQeCsETchkAY5Oc3u9myTzhSg1quR7%2FeQrBndsS0eVxuXLE%2B8raKajjEZH45HH9%2FWix%2Fy%2BjxJUdDBldsxL6QV%2Fako2GEAUj438APH3VyXWmqEIWbQUc8NhobOQI8Y9lWizX1lfvJlodaSD5gDZOih2Aj3t%2BAimVWyD6mWmd%2FSDad3ZEn2j%2FDONvQbfgIoomchFRYriyLnI9N7qQwZyUUeKP8KtpQQqJ7j3u20MfoVifLfbJxl8Wgsf3NK8Qul4Vr8S6SVoRdWIe9z%2Bb%2Bfyi06E7IveAO%2BbYqe6b9subjhTEjWD4zKS5%2FvprgJjha85GkU%2FPf29%2BmpOL2FYrOY6Is3%2BdFR9P9XSePXAmfic55acYkEbKRWlDmhHl9wJTIg39E8Gku2tFIhNZBr%2BqySXuZigd%2F9OwqyLwcDrfBc48%2Blw%2B%2BEtBwyp98kFdWcRhABzxpMzDJFmj7%2F6vq65q9agaunKgz1KrX%2BfWPKYfUWQEUYTTa4Lwr5FI8wLc43MORFDaYukv0qgyxLDiw1XT6ryRJWekaZbUjbhfILn8yZXACMZVLatZPcWHvij78aGQfBpwGP5ygu1Fw%2B%2FuYgn0deQkPeg%2BQ0UgdXgOvQc%2FAJJghtUcw%2FMfWzwY6pgGlbWXBlM%2BzzV3h8h6lZeluP0Q3KsvNCSsVc2soUdpDPAzJbYVwiofLOA4BDEZmaFAcn8v7din0mM1lBhiJGSCmev5qyMJYKv1Cptb2Qs6C0V7WKDnsefrLkYSPytHcW0Rk%2FcsgHWkNSFArJF5e5mbTiU8M%2FvAx8JhDZcVqM4J0BMFzpoQMrfzwypjqGRfRoGTS42ogWXTO4AompmUK7AfxNNG5cFos&X-Amz-Signature=c1d128b7e3d814f9e90c3c9f9c076928ae4fa5b56a237b13f29a2b23b727d878&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







