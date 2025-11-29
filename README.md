



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STINBM62%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T011056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEBwUgeO2lZKOJruL1%2F6KUwq%2Bh9Roe7yYoQb659pA09kAiEA6D9Yt5oHEw2XdCpahizz%2Fpqg6WwW0vmgGTO6rWWbtY4qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF1W6S6oc%2B4iSks4XyrcA5u20hDS1SANnKFTHoppdDWIKmbUR%2BKy9duk9EGIC2JU3TmaOYfkA4yHzujgMYPzJyFhQDnJGNciP1Q66uQAJ6qVCyOvnT3IDUZRNV2Rp4XoHsamVBFm5gBtQl0QXVc3XXfMdv%2B4DdgcCZsMCWo1rJr%2BXchNdqHqVJHVKHVTZi8i9PeDrM6HVa8GVRYC7NOwIf9j7YIRrl2WumjRLO55wEZzeUyGx1Q%2BGktQLcxt2JPKm2j5PS1SV2nKpDRG2ACZtlap2aYZvkJklRwYf4FvWrm0luN2VN3wElHQyGU3yyn%2FvFdw7RXfnh%2BjBj%2BgoacHuTiraypR%2FADQILulZziceF5LT68HYxwJg%2FsmjYiPMmwZZ2UXhOPIsNH9iCSacNRLCa8BUm%2BK0pdu9Con8BwlMVD%2FxIFWR8J9CQdSuuNvV4Q8v4%2BsRRWf%2BqHBQtMHpe4ULBVe9%2BSlyU%2FGukSiaudeuz4Q6e62G3ziAqLNGJ3Zo6KGf%2Fy4KlY6gXV%2F5DLFpRTq1QiuNT2ya4nS%2FZrWJb%2F4HJlxGUj4wJGFitKhjDkvHFOp5jaaHAmep%2FWXKooFqgYcr%2BAZM27S6CM%2Bia7TUmoYPHtfWJHX4W9M9PejpSg8dCvRnlD%2FD6h4XAoIU1vLMIL1p8kGOqUB2Fb8%2Fas2cqIvgX0sKD4Pi9R3IZ4jHAxC67tfaulyPDDeR%2BTtoQQqevaqim5bwUGqTNvH1mdxjm6eXh96RiSUHbn08RDq7Fsdo2aNl04CvTelSMiNp8RicFpiausp8YO1t6xdnxaf25D1KOGdpvvRxK4rLctns0ZUny0jAGysa%2FsWuPvr1N8vdiIpCap3w5TmD519fxc%2BBF36G%2FHSh26PA0Srilt0&X-Amz-Signature=cbd4138f8a07bae9f18b2148d552a465981ae67f744a2773d0a364ebe9c53438&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STINBM62%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T011056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEBwUgeO2lZKOJruL1%2F6KUwq%2Bh9Roe7yYoQb659pA09kAiEA6D9Yt5oHEw2XdCpahizz%2Fpqg6WwW0vmgGTO6rWWbtY4qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF1W6S6oc%2B4iSks4XyrcA5u20hDS1SANnKFTHoppdDWIKmbUR%2BKy9duk9EGIC2JU3TmaOYfkA4yHzujgMYPzJyFhQDnJGNciP1Q66uQAJ6qVCyOvnT3IDUZRNV2Rp4XoHsamVBFm5gBtQl0QXVc3XXfMdv%2B4DdgcCZsMCWo1rJr%2BXchNdqHqVJHVKHVTZi8i9PeDrM6HVa8GVRYC7NOwIf9j7YIRrl2WumjRLO55wEZzeUyGx1Q%2BGktQLcxt2JPKm2j5PS1SV2nKpDRG2ACZtlap2aYZvkJklRwYf4FvWrm0luN2VN3wElHQyGU3yyn%2FvFdw7RXfnh%2BjBj%2BgoacHuTiraypR%2FADQILulZziceF5LT68HYxwJg%2FsmjYiPMmwZZ2UXhOPIsNH9iCSacNRLCa8BUm%2BK0pdu9Con8BwlMVD%2FxIFWR8J9CQdSuuNvV4Q8v4%2BsRRWf%2BqHBQtMHpe4ULBVe9%2BSlyU%2FGukSiaudeuz4Q6e62G3ziAqLNGJ3Zo6KGf%2Fy4KlY6gXV%2F5DLFpRTq1QiuNT2ya4nS%2FZrWJb%2F4HJlxGUj4wJGFitKhjDkvHFOp5jaaHAmep%2FWXKooFqgYcr%2BAZM27S6CM%2Bia7TUmoYPHtfWJHX4W9M9PejpSg8dCvRnlD%2FD6h4XAoIU1vLMIL1p8kGOqUB2Fb8%2Fas2cqIvgX0sKD4Pi9R3IZ4jHAxC67tfaulyPDDeR%2BTtoQQqevaqim5bwUGqTNvH1mdxjm6eXh96RiSUHbn08RDq7Fsdo2aNl04CvTelSMiNp8RicFpiausp8YO1t6xdnxaf25D1KOGdpvvRxK4rLctns0ZUny0jAGysa%2FsWuPvr1N8vdiIpCap3w5TmD519fxc%2BBF36G%2FHSh26PA0Srilt0&X-Amz-Signature=30facf9e8e848176d9c3b71dd3973b3931426ab86f811978a8d1c65971ae76aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







