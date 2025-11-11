



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JE3C4RF%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T062412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIQDbHHUQIFYR2H6cRnsne8KOuu3dNc0qJwKHNAAzApBWawIgU3hrUVsSTHyJYE9RGvIoFsYCo2dXfUlzbkKafirObO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFrSAwqOR6w3k7URZircA0Tsoo077zghP%2FA1fwH%2F2l6nmVEQugRwlUsj0hAIDF%2Bdm4zs%2BHzLKapCakwMM1UzJDT67FNXMc9DZ%2BEwylK8fMcx5yBAfxxb6YYcN%2FQajA%2BEitysRhFYn%2BIun6RP6XUdPawYGuc8k08OfV1DUnJ%2FheqwEbQ7b%2FeMeiumYt5LTmJpAh6Uo%2BYhQMyTsZEPYw5xjBIkugNCRkzWJx9CJylU8neGGX%2BIPZQpLLj9Ts5eY3SBuMhGiCjnTqJKejdv8Mv8Glm2Qov9J%2BqEqKiRkGBA5tEBtxXmQz2xirLQT%2BPQowJ7%2BYRu%2BGinDVQklIJ2QahGBsmOb97yC6M1OG7Mbm9jNs9V9vEFWlcXD0e0O%2FMRBZM8Nr8DNWU%2FeO4vO1mhGHtfkyGQh%2FCH3nvjDipH6kCZ7NVQSAOi8wEBrvTv8RmJFXmGhy7Z90bDZGXopKLQ7Ydpt7uuN6UuoMw225YY44aIlA7AlRzBhj0Y2YX3UuZ3JqZOfXRm%2BwkRsNRyST8oeuRGs7yVKm5E9Dmh%2Byl10ZxUTCLCXF%2FTxgF1I0X95fpx0JDqqyZCSw0ij0kfbiV%2BAOkz9tjxSohHhOihHKhQPG4k%2FsOfjImKupNZ5SQ%2B9h3%2FDDj4cTZ8tYzHVwMQ57xXMISay8gGOqUBlPU8l9OJ9S77QTmJIePJRJ1qaQcUBos5pLtadxX5aA%2BkD8msFODnqrwmRs%2FlQL%2F2gzh4MUne5YeX%2FDP5UxK6SresUNcP1FExGGGjOOTCbqco3qRYi%2BS4Qvi8Ok38dXIPAGkEPY74m2J5nf7ZNSNsWJUUnpDcCkU%2B9gQvA4zAkKnt3UlLhxmkzrPZmQu2sr7s1aceWJEEyVP1eiWezn2uiM%2BGDvnR&X-Amz-Signature=e908f3912ffae0eeb9f06a1b2b51ac040b50c295f7c18cf9f40111def4931f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JE3C4RF%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T062412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIQDbHHUQIFYR2H6cRnsne8KOuu3dNc0qJwKHNAAzApBWawIgU3hrUVsSTHyJYE9RGvIoFsYCo2dXfUlzbkKafirObO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFrSAwqOR6w3k7URZircA0Tsoo077zghP%2FA1fwH%2F2l6nmVEQugRwlUsj0hAIDF%2Bdm4zs%2BHzLKapCakwMM1UzJDT67FNXMc9DZ%2BEwylK8fMcx5yBAfxxb6YYcN%2FQajA%2BEitysRhFYn%2BIun6RP6XUdPawYGuc8k08OfV1DUnJ%2FheqwEbQ7b%2FeMeiumYt5LTmJpAh6Uo%2BYhQMyTsZEPYw5xjBIkugNCRkzWJx9CJylU8neGGX%2BIPZQpLLj9Ts5eY3SBuMhGiCjnTqJKejdv8Mv8Glm2Qov9J%2BqEqKiRkGBA5tEBtxXmQz2xirLQT%2BPQowJ7%2BYRu%2BGinDVQklIJ2QahGBsmOb97yC6M1OG7Mbm9jNs9V9vEFWlcXD0e0O%2FMRBZM8Nr8DNWU%2FeO4vO1mhGHtfkyGQh%2FCH3nvjDipH6kCZ7NVQSAOi8wEBrvTv8RmJFXmGhy7Z90bDZGXopKLQ7Ydpt7uuN6UuoMw225YY44aIlA7AlRzBhj0Y2YX3UuZ3JqZOfXRm%2BwkRsNRyST8oeuRGs7yVKm5E9Dmh%2Byl10ZxUTCLCXF%2FTxgF1I0X95fpx0JDqqyZCSw0ij0kfbiV%2BAOkz9tjxSohHhOihHKhQPG4k%2FsOfjImKupNZ5SQ%2B9h3%2FDDj4cTZ8tYzHVwMQ57xXMISay8gGOqUBlPU8l9OJ9S77QTmJIePJRJ1qaQcUBos5pLtadxX5aA%2BkD8msFODnqrwmRs%2FlQL%2F2gzh4MUne5YeX%2FDP5UxK6SresUNcP1FExGGGjOOTCbqco3qRYi%2BS4Qvi8Ok38dXIPAGkEPY74m2J5nf7ZNSNsWJUUnpDcCkU%2B9gQvA4zAkKnt3UlLhxmkzrPZmQu2sr7s1aceWJEEyVP1eiWezn2uiM%2BGDvnR&X-Amz-Signature=790944f6d62c918c9a6590ea540170e22bb67d3918589f974ad91b2b85c10122&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







