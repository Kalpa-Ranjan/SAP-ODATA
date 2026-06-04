



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5M7SZY%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T195841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlQ0iayZnAtE9KwOM93unvCCW4NaPqgcKZL7xg4ra97AiAvTvyweTEbEPVVS6VZUrtl4qOXr0H5s%2Bc64OmcSrzuCCr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMsh5q3kQqeAsrx1FZKtwDByMEAjtZm2mp%2FpZip2qbIK5xuqN0K98pkipg%2BKqiUcmD8Dz3DPQEjoTFViQSCbvW%2B7Hq%2BFJgCFs%2Fp%2FgybcSf2%2B7SEpmSiZxfs9WRanTRuK66wy5HSHTsvVckyiCmg04W9RENQzOSVpWoFaCONM5ZjAymgX0D2L1S%2FeEpkSZbVyQdyHq3Tm6jrtvHEqU5V4X2p%2BQ3WWQibsH%2BISE766TI3grdlLv8fCEM637GY7lpzsxSZLJCH1ddU4hKldM3cFULYTPelPb55I%2Fwh5nqD3sv2P%2FmShuBbHBa9hLLaCphPgP3y7FgGa3siXhVEZaHbkqdpnl494jFixLTG61qi5VUlAuRnRJGPJSdlHAT%2Bqi47qQB1GHy9B7pEhk0SPPM5%2FdmCeFP8XY9sjygfIbXkRRQWYMI7VwbfMdBuR7ldOB0n4Wn6KID1t2qG%2BxANxTLwFDp8h56NnYI7gSC8AmQhbSfk1w5yWwWozJ9fDVLZfNDgL%2FcJzi2hsSqk%2F2QGVG00wQN43G4f3iK3wgyvxnIFweF%2FXEPqwsvfGOGM23zu%2BaheybhTQAsgVZtZBwn4HRGErEspdnVshiT9eoMeKSyQzpHHucQm%2BKvLqw5r%2BTbMdoq2J749iD1TuKBOIDdMpgw0K6H0QY6pgG2P4ahmieP3VEhfHRa3QG5mkqQ%2BMrKGdfqdhWcJoW0ud8p1K1W4zD16NDRJUZTPPvtI9jfjaenK%2FfWh2D4rYZswzj5ve%2FGtrZigbBx8lT3hqHukiuAwKqv5ZycdeR%2FigO0HH%2FT2u9ASwMnndkEurLZS5Vcueh9OP1cm%2B6XYV2VDTopSAEYKA1VsUpQ%2F2Fk4XWjDEmrTvwp9dVsH1EQ9jyE63PCj8gv&X-Amz-Signature=19de4cb398a729fcfdc1229c15212ee6583068ab94ebe8feb838eb4487112b40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5M7SZY%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T195841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlQ0iayZnAtE9KwOM93unvCCW4NaPqgcKZL7xg4ra97AiAvTvyweTEbEPVVS6VZUrtl4qOXr0H5s%2Bc64OmcSrzuCCr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMsh5q3kQqeAsrx1FZKtwDByMEAjtZm2mp%2FpZip2qbIK5xuqN0K98pkipg%2BKqiUcmD8Dz3DPQEjoTFViQSCbvW%2B7Hq%2BFJgCFs%2Fp%2FgybcSf2%2B7SEpmSiZxfs9WRanTRuK66wy5HSHTsvVckyiCmg04W9RENQzOSVpWoFaCONM5ZjAymgX0D2L1S%2FeEpkSZbVyQdyHq3Tm6jrtvHEqU5V4X2p%2BQ3WWQibsH%2BISE766TI3grdlLv8fCEM637GY7lpzsxSZLJCH1ddU4hKldM3cFULYTPelPb55I%2Fwh5nqD3sv2P%2FmShuBbHBa9hLLaCphPgP3y7FgGa3siXhVEZaHbkqdpnl494jFixLTG61qi5VUlAuRnRJGPJSdlHAT%2Bqi47qQB1GHy9B7pEhk0SPPM5%2FdmCeFP8XY9sjygfIbXkRRQWYMI7VwbfMdBuR7ldOB0n4Wn6KID1t2qG%2BxANxTLwFDp8h56NnYI7gSC8AmQhbSfk1w5yWwWozJ9fDVLZfNDgL%2FcJzi2hsSqk%2F2QGVG00wQN43G4f3iK3wgyvxnIFweF%2FXEPqwsvfGOGM23zu%2BaheybhTQAsgVZtZBwn4HRGErEspdnVshiT9eoMeKSyQzpHHucQm%2BKvLqw5r%2BTbMdoq2J749iD1TuKBOIDdMpgw0K6H0QY6pgG2P4ahmieP3VEhfHRa3QG5mkqQ%2BMrKGdfqdhWcJoW0ud8p1K1W4zD16NDRJUZTPPvtI9jfjaenK%2FfWh2D4rYZswzj5ve%2FGtrZigbBx8lT3hqHukiuAwKqv5ZycdeR%2FigO0HH%2FT2u9ASwMnndkEurLZS5Vcueh9OP1cm%2B6XYV2VDTopSAEYKA1VsUpQ%2F2Fk4XWjDEmrTvwp9dVsH1EQ9jyE63PCj8gv&X-Amz-Signature=2d4afd8cacc01ef51dbacbe04714d7dd5d85dd01d0197061ee687a803cece057&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







