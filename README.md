



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXGHFIYZ%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T194710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCID9VvmBko5MbEOLuKPGJVoCeZ4aQg9s39r4n5hc6eq7AAiAoRbc2IuhUALqeOtWOInv8zyh8gy4aweLiCPJx9wdgICqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVACQ72W6oRYHoQebKtwDfzjL2VlXmFrqYOeFFzZTYnwldFNoqYrDB0j%2B5cy7Yrx3m44ho1QayHm9PNpFB9oUVzEL6zogbS8F6g4DA621IGuu42FyVFJ9Io2E4xWqzcJntCnsnOiV2D1e535eIQ1TeaYq8KaStovgrPvkYmrbjBj14d8KK93iW8UfugUYG7vLkiNPNLTCxbLb%2BGQD4SjYVm8KkKbrEbwNwlGEd6cCP2hNT3CbHmaTQK03hnHvCisi93d1THwt0LzRLMhtSg2yxbqc5aCLwn80MbCAINd5BguuBGDT16P98xFBYTdBQYlI%2BoqfPk1w3A3TWn7U%2Fr%2BFkHYvZB%2FhhP2JlC9g55%2BaQ44I%2FZnzYMdnhdweStFs7Guu1SqezPKg6FgUMk%2FyQ%2BY2kNqD1Eoxa69U72AAYIpRJOeu8cGoRqMhrg27f9X%2BplQ5crjOv%2F%2BKRVDevURA3c5CgCun%2Fm89iDRrIkCCIoTdbSj%2BX5GxxdSEW4J7O57SiHaI1214qlhaliOvaTu5d3k00psqGcRfOTOLKTWvWXx9nHtsfcOnZLT7GxhyPFyGZc6GqeyZdBkLp5vR58tDg0q%2FnkoFrv49zMUf2zYhASdBIHxjvCOgxavQw0Qm78ZBGX9BNK%2BF%2BmJCw7rpLMQwtNCP0gY6pgFu9nSu4JH0jNaJodf4Qi1MBf7Hxy%2FSblC%2BaLiaS0J0VXxxEO4PwglaVT7IVRVs%2FDcITvGt8DM8aOXd3pl3BmotY%2BEns1540DCfHBovwbqznz%2Fr9s1RwSdSeSdmcN%2FE2D1Ybly3S3gprqcvNny0lQZklrDtfaVTys%2FK7dQNniLt%2FFlFX5ppTHOxmiuQ%2Fd%2Fa9%2BfJ8vg22oj7w%2FUA2pOC4TZ34wiCY5v2&X-Amz-Signature=f2e9293443e3f7797c415f91689a3b21cd1e0a5b16083779d8e67b93e68a2d76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXGHFIYZ%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T194710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCID9VvmBko5MbEOLuKPGJVoCeZ4aQg9s39r4n5hc6eq7AAiAoRbc2IuhUALqeOtWOInv8zyh8gy4aweLiCPJx9wdgICqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVACQ72W6oRYHoQebKtwDfzjL2VlXmFrqYOeFFzZTYnwldFNoqYrDB0j%2B5cy7Yrx3m44ho1QayHm9PNpFB9oUVzEL6zogbS8F6g4DA621IGuu42FyVFJ9Io2E4xWqzcJntCnsnOiV2D1e535eIQ1TeaYq8KaStovgrPvkYmrbjBj14d8KK93iW8UfugUYG7vLkiNPNLTCxbLb%2BGQD4SjYVm8KkKbrEbwNwlGEd6cCP2hNT3CbHmaTQK03hnHvCisi93d1THwt0LzRLMhtSg2yxbqc5aCLwn80MbCAINd5BguuBGDT16P98xFBYTdBQYlI%2BoqfPk1w3A3TWn7U%2Fr%2BFkHYvZB%2FhhP2JlC9g55%2BaQ44I%2FZnzYMdnhdweStFs7Guu1SqezPKg6FgUMk%2FyQ%2BY2kNqD1Eoxa69U72AAYIpRJOeu8cGoRqMhrg27f9X%2BplQ5crjOv%2F%2BKRVDevURA3c5CgCun%2Fm89iDRrIkCCIoTdbSj%2BX5GxxdSEW4J7O57SiHaI1214qlhaliOvaTu5d3k00psqGcRfOTOLKTWvWXx9nHtsfcOnZLT7GxhyPFyGZc6GqeyZdBkLp5vR58tDg0q%2FnkoFrv49zMUf2zYhASdBIHxjvCOgxavQw0Qm78ZBGX9BNK%2BF%2BmJCw7rpLMQwtNCP0gY6pgFu9nSu4JH0jNaJodf4Qi1MBf7Hxy%2FSblC%2BaLiaS0J0VXxxEO4PwglaVT7IVRVs%2FDcITvGt8DM8aOXd3pl3BmotY%2BEns1540DCfHBovwbqznz%2Fr9s1RwSdSeSdmcN%2FE2D1Ybly3S3gprqcvNny0lQZklrDtfaVTys%2FK7dQNniLt%2FFlFX5ppTHOxmiuQ%2Fd%2Fa9%2BfJ8vg22oj7w%2FUA2pOC4TZ34wiCY5v2&X-Amz-Signature=17dd8d217ee164cea072887c87e725840b21d5e45ebeb2b3cb52dd9cbbc840e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







