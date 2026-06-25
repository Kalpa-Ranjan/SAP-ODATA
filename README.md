



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTDVYBLG%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDtEr2mWAzHvQ0Dj4WmiJxcvNLo1%2FzyyEHsM1goYnDu%2BwIgGNBumvt29lShSD3EbVwapiAJOOtXrOCOfX5MhLSwzx4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDESORJZF74zawL0LkSrcAwhRpk0eoJdLwWorsLqlkYvcT0d1hvT4DDpfYVghtEu81BzQMgB9etezeg7KNWo8T%2B37IQ8cOsd9PGIKzksB84qi8vVyFyzarCngMkkAcADynTHO2SekYJvQXyDtL5Ut37UL6d5owEJIRZY%2Bitzee5RoGszNbluQxmnNbxPvahBR3BhyIhM5IQSXmYduEzJRUhjEkZuJc912lVib6EVW3sRHqH5PnatEyVVOSnkvFyJldHD3anF4Ns%2F9DzMQKHV54Sx6WWV7nRMYxSPFsd9Qluu0WOzNeyvzUbnBtiwJLD6%2FSzePYIZ5u6co62m5BuwUqzB%2FjtVDdbHxp9hbwJ5dAfRUmnC2ZsNFdS0v4SKgRjAkySjNzz7ol%2FBgS%2BhTgVbvvCqLrnoqCCWZ3vDhG5uhK2N%2FeweBsKA%2FGdakuZqX7jf7YVG0i1bBuLcAJJZmkA16oJWNHsYOeVBfj9YauC4FrDa1DAtrIQWalVF123RyPnrZdq0mzhKuLSorchuvuryFmOmWu5aJ%2FSbbzWN0kY1d5n6Wyk8y2lJRWwBa4a9HmpHDKxo6R4QsgiAlicr%2BS2u9wwoDhbBBIgU29uEtUFu7RoXoE3tVT%2FmPhHU8uhZ41%2BkHM2246IRCywRhBCWWMP2q8tEGOqUBekzK8fqtJ6g2iafsifn8LGIn3HC3kpuvm689IBLZkmNDsu7ZaE5eGl3EqEFqUR5w6H78wgG%2BM%2BXHolv1pQb0gfZ8Br3GiCkpr8AjT2cGdjk1iXDSbxOxeGUc2HIRsgybwY1VHNJrAzPVxPRVabqTD4FM9Zyl41Hg2isdwcB4g8TPmTCjQw8%2FleRrieV3eA5mdTs3mPT1ZpWKAWNK8BIlPX6DXlsx&X-Amz-Signature=5f683323dc3801cd585fe4cf986e2344b2c90ae94224ee1895c4fe122a18ed62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTDVYBLG%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDtEr2mWAzHvQ0Dj4WmiJxcvNLo1%2FzyyEHsM1goYnDu%2BwIgGNBumvt29lShSD3EbVwapiAJOOtXrOCOfX5MhLSwzx4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDESORJZF74zawL0LkSrcAwhRpk0eoJdLwWorsLqlkYvcT0d1hvT4DDpfYVghtEu81BzQMgB9etezeg7KNWo8T%2B37IQ8cOsd9PGIKzksB84qi8vVyFyzarCngMkkAcADynTHO2SekYJvQXyDtL5Ut37UL6d5owEJIRZY%2Bitzee5RoGszNbluQxmnNbxPvahBR3BhyIhM5IQSXmYduEzJRUhjEkZuJc912lVib6EVW3sRHqH5PnatEyVVOSnkvFyJldHD3anF4Ns%2F9DzMQKHV54Sx6WWV7nRMYxSPFsd9Qluu0WOzNeyvzUbnBtiwJLD6%2FSzePYIZ5u6co62m5BuwUqzB%2FjtVDdbHxp9hbwJ5dAfRUmnC2ZsNFdS0v4SKgRjAkySjNzz7ol%2FBgS%2BhTgVbvvCqLrnoqCCWZ3vDhG5uhK2N%2FeweBsKA%2FGdakuZqX7jf7YVG0i1bBuLcAJJZmkA16oJWNHsYOeVBfj9YauC4FrDa1DAtrIQWalVF123RyPnrZdq0mzhKuLSorchuvuryFmOmWu5aJ%2FSbbzWN0kY1d5n6Wyk8y2lJRWwBa4a9HmpHDKxo6R4QsgiAlicr%2BS2u9wwoDhbBBIgU29uEtUFu7RoXoE3tVT%2FmPhHU8uhZ41%2BkHM2246IRCywRhBCWWMP2q8tEGOqUBekzK8fqtJ6g2iafsifn8LGIn3HC3kpuvm689IBLZkmNDsu7ZaE5eGl3EqEFqUR5w6H78wgG%2BM%2BXHolv1pQb0gfZ8Br3GiCkpr8AjT2cGdjk1iXDSbxOxeGUc2HIRsgybwY1VHNJrAzPVxPRVabqTD4FM9Zyl41Hg2isdwcB4g8TPmTCjQw8%2FleRrieV3eA5mdTs3mPT1ZpWKAWNK8BIlPX6DXlsx&X-Amz-Signature=31b5adfda2be4527f6c8173a9317d89fe69425ee804064a20e1cab8b013c2e5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







