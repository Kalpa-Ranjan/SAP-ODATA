



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMRSWAS4%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T062350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCizn%2BSAW3VDHTIPtEeZp7pgn%2BwCCeIGhbR%2Ff2hdh%2Fj7QIgPCaC6cs6edrvUgGJ5R1VrdmGfLxdgFvz4O1Vc4DW5XUqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJGZ8PDqSwl5mVno%2FircA2XKC%2Ff%2F%2FbYyUPsNm%2B%2Bmhtt%2FJuN7IpWAqGI8dpU3CcmcyTsZumDytEuA%2BY6my9KFIh4CaP%2BBey8SICu95uN6bCdfXvq1gJII6%2FliqzLxs1eaCfSNLPTw5gI0Ql4jBa0AyjdC9rmDnIJ5PmWxBtUzAxr%2FrdDxob0XSCJ2SjJkpKeUQMVfWAfqbJaCBD60JuYeuKhkkK6yIxRr7ojQ57MXyLtH1Qj67uMeR%2BQ1HoKv20A27fL39L4%2FJQNmhVX8IEY0H4dg%2FtyOnIw0HFiLPuMujpcU3KqUIfQKF8OXHYbNChS4dc%2Fg%2BZ%2BVfPF6aZGu%2FqzZqUtjQkpsTDJikkosTRKoFwEqXo4gBt11AK%2FTgcWmVWR36ykwkm%2Bm5%2F3E57W2JDzyDr3Xp8O2mkD0C45vScl3pWSGQy8Chz%2FfkAO3o3UiXrm%2Bm3J8Lpf%2FyqGdZSQza0ngp9dMjnWC8NO486z2CH2pO2xd9UfYfRVrmdFupih60rmh5ZXnGv4R%2FrURvif1el9mPVaG2ZvsZcgWUh6IqtvEfoFB44FMKnV2YKFuHdrbMIh3lEX6%2BUSnOUqKbnDbODFEZ0aXUsaro%2BabiTynLIZ0L17Xkb%2FVN2w8aH7dV1PLMDBaHFMk3yZNhGRA%2FemeMOWPtsgGOqUBRj65jRJuJM%2Bgv2VHAiCaorJnCh4awbpaSw4SVXudvFg6ztmGZj%2FYpJPoMU5bQ2BYYFwvOI%2FuHTP8iXMwgwmR9BNcPAUrIMpnfKD6RWiFLDUpvncENS7DesllNVNqFVyDp099eEoKKqJXJ4hXUFXeJkgcd9ABcs0fGfZjVbN%2FP5kDLSjpLxFAKzGnr5CK%2BHMQrgKZiOS6BWu%2BKJUfk%2B6tnuVonFoI&X-Amz-Signature=095454f7e4c250d198be1bd526832bd064d7de285b04e9da7255aad8577e7223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMRSWAS4%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T062350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCizn%2BSAW3VDHTIPtEeZp7pgn%2BwCCeIGhbR%2Ff2hdh%2Fj7QIgPCaC6cs6edrvUgGJ5R1VrdmGfLxdgFvz4O1Vc4DW5XUqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJGZ8PDqSwl5mVno%2FircA2XKC%2Ff%2F%2FbYyUPsNm%2B%2Bmhtt%2FJuN7IpWAqGI8dpU3CcmcyTsZumDytEuA%2BY6my9KFIh4CaP%2BBey8SICu95uN6bCdfXvq1gJII6%2FliqzLxs1eaCfSNLPTw5gI0Ql4jBa0AyjdC9rmDnIJ5PmWxBtUzAxr%2FrdDxob0XSCJ2SjJkpKeUQMVfWAfqbJaCBD60JuYeuKhkkK6yIxRr7ojQ57MXyLtH1Qj67uMeR%2BQ1HoKv20A27fL39L4%2FJQNmhVX8IEY0H4dg%2FtyOnIw0HFiLPuMujpcU3KqUIfQKF8OXHYbNChS4dc%2Fg%2BZ%2BVfPF6aZGu%2FqzZqUtjQkpsTDJikkosTRKoFwEqXo4gBt11AK%2FTgcWmVWR36ykwkm%2Bm5%2F3E57W2JDzyDr3Xp8O2mkD0C45vScl3pWSGQy8Chz%2FfkAO3o3UiXrm%2Bm3J8Lpf%2FyqGdZSQza0ngp9dMjnWC8NO486z2CH2pO2xd9UfYfRVrmdFupih60rmh5ZXnGv4R%2FrURvif1el9mPVaG2ZvsZcgWUh6IqtvEfoFB44FMKnV2YKFuHdrbMIh3lEX6%2BUSnOUqKbnDbODFEZ0aXUsaro%2BabiTynLIZ0L17Xkb%2FVN2w8aH7dV1PLMDBaHFMk3yZNhGRA%2FemeMOWPtsgGOqUBRj65jRJuJM%2Bgv2VHAiCaorJnCh4awbpaSw4SVXudvFg6ztmGZj%2FYpJPoMU5bQ2BYYFwvOI%2FuHTP8iXMwgwmR9BNcPAUrIMpnfKD6RWiFLDUpvncENS7DesllNVNqFVyDp099eEoKKqJXJ4hXUFXeJkgcd9ABcs0fGfZjVbN%2FP5kDLSjpLxFAKzGnr5CK%2BHMQrgKZiOS6BWu%2BKJUfk%2B6tnuVonFoI&X-Amz-Signature=3d6f714dab3fbc51ee051897eeb556dffec8e02720d143e6be827e84031ecab8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







