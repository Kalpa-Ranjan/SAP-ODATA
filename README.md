



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VRLQ6EG%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T061233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC5HOeQf65jc5WkvKZYcZD5mV8zXh9aY9TcvI2YV%2BXyPAiAvTpgm0uqxd6ghQQegrreC7QjMS11u1ZwoH6%2FDoTD7%2Fyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMY%2FYmtiAK1T4ZgHufKtwDF0TXk8rrP3ayz1LRKUhTUqFg5hnFJbiwnHxVJJwgVD26b3H5ICny6EV6V2WsCMu3pSbQBUtygZTH1qC4wP9Mfic2CXoqNqVCnXofvanysOL4f04PXFNee7jqPattW5LV7CPHG%2BDtSRsWV8DPoRfP1OEucdnuBDuR4bAhdmYm6yPAgn3hJL9NTIhOp%2BRkGDyFYUn35oxTjlG7oF3j1atzz5xASV6GLDfFEEYWOnqP4KBgd17OXn115yX2%2BEIYyRP3782URBVuEUL0qcfG7D6pxNEHIYQfgzJfMeY1FYGNUX5ltV8wPPCrFTndI5Rthgs7IDPFqGJD7U8d%2FUyeT349DyIYE0%2FA0ewAbUTNeUem28QBt%2B8twm6HDMDylEjABjtNpHsaVYMf0PP5EBCHvBMkSWV7JFcYNiDp949CYIgkZfoabWxmX%2F7bKPFJm4Yt7reUcPW%2FgtHQpuQL426lLNy8N8nMASeKcopwr6xKdBtuU2TVcnp6tOFgyNXXo798kAM54tb1F%2F%2F3TJWKDPEgp3NxTjzahzRjwwnFh1J%2BaInAM4JsSU56PuAftA8sS0lPjH6Iup8TTWrCIjBVBEKm9VOGJ%2BWIBoLnchcAvyem7qWAigc%2BAJpNPyoJ%2FQiiyBAwodDm1gY6pgE2MvShVdUio3V8HXGsYRY3Ka00w%2B%2FpbwOdBlwLNI13DpvLmBbwCfJEuG4KX2t8KxVAdIufok%2Fsu2wMsXcKUZE%2FL%2FiR7ZZtmgxB7ffLja8Zje1P1kY89ux0vzDOvcsxKFSxxKsRxk9jjb5EDoYA%2FMjcRijd4z5HXpAYvsHfcbvdIZwKNukeaqceNUjhbKw%2FhM8oPTowzMiEwGDWESRMALx%2B6Y7Ng49z&X-Amz-Signature=6e28bfd97e2d6dc887a2ec492d9cd439e270dc6bdb99e460ae5e9efd0f6467d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VRLQ6EG%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T061233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC5HOeQf65jc5WkvKZYcZD5mV8zXh9aY9TcvI2YV%2BXyPAiAvTpgm0uqxd6ghQQegrreC7QjMS11u1ZwoH6%2FDoTD7%2Fyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMY%2FYmtiAK1T4ZgHufKtwDF0TXk8rrP3ayz1LRKUhTUqFg5hnFJbiwnHxVJJwgVD26b3H5ICny6EV6V2WsCMu3pSbQBUtygZTH1qC4wP9Mfic2CXoqNqVCnXofvanysOL4f04PXFNee7jqPattW5LV7CPHG%2BDtSRsWV8DPoRfP1OEucdnuBDuR4bAhdmYm6yPAgn3hJL9NTIhOp%2BRkGDyFYUn35oxTjlG7oF3j1atzz5xASV6GLDfFEEYWOnqP4KBgd17OXn115yX2%2BEIYyRP3782URBVuEUL0qcfG7D6pxNEHIYQfgzJfMeY1FYGNUX5ltV8wPPCrFTndI5Rthgs7IDPFqGJD7U8d%2FUyeT349DyIYE0%2FA0ewAbUTNeUem28QBt%2B8twm6HDMDylEjABjtNpHsaVYMf0PP5EBCHvBMkSWV7JFcYNiDp949CYIgkZfoabWxmX%2F7bKPFJm4Yt7reUcPW%2FgtHQpuQL426lLNy8N8nMASeKcopwr6xKdBtuU2TVcnp6tOFgyNXXo798kAM54tb1F%2F%2F3TJWKDPEgp3NxTjzahzRjwwnFh1J%2BaInAM4JsSU56PuAftA8sS0lPjH6Iup8TTWrCIjBVBEKm9VOGJ%2BWIBoLnchcAvyem7qWAigc%2BAJpNPyoJ%2FQiiyBAwodDm1gY6pgE2MvShVdUio3V8HXGsYRY3Ka00w%2B%2FpbwOdBlwLNI13DpvLmBbwCfJEuG4KX2t8KxVAdIufok%2Fsu2wMsXcKUZE%2FL%2FiR7ZZtmgxB7ffLja8Zje1P1kY89ux0vzDOvcsxKFSxxKsRxk9jjb5EDoYA%2FMjcRijd4z5HXpAYvsHfcbvdIZwKNukeaqceNUjhbKw%2FhM8oPTowzMiEwGDWESRMALx%2B6Y7Ng49z&X-Amz-Signature=00eceed077e1716b4be15afaf6798a712c4ce5b5a88d9f844b608b2c9a23f2fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







