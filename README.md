



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQPM25V5%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T033357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdzkHdJ3K%2FAPbhpibwgeVfhB8Tf9lR6LM5zWT2TjfyUgIhAO9LAhBoLy7q2GwEv3hLgOhYnAUuwdnkpLuICKe%2FBTGxKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztkNThnUl5q8NW5jsq3ANcX2hyAmtiE1%2FpnGgIns7MWjgEERy6uweD0NfQtsvKtaTXKVlyCClOeZ93QlY%2BE%2Fn6jHDjqWL5THMELb5FfFOjeCnC2ofdt3Ia6QSqLGz3BcBi%2FyiVPs0VIUDljyCQfOoqSVooruUm8UegyewsoTQrS594krNOtZrGwGIhCJuWE7l9IN9xP8LRUwfgFoeovXVqBuaEU7CA2bnymrp5l0F7HscDlvuIq04asaFyKRW5F%2FqphzOMfvmN1svnQ0ZDalHpge9wjw%2FR1jMeSK41LjSCAJXxIEle7Mql%2BA1F%2B7rOSGBwWBKt%2FUFSuvkV2jE8yJSLCckW7BM4LI5mbW6HZbGX1CTgTIDHnM%2Fcnek9GFI3drLFwH9koXn4ghn2OcEaVa29rkyHW%2B3rEx9wUe34eRU4I68qHfkOAtXY2pu6PVFYgSHf2b1wc7%2F5CvD212CBH6A2R148uPvDc7RKaUSERMjv6jfHFHmGzUW8O0RVXtJEFaYUYSU4t2JBtxVAfCZaNBQayEJGoCYaoXRksyvD7jxl892WJg6T186XeFv%2FlfpunJhtkdsvDo%2B2rJ1QAKrx37P8cf9O7ReHd7GeozPKWp1A9dHKyxx%2F%2BDcXXsc3QFKmqfgM0b%2BcCsmuOE9ZijCjt8fRBjqkAWj2495rxfmP0e3QCW9W9adFU4mmkJFjn1sFWg3t6e7jKnznpC6ciU3mrzR0FExHK8yt3rLxVms5w99t%2FGMlDYcAUuPhp%2BaRweb4WvQuB8ozSPZKbrKW6p99%2BNSUL%2FfyJUCrOgPWS4bb4051TunWY7wD8WMi5cRCudUz9vv8aem6Vzi9kv5yhXc8qoWZu0g7RRVyAuBOPC%2FBmwrHlyvo2YQuFN2n&X-Amz-Signature=d987cc9c7bf0f817bfacfedc9d037f483ddb0f2aaeadbde45a467be773115e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQPM25V5%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T033357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdzkHdJ3K%2FAPbhpibwgeVfhB8Tf9lR6LM5zWT2TjfyUgIhAO9LAhBoLy7q2GwEv3hLgOhYnAUuwdnkpLuICKe%2FBTGxKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztkNThnUl5q8NW5jsq3ANcX2hyAmtiE1%2FpnGgIns7MWjgEERy6uweD0NfQtsvKtaTXKVlyCClOeZ93QlY%2BE%2Fn6jHDjqWL5THMELb5FfFOjeCnC2ofdt3Ia6QSqLGz3BcBi%2FyiVPs0VIUDljyCQfOoqSVooruUm8UegyewsoTQrS594krNOtZrGwGIhCJuWE7l9IN9xP8LRUwfgFoeovXVqBuaEU7CA2bnymrp5l0F7HscDlvuIq04asaFyKRW5F%2FqphzOMfvmN1svnQ0ZDalHpge9wjw%2FR1jMeSK41LjSCAJXxIEle7Mql%2BA1F%2B7rOSGBwWBKt%2FUFSuvkV2jE8yJSLCckW7BM4LI5mbW6HZbGX1CTgTIDHnM%2Fcnek9GFI3drLFwH9koXn4ghn2OcEaVa29rkyHW%2B3rEx9wUe34eRU4I68qHfkOAtXY2pu6PVFYgSHf2b1wc7%2F5CvD212CBH6A2R148uPvDc7RKaUSERMjv6jfHFHmGzUW8O0RVXtJEFaYUYSU4t2JBtxVAfCZaNBQayEJGoCYaoXRksyvD7jxl892WJg6T186XeFv%2FlfpunJhtkdsvDo%2B2rJ1QAKrx37P8cf9O7ReHd7GeozPKWp1A9dHKyxx%2F%2BDcXXsc3QFKmqfgM0b%2BcCsmuOE9ZijCjt8fRBjqkAWj2495rxfmP0e3QCW9W9adFU4mmkJFjn1sFWg3t6e7jKnznpC6ciU3mrzR0FExHK8yt3rLxVms5w99t%2FGMlDYcAUuPhp%2BaRweb4WvQuB8ozSPZKbrKW6p99%2BNSUL%2FfyJUCrOgPWS4bb4051TunWY7wD8WMi5cRCudUz9vv8aem6Vzi9kv5yhXc8qoWZu0g7RRVyAuBOPC%2FBmwrHlyvo2YQuFN2n&X-Amz-Signature=17190d56b21f41eb34d9bd35fca84aab52fd1e0667ff4f2331e23f0e95cc59cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







