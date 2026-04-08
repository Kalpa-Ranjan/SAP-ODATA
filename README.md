



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYQLM52%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T131059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIQDcTY99Rjy1PLh2FKgum0xBG0%2FrF6ZFrxx43v9y%2BbYEQgIgHK7bqHGJWMgMcyWkdzLbisoCHQ8AZmMTrUz9z8vkxoQqiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMNzn0DFKpIDgEFXyrcA4iaJxDBAM%2FuiUTfp%2FGjN9OzL8b5zlDzd8P2Mkl1YW%2Fa8uL0WTWA10x1iPM%2BWa4Bla86fHNVeRuDLiKVm5Pfh%2Bs4tuAqytmdiN%2Fsuy3aPLhkhX2cFojUuaR5U%2Bod1EnnIkFBPmON%2BoAwwbPvXPH0wz3gQZ7W6yyPR3J9hwoU6YWtyJyLa01imgnXyU3hqZ0U5mWoKvTVoO55jCymKRHfgr0Gslu%2Bov10m8s0Jrrrqu8qqu%2B3aRgScdx2aGkXD5MaHGWSP2lSfFzYq4k4%2FXAV3V%2FtZZuqE9CcAz5M5fUJOTERLluOeyJpMTOhDFCN1MqrNNlyeUS%2FOfAMWfWlbXNK%2Brs6a10uM8ya06UPMLoFWlNDk%2Fria1kbGeW%2BQB%2FQZxJ0Lgg26eaC0UIGYayKSGtbNSvFPlZCen2h0f28CCSAuBQ7dSZGrCEFVWdJ4QfntodsaPKyr%2BqSJ8j%2F9WmMv2azsNI%2BwCeXSYrhrQwHbSWsrnvGVdVKI04T0DWzBsCcwQCIq5tVwwscVjsnQmjGE0rdjy9AyYEOyx5UFf%2BwR1f14OmjAdw%2FC1jxrvH3jRBTgwt%2BRdodewGl8i%2FgeFRzF0SgpEe7k6AkXnyOEYCEz2187OObt3TxALTn6%2BnRLTaDMICZ2c4GOqUBDbNcF98aK3B4wXWlOkxcp63j8Pse9zcj%2FmBOZF00vV0KBYHDCf9t6nSiSfkmitZJGC6MLGu4O2AXlQSzSuRqFyRFX47Z2Uijnd4iGQYBMknPpg1nvI2KcldD1zCUJIknCNMU8K%2BrECNz89XgLlpu0yWutcdJwoPMfFQIAuMYlSkPVa99c2x4a9bOwcKqGFUTodKDjTOne6dpAWDzKLKhDYouF%2BX0&X-Amz-Signature=d16ec6bea127c2f7159d92a0bdd2e1243fd7e8bfcb0073498b78f332fc961013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYQLM52%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T131100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIQDcTY99Rjy1PLh2FKgum0xBG0%2FrF6ZFrxx43v9y%2BbYEQgIgHK7bqHGJWMgMcyWkdzLbisoCHQ8AZmMTrUz9z8vkxoQqiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMNzn0DFKpIDgEFXyrcA4iaJxDBAM%2FuiUTfp%2FGjN9OzL8b5zlDzd8P2Mkl1YW%2Fa8uL0WTWA10x1iPM%2BWa4Bla86fHNVeRuDLiKVm5Pfh%2Bs4tuAqytmdiN%2Fsuy3aPLhkhX2cFojUuaR5U%2Bod1EnnIkFBPmON%2BoAwwbPvXPH0wz3gQZ7W6yyPR3J9hwoU6YWtyJyLa01imgnXyU3hqZ0U5mWoKvTVoO55jCymKRHfgr0Gslu%2Bov10m8s0Jrrrqu8qqu%2B3aRgScdx2aGkXD5MaHGWSP2lSfFzYq4k4%2FXAV3V%2FtZZuqE9CcAz5M5fUJOTERLluOeyJpMTOhDFCN1MqrNNlyeUS%2FOfAMWfWlbXNK%2Brs6a10uM8ya06UPMLoFWlNDk%2Fria1kbGeW%2BQB%2FQZxJ0Lgg26eaC0UIGYayKSGtbNSvFPlZCen2h0f28CCSAuBQ7dSZGrCEFVWdJ4QfntodsaPKyr%2BqSJ8j%2F9WmMv2azsNI%2BwCeXSYrhrQwHbSWsrnvGVdVKI04T0DWzBsCcwQCIq5tVwwscVjsnQmjGE0rdjy9AyYEOyx5UFf%2BwR1f14OmjAdw%2FC1jxrvH3jRBTgwt%2BRdodewGl8i%2FgeFRzF0SgpEe7k6AkXnyOEYCEz2187OObt3TxALTn6%2BnRLTaDMICZ2c4GOqUBDbNcF98aK3B4wXWlOkxcp63j8Pse9zcj%2FmBOZF00vV0KBYHDCf9t6nSiSfkmitZJGC6MLGu4O2AXlQSzSuRqFyRFX47Z2Uijnd4iGQYBMknPpg1nvI2KcldD1zCUJIknCNMU8K%2BrECNz89XgLlpu0yWutcdJwoPMfFQIAuMYlSkPVa99c2x4a9bOwcKqGFUTodKDjTOne6dpAWDzKLKhDYouF%2BX0&X-Amz-Signature=7798a1ce3e30b86701d7cac0016276f71425936bed794ed5fb0ccc81d63c01fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







