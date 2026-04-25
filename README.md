



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFTNVK76%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T184159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDitQiRRjgzdCcSfP96sO2d5D5l54WzjrG3CfvgXVdpqAiEAy1k%2F%2Blx682BQmBWQ6aPN0HdYrerO8tm3v6trCc%2BMAfMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8gzGgtwc4%2Bys4vYSrcA7ioy%2F0pARngJEYsJPJW%2BFxGMpTrMsFm07W9ygKr358Sp1m7lXYT0jrpkLFZRddS3KwVm6b80fpgv7pnqg6S9Wd57BATjHpPWj7Sq7hJNUoGWvVOLrNlPFSW%2F5OtGeSIhArrWilaXNwGVgltUXWB3iQLA7ED08RkvQIprTXYVeh9Dt6gLR55cnaYxaHNaUCr6tlmeWOM6ZszbcVDJlOHIPp2bL%2Fu0zzEbN0eLjFelVODTju6YyP7U40sVkooCdvwL5kTcUUOcooTqc0dYYH3MnMC5clOpDM0AqFKHj1AoCh1HmTbDpjNYIhgIbfjdZTE16vAPQjnziok6gPxgOYClZ8AXRBDtcuYCRsqclYh1cpUj66vtOj%2FRucI8XwcRhxDPzYu0iKoig7ukvSX7Dz2NHqv0Bk6DygbHpyP0vLWdTIDH4fbbKypg3S4iSwkET2chZHbPTgNSemDEOfRv4D61kaFYEkskqBz6znpQPSzIRBB4eQ8R6mjimyyDQ%2BPhcNhnk%2FuFQw9YLvJrpyovPmu4qh16zvwWSkEjv%2FRZ2hqtZwR04mOhPNUDlpdydHAfelf%2FoJG7ojbrnGqjzlDawg2dG9fRtGaPoc5%2F9HqqjDnOSGMIUNItNUqnzPcTMSOMKSJtM8GOqUBDcAqNuL1b1P3NUFgH227OS8cO7gTmUevbFrbCO8E76wJnov4MaPfoO%2BMOuHxxic9xGaOCOoWiMC9a3pj3o5PrlZ%2FU%2BMXsvcyUCHAOSx7F1FVrRs7aiFWg00rmG2K6FDYuWjeZ8bPKKX9FgGV4%2BjuVl4OXIzcnmJD77YM2qHy5PHsyrVUrIxWQc%2F0ByRqgjk6vp4RBRXyqbwt9%2F%2Fdnyl8JOTAOMdh&X-Amz-Signature=daf7ec6225234c94ee443e814a2cbde6dd7796a93e7e95ab776580106acb6021&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFTNVK76%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T184159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDitQiRRjgzdCcSfP96sO2d5D5l54WzjrG3CfvgXVdpqAiEAy1k%2F%2Blx682BQmBWQ6aPN0HdYrerO8tm3v6trCc%2BMAfMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8gzGgtwc4%2Bys4vYSrcA7ioy%2F0pARngJEYsJPJW%2BFxGMpTrMsFm07W9ygKr358Sp1m7lXYT0jrpkLFZRddS3KwVm6b80fpgv7pnqg6S9Wd57BATjHpPWj7Sq7hJNUoGWvVOLrNlPFSW%2F5OtGeSIhArrWilaXNwGVgltUXWB3iQLA7ED08RkvQIprTXYVeh9Dt6gLR55cnaYxaHNaUCr6tlmeWOM6ZszbcVDJlOHIPp2bL%2Fu0zzEbN0eLjFelVODTju6YyP7U40sVkooCdvwL5kTcUUOcooTqc0dYYH3MnMC5clOpDM0AqFKHj1AoCh1HmTbDpjNYIhgIbfjdZTE16vAPQjnziok6gPxgOYClZ8AXRBDtcuYCRsqclYh1cpUj66vtOj%2FRucI8XwcRhxDPzYu0iKoig7ukvSX7Dz2NHqv0Bk6DygbHpyP0vLWdTIDH4fbbKypg3S4iSwkET2chZHbPTgNSemDEOfRv4D61kaFYEkskqBz6znpQPSzIRBB4eQ8R6mjimyyDQ%2BPhcNhnk%2FuFQw9YLvJrpyovPmu4qh16zvwWSkEjv%2FRZ2hqtZwR04mOhPNUDlpdydHAfelf%2FoJG7ojbrnGqjzlDawg2dG9fRtGaPoc5%2F9HqqjDnOSGMIUNItNUqnzPcTMSOMKSJtM8GOqUBDcAqNuL1b1P3NUFgH227OS8cO7gTmUevbFrbCO8E76wJnov4MaPfoO%2BMOuHxxic9xGaOCOoWiMC9a3pj3o5PrlZ%2FU%2BMXsvcyUCHAOSx7F1FVrRs7aiFWg00rmG2K6FDYuWjeZ8bPKKX9FgGV4%2BjuVl4OXIzcnmJD77YM2qHy5PHsyrVUrIxWQc%2F0ByRqgjk6vp4RBRXyqbwt9%2F%2Fdnyl8JOTAOMdh&X-Amz-Signature=e7d71e54eb70e1ead16ce8632d9327e64a7a093e86aa8831c4c4ce37ea873368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







