



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUH2XHE%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T062311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFi1du26QldoBE1ODY3DAii3vd5oUOSZzImNzN1A540zAiA7A58qZld6tzYz4mptjieHkGkBcWGZhV0hgclyyUUSeiqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpk%2BGHaTeHtGayzdxKtwDqXddfdCge2cAwVbpMfpos2lR5xoXBPtUVpsjgt01sA46lB8NqEDY9HxMUxD%2FdlyEjLaUgz6JqBWqhzb%2FL0C7MG4GXhmF4pXCw7GQb%2B%2BY0JMgNyO%2F05J%2Fq8k8BjJlWJ%2BSrwMt%2F%2BacFh7BcsyQjQ%2BGKPfQgmy1D9yoLdpCozqb3sDqlhSy1%2BK9bnB125abv3tjfO9y4MH5axYIqftjFBUNtOeS10iAiHnZjTSL26oZOuPtMd%2F2pNVIUIEqVkxsVsf95ls%2BvVxouZvTEZBio4aYK8Z%2Bye9rJL2ohnTx4HmHh5vnSgGoVa4xAGB%2Ff34eJxXuxDgCcTotWOOQBdqmtyNnA7%2BxYhgz%2FQfkrl6vOtINR2swjKVcODqMwB73wlvAyCTB6UkLYd1yu6kSqrejoct8teIWESlv1A47n3eml%2F0J3o03stGEqy36VthO%2BJLWBhuzKFjBpocmziHvvb9icb1YzE1ccJrfnvi4S%2Ft2XGYw89kgglxrWX82FcMtHRKFyoO5NOaIrXkflEvt7YQixAVTzp12n%2FtyosFbFvUyqpvetxT1eHOdY1%2F6q5H1uItx1maOfDtTg%2Fryiyr24B%2Bn5v%2FBFEOiTbF%2FwjOiDfIODHfAFj3wmT8OfPIOEYFP%2F%2FAwwpyvyQY6pgF2cUkxHKfrAbibGgqSdLqqtaQeRIaKkhMWo%2BRgKghr7LWTleQRxVJQw2XMimmqpRHLzY2zRlSr6myM5pmIKA%2BR336eSqWt1tyehQAlbPrVLZQL6t1K75y2CEUrl%2FW4SFazdyOUxeCKPfnytk240Pxjs7aQsKZamd49w7QyU%2FtBO8LpK5SF7qlqeuStrg30u%2B6Xf5hps2SM%2BREtiGXLJ6BS%2BZgaQNZJ&X-Amz-Signature=a39e75043b4816e8297898afbb31b68251436ce9a4407f5a31a91ae2734e8363&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNUH2XHE%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T062311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFi1du26QldoBE1ODY3DAii3vd5oUOSZzImNzN1A540zAiA7A58qZld6tzYz4mptjieHkGkBcWGZhV0hgclyyUUSeiqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpk%2BGHaTeHtGayzdxKtwDqXddfdCge2cAwVbpMfpos2lR5xoXBPtUVpsjgt01sA46lB8NqEDY9HxMUxD%2FdlyEjLaUgz6JqBWqhzb%2FL0C7MG4GXhmF4pXCw7GQb%2B%2BY0JMgNyO%2F05J%2Fq8k8BjJlWJ%2BSrwMt%2F%2BacFh7BcsyQjQ%2BGKPfQgmy1D9yoLdpCozqb3sDqlhSy1%2BK9bnB125abv3tjfO9y4MH5axYIqftjFBUNtOeS10iAiHnZjTSL26oZOuPtMd%2F2pNVIUIEqVkxsVsf95ls%2BvVxouZvTEZBio4aYK8Z%2Bye9rJL2ohnTx4HmHh5vnSgGoVa4xAGB%2Ff34eJxXuxDgCcTotWOOQBdqmtyNnA7%2BxYhgz%2FQfkrl6vOtINR2swjKVcODqMwB73wlvAyCTB6UkLYd1yu6kSqrejoct8teIWESlv1A47n3eml%2F0J3o03stGEqy36VthO%2BJLWBhuzKFjBpocmziHvvb9icb1YzE1ccJrfnvi4S%2Ft2XGYw89kgglxrWX82FcMtHRKFyoO5NOaIrXkflEvt7YQixAVTzp12n%2FtyosFbFvUyqpvetxT1eHOdY1%2F6q5H1uItx1maOfDtTg%2Fryiyr24B%2Bn5v%2FBFEOiTbF%2FwjOiDfIODHfAFj3wmT8OfPIOEYFP%2F%2FAwwpyvyQY6pgF2cUkxHKfrAbibGgqSdLqqtaQeRIaKkhMWo%2BRgKghr7LWTleQRxVJQw2XMimmqpRHLzY2zRlSr6myM5pmIKA%2BR336eSqWt1tyehQAlbPrVLZQL6t1K75y2CEUrl%2FW4SFazdyOUxeCKPfnytk240Pxjs7aQsKZamd49w7QyU%2FtBO8LpK5SF7qlqeuStrg30u%2B6Xf5hps2SM%2BREtiGXLJ6BS%2BZgaQNZJ&X-Amz-Signature=fba9f67a1ecec2bf4497e0bfbe2f2b3ac386381ae6ba36f83000b75d95957a70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







