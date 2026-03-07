



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSLA5ZV4%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T182647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDbYtE9SjCa0Epgd85eOusS06G3gOcZM4TXmPnyROraDAIhAMt8CeYnXBGKek8toYVYQ3x%2F67%2BdWtiODCRNDNdfPdK7Kv8DCAMQABoMNjM3NDIzMTgzODA1IgxjBp%2BefD5r%2B1C%2FVrMq3AN7CvRDG%2FW%2BWcs%2FGTyJsROpdF2rCX1%2BRPI3pPyGvzDIRqS1MkFgJAUyjtgSIJoDZOD7C4%2BraJc%2BOLGdkfn0KzzhbXPY8WlKfJYBLm6qu4vhlAsHixDVGaWc7mtJS7NyV1Br3aOF4THW8LX%2B9w9494i%2BzJMjntIhN82ZBxkgp7Cag6WilVsyZ5n0%2FT%2BuaRZQDKbrmj4cPG2LvQEBcUzngkximXXMQ2jq2cN9jbNTHbFNtY9d4gxNNTrd%2F6t8MefyYzyV0dafZ4hHzcCZsjLI%2BiYHaCd9F3P4Jpr7tFZpdzHv0D6G%2FiI8WIhkCn1PRmhiRPAV1UpWKH5H35Z76204i%2BuaRVkbcKiJM49BsS4JWBdH%2FGyqmREQIBrsUlrl1FX1HsFoj%2F1NKzMC%2FK%2FX3wWHpZe0z7%2FGINgXRZyPnkEz18XJ5fRULOAiK%2BWUMWpDPKE8bNPotw4rkaHGyvvSUmJdg15r9O7t0XN06xpadl5GvuyWwQVqULWw6u5zPSVIQ2UxggJ0YwMkGxY29WJkhokggIcOUmsBKld9jAT1Nxx3r4k1S7Kxcd0LTP205WdqC8HVOfuQ7QD5PbC1W1v9SsumVent87HmGHfsQQPzDaFPb7gACUiQ9WRbRoeGwcJYwzCR1bHNBjqkAW4YRoMe5DaBw3hIB%2B9z8I1DdSJ7cPnR3MAik1ESSpv12nDnx2ddW1LnKtkB9%2Bd7%2FKsDhhDJ8THBviIAp0SaHcWXsoUG9DakLmV5%2FUvOTBYNYSOa3G%2FR50jZNVy%2BeGsIhGJsxO7E1mbciO99Cl9d2XKc9bmazP0dSf0sc1TJ6Xk4Q6TuAh7%2Bib6Sqt3P5Dv7jC3Et05ppB50KHc6bU5JmjiJpc6B&X-Amz-Signature=5708213e442086bda63b0ce6effa5fe8430484aa5d286b3947bb9b0941b9fcbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSLA5ZV4%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T182647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDbYtE9SjCa0Epgd85eOusS06G3gOcZM4TXmPnyROraDAIhAMt8CeYnXBGKek8toYVYQ3x%2F67%2BdWtiODCRNDNdfPdK7Kv8DCAMQABoMNjM3NDIzMTgzODA1IgxjBp%2BefD5r%2B1C%2FVrMq3AN7CvRDG%2FW%2BWcs%2FGTyJsROpdF2rCX1%2BRPI3pPyGvzDIRqS1MkFgJAUyjtgSIJoDZOD7C4%2BraJc%2BOLGdkfn0KzzhbXPY8WlKfJYBLm6qu4vhlAsHixDVGaWc7mtJS7NyV1Br3aOF4THW8LX%2B9w9494i%2BzJMjntIhN82ZBxkgp7Cag6WilVsyZ5n0%2FT%2BuaRZQDKbrmj4cPG2LvQEBcUzngkximXXMQ2jq2cN9jbNTHbFNtY9d4gxNNTrd%2F6t8MefyYzyV0dafZ4hHzcCZsjLI%2BiYHaCd9F3P4Jpr7tFZpdzHv0D6G%2FiI8WIhkCn1PRmhiRPAV1UpWKH5H35Z76204i%2BuaRVkbcKiJM49BsS4JWBdH%2FGyqmREQIBrsUlrl1FX1HsFoj%2F1NKzMC%2FK%2FX3wWHpZe0z7%2FGINgXRZyPnkEz18XJ5fRULOAiK%2BWUMWpDPKE8bNPotw4rkaHGyvvSUmJdg15r9O7t0XN06xpadl5GvuyWwQVqULWw6u5zPSVIQ2UxggJ0YwMkGxY29WJkhokggIcOUmsBKld9jAT1Nxx3r4k1S7Kxcd0LTP205WdqC8HVOfuQ7QD5PbC1W1v9SsumVent87HmGHfsQQPzDaFPb7gACUiQ9WRbRoeGwcJYwzCR1bHNBjqkAW4YRoMe5DaBw3hIB%2B9z8I1DdSJ7cPnR3MAik1ESSpv12nDnx2ddW1LnKtkB9%2Bd7%2FKsDhhDJ8THBviIAp0SaHcWXsoUG9DakLmV5%2FUvOTBYNYSOa3G%2FR50jZNVy%2BeGsIhGJsxO7E1mbciO99Cl9d2XKc9bmazP0dSf0sc1TJ6Xk4Q6TuAh7%2Bib6Sqt3P5Dv7jC3Et05ppB50KHc6bU5JmjiJpc6B&X-Amz-Signature=7a4b43aed5b7984ad0bd7e21028f5494a364c2900693f9c118986da824ed460e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







