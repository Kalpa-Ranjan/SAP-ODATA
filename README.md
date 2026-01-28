



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH7WSCM%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T012039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7an%2FMROuCKdrq6%2BQoFzs3tzSFCx8F9xLLoi%2F54V%2BZYAiEAlh1KPTD8yrWFwltBhCZqtHnU%2BClkXKAGaeINqTJHyCIq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDCkFZEoX7Br8xy4y5SrcA19h6gR9%2FQAD%2Bxr3d6DbwU%2BTVdHjJu0R6mgzRY%2Fl5sTgfgC6keKTCcWIhamhFJhjaziE3QjSnW1n%2Bgch3w4WcEkA%2FK76enLRprGj2UvED7Xamz3uJj8lfAF%2BK7xZ%2BXdu33MwUdsqWk2Ke5PL0V1ue4WoCaCKJPPSt23r90Sw2yw9RYPTv7CYi0A%2F4%2FLbQr9ftppjbQbdBeIKDZ8xTNvzoTv4Sp%2BnbB811HcCtGEEVqoSVdTpmjJG%2FBHWK3FVKOA%2FHL3A8jEAjQ5CTeMMfHRDXS4%2BU100GLQYZHZ4ceulbYbRXN1K10Zx1JllWh4bTyr6Y1dfoUhEcYTiQz5a6JS69HtOQoRa9BzMRfH3x8AVBZFnjlkBiH43Vbk5vb1BoCiVu0ceIHyN8SRJEQCfv4fYukl%2Fkg%2BTgllc5k8oLZJuLMwJMqc4ksUZdAJKcgSGrmPW076z945fddIhzExzjOiIapqISjAOmAwm7%2BDUt2UDMLEVWcQFnZQIQj4jjOC%2FTzC67CqVJt202q2cYF6%2BS%2B5oEcui9v8pblBA7bFpyheQJzzLNLFxcu0wWu16Abs3eltqXyo4kUAo76F7cmVQbo8LX%2BK%2FventYrMIrzTptPF3x3Wwvj%2BxYGAqTyTFw%2BFAMIOW5csGOqUBrOGWRtU5Ajg17YmEtHxpKwXgjRNQloGpH6pMgG6C0JymuEzO%2F5y5S%2BuCkmc5tt0L%2FXYLaIA4g6X5gXWuE2dVG9uUn4rqfO9XROYAQvrAivQ9h5BLVfLAyhdwPxcFqutMrMwS8s4Cl3lWRMKCjYO%2FLCCdMVuhvAFE%2FKxRprAWK5W%2Bm%2FPaiaWbnLIr4XIBoQBu5GpIxvS7qnNNtfHdOUSOogVtix4d&X-Amz-Signature=ce3d382acf198736f1753e0ca0a1ab36cac1217a1eb92bf45a71d24a38b74c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH7WSCM%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T012040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7an%2FMROuCKdrq6%2BQoFzs3tzSFCx8F9xLLoi%2F54V%2BZYAiEAlh1KPTD8yrWFwltBhCZqtHnU%2BClkXKAGaeINqTJHyCIq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDCkFZEoX7Br8xy4y5SrcA19h6gR9%2FQAD%2Bxr3d6DbwU%2BTVdHjJu0R6mgzRY%2Fl5sTgfgC6keKTCcWIhamhFJhjaziE3QjSnW1n%2Bgch3w4WcEkA%2FK76enLRprGj2UvED7Xamz3uJj8lfAF%2BK7xZ%2BXdu33MwUdsqWk2Ke5PL0V1ue4WoCaCKJPPSt23r90Sw2yw9RYPTv7CYi0A%2F4%2FLbQr9ftppjbQbdBeIKDZ8xTNvzoTv4Sp%2BnbB811HcCtGEEVqoSVdTpmjJG%2FBHWK3FVKOA%2FHL3A8jEAjQ5CTeMMfHRDXS4%2BU100GLQYZHZ4ceulbYbRXN1K10Zx1JllWh4bTyr6Y1dfoUhEcYTiQz5a6JS69HtOQoRa9BzMRfH3x8AVBZFnjlkBiH43Vbk5vb1BoCiVu0ceIHyN8SRJEQCfv4fYukl%2Fkg%2BTgllc5k8oLZJuLMwJMqc4ksUZdAJKcgSGrmPW076z945fddIhzExzjOiIapqISjAOmAwm7%2BDUt2UDMLEVWcQFnZQIQj4jjOC%2FTzC67CqVJt202q2cYF6%2BS%2B5oEcui9v8pblBA7bFpyheQJzzLNLFxcu0wWu16Abs3eltqXyo4kUAo76F7cmVQbo8LX%2BK%2FventYrMIrzTptPF3x3Wwvj%2BxYGAqTyTFw%2BFAMIOW5csGOqUBrOGWRtU5Ajg17YmEtHxpKwXgjRNQloGpH6pMgG6C0JymuEzO%2F5y5S%2BuCkmc5tt0L%2FXYLaIA4g6X5gXWuE2dVG9uUn4rqfO9XROYAQvrAivQ9h5BLVfLAyhdwPxcFqutMrMwS8s4Cl3lWRMKCjYO%2FLCCdMVuhvAFE%2FKxRprAWK5W%2Bm%2FPaiaWbnLIr4XIBoQBu5GpIxvS7qnNNtfHdOUSOogVtix4d&X-Amz-Signature=94d57c278b05548997c3a376e17e011a12b5e984ab24a923308f43e9b355be4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







