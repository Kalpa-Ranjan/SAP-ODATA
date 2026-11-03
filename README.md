



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52UAOZM%2F20261103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261103T120706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGbv3XFEpz2wUR8ThsmZ80iACiwgG2v3I4vNKIg35UV2AiEAy7SKW5kz3miUf3uCM1RSG5ckyEDzQXzPQb6Rt1eSfu8qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FRBOIMYUwMdVL4FCrcA61d68F0dHQ6NV6S%2F8LFfWRP9tWldTETH%2BCclmHywSjtOjmvkCBXIYGjI6AFVWOhPQRSfVhVJYomg1PESE3m0f9pB3SU37qYyr5RQSnK3psGZmyzgLeot9J0XTh1T7p%2FmV%2Butex2vWH4PL99mONC1H7WyqGoASco7RVuaSDuzOYEdQwmvRfw5EyS7uoK2szRieWHMujZ81YMSHn4t7xouziq1jOT%2FE9q%2BkV4eCqm5sSOqAIIC1XHoeT%2BKbBssHIpNht%2BIRRWk1vY5uQT0ltBXyS7cLIfSHWhrAtYpDqmYvn6C4Mv5Wu2sMDmTgiPIZQZRvCitI9u7%2BPMZmnn%2ByrBb9tY6JB5L44%2BDum%2Fp624J9qKlN35JhTdN6yDyjwuB3bYo5kbJyGrpRzaNQjFBu%2F4MuKiiuAMTG9bUqT4QWbtE2c2WM1bEitNGTB4ih74a7T8M4Xti6QkTp0%2BYD3dHN7haUIp28QSIVOxyc2Vh3fAZlIrogEatcjmiITTZtrlIO9r%2BJx1j%2FJAOE3%2B9BUmUxZvAArkIztgrb6Ti9C%2FBGyFd7%2B6j%2FPJ%2Ft65r1SI%2BGwzstP2%2B4hp%2FPjZKRr5YkiiKjuOmW9xpSw3ZL993WAbefaVvsbHy7oaP53dkcMR5YGbMPSCp9cGOqUBE9LC3HX31wpbOiWwEJqY7oq9v3DvYP350J4IhD1QbJZwgwtCuONA5bPjxk6E29AFmavYbBH2rYZPvCXDDPwEo0cBUYUpfETgw63FM7%2FvdTvA5TIE7253y0IDC970zuJa%2F4T%2F%2FPiOidO%2FnnscJY5ukGCGQCVw21KugrPE45o63OChyW7YzmKGewmLBRJeCCHylpxQq2nhH8t0k1wtXbUIrggXfHkV&X-Amz-Signature=4f40d5bc3cd8dd13475d84e66e7174eedd2722f0f3daeb5b8fc99516eb599bb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52UAOZM%2F20261103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261103T120706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGbv3XFEpz2wUR8ThsmZ80iACiwgG2v3I4vNKIg35UV2AiEAy7SKW5kz3miUf3uCM1RSG5ckyEDzQXzPQb6Rt1eSfu8qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FRBOIMYUwMdVL4FCrcA61d68F0dHQ6NV6S%2F8LFfWRP9tWldTETH%2BCclmHywSjtOjmvkCBXIYGjI6AFVWOhPQRSfVhVJYomg1PESE3m0f9pB3SU37qYyr5RQSnK3psGZmyzgLeot9J0XTh1T7p%2FmV%2Butex2vWH4PL99mONC1H7WyqGoASco7RVuaSDuzOYEdQwmvRfw5EyS7uoK2szRieWHMujZ81YMSHn4t7xouziq1jOT%2FE9q%2BkV4eCqm5sSOqAIIC1XHoeT%2BKbBssHIpNht%2BIRRWk1vY5uQT0ltBXyS7cLIfSHWhrAtYpDqmYvn6C4Mv5Wu2sMDmTgiPIZQZRvCitI9u7%2BPMZmnn%2ByrBb9tY6JB5L44%2BDum%2Fp624J9qKlN35JhTdN6yDyjwuB3bYo5kbJyGrpRzaNQjFBu%2F4MuKiiuAMTG9bUqT4QWbtE2c2WM1bEitNGTB4ih74a7T8M4Xti6QkTp0%2BYD3dHN7haUIp28QSIVOxyc2Vh3fAZlIrogEatcjmiITTZtrlIO9r%2BJx1j%2FJAOE3%2B9BUmUxZvAArkIztgrb6Ti9C%2FBGyFd7%2B6j%2FPJ%2Ft65r1SI%2BGwzstP2%2B4hp%2FPjZKRr5YkiiKjuOmW9xpSw3ZL993WAbefaVvsbHy7oaP53dkcMR5YGbMPSCp9cGOqUBE9LC3HX31wpbOiWwEJqY7oq9v3DvYP350J4IhD1QbJZwgwtCuONA5bPjxk6E29AFmavYbBH2rYZPvCXDDPwEo0cBUYUpfETgw63FM7%2FvdTvA5TIE7253y0IDC970zuJa%2F4T%2F%2FPiOidO%2FnnscJY5ukGCGQCVw21KugrPE45o63OChyW7YzmKGewmLBRJeCCHylpxQq2nhH8t0k1wtXbUIrggXfHkV&X-Amz-Signature=6f734c03d6cf234cec941d10423b78b7dc8094e242b4943e0fb2e406dee46de0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







