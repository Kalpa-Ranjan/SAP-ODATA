



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636PAWTPK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T062512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIB6UoXG4mgF8fkqh5btFQxjJ1%2BdXTstF38tH%2BCnLokm8AiEA%2BX16ENEkC0gm%2BOPie5JXCuukVNVcAT14nexuIk7z%2B7wq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNveWXEPi0gNhd%2B5HyrcA01Vy2CM7w9in9sh8nBMcAHANqka1dwePhicqm1UijFAFHUHQVsA4b5XR8ie0B8%2Fdd6TnTBbHP4cedmtPyd5UjObZ5v4GqFlL%2BgCp9vyjiGGS7Ov6akDLXM0w0ARjZUW32%2Fj8q3th48liXHKHVYZ%2F83CUJhTxNFgejZNVBAJaJUv1PaeJr1YovWWRfIjtGvkEl%2BnW1hvIzxP9vbPyvtoLBGWaYCbM1DSljgIXPN0cwWOOj7mVqCrIW5j76k2nDM0yRGTj4EHXmnZMWpbHWIX2r7UwXmyLU4GtlTUBXHMa73HWiY68ZG8jYykQNbXcJQqur9PtVxWixoL87e02AYQjEvLY%2F8OFj7d%2Bed0PSxEMpzCBwm%2Fvd%2FjUlWS9lYm6hJ%2FJZXa7HAVyhXa0ednA45C3DTKeIK3S9yHkikKV7MlzJ5B065WZ4ap8qU4k27i4yzZj0xd4%2BZ05xwKtyCFmDhygpkMii4HCHgVXcHdUgAQ2Kuf48yLDDfvfscVc8eHV7jdhe7rhVKBhN5ZOwlFZ%2FlLo9ijHVv%2Bp9GWvF1PvSTd2zIRw9UlA%2FNHX%2B%2Bvid4Oj5XQY4zhFhzbEOBSrVm3JcjA7t7BpUm7QJHjfnk8PyB9hInhDWYg6c9PjRFMmaU2MPrg1ssGOqUBfPg1dBNb8ZcjmlEwMLkHALbctU3B1zcHzstWz6wE84qjM21Ja%2FsgYHPT%2FEQPTy4acrxKVy%2BrmHR4VzrRHGmtVUNWXqE%2BliF5bj4rN7zeJliIZ%2FuwigsD7KAVOgQe%2BD2VXLCtFY962GrriPZEywLKfFX%2BBONswR%2FRuABPC%2BajLT5eqn%2B1AKPORBXAbwaoWfgsuVQEW%2B4ny21JEErTUJNu4uH6Ueo2&X-Amz-Signature=a4ead7c6d5815cc8d5b91fbf88d1951c23bb01dbbc32a343804f56bf7b9de3fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636PAWTPK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T062513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIB6UoXG4mgF8fkqh5btFQxjJ1%2BdXTstF38tH%2BCnLokm8AiEA%2BX16ENEkC0gm%2BOPie5JXCuukVNVcAT14nexuIk7z%2B7wq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNveWXEPi0gNhd%2B5HyrcA01Vy2CM7w9in9sh8nBMcAHANqka1dwePhicqm1UijFAFHUHQVsA4b5XR8ie0B8%2Fdd6TnTBbHP4cedmtPyd5UjObZ5v4GqFlL%2BgCp9vyjiGGS7Ov6akDLXM0w0ARjZUW32%2Fj8q3th48liXHKHVYZ%2F83CUJhTxNFgejZNVBAJaJUv1PaeJr1YovWWRfIjtGvkEl%2BnW1hvIzxP9vbPyvtoLBGWaYCbM1DSljgIXPN0cwWOOj7mVqCrIW5j76k2nDM0yRGTj4EHXmnZMWpbHWIX2r7UwXmyLU4GtlTUBXHMa73HWiY68ZG8jYykQNbXcJQqur9PtVxWixoL87e02AYQjEvLY%2F8OFj7d%2Bed0PSxEMpzCBwm%2Fvd%2FjUlWS9lYm6hJ%2FJZXa7HAVyhXa0ednA45C3DTKeIK3S9yHkikKV7MlzJ5B065WZ4ap8qU4k27i4yzZj0xd4%2BZ05xwKtyCFmDhygpkMii4HCHgVXcHdUgAQ2Kuf48yLDDfvfscVc8eHV7jdhe7rhVKBhN5ZOwlFZ%2FlLo9ijHVv%2Bp9GWvF1PvSTd2zIRw9UlA%2FNHX%2B%2Bvid4Oj5XQY4zhFhzbEOBSrVm3JcjA7t7BpUm7QJHjfnk8PyB9hInhDWYg6c9PjRFMmaU2MPrg1ssGOqUBfPg1dBNb8ZcjmlEwMLkHALbctU3B1zcHzstWz6wE84qjM21Ja%2FsgYHPT%2FEQPTy4acrxKVy%2BrmHR4VzrRHGmtVUNWXqE%2BliF5bj4rN7zeJliIZ%2FuwigsD7KAVOgQe%2BD2VXLCtFY962GrriPZEywLKfFX%2BBONswR%2FRuABPC%2BajLT5eqn%2B1AKPORBXAbwaoWfgsuVQEW%2B4ny21JEErTUJNu4uH6Ueo2&X-Amz-Signature=a53ddd1613657167dfd688bddac63f1993c86e3bc79edd709e3d1bae6b1898ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







