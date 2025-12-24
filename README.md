



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YXK37HQ%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T062701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQDMEB8pD2WOrKduq6TekLl5WXpKxVnGtAilGSrQkQ6L0wIgPWcwt35LjWJXUTowT%2FvAdQ0%2F9J%2B4lE72LJcmUDjALSQq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDBxbUP0fDlEdPTKbOSrcA7KmgRFFxSz34%2Fyj3gx%2FSbQBEIG6cLvP0GQKvrTeN7dUJzmJ2M0BVz0jWaZWQwrWUmjAOS3imRRkaGkfHqRvAZdcLjW0GEzT42z7cm2fBgipKxQsKIkEE5BiiMgqE6j5xnckg7kj7dumig%2Bkg6ZiZj2aSMq%2FIYHpZfGNA60EIvWPLNZkdDEmWqZJ9FrSoSe79UNYd5vHAQ4MqaLBrgr4E1GAAQpS5exX%2BFJheVA8wtTBA9u8kWvoZB730zEmxV%2FxJXxdKSdTk6j3BmcgkisFMjc60srDIK%2BIQIg%2BHwtVE6a5%2BSBRr8pK%2BbrLCgKUY1XpbMbZZkxkMxMuSJgTBVfn9rT1VbEh2lowWfDIpMVYllC1EYX17k5Y7KrdxeTQj5X8ikZBGbz4v5S%2FTbij5binrp3ZngwU7TTBTdqouUltvNGogMeCELqTLzUYAHjBE9vL746n7SsPTRZ4LuHYYM0qRrOq5icdRkGmOkpEd7UEQsaVHm1Q7gm%2BJTYnsAsIa0Mg6edDtlDGM3oaPp4SoDLTKYrqIMLPjCPOz%2FqjLL0jU0DPspFl71dyGzRTeuFAiIQCc4m%2FyTZQQBDuaKXJ0Vx%2FiRLrTsEUfAsP%2BglnP2VhulfS4%2BWDrFl4wBA5hhriMMDdrcoGOqUBgn5c8qfVoFoRErkOUW5aN8WQqBcE6AAyMaWW%2FY0PU8oIrGXZeawlRfmYac4cyxancOiLmA%2FwIZxuG7Rw4FyTGtvzA8v9O60%2B3BUmkrD0qkQqE9y7efOO6IoJqjV%2BQzf3%2BJytpr9gkIltnu1e0xGHS9g1cvFUFvoP7W%2FglbJ5q%2BwiYsFRYIp4f24uDoA179Z%2Fy%2FtoxAyqvczh6MgacLSngJwJ6I33&X-Amz-Signature=6d4a0daeeadb20bfb1663e5189cfd31247ff7a9500fe723976aaa49e6ecdb308&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YXK37HQ%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T062701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQDMEB8pD2WOrKduq6TekLl5WXpKxVnGtAilGSrQkQ6L0wIgPWcwt35LjWJXUTowT%2FvAdQ0%2F9J%2B4lE72LJcmUDjALSQq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDBxbUP0fDlEdPTKbOSrcA7KmgRFFxSz34%2Fyj3gx%2FSbQBEIG6cLvP0GQKvrTeN7dUJzmJ2M0BVz0jWaZWQwrWUmjAOS3imRRkaGkfHqRvAZdcLjW0GEzT42z7cm2fBgipKxQsKIkEE5BiiMgqE6j5xnckg7kj7dumig%2Bkg6ZiZj2aSMq%2FIYHpZfGNA60EIvWPLNZkdDEmWqZJ9FrSoSe79UNYd5vHAQ4MqaLBrgr4E1GAAQpS5exX%2BFJheVA8wtTBA9u8kWvoZB730zEmxV%2FxJXxdKSdTk6j3BmcgkisFMjc60srDIK%2BIQIg%2BHwtVE6a5%2BSBRr8pK%2BbrLCgKUY1XpbMbZZkxkMxMuSJgTBVfn9rT1VbEh2lowWfDIpMVYllC1EYX17k5Y7KrdxeTQj5X8ikZBGbz4v5S%2FTbij5binrp3ZngwU7TTBTdqouUltvNGogMeCELqTLzUYAHjBE9vL746n7SsPTRZ4LuHYYM0qRrOq5icdRkGmOkpEd7UEQsaVHm1Q7gm%2BJTYnsAsIa0Mg6edDtlDGM3oaPp4SoDLTKYrqIMLPjCPOz%2FqjLL0jU0DPspFl71dyGzRTeuFAiIQCc4m%2FyTZQQBDuaKXJ0Vx%2FiRLrTsEUfAsP%2BglnP2VhulfS4%2BWDrFl4wBA5hhriMMDdrcoGOqUBgn5c8qfVoFoRErkOUW5aN8WQqBcE6AAyMaWW%2FY0PU8oIrGXZeawlRfmYac4cyxancOiLmA%2FwIZxuG7Rw4FyTGtvzA8v9O60%2B3BUmkrD0qkQqE9y7efOO6IoJqjV%2BQzf3%2BJytpr9gkIltnu1e0xGHS9g1cvFUFvoP7W%2FglbJ5q%2BwiYsFRYIp4f24uDoA179Z%2Fy%2FtoxAyqvczh6MgacLSngJwJ6I33&X-Amz-Signature=df4188117690257eae33c5a2e39d32506117f546ff5651c6f1cadc948f155251&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







