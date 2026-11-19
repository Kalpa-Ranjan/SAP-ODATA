



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655GPTXP5%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T180534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDCH3jEwyLoPK9c5gqHQRTIfrMwa1IlCuSB9xTf0bbV9wIgPc1w0s27CFG4DW3ptDFzzvmKXDaBRftLbGJQXaiqi20q%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDD5c4TeQD8I35r%2BcHSrcA9NdUh2IV9B0hFsrhn6bfcWf%2BCVnpDnfIV1xvXP18JEL2wt1C9nM5ECebC84NOpn0VeMvvDbNRnYYd0W8EGBgZXrvnu%2BVWKptgKaJ%2BnuOo1JVyxxxxXxuURSOZ%2BG10fpYZ0B1xR2wq0b0YQ7MXwzgf5ZfVcMU67foTpSTJmNpbEUSHlAdej967osi9Wq9ZGPJI3FKu1R%2B51R3Sk3MLM3cq6SYDjNuaEptODcwoQDJ8xl8pIBj0EYU229z3kZVSp4UtIfJ2xBFirS08QkMhHuMTqC78EdHs%2Bdj7wn0iNQ0FiBVDe7YQ9P5cL%2FfnO9841LzVxtf1P54L3kUbr6jGSKRrkj2AtkSkpc%2B1e9nxDxg24iMHjrt4XX%2B6DEU7Vu0JQzA3VfaYh7Rpw0zjl50u8KdTxvZ1oCEJdkWYIwGNfggTZ11XlCCBvs03nAZcnD1zjG5tkOPQIJvVHLAAV6ZpuqppmnJFawcyvv701O6TXJiylr%2B5Jsyv1fHPHrrLSaNTTmJDd7c00mOCSTIdZ%2B%2B63S2Vf0jOLNvkorO5M1feW1HqhMC3IgZrv9O%2Fwmqb2Gs1WoxHa6wLJy63WtZk4OlW5W0qK0l6Iq5usLa5w9LJLqSJ0DFnuRxNFc3yK6OMKiMP6t%2FNcGOqUBAPhTL4SYuj7AyUzbPqsIHBbzk41II8jGrCxHQD8dyjtVXvNhm377SVTVSzNv5J8HZ30MumhLGrsksggmKrV1Cljktd5ds1XNI4fB8soUBW6ZiGW2%2FX1BHmxEwYSMs8kMjR3t%2FGDM7DHUrzyCGQO%2ByudJIS8GSrNbf%2BabxA7b7GhsYXVkYRH832jNDegfYsSxyAfwaPT56zwY0Ml3iv8bqUHdc8Jz&X-Amz-Signature=fa994081d93ce0b2db1ce934a3d2920b542652a2b360d3f9b8a6bcb376a1281a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655GPTXP5%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T180534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDCH3jEwyLoPK9c5gqHQRTIfrMwa1IlCuSB9xTf0bbV9wIgPc1w0s27CFG4DW3ptDFzzvmKXDaBRftLbGJQXaiqi20q%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDD5c4TeQD8I35r%2BcHSrcA9NdUh2IV9B0hFsrhn6bfcWf%2BCVnpDnfIV1xvXP18JEL2wt1C9nM5ECebC84NOpn0VeMvvDbNRnYYd0W8EGBgZXrvnu%2BVWKptgKaJ%2BnuOo1JVyxxxxXxuURSOZ%2BG10fpYZ0B1xR2wq0b0YQ7MXwzgf5ZfVcMU67foTpSTJmNpbEUSHlAdej967osi9Wq9ZGPJI3FKu1R%2B51R3Sk3MLM3cq6SYDjNuaEptODcwoQDJ8xl8pIBj0EYU229z3kZVSp4UtIfJ2xBFirS08QkMhHuMTqC78EdHs%2Bdj7wn0iNQ0FiBVDe7YQ9P5cL%2FfnO9841LzVxtf1P54L3kUbr6jGSKRrkj2AtkSkpc%2B1e9nxDxg24iMHjrt4XX%2B6DEU7Vu0JQzA3VfaYh7Rpw0zjl50u8KdTxvZ1oCEJdkWYIwGNfggTZ11XlCCBvs03nAZcnD1zjG5tkOPQIJvVHLAAV6ZpuqppmnJFawcyvv701O6TXJiylr%2B5Jsyv1fHPHrrLSaNTTmJDd7c00mOCSTIdZ%2B%2B63S2Vf0jOLNvkorO5M1feW1HqhMC3IgZrv9O%2Fwmqb2Gs1WoxHa6wLJy63WtZk4OlW5W0qK0l6Iq5usLa5w9LJLqSJ0DFnuRxNFc3yK6OMKiMP6t%2FNcGOqUBAPhTL4SYuj7AyUzbPqsIHBbzk41II8jGrCxHQD8dyjtVXvNhm377SVTVSzNv5J8HZ30MumhLGrsksggmKrV1Cljktd5ds1XNI4fB8soUBW6ZiGW2%2FX1BHmxEwYSMs8kMjR3t%2FGDM7DHUrzyCGQO%2ByudJIS8GSrNbf%2BabxA7b7GhsYXVkYRH832jNDegfYsSxyAfwaPT56zwY0Ml3iv8bqUHdc8Jz&X-Amz-Signature=9e648902826b78a440f5e384bfa457c39c683651e1d6ec85930a1d9dfa9ad9a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







