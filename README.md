



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZNCEMBT%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T145410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIHnwniuoHEGeLJnK%2FOSo0PBUvNbgdTxIDWlM2DPexhLgAiBnZx9PYhDE0ynv%2F3Eu7Wfn40J3SWfhuNot1uXeW3V9Zir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMWG6iQE%2BGoOZG0yXjKtwDf9bZcidqrliqZev5HVWfxhx731oRiIG2W0ubPOmHIQ1HGYRY%2FSDyOFRYRWe6wxfApSU3SQM3lCWJvY9H4%2BNRZvTgIvNBLEfFsiTx%2FRta%2BEzMu6v08ijDyKXOxhbvdqpMy4NXvY2jbLRb4cLRbYfxGgYVDdzi1Rd6lO%2BYNAlZvs7hRSxMonDPffOtBMRXoEd96YQLHg%2BtFASiMdmxSBGerqtxuAGgkhRkwHmb9aHTficbcToEzC3zcCjSZ%2BRhF%2B6Ew2Ogfw3GemTo1elWCbpPdJhdk6gR8vCSXPN5zeLe9%2FIRYIrzJi74Hs6dop5my%2F%2BwjxZz91SR3lO%2BzFe0LYtk%2FdVWavFHPY33CZ9k4FxICvmiPCQ39ikFXQu4iH51yWim2zV19CM05uQwEjV8JObPm7ix7Q3W0j8HnAjT1KCJeMhJ4%2FXSEyLmXKtxULzV9fpNzrz%2Bj6nHFR3NdPkFmDOYMoLDLPctWXoPEZQbH8janTtvQwF%2FbJ%2BVGKU%2BAjBWF4SIHpmVGPYh%2FiIEjhW5zMJdGwo9NATCIeiGjL%2BjvRL71fJAL6Jd64NT7UARet2UdI6bkMHUQcpQ7f01n5BUAT1XIrjmn6%2BJLzwi9HugszYMXNbcaaJqGje6t7MEN%2F0wjPq70AY6pgHiozwSdKZm4PFlhkMuuhGaxq%2BdbGTOoFt8lAnBifQTwOKciNVGxcgH15Vf3cXcge8%2FRczQCTHtJcxJWoC1vAbWGt8aS7ykpdOboRkGbffXW6YnKlpVn5%2FyZEPtg1VhkksyhWfvJCIbIq8JhsldTgUgJjU6NL027WjKeRA9Rf27pmTxKkrXhtkXNTevDh7pOL5H%2BDrbUJJejqSBV%2FkDxgfRiq%2BCEDxd&X-Amz-Signature=90e5f680e0bae438ef0524afb5a9ad6193b37ef1cb682d6008aa6dd86c2f4c13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZNCEMBT%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T145411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIHnwniuoHEGeLJnK%2FOSo0PBUvNbgdTxIDWlM2DPexhLgAiBnZx9PYhDE0ynv%2F3Eu7Wfn40J3SWfhuNot1uXeW3V9Zir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMWG6iQE%2BGoOZG0yXjKtwDf9bZcidqrliqZev5HVWfxhx731oRiIG2W0ubPOmHIQ1HGYRY%2FSDyOFRYRWe6wxfApSU3SQM3lCWJvY9H4%2BNRZvTgIvNBLEfFsiTx%2FRta%2BEzMu6v08ijDyKXOxhbvdqpMy4NXvY2jbLRb4cLRbYfxGgYVDdzi1Rd6lO%2BYNAlZvs7hRSxMonDPffOtBMRXoEd96YQLHg%2BtFASiMdmxSBGerqtxuAGgkhRkwHmb9aHTficbcToEzC3zcCjSZ%2BRhF%2B6Ew2Ogfw3GemTo1elWCbpPdJhdk6gR8vCSXPN5zeLe9%2FIRYIrzJi74Hs6dop5my%2F%2BwjxZz91SR3lO%2BzFe0LYtk%2FdVWavFHPY33CZ9k4FxICvmiPCQ39ikFXQu4iH51yWim2zV19CM05uQwEjV8JObPm7ix7Q3W0j8HnAjT1KCJeMhJ4%2FXSEyLmXKtxULzV9fpNzrz%2Bj6nHFR3NdPkFmDOYMoLDLPctWXoPEZQbH8janTtvQwF%2FbJ%2BVGKU%2BAjBWF4SIHpmVGPYh%2FiIEjhW5zMJdGwo9NATCIeiGjL%2BjvRL71fJAL6Jd64NT7UARet2UdI6bkMHUQcpQ7f01n5BUAT1XIrjmn6%2BJLzwi9HugszYMXNbcaaJqGje6t7MEN%2F0wjPq70AY6pgHiozwSdKZm4PFlhkMuuhGaxq%2BdbGTOoFt8lAnBifQTwOKciNVGxcgH15Vf3cXcge8%2FRczQCTHtJcxJWoC1vAbWGt8aS7ykpdOboRkGbffXW6YnKlpVn5%2FyZEPtg1VhkksyhWfvJCIbIq8JhsldTgUgJjU6NL027WjKeRA9Rf27pmTxKkrXhtkXNTevDh7pOL5H%2BDrbUJJejqSBV%2FkDxgfRiq%2BCEDxd&X-Amz-Signature=648bcc9cdef419c66c7c83f482f372d89c169d6dfb9b874da70ae0cf7970e97a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







