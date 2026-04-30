



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNSOULEZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T081141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCID0o003qb8W0hhtRxgUnygCeNUNXSlzjJ%2FL0QYuBWicbAiEA%2BsviRmqC0RScm1fGZwmAKHxNcVqdXMq6zAZHloyKNF0q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJKJxYTKAXMkkag6ACrcA4qLi7ZFXE7X3MF6qWsjr9a1oACttxN1m79xVpHI2o4JpWWoielYwx3R4c7KQctTFslusGoj7YV%2FUnJnJdBDIvZbxxceplnXnHmAhLphi3StfzHUZq6QQzuMWEZAbhE4eJDl6leZEQkTlgOsQw8Rfg1VhH90j4aeW7lkztD1iwkuESJAwtrlZSPXHSdYW0QdySivLTygcHDqrGNfObn6wIpVXumdwbCvRfv8nKcNfrhbZMmlzwANaHWfqtJ%2FLoscc%2FzqbHGVjZuN2fibSqVZYoGxVEjj7VgaQeXu9%2BCj6U4R72p2U85hWEgEvQnyWGnLpKTBhip87NZjBexb6K9w5vonQpUqQkb6t8l2ITalYlOqPYzkQksx2pKgF3qYCI1Fdjreny8QsFhvdPkKr8z5NGSXkU9UCjQvDuv1ZuiZ4ynNhzfUCRBKdH6BiMAm%2BTNc002yznp5FZYNIQIDCWtJCnKAMX0KsA6lRQqZg41tudLTmAvRe5%2FrCdRTK5qUQCyoY4lyNx5SSxw1bT%2BGXMmVpRCXSMOCXnZevKjdMEx4UxfYZSrRX79aI8LkH%2BA%2FCiEWiJjuKDf%2BfhVyoAwEdnn33FR530uI5BGdu7k2Djt7hK5%2Bz3WqQrNW95bCfJcfMM2czM8GOqUB8VG9IgmTtt%2FKb67tk6G6ND0nzmO1NxYTUFfo14UD84dOJP07FxJ14kyutbD0FRIYZelbagn8IYO%2FTm%2FfW4T9zO1VHPl1rD%2FclEY6bEorv6opPtEuDyo7xU2awiAtedTDBY4Fo8sBdWoMeOXL9eMkQJpm7iXj18OxQbj5v8nXEc3UW6n0ToDMfSmq2yGU0oUDVil4JM8PFEy1nZu7DldUuhqS60eB&X-Amz-Signature=700178cb7f141e0d601496a37b69162578b496657dcb57e8124e6312d9469ba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNSOULEZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T081142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCID0o003qb8W0hhtRxgUnygCeNUNXSlzjJ%2FL0QYuBWicbAiEA%2BsviRmqC0RScm1fGZwmAKHxNcVqdXMq6zAZHloyKNF0q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJKJxYTKAXMkkag6ACrcA4qLi7ZFXE7X3MF6qWsjr9a1oACttxN1m79xVpHI2o4JpWWoielYwx3R4c7KQctTFslusGoj7YV%2FUnJnJdBDIvZbxxceplnXnHmAhLphi3StfzHUZq6QQzuMWEZAbhE4eJDl6leZEQkTlgOsQw8Rfg1VhH90j4aeW7lkztD1iwkuESJAwtrlZSPXHSdYW0QdySivLTygcHDqrGNfObn6wIpVXumdwbCvRfv8nKcNfrhbZMmlzwANaHWfqtJ%2FLoscc%2FzqbHGVjZuN2fibSqVZYoGxVEjj7VgaQeXu9%2BCj6U4R72p2U85hWEgEvQnyWGnLpKTBhip87NZjBexb6K9w5vonQpUqQkb6t8l2ITalYlOqPYzkQksx2pKgF3qYCI1Fdjreny8QsFhvdPkKr8z5NGSXkU9UCjQvDuv1ZuiZ4ynNhzfUCRBKdH6BiMAm%2BTNc002yznp5FZYNIQIDCWtJCnKAMX0KsA6lRQqZg41tudLTmAvRe5%2FrCdRTK5qUQCyoY4lyNx5SSxw1bT%2BGXMmVpRCXSMOCXnZevKjdMEx4UxfYZSrRX79aI8LkH%2BA%2FCiEWiJjuKDf%2BfhVyoAwEdnn33FR530uI5BGdu7k2Djt7hK5%2Bz3WqQrNW95bCfJcfMM2czM8GOqUB8VG9IgmTtt%2FKb67tk6G6ND0nzmO1NxYTUFfo14UD84dOJP07FxJ14kyutbD0FRIYZelbagn8IYO%2FTm%2FfW4T9zO1VHPl1rD%2FclEY6bEorv6opPtEuDyo7xU2awiAtedTDBY4Fo8sBdWoMeOXL9eMkQJpm7iXj18OxQbj5v8nXEc3UW6n0ToDMfSmq2yGU0oUDVil4JM8PFEy1nZu7DldUuhqS60eB&X-Amz-Signature=de5543a5983c7d0cfbd5ddcbe6b002fed99d100000dc5b9b97b343189001d6f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







