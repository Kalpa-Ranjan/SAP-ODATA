



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZU7DYU2%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T135047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBYRcBmKGNUI%2B3WXlgRPAs4uAcdiPw81iLIbZhiLsUkgIgFgqcZ3NHS8z3AE4rl0OsgDVqThdHA%2FxIu2%2F0Z%2BGuxC4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYWUnZHCMQdQMmrXCrcAw%2FVesTVeUhZjgOzE5nlQ0GMgrjrVDY6Vjn4AVC6LVRovp14YG3zbYiXelAJ6eCCTdLU%2FAZivYs3PZojHQDHHGzMHXEXjZoEvd8Bt8Rd0MClaupgrx%2Blf4aJc5ySAw1TMCNZ%2B5ZVr1sCq9sthSdGJrFWToTZKtqZsvSffZeh50znAKu9jiaAOOP3%2Fv9AMWXK8wd1c5UztJNvZ8qGXgQ14ezQG2bB1VeJIOjc7w8ROkrLDfWyXre61sS1mt8cgIcol2MjQG30nAzHyzNEcrHaVBj95NSl1uvTECiQmIPtp8xcYNHgB9uCcdc249gnRqFs9eVxyw5V9BEJYF%2Fe9GrUQJha8f%2FKjZr3EVpqGCzLY5mndZnMH0PlN1DmtS8tMdzpoNlCIMLyrBSNGcbWJll8NN8ed74gb8KlFz791wsMOvOhN9uG7z8nkt%2FD7ZVw3ffnIuGfT2sON5KdDfJWTdT1%2F4oI6Ft6iRq8TbQf7sinGJDOCikqQwBAAtY8DNjt1zXwMldav09wbv0fsHGVQia1dTGf646e%2BQPI0AkNmjl%2BQCqlbBm%2BKI6h83sqQ5sL1SFvPFbSKfBIJ4sJM4EKEGpuy8eER%2BiwCTiIUog%2FnGRwK57iJvXxsUwhkZlH%2BV7IMMumudIGOqUBttd6b5us689LNGGQ5nKtM7tjwFnM4Dc23%2BjpQKe1is1EJ10yowpi4TglAc33HiDFddCn1hs6%2BJw6I7MMuUC0HbkFebtYeZu99NaSTTaMk5qZ%2Fs8NOnjBwXT%2Fr5UOTS1CM%2FidCPX8xT1hAm0tk5lvUOvbtXo%2FXsjZEySKMY0LJUljmxoC05O5lmGdPdR%2B6kXBW3lO%2BBPYQMWga69M7prrt0qrddTP&X-Amz-Signature=d2d9e21476c8adea696746aec72b558cdfee9b8dee76cd970e5fe37368f5b7b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZU7DYU2%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T135047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBYRcBmKGNUI%2B3WXlgRPAs4uAcdiPw81iLIbZhiLsUkgIgFgqcZ3NHS8z3AE4rl0OsgDVqThdHA%2FxIu2%2F0Z%2BGuxC4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYWUnZHCMQdQMmrXCrcAw%2FVesTVeUhZjgOzE5nlQ0GMgrjrVDY6Vjn4AVC6LVRovp14YG3zbYiXelAJ6eCCTdLU%2FAZivYs3PZojHQDHHGzMHXEXjZoEvd8Bt8Rd0MClaupgrx%2Blf4aJc5ySAw1TMCNZ%2B5ZVr1sCq9sthSdGJrFWToTZKtqZsvSffZeh50znAKu9jiaAOOP3%2Fv9AMWXK8wd1c5UztJNvZ8qGXgQ14ezQG2bB1VeJIOjc7w8ROkrLDfWyXre61sS1mt8cgIcol2MjQG30nAzHyzNEcrHaVBj95NSl1uvTECiQmIPtp8xcYNHgB9uCcdc249gnRqFs9eVxyw5V9BEJYF%2Fe9GrUQJha8f%2FKjZr3EVpqGCzLY5mndZnMH0PlN1DmtS8tMdzpoNlCIMLyrBSNGcbWJll8NN8ed74gb8KlFz791wsMOvOhN9uG7z8nkt%2FD7ZVw3ffnIuGfT2sON5KdDfJWTdT1%2F4oI6Ft6iRq8TbQf7sinGJDOCikqQwBAAtY8DNjt1zXwMldav09wbv0fsHGVQia1dTGf646e%2BQPI0AkNmjl%2BQCqlbBm%2BKI6h83sqQ5sL1SFvPFbSKfBIJ4sJM4EKEGpuy8eER%2BiwCTiIUog%2FnGRwK57iJvXxsUwhkZlH%2BV7IMMumudIGOqUBttd6b5us689LNGGQ5nKtM7tjwFnM4Dc23%2BjpQKe1is1EJ10yowpi4TglAc33HiDFddCn1hs6%2BJw6I7MMuUC0HbkFebtYeZu99NaSTTaMk5qZ%2Fs8NOnjBwXT%2Fr5UOTS1CM%2FidCPX8xT1hAm0tk5lvUOvbtXo%2FXsjZEySKMY0LJUljmxoC05O5lmGdPdR%2B6kXBW3lO%2BBPYQMWga69M7prrt0qrddTP&X-Amz-Signature=7e39864bc18cb7212968ebaa2ed4cf09a71314a9e5dcc099677903f7fc82ed65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







