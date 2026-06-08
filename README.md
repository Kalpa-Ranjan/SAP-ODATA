



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KM5VCVB%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T200708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1PV6PS9BQYGzQPl9bJt9tm0xr44pYZrUsNyjykhw7uQIgF5LfCG90zjKujv71QoPnrRcBJEM49l1cwwsWNqW9N6UqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEtJJQdiIW5bM2zEoCrcA9SNfwHPBIX4xjEk4dZ%2Fcyb53sCRZeL%2BqpP4uzFU1tQwevPOhsxO6PckmlTajofDf7OYROKppv%2BzEE53E%2FeZ%2FIGsGlhO0atXVKjs5JIDoIerWjPD%2B%2Bkekm7HTrCkQo%2BzevYWSpE9YW6AQh01I9KdyrxRaH4h69UZfkCgXZE4kAYLzQN7nbAIxs9OF7e4Qnm005sylxA0J2cFPf3eYUIMsKvnKWcmb8XgTHlnWp3Ov6L%2FSg%2BgB785y7U5h2M7%2F4FbsqJi0CZuYi2F85LoozopcVR2vNi9jNf1IOPPsrDlOHri3jIkzDEAgPoKwwQ9Bg9nQI5XH9j06FmrNPOL8KtyjIdOwuRy8aE0HmZ9NZrVoF01UIlN0RI2pq%2FYybc1zIR4AJNSzj5NcG8H0RK63SvDH9XyNLmeMHTtlGUksR1s4ymbQ3Q5nWJfxBVohVvENgRFhpyLUeTxcbAqiJaHv5YmnPEQxHl%2Fs1L7qnD8oGy%2FLqX1BXfnZ6KV%2BxBrG9IFvzQ25Hn8dsXjcTPwbYz26I3eyYZywk4juHt1Yme57nHKcfhQOdCzVcNy91Nf3%2BZAQnP%2FZwZgtS4omAeSwcRDrl8oOp7ZhWCkjjewYjhLF1lj7r8zfxvaGyd6rL1Z3T1xMNv6m9EGOqUBD1Y2nQvCnm2THECvTrEEOJVhsIzBYhpAWBlXAxJA75rDVW2TiifnONeRScbrzsJlRG4AbUtGkbB%2BFwL3yDrFlEFGXgIwBi8upFwQyR81NiGG2ccXNLqxYaPmYt37hYR%2FhQNdGS%2F%2BeHgCc3WW%2Bx1TSDuIDIzDHRBJ4rfYbtMdUuwg1y%2B2nkCfzpLApSb3XW%2FqN9A%2FYsw%2FAqRdDbUYKjntd3q88o0Z&X-Amz-Signature=460db83fc187209db3c10e9e3f58bba9df56590ac45a4713bdd519d741d9ccfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KM5VCVB%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T200708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1PV6PS9BQYGzQPl9bJt9tm0xr44pYZrUsNyjykhw7uQIgF5LfCG90zjKujv71QoPnrRcBJEM49l1cwwsWNqW9N6UqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEtJJQdiIW5bM2zEoCrcA9SNfwHPBIX4xjEk4dZ%2Fcyb53sCRZeL%2BqpP4uzFU1tQwevPOhsxO6PckmlTajofDf7OYROKppv%2BzEE53E%2FeZ%2FIGsGlhO0atXVKjs5JIDoIerWjPD%2B%2Bkekm7HTrCkQo%2BzevYWSpE9YW6AQh01I9KdyrxRaH4h69UZfkCgXZE4kAYLzQN7nbAIxs9OF7e4Qnm005sylxA0J2cFPf3eYUIMsKvnKWcmb8XgTHlnWp3Ov6L%2FSg%2BgB785y7U5h2M7%2F4FbsqJi0CZuYi2F85LoozopcVR2vNi9jNf1IOPPsrDlOHri3jIkzDEAgPoKwwQ9Bg9nQI5XH9j06FmrNPOL8KtyjIdOwuRy8aE0HmZ9NZrVoF01UIlN0RI2pq%2FYybc1zIR4AJNSzj5NcG8H0RK63SvDH9XyNLmeMHTtlGUksR1s4ymbQ3Q5nWJfxBVohVvENgRFhpyLUeTxcbAqiJaHv5YmnPEQxHl%2Fs1L7qnD8oGy%2FLqX1BXfnZ6KV%2BxBrG9IFvzQ25Hn8dsXjcTPwbYz26I3eyYZywk4juHt1Yme57nHKcfhQOdCzVcNy91Nf3%2BZAQnP%2FZwZgtS4omAeSwcRDrl8oOp7ZhWCkjjewYjhLF1lj7r8zfxvaGyd6rL1Z3T1xMNv6m9EGOqUBD1Y2nQvCnm2THECvTrEEOJVhsIzBYhpAWBlXAxJA75rDVW2TiifnONeRScbrzsJlRG4AbUtGkbB%2BFwL3yDrFlEFGXgIwBi8upFwQyR81NiGG2ccXNLqxYaPmYt37hYR%2FhQNdGS%2F%2BeHgCc3WW%2Bx1TSDuIDIzDHRBJ4rfYbtMdUuwg1y%2B2nkCfzpLApSb3XW%2FqN9A%2FYsw%2FAqRdDbUYKjntd3q88o0Z&X-Amz-Signature=8e707d99f4d5973a8a6b8dcf8ba213e883d008993075fcb938ec034aaef192f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







