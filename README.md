



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGV3I6DY%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T132503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIGB2pHczkvldrMmRDdNCIwQexqZVgn7VTUCEU%2BLEUuVpAiEAoMZiGYMMZgFaY410ost7vqWDrfY65DS8%2BxGf60oJ%2B%2Foq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDO5PWSTX6n3aIAFuySrcA4NZNlAXN4sZ3KOwajO5LH%2Fqm3oFOE5XFGKD7XwCadWwD%2BJLi2hginZb9ZCbKo9X59wghLA%2BlFz2Fxa%2BaVnRL1e4uRjmnNPbLo8cFyFpOuhspDI37nBL5XbGbJYM5rxkIvOpGqHq0GOAp2jUDjI3D8wVe9kquGMhXOvDWoKLuJIa8ELvOZkHBksPmYrvUcRtNFPyl1k0suHM%2F5ksd0l5bFJJJhjesBxLg9eshAm4ccsgMusm9olYQ81wB0IlBSY1bYiNZGFhPnrrqrvSGDtUIQdv6GxCi4tGYLKZDY%2Bj%2FFlkqlA%2Bhx1l3BebvUQjZguq33lqtp%2FSLnS927Wtq4Tu6uxDbsyQJ6pDzxWsXqs8f%2FCd8hWiMVNOe%2Fk8upRfAD5mxFo6gdU%2Fm18hAV4t6gw74g1Z44QE4hhmA5E%2B1Y91blcutQGxBXGevYNc%2F809F7VY2dAc%2FeJAf2F680vHU1GEkfKZZYYVN1uXmEy7ru%2BWKEX8t52UF4YkbrVznc0qljhSE1K6GOLqUNc9IUTGR%2FZ6rXlAKgb1urlg5ub%2B%2B747E8cf8cwyDnLgb4Yb4Nl3aEa%2FVmHFWz4arLks9vMMEWpoQWuOl49Y2C5KjLA%2FE3NEBIBqyx1oGRIAaaThoACRMIvkjNMGOqUBPta2HPvThjoCsXW2WIWKfj6tzrMIYuXE9s5WRXQjz2RSjOQzuKPdPEH902gPc%2BGs5SXQ3mzybrwRnW8Pmveo95h6URD2I2n6XYpkF%2FMQHQzXXDxZyy7zrdZn5SP0NNv%2BWclWzgXsuajTt1IhWHP45WM7hE9EwR%2FN2spgEFt0wCy2OV81%2Fb2ZCzOz6tp8tx77DELUsV2PCDHUs62eeG7IMov%2BJk8g&X-Amz-Signature=b59b5323bda28771a82bb3946168f7ce3724cb3b35d79df67b6fadcb1ca1ee6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGV3I6DY%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T132503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIGB2pHczkvldrMmRDdNCIwQexqZVgn7VTUCEU%2BLEUuVpAiEAoMZiGYMMZgFaY410ost7vqWDrfY65DS8%2BxGf60oJ%2B%2Foq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDO5PWSTX6n3aIAFuySrcA4NZNlAXN4sZ3KOwajO5LH%2Fqm3oFOE5XFGKD7XwCadWwD%2BJLi2hginZb9ZCbKo9X59wghLA%2BlFz2Fxa%2BaVnRL1e4uRjmnNPbLo8cFyFpOuhspDI37nBL5XbGbJYM5rxkIvOpGqHq0GOAp2jUDjI3D8wVe9kquGMhXOvDWoKLuJIa8ELvOZkHBksPmYrvUcRtNFPyl1k0suHM%2F5ksd0l5bFJJJhjesBxLg9eshAm4ccsgMusm9olYQ81wB0IlBSY1bYiNZGFhPnrrqrvSGDtUIQdv6GxCi4tGYLKZDY%2Bj%2FFlkqlA%2Bhx1l3BebvUQjZguq33lqtp%2FSLnS927Wtq4Tu6uxDbsyQJ6pDzxWsXqs8f%2FCd8hWiMVNOe%2Fk8upRfAD5mxFo6gdU%2Fm18hAV4t6gw74g1Z44QE4hhmA5E%2B1Y91blcutQGxBXGevYNc%2F809F7VY2dAc%2FeJAf2F680vHU1GEkfKZZYYVN1uXmEy7ru%2BWKEX8t52UF4YkbrVznc0qljhSE1K6GOLqUNc9IUTGR%2FZ6rXlAKgb1urlg5ub%2B%2B747E8cf8cwyDnLgb4Yb4Nl3aEa%2FVmHFWz4arLks9vMMEWpoQWuOl49Y2C5KjLA%2FE3NEBIBqyx1oGRIAaaThoACRMIvkjNMGOqUBPta2HPvThjoCsXW2WIWKfj6tzrMIYuXE9s5WRXQjz2RSjOQzuKPdPEH902gPc%2BGs5SXQ3mzybrwRnW8Pmveo95h6URD2I2n6XYpkF%2FMQHQzXXDxZyy7zrdZn5SP0NNv%2BWclWzgXsuajTt1IhWHP45WM7hE9EwR%2FN2spgEFt0wCy2OV81%2Fb2ZCzOz6tp8tx77DELUsV2PCDHUs62eeG7IMov%2BJk8g&X-Amz-Signature=2263c27b48aee152aaf49484f49a40db1ccd66d55f0120c32f72fe43657a2050&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







