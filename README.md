



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUMCWKV%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T122717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCxmiXa3ZiVZOhJi%2BxU5zzxYAe%2FpFGj3ihwnuByAilYhQIgSkyyZOl1OfAh26yRhT7X3wJP5jJZ6l%2FFfo%2FhN238u3Qq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDNpX6zAXW9DwXdyZgyrcA9bIhuScjPa4aH7a1qWypSVWXeAciFqrNg0pr98w8t6dYuy6mAVKRqcPymIm5817flg%2FdoWDeRAOnRZh%2BmXGNO183t9MMFmqXxvkVM8rPuZawyVfmQPWOc5dcmVe5SB2dEXixExLCgMqnnCGqq83h568cLvPeHecs%2BytAEMGS2IokXgcOkSvuaKpvnKDZwMX4ukFWLxQJ91lpa0eONYiEKeIwBtqFW0Z9NHvuyx%2FoKY2oktPSidpnlY2AOPTIBSARxyUcXmarZXZ%2BH2sgA7j%2Bx3LgDyaJ%2FcSPl2oksJZwhXPdg%2FZvXaznobGJbG7b5xNwG0gYGXO3by%2BSF%2B8Y3tpd3tekmTvaj5RN%2FkPWtmMG74kp9YI%2FS18fqKD8QlmO8rBENbjmnQ3ZJk33%2BkyWENGJjz6eFYdCWWn5qUG%2FmMvkYuJccPjRXp4gCXFRt81QAt4uBEWDKPDIJp%2FFJNXQVoCcfDORU6nrreymnfB8qyTm%2FPEctXaY%2Fp%2BGHrixgxWuigsQMDdLmc%2FVk1v7vjIelIzpXmJ3P24zFP%2FdPJAZc9uRnq1pbz%2Bayu5qD5djqWobzEDl4LkSgr2oZoi0TCH1CX1Gymtbt7OCTzdqNDaaFnCxy4MsE2BZNIBR4KnCTa0MLyti8kGOqUBGQORpDn0JyoN8dNrI3VZsdxD0r2e2qPhm%2B6f2ZLSdY%2BEXy7Tl%2BAhmhCPrgKRJ2w%2FvkfXua%2BRwr%2FstxaOkev0KtxY59Hjy3oTxVUDoBcSceoZZfZh842%2F4ZO2%2FBByAe86BThUokfcSIRb5BjZEDGHGMMdzb6Q7F6ir2O%2BJgHvvAsH0zzqsv0iQYtG3ApwnQ0%2B8A2eVM9qRkjXkC1plE8HEQIuwwaU&X-Amz-Signature=5fb1b1b61a110716f0a6d3ef279cb1f37748a6aac01eb3c3e41b0dea58b56149&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUMCWKV%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T122717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCxmiXa3ZiVZOhJi%2BxU5zzxYAe%2FpFGj3ihwnuByAilYhQIgSkyyZOl1OfAh26yRhT7X3wJP5jJZ6l%2FFfo%2FhN238u3Qq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDNpX6zAXW9DwXdyZgyrcA9bIhuScjPa4aH7a1qWypSVWXeAciFqrNg0pr98w8t6dYuy6mAVKRqcPymIm5817flg%2FdoWDeRAOnRZh%2BmXGNO183t9MMFmqXxvkVM8rPuZawyVfmQPWOc5dcmVe5SB2dEXixExLCgMqnnCGqq83h568cLvPeHecs%2BytAEMGS2IokXgcOkSvuaKpvnKDZwMX4ukFWLxQJ91lpa0eONYiEKeIwBtqFW0Z9NHvuyx%2FoKY2oktPSidpnlY2AOPTIBSARxyUcXmarZXZ%2BH2sgA7j%2Bx3LgDyaJ%2FcSPl2oksJZwhXPdg%2FZvXaznobGJbG7b5xNwG0gYGXO3by%2BSF%2B8Y3tpd3tekmTvaj5RN%2FkPWtmMG74kp9YI%2FS18fqKD8QlmO8rBENbjmnQ3ZJk33%2BkyWENGJjz6eFYdCWWn5qUG%2FmMvkYuJccPjRXp4gCXFRt81QAt4uBEWDKPDIJp%2FFJNXQVoCcfDORU6nrreymnfB8qyTm%2FPEctXaY%2Fp%2BGHrixgxWuigsQMDdLmc%2FVk1v7vjIelIzpXmJ3P24zFP%2FdPJAZc9uRnq1pbz%2Bayu5qD5djqWobzEDl4LkSgr2oZoi0TCH1CX1Gymtbt7OCTzdqNDaaFnCxy4MsE2BZNIBR4KnCTa0MLyti8kGOqUBGQORpDn0JyoN8dNrI3VZsdxD0r2e2qPhm%2B6f2ZLSdY%2BEXy7Tl%2BAhmhCPrgKRJ2w%2FvkfXua%2BRwr%2FstxaOkev0KtxY59Hjy3oTxVUDoBcSceoZZfZh842%2F4ZO2%2FBByAe86BThUokfcSIRb5BjZEDGHGMMdzb6Q7F6ir2O%2BJgHvvAsH0zzqsv0iQYtG3ApwnQ0%2B8A2eVM9qRkjXkC1plE8HEQIuwwaU&X-Amz-Signature=423a4d18f4e146ad49e53aaa7055c8cb2e5c72348373b87e2b7b377d4912078e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







