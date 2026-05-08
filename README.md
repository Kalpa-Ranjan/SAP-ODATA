



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJ23ZLO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T072216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGzCOIoD42KnuwhWqc4ERSuzPoh0Y8v%2FFwDIO7ssRtLkAiBcLPNt41fhd8SicRu4T5ubit3yhHao85uKzLTWY9X%2FuCqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowebSf0JlLCd8OKZKtwDgM62gIpKHcapccORp22%2BqKUNE4Pfdf7g1hJu%2B5%2B0FgWO6LlXkV37%2FfOfukM%2BSjArkvLDr%2BROunJN7U4cyycy6zjC7iAYL0anpsylkNvXDBV%2BrR1jyPfzqHiwWhMYYLdSHa7s7Rl17G%2FzVjAbnZx7jvCe4kR8VNlCFLpF%2Beck5wlioT6AzWMxteYnGgWMuteWhYjoe1IaosKG5l%2ByAH%2BZsQ108Oy2cY%2Fo%2BQ7YBr5Zd2PrQVmoZbLZFeXPOWeUjOzwH83uwtk8YklHU4JBzGagnwQPxVenf9hXl7pVWhmwkjpbF1Wf91GNG4OoTNJFBE6ByP%2FLDJwyqtw4h%2FSNO%2FW%2BxOLSokuY8Pg9Gv56PVnK7Hn85do%2FNBUmrETzt794OVlz1m9cUvxfpWEB2Ky7wG%2BU1fFbdjWAAOVF%2Bf%2F%2FmBRpW0z9ZoIm5xl9nafoqRaJQD1TPwBGqc4qWi31gNOLxMmmyXOATzXZ3PKoedW0VHI0PDLY%2FfiwqNncbwENCZkaw3m%2BLHaDlEE0GUuxoH7nzmWMmtcntTAOixcon3BjohlOy98engWcGncFbB2fKwAUPth1VCnD%2Flbj7KuHCPTXZnZnWRa%2FlSeL8EOu%2BA4%2FokfmWq4ZWtFv9%2B1zZ5GRImYw%2FoH2zwY6pgFRHFwDh6bsd3k1eTQ1TcKF2J0VzMik9ohF%2BjCAZopJepG%2BcCwfOEzKn7WPhVnAeIQkPV%2FMikZBSNfKg8Q3DBgIHpuc4EjvaMbxk8o2wauBgYIkssU3Q5cBsuMseDbWkNCDAEOxCkNEjB6pzoW%2Bt3%2BtPxS3slGN%2F8UXEWEj76Jbk0bTFMld1CJJOj9%2FOZORQ1Yr0zIMifb5Qsl8dZR%2BCRbSrXk%2BmA3I&X-Amz-Signature=df3eda434ffaeaffa588d73c589e209710e4dfb0ce566810600d13e73c690b16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJ23ZLO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T072217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGzCOIoD42KnuwhWqc4ERSuzPoh0Y8v%2FFwDIO7ssRtLkAiBcLPNt41fhd8SicRu4T5ubit3yhHao85uKzLTWY9X%2FuCqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMowebSf0JlLCd8OKZKtwDgM62gIpKHcapccORp22%2BqKUNE4Pfdf7g1hJu%2B5%2B0FgWO6LlXkV37%2FfOfukM%2BSjArkvLDr%2BROunJN7U4cyycy6zjC7iAYL0anpsylkNvXDBV%2BrR1jyPfzqHiwWhMYYLdSHa7s7Rl17G%2FzVjAbnZx7jvCe4kR8VNlCFLpF%2Beck5wlioT6AzWMxteYnGgWMuteWhYjoe1IaosKG5l%2ByAH%2BZsQ108Oy2cY%2Fo%2BQ7YBr5Zd2PrQVmoZbLZFeXPOWeUjOzwH83uwtk8YklHU4JBzGagnwQPxVenf9hXl7pVWhmwkjpbF1Wf91GNG4OoTNJFBE6ByP%2FLDJwyqtw4h%2FSNO%2FW%2BxOLSokuY8Pg9Gv56PVnK7Hn85do%2FNBUmrETzt794OVlz1m9cUvxfpWEB2Ky7wG%2BU1fFbdjWAAOVF%2Bf%2F%2FmBRpW0z9ZoIm5xl9nafoqRaJQD1TPwBGqc4qWi31gNOLxMmmyXOATzXZ3PKoedW0VHI0PDLY%2FfiwqNncbwENCZkaw3m%2BLHaDlEE0GUuxoH7nzmWMmtcntTAOixcon3BjohlOy98engWcGncFbB2fKwAUPth1VCnD%2Flbj7KuHCPTXZnZnWRa%2FlSeL8EOu%2BA4%2FokfmWq4ZWtFv9%2B1zZ5GRImYw%2FoH2zwY6pgFRHFwDh6bsd3k1eTQ1TcKF2J0VzMik9ohF%2BjCAZopJepG%2BcCwfOEzKn7WPhVnAeIQkPV%2FMikZBSNfKg8Q3DBgIHpuc4EjvaMbxk8o2wauBgYIkssU3Q5cBsuMseDbWkNCDAEOxCkNEjB6pzoW%2Bt3%2BtPxS3slGN%2F8UXEWEj76Jbk0bTFMld1CJJOj9%2FOZORQ1Yr0zIMifb5Qsl8dZR%2BCRbSrXk%2BmA3I&X-Amz-Signature=7fd6c3510d0d94185daf4cc8320e169758f499c60b6eb7a48ab35d4247d56dd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







