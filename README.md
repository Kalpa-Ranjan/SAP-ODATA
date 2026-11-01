



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7S75BIT%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T120602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FSZzLNFfP5sAU02qC0vypO4SulmK5%2FL2s8c87D5%2FOVgIgXbyvRGedgL3NTVMvbCzJxGOioK82zCuAmogNLjGsKjIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDPu35c0Pvm7bG8FXgircAxpe4VHEX%2Flm2z1iSpns8gwmiBy3zYb0w2egQPnHJNmxvgYg90j%2B2Jq9LCf6%2BIeB%2F7Fm0FMkXlSBVtQqlPWr4kkquArmEDLWzq13odUNAbgmhTR5qywk63pDELpNBNdotgFXzfS6Aat4sq5en9Ao3qjzvwvqn82pUkZk9I4Vb6l41olfZnj207gt0DQvzOJgUZJ9wGw6ZEZ6w85FtL4fC%2Bi7LHp1P0aiw1we92QFtw3NUJpgAEYXXOMtBIV8%2B187NV1phys9TvMwcFKtKlRF0Eh%2FeoazYY%2BXl0ouMeeQKsY28JsES4ykYbmdM%2BPLxvx5ppFjShVxpWPv%2BdHIt4QBDiIQWIkGPp%2BMlStVkG70DxxLCcRRWdaKt3EIEg2ydWCBz83BHB5ehtqPhTHvZNQYzRxvxiBE4MuzDA63ejMsRwL2Ocle1ESG6VAbxHrpEJqmHQ9R5mY%2BbkqhmEhYUMqhZTNuEEbRLwpdCtI2JwYsnhhTDnim%2ByZHyUlIx%2Bp6guMu2vQV%2BKBLQmzAJnsPJ9wvK1foOyZpe6cM0o8%2Br76eue9oWH%2F%2FEJ%2F4MdsCd%2FQL5rPj24uJbCWsqF5pumJ7ZaaW1%2Fh4q1WP7wutDCD8PQmjkGHLcAUB1ipKvRPYSPakMMaTnNcGOqUB4TET2wwfOw9x5wHTsBrF48gl0OqMt%2BMaLclegVaLJGt6ueaU5v4AQZToeWS3XSmf%2FpTEC635%2Bp4sfoG9k5cYcKKc4kaK3pbcExVzrWtMGOFIuaUrI2n86lLgtV546MkJYl35BglavtaIVi2Dp%2Fa7uLLUkCVqPNRjIbZ88JFauJY9HMiPN7Ebgu8MPyaNJAP1Gp0e0f1Vcl6zQDSuAMLzqR%2FMa%2FHL&X-Amz-Signature=989fc0387733e6e4f91ca8146df72fd7b53ad417c79fca7d4f5af0be8bbf0f0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7S75BIT%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T120602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FSZzLNFfP5sAU02qC0vypO4SulmK5%2FL2s8c87D5%2FOVgIgXbyvRGedgL3NTVMvbCzJxGOioK82zCuAmogNLjGsKjIq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDPu35c0Pvm7bG8FXgircAxpe4VHEX%2Flm2z1iSpns8gwmiBy3zYb0w2egQPnHJNmxvgYg90j%2B2Jq9LCf6%2BIeB%2F7Fm0FMkXlSBVtQqlPWr4kkquArmEDLWzq13odUNAbgmhTR5qywk63pDELpNBNdotgFXzfS6Aat4sq5en9Ao3qjzvwvqn82pUkZk9I4Vb6l41olfZnj207gt0DQvzOJgUZJ9wGw6ZEZ6w85FtL4fC%2Bi7LHp1P0aiw1we92QFtw3NUJpgAEYXXOMtBIV8%2B187NV1phys9TvMwcFKtKlRF0Eh%2FeoazYY%2BXl0ouMeeQKsY28JsES4ykYbmdM%2BPLxvx5ppFjShVxpWPv%2BdHIt4QBDiIQWIkGPp%2BMlStVkG70DxxLCcRRWdaKt3EIEg2ydWCBz83BHB5ehtqPhTHvZNQYzRxvxiBE4MuzDA63ejMsRwL2Ocle1ESG6VAbxHrpEJqmHQ9R5mY%2BbkqhmEhYUMqhZTNuEEbRLwpdCtI2JwYsnhhTDnim%2ByZHyUlIx%2Bp6guMu2vQV%2BKBLQmzAJnsPJ9wvK1foOyZpe6cM0o8%2Br76eue9oWH%2F%2FEJ%2F4MdsCd%2FQL5rPj24uJbCWsqF5pumJ7ZaaW1%2Fh4q1WP7wutDCD8PQmjkGHLcAUB1ipKvRPYSPakMMaTnNcGOqUB4TET2wwfOw9x5wHTsBrF48gl0OqMt%2BMaLclegVaLJGt6ueaU5v4AQZToeWS3XSmf%2FpTEC635%2Bp4sfoG9k5cYcKKc4kaK3pbcExVzrWtMGOFIuaUrI2n86lLgtV546MkJYl35BglavtaIVi2Dp%2Fa7uLLUkCVqPNRjIbZ88JFauJY9HMiPN7Ebgu8MPyaNJAP1Gp0e0f1Vcl6zQDSuAMLzqR%2FMa%2FHL&X-Amz-Signature=3a67d00a3fd07525c17722d9672ae5538e3d9853a65533d7a7f5e7522d38e21c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







