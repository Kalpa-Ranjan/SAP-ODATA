



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CT5MQ7R%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T012220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDHRYENVAy%2FeXeUcuBkZlYWrKhpheCJ6YA1UUlvJBcl0QIge1lG6HUXrQt2ePQcCnlxYM9N5WkUg3WaA8jcwWVd16oqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ0BjF7XuMuyzusnircAySBzzmAnvsyiOcCIZ%2BvfeYJYWAlZ%2BpuEJRXGMl%2FJI6he5luJ3qkzKalGYIEqwOa9ml46iQxKiOALw2shhP5Rwtjp7r1XDE0vzFi%2FQAlpvHzYPkvBKlVbz85IYy8TlXwP2A7qXCiFX%2FZ3wTtBTLr2YsTx8smZSaTl0hXLwI0OElzBE4u%2F8TZF%2BaipZNC8fZNzvZlPR2NhYTczzFbyYhdb1VvfcGipe4hNfaQMN0Xfq5lYr1H2cvZSWbHarNWFBXl7wvnZ%2BMsZYDR8L%2FMk9SlEomsj8JTD7h1Espmo2ocy13aKrzcFQiFpZVq6UvF%2FUhfOJxQqyNWP%2BwqmrJiJbEkFs7vKmPNhl3bGYIUcm%2FDJhzGycrxVEuZEroDHVaUOibaJXEQu%2F9TA6G1LTsIZBWrHbM%2F8i%2BCRUookrLJ%2Fl%2BN3C0etEojhp1zVa8QND1NLF1eeLUh%2BuL0mtBropqOnI0qakBohKdXy8O8i8qUL1GcvYtBhbznxugAcUk0%2F%2BKqWPGuArliqL3yERdrK3H058dVWXR0Yn5mgbcDbD%2Fz90zo4H6PCOz6yMBKgbuK%2FxPPFWdagbyU9EfojjLhfrFhIHNUdyyevbBarpwxrNPcIFJY%2BurD%2Fz9%2FW6hiXz5kDWzoMNX4kMsGOqUBFGU68qIHXq5%2BS5SBm7vg6LSSJuz38wYHrKqGcuv7hdnPMVy9k9Mvx5daRU5ffEpjKrpA%2Bt9EBOFk9ULMRHzLwBbYIEcPR%2FbypkMVCZfqmscLjY1LPIRy%2BVUyoVeCrPHeeghl8Z392r8oo2cG%2BwHE4pgLmU0TsppSWlJoKsinhnebNIMkTDCGSwPfFsOW8%2BgL%2FrMAOUnwSZeWrQGLdvcq1LMFL0X2&X-Amz-Signature=7e23210021ba2f4a5ffe0004b3a8f5fcdd9d0530933b1975309f1a26e2e2a36a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CT5MQ7R%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T012220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDHRYENVAy%2FeXeUcuBkZlYWrKhpheCJ6YA1UUlvJBcl0QIge1lG6HUXrQt2ePQcCnlxYM9N5WkUg3WaA8jcwWVd16oqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ0BjF7XuMuyzusnircAySBzzmAnvsyiOcCIZ%2BvfeYJYWAlZ%2BpuEJRXGMl%2FJI6he5luJ3qkzKalGYIEqwOa9ml46iQxKiOALw2shhP5Rwtjp7r1XDE0vzFi%2FQAlpvHzYPkvBKlVbz85IYy8TlXwP2A7qXCiFX%2FZ3wTtBTLr2YsTx8smZSaTl0hXLwI0OElzBE4u%2F8TZF%2BaipZNC8fZNzvZlPR2NhYTczzFbyYhdb1VvfcGipe4hNfaQMN0Xfq5lYr1H2cvZSWbHarNWFBXl7wvnZ%2BMsZYDR8L%2FMk9SlEomsj8JTD7h1Espmo2ocy13aKrzcFQiFpZVq6UvF%2FUhfOJxQqyNWP%2BwqmrJiJbEkFs7vKmPNhl3bGYIUcm%2FDJhzGycrxVEuZEroDHVaUOibaJXEQu%2F9TA6G1LTsIZBWrHbM%2F8i%2BCRUookrLJ%2Fl%2BN3C0etEojhp1zVa8QND1NLF1eeLUh%2BuL0mtBropqOnI0qakBohKdXy8O8i8qUL1GcvYtBhbznxugAcUk0%2F%2BKqWPGuArliqL3yERdrK3H058dVWXR0Yn5mgbcDbD%2Fz90zo4H6PCOz6yMBKgbuK%2FxPPFWdagbyU9EfojjLhfrFhIHNUdyyevbBarpwxrNPcIFJY%2BurD%2Fz9%2FW6hiXz5kDWzoMNX4kMsGOqUBFGU68qIHXq5%2BS5SBm7vg6LSSJuz38wYHrKqGcuv7hdnPMVy9k9Mvx5daRU5ffEpjKrpA%2Bt9EBOFk9ULMRHzLwBbYIEcPR%2FbypkMVCZfqmscLjY1LPIRy%2BVUyoVeCrPHeeghl8Z392r8oo2cG%2BwHE4pgLmU0TsppSWlJoKsinhnebNIMkTDCGSwPfFsOW8%2BgL%2FrMAOUnwSZeWrQGLdvcq1LMFL0X2&X-Amz-Signature=eeb521ca02d3a7efb0cbf43648f89e84a6edeaf9646c753d2838b613d2d8b838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







