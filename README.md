



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE5I2FDU%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T135802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIF6f%2Fa6438PzMk7kjIcfd%2B8mDdt24%2FBlef%2BVDrny4hX%2BAiEA0mVZALagThSSz5nZ39H%2Fb%2B0GxrJ%2FT%2B26y%2BYYXjR6gJwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI5BWMFp6vY%2B8t6aSyrcA1Hq6vdj1BeCqb8DN13AqDiyUAmymw38E%2FSesMdYfA9Ire%2BE8K0vlgp5MXynpWB62x2y0aujEz01r3EdBGgRNIINTk6BbQ67hD5M1WRyOuzm64n5lZQ3qvXEFgQYTFfg6eq3f3%2FkacdmvMwtRHgLKW5hFzhBouVOuHyIykgPtp3B7dEMtkfdySTWVJsx3TY4IalhQym%2BdDlsg09ZzZt7YqBTk9xByCBXmxyf4HNbcA2S5albZfE0VNXg0VVhP%2FU16oM1c9U8HBGyqoOwRzCby%2BzwiyHKMxqFNUpBCDqgUPefboEN9mVxap8f5L49ZbrQ8XgFjJVwFqGO%2Bh2EW1Xwvz62czkdTajTGbr2V%2Fv12GycTJXtwz5avtnqqZENfCqrczeEXFEDYV3L9R7y9Df5xb6DHlAjoMg5wmxtrJZ2EZ7hY3M1xwa%2FplvQUEgUHurnHRZLNEtB8bkrRuhs4mfq4c8g%2BFPZBT%2BAqZGPKbDn3NWzq1NrRFKPWUoiOpfzOq61OPq7SZ2dKVLE7if9NjijIaoqukeq4Td18X0AS0zs9CSxEKNVIQuRg22js6y%2BKHFDebowhCTgm%2Fo53OJkRDJM4jiZSLZIXU73MVGHDzSCH00f6wzBYw1kCbbSHJ57MOyk39EGOqUB%2F4W912qf1R5pPAkbdh6jRPecTiy61WQDMBF8yDOPLpS1coGV4re8b%2BEH%2FniGY4LffCYI%2Belljsc5%2Br5CtikQbc3X8eQXn1F%2FjvBqXIpbcA2lCPPtEiyqZloHvniUygck%2FNezpDzlO3xPVuobpcxNADzRw%2BOTWl%2BTHGaLkZUbrrUP4BRJz6VDws5ExwhI4GUpv%2BcEYxvj%2BCQn%2FT6km7YNzHiBsxsu&X-Amz-Signature=028128a37f98469b96c2ecbea2db3bbd0582a3154d1d74b60084db16bc8161ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE5I2FDU%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T135802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIF6f%2Fa6438PzMk7kjIcfd%2B8mDdt24%2FBlef%2BVDrny4hX%2BAiEA0mVZALagThSSz5nZ39H%2Fb%2B0GxrJ%2FT%2B26y%2BYYXjR6gJwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI5BWMFp6vY%2B8t6aSyrcA1Hq6vdj1BeCqb8DN13AqDiyUAmymw38E%2FSesMdYfA9Ire%2BE8K0vlgp5MXynpWB62x2y0aujEz01r3EdBGgRNIINTk6BbQ67hD5M1WRyOuzm64n5lZQ3qvXEFgQYTFfg6eq3f3%2FkacdmvMwtRHgLKW5hFzhBouVOuHyIykgPtp3B7dEMtkfdySTWVJsx3TY4IalhQym%2BdDlsg09ZzZt7YqBTk9xByCBXmxyf4HNbcA2S5albZfE0VNXg0VVhP%2FU16oM1c9U8HBGyqoOwRzCby%2BzwiyHKMxqFNUpBCDqgUPefboEN9mVxap8f5L49ZbrQ8XgFjJVwFqGO%2Bh2EW1Xwvz62czkdTajTGbr2V%2Fv12GycTJXtwz5avtnqqZENfCqrczeEXFEDYV3L9R7y9Df5xb6DHlAjoMg5wmxtrJZ2EZ7hY3M1xwa%2FplvQUEgUHurnHRZLNEtB8bkrRuhs4mfq4c8g%2BFPZBT%2BAqZGPKbDn3NWzq1NrRFKPWUoiOpfzOq61OPq7SZ2dKVLE7if9NjijIaoqukeq4Td18X0AS0zs9CSxEKNVIQuRg22js6y%2BKHFDebowhCTgm%2Fo53OJkRDJM4jiZSLZIXU73MVGHDzSCH00f6wzBYw1kCbbSHJ57MOyk39EGOqUB%2F4W912qf1R5pPAkbdh6jRPecTiy61WQDMBF8yDOPLpS1coGV4re8b%2BEH%2FniGY4LffCYI%2Belljsc5%2Br5CtikQbc3X8eQXn1F%2FjvBqXIpbcA2lCPPtEiyqZloHvniUygck%2FNezpDzlO3xPVuobpcxNADzRw%2BOTWl%2BTHGaLkZUbrrUP4BRJz6VDws5ExwhI4GUpv%2BcEYxvj%2BCQn%2FT6km7YNzHiBsxsu&X-Amz-Signature=6fc60310fdfbec19d9ec459eabc1d9f0533397dc2af227d2bf3003e8a82367c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







