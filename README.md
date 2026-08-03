



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKX7R2PQ%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T142642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDxFlGf5YfJCB0S%2B2JzOPw%2Bf%2BYbHW08v1v4wVOpXzzaMgIgIfkpASTllX4VFIcrZ49rVh6pxSCwIF5gfSLXXeCBAJwqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9u%2FRuZ0lFQWNbF%2FCrcA81ceN%2Bo2Unk3WvOUehPrff7VBti2AB55DFMyX1y527JlBUct%2ByrT2CBi5tBgn17KW5OeFAWcFVuTYBs1m0xCZa5Vl1irlJyaR%2BHXv6zYEe4MtcFR5dry6rMvBWregff3M7X29lGek6n0r2khuIo%2BhUzymj9EgtY9Ls9Xxd%2FFqmBceB2RYLBuMJ5OrY2NLhMVW71co0NxQLLTL3IbLx47VtWWLXiXVVhKOS2LMX4ZaieuUPZV0L7vRWJSUXSmhW6D9PXk5ybRyk9Il9W%2B2JcLskoreOqNHnK6OqE2XR68qhuYorxWbcnO5c%2BOIUnNUNK3qWm%2FBx0g1WoxvDA%2B2TP9gyo%2BNoNlD6s7%2BiR4syEhf3%2FfiYMvNkijBUbjvSttpkuOmXjVgY8bMARp%2B%2BrrvcDthxYmPRFNaLRZJtI%2FWeb9%2FWTzyne%2F%2BAa0jYZP1AALE68hJ3YDmjVQvHdT2KL%2BTtBk8UhW2Flq98JiYafuWUuVjeKWGDVmhDWAGtOLQnaXBhgXxiby%2Bjw0E5N4tKTwJBcjeNJQ9bolZkrWcisSpx6peDxvbv4UMUXR5j%2BNAc357ts%2BHy42dnSO7JyHJYJoUUI2jpqzu%2F57%2B1TJiAYGdLauDBJUL671M%2BnMSq5m71fMKj%2BwdMGOqUBly3X3SuoifSzNNh%2BhUfAL%2BkAPj9FZbeQ07lg2bHkwdi61uBHADaQ%2BisrkHf%2BeguLjAgJNujClAyfPBUA9xsH3AGYeiXwQaTvHHe5chu0GiziGUV4OJsk2dLficOllKVd9B2V259iB0zYUS6WG9sB383SZfftqDisQ7gSP9tYss35Zj9c9ivZcZ97DsELkTzAeK8XphxWm4cdxM1YeMQlUxWgNVrg&X-Amz-Signature=349cd4629e3270d5875fce3c254a82be4e13b970c948ae2aa8422bd0abfc5220&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKX7R2PQ%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T142642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDxFlGf5YfJCB0S%2B2JzOPw%2Bf%2BYbHW08v1v4wVOpXzzaMgIgIfkpASTllX4VFIcrZ49rVh6pxSCwIF5gfSLXXeCBAJwqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9u%2FRuZ0lFQWNbF%2FCrcA81ceN%2Bo2Unk3WvOUehPrff7VBti2AB55DFMyX1y527JlBUct%2ByrT2CBi5tBgn17KW5OeFAWcFVuTYBs1m0xCZa5Vl1irlJyaR%2BHXv6zYEe4MtcFR5dry6rMvBWregff3M7X29lGek6n0r2khuIo%2BhUzymj9EgtY9Ls9Xxd%2FFqmBceB2RYLBuMJ5OrY2NLhMVW71co0NxQLLTL3IbLx47VtWWLXiXVVhKOS2LMX4ZaieuUPZV0L7vRWJSUXSmhW6D9PXk5ybRyk9Il9W%2B2JcLskoreOqNHnK6OqE2XR68qhuYorxWbcnO5c%2BOIUnNUNK3qWm%2FBx0g1WoxvDA%2B2TP9gyo%2BNoNlD6s7%2BiR4syEhf3%2FfiYMvNkijBUbjvSttpkuOmXjVgY8bMARp%2B%2BrrvcDthxYmPRFNaLRZJtI%2FWeb9%2FWTzyne%2F%2BAa0jYZP1AALE68hJ3YDmjVQvHdT2KL%2BTtBk8UhW2Flq98JiYafuWUuVjeKWGDVmhDWAGtOLQnaXBhgXxiby%2Bjw0E5N4tKTwJBcjeNJQ9bolZkrWcisSpx6peDxvbv4UMUXR5j%2BNAc357ts%2BHy42dnSO7JyHJYJoUUI2jpqzu%2F57%2B1TJiAYGdLauDBJUL671M%2BnMSq5m71fMKj%2BwdMGOqUBly3X3SuoifSzNNh%2BhUfAL%2BkAPj9FZbeQ07lg2bHkwdi61uBHADaQ%2BisrkHf%2BeguLjAgJNujClAyfPBUA9xsH3AGYeiXwQaTvHHe5chu0GiziGUV4OJsk2dLficOllKVd9B2V259iB0zYUS6WG9sB383SZfftqDisQ7gSP9tYss35Zj9c9ivZcZ97DsELkTzAeK8XphxWm4cdxM1YeMQlUxWgNVrg&X-Amz-Signature=5090c5d71896e305160d48abbd02de4097e2cf67c4d4db28cd68e144dc95ff9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







