



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMKXRF4%2F20251103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251103T123252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH5629xkLlkzZd4TKDAX8ArIZI7ir2q2txuimkCOfl%2BfAiEAiBDkOIU3oAHSb2C211Ulxydjusp8WN7w4FFC1qgu5zwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDH2pozhijahRoSMSCircA0xuUfqY9fyGwW4ahePN9Ur9CwEJM3iV55HUHFVtFgpO3yYxC1uJECQr2h2OwSsfwKmSpRW0H5uHZOqKm%2Fe%2Fk4sR1vBwhndh4NJUyLfRsRbBtywWsKrMWILFVP1FnegHvoQ3Cn0SRMm77O413%2FxqfpyNLZeNONmySiEIrwBz7MAhVokV73OgFe9%2BD0zOXhkpoibthgnxDfsr7qv%2BQmVoU8QJQKpUKJjpa6ZEy19XseeI6rGwMsbU0Bh%2Bv8fuQbqynw0uksp01yu%2BpPOqAKkylpFofuChmuO32XNev8tCuEH8Op%2BFxasX8BwXl3UungT5yK%2BuMZgdQ7vu3D4gYt0akSoyqR19eg6Ojpk8XHFH%2FBpD1tW1S1qK9CKSk2lxaNcB36fMZQXRVRv8RdE%2FLfF5fMWV0Ab9%2BksQRN3Jz07rGz3UOfKIdM0n6h%2FxBq2iK9dPB3Fm6Wi9HcrFJmeLtLxJHOzuZzkpKo8tzs9uu4NoFo1dNkbhE%2Bxd791BgaEiL4rzLhVzLPGIUUucDL6bcrwSYD56%2BTVXtQ%2FkPnwXJ7CU%2Bm1U51wXmQaSZK2SzKR8OYRcKlmscUuCbSu0EVP94j%2BCvI3qgp%2FT6rMt85FpMD1%2Fs7dHMnB3jm5evJRIro6LMNm3osgGOqUBAR2xTsxlZ%2BZMruSvNZCmWVsZ6wQmWxB7e8CX3Q64RJaokQ3aY51ocxqPyvC9jegBiJqiLxzZOORHBgGyxWUxIF33eIsjW22X9W7WxvN7RNK2UzihH8lDMgWKoh%2BbqiCd9bQE9uEgIyT1h9aARZMStr1K44Gy1Mo9SbK%2FYyJ%2B%2BQkxaymWIGJbXBuJyxMRLJSKcc0rt%2BSrMRSNM49srajCcqnBEzHV&X-Amz-Signature=c4fe7526bf0b4a2b90ce1d526050b8ed27c7484dfdf473631a64145e2adbcd69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWMKXRF4%2F20251103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251103T123252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH5629xkLlkzZd4TKDAX8ArIZI7ir2q2txuimkCOfl%2BfAiEAiBDkOIU3oAHSb2C211Ulxydjusp8WN7w4FFC1qgu5zwq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDH2pozhijahRoSMSCircA0xuUfqY9fyGwW4ahePN9Ur9CwEJM3iV55HUHFVtFgpO3yYxC1uJECQr2h2OwSsfwKmSpRW0H5uHZOqKm%2Fe%2Fk4sR1vBwhndh4NJUyLfRsRbBtywWsKrMWILFVP1FnegHvoQ3Cn0SRMm77O413%2FxqfpyNLZeNONmySiEIrwBz7MAhVokV73OgFe9%2BD0zOXhkpoibthgnxDfsr7qv%2BQmVoU8QJQKpUKJjpa6ZEy19XseeI6rGwMsbU0Bh%2Bv8fuQbqynw0uksp01yu%2BpPOqAKkylpFofuChmuO32XNev8tCuEH8Op%2BFxasX8BwXl3UungT5yK%2BuMZgdQ7vu3D4gYt0akSoyqR19eg6Ojpk8XHFH%2FBpD1tW1S1qK9CKSk2lxaNcB36fMZQXRVRv8RdE%2FLfF5fMWV0Ab9%2BksQRN3Jz07rGz3UOfKIdM0n6h%2FxBq2iK9dPB3Fm6Wi9HcrFJmeLtLxJHOzuZzkpKo8tzs9uu4NoFo1dNkbhE%2Bxd791BgaEiL4rzLhVzLPGIUUucDL6bcrwSYD56%2BTVXtQ%2FkPnwXJ7CU%2Bm1U51wXmQaSZK2SzKR8OYRcKlmscUuCbSu0EVP94j%2BCvI3qgp%2FT6rMt85FpMD1%2Fs7dHMnB3jm5evJRIro6LMNm3osgGOqUBAR2xTsxlZ%2BZMruSvNZCmWVsZ6wQmWxB7e8CX3Q64RJaokQ3aY51ocxqPyvC9jegBiJqiLxzZOORHBgGyxWUxIF33eIsjW22X9W7WxvN7RNK2UzihH8lDMgWKoh%2BbqiCd9bQE9uEgIyT1h9aARZMStr1K44Gy1Mo9SbK%2FYyJ%2B%2BQkxaymWIGJbXBuJyxMRLJSKcc0rt%2BSrMRSNM49srajCcqnBEzHV&X-Amz-Signature=d089eae80c4f6078b18295a7806efd715df14c69dddbe5b918e0461fbec8ac51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







