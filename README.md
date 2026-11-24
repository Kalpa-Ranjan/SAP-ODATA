



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBII2RO%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T180546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTxBBiempx7ybjloSo2xMC4TTTPgzRzA9UH2oFh9MxrAiAlCxJ09A0cEoNHgZ7XYILpWE684UCDaC9dbVQQWsCorSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmGQBSz9SFqMhrlFbKtwDaIhcz8utkHroCeTlu45zLrabPC0q%2BGWGwYJxPDSNv%2FS%2Bi5V65t16uqLn2HwWroRXgXYL31fCmGQqO9qdald3nMjjj8cu3006mdWFsUkGo9Svdi9vR%2Fr4kQhSgsQa2MGxXjJhkeCD8srhhulaeehrtCA9JN3dNu0e6YqWY1PLHx3Zd0sml0oRjtY2qUVpo7Pia%2BncBMHs9QOguJKGUM9kK%2Fpw6Xy0r9BtjA5Whe6T41TvPGqKA%2FOi%2FCIfMxtRMNve8M9FpnEjd0f2IBBc5J9IVmRJnkopvRqm%2B5uDlyor48p87Jwa5I3mc8xgNdKSCIEi9t0SVrBl2SK4MrjluGRjyDuIsrftDdxQdeuJxAw0SVUBw7W5jdqw4VHbXj24dQw9%2BZMYUcD4PoFUwM9U3NkqgF0t3HzL%2FbwsUV8CfsXzYW3Zx0q%2BWqWXfcIu7n4HioPjU9vdr8thwHOW3cVc%2FSTtOwLRQlssCdd8x%2FvehwrEOGtdwrqo8Z5g%2BJxmm%2FDV0MPW1oc%2Fr1i1Nl4u3oB1pEjylvLJWjJe69r8wTjK1WPjUrReoHRC5%2B5rfSrjGXt7QDOeMRvUpQCXykmMC%2BCjkL7tqqo%2FIvAk9toLFnL33eCawejbLrAy1Eg%2F0qLfAAgw5YyX2AY6pgGryPQ8tktPq%2Fsa9eNyMk%2FwPImxzbQqWrMbznNaMoMrbbejQiE8tVE36daSlXjJWswZ1htm%2BVLOlzVU6ABbG20c2rBnaO%2B0GLyGkeQ0%2BvRRdBu%2FTXEupvnnAOz7V%2BGLS0AEd6JnuT8xDKOalJVzwpIF8xZQXekhBkbWzxzycBaclPVCjJU1Fp9denJ3SJMyoBuldGL3xzG3v73az5zqK7%2B%2F0rn%2BxTPi&X-Amz-Signature=31a0f168c86fc0bde0645dab60062f31f8a357da3eb02af98990d100e5c1ea60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBII2RO%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T180546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTxBBiempx7ybjloSo2xMC4TTTPgzRzA9UH2oFh9MxrAiAlCxJ09A0cEoNHgZ7XYILpWE684UCDaC9dbVQQWsCorSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmGQBSz9SFqMhrlFbKtwDaIhcz8utkHroCeTlu45zLrabPC0q%2BGWGwYJxPDSNv%2FS%2Bi5V65t16uqLn2HwWroRXgXYL31fCmGQqO9qdald3nMjjj8cu3006mdWFsUkGo9Svdi9vR%2Fr4kQhSgsQa2MGxXjJhkeCD8srhhulaeehrtCA9JN3dNu0e6YqWY1PLHx3Zd0sml0oRjtY2qUVpo7Pia%2BncBMHs9QOguJKGUM9kK%2Fpw6Xy0r9BtjA5Whe6T41TvPGqKA%2FOi%2FCIfMxtRMNve8M9FpnEjd0f2IBBc5J9IVmRJnkopvRqm%2B5uDlyor48p87Jwa5I3mc8xgNdKSCIEi9t0SVrBl2SK4MrjluGRjyDuIsrftDdxQdeuJxAw0SVUBw7W5jdqw4VHbXj24dQw9%2BZMYUcD4PoFUwM9U3NkqgF0t3HzL%2FbwsUV8CfsXzYW3Zx0q%2BWqWXfcIu7n4HioPjU9vdr8thwHOW3cVc%2FSTtOwLRQlssCdd8x%2FvehwrEOGtdwrqo8Z5g%2BJxmm%2FDV0MPW1oc%2Fr1i1Nl4u3oB1pEjylvLJWjJe69r8wTjK1WPjUrReoHRC5%2B5rfSrjGXt7QDOeMRvUpQCXykmMC%2BCjkL7tqqo%2FIvAk9toLFnL33eCawejbLrAy1Eg%2F0qLfAAgw5YyX2AY6pgGryPQ8tktPq%2Fsa9eNyMk%2FwPImxzbQqWrMbznNaMoMrbbejQiE8tVE36daSlXjJWswZ1htm%2BVLOlzVU6ABbG20c2rBnaO%2B0GLyGkeQ0%2BvRRdBu%2FTXEupvnnAOz7V%2BGLS0AEd6JnuT8xDKOalJVzwpIF8xZQXekhBkbWzxzycBaclPVCjJU1Fp9denJ3SJMyoBuldGL3xzG3v73az5zqK7%2B%2F0rn%2BxTPi&X-Amz-Signature=19e83fe9eeb7880507d2a33526554b26b4cb213ec08858153682a102df12720c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







