



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6GGFND%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T093638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFvmfhxdgebtIp%2Bc%2BdrDX%2FLsp5bKvZOLsyj7cAsiJVZwAiEA87Ffar9AhIcynYncp85MlvewISNt5oEovvb28iL4kvMqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRgO0rhnDPRlT%2FLbSrcA7efhT9%2BdwjzaTGBQvmsNwgrrHjsA5SRtUrFveN1J%2By%2BJFqBb40Qy1YWS5enRC0892bc809DmsvFgfvPRYE8OcvcSZVMjYw1TkTju57xX6f7aN9bPwyYAjuHJlPje316Y280%2BY686Evo%2FSWG8TvlCQ4inBQnqClDwZZWhOScqwZ7TofvYJPSLpzeSZvpIscAGasCqxDG6i7xswatuWA8AuBQBelvMrprnBrTJG8HCcc6gIrjqwa2nPV6ELR%2BCk%2F019Ctw4Qdkla2Z0dNbB2vtZPB0lSuwlfGFmL6hQKVCracv%2B4DyPQVx3xTvO%2F0p1VjDwntiBeaahu91Pdx9ZFzVg8b67quiDFZXSBqTVj0%2B17Ekp3SteRzFlq6hPWFiFAO40MScPHjdx89XpkOcrAghjtyK2eRyLr7Q3PFKbFvYBTLvviQPf3daxGmTxRtW6UkLmwubbWVMpupAZTSEI1IMziS5iRcGTZ1XgBCFHIehktazgTluYAS977lppd%2FcDjoHijrZWfOByCLVzWS7B40qKajmyYSSbNTXGn9EVrN7lAK93KrpAQDQtGm5Gs4H4ev%2FzAsqev7JbPXO8fqd7YQYLk5syeliFv6R0nAWhy6Juyn8d6JwXX37uRhSokRMMWok9IGOqUBVvMzq6kInloPzwhxAIu%2FPLy0mSSJQ1oPSjhnHkJljgTouNsj4CcNSkQJo7EbUG%2BKVHCU6CtXpg66Tepmeu9e7q89zJ6OQvQBi%2B3Go%2BUJ5GYqoTowPhctnU9Fk63k6Hh8gvnf6CPOC8H%2BNLDmcZif4vApMZ5Z8oj%2BfxDR5UMJz0oDXH5mACl7qL6TTHJkDB89rYlawJHopw6ITnVajK2eAYrCIyMG&X-Amz-Signature=7831c6f05aa8797aa0f1f85001e2947ec3ee68818875931774a3381322538224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6GGFND%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T093638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFvmfhxdgebtIp%2Bc%2BdrDX%2FLsp5bKvZOLsyj7cAsiJVZwAiEA87Ffar9AhIcynYncp85MlvewISNt5oEovvb28iL4kvMqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRgO0rhnDPRlT%2FLbSrcA7efhT9%2BdwjzaTGBQvmsNwgrrHjsA5SRtUrFveN1J%2By%2BJFqBb40Qy1YWS5enRC0892bc809DmsvFgfvPRYE8OcvcSZVMjYw1TkTju57xX6f7aN9bPwyYAjuHJlPje316Y280%2BY686Evo%2FSWG8TvlCQ4inBQnqClDwZZWhOScqwZ7TofvYJPSLpzeSZvpIscAGasCqxDG6i7xswatuWA8AuBQBelvMrprnBrTJG8HCcc6gIrjqwa2nPV6ELR%2BCk%2F019Ctw4Qdkla2Z0dNbB2vtZPB0lSuwlfGFmL6hQKVCracv%2B4DyPQVx3xTvO%2F0p1VjDwntiBeaahu91Pdx9ZFzVg8b67quiDFZXSBqTVj0%2B17Ekp3SteRzFlq6hPWFiFAO40MScPHjdx89XpkOcrAghjtyK2eRyLr7Q3PFKbFvYBTLvviQPf3daxGmTxRtW6UkLmwubbWVMpupAZTSEI1IMziS5iRcGTZ1XgBCFHIehktazgTluYAS977lppd%2FcDjoHijrZWfOByCLVzWS7B40qKajmyYSSbNTXGn9EVrN7lAK93KrpAQDQtGm5Gs4H4ev%2FzAsqev7JbPXO8fqd7YQYLk5syeliFv6R0nAWhy6Juyn8d6JwXX37uRhSokRMMWok9IGOqUBVvMzq6kInloPzwhxAIu%2FPLy0mSSJQ1oPSjhnHkJljgTouNsj4CcNSkQJo7EbUG%2BKVHCU6CtXpg66Tepmeu9e7q89zJ6OQvQBi%2B3Go%2BUJ5GYqoTowPhctnU9Fk63k6Hh8gvnf6CPOC8H%2BNLDmcZif4vApMZ5Z8oj%2BfxDR5UMJz0oDXH5mACl7qL6TTHJkDB89rYlawJHopw6ITnVajK2eAYrCIyMG&X-Amz-Signature=99dc54d1a2569595e2d980acf818db82210dc78046d8bd6d09c2746a2edfbc90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







