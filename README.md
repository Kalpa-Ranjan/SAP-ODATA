



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XBKVG6S%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T012652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCtYq4HwDlJRdwk3KleLMTtm%2BLHtVzvVOzA7708sK56aAIgDLLhuDYxh7A%2BytjaM5Z8HQ61BM1KVTWUUTOIsqvzbJcq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKV3FXGTf5KnVAgfwSrcAwdfRrC1V4gsSwO1loefbQDv5QIs1VIF3eY8D3oajKwZWQH8yiq0SucxiLkQ9phcDFGnYyUzNLXrIvtcqt3yOtCgCbvhhvXZhIOX5QXBrzJkXuZ7bPb8kXvb6DgM4NHsvvEpaYMWJCgUxajwTs8rnB9bzEoYUndwegawNLaZTjb1cyFgXjcLDZkHbV67UlQ%2B6%2FLGy3KUKG5%2FVqOj16%2B%2FS81OPJs6ydTR%2FxCLDdN7OqcN9SUO7%2FDUYXmfd%2FlpvoOZxZrhf0wG4sgrWUDikVX%2FSEjGUwpzTI0Hl%2BVVzVhTY37nicDfaJQYWFxG%2FQIlkWvHJqGNAls25WumiTkEQIh%2BB%2FTDkPTg1lEFi3VCqKBhyVuioF5ljG1nmStAs%2BQisiDyf3yar3mvbgT7w8AOJw%2BuFnv%2BRTYlWa22HepfbCFp%2BzNg%2B4gCM3pnUAXpL4ldiv86AM0pGzyHXoTy2Y9KWugn4CzY8bhCGNcRDTPQ0pS6NeqmGEszVN7MZaIeG0rAQgsgT8YDZU6TOwIuUyGfaKCmj4s6GmYfG8zQ1xNMltFD5HVWdrSKcdrSS%2F%2Bj%2B1l4pQgtLhPpLWG53nMik9W4aRfzj6ConrHCiHqhqs%2BYlS2q5biqlrOElxUB9WjJrwAMMJzO1csGOqUBg6H9PAO40o%2FjMs5%2BN2peok0hSnyuzv7wgGIzGeaR0vEOyZcpTEQvfO%2FXtIgZMqalxRxJYslmmQw36hksIyIOu0CtARnK90oTOcUCJPoP%2FB4aW8paUUNrq%2B267EqlkRPLmazM79tHL8V85nQgCibMNqSoQsef%2FoHDW8YT7zMS%2FRs%2F1A2zFM3cz255l725fzynCPNYiVXO%2BUwHSpB0Xx7jESUd%2FBIP&X-Amz-Signature=647d101f3158a02c0864f7cf12b755570d35b4caab8dd6a69e22a9f0b270d706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XBKVG6S%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T012652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCtYq4HwDlJRdwk3KleLMTtm%2BLHtVzvVOzA7708sK56aAIgDLLhuDYxh7A%2BytjaM5Z8HQ61BM1KVTWUUTOIsqvzbJcq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKV3FXGTf5KnVAgfwSrcAwdfRrC1V4gsSwO1loefbQDv5QIs1VIF3eY8D3oajKwZWQH8yiq0SucxiLkQ9phcDFGnYyUzNLXrIvtcqt3yOtCgCbvhhvXZhIOX5QXBrzJkXuZ7bPb8kXvb6DgM4NHsvvEpaYMWJCgUxajwTs8rnB9bzEoYUndwegawNLaZTjb1cyFgXjcLDZkHbV67UlQ%2B6%2FLGy3KUKG5%2FVqOj16%2B%2FS81OPJs6ydTR%2FxCLDdN7OqcN9SUO7%2FDUYXmfd%2FlpvoOZxZrhf0wG4sgrWUDikVX%2FSEjGUwpzTI0Hl%2BVVzVhTY37nicDfaJQYWFxG%2FQIlkWvHJqGNAls25WumiTkEQIh%2BB%2FTDkPTg1lEFi3VCqKBhyVuioF5ljG1nmStAs%2BQisiDyf3yar3mvbgT7w8AOJw%2BuFnv%2BRTYlWa22HepfbCFp%2BzNg%2B4gCM3pnUAXpL4ldiv86AM0pGzyHXoTy2Y9KWugn4CzY8bhCGNcRDTPQ0pS6NeqmGEszVN7MZaIeG0rAQgsgT8YDZU6TOwIuUyGfaKCmj4s6GmYfG8zQ1xNMltFD5HVWdrSKcdrSS%2F%2Bj%2B1l4pQgtLhPpLWG53nMik9W4aRfzj6ConrHCiHqhqs%2BYlS2q5biqlrOElxUB9WjJrwAMMJzO1csGOqUBg6H9PAO40o%2FjMs5%2BN2peok0hSnyuzv7wgGIzGeaR0vEOyZcpTEQvfO%2FXtIgZMqalxRxJYslmmQw36hksIyIOu0CtARnK90oTOcUCJPoP%2FB4aW8paUUNrq%2B267EqlkRPLmazM79tHL8V85nQgCibMNqSoQsef%2FoHDW8YT7zMS%2FRs%2F1A2zFM3cz255l725fzynCPNYiVXO%2BUwHSpB0Xx7jESUd%2FBIP&X-Amz-Signature=5fe1a30a886e92c6b2f45f302ec56182af629a5ddc944ddb50fd567b615693e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







