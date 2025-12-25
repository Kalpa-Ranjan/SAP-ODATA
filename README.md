



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMIRKLD3%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T182301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIC%2FpxTwLFKdO4mx6WR5Pml6f2VeYCCuz601br0c9yJoUAiEA3YPnKy2P7FxbHam7IILgYhM53Ge1Qq1oV0BUz93R2%2BIq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBsYyKiZ8N%2B%2BNtftYSrcA%2FQtu7TT45AfZjpWXLuup5eufQJqUnfv7dJO48yGB0L8krmOqgNmjGXg%2BW6%2FAJnHO6cSz3uBaQNUzTC0OgMcde%2BkfXsC2%2F70cTT%2Fho11M0u8UwvG6Xw2wRgnmcNqXc5wOI%2Fkejm5e17KA%2BHhLMOE%2F9Kh9ZrQffEhKEl1LS5ymky2fR5vN3%2Fo9bqogqLPFJhirfAskSWDhHcV6EusJKwVyJ5Eh%2BsS%2BBLGukt%2FTes7bzrSlPyvgGQhTGQoLhpC8u%2FJzsT51WPdYVgO2VnMBuM%2BqIv%2FgiMZ5fyXoMoWI48A8MmpEw96oCFZU7SJLNofyvyMPNLEP4BKxRMl8oz9uYaondOVsiow%2Bdd9Wn3cIiy4mZfAb0j63HqVRUhtpk5rw7xKKU3Wa66MuA73So34odIs4tdfUTLIt0u9dbPYQPECC1e79UbJInyHcTxticY8DZubMeJGLpoLAmw6x7xbB06CcZardvH4Z9RyWJLxm863DnrttIQOk2t2tCwb6QQYPIxqG7Ucw11aR%2BmMut1rc%2Fx5ok0n1zqAM5o3ARtHpZJNiEWi8Xcr39dpcHmCVkHp3HZYV4dlqslLQ%2F0jxHggulbD5q8hvNRmOrj7HGyhERrW4s9yc4H7gZQXQW0yFUcUMI6OtcoGOqUB99QcARYDImXlGsDc0eE56a8URxKUBX5iVTegXXMKhL%2BfhuFbTvrz3HHn5TvCZY3LIAB1KsUSC4YMqZ6icOubvERRGm3Kfb3luuR9lYCiYCbfeM9mh%2BijPTi%2FWpwiPO89v6cqr3jkBHJ1ESQwv9EUmWPmqfxjdoMj%2BG34SkIrrS6JKZdCbLwW3T1GLV0W1iFjUczlAjka6qOWOR07g6Qe26ovoOES&X-Amz-Signature=f522baacd90edcf539d98c1cd2cc50532d83636bbce863291b9c6bed43fe25d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMIRKLD3%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T182301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIC%2FpxTwLFKdO4mx6WR5Pml6f2VeYCCuz601br0c9yJoUAiEA3YPnKy2P7FxbHam7IILgYhM53Ge1Qq1oV0BUz93R2%2BIq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBsYyKiZ8N%2B%2BNtftYSrcA%2FQtu7TT45AfZjpWXLuup5eufQJqUnfv7dJO48yGB0L8krmOqgNmjGXg%2BW6%2FAJnHO6cSz3uBaQNUzTC0OgMcde%2BkfXsC2%2F70cTT%2Fho11M0u8UwvG6Xw2wRgnmcNqXc5wOI%2Fkejm5e17KA%2BHhLMOE%2F9Kh9ZrQffEhKEl1LS5ymky2fR5vN3%2Fo9bqogqLPFJhirfAskSWDhHcV6EusJKwVyJ5Eh%2BsS%2BBLGukt%2FTes7bzrSlPyvgGQhTGQoLhpC8u%2FJzsT51WPdYVgO2VnMBuM%2BqIv%2FgiMZ5fyXoMoWI48A8MmpEw96oCFZU7SJLNofyvyMPNLEP4BKxRMl8oz9uYaondOVsiow%2Bdd9Wn3cIiy4mZfAb0j63HqVRUhtpk5rw7xKKU3Wa66MuA73So34odIs4tdfUTLIt0u9dbPYQPECC1e79UbJInyHcTxticY8DZubMeJGLpoLAmw6x7xbB06CcZardvH4Z9RyWJLxm863DnrttIQOk2t2tCwb6QQYPIxqG7Ucw11aR%2BmMut1rc%2Fx5ok0n1zqAM5o3ARtHpZJNiEWi8Xcr39dpcHmCVkHp3HZYV4dlqslLQ%2F0jxHggulbD5q8hvNRmOrj7HGyhERrW4s9yc4H7gZQXQW0yFUcUMI6OtcoGOqUB99QcARYDImXlGsDc0eE56a8URxKUBX5iVTegXXMKhL%2BfhuFbTvrz3HHn5TvCZY3LIAB1KsUSC4YMqZ6icOubvERRGm3Kfb3luuR9lYCiYCbfeM9mh%2BijPTi%2FWpwiPO89v6cqr3jkBHJ1ESQwv9EUmWPmqfxjdoMj%2BG34SkIrrS6JKZdCbLwW3T1GLV0W1iFjUczlAjka6qOWOR07g6Qe26ovoOES&X-Amz-Signature=83a34de32f76f1c4abd134946b2fbe2f2f7da45cb46f44dc377ec81a4c59e91d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







