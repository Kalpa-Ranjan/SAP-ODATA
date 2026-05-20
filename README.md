



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WJR4MXC%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIEbsRZVPYPuwS7E5VZDI4ow6bx1KAAHLhGj8nGcIXI4EAiEAh3f%2BCJfT%2FrwD%2Bbl6m5gKRfgm7PcnHRV%2BgvoLKkXFAv0qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSdbv9hobgkrT2BDSrcA8zo8Jm0OdoJuOnEbMyOJxOpH4ahOGg1ANHRdZbGh%2BkGDRHIrrCO3ldRApGlf6L6Uxc2f0O49ZgS%2Fi%2Fd1xVhbaC5Y1ptnZLF64KDWKAUFYWBATjs3%2BMqoXFY9E2E2NDJPFjXKlZCfKfqS%2BoL%2FV7pfJit4xnp6pkcJW6iGUn58LcvInyQ2KAE09bHSePIepDoZyf7SM%2By8l8m4feLryEtS206SNM8Pfas%2BsZmy7YpbKMz1UnS53PT5fjemv7q6vVhkT%2FHdUQuhyhZUpC%2BeecN5PKx%2BdT4pPsbjW7KmzU5pvsRxKI9Bet3a7kakAgfzE1lrVVAY184%2FSZEjhNMiLecuD%2BXOdA3V3D2OQ8P%2BoyesG3mR6ADLToAXdYQkfqEd8%2FkpreJwCQugmB%2Bnu9zoKdOVB79%2Bskr7qQ7mRC7W7SrayP3XLadXB%2ByYUUYmdhLeEwdyqUiZWpQf2zx7re5x6LoSTwxzDrlViB%2BlQn8GFZaVxtvXbAzqGKhtz%2BLdWnLK%2Bv4LAo2ruMP40ZJFnDg2uQNZyZ%2FP5INXP69aaGj0S3e97a0Qsb%2FeY%2FMvzcM4WWrxW0tg%2FP6KlWM006Ek%2FIIk3oOv%2BKKhQ8FjlNoynFd5qdIRZl7MMhudpV0Vqpfyy5qMPe0tNAGOqUBSPrfJuE0I4tGgntC4YJ0%2BY5wTd3X3HFBJmBc21Wyrr%2FqjjvxxYR8jusorTDTRFbXRnveB2HMDJIjdCBGnxDh8UFe5UChKHGlVPLOu%2FuyndfW31cyAjDjbs38xvsFGwImCZ%2FslxUYLFkHSrFBW3Es%2FOr1Fo%2BFplZ6KIKy2NGzSYuSX2t9CHNqqZ15KWInVyK%2FhkV3kX1tW5eapTJzScMsXKcaGbr9&X-Amz-Signature=d3ec9ad4b629befa6b09806890e0ebd63073abc429f1fbd5d25667d4c0e8193d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WJR4MXC%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIEbsRZVPYPuwS7E5VZDI4ow6bx1KAAHLhGj8nGcIXI4EAiEAh3f%2BCJfT%2FrwD%2Bbl6m5gKRfgm7PcnHRV%2BgvoLKkXFAv0qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSdbv9hobgkrT2BDSrcA8zo8Jm0OdoJuOnEbMyOJxOpH4ahOGg1ANHRdZbGh%2BkGDRHIrrCO3ldRApGlf6L6Uxc2f0O49ZgS%2Fi%2Fd1xVhbaC5Y1ptnZLF64KDWKAUFYWBATjs3%2BMqoXFY9E2E2NDJPFjXKlZCfKfqS%2BoL%2FV7pfJit4xnp6pkcJW6iGUn58LcvInyQ2KAE09bHSePIepDoZyf7SM%2By8l8m4feLryEtS206SNM8Pfas%2BsZmy7YpbKMz1UnS53PT5fjemv7q6vVhkT%2FHdUQuhyhZUpC%2BeecN5PKx%2BdT4pPsbjW7KmzU5pvsRxKI9Bet3a7kakAgfzE1lrVVAY184%2FSZEjhNMiLecuD%2BXOdA3V3D2OQ8P%2BoyesG3mR6ADLToAXdYQkfqEd8%2FkpreJwCQugmB%2Bnu9zoKdOVB79%2Bskr7qQ7mRC7W7SrayP3XLadXB%2ByYUUYmdhLeEwdyqUiZWpQf2zx7re5x6LoSTwxzDrlViB%2BlQn8GFZaVxtvXbAzqGKhtz%2BLdWnLK%2Bv4LAo2ruMP40ZJFnDg2uQNZyZ%2FP5INXP69aaGj0S3e97a0Qsb%2FeY%2FMvzcM4WWrxW0tg%2FP6KlWM006Ek%2FIIk3oOv%2BKKhQ8FjlNoynFd5qdIRZl7MMhudpV0Vqpfyy5qMPe0tNAGOqUBSPrfJuE0I4tGgntC4YJ0%2BY5wTd3X3HFBJmBc21Wyrr%2FqjjvxxYR8jusorTDTRFbXRnveB2HMDJIjdCBGnxDh8UFe5UChKHGlVPLOu%2FuyndfW31cyAjDjbs38xvsFGwImCZ%2FslxUYLFkHSrFBW3Es%2FOr1Fo%2BFplZ6KIKy2NGzSYuSX2t9CHNqqZ15KWInVyK%2FhkV3kX1tW5eapTJzScMsXKcaGbr9&X-Amz-Signature=46b65698ef2b5d34ecf0304ffe9bc4e22434c650ddd759ce9a4a2579cb0c28df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







