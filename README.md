



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MK7GYWU%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T124257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIEGPwUEsqChGEvw6k9T8klwyGM7pHR9CVdechyCkTN73AiEA7zhm%2BletSOCJ%2BRgUDfzkuvG8JfExd8gB8vggVYJ6vyEqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEagg6Pw1%2BBy9YAi5ircA488ruWOCV18s%2BQIG8koV4TSibD8NrMothnOQeksFzwTYP5Fq8BFJ7rnrTqdyFMzr2MJPVV70phUIwv56SugmaylYpvxbdjCptA9X5lGgYVnIgul%2BbagZ%2BWZaoHkp8%2BgTwD4%2F77nJLTEAmp4VPo0zM1IGKcaDPJwFvDzo3vHjvrB9Qg2yR0zMttpRKmgCSM62ST4JFOQpYN1FRYgG9mQvzt0SJmfSY2BdjscDiUvYli05eL1MSlWVy0T6S082GvOiNxZal%2BeANk9WxVGEA6BnVNpuK7cv6gk3InAPpH38SKfK4BRHUuqydTmH%2FEfLoRUPQPgHU1Q%2BqHhsNfkRchLouYPjzb%2BGcTckRLZ4JZAE%2Fx5AORUOl4WyHCxi8xdwkGh8Aiwz3m2AeCHiIUZ%2BIceMhKwiIpDpZXnXCvb%2FCfHdX3nPKcBrXnAUHR3R4%2BRTgdocPBGN6ulGsTeGXAwl0VUQgpY0wAUBreTwmvUXTUX0hNPTMg8JYiU7a1yYoYpf2iXA%2BGGk%2F0NfFLfbXqcPCzgZ1fVRjEJyVWaSyfIKyYGKAGiw6OtXse2VbDktV6DpUqz6x5iqfVeZ%2B3u%2FhGA2g7C6eLU%2F7I%2FGhstiYJhGoxt9olxZAm4K%2BzZ%2BNEec0dhMLPnqs0GOqUBnSI6Bsrv1%2F59Xhcgt%2F6kRbe3LfV4%2FD86y4F%2FN%2BChSDI%2BKXV%2FUb8oe93yhM5zkB3V4mjG6ceErKou2fD0CSzEO6mXoJP2DJyt3%2FAp2JfJe2HIOAOdBWuOetzKFd5OsLDtLgZbF%2FxE5Pnyo8HPMGda28pa7Q5NqzgD1I5xHBqVSuvhfv2lTfVwdQo%2B9Y6kLklztCYy2oUJeXLGBNMx2T3C6hcLTzWa&X-Amz-Signature=bc96a84703ec26aa4c241fa843b16ea9089d9f264bc402048d68526814078bf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MK7GYWU%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T124257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIEGPwUEsqChGEvw6k9T8klwyGM7pHR9CVdechyCkTN73AiEA7zhm%2BletSOCJ%2BRgUDfzkuvG8JfExd8gB8vggVYJ6vyEqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEagg6Pw1%2BBy9YAi5ircA488ruWOCV18s%2BQIG8koV4TSibD8NrMothnOQeksFzwTYP5Fq8BFJ7rnrTqdyFMzr2MJPVV70phUIwv56SugmaylYpvxbdjCptA9X5lGgYVnIgul%2BbagZ%2BWZaoHkp8%2BgTwD4%2F77nJLTEAmp4VPo0zM1IGKcaDPJwFvDzo3vHjvrB9Qg2yR0zMttpRKmgCSM62ST4JFOQpYN1FRYgG9mQvzt0SJmfSY2BdjscDiUvYli05eL1MSlWVy0T6S082GvOiNxZal%2BeANk9WxVGEA6BnVNpuK7cv6gk3InAPpH38SKfK4BRHUuqydTmH%2FEfLoRUPQPgHU1Q%2BqHhsNfkRchLouYPjzb%2BGcTckRLZ4JZAE%2Fx5AORUOl4WyHCxi8xdwkGh8Aiwz3m2AeCHiIUZ%2BIceMhKwiIpDpZXnXCvb%2FCfHdX3nPKcBrXnAUHR3R4%2BRTgdocPBGN6ulGsTeGXAwl0VUQgpY0wAUBreTwmvUXTUX0hNPTMg8JYiU7a1yYoYpf2iXA%2BGGk%2F0NfFLfbXqcPCzgZ1fVRjEJyVWaSyfIKyYGKAGiw6OtXse2VbDktV6DpUqz6x5iqfVeZ%2B3u%2FhGA2g7C6eLU%2F7I%2FGhstiYJhGoxt9olxZAm4K%2BzZ%2BNEec0dhMLPnqs0GOqUBnSI6Bsrv1%2F59Xhcgt%2F6kRbe3LfV4%2FD86y4F%2FN%2BChSDI%2BKXV%2FUb8oe93yhM5zkB3V4mjG6ceErKou2fD0CSzEO6mXoJP2DJyt3%2FAp2JfJe2HIOAOdBWuOetzKFd5OsLDtLgZbF%2FxE5Pnyo8HPMGda28pa7Q5NqzgD1I5xHBqVSuvhfv2lTfVwdQo%2B9Y6kLklztCYy2oUJeXLGBNMx2T3C6hcLTzWa&X-Amz-Signature=ce53980510a25a9ad9205718014a1619fc798bdb4de86435508b79a2cecf96d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







