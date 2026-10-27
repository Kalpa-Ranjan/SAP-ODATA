



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ2H3JTT%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T180708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDDT%2FNrpWQTebwHrHTB%2BzAS%2Ftf8TRXKqZ5RpBlck2K1wwIgfJai%2Fspa3Xoii5O8MzA4btBSTLh%2FseS%2B5quQBZ7h8z0qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJdouApRcvjFGHbGCrcA4UP0h6%2Bd7E6a6qrEgLrEJwJ%2Fv0A6yoT2osTpa%2FFCm5Cbjj3jxCTVwivFPPIuM%2BaduvvvPn5%2BBwnnZkW%2F9XM5XJc3OmppnoJBaV7LCC2KW4ncfG%2FQO9N1TuGoEiHAVl2Fn6%2B3L9VcSgiHK%2FUj040BM8klitg4OKTaqDXMMNcP4jl5ZZvqtrwGo92ft%2B0Am6Nw%2FJkzDwkmldTkZWTYdStxOcdT%2F7DoaBiYumDhZHB%2F%2Fu7oWoenGELh1txLCRzTia87pkOj8u%2BsiXiDAeWtNQ1mgjbUly8Rq9%2FurBfvKwIeHY62AtpgoIvRAxNF%2BmolQnaM1HjitTMj0oZpfJPRO31OMUhwJ5FaVMRcZkSCx3tcvMzaLSxWXIQsdm7H%2B%2F3mylGv3WLhCbyvwz3th3RjvLo8V%2BCyO3Hh7Wnm2RsUhxXKvm%2B4soUG2f7R3TowcIBuQHOEZUsAomiRxpMzv9LrdB1t0rIL5pqNUgXYI7641KM00mo%2BydN9c4xWMctd3hQ%2BGCQPxmdDISNZMLriJldbqALgInOWXRWarSaQfD9Dgke6KYMuHTiQXWm47CuMVW4RGECSTs6K64PcQX6oyv31WyD%2F65NBs5y1P3Y7M9cQP7mdFp6FmAFVSpST2mi%2BaMgMLGig9cGOqUBMKCMxZjOL3o8Zt0BPgnMGQFNx2%2FBmFg9f6Pd9r99K7P2%2FMqvt9jqmypGAYzegMPab7vfGgT088ChM0iJ8WmOUgpZKiUuVEJPEKQGBiyGD01M9N9lnbkfCd0JaH0Uh9IY0LHsOV8F4417bJvxfSzsAb25%2F6hDjEX7GI%2B3gce3dzgtz1IBJCBo%2FUzZNoWiQp67Z9snC%2F7xz6SUQxzvKFCchnWjkdM%2B&X-Amz-Signature=142a7e99bfd09cf55e063db79795466b630c3b80818b3c61a7504b18fcef8f2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ2H3JTT%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T180708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDDT%2FNrpWQTebwHrHTB%2BzAS%2Ftf8TRXKqZ5RpBlck2K1wwIgfJai%2Fspa3Xoii5O8MzA4btBSTLh%2FseS%2B5quQBZ7h8z0qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJdouApRcvjFGHbGCrcA4UP0h6%2Bd7E6a6qrEgLrEJwJ%2Fv0A6yoT2osTpa%2FFCm5Cbjj3jxCTVwivFPPIuM%2BaduvvvPn5%2BBwnnZkW%2F9XM5XJc3OmppnoJBaV7LCC2KW4ncfG%2FQO9N1TuGoEiHAVl2Fn6%2B3L9VcSgiHK%2FUj040BM8klitg4OKTaqDXMMNcP4jl5ZZvqtrwGo92ft%2B0Am6Nw%2FJkzDwkmldTkZWTYdStxOcdT%2F7DoaBiYumDhZHB%2F%2Fu7oWoenGELh1txLCRzTia87pkOj8u%2BsiXiDAeWtNQ1mgjbUly8Rq9%2FurBfvKwIeHY62AtpgoIvRAxNF%2BmolQnaM1HjitTMj0oZpfJPRO31OMUhwJ5FaVMRcZkSCx3tcvMzaLSxWXIQsdm7H%2B%2F3mylGv3WLhCbyvwz3th3RjvLo8V%2BCyO3Hh7Wnm2RsUhxXKvm%2B4soUG2f7R3TowcIBuQHOEZUsAomiRxpMzv9LrdB1t0rIL5pqNUgXYI7641KM00mo%2BydN9c4xWMctd3hQ%2BGCQPxmdDISNZMLriJldbqALgInOWXRWarSaQfD9Dgke6KYMuHTiQXWm47CuMVW4RGECSTs6K64PcQX6oyv31WyD%2F65NBs5y1P3Y7M9cQP7mdFp6FmAFVSpST2mi%2BaMgMLGig9cGOqUBMKCMxZjOL3o8Zt0BPgnMGQFNx2%2FBmFg9f6Pd9r99K7P2%2FMqvt9jqmypGAYzegMPab7vfGgT088ChM0iJ8WmOUgpZKiUuVEJPEKQGBiyGD01M9N9lnbkfCd0JaH0Uh9IY0LHsOV8F4417bJvxfSzsAb25%2F6hDjEX7GI%2B3gce3dzgtz1IBJCBo%2FUzZNoWiQp67Z9snC%2F7xz6SUQxzvKFCchnWjkdM%2B&X-Amz-Signature=a100a95304271e5a717f4cea76f166037cd0030b07e6925cd7b8f7d349e9ead3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







