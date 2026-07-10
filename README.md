



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHNWQWOG%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T192006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH3bSkNIGJzy3lQHGWDhRhTdLE2K6%2FGQQaoH1%2BHovoWbAiBHZ2R996YGRS3S0wdMXQK9N9Xus%2FMzjBxRP4MakU1GtyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF0%2B5%2BS4beiJVOwoxKtwDv%2F1heroJNbG1CzWQG7%2F%2FQIIx3TPnnl2GB1Bb7fcy0ScOmMi2TnxqO2K%2FOVLF7wBd2aL80HdofHaXgfGfMkryc%2F0tcACkHvrc2l8kYeN4Xipc5UGGW2OT02cBcHBOrHggam9Kk1veTydhY4fajVnNfLaBNtUY%2BNKLVbhuZ2u2kJba0sYQnOacZX%2Fj%2BkDLmpoppNoDxSxZHEayHcyAU%2BPTHFrKO1C6o323zHutI5O8a%2Fg5LfWzt5eemerct5T2HKusP3nyXYEyDy6Zl7%2B7b25ug8%2BFSW53JqYbaP1e8DkgfPZyaid5XdGLts3IT%2BoaPm%2F3JyZMw81ZONoxbQneOZwAfWhguvOhNiq191zXqiKl%2B5d2j4n4weF8UU3w3U4VY4CFpqYiD%2FUYG92OgrT8eXrZwccNoXrxI1Es2h9JlDLLMciWu77z8znhRh2SAJxgMKUTbFinOD0gtNdhpwM869qotEch8VfZ3WV693W8rVF9K%2FHedi78m2oCwnO4lrTds9OL1KyfxyLo7BFL3OiGpTjWbgw86pFMk6Lcym2vNZJwpV%2FM57zhVynPNRaqcRzEZ92dXuhNZcV1VXXs1bEUDz4McXrM6mbv6%2FEny0mkHCt4ScOWx1f5wt3tDb%2BmrnEw6%2B3E0gY6pgFG9tS9AoSWwgbOajKw%2FJWuyXs42D3GyVtSokCYEEK8GmSKCLSu5nEWlCL0PJkUa%2FWFwrCSmClx4bnYUq%2Br12c3HTQL0Hm2cOU4uQlwAiBoOrLwKjz0UbPWXeXmG1Shnu6ooE9WuDsANexbW1eefUDf44jU1yat9DGiUAhi%2BVnyMAQmyaA18vFfKaqYq20okRira2crbrEld7YtO45HHhszq6xXfloX&X-Amz-Signature=394882b7f6bfc0e89af239e392cee9ffbc74affea2423bac3dbcf4ffc59e7ebc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHNWQWOG%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T192006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH3bSkNIGJzy3lQHGWDhRhTdLE2K6%2FGQQaoH1%2BHovoWbAiBHZ2R996YGRS3S0wdMXQK9N9Xus%2FMzjBxRP4MakU1GtyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF0%2B5%2BS4beiJVOwoxKtwDv%2F1heroJNbG1CzWQG7%2F%2FQIIx3TPnnl2GB1Bb7fcy0ScOmMi2TnxqO2K%2FOVLF7wBd2aL80HdofHaXgfGfMkryc%2F0tcACkHvrc2l8kYeN4Xipc5UGGW2OT02cBcHBOrHggam9Kk1veTydhY4fajVnNfLaBNtUY%2BNKLVbhuZ2u2kJba0sYQnOacZX%2Fj%2BkDLmpoppNoDxSxZHEayHcyAU%2BPTHFrKO1C6o323zHutI5O8a%2Fg5LfWzt5eemerct5T2HKusP3nyXYEyDy6Zl7%2B7b25ug8%2BFSW53JqYbaP1e8DkgfPZyaid5XdGLts3IT%2BoaPm%2F3JyZMw81ZONoxbQneOZwAfWhguvOhNiq191zXqiKl%2B5d2j4n4weF8UU3w3U4VY4CFpqYiD%2FUYG92OgrT8eXrZwccNoXrxI1Es2h9JlDLLMciWu77z8znhRh2SAJxgMKUTbFinOD0gtNdhpwM869qotEch8VfZ3WV693W8rVF9K%2FHedi78m2oCwnO4lrTds9OL1KyfxyLo7BFL3OiGpTjWbgw86pFMk6Lcym2vNZJwpV%2FM57zhVynPNRaqcRzEZ92dXuhNZcV1VXXs1bEUDz4McXrM6mbv6%2FEny0mkHCt4ScOWx1f5wt3tDb%2BmrnEw6%2B3E0gY6pgFG9tS9AoSWwgbOajKw%2FJWuyXs42D3GyVtSokCYEEK8GmSKCLSu5nEWlCL0PJkUa%2FWFwrCSmClx4bnYUq%2Br12c3HTQL0Hm2cOU4uQlwAiBoOrLwKjz0UbPWXeXmG1Shnu6ooE9WuDsANexbW1eefUDf44jU1yat9DGiUAhi%2BVnyMAQmyaA18vFfKaqYq20okRira2crbrEld7YtO45HHhszq6xXfloX&X-Amz-Signature=393a1a5c0cc5c39debc8b04609273d33922ba281c6826a1f1b0d1ff2b5ff5039&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







