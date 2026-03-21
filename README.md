



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHUOABEK%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T012844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIDpe9jysDqw1D9ki7RrUsFoMATo1%2F3r3Ys36wlTK6uG9AiA0FT%2FLzdmY3N0nFtAoL2xc3gUyTxRDiSrPz%2BndPOZF2yr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIM300GmQ%2FRIdnuSRk0KtwDqaA9NbLHi6Kxaw9oVY%2FG%2FNONG8SPXytcfMdVS%2FV1Uh5yObjW%2FOG7TLkt6Cy2IKjFTpXvpJk2zzCiE%2F97DBaVn1SiWYoCYMRWe39ggrwIAF2mKTHK1ZBLvaFVm0fIk3AvXWhHjRiZhUH4GX85Rs1DxZsLGr9DuITV7h%2Fva8bhu0B17f8W%2FpHz6TCGjNcHn3TCX47vTIZZXXkqRcVeqpaCmCfPbP3nCUqLB6qAHnH4PHVvKZq15VPfXsjlC%2Fjf%2F%2Bth9p1TE8p5t8QYKH2ZS9%2Fq1G8gv9F8hYtl2WtP0JcVVpytzo9PEfpEyWimsWAgJT2LzOuxRlZkZW49UNVWhzg1nv8RIsX6e%2FwdwPyNgowHofEIuqVxd%2B8fTUgdZKcFV7TPsqv%2BvZ91l49IAkJ2zgXX0D1HOCoDUx3MuPqoH3wo3qa78yPmp7fykCX%2BNEdzhcxAMxu9M0mVXeuaedgibYL9wYpnSCOcNNoypdHe476GpzZBQ34wYTOkux4MGUq%2BId6PjLe11jUAy4EAa6uL%2BvDMoidwM%2Btk86PHLS8LIuxCFrlPoiLMVIKAIPUhJFGIr9X7EPjUokeL2vBPX1FtzPLmnHLbUWtNMFx04K22tz5meIV%2BUn%2FZkph6JymrAOIw79z2zQY6pgEYZChNMVGQgK4q6kwAytIZE%2BOZjIhT0ixebsJtvwprlc%2FiK3I6EcoD2lNpxAaZ2qxKNtfXqnv0FZgHJQM%2F2CgtKBbagAJHVH4ekBOoQiOuDu6fbdgiGhuvwK403X94Y5bqVSeWwusKfgB1zA4M3Lw6yLUEetGmLZ8HFeRBYGop8e1I486%2FpZlGQ%2BQIIAUZPaL33mzo1hyYjRy4jWeZB9mOSLFpiBxI&X-Amz-Signature=48ee967977b827e82812d0c4296331486bc1f708127720640e4b9ea65c0f781f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHUOABEK%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T012844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIDpe9jysDqw1D9ki7RrUsFoMATo1%2F3r3Ys36wlTK6uG9AiA0FT%2FLzdmY3N0nFtAoL2xc3gUyTxRDiSrPz%2BndPOZF2yr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIM300GmQ%2FRIdnuSRk0KtwDqaA9NbLHi6Kxaw9oVY%2FG%2FNONG8SPXytcfMdVS%2FV1Uh5yObjW%2FOG7TLkt6Cy2IKjFTpXvpJk2zzCiE%2F97DBaVn1SiWYoCYMRWe39ggrwIAF2mKTHK1ZBLvaFVm0fIk3AvXWhHjRiZhUH4GX85Rs1DxZsLGr9DuITV7h%2Fva8bhu0B17f8W%2FpHz6TCGjNcHn3TCX47vTIZZXXkqRcVeqpaCmCfPbP3nCUqLB6qAHnH4PHVvKZq15VPfXsjlC%2Fjf%2F%2Bth9p1TE8p5t8QYKH2ZS9%2Fq1G8gv9F8hYtl2WtP0JcVVpytzo9PEfpEyWimsWAgJT2LzOuxRlZkZW49UNVWhzg1nv8RIsX6e%2FwdwPyNgowHofEIuqVxd%2B8fTUgdZKcFV7TPsqv%2BvZ91l49IAkJ2zgXX0D1HOCoDUx3MuPqoH3wo3qa78yPmp7fykCX%2BNEdzhcxAMxu9M0mVXeuaedgibYL9wYpnSCOcNNoypdHe476GpzZBQ34wYTOkux4MGUq%2BId6PjLe11jUAy4EAa6uL%2BvDMoidwM%2Btk86PHLS8LIuxCFrlPoiLMVIKAIPUhJFGIr9X7EPjUokeL2vBPX1FtzPLmnHLbUWtNMFx04K22tz5meIV%2BUn%2FZkph6JymrAOIw79z2zQY6pgEYZChNMVGQgK4q6kwAytIZE%2BOZjIhT0ixebsJtvwprlc%2FiK3I6EcoD2lNpxAaZ2qxKNtfXqnv0FZgHJQM%2F2CgtKBbagAJHVH4ekBOoQiOuDu6fbdgiGhuvwK403X94Y5bqVSeWwusKfgB1zA4M3Lw6yLUEetGmLZ8HFeRBYGop8e1I486%2FpZlGQ%2BQIIAUZPaL33mzo1hyYjRy4jWeZB9mOSLFpiBxI&X-Amz-Signature=7fc33305340f431cdd5e8a0062671366122777051a3e58fec2de201f746d6b53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







