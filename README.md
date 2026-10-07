



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OG3ZCDE%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T181007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGcjMxxTXkSMItZGLJHat2gLqqJNaEuEylThzzJ3pfczAiEAzX1%2BxgWFYjylPtK2sHjaq%2Fh9NkcE7iPQ05jpUSd2TW8q%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDKnz7VodXNbv%2FEN2sSrcA64xphLLqJu4oPy1oVq6oxT2R36hwmha554v9NaqYbe4EOIJWo1r%2FOVVpKILIOOsI8LgzUSI2T%2BFbPF6cQmOn3mmkOg088YOkbKpzwsloEMqvLyHNTvXr%2ByK%2BAPKaiP%2BHmQdFD9D%2BuP4v2ZJztpNPbMitYyHi7DdLufJEBb1FN9MDlrUGwRshcsA1P2UrFSuKk5PbKqF60jk%2BtKamdkvRNyrjPn1tY%2B8imDyp86SXkmPmpLq2fYNxnoPZDFVuu8mg%2BHQKDx8rESX3GsWv0ago%2FNmOtAAs%2FVf3TffJrJgoL9RHxaPr5Y3tA8mM8Z%2FQ8lX0bIop8zN4xVCGizKhV2XGv7GaguYSb45JmUpbNfSzucgaMNBCgPEK8QFI2YsytJBL7r0bGcHoB7VBBiplXTGixekqCXAFgvUqz5ZvRvqIr%2BVXAlnQ90pM0Ypf5hLuQL%2FLTju%2F6%2FJO2kEmXhxilMLG70O%2FmEqmqHFTBP2quljH6RsG%2F7ZzkkIInpUiqQuwWK3cQSTNQduqejuvYpfTK0s89dBb6pSLfEjmTfwyhThM7XexWY1eTV%2B4Z%2F6AizIRjewhgGs1%2FE34zOtZm8TUYUKbJCeRc01P0kZycu1diqNj%2Fj5LjFUHnPOpWTTMMYIMJf0mdYGOqUB%2BcuHTZ90NP9TTDxHhyMk2xyBwOxxsWKjni9pk%2B8rgD7JGzAe5L3Me5ICJP6imNG1%2BAB5tueHr%2F6tN9NplZCc6R9UIbZxTIyYJpdWdNBdBf%2BrB2Kz8IthM3nbND56%2FAMSt3bW9PgzkgMTq6S6SrthDnTbH8XE03oApaq9WSJlnoYGX3uMLdcUGKZAh9iQR%2FI9J8e9MHNaUGK3bmZFhz2kcEGuAd6P&X-Amz-Signature=5595ca2b1b44e32dfad60d8b6ee6b4fe751943079a341e9908932d3d095663a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OG3ZCDE%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T181007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGcjMxxTXkSMItZGLJHat2gLqqJNaEuEylThzzJ3pfczAiEAzX1%2BxgWFYjylPtK2sHjaq%2Fh9NkcE7iPQ05jpUSd2TW8q%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDKnz7VodXNbv%2FEN2sSrcA64xphLLqJu4oPy1oVq6oxT2R36hwmha554v9NaqYbe4EOIJWo1r%2FOVVpKILIOOsI8LgzUSI2T%2BFbPF6cQmOn3mmkOg088YOkbKpzwsloEMqvLyHNTvXr%2ByK%2BAPKaiP%2BHmQdFD9D%2BuP4v2ZJztpNPbMitYyHi7DdLufJEBb1FN9MDlrUGwRshcsA1P2UrFSuKk5PbKqF60jk%2BtKamdkvRNyrjPn1tY%2B8imDyp86SXkmPmpLq2fYNxnoPZDFVuu8mg%2BHQKDx8rESX3GsWv0ago%2FNmOtAAs%2FVf3TffJrJgoL9RHxaPr5Y3tA8mM8Z%2FQ8lX0bIop8zN4xVCGizKhV2XGv7GaguYSb45JmUpbNfSzucgaMNBCgPEK8QFI2YsytJBL7r0bGcHoB7VBBiplXTGixekqCXAFgvUqz5ZvRvqIr%2BVXAlnQ90pM0Ypf5hLuQL%2FLTju%2F6%2FJO2kEmXhxilMLG70O%2FmEqmqHFTBP2quljH6RsG%2F7ZzkkIInpUiqQuwWK3cQSTNQduqejuvYpfTK0s89dBb6pSLfEjmTfwyhThM7XexWY1eTV%2B4Z%2F6AizIRjewhgGs1%2FE34zOtZm8TUYUKbJCeRc01P0kZycu1diqNj%2Fj5LjFUHnPOpWTTMMYIMJf0mdYGOqUB%2BcuHTZ90NP9TTDxHhyMk2xyBwOxxsWKjni9pk%2B8rgD7JGzAe5L3Me5ICJP6imNG1%2BAB5tueHr%2F6tN9NplZCc6R9UIbZxTIyYJpdWdNBdBf%2BrB2Kz8IthM3nbND56%2FAMSt3bW9PgzkgMTq6S6SrthDnTbH8XE03oApaq9WSJlnoYGX3uMLdcUGKZAh9iQR%2FI9J8e9MHNaUGK3bmZFhz2kcEGuAd6P&X-Amz-Signature=d1a0971d4f286dd01f55df2777c380d0d6a4aec5d95ed25aca7ac8ba73f5994d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







