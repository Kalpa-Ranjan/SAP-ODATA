



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJSAJH4V%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T123718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC7x%2BlIGDr7lAGSZeX6pupDkd0%2Bfdpf59PVcIwsQfswqwIgF16vmVo76WYej0Xe8iUwskfchW49bhnr93xhXMsDQYYq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDHyqsiTWu4so%2BWVP3yrcA%2FhAKfWrHxe3KdaRaTpgcPqhdsf5hGiMBn%2Fz04bS6etlBrNRbNvVnu4SNqJrYqYOVOFFY5fmA9u0e1RMZuO2h3dHX1M%2FDkmn3pvyNDV8mF0%2FrVgbQoL13TOCSPbFuFfCK%2FfEb85WmdhRVTkvqL4omUNMBlvOruv4X6a1xluQgoZoBO4CBhLXJw%2BhCqP7b3TPsE316dTxGebMCOpvqln25qhW%2F7WX8eNTeW75QryBKBroM%2FjWtyO13FVUoZEXjobK59%2BLXHww%2BmlHUENIY9U2xbRVXNOC8QG22OOUb%2FCa2oItLOA3nvZy1o%2BojxeEyqzsuDMSTm4yfZ4kxtn6yr%2F9f90jfBt1hjcHNr3vztK2oAc1Xy42uE6BOq6N2eR%2F%2Fc7M%2F5zQ3O5ZAAFnkCdhrNhujqrWSan01Z0uu4tAe38vBtGPOMTw%2BNbaIYBVeaOyTXbpeHd4%2B4y%2BMvK2leMRXGP7pCzJmQheuV%2BoOcl%2FNDxpr%2B7OIM1FIsDZOzwpgISkhPMCPoMtCqgwW%2FR98bZzMboG73%2Bjo2MWJk7QAlI6A32KSjQBniiNJg3MVR3d%2FcVJhlNMpfXeTi91JDhlOA6G%2FhBHfw6BbxuTOmrtaXUi3daBFGPQomlhuW9RMZIZHLIPMJvmmMsGOqUBuLM%2FKLbCV3mmqDOEt73R7Q9eDFhTIJpArX6Gn8dv6TayBbArklckQj6wPs%2BTAQ5wq7Le%2Blbo0UYuQKOr4vWViAFqIFhDAAN2JKtulGgyHF9heyYm82kG1lJerp%2BS%2FSh%2Baa0tpLZhN676lisWiQvGHKqsKFSUzo1XDXnTLFTn2GIFelnMty1hRwvQCdvjg8CjDQ3wN9ZkqPd%2FstDMVpCTTlzRlWVi&X-Amz-Signature=ae871ef6d504fac8983ec3654c7e70279ca39a12e628b46370d3980e69373161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJSAJH4V%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T123718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC7x%2BlIGDr7lAGSZeX6pupDkd0%2Bfdpf59PVcIwsQfswqwIgF16vmVo76WYej0Xe8iUwskfchW49bhnr93xhXMsDQYYq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDHyqsiTWu4so%2BWVP3yrcA%2FhAKfWrHxe3KdaRaTpgcPqhdsf5hGiMBn%2Fz04bS6etlBrNRbNvVnu4SNqJrYqYOVOFFY5fmA9u0e1RMZuO2h3dHX1M%2FDkmn3pvyNDV8mF0%2FrVgbQoL13TOCSPbFuFfCK%2FfEb85WmdhRVTkvqL4omUNMBlvOruv4X6a1xluQgoZoBO4CBhLXJw%2BhCqP7b3TPsE316dTxGebMCOpvqln25qhW%2F7WX8eNTeW75QryBKBroM%2FjWtyO13FVUoZEXjobK59%2BLXHww%2BmlHUENIY9U2xbRVXNOC8QG22OOUb%2FCa2oItLOA3nvZy1o%2BojxeEyqzsuDMSTm4yfZ4kxtn6yr%2F9f90jfBt1hjcHNr3vztK2oAc1Xy42uE6BOq6N2eR%2F%2Fc7M%2F5zQ3O5ZAAFnkCdhrNhujqrWSan01Z0uu4tAe38vBtGPOMTw%2BNbaIYBVeaOyTXbpeHd4%2B4y%2BMvK2leMRXGP7pCzJmQheuV%2BoOcl%2FNDxpr%2B7OIM1FIsDZOzwpgISkhPMCPoMtCqgwW%2FR98bZzMboG73%2Bjo2MWJk7QAlI6A32KSjQBniiNJg3MVR3d%2FcVJhlNMpfXeTi91JDhlOA6G%2FhBHfw6BbxuTOmrtaXUi3daBFGPQomlhuW9RMZIZHLIPMJvmmMsGOqUBuLM%2FKLbCV3mmqDOEt73R7Q9eDFhTIJpArX6Gn8dv6TayBbArklckQj6wPs%2BTAQ5wq7Le%2Blbo0UYuQKOr4vWViAFqIFhDAAN2JKtulGgyHF9heyYm82kG1lJerp%2BS%2FSh%2Baa0tpLZhN676lisWiQvGHKqsKFSUzo1XDXnTLFTn2GIFelnMty1hRwvQCdvjg8CjDQ3wN9ZkqPd%2FstDMVpCTTlzRlWVi&X-Amz-Signature=3c5cb2ee2904eb2a7d32c26920ff45a13afd02f8926b2fb9f3030f8b143f744c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







