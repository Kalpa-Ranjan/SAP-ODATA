



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIZUZBBV%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T182400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDHT47JESrYS5QtVtQ4fYJcdExhwstcSXr00HzlvIjevQIhAJGzQnrLItMRc%2Foc1DZBI%2ByYBGR2wFL9XX6YH0B7l0xYKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMo2PGI5nd0ORj39Uq3APzKO1aMa750zgO%2BKc22oVpI2V4qbTAmVfqTSp1riM1ZNSM5Mq%2F2yP4YGbOz4Zs9RFOFFO%2BNZMfNVUSi9lXcdTz4CarNkuYmdsKy7Rkangj0XpxUXiO7QBtmMMpF3bOTDgiSy67ZBSShX9x9naFaysRDwxHaXSIo1KwhGZTG6WORxz5Vp3jDU0a3n3NGooZKduJe8ua15xEkn1WCnLcGR3Qs7qiwymadyHcocTfu%2BHdOOFz7usdQO7GkD1wqATkBjuDPwZvTehPKtUApU32jutxqiBblKUVls37I3tdGX%2FejcMXAuXpSbH1AAALAlpa8jjIIlGdxynRxpPelrK220q4PLgLmEOSPGKk6%2BdB27x3LOLtAj%2FgHp85f2sST26lwrkXxl7M7gpOLJ2r8JL65B3beNo0MdS8idfmQmG44nAg2kG0WByAWESxv8CEHqKjBu4Tm5koxeamv4AOa4FyPigrcaMCYxwtwZolsDMu2CdY2M89x8%2Fc0NMFc8sZvF3kAIvps1Q2NxskZGXuApULtHxSCYeu4AcuybjRjcRSiB6bTDPLBFJ2FlMwNgp3M71ysxry%2BMTHqu3P9M%2BfhhYdEzkFSFNrvmithw5ZztbBNsZv4IpwUhMTbLfGq1bgqDCR9tnKBjqkAce10vy0E2Ev6ntAqBe2yB04j5IZrpRXUsFEgnxNy2h%2FtjULqACbzwc%2BOYkuB52850iPgcBgGwlqC9Y3W5WhUf1Vu05NOgda920DwBuK2NtU0NS4uBuXJe%2FuKeDdyZbrOpMnL%2B%2BVKZbH6K%2F8CX0lbJ4wYxhzCovSOL8EW96E5y8BFRHPOVrhCCtnGLxbbF58ImrUZUQUbfiqTls1c1sNoaS22bcr&X-Amz-Signature=f66f6c52b29acce148e81e0dc11e808d8b268649b945bb1e4027c6546a4716bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIZUZBBV%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T182400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDHT47JESrYS5QtVtQ4fYJcdExhwstcSXr00HzlvIjevQIhAJGzQnrLItMRc%2Foc1DZBI%2ByYBGR2wFL9XX6YH0B7l0xYKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMo2PGI5nd0ORj39Uq3APzKO1aMa750zgO%2BKc22oVpI2V4qbTAmVfqTSp1riM1ZNSM5Mq%2F2yP4YGbOz4Zs9RFOFFO%2BNZMfNVUSi9lXcdTz4CarNkuYmdsKy7Rkangj0XpxUXiO7QBtmMMpF3bOTDgiSy67ZBSShX9x9naFaysRDwxHaXSIo1KwhGZTG6WORxz5Vp3jDU0a3n3NGooZKduJe8ua15xEkn1WCnLcGR3Qs7qiwymadyHcocTfu%2BHdOOFz7usdQO7GkD1wqATkBjuDPwZvTehPKtUApU32jutxqiBblKUVls37I3tdGX%2FejcMXAuXpSbH1AAALAlpa8jjIIlGdxynRxpPelrK220q4PLgLmEOSPGKk6%2BdB27x3LOLtAj%2FgHp85f2sST26lwrkXxl7M7gpOLJ2r8JL65B3beNo0MdS8idfmQmG44nAg2kG0WByAWESxv8CEHqKjBu4Tm5koxeamv4AOa4FyPigrcaMCYxwtwZolsDMu2CdY2M89x8%2Fc0NMFc8sZvF3kAIvps1Q2NxskZGXuApULtHxSCYeu4AcuybjRjcRSiB6bTDPLBFJ2FlMwNgp3M71ysxry%2BMTHqu3P9M%2BfhhYdEzkFSFNrvmithw5ZztbBNsZv4IpwUhMTbLfGq1bgqDCR9tnKBjqkAce10vy0E2Ev6ntAqBe2yB04j5IZrpRXUsFEgnxNy2h%2FtjULqACbzwc%2BOYkuB52850iPgcBgGwlqC9Y3W5WhUf1Vu05NOgda920DwBuK2NtU0NS4uBuXJe%2FuKeDdyZbrOpMnL%2B%2BVKZbH6K%2F8CX0lbJ4wYxhzCovSOL8EW96E5y8BFRHPOVrhCCtnGLxbbF58ImrUZUQUbfiqTls1c1sNoaS22bcr&X-Amz-Signature=5031c7a943b4d892fe52655ff822ff43d529c6d0f8de47ad4e170484da7b565d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







