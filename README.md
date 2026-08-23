



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDLH53ZV%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T005930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIBMtMOjPf8yh5L2HxUMHqyhnjuiPXCRJtruKWxeXdk9eAiB1CLe3ZKSVQB2C5jVXdUWmlTgN5u8N3yDdoWyBNpBZOCqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxkHegxUCPMviMunbKtwDqpsRKa1NJi3Nc9Xy6xujAFGNNWJmp3%2Bkd%2FUVpvdWDhh6RzHSOZqK%2BD6HVqMoUrIpDaY5klexS8Bo8P%2BlyeBM4oFY0BDMWlFolbzGy0v5OIyjwn0SF7mKsARm%2BNmcpyiRFKlA3X4H78HLPBaSe1Td%2BTgmzD1oSbWe%2FeBAFhAmA%2BeqxR9AILswEc0heKxyOQUJH48TCiZ564gfuBvaFOhAXiZc%2FZ6kKHwzH09Am9InQLeDu6%2F2RQGsRYRC3r1UbrKLdP0Lbbl1ZTq43g97Xovvoazd6EjYjdmaCxs1cK94AczwID3w7mUPaY%2Bou80T8AnAPe3xj5vN4hqY0CgTdVmB8pEzd0kHAOyGudgIkBv0qqG%2BPZTGuMxgyyuIIrKRt%2FMJkmHvIQzHadGZstUG7i%2B4Yq9OuZp9XGlsssZBYYdmh7ti1uyWtazF5NtzO8%2BKtse2S%2BUNms%2Ftx2mFNAqidmYN890NdHhsVSGjnJSxO%2BclUUXoA61TdMU7isJoXS57U7SLWjtCe9m%2B6XUqpeAogO3Sd4Zx%2BRu5hMwuWBpJG5%2Bpry%2F88k65ZQyh3BaIn%2B9kHAEAV3tNaj07D43SBLhnxXC0IPidUPYQ3aZwha6pFY2esPbVBBJ9xhhwBdFMAYUwsIWp1AY6pgHsQ2wWvEUH8nSl8E2JYOtYizzqCSJWQyY16%2BTy8ba7CZNIaI9tUuHnkYJwUS5yz%2BEzksze%2F0gFMbvVOTaUY5l6YdSlKrxbTc8Vp8ECZnQv2fNx7xk9v%2Ft5L44CknF4WjFCP9wYqIShmNI%2Fa0dXFeuCLbc1uBoXV8juHJiOEilM%2FkNaTLxEu9vESbYTC3jycjT2tfzhTZ8XUwqPOoGvEPrVp2BBG4hG&X-Amz-Signature=5577dfcb48e4013cacbd0228fd2a281f22795a1251f413078038156c26f4829e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDLH53ZV%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T005931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIBMtMOjPf8yh5L2HxUMHqyhnjuiPXCRJtruKWxeXdk9eAiB1CLe3ZKSVQB2C5jVXdUWmlTgN5u8N3yDdoWyBNpBZOCqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxkHegxUCPMviMunbKtwDqpsRKa1NJi3Nc9Xy6xujAFGNNWJmp3%2Bkd%2FUVpvdWDhh6RzHSOZqK%2BD6HVqMoUrIpDaY5klexS8Bo8P%2BlyeBM4oFY0BDMWlFolbzGy0v5OIyjwn0SF7mKsARm%2BNmcpyiRFKlA3X4H78HLPBaSe1Td%2BTgmzD1oSbWe%2FeBAFhAmA%2BeqxR9AILswEc0heKxyOQUJH48TCiZ564gfuBvaFOhAXiZc%2FZ6kKHwzH09Am9InQLeDu6%2F2RQGsRYRC3r1UbrKLdP0Lbbl1ZTq43g97Xovvoazd6EjYjdmaCxs1cK94AczwID3w7mUPaY%2Bou80T8AnAPe3xj5vN4hqY0CgTdVmB8pEzd0kHAOyGudgIkBv0qqG%2BPZTGuMxgyyuIIrKRt%2FMJkmHvIQzHadGZstUG7i%2B4Yq9OuZp9XGlsssZBYYdmh7ti1uyWtazF5NtzO8%2BKtse2S%2BUNms%2Ftx2mFNAqidmYN890NdHhsVSGjnJSxO%2BclUUXoA61TdMU7isJoXS57U7SLWjtCe9m%2B6XUqpeAogO3Sd4Zx%2BRu5hMwuWBpJG5%2Bpry%2F88k65ZQyh3BaIn%2B9kHAEAV3tNaj07D43SBLhnxXC0IPidUPYQ3aZwha6pFY2esPbVBBJ9xhhwBdFMAYUwsIWp1AY6pgHsQ2wWvEUH8nSl8E2JYOtYizzqCSJWQyY16%2BTy8ba7CZNIaI9tUuHnkYJwUS5yz%2BEzksze%2F0gFMbvVOTaUY5l6YdSlKrxbTc8Vp8ECZnQv2fNx7xk9v%2Ft5L44CknF4WjFCP9wYqIShmNI%2Fa0dXFeuCLbc1uBoXV8juHJiOEilM%2FkNaTLxEu9vESbYTC3jycjT2tfzhTZ8XUwqPOoGvEPrVp2BBG4hG&X-Amz-Signature=9660d44e1864fd07e82b8179caa78c86087233c796bac8ec1814c7699ede1214&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







