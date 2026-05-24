



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QF2R5TX%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T190949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxUQDZ6cySbOrZk5bcvKLh8RxoYX%2F1WPQw77Z56BpxGAiAL3A1bmO5b4Ycc4dQddk0RItyOARdGzUboZIQZc1llpCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMCY4ul3BNQvjT45ZEKtwDqEAVdMCbnFlsglaBLMe4ppsNJjYSyIZqlEV4m9m%2FCXT5T5BPcqGANRyloemC3IPii47VnwUGBF%2BMTpMp6GhhwLNhF98%2FqhNHok6YaO0d4e%2FEgisFo7w2O07rVO%2FAGqy448lv2rOfIQyg0SmuyXdsLu%2FdtDnauqSFGQiSi4bOx%2BWAuPfmeCleJmGDzARs1tIC13zunpNcBRJBsGj%2F%2Fbz2Mytv4fPIiLzXnuXAXeWyL%2FYmWAC1DajnoHQbWwkcx7QN%2FSScmqG57uCP20VHiq5ihKD8lRKzyYmdu4dqybUAS%2FlH24gJbgzbMw3L5cmWUc689siZj6qQUCbF%2F1htPQgQI6F67Yn2m4kd8MNdDKmPsrl%2F1215GsukHqA99q8cptjJtMeC6%2B99tYT1cQ1fug52XoYYIyAtOXxVqhw4w9HQ9uiIyu7RpI0ngXATdN0KdfIMrXPBZcQ2khkW4DVjGCFhybH74BglbnOJcFTLBcKOAMDzhjhTLBgCq67x3Cw7ppDdFusrU8I6cYYiLle1B%2FEo0%2Fmi3VDsocDQG1dqu2gRKvPazT7B%2Bl0SzyWqe6cuMoAdurpEvFOMT41KQ4aKVRQ2GEoIcyTzS%2FToFMAJxSSnutjIkh8KWz58IHRIn4ow5ofN0AY6pgHiGUrVsNpOEkouETUwCaJ7wFormPFLxklT2wvGq1my20Coc%2FVA2iD2Nw64ns5L5SLqpq1XRbFvrtdvmQTWXkRnEffF3Gnx7PZY1Xg1oAWojgUD0KJCVPLoHvBsz8aVIZ8l4VnK%2BbaXaGVXPjzRXNKccn8AsdEvjFll05YE7VCmfTSngV573i0Oq0EjMXqRmUZXWx9RLXWyku2XyjSjnEMOVwm5fHrw&X-Amz-Signature=cae1c1009ff3b0a6cd997e22549f5ba2b37f3ab1f32cb748d1f7d74da9302b97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QF2R5TX%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T190949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxUQDZ6cySbOrZk5bcvKLh8RxoYX%2F1WPQw77Z56BpxGAiAL3A1bmO5b4Ycc4dQddk0RItyOARdGzUboZIQZc1llpCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMCY4ul3BNQvjT45ZEKtwDqEAVdMCbnFlsglaBLMe4ppsNJjYSyIZqlEV4m9m%2FCXT5T5BPcqGANRyloemC3IPii47VnwUGBF%2BMTpMp6GhhwLNhF98%2FqhNHok6YaO0d4e%2FEgisFo7w2O07rVO%2FAGqy448lv2rOfIQyg0SmuyXdsLu%2FdtDnauqSFGQiSi4bOx%2BWAuPfmeCleJmGDzARs1tIC13zunpNcBRJBsGj%2F%2Fbz2Mytv4fPIiLzXnuXAXeWyL%2FYmWAC1DajnoHQbWwkcx7QN%2FSScmqG57uCP20VHiq5ihKD8lRKzyYmdu4dqybUAS%2FlH24gJbgzbMw3L5cmWUc689siZj6qQUCbF%2F1htPQgQI6F67Yn2m4kd8MNdDKmPsrl%2F1215GsukHqA99q8cptjJtMeC6%2B99tYT1cQ1fug52XoYYIyAtOXxVqhw4w9HQ9uiIyu7RpI0ngXATdN0KdfIMrXPBZcQ2khkW4DVjGCFhybH74BglbnOJcFTLBcKOAMDzhjhTLBgCq67x3Cw7ppDdFusrU8I6cYYiLle1B%2FEo0%2Fmi3VDsocDQG1dqu2gRKvPazT7B%2Bl0SzyWqe6cuMoAdurpEvFOMT41KQ4aKVRQ2GEoIcyTzS%2FToFMAJxSSnutjIkh8KWz58IHRIn4ow5ofN0AY6pgHiGUrVsNpOEkouETUwCaJ7wFormPFLxklT2wvGq1my20Coc%2FVA2iD2Nw64ns5L5SLqpq1XRbFvrtdvmQTWXkRnEffF3Gnx7PZY1Xg1oAWojgUD0KJCVPLoHvBsz8aVIZ8l4VnK%2BbaXaGVXPjzRXNKccn8AsdEvjFll05YE7VCmfTSngV573i0Oq0EjMXqRmUZXWx9RLXWyku2XyjSjnEMOVwm5fHrw&X-Amz-Signature=49b74957c05f73d26c94703e27b565cf7584d444f507e12d4c8ba85acad8aa9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







