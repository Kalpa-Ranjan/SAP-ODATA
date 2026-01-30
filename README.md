



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDMZFGRT%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T014204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7jf0hnkGnzD0DKrIpQEqbzTO%2F6xtpJhFttCwzCQXneQIgYgrH3FVzcIYxH135yyNbaEcOC1fc5iHrkSBlHs%2BnNQcqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb1KHlGPJsa6bHOjCrcA4iMiD9%2BGHe4iOVFaC2%2FG1ECF8EjRIhpWGPlp5wsrK9jcscViwaVrSFsehGgI2GYpn2MbSa58U6i3fklhacBm2R1IPiYVecyU91hYhbOETUNc2tKfK5rURM%2FTCB4%2FcrYZq%2BVwnY277N7%2Bag7Eh%2Bh9FmdyFEvolsaIkw7IoBGArXZCtGW8zkERetq0SNNHwZv6PIh8bi4C9unBEPXX1Gw86fcoE408sQvaYaqaTgticfKdpNB%2BE8fcfi7ocn3RHISdOXB0ZIo3mcu%2FJbNhE2nWUEptCVXVxi8fxvZoaze7%2BAvh%2FeeoGSz2vMiSloNIdXkAT1cIfcFk33ORtglLOY1yZ70NgITYN2CAmV9kohiWYTGNur7d8MvS2%2Fys0yUtCOatMTbqzzUb8NC1dUyvzoqdncgUu9lpgLViJqeTKqnCAbB6IWDFFRqgIrmGTEIlzFKD7TxSjtuazs1peRExe2umhPbL%2FCHfNucN7es19WFMWptai6x%2BbkKFfYGLHyoOLWStizT5k03lYylpt637B2Zqp5cuKW3H%2BEFM5WNrTGrbe7574MSqywfzDAVBjnidgzVgpANaocs3sz1%2FgwPtc4Vi8SWTtKksQWWc8xDimNB0dIPgXLFx2QIu%2FG81%2FggMLOB8MsGOqUB6r72PNj0FlXaeG18y%2FWpWSCMv4lMuMZ%2B7LdAAqKMG7YWiinhmjyh0HYH6fge%2B8MTKhDuacw1Qpo0ILUtfhkylTuc7lI5q%2BiS79HOMz66dPtTGfej2hRmSu9%2FjojvyXM39Ue39qnalfnuQqHAs%2BeYESQHhINEhtCJZ3Wdis%2FzTDpB69Q%2FwSDjKLEVJfmIwnfOpYAL4XC%2B2Pe0ba5v%2BZBT2wOoOI2x&X-Amz-Signature=38185ba51c374c97de07238c069e95bd1239413005c913b98a17b0e0fe3c5f53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDMZFGRT%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T014204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7jf0hnkGnzD0DKrIpQEqbzTO%2F6xtpJhFttCwzCQXneQIgYgrH3FVzcIYxH135yyNbaEcOC1fc5iHrkSBlHs%2BnNQcqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb1KHlGPJsa6bHOjCrcA4iMiD9%2BGHe4iOVFaC2%2FG1ECF8EjRIhpWGPlp5wsrK9jcscViwaVrSFsehGgI2GYpn2MbSa58U6i3fklhacBm2R1IPiYVecyU91hYhbOETUNc2tKfK5rURM%2FTCB4%2FcrYZq%2BVwnY277N7%2Bag7Eh%2Bh9FmdyFEvolsaIkw7IoBGArXZCtGW8zkERetq0SNNHwZv6PIh8bi4C9unBEPXX1Gw86fcoE408sQvaYaqaTgticfKdpNB%2BE8fcfi7ocn3RHISdOXB0ZIo3mcu%2FJbNhE2nWUEptCVXVxi8fxvZoaze7%2BAvh%2FeeoGSz2vMiSloNIdXkAT1cIfcFk33ORtglLOY1yZ70NgITYN2CAmV9kohiWYTGNur7d8MvS2%2Fys0yUtCOatMTbqzzUb8NC1dUyvzoqdncgUu9lpgLViJqeTKqnCAbB6IWDFFRqgIrmGTEIlzFKD7TxSjtuazs1peRExe2umhPbL%2FCHfNucN7es19WFMWptai6x%2BbkKFfYGLHyoOLWStizT5k03lYylpt637B2Zqp5cuKW3H%2BEFM5WNrTGrbe7574MSqywfzDAVBjnidgzVgpANaocs3sz1%2FgwPtc4Vi8SWTtKksQWWc8xDimNB0dIPgXLFx2QIu%2FG81%2FggMLOB8MsGOqUB6r72PNj0FlXaeG18y%2FWpWSCMv4lMuMZ%2B7LdAAqKMG7YWiinhmjyh0HYH6fge%2B8MTKhDuacw1Qpo0ILUtfhkylTuc7lI5q%2BiS79HOMz66dPtTGfej2hRmSu9%2FjojvyXM39Ue39qnalfnuQqHAs%2BeYESQHhINEhtCJZ3Wdis%2FzTDpB69Q%2FwSDjKLEVJfmIwnfOpYAL4XC%2B2Pe0ba5v%2BZBT2wOoOI2x&X-Amz-Signature=bf3ede0fd4ab94abac2fcb233a69d9ef19a53c5850f1750c67e0975d7782e013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







