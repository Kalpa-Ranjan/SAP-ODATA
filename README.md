



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYBGNBRG%2F20261113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261113T060758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG5rOs5mdhtSIJ7a81t4J1JgUhEPyAUzGDkCpQAYXTdAAiAJTZahkX8tRtu1slOpGWqEdNdk9WYgcLnTx2mSYLyNxir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMN9ZRcZVgBsB7DQmnKtwDEQogHRIBiEaY3m5faaQUO%2Fww0oW77UGZCu1%2BN5%2BNpdVDkgiMWcm0VC97xzXs9YaMeBS2OvXwh4h18W78oO53N7hwgzihTZLF7W5n2cIS%2FlxA0U5v09SNqCpL%2Frg1asZgVIv4aZgI5FEd81Z8azQvbNi4MhSnzxZA0lfMTuZ8NV2H2ahRYO%2BylDECwxqYBKRhSV5KOfYzbPSx1SdVcc0PnAkvGFBlxOTnKARa90NWJUCwzY0kIBA8zUWBg4cKVi7Akau7mWh16r0O1TtziEjzXoEbuOBh4vQrqPIG66BwusesvddXeDbYogKtrE8ZKf2f0004q6y%2F4gxqMvIS%2F4ACY42u5rOUR9ZYp%2Fpt4Xmm7I2UF50lc2KseeLhtn62AFbAb%2ByodplylszqMY3MDa3RlBiV39ui14WByjAIhC7evAnWRZ3LDuxiruquCc6u3rf48Ge7E1VN%2Fbt%2FIbTi1LeGfG7%2BTxDNDQYrDRhPhER%2BPNpWRimZCaIlJjBesQl5r5wN2y5I3bOAllv7ahn5sFhn5PuqVsLuV8a8IFttpOW7tfBZ5d5UupJmOGeIMVN9nQuwxf8IWTk7gICcVMPVOtoHjHQCz8UGfFpGNfWFfG%2B8hAQTfRKPFiz8ym%2BwTKAwsb7a1wY6pgEcbpXOJH11%2BE%2Fr73n3qO7AOLLi3PhKVgLVMFg%2BifgJXmqmFDZ%2FMRPuK0Nwg8%2Fjks8Ysfmn5lD%2BGXHpOFicB6xCTEK2MDd50j97VLo9ivJWn7yOmPBIjcSqoZo4S84aJl8ItBkchKPI966yc%2FeUfq1d1wiT%2BYZLwuVPUbKda8rWV0CBX6Z9dBqsQ1hvOhh2XNidq8aiaSaPam%2Fanj5IMGM0X0t19X2N&X-Amz-Signature=c621cdfca8fdc35a17ec31cd5fd430e35dbb6df1e819763397c3459dcca15698&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYBGNBRG%2F20261113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261113T060758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG5rOs5mdhtSIJ7a81t4J1JgUhEPyAUzGDkCpQAYXTdAAiAJTZahkX8tRtu1slOpGWqEdNdk9WYgcLnTx2mSYLyNxir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMN9ZRcZVgBsB7DQmnKtwDEQogHRIBiEaY3m5faaQUO%2Fww0oW77UGZCu1%2BN5%2BNpdVDkgiMWcm0VC97xzXs9YaMeBS2OvXwh4h18W78oO53N7hwgzihTZLF7W5n2cIS%2FlxA0U5v09SNqCpL%2Frg1asZgVIv4aZgI5FEd81Z8azQvbNi4MhSnzxZA0lfMTuZ8NV2H2ahRYO%2BylDECwxqYBKRhSV5KOfYzbPSx1SdVcc0PnAkvGFBlxOTnKARa90NWJUCwzY0kIBA8zUWBg4cKVi7Akau7mWh16r0O1TtziEjzXoEbuOBh4vQrqPIG66BwusesvddXeDbYogKtrE8ZKf2f0004q6y%2F4gxqMvIS%2F4ACY42u5rOUR9ZYp%2Fpt4Xmm7I2UF50lc2KseeLhtn62AFbAb%2ByodplylszqMY3MDa3RlBiV39ui14WByjAIhC7evAnWRZ3LDuxiruquCc6u3rf48Ge7E1VN%2Fbt%2FIbTi1LeGfG7%2BTxDNDQYrDRhPhER%2BPNpWRimZCaIlJjBesQl5r5wN2y5I3bOAllv7ahn5sFhn5PuqVsLuV8a8IFttpOW7tfBZ5d5UupJmOGeIMVN9nQuwxf8IWTk7gICcVMPVOtoHjHQCz8UGfFpGNfWFfG%2B8hAQTfRKPFiz8ym%2BwTKAwsb7a1wY6pgEcbpXOJH11%2BE%2Fr73n3qO7AOLLi3PhKVgLVMFg%2BifgJXmqmFDZ%2FMRPuK0Nwg8%2Fjks8Ysfmn5lD%2BGXHpOFicB6xCTEK2MDd50j97VLo9ivJWn7yOmPBIjcSqoZo4S84aJl8ItBkchKPI966yc%2FeUfq1d1wiT%2BYZLwuVPUbKda8rWV0CBX6Z9dBqsQ1hvOhh2XNidq8aiaSaPam%2Fanj5IMGM0X0t19X2N&X-Amz-Signature=e71efbf2ed16de6ddffef5ee72ddcf1254eb4565c4c46bd641110567ce3b94a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







