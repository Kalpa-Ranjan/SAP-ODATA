



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPYAYTOZ%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T072239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDpaSYttCjCUzTZUNuazmhlBBBr3Y3sOdBpdRJ1gYIisAiEA3bFFSVTEjIY5Iv17vcobG%2FwBGNwTH50ifXTxu%2B5hTJoqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6JYQAkIEGJu0CnnSrcA23rDrRL1YoQfx0RtnCmpzqMbzAbd%2F3Fqyv5a5RR35VJV%2FejWLaCf8iv2jyVACJaE%2B74cLeJ%2F%2FvLRj6bXHUKVCJrrTaaohq3I%2BZjhvRoh3BzeSB6LvUcUnNx8WZy9pa7zvjNfW45qYdSDohlADMp5INycBIzhPZrLxsU%2BMITdbS3Uqlqw78cppLJdAaUL5RtD%2FL5%2BZFS95%2FQeNdp1BvF23%2FV4owMofsyA4H2EbLuIQfdP%2FinUcuV27xHY6YuZ0CILVvtx97A2C2HgqzF67xiyGKUAPpOTAVKqPxzEmwIOkDa7ZpvU4zD2tlIKtcCy9sSJ1qPtCFdfeilvNegMkwS%2F168SR4vfYkrvNTL3oGqWohVgC7oy9fjOz%2FhcbG4wJKap%2FhMR7W3uUZLZpSZL5pTBiWLeJEK0nWHpN%2FDGPSnDjxwO%2Bd0REngBZtNcTjBdPI2MpluCc9m4BI4Cs%2F3nRJzxSOxS%2BmtRfglBJs6OaRNfoNUWvBKxgfv%2B%2FKsfHKyTouhlWRJ69FdfiCYPp9F%2FeBkcOTSuzLRu32l01%2FD2vY%2Ff87zrZCIPBDdVo%2FNvlgu3T9Ni1CAVGl4Hif3gWKTMeYTih%2FhB7xFz%2FiotKbDYmZy5FInYJjr08eQhvgAKeKqMLSzzc4GOqUB6sqF3byuKfL%2BXA%2FxNBgl9bpoOKXF1l%2BzprikZlPm0n3eNJZYeM3KA2H0GAYKRQ7hQQFVps5H%2B83qAperbejskGVNT1q1P4mXoB32QxfIWRslMr3L6hiRmWdd%2Fhp21V3xJRdXfymTy8Hc23zoO5rjUkJZ5MgV3DSo06%2BY4oplq3zOhhMoa%2FZsI3ug4%2FqNwvDbZUZpcxDtNciXv7r4dvauVw5vVwdr&X-Amz-Signature=29b6714c3aecf446d480954b2a23df23ce9d1e47f8fdd2fdb56a3c10c9be584b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPYAYTOZ%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T072239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDpaSYttCjCUzTZUNuazmhlBBBr3Y3sOdBpdRJ1gYIisAiEA3bFFSVTEjIY5Iv17vcobG%2FwBGNwTH50ifXTxu%2B5hTJoqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6JYQAkIEGJu0CnnSrcA23rDrRL1YoQfx0RtnCmpzqMbzAbd%2F3Fqyv5a5RR35VJV%2FejWLaCf8iv2jyVACJaE%2B74cLeJ%2F%2FvLRj6bXHUKVCJrrTaaohq3I%2BZjhvRoh3BzeSB6LvUcUnNx8WZy9pa7zvjNfW45qYdSDohlADMp5INycBIzhPZrLxsU%2BMITdbS3Uqlqw78cppLJdAaUL5RtD%2FL5%2BZFS95%2FQeNdp1BvF23%2FV4owMofsyA4H2EbLuIQfdP%2FinUcuV27xHY6YuZ0CILVvtx97A2C2HgqzF67xiyGKUAPpOTAVKqPxzEmwIOkDa7ZpvU4zD2tlIKtcCy9sSJ1qPtCFdfeilvNegMkwS%2F168SR4vfYkrvNTL3oGqWohVgC7oy9fjOz%2FhcbG4wJKap%2FhMR7W3uUZLZpSZL5pTBiWLeJEK0nWHpN%2FDGPSnDjxwO%2Bd0REngBZtNcTjBdPI2MpluCc9m4BI4Cs%2F3nRJzxSOxS%2BmtRfglBJs6OaRNfoNUWvBKxgfv%2B%2FKsfHKyTouhlWRJ69FdfiCYPp9F%2FeBkcOTSuzLRu32l01%2FD2vY%2Ff87zrZCIPBDdVo%2FNvlgu3T9Ni1CAVGl4Hif3gWKTMeYTih%2FhB7xFz%2FiotKbDYmZy5FInYJjr08eQhvgAKeKqMLSzzc4GOqUB6sqF3byuKfL%2BXA%2FxNBgl9bpoOKXF1l%2BzprikZlPm0n3eNJZYeM3KA2H0GAYKRQ7hQQFVps5H%2B83qAperbejskGVNT1q1P4mXoB32QxfIWRslMr3L6hiRmWdd%2Fhp21V3xJRdXfymTy8Hc23zoO5rjUkJZ5MgV3DSo06%2BY4oplq3zOhhMoa%2FZsI3ug4%2FqNwvDbZUZpcxDtNciXv7r4dvauVw5vVwdr&X-Amz-Signature=556f48a88ae35a7fb7e6e96affa5b03f4a376463a8f757760ed8eadf93d3887b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







