



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRX7PJWT%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T011318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRn%2FfeuOUfpaV2pdzf1uxxT8YOAU96cCcUZ9jAJ6UszAiBctBqYjp22CgLs%2FH2uyzXhm3SzoOnb%2BNkxR3KqjiV4oir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM4y9gb%2B75YOKznApSKtwDFWsGEaG5G3tR4htGySAGuh8aYf8NzoxKoQT7udD6Gc9o9mXYKtSQCw5DmL%2BPibGBEz762rWUCVYn4Xu0mfmeRk5LkYY3UEhEw2%2BK7sxnl%2FeXwIxrl4BMS767VeJrucM8Xoe7XiheB9WZp6C1bG6ky34DYo%2BRnlVX7e5oVW6lgldEPp3O%2BIXZkkdDbrQPIeWru7Co%2BGKV%2FQhR6v9S5V%2F9yxDhvrIf2vmkeICxKMbLgzErn4kJp6w8vDcghT80cxmt3o1%2FG%2BvfktT0fkfXyp9gioziqFWQk%2BGP8QQ90%2FH6Y37XB3jcw2hKFrZomMQm%2BeZ26gr2P6qoakKSi35GdtuJy9fN2bP5cJ0BDD8QcfinRjboLOnfu8OnYxHnSJc%2Bz4bb7ZKmWIzUEsrP0c52PXvk9Or5Fu0aVapUQko7TsVXTht8YOOI1zj5%2BPg9%2B5sx%2BsP18TtPYVYuLZD3TDD8oXU%2Bxwa1wysgCrRupIWaLwMM2qF2TJYFy%2BjKHPd10WniZ6o7RLQQ4GjofBvbEOYu6OYd187CDsgz8hWNqxKm9DpuREKlpPW0oEqRumsG06OxQFYh1YmUsJV6AptjwraWm5hUkgWJbw3MVBXZ7xbmuNbRLfc6f2bCoXVMfnYeKrYw8typyAY6pgHaFUs3D3oWZF6VGkGjbMzQBpxDNUpgqDaYRYxRi2ihqGT%2FxQMa07w6cBcXjWQofAhuLo637Oe%2F8N%2FonVRRs1NrlP9YmAi3Ej3dfsRdjcC7%2B8H2Fdz9qf3l8JRBrnyRvg3GhSRLg3JpNpUlw1drUIj85bD7q3ESZ3sbm%2BMp9DNm6XEj3gO6%2B1v%2B%2BNMFkzO39u2eVeR8ImCHZ63nI661tqiooJ5%2F%2Fn3N&X-Amz-Signature=75312ec1192981aa8fdfad392e1f9435e3776be06d84ba1bcaf763795968a1dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRX7PJWT%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T011318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRn%2FfeuOUfpaV2pdzf1uxxT8YOAU96cCcUZ9jAJ6UszAiBctBqYjp22CgLs%2FH2uyzXhm3SzoOnb%2BNkxR3KqjiV4oir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM4y9gb%2B75YOKznApSKtwDFWsGEaG5G3tR4htGySAGuh8aYf8NzoxKoQT7udD6Gc9o9mXYKtSQCw5DmL%2BPibGBEz762rWUCVYn4Xu0mfmeRk5LkYY3UEhEw2%2BK7sxnl%2FeXwIxrl4BMS767VeJrucM8Xoe7XiheB9WZp6C1bG6ky34DYo%2BRnlVX7e5oVW6lgldEPp3O%2BIXZkkdDbrQPIeWru7Co%2BGKV%2FQhR6v9S5V%2F9yxDhvrIf2vmkeICxKMbLgzErn4kJp6w8vDcghT80cxmt3o1%2FG%2BvfktT0fkfXyp9gioziqFWQk%2BGP8QQ90%2FH6Y37XB3jcw2hKFrZomMQm%2BeZ26gr2P6qoakKSi35GdtuJy9fN2bP5cJ0BDD8QcfinRjboLOnfu8OnYxHnSJc%2Bz4bb7ZKmWIzUEsrP0c52PXvk9Or5Fu0aVapUQko7TsVXTht8YOOI1zj5%2BPg9%2B5sx%2BsP18TtPYVYuLZD3TDD8oXU%2Bxwa1wysgCrRupIWaLwMM2qF2TJYFy%2BjKHPd10WniZ6o7RLQQ4GjofBvbEOYu6OYd187CDsgz8hWNqxKm9DpuREKlpPW0oEqRumsG06OxQFYh1YmUsJV6AptjwraWm5hUkgWJbw3MVBXZ7xbmuNbRLfc6f2bCoXVMfnYeKrYw8typyAY6pgHaFUs3D3oWZF6VGkGjbMzQBpxDNUpgqDaYRYxRi2ihqGT%2FxQMa07w6cBcXjWQofAhuLo637Oe%2F8N%2FonVRRs1NrlP9YmAi3Ej3dfsRdjcC7%2B8H2Fdz9qf3l8JRBrnyRvg3GhSRLg3JpNpUlw1drUIj85bD7q3ESZ3sbm%2BMp9DNm6XEj3gO6%2B1v%2B%2BNMFkzO39u2eVeR8ImCHZ63nI661tqiooJ5%2F%2Fn3N&X-Amz-Signature=ad6956d631a15aa2d7b99670bf42cfc61236296ba15bf10ff5d5b0e88b81df7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







