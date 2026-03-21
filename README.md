



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V4BPGCS%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T063645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIGwZQW6Ww1Q%2BM7UkM4x3WCpFtrZ4KzLpKv%2FdJgHch85JAiEA209Q1Bh6slMKApjDxhGOSrY5shOfwZqMKUhsSws3Y3sq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDOLhIdERnlm9fffGBCrcA6yEFyrBD533UzPdF8A%2FinutFmA6f9N9oOBogW91iOVp3bGUAg8in6WCN7iZI4pP8792zw6e40baAvyp%2F0cgxrGliv9Mk8lJDEPvKLNQA2DHtz%2Boy9sqaPKMNl6G35%2BbPDzhAzQ%2BTdPJS2zmEROUWC%2F4%2F%2Bf%2F8zt0pxg55qDfJl6uodbSYeqoQewcnuicAPa29IAukV2hUokYk1M7gxQiQHvxOOStZXaxd04jL%2B478QQFlzODyXOfD6kjnB73ER8cfENMu%2Bmo%2Foru6oYNoP7Gn6An6iuyKUE7vROeSVzH3PqQXzaYCgKleu19uqZ%2Bq%2BPxC52MLDQqW3zWE6a99kk0y4c7Jq1joF2O3qJXekC9e1ZmSLRhm7qDuYLcvKcA9wAMnXWkGWhupLN8xpLqz8hhtJSvoIiG4jWUOmnWp2iKhu3euqH7FczKv%2BfAQW1Nmt%2FJg0RajuqkoZkdo%2FSLH4qdRIrJUngZOJJd%2FxBRtwmzlcXTtIVm1n1hlmEyOthuR%2Ff7s9LDUCRW3TS4q6rX6nTcBudTatIq2ZQPCQ1q4UyKNonHeLL79iEdppzAjK1wNlMdyXFEs74%2BC7jKWt6MfJOzOo%2BI%2BSb7O7L0Cs15GzWG1V8OLWIJEJeTdemH6mdBMNnm%2BM0GOqUBpCwy%2BOjJsdtsOOR%2FAGeUNc79S%2BISRn5e6tAS74l3dvY2hHvR0%2FMLaRPh6Hfydvc863tDW3evjCwH9jf%2F3QHEzZAl0zp9YgJtJtOw9Kux4QWqX5Yp2bpqqrHeRPY0CP0IDfjvazy1%2F8kJumTtAmOjT3dNW%2FGKc4BepRDxMTUMi0SvBkjLUtsbB2WkHMzpIGItnC0RdOEIjcyMHPY7C%2B0ZqLNwxviS&X-Amz-Signature=cd355bc5e063d58c364a16acbe803590c43ee542c6421f0e321ab47694d92d3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V4BPGCS%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T063645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIGwZQW6Ww1Q%2BM7UkM4x3WCpFtrZ4KzLpKv%2FdJgHch85JAiEA209Q1Bh6slMKApjDxhGOSrY5shOfwZqMKUhsSws3Y3sq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDOLhIdERnlm9fffGBCrcA6yEFyrBD533UzPdF8A%2FinutFmA6f9N9oOBogW91iOVp3bGUAg8in6WCN7iZI4pP8792zw6e40baAvyp%2F0cgxrGliv9Mk8lJDEPvKLNQA2DHtz%2Boy9sqaPKMNl6G35%2BbPDzhAzQ%2BTdPJS2zmEROUWC%2F4%2F%2Bf%2F8zt0pxg55qDfJl6uodbSYeqoQewcnuicAPa29IAukV2hUokYk1M7gxQiQHvxOOStZXaxd04jL%2B478QQFlzODyXOfD6kjnB73ER8cfENMu%2Bmo%2Foru6oYNoP7Gn6An6iuyKUE7vROeSVzH3PqQXzaYCgKleu19uqZ%2Bq%2BPxC52MLDQqW3zWE6a99kk0y4c7Jq1joF2O3qJXekC9e1ZmSLRhm7qDuYLcvKcA9wAMnXWkGWhupLN8xpLqz8hhtJSvoIiG4jWUOmnWp2iKhu3euqH7FczKv%2BfAQW1Nmt%2FJg0RajuqkoZkdo%2FSLH4qdRIrJUngZOJJd%2FxBRtwmzlcXTtIVm1n1hlmEyOthuR%2Ff7s9LDUCRW3TS4q6rX6nTcBudTatIq2ZQPCQ1q4UyKNonHeLL79iEdppzAjK1wNlMdyXFEs74%2BC7jKWt6MfJOzOo%2BI%2BSb7O7L0Cs15GzWG1V8OLWIJEJeTdemH6mdBMNnm%2BM0GOqUBpCwy%2BOjJsdtsOOR%2FAGeUNc79S%2BISRn5e6tAS74l3dvY2hHvR0%2FMLaRPh6Hfydvc863tDW3evjCwH9jf%2F3QHEzZAl0zp9YgJtJtOw9Kux4QWqX5Yp2bpqqrHeRPY0CP0IDfjvazy1%2F8kJumTtAmOjT3dNW%2FGKc4BepRDxMTUMi0SvBkjLUtsbB2WkHMzpIGItnC0RdOEIjcyMHPY7C%2B0ZqLNwxviS&X-Amz-Signature=6bd494ead4a2512c3e2938cf38fc0237becc410e87ec956300e0c341aa5f2aef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







