



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWVJXNRE%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T194308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAIZAnT%2FQ7xT9CdzwecmI9J7oAA4Auxkbiz1oLSX6PDRAiAsdJWr0rGpdzA2dmzrQfbzTQoGrnawFoP%2BGnaGOu2NuSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMTgq6becd51JgXh83KtwDoW5qP4a%2BCXHGGEDh0yDKDG%2F833WiLwAfakbXvpsDPeX4DuTLBv7Js1l5Yzkh3pHcUvOM6Rf7HDzcdE9vtWfVqh0LzgqCz%2FdGsXp%2Fpgjsa4z%2F8QtZ1oA2n9bTBIj%2BZcPoQJRzzD6zBaVyPk54sMDPpWblIW0M72tToxm8s4mWV5dJ%2Bs8demAjMpKJFjR1EXNCGw8DsBfpAIarRt9oX2lfTBUQmdycsmgt7PovhgxgFiSC9NUaKQeF0ujAHJ2tNcuO7%2BJzPrctR%2BnaU2TidDTyGY%2B0S4ui5BnPc6rQe2W%2F22shF1R%2BtVQLu7Aq4jhL%2BREG2YXasvjlrVAcP5xMSYzxBMXimXUeWDAP4tBKigray5ix4jid%2BjFllCKWWRMyf33RWuJ98iROOwadTpi3gGbF9yUwcSFdK3V2Em65jSZYgkl8p%2BDLJP%2BIG3EuLMgOUfxXsTkvK3MUi%2Bp7qpvZcB1Xy9RJd7FmrQhD4Evq%2BEqsBjqgoT%2BoHPa9Xalxus6mcMttO9s7lbF%2BfQMeTtdCvi6k2xjDx71e8xs8R6P3MVlxNjH7Y%2BQPzBzffLI33u6hXxARXuBhEBL%2FAJR%2FCR6oidojs1Jz5itZoQ%2BO3g4bCTvLOroNqf8mVYqq5goIdKUw7P%2BN0AY6pgF7CqwSYUwCIbul5fDzImfJXryoBbfEHy99IFmoOQKyCaVSGnok9IGkWuWYMuZo%2F%2F%2Ft9TMUEUrT%2Bt7H48i8Mb3UUH4gCjH5jba3ykAf2M6VGUPQQnjiErcPzrhmcm8NeGT%2Fdv8l9Buiq2SLIT45uDqzqEmV2L4WlPMPv4VcP8XBSBxsLlbtz5qpvkSUvYOWsuwOKbII9i0wzeklI3M1CBwnw02AqF1B&X-Amz-Signature=112c3576a4f6a9901a7e259664d3adc61a5d59f1f91ffea5ad63c9a646c318db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWVJXNRE%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T194308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAIZAnT%2FQ7xT9CdzwecmI9J7oAA4Auxkbiz1oLSX6PDRAiAsdJWr0rGpdzA2dmzrQfbzTQoGrnawFoP%2BGnaGOu2NuSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMTgq6becd51JgXh83KtwDoW5qP4a%2BCXHGGEDh0yDKDG%2F833WiLwAfakbXvpsDPeX4DuTLBv7Js1l5Yzkh3pHcUvOM6Rf7HDzcdE9vtWfVqh0LzgqCz%2FdGsXp%2Fpgjsa4z%2F8QtZ1oA2n9bTBIj%2BZcPoQJRzzD6zBaVyPk54sMDPpWblIW0M72tToxm8s4mWV5dJ%2Bs8demAjMpKJFjR1EXNCGw8DsBfpAIarRt9oX2lfTBUQmdycsmgt7PovhgxgFiSC9NUaKQeF0ujAHJ2tNcuO7%2BJzPrctR%2BnaU2TidDTyGY%2B0S4ui5BnPc6rQe2W%2F22shF1R%2BtVQLu7Aq4jhL%2BREG2YXasvjlrVAcP5xMSYzxBMXimXUeWDAP4tBKigray5ix4jid%2BjFllCKWWRMyf33RWuJ98iROOwadTpi3gGbF9yUwcSFdK3V2Em65jSZYgkl8p%2BDLJP%2BIG3EuLMgOUfxXsTkvK3MUi%2Bp7qpvZcB1Xy9RJd7FmrQhD4Evq%2BEqsBjqgoT%2BoHPa9Xalxus6mcMttO9s7lbF%2BfQMeTtdCvi6k2xjDx71e8xs8R6P3MVlxNjH7Y%2BQPzBzffLI33u6hXxARXuBhEBL%2FAJR%2FCR6oidojs1Jz5itZoQ%2BO3g4bCTvLOroNqf8mVYqq5goIdKUw7P%2BN0AY6pgF7CqwSYUwCIbul5fDzImfJXryoBbfEHy99IFmoOQKyCaVSGnok9IGkWuWYMuZo%2F%2F%2Ft9TMUEUrT%2Bt7H48i8Mb3UUH4gCjH5jba3ykAf2M6VGUPQQnjiErcPzrhmcm8NeGT%2Fdv8l9Buiq2SLIT45uDqzqEmV2L4WlPMPv4VcP8XBSBxsLlbtz5qpvkSUvYOWsuwOKbII9i0wzeklI3M1CBwnw02AqF1B&X-Amz-Signature=9e03ab5ce2bc69c8362308c2bcae0e357db54ab3ac2fc7e1c8f458d551dd45d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







