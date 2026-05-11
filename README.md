



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664DEVY2C%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T194102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIAhc5VAjCq2sBTObMYNRd3sAoL%2BaGb85tBTx3ppVpwG4AiB%2Fw%2FyBWkiDfFvhaVxPV1fTvgv7wr3r7Kl64ECSnMwDlCr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMpDblBxZl3kMxN9oVKtwDuYeIKEVrjA9vn34Avld50%2BK5gKEGvy147qgXshM2EiE3Cmbi1W36jzM9VuKkwjNuA0Tht04EkNMGZ8nEmiwHkXUZEWLlQJlEDEK5CaNca0GkZbQUZUVI9D7PtCaIjxDeavvs%2BhGgKVw%2FwEBsa%2FysU%2B6YtzvU%2B6uEOZnJKggEGRvQP%2Bimdhjji4Wg9VZzncLgUgp2DSS5HVQ7etXlp0MJvYmp5aXNZmCHWLyFUQEyv16%2BHg7az50oJbrHsE%2FmbuR78Rd%2FpKRckInhiwWyHQLSe8AsieYN4ptw421umeXDHQNff5pJKLADjz%2F3KEO8FPA0%2B3%2B1Xjdedot2FEImjUooLsnu%2F%2Fw9BE55osNPS87TOz%2FxoAFNUT2IkmgO655j5BVRWTHvCmZYnfvO1Z4dDq4g2Uu911HfPFvART%2BYUx%2F9HdAtF8O5hEaKGzMtdRucP86EgGErcP1Pel2PzWoSdLzfSk47NVZtjigp38P75Im4CnEhe5zXX6Cs16A9Unzzhei2NSzBvtk0cv9%2BNGriGVuiBR5LUKvpx9M9llB7BxlNFV5DHNPuQNgs8s9d%2FdHMNlh59REVjNbXkfUevwWeIrAIRsnwQV%2B6RmhqoE%2FvRpFriMsD1dDwyQOsVbNWyaYwh7%2BI0AY6pgHRUsndPIAzokVRQkDNF8VADPz8GEBgp3JMUTQBS4iBLJ2ghdlMlm5NUPLVvO3X8nxqYt4DiS%2BoYwAaKNoXkpjlleZ6oRhDA%2Bz7xaWiaC21fwS3oGaL%2B4PnyodYUtEpHULNTyXgl1Os25x15KhOVrfRV0KJ76xicCNcTYuN%2FTGosjMeWgAo6uOJ0WrDmFgpgN5QdVlaW5fnszci9mEJyDMHRUlMPz0S&X-Amz-Signature=0896011780d8e5d1be77f2ce71e5492b6ceecd7d99d4109e4eb3e0a494cf1493&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664DEVY2C%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T194103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIAhc5VAjCq2sBTObMYNRd3sAoL%2BaGb85tBTx3ppVpwG4AiB%2Fw%2FyBWkiDfFvhaVxPV1fTvgv7wr3r7Kl64ECSnMwDlCr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMpDblBxZl3kMxN9oVKtwDuYeIKEVrjA9vn34Avld50%2BK5gKEGvy147qgXshM2EiE3Cmbi1W36jzM9VuKkwjNuA0Tht04EkNMGZ8nEmiwHkXUZEWLlQJlEDEK5CaNca0GkZbQUZUVI9D7PtCaIjxDeavvs%2BhGgKVw%2FwEBsa%2FysU%2B6YtzvU%2B6uEOZnJKggEGRvQP%2Bimdhjji4Wg9VZzncLgUgp2DSS5HVQ7etXlp0MJvYmp5aXNZmCHWLyFUQEyv16%2BHg7az50oJbrHsE%2FmbuR78Rd%2FpKRckInhiwWyHQLSe8AsieYN4ptw421umeXDHQNff5pJKLADjz%2F3KEO8FPA0%2B3%2B1Xjdedot2FEImjUooLsnu%2F%2Fw9BE55osNPS87TOz%2FxoAFNUT2IkmgO655j5BVRWTHvCmZYnfvO1Z4dDq4g2Uu911HfPFvART%2BYUx%2F9HdAtF8O5hEaKGzMtdRucP86EgGErcP1Pel2PzWoSdLzfSk47NVZtjigp38P75Im4CnEhe5zXX6Cs16A9Unzzhei2NSzBvtk0cv9%2BNGriGVuiBR5LUKvpx9M9llB7BxlNFV5DHNPuQNgs8s9d%2FdHMNlh59REVjNbXkfUevwWeIrAIRsnwQV%2B6RmhqoE%2FvRpFriMsD1dDwyQOsVbNWyaYwh7%2BI0AY6pgHRUsndPIAzokVRQkDNF8VADPz8GEBgp3JMUTQBS4iBLJ2ghdlMlm5NUPLVvO3X8nxqYt4DiS%2BoYwAaKNoXkpjlleZ6oRhDA%2Bz7xaWiaC21fwS3oGaL%2B4PnyodYUtEpHULNTyXgl1Os25x15KhOVrfRV0KJ76xicCNcTYuN%2FTGosjMeWgAo6uOJ0WrDmFgpgN5QdVlaW5fnszci9mEJyDMHRUlMPz0S&X-Amz-Signature=fbe9fbce612d6716f0f3d93c2d685ea176b89e1546605c914c8e005eb2b32337&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







