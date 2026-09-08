



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZV3VC2%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T061245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEX%2BsnUBnl8sXuN9nj%2FwnWR22IpjitbJaL2O7khbFTNDAiA%2Fr8fJB%2BnM7ID9q0sygFO7Z0HqyranhKMUlfPffAArISr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMQmFgr4Ib0EbHcD26KtwD6jhkF9VCuuwlhYLHsKHz0fAIjIWlVU%2FOO8Sq9omUYXfJ0aDBesS%2FmikydEIOMM%2BLH8iwPe7culEG4zBAliL1hEP2O3sQJHExtnORb4IVk62h%2FSbCW44xubVw69r4IY3wWnHs5yvcp8TkUIrE2DHynCCUdIhYdJkhJnqdrkqR7pp3KB%2Bxm5%2FwuxfauwgcqiXE76%2BJyg6DiDzE%2BSE1Ahm%2Fv0MFtOOC1ubYAhCN8yTr%2FjUPIaJCgDQDTc7QjjeA%2FYFgWIQGPyK%2BLHD5PC5eU7swYqtOh31L5XIOtJtlyynWntxfDku17EjP9mpYwYKO3DkFGN5jhdQmIgl1vMRLu99b9BE2U7dVQuSJoCpn76QzIHbt4W%2BB5EJodigFWeb8cxtMb2NEwkLiF8e4%2F6pr6%2BedcuheI3%2BYPlpBK1vJognWiWt2liO3Dtbu6fF%2BG6epIsQ4vMnEuwgVYlbXReoEic38GoUT6%2BCDnEveGKML3GkxbpT1eWLWtVLFF1cXqV2cRZWE9zZDsmaKJMWBkKUZZTU8X%2B1ISIZmZP7AMn23Bp3miiJ0CFi8G8jkezT31LqHBS4Q%2FTSwBWK%2FLS9b0g15nan8QmaY4u4Uui5EScapTUO4aQL0XVzLJ1sQrh6Z0ogw7Zf%2B1AY6pgH1LS8JTBnh1AhfM0jR%2FfSyClBUhhKO5EgMsbz592tIkgo2cyi84ajtsSTuzIPqUTLpK4wn18csC%2Bk9alf8nNDRCrQhe1JOFF2ZIGz%2Bzw3cg2kyszpbzOG3M9%2Fvjlh7mdlgTnWgZlB01eB8TMmzTYpSosLQFa1Eia1ZXnrS5AYMLHhm7byq1TRcND98ufhwHo6HJIX9Bcd8JYgaF%2BEqnuQHqkYmt2oL&X-Amz-Signature=68c12c5b2ac9b0d5cac73158eff6d9be39ed0df958f08c423539718458900a29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJZV3VC2%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T061245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEX%2BsnUBnl8sXuN9nj%2FwnWR22IpjitbJaL2O7khbFTNDAiA%2Fr8fJB%2BnM7ID9q0sygFO7Z0HqyranhKMUlfPffAArISr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMQmFgr4Ib0EbHcD26KtwD6jhkF9VCuuwlhYLHsKHz0fAIjIWlVU%2FOO8Sq9omUYXfJ0aDBesS%2FmikydEIOMM%2BLH8iwPe7culEG4zBAliL1hEP2O3sQJHExtnORb4IVk62h%2FSbCW44xubVw69r4IY3wWnHs5yvcp8TkUIrE2DHynCCUdIhYdJkhJnqdrkqR7pp3KB%2Bxm5%2FwuxfauwgcqiXE76%2BJyg6DiDzE%2BSE1Ahm%2Fv0MFtOOC1ubYAhCN8yTr%2FjUPIaJCgDQDTc7QjjeA%2FYFgWIQGPyK%2BLHD5PC5eU7swYqtOh31L5XIOtJtlyynWntxfDku17EjP9mpYwYKO3DkFGN5jhdQmIgl1vMRLu99b9BE2U7dVQuSJoCpn76QzIHbt4W%2BB5EJodigFWeb8cxtMb2NEwkLiF8e4%2F6pr6%2BedcuheI3%2BYPlpBK1vJognWiWt2liO3Dtbu6fF%2BG6epIsQ4vMnEuwgVYlbXReoEic38GoUT6%2BCDnEveGKML3GkxbpT1eWLWtVLFF1cXqV2cRZWE9zZDsmaKJMWBkKUZZTU8X%2B1ISIZmZP7AMn23Bp3miiJ0CFi8G8jkezT31LqHBS4Q%2FTSwBWK%2FLS9b0g15nan8QmaY4u4Uui5EScapTUO4aQL0XVzLJ1sQrh6Z0ogw7Zf%2B1AY6pgH1LS8JTBnh1AhfM0jR%2FfSyClBUhhKO5EgMsbz592tIkgo2cyi84ajtsSTuzIPqUTLpK4wn18csC%2Bk9alf8nNDRCrQhe1JOFF2ZIGz%2Bzw3cg2kyszpbzOG3M9%2Fvjlh7mdlgTnWgZlB01eB8TMmzTYpSosLQFa1Eia1ZXnrS5AYMLHhm7byq1TRcND98ufhwHo6HJIX9Bcd8JYgaF%2BEqnuQHqkYmt2oL&X-Amz-Signature=743a9c071ae8a104601ae63dcaecfe63b59c7f59019c97248f2c70c5ef2c4202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







