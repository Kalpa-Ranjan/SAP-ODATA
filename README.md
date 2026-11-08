



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE64YGVG%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T180459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIGu46VIpaTLXSEhyalsRcLRuXT7%2FoYkNdscRKIQ25xpHAiEAj2gMFgj1GqZzyympv2AOtvs2Bt4HxmZmibSdbuY7uhgq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMq7fDVcGiEba9%2BGkyrcA%2FM23BC6Hnf2epR0Cqh1Lbl0GXwJgHSbgz9nhRvLvkLsAq7YJDFkWa5B3ETESS7H7VckTW%2FGXufCBHrM3Ir%2FDOyC4bXjqyfy7D26KN6glsbJqJcuUUtU4ZOquluLskQEYecr0WhGabmI0Scxur2NCp0alr03zDkxHdgVg%2BwVRlKdZxHv5ym0CZFTK2j7LEjp0F4tOJvZ0fzjb9CVFM9V92UaqDUsm9bN%2FuUurgQ%2BKCmmITgrQ48p4Bv3k54kQT6G%2Bjvl0seIQ9ucGl5Xle3HNshetrE2Ro%2FPvyYqw7%2FmRtfH%2FYdKakfX98%2Fkg3ANZZQ3bCmRmNeMjT7PD4qEIEA49roND5dnS07W9ZGBpj6f%2BbNZsXWf%2F5KRhh2XcvTC%2BYDWKpV%2FT4Iykryr2EfCl6rbu%2FKbTxsyMGSRpzb8tTFmjcqKKPM4%2FcNNlsI9F%2FFEi4CjaRtlmMY0vqraWU4%2F6rQLMTQDxHZ1kEPTv0qMoszetIBX0osA66VYSifN4DBMJLPgt5K1TtQggbSOLNxjl0wPuoaSw8gYiOvDsbPq7a%2FY84%2F9NuUmOLKq1uwIUG8p5cP7nmPXXccm%2B9lyHROvO4Tp9S7Dq79e%2BZqKI2otd%2FH5OdlZzvHWbTN1%2Bse8ulBXMPjwwtcGOqUBfnhodBCVEAFlXbOjlyXPtEiORBUWQXcchC4Gh%2FyUNOVtDbzXpDTihh89pXMiFDZzmUnBstm4w23dACukk0lKjU0yaIoJEwnIH6OwbTqFwta9O4WNStjMK3BXaKbokkIRLw4kiVjsM9gYJe91ERFaBtBHqs%2F9jNZuxH6hj33YwbcWtTvRzRukq6QAJEjU%2FJ3h8QDy%2FGCDl9nDUMM7QLhYZy2QCqHB&X-Amz-Signature=4264e9f585a83bf836f3f6bbaede556e91bdba3251747de43c3082868e076cb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE64YGVG%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T180459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIGu46VIpaTLXSEhyalsRcLRuXT7%2FoYkNdscRKIQ25xpHAiEAj2gMFgj1GqZzyympv2AOtvs2Bt4HxmZmibSdbuY7uhgq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMq7fDVcGiEba9%2BGkyrcA%2FM23BC6Hnf2epR0Cqh1Lbl0GXwJgHSbgz9nhRvLvkLsAq7YJDFkWa5B3ETESS7H7VckTW%2FGXufCBHrM3Ir%2FDOyC4bXjqyfy7D26KN6glsbJqJcuUUtU4ZOquluLskQEYecr0WhGabmI0Scxur2NCp0alr03zDkxHdgVg%2BwVRlKdZxHv5ym0CZFTK2j7LEjp0F4tOJvZ0fzjb9CVFM9V92UaqDUsm9bN%2FuUurgQ%2BKCmmITgrQ48p4Bv3k54kQT6G%2Bjvl0seIQ9ucGl5Xle3HNshetrE2Ro%2FPvyYqw7%2FmRtfH%2FYdKakfX98%2Fkg3ANZZQ3bCmRmNeMjT7PD4qEIEA49roND5dnS07W9ZGBpj6f%2BbNZsXWf%2F5KRhh2XcvTC%2BYDWKpV%2FT4Iykryr2EfCl6rbu%2FKbTxsyMGSRpzb8tTFmjcqKKPM4%2FcNNlsI9F%2FFEi4CjaRtlmMY0vqraWU4%2F6rQLMTQDxHZ1kEPTv0qMoszetIBX0osA66VYSifN4DBMJLPgt5K1TtQggbSOLNxjl0wPuoaSw8gYiOvDsbPq7a%2FY84%2F9NuUmOLKq1uwIUG8p5cP7nmPXXccm%2B9lyHROvO4Tp9S7Dq79e%2BZqKI2otd%2FH5OdlZzvHWbTN1%2Bse8ulBXMPjwwtcGOqUBfnhodBCVEAFlXbOjlyXPtEiORBUWQXcchC4Gh%2FyUNOVtDbzXpDTihh89pXMiFDZzmUnBstm4w23dACukk0lKjU0yaIoJEwnIH6OwbTqFwta9O4WNStjMK3BXaKbokkIRLw4kiVjsM9gYJe91ERFaBtBHqs%2F9jNZuxH6hj33YwbcWtTvRzRukq6QAJEjU%2FJ3h8QDy%2FGCDl9nDUMM7QLhYZy2QCqHB&X-Amz-Signature=055ffd142430ce76e0a0eb3458cfb9cf945829835612725c4c00807709a2a3c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







