



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYVOSSV4%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T181024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFIPqP1PN7PR%2BXfH%2Bp11m6D5Ge9S1X%2FVD0OA8%2BSEXPx2AiEA8TXFnFU7uly6t6NSVKDmkRzigogQNkwcaGF48%2FrnbSkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIDjO8VAfS6Nv4uW0ircA0Ti6EOVrcknT1v0%2BmEb4Hwi2AXM2J3jtVapabWEtsUqSheiLg2FFFQrBWfI1ZkuoCFhAKpvPAlC9yFaAAElJ74pPOmlOSv6UiMgvg1%2Bt6XL8%2Brrr8Ef18WwmbTnp0dl0xGqFGpei7Mu3ki35opwIsgHuXZ%2BLwc7yxhSellNsUvZ1H9FuV%2BpUcNQEtNmkNtg%2F7z3Vu7jgRRWdUhPIeHpRr3Ai0lDz528%2BX8nOAiRH9V9GKw6Fz97fksM7Hk7TkYtzjOBbtl4AfBaIkSQpbWrGp8N2hmEdCF44nZWfgAr9yRGAzMYpv1Ix4tNjdJbkxeslhAPFUmxd4W5h28fsBiuYxfs4tmNqQI0fuQYqSsR57Vg8LllDOJveNlj854Wfhs7LjmQO51Xjp3EqquCYHDgHnHerwHwdnKMPEXQC5lbR5iZLXlSNuM75ujP%2FR6Opmy%2FJe6x7kfY0sMSfb0NylqkfDU%2BhaIV1v%2BfTLR%2Fu6zdVBBRi5Jxs0NJVhTnG4uGq%2BfUHjEiDoAyP41hqHEkbxYddAk6cfehR%2FMoQFN3uAmusYXwN%2BgfVB%2B6uimbeoaqszw1BJVA71j8aG1BxJDIXP11bR60hnW1v4LmwsdGigHqS2iD9ZZL9pU3XNcllAXxMK7oz9UGOqUB6JuQOZpsqCgZqBjyNaawScssn%2F3LneLB%2BXpRYU7XiswIxrdW2esti9s9THYepeAoNDOFs0O%2F0yqY1N0ZB10YcQgvcwLb%2FVNseHKJ7oOGRSW1KJKuj2EU8jLnrTIDE4pdg69QRoWwbEM3DLi3EzEmUd4w9J2ynJ%2FufIdkMgkiDg%2FqvfYPWTvTp7hM%2BFotnIHP0LnlLQbOa8157z1seBgsi56oflju&X-Amz-Signature=2b2c1e4a08afdefffd9ed3f776c079bbc32154939389f5cce5fa0b22d0a2434d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYVOSSV4%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T181024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFIPqP1PN7PR%2BXfH%2Bp11m6D5Ge9S1X%2FVD0OA8%2BSEXPx2AiEA8TXFnFU7uly6t6NSVKDmkRzigogQNkwcaGF48%2FrnbSkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIDjO8VAfS6Nv4uW0ircA0Ti6EOVrcknT1v0%2BmEb4Hwi2AXM2J3jtVapabWEtsUqSheiLg2FFFQrBWfI1ZkuoCFhAKpvPAlC9yFaAAElJ74pPOmlOSv6UiMgvg1%2Bt6XL8%2Brrr8Ef18WwmbTnp0dl0xGqFGpei7Mu3ki35opwIsgHuXZ%2BLwc7yxhSellNsUvZ1H9FuV%2BpUcNQEtNmkNtg%2F7z3Vu7jgRRWdUhPIeHpRr3Ai0lDz528%2BX8nOAiRH9V9GKw6Fz97fksM7Hk7TkYtzjOBbtl4AfBaIkSQpbWrGp8N2hmEdCF44nZWfgAr9yRGAzMYpv1Ix4tNjdJbkxeslhAPFUmxd4W5h28fsBiuYxfs4tmNqQI0fuQYqSsR57Vg8LllDOJveNlj854Wfhs7LjmQO51Xjp3EqquCYHDgHnHerwHwdnKMPEXQC5lbR5iZLXlSNuM75ujP%2FR6Opmy%2FJe6x7kfY0sMSfb0NylqkfDU%2BhaIV1v%2BfTLR%2Fu6zdVBBRi5Jxs0NJVhTnG4uGq%2BfUHjEiDoAyP41hqHEkbxYddAk6cfehR%2FMoQFN3uAmusYXwN%2BgfVB%2B6uimbeoaqszw1BJVA71j8aG1BxJDIXP11bR60hnW1v4LmwsdGigHqS2iD9ZZL9pU3XNcllAXxMK7oz9UGOqUB6JuQOZpsqCgZqBjyNaawScssn%2F3LneLB%2BXpRYU7XiswIxrdW2esti9s9THYepeAoNDOFs0O%2F0yqY1N0ZB10YcQgvcwLb%2FVNseHKJ7oOGRSW1KJKuj2EU8jLnrTIDE4pdg69QRoWwbEM3DLi3EzEmUd4w9J2ynJ%2FufIdkMgkiDg%2FqvfYPWTvTp7hM%2BFotnIHP0LnlLQbOa8157z1seBgsi56oflju&X-Amz-Signature=d044812c287df5c85dbe4d1031cdcfb6cde6724cb33aeaedf25337c889633cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







