



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQXIOYN4%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T123158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRSJioH6%2BSfsSzb484%2BDn%2BzavLkBUEps2kL6f04cdiTwIgKjRDCLMKqrGt0GjRPQ6x7f5qCObu1VOVJ9f7UlYFjd4qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpTcWB2dKXkAGgzwSrcAzsbGSlbvoqLt3uF4Pro1pKotAKhzCQmu%2B49n85TFUlGLYwgieab8VDrNMz42xOsnRvh8l8a6vPhYkfEn8%2BMEq9MltwvGPIKKLeOhznD4%2Fb7YASacQNzQlwlcsCBS5C6RBGr6G405zDIMt4r1YntYmMe2u1KmVtAna%2Bkob7e8a%2BFSCRizIOxBBfd9kuy9z3cgSFNZNVGNY2k6KAX7Xtel6zUa6FwlkHneZF8cLvob2QioFBcEZiVVnivqTGbBwKseX%2BBP%2BMO1FjM48SEmIYk8urKLOiT%2FsFCNBU6W5JrkywyY1n4%2F2HJgfKjDEVg%2Bf9r33ybqXFcxu7DA1Gx2dxpOWkYauHvvoO5uOdFx%2BffBKFY0l%2B4lAumNiODclPbzN9sA1P60wZfMNMdE2IHVFLZ6qlHclKdKUZdnTuA8IG3ZYVPvpjgdVFety2o6gKmR8GuXrd1jvAfPoFL2Bfl1Xt2Pd1dSj3EqqVNAF%2FfLD2N%2FaPxCzC9Afae9vKsEazTYWhmEgO2XUWWNAEEAwfIxV%2BqERX5asGKYxaI%2FOKqd4MA9ePRwAUVonaKlc7zrkfSewbZyZFo2Ojev%2FzmYTVRYTC8RC54yd0%2F9Vnr3lilry75urqQxBYQoei%2F7N3DwpZbMN%2FLpckGOqUB3awdnSiga5lVETuN6x2jDJeoftiR54FeY7sAb6NYyOSyJpZe5pHa132%2B07qUqi8aLDCYPG5sqQ3cAm7pMcenuUVbV%2FlVZOgrtGHxVfnMm4S4cLjsViAAgp7weNgh%2BrU9xSMWtwIQRfp5tRclV%2FM%2Bx0A%2F8dsoXrNhZLFHHYk0Mes8VuQoCCTAKek8fTHiZk4OuHc2OYQv%2FMYqUiv%2BK44QTM2KSz1q&X-Amz-Signature=d1d125ae6555ff2d3436e042ae19ec90a4790c57a5159b91c4660ea84364a632&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQXIOYN4%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T123158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRSJioH6%2BSfsSzb484%2BDn%2BzavLkBUEps2kL6f04cdiTwIgKjRDCLMKqrGt0GjRPQ6x7f5qCObu1VOVJ9f7UlYFjd4qiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpTcWB2dKXkAGgzwSrcAzsbGSlbvoqLt3uF4Pro1pKotAKhzCQmu%2B49n85TFUlGLYwgieab8VDrNMz42xOsnRvh8l8a6vPhYkfEn8%2BMEq9MltwvGPIKKLeOhznD4%2Fb7YASacQNzQlwlcsCBS5C6RBGr6G405zDIMt4r1YntYmMe2u1KmVtAna%2Bkob7e8a%2BFSCRizIOxBBfd9kuy9z3cgSFNZNVGNY2k6KAX7Xtel6zUa6FwlkHneZF8cLvob2QioFBcEZiVVnivqTGbBwKseX%2BBP%2BMO1FjM48SEmIYk8urKLOiT%2FsFCNBU6W5JrkywyY1n4%2F2HJgfKjDEVg%2Bf9r33ybqXFcxu7DA1Gx2dxpOWkYauHvvoO5uOdFx%2BffBKFY0l%2B4lAumNiODclPbzN9sA1P60wZfMNMdE2IHVFLZ6qlHclKdKUZdnTuA8IG3ZYVPvpjgdVFety2o6gKmR8GuXrd1jvAfPoFL2Bfl1Xt2Pd1dSj3EqqVNAF%2FfLD2N%2FaPxCzC9Afae9vKsEazTYWhmEgO2XUWWNAEEAwfIxV%2BqERX5asGKYxaI%2FOKqd4MA9ePRwAUVonaKlc7zrkfSewbZyZFo2Ojev%2FzmYTVRYTC8RC54yd0%2F9Vnr3lilry75urqQxBYQoei%2F7N3DwpZbMN%2FLpckGOqUB3awdnSiga5lVETuN6x2jDJeoftiR54FeY7sAb6NYyOSyJpZe5pHa132%2B07qUqi8aLDCYPG5sqQ3cAm7pMcenuUVbV%2FlVZOgrtGHxVfnMm4S4cLjsViAAgp7weNgh%2BrU9xSMWtwIQRfp5tRclV%2FM%2Bx0A%2F8dsoXrNhZLFHHYk0Mes8VuQoCCTAKek8fTHiZk4OuHc2OYQv%2FMYqUiv%2BK44QTM2KSz1q&X-Amz-Signature=fd4d6b3030ee2dadbb8bcea47666be067dd323710d51361360cbd33f0b98756e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







