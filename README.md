



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2BTPTIM%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T064333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BA%2BltqweLjlY5S%2B1bsqtfGs3xE4Uw86g3kVDWg2u9vwIgPx6jonVZuzUPD74gCQ9%2FwBuxXqSsop%2BtD1MEFqEqoOkq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDE11AxUHyeeaa4T64SrcA418WSn4kQil1Bp0SlANyPubs%2F91s%2F3YoHVYGp4mVd9l4Wld%2Bhxm2QpFxxXYk44wl1SDP%2FtKLh6yaf7QnueRTumKV6qiJWQOBo%2FD6bXwa2VF8YaWABWKEkQEDzjhfifJrvOqAu1RRYsbaW%2FXqw8hVktypnABRCyqL0tXAFV0yiIa%2FL0DfaUqLRdai8TKF%2BN5DE%2Fa7wR0Ly30paWC0wHjArJvUf9Gu6gdgqbNU64yxwRrbZfDZ4IVRgZtHQkOGjxjockl2Mu8sSjTbo4BDS1pBsiKxOJZ5m23nCSFtTKBMyiC7ShDHqYlo10xKUmSXcuSDZCWwfk%2BNzkUkRlPtod1KFuwhTw0NWfkknI1xJO4Ybp6XHTTYVa5ZetjmVoAmrS65A6Lt21ewGPKdyCwO5zhh%2F1dUmVxo%2FVvvII9YseffQpKebbJlg%2FTPki%2FKRe8oVObUnDVhF%2FvZanhnFaCRL5A4PB31XVyptWzANzyTHKIcsZKQwLsnuFNuWQitAkaxZkyCVdZVOlKwwsAA9WURt%2FKFPjYLKY1%2B15JSyxZhFKQevxehJIcg4tuFcdsWNCUA3FZsPUSSBskthkyIPJeMdBGoaBg2NV1KS5yS9TIl5Byqbyqe3CxFJ8jJ0j%2Fh%2F30MK%2F7%2Fc0GOqUBSgoLBvI%2FGx47cnyeTx4y4WNre%2BT4xDINxxpAD9XBCJ%2BEw%2BiRWhaDprizFuCDcoXBtALamv06LW2zOHIGGwlI8V0AHkqdW3YWLHF%2F4E3%2FY%2BxUdItK9fiDestK%2BqJEKgq0wHlhdMJ6xLJ5BnTKiCOf0vvrdWCMaTRJxHiMDGF4C0sXmoQUbW%2FvELKZXoZV127X3am5CfThzQ0wlW1ja%2BtmDWHl4Jea&X-Amz-Signature=f10c74a07a650a49beec1dda316d0269c0c17ffe3c306990555f92035552b236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2BTPTIM%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T064333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BA%2BltqweLjlY5S%2B1bsqtfGs3xE4Uw86g3kVDWg2u9vwIgPx6jonVZuzUPD74gCQ9%2FwBuxXqSsop%2BtD1MEFqEqoOkq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDE11AxUHyeeaa4T64SrcA418WSn4kQil1Bp0SlANyPubs%2F91s%2F3YoHVYGp4mVd9l4Wld%2Bhxm2QpFxxXYk44wl1SDP%2FtKLh6yaf7QnueRTumKV6qiJWQOBo%2FD6bXwa2VF8YaWABWKEkQEDzjhfifJrvOqAu1RRYsbaW%2FXqw8hVktypnABRCyqL0tXAFV0yiIa%2FL0DfaUqLRdai8TKF%2BN5DE%2Fa7wR0Ly30paWC0wHjArJvUf9Gu6gdgqbNU64yxwRrbZfDZ4IVRgZtHQkOGjxjockl2Mu8sSjTbo4BDS1pBsiKxOJZ5m23nCSFtTKBMyiC7ShDHqYlo10xKUmSXcuSDZCWwfk%2BNzkUkRlPtod1KFuwhTw0NWfkknI1xJO4Ybp6XHTTYVa5ZetjmVoAmrS65A6Lt21ewGPKdyCwO5zhh%2F1dUmVxo%2FVvvII9YseffQpKebbJlg%2FTPki%2FKRe8oVObUnDVhF%2FvZanhnFaCRL5A4PB31XVyptWzANzyTHKIcsZKQwLsnuFNuWQitAkaxZkyCVdZVOlKwwsAA9WURt%2FKFPjYLKY1%2B15JSyxZhFKQevxehJIcg4tuFcdsWNCUA3FZsPUSSBskthkyIPJeMdBGoaBg2NV1KS5yS9TIl5Byqbyqe3CxFJ8jJ0j%2Fh%2F30MK%2F7%2Fc0GOqUBSgoLBvI%2FGx47cnyeTx4y4WNre%2BT4xDINxxpAD9XBCJ%2BEw%2BiRWhaDprizFuCDcoXBtALamv06LW2zOHIGGwlI8V0AHkqdW3YWLHF%2F4E3%2FY%2BxUdItK9fiDestK%2BqJEKgq0wHlhdMJ6xLJ5BnTKiCOf0vvrdWCMaTRJxHiMDGF4C0sXmoQUbW%2FvELKZXoZV127X3am5CfThzQ0wlW1ja%2BtmDWHl4Jea&X-Amz-Signature=50e0b96fa74a27aef0af18ca57d39a24ece77b3c53a5005cbfceb98e9757060c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







