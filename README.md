



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMI7SCRO%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T012559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFHBotmBG4GKOJOmQqhMqQJQg2nf35RllVn%2B62N86wGAIgTKEeD8pokWn3cbZrPmYblLD5%2F%2FNzYlpILtgmzmX5YjMqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJRpJhQt8%2Blbzut%2BvyrcAxMDH1E0V1QqRHrzwUtLALNK%2B1FOO2gUqDp5my52VArzsUt%2F1XL5NqiTlAzuMOfeGtV3K1drsTLwK%2FfuiAIkRoTRmC%2FlvCcop1ih6lV%2B%2BlYK%2BTbEvS1QlLpfFDRS2dxHYZ3JzsIUJ1oHBj72yymd888ml8jrgv6jgtaMv077otkkXaieAlNJEx47Gf6EeCDbixE3yMCylcAPuZIOMJrc9ZxxhR%2FTAiObE9hVhzkI04FguAt8AK3%2FPl6ylKp6HgAy5tSLxC6hfDrYkfz01IU082sk9v0BYJq0Yndhm6K2T0sR86Y2Z8zKHOGqxOvfGBVstYEhGwbfv%2BIMc82EwObI%2Fp8sTYl1A5pdoXYyWgSrewK%2B1XonMeDoxl7wMdd7%2BhKATUykKPw2AjHdgIz3OObUjyUq7EFGmeElRO%2F8YFwj3bnbXiFaZsDdFiPFEsiIo%2F80MS4lqX90Y0TEj1LhDXkeYVd60ludp8hz7KHsEQpgSTcjjb02B1fH7kILTKXBZ0gwyfwCNWOC4kQOum3b5GDO8iRUm28kH3os5aNuXhe5UnlgWhXMmvfxHJhOddTzzcugvNbtZDvihE3xV1oNqyLEOctlZJOf64eUw2TDuImT8J5kjQQL0%2B0QeS4YsZ0iMPXdissGOqUB51czF0C%2FOWHJwWUbcZFWOiCOlzL5bA7CObuEenW0AZvElFmotd5GTSOuY0aO6djimuTxv1zur7jhcdkuKpZEmlnS0%2FgC17ciXa5rDlH%2BoEXRle6G6l4D504qJR7%2BoH5wQO4bFtm8p77nqzP5e16KEMa4F42NTVPK3TI5aJycRG%2BGAHS5y5WCAFL4T8npXtjegKRsWmskx1C2W76Ps3TrKwA3wfcT&X-Amz-Signature=a70c9426c8939f6dbaa04a9037e1d69e343ad73ff9dbabe6890da1662c567da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMI7SCRO%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T012559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFHBotmBG4GKOJOmQqhMqQJQg2nf35RllVn%2B62N86wGAIgTKEeD8pokWn3cbZrPmYblLD5%2F%2FNzYlpILtgmzmX5YjMqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJRpJhQt8%2Blbzut%2BvyrcAxMDH1E0V1QqRHrzwUtLALNK%2B1FOO2gUqDp5my52VArzsUt%2F1XL5NqiTlAzuMOfeGtV3K1drsTLwK%2FfuiAIkRoTRmC%2FlvCcop1ih6lV%2B%2BlYK%2BTbEvS1QlLpfFDRS2dxHYZ3JzsIUJ1oHBj72yymd888ml8jrgv6jgtaMv077otkkXaieAlNJEx47Gf6EeCDbixE3yMCylcAPuZIOMJrc9ZxxhR%2FTAiObE9hVhzkI04FguAt8AK3%2FPl6ylKp6HgAy5tSLxC6hfDrYkfz01IU082sk9v0BYJq0Yndhm6K2T0sR86Y2Z8zKHOGqxOvfGBVstYEhGwbfv%2BIMc82EwObI%2Fp8sTYl1A5pdoXYyWgSrewK%2B1XonMeDoxl7wMdd7%2BhKATUykKPw2AjHdgIz3OObUjyUq7EFGmeElRO%2F8YFwj3bnbXiFaZsDdFiPFEsiIo%2F80MS4lqX90Y0TEj1LhDXkeYVd60ludp8hz7KHsEQpgSTcjjb02B1fH7kILTKXBZ0gwyfwCNWOC4kQOum3b5GDO8iRUm28kH3os5aNuXhe5UnlgWhXMmvfxHJhOddTzzcugvNbtZDvihE3xV1oNqyLEOctlZJOf64eUw2TDuImT8J5kjQQL0%2B0QeS4YsZ0iMPXdissGOqUB51czF0C%2FOWHJwWUbcZFWOiCOlzL5bA7CObuEenW0AZvElFmotd5GTSOuY0aO6djimuTxv1zur7jhcdkuKpZEmlnS0%2FgC17ciXa5rDlH%2BoEXRle6G6l4D504qJR7%2BoH5wQO4bFtm8p77nqzP5e16KEMa4F42NTVPK3TI5aJycRG%2BGAHS5y5WCAFL4T8npXtjegKRsWmskx1C2W76Ps3TrKwA3wfcT&X-Amz-Signature=052a16e6e81fc543b00c936a4a06f0f3ad7eebc84d768f037bc2a169306b49d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







