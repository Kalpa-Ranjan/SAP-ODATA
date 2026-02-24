



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPXKSVT%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T185507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCGHGmf4CQMD4FMy1mCo6OuBFtMc1%2FvynPicNa%2FcTlPwAIgZRwSmzw0PLNPUY9oFPfXF1kj1K9TRWK76skQoc4IrtMqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJL42t8PeJSlijYTzircAy9N4Qvk46pRn%2F9WiNwcD2tKxaRScIL0zin6SXimAW91saCjoStelq40MiByf1X68Yi5k%2FtwChC9Ub30qgsENYD0nbQ1iouEZLVSWjiqwAX56PtIOJ1y8wIm%2BxE%2FvnoVyNHAwzIXEH9HxkKMd1%2FtsxjJUHmE8CxMbHMH2VlNE0SynTXUE5NkGSwjd6YeZUhHhZfe%2Bfd9RBSJzVvx2SCHOpYIMLM75eMdAVU%2Fm%2B9oDcnWnhKUWXHyc%2FPm7eHoamOx1D%2BqyRkfESH1OWiKkcFZ3mr49qu8J57ZtWkgAAoiufMyn1OHBNXPM%2BnfzyhBsLleGfUPb04naDHVNulThjsa0Oi3OiML2vmqq0qhoEMPP39n86VGiOX4RYJ6CVTWhbwkI6nussoXk56YN5J6zwRnMXRnOBSohE5fr0daOxTeUqrIm1u%2FFD%2F47b2qpFYvAs4sDnt1AiU%2FZXRbwRWMpot3iXYJLPOyLxE4aVtsdIRomu7pCsygOYuO0pLwXbNZfBTmsLpjzuJfdKRAkq7eilgw%2B1FNuhRO0x%2F0Yn%2B%2F43HcLm4lrC9quW1opIxb8p%2F46MU5DUmfspVy%2BrWClUbdQe9ToVpbAsbcAh1s5h0p7JM2qDMfziWR3noLdhIe0WRGMIyj98wGOqUB2WGtFQKCJHbm5NrnaAXxk6O6a8nRdHDtGRGaT68beQtZw%2BdKIbC3ZOTmdk%2B4JjLmGHDJnQKFh2n4bG9G7ybiQtA7MuXlYNSIuqbBiOxaJ%2FxjyR4BLi5KKnv%2FM3j%2BWohqKvUmZHgUFLZPzH%2F8QDlM6DDOIA22BXEAYy7Bt1rStDtLL0TqVQDbhKEXTcI4d0lTRyI%2FMWbFOzvDLlQ94P%2F6XDYFBYuw&X-Amz-Signature=cf40c762e6f85fc3ca2c5223294b7efbbbd69c60ab14f45e9edea17d229eebb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPXKSVT%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T185509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCGHGmf4CQMD4FMy1mCo6OuBFtMc1%2FvynPicNa%2FcTlPwAIgZRwSmzw0PLNPUY9oFPfXF1kj1K9TRWK76skQoc4IrtMqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJL42t8PeJSlijYTzircAy9N4Qvk46pRn%2F9WiNwcD2tKxaRScIL0zin6SXimAW91saCjoStelq40MiByf1X68Yi5k%2FtwChC9Ub30qgsENYD0nbQ1iouEZLVSWjiqwAX56PtIOJ1y8wIm%2BxE%2FvnoVyNHAwzIXEH9HxkKMd1%2FtsxjJUHmE8CxMbHMH2VlNE0SynTXUE5NkGSwjd6YeZUhHhZfe%2Bfd9RBSJzVvx2SCHOpYIMLM75eMdAVU%2Fm%2B9oDcnWnhKUWXHyc%2FPm7eHoamOx1D%2BqyRkfESH1OWiKkcFZ3mr49qu8J57ZtWkgAAoiufMyn1OHBNXPM%2BnfzyhBsLleGfUPb04naDHVNulThjsa0Oi3OiML2vmqq0qhoEMPP39n86VGiOX4RYJ6CVTWhbwkI6nussoXk56YN5J6zwRnMXRnOBSohE5fr0daOxTeUqrIm1u%2FFD%2F47b2qpFYvAs4sDnt1AiU%2FZXRbwRWMpot3iXYJLPOyLxE4aVtsdIRomu7pCsygOYuO0pLwXbNZfBTmsLpjzuJfdKRAkq7eilgw%2B1FNuhRO0x%2F0Yn%2B%2F43HcLm4lrC9quW1opIxb8p%2F46MU5DUmfspVy%2BrWClUbdQe9ToVpbAsbcAh1s5h0p7JM2qDMfziWR3noLdhIe0WRGMIyj98wGOqUB2WGtFQKCJHbm5NrnaAXxk6O6a8nRdHDtGRGaT68beQtZw%2BdKIbC3ZOTmdk%2B4JjLmGHDJnQKFh2n4bG9G7ybiQtA7MuXlYNSIuqbBiOxaJ%2FxjyR4BLi5KKnv%2FM3j%2BWohqKvUmZHgUFLZPzH%2F8QDlM6DDOIA22BXEAYy7Bt1rStDtLL0TqVQDbhKEXTcI4d0lTRyI%2FMWbFOzvDLlQ94P%2F6XDYFBYuw&X-Amz-Signature=f20b7550b6217c685da8201bbd11c73d711d88dbe7455e54992aaf01ad3f0767&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







