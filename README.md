



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ5WKPM3%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T064528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDIVf%2B2pGVF1FG2rZ2llAIJgGtWqN8gFx7dPkqhSMs5bwIgKsL4LZu6QQbpe4qKntOL0sIyABDIIOisboTZRhUu%2B%2Bkq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDP069JeUTa%2B9YVjP%2ByrcA1MzDNLhiK0LOAuBWiKUPgXZmJaLoL6xRD0Ro0RewRjjU1yRlpJHFAP%2FAncPre59fdCe238l%2B5Kb0S7Bv5Feu9b7istDdyzAuHTXF4p2%2B1FOaqO%2BpO%2Bn60PhCLhw0rcOffieUaTjJsY1DTzAMkhg%2FodEyNHVjUDBc%2Bu5RMRiRCoYg25l%2FJ1OPYVZqiG4sWN398bF0mzwgFA3UIoil5DXIx97T%2BrbdyfV5SqL5ZYh%2BomNV7GC7vWZI5%2FXwp%2FYHJOXw5Z8hzaLtAny9HOuY8Ly%2FEKZTZaKVl3UZHg%2BV762597Q77O3DHY6ntjGKikaTIflX3uFSj7MZkY%2Ff6d8%2BQ%2BuwpTOltKjENmvh%2BnL9C2zkJ%2BwFTbTume9n%2FLuSkuO5jiMJxThsRgG1zj1Sj7u53Mp2ijFkVAOYGvGyuHpj9XVqjIxPHNdzuwu8JIluhl8qBZMXEIHO5Q0N604PPR5U1Vk3Ild59F9Hyzn0vRPivQvNpMBhQSUlEzWiH1BsUIJK6WUbppl2eZDL8fTodIcNBfWn8cjhjcc7BbOhhJsdLtaz6gAFKPeyy3uwaLsRfuOdx4z%2ByxiSVaqkAFlc11iCtcljEdlW5ZL4ytFERO3Ik2uXiAlEzkQLs77u6heDC8ZMJ3VhM0GOqUBIFlU3SiDTo79kbtGzaPbEauKBCEdF1PNlchJQT7QWmsUaVhOpNgefIn9nibU5X2DXQJtQwN8SNW5f1H70wgKf0MYTEgHUhgWBe2IYvjgGq0hjnWdPHLi7N%2FAgl%2FqUO04jY1VYbfxQ4bQDm9JvrFC4IGV6HN7YN9Ap3Q9vorD49L0tnWnfqXCFeh5luL4tW5f%2FYnGtAGbrhQ650gOHFo7We%2FEfgK%2B&X-Amz-Signature=ac071cff9b8a8e8818ec1f469bda2378c5ddb6a07b84f7518006cdb92cfc2b20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ5WKPM3%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T064528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDIVf%2B2pGVF1FG2rZ2llAIJgGtWqN8gFx7dPkqhSMs5bwIgKsL4LZu6QQbpe4qKntOL0sIyABDIIOisboTZRhUu%2B%2Bkq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDP069JeUTa%2B9YVjP%2ByrcA1MzDNLhiK0LOAuBWiKUPgXZmJaLoL6xRD0Ro0RewRjjU1yRlpJHFAP%2FAncPre59fdCe238l%2B5Kb0S7Bv5Feu9b7istDdyzAuHTXF4p2%2B1FOaqO%2BpO%2Bn60PhCLhw0rcOffieUaTjJsY1DTzAMkhg%2FodEyNHVjUDBc%2Bu5RMRiRCoYg25l%2FJ1OPYVZqiG4sWN398bF0mzwgFA3UIoil5DXIx97T%2BrbdyfV5SqL5ZYh%2BomNV7GC7vWZI5%2FXwp%2FYHJOXw5Z8hzaLtAny9HOuY8Ly%2FEKZTZaKVl3UZHg%2BV762597Q77O3DHY6ntjGKikaTIflX3uFSj7MZkY%2Ff6d8%2BQ%2BuwpTOltKjENmvh%2BnL9C2zkJ%2BwFTbTume9n%2FLuSkuO5jiMJxThsRgG1zj1Sj7u53Mp2ijFkVAOYGvGyuHpj9XVqjIxPHNdzuwu8JIluhl8qBZMXEIHO5Q0N604PPR5U1Vk3Ild59F9Hyzn0vRPivQvNpMBhQSUlEzWiH1BsUIJK6WUbppl2eZDL8fTodIcNBfWn8cjhjcc7BbOhhJsdLtaz6gAFKPeyy3uwaLsRfuOdx4z%2ByxiSVaqkAFlc11iCtcljEdlW5ZL4ytFERO3Ik2uXiAlEzkQLs77u6heDC8ZMJ3VhM0GOqUBIFlU3SiDTo79kbtGzaPbEauKBCEdF1PNlchJQT7QWmsUaVhOpNgefIn9nibU5X2DXQJtQwN8SNW5f1H70wgKf0MYTEgHUhgWBe2IYvjgGq0hjnWdPHLi7N%2FAgl%2FqUO04jY1VYbfxQ4bQDm9JvrFC4IGV6HN7YN9Ap3Q9vorD49L0tnWnfqXCFeh5luL4tW5f%2FYnGtAGbrhQ650gOHFo7We%2FEfgK%2B&X-Amz-Signature=b53cac63e3777d380de8c8f034ed72193ebbbfb660ea09c00e91a3a2ec739cdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







