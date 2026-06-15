



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5W74EJ%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBROndMsrg87FRvKrY41%2BV8ZhHlBOE8tm28fIvKiNN65AiAXocwTxigIVRTauS3nWhyweUf%2BsmAO%2BwhW%2BERGoc%2FCCCr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMhd%2BYISLP6SkrwxpEKtwDOFhN8hEfqKUCOyLAn0%2FBE7yyzxllczGXB0jqO6jxvFr0eTEB1Lh2rXq08vSUBvxxFmWmwfVgPQt86XJuCcafBWGjRpantuh5NpxXHoCn5V%2BdOryBLJhYLVZf24SzTqD%2FZr6OTTNkQOWUz%2FxNrnBwGgofDj4gBnirJJpx69otyUmCW3WS1IK%2FEIR%2FLIl0v9ndFVo1jyyy7ZY%2F3VfK95z3b5xewj4YMtKfQ7FRtWRW1rq2dQ%2B22Jqhn8ENTT9j28buk7UpecR9cHpXWFTb3R3kwW1%2Bivnv9BUw4wYtp4tIW3GpEMDd4bRgV8gaEp3NeFfFgWAh7oZgjUDTuexA01YAiUbnTJkb3RhKKbJ5H%2BwMZ7taxODQRdUU00LPjGS%2B8aA0n7k7AtPjiS9VgdM7Ct8LqcT6CtjdM1S0ysuUf2BR3L%2F30ADmbIMgb0o0rAru0GOuCBdF9Bn4A7x9I8k8GTzQQEd9mdk0SqLdcalmsebJdwaF0XIbYQz5l6IKRj6uuf4wzxM%2BPQJq4nAVLvEDnap%2BXN4K8fbJYpHvw2m59SFgAp%2BHBVtphz9xfCw12e5LBGnpzCNIbSdAKGX2fgkpGsEaCk72Ubh5OVMFPm1kU0eD1k3AOouWo9zUw5sdAUow2bK90QY6pgHv4Wi5E0EmghOewDvB1J4Exe%2ByIzhp1LdqxL94sBuAxKObRY3tAmVxfB99XauGIU%2BnaeSOcFf8LggXhqc95qLEUtobEIQKZtFS1kASQXAX01OrwDvPVCyq%2F47XN1RZzWerI2Yxr%2F3qsLYA8yRYoJoqsOZ7%2BfNwwYK%2BJQC%2Bs7SeZDe5y9yifwT0irbEvh74OlZkYfJs11gnxBSC15VcUs%2FhbqvVR3wL&X-Amz-Signature=5c6e69aeac0e7c9b9a68005a581cc431013888e9f2ee55235a12eee20f0b8fa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5W74EJ%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBROndMsrg87FRvKrY41%2BV8ZhHlBOE8tm28fIvKiNN65AiAXocwTxigIVRTauS3nWhyweUf%2BsmAO%2BwhW%2BERGoc%2FCCCr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMhd%2BYISLP6SkrwxpEKtwDOFhN8hEfqKUCOyLAn0%2FBE7yyzxllczGXB0jqO6jxvFr0eTEB1Lh2rXq08vSUBvxxFmWmwfVgPQt86XJuCcafBWGjRpantuh5NpxXHoCn5V%2BdOryBLJhYLVZf24SzTqD%2FZr6OTTNkQOWUz%2FxNrnBwGgofDj4gBnirJJpx69otyUmCW3WS1IK%2FEIR%2FLIl0v9ndFVo1jyyy7ZY%2F3VfK95z3b5xewj4YMtKfQ7FRtWRW1rq2dQ%2B22Jqhn8ENTT9j28buk7UpecR9cHpXWFTb3R3kwW1%2Bivnv9BUw4wYtp4tIW3GpEMDd4bRgV8gaEp3NeFfFgWAh7oZgjUDTuexA01YAiUbnTJkb3RhKKbJ5H%2BwMZ7taxODQRdUU00LPjGS%2B8aA0n7k7AtPjiS9VgdM7Ct8LqcT6CtjdM1S0ysuUf2BR3L%2F30ADmbIMgb0o0rAru0GOuCBdF9Bn4A7x9I8k8GTzQQEd9mdk0SqLdcalmsebJdwaF0XIbYQz5l6IKRj6uuf4wzxM%2BPQJq4nAVLvEDnap%2BXN4K8fbJYpHvw2m59SFgAp%2BHBVtphz9xfCw12e5LBGnpzCNIbSdAKGX2fgkpGsEaCk72Ubh5OVMFPm1kU0eD1k3AOouWo9zUw5sdAUow2bK90QY6pgHv4Wi5E0EmghOewDvB1J4Exe%2ByIzhp1LdqxL94sBuAxKObRY3tAmVxfB99XauGIU%2BnaeSOcFf8LggXhqc95qLEUtobEIQKZtFS1kASQXAX01OrwDvPVCyq%2F47XN1RZzWerI2Yxr%2F3qsLYA8yRYoJoqsOZ7%2BfNwwYK%2BJQC%2Bs7SeZDe5y9yifwT0irbEvh74OlZkYfJs11gnxBSC15VcUs%2FhbqvVR3wL&X-Amz-Signature=1793630168ef9bb0b468dd8ddef35641096bc066c9dac2a3a17f6c69276bedfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







