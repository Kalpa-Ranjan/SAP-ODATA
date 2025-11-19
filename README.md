



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOQEW5L%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T182308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIHLucX9F9LYxB78%2FpA3SKqrz13EmjYWjkqwWbOx4k9RcAiEAna2Xj%2F%2BMznrEHYb4btEaJzzLO%2BBucVp8uKv6BSaqPKAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNSyeLBqXW6HG9xX0SrcAwykCeX9tApGRX1b0%2BR2qI6NX1SSWgRL599EaacRa%2BZoKs15QaFGCIVwv6RV5yUiVjlWRrmtyCaQ5DsXzG2PbW05u2QP7rKSkRIOt6tYyUNwhGgg4kb0KKoPzbCGD%2FdvmpnAyMYWDkAatCG29ZQhh1L5MZ2ZQ15Rc64cjnPuEtJ0P2EWRmRvlPJE6eDdEo8RP5z0eA%2BC4xUTwGsAlX%2Bllay7g55OE68K0XRIJ0UAVytzei5juut6nLXg64tLU1K%2Bzrld1NWi%2FgLHMMF6PSF57DL9cACJTMNI2wulQT%2BKzmCO5P9ZbE6sKp8TLbh4xMvX95sxDnyzLwMta%2BuWvo%2B0SQ9cJGFZ%2FvrnNSLNpuvH9QY4yK%2BEq%2BF0bEoi4%2BvhWXKY5hhQCGaP7b1MT0Xrl0f4q4xgrB6JBAaqtiAELiPjV1yRCWczFVE0njjNdIreT6v6UaO28LMryj3XFS9CH0N01rm7q4UTvKrqxI%2BbT%2FP5gz6KXqWbSuaZJM3hE4N7RhajM4aGYgx29IFBNsFQGCNUARn2zkLKn6gXVPucHtPdG7xHeCO0Rj%2Bjh7539K9qwMphL%2FOEEEOEwR8krcVT0a5ojchxgeh7iSuB11TMzDBtmrebk6ftrfTaiDeaL7IkMJH498gGOqUBYws4YCkNfbKhbY61S0E4VUhZUAy2uY%2FdlCnl%2BIrmBHuO%2FYBTn5zKwsk1YJA57jkFOAE5PtU1k%2BOr0lbGz72WrPzTjrqsGaCTmd7xltthz07HyP%2Bb9x%2Bv9XiC3VBGKggI%2Bqb9zuS3Wmi8AlpMOUYmux5OSqI87lyO5oJuRplEzR1RvYB8j%2Fjx2qbj02XKxr4rr%2F9zbchAxMIrCqpfR5IoAi2h1NoA&X-Amz-Signature=fcf17cb97fd8a6f8eb58b2e9a8e6e3130444e4cf589f7c7ffc41be04745ae8e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOQEW5L%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T182308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIHLucX9F9LYxB78%2FpA3SKqrz13EmjYWjkqwWbOx4k9RcAiEAna2Xj%2F%2BMznrEHYb4btEaJzzLO%2BBucVp8uKv6BSaqPKAqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNSyeLBqXW6HG9xX0SrcAwykCeX9tApGRX1b0%2BR2qI6NX1SSWgRL599EaacRa%2BZoKs15QaFGCIVwv6RV5yUiVjlWRrmtyCaQ5DsXzG2PbW05u2QP7rKSkRIOt6tYyUNwhGgg4kb0KKoPzbCGD%2FdvmpnAyMYWDkAatCG29ZQhh1L5MZ2ZQ15Rc64cjnPuEtJ0P2EWRmRvlPJE6eDdEo8RP5z0eA%2BC4xUTwGsAlX%2Bllay7g55OE68K0XRIJ0UAVytzei5juut6nLXg64tLU1K%2Bzrld1NWi%2FgLHMMF6PSF57DL9cACJTMNI2wulQT%2BKzmCO5P9ZbE6sKp8TLbh4xMvX95sxDnyzLwMta%2BuWvo%2B0SQ9cJGFZ%2FvrnNSLNpuvH9QY4yK%2BEq%2BF0bEoi4%2BvhWXKY5hhQCGaP7b1MT0Xrl0f4q4xgrB6JBAaqtiAELiPjV1yRCWczFVE0njjNdIreT6v6UaO28LMryj3XFS9CH0N01rm7q4UTvKrqxI%2BbT%2FP5gz6KXqWbSuaZJM3hE4N7RhajM4aGYgx29IFBNsFQGCNUARn2zkLKn6gXVPucHtPdG7xHeCO0Rj%2Bjh7539K9qwMphL%2FOEEEOEwR8krcVT0a5ojchxgeh7iSuB11TMzDBtmrebk6ftrfTaiDeaL7IkMJH498gGOqUBYws4YCkNfbKhbY61S0E4VUhZUAy2uY%2FdlCnl%2BIrmBHuO%2FYBTn5zKwsk1YJA57jkFOAE5PtU1k%2BOr0lbGz72WrPzTjrqsGaCTmd7xltthz07HyP%2Bb9x%2Bv9XiC3VBGKggI%2Bqb9zuS3Wmi8AlpMOUYmux5OSqI87lyO5oJuRplEzR1RvYB8j%2Fjx2qbj02XKxr4rr%2F9zbchAxMIrCqpfR5IoAi2h1NoA&X-Amz-Signature=b238cc1e50df4a658cf997ed6bff3305d8d69ee9abb39992bda2f6d5ceaa5952&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







