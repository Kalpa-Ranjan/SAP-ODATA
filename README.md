



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVNF32EE%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T121114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIH4fKtC1e2%2F5kzDQzwgV5dH0%2BWU20pHpTKQd%2FeCfgGM9AiEAij3ImE47k7tCFtijx8WlxP1XsLvhRv8OBVQ8Grk6Mgoq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDGvviWm4aLQrRpnpbCrcA4JFRJtdsMfTYMvBFjKk4tMxvNev9fb8yR7cIRw%2FCWf%2FeWXsdP25UpOEYP80o9oKbNBvB11W2Pfbyov%2BI9jC46OT8k9A%2FoU0HRbtCwge3rKrbidfaKhQEN1vVXIrd%2Fe6tsnCNGM3%2FKOA3GqRUyyNdFxYiIdmLd56dfJ9xjLIzXNols7oQ3myar1XD0tXMNyFuiyWbMAR4UAoUvPczA7CYoTZvQ3idgTPub7dm4nfv510714mMJW%2FKenfrpSwLiAG2Nlft64vB3PDo5PH%2BpJoYJuE1g2zCHlnw45DD62KUbhb4Sk6hP2CEIdqYTjKXosrSxiZsh%2FthbiDaUufiXHe%2F7KKCfKFiVVHbAu6ZBUrMpqcZcwIAmo8aAx0Pl0NFtzZ8HFXhN07zdWF8M55Keb9d1nVwD%2Bt2aK0ra3DeLfM3ZuNLr5ing3tZEldIt2Sj1ScVEwhYUjiJtjWaa0smTLFXuWFeeaQvGTTofxpiOFJEt2hsYqUq0aUFozGUDBXoUCQ2uy%2FNi51YuGfw6zWdzt1oq%2BiRRkh8QqlkGh4iaBF9T77BLmPw49LlihD%2Fdkud015U0kBgCFvt06vtQRKMB3zGPUpS%2F8PM99uxgYU212TihGGi%2FkEIRvjeVHToAIyMJyi3dYGOqUB%2FLV%2FUVOA%2F8fJTx%2FpRAq6hkOm3U2LyoHy54U2tRviCEe%2FXWDixagPmhUV3bUDzHhGthEXMwtagWGohRJzL%2BiiZrj76DuAMZdMpqFuf7gjuCeaFJ1ihU7rYr%2BkibuVXYhguBG94pV8EeslQFBggrAABo5WfsuOB9QSg4KnO1Wltp%2BFdy3HawnA61MIr4CEdq5ZfMzJAZGxbSmuZso4cYm80Q%2FJr6iw&X-Amz-Signature=b5fc3bc158283b3837b2058233297e22d9a6de08cf71c8d2bafd47e72f7ba724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVNF32EE%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T121114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIH4fKtC1e2%2F5kzDQzwgV5dH0%2BWU20pHpTKQd%2FeCfgGM9AiEAij3ImE47k7tCFtijx8WlxP1XsLvhRv8OBVQ8Grk6Mgoq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDGvviWm4aLQrRpnpbCrcA4JFRJtdsMfTYMvBFjKk4tMxvNev9fb8yR7cIRw%2FCWf%2FeWXsdP25UpOEYP80o9oKbNBvB11W2Pfbyov%2BI9jC46OT8k9A%2FoU0HRbtCwge3rKrbidfaKhQEN1vVXIrd%2Fe6tsnCNGM3%2FKOA3GqRUyyNdFxYiIdmLd56dfJ9xjLIzXNols7oQ3myar1XD0tXMNyFuiyWbMAR4UAoUvPczA7CYoTZvQ3idgTPub7dm4nfv510714mMJW%2FKenfrpSwLiAG2Nlft64vB3PDo5PH%2BpJoYJuE1g2zCHlnw45DD62KUbhb4Sk6hP2CEIdqYTjKXosrSxiZsh%2FthbiDaUufiXHe%2F7KKCfKFiVVHbAu6ZBUrMpqcZcwIAmo8aAx0Pl0NFtzZ8HFXhN07zdWF8M55Keb9d1nVwD%2Bt2aK0ra3DeLfM3ZuNLr5ing3tZEldIt2Sj1ScVEwhYUjiJtjWaa0smTLFXuWFeeaQvGTTofxpiOFJEt2hsYqUq0aUFozGUDBXoUCQ2uy%2FNi51YuGfw6zWdzt1oq%2BiRRkh8QqlkGh4iaBF9T77BLmPw49LlihD%2Fdkud015U0kBgCFvt06vtQRKMB3zGPUpS%2F8PM99uxgYU212TihGGi%2FkEIRvjeVHToAIyMJyi3dYGOqUB%2FLV%2FUVOA%2F8fJTx%2FpRAq6hkOm3U2LyoHy54U2tRviCEe%2FXWDixagPmhUV3bUDzHhGthEXMwtagWGohRJzL%2BiiZrj76DuAMZdMpqFuf7gjuCeaFJ1ihU7rYr%2BkibuVXYhguBG94pV8EeslQFBggrAABo5WfsuOB9QSg4KnO1Wltp%2BFdy3HawnA61MIr4CEdq5ZfMzJAZGxbSmuZso4cYm80Q%2FJr6iw&X-Amz-Signature=285cdc47338a807fc1bd551b18dd585f7a05b8753fe5f47879084e2ad18a3a14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







