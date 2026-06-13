



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X43RM5IV%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T134856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGxbHXcg4OgNMK%2BIFGy9extEye60sBTSn2zk1DnJrMhdAiEA4HZRzOfbOqEpB%2BeEY5cux00ylZHI3%2FKUv%2B%2BGGCrJh%2FAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKyoPJ4yM6eII4w3wCrcAw12fboTJ4brV3BRBUdCPYXJOgm77uHX5tlB3YDbzesszT36ZYI8%2ByAPdYge%2BiQvP%2B1ZKrUd3h7PP5sTlVt%2FizRGhxPAPnI%2BTLaQ5VJ3o8ZLMjyXgLNuES%2Fj7WQK%2FPcJmwIxcyhticg2HKyZDpGhsKDPmV5fTLR95CiqbRtLjJ48iHBw0qRsscflPNkWJ%2BY6EkiqSSc1EerDG0mbFZ%2Fs5YdZpYrWEB%2FCBBM21yR%2FI1PZb9w8qZ%2FV0SsJJCkJXUBQe8G9k5T0biGaOifLgMLfZuvwsFd593z5whw1YeAawkXJ0hUHy1aabXZQLIFfQvg65p0AvrBf%2FzvG%2FGuLU%2FwGiqOLnvAR4IXWXC3ZjPeF8Qgk31pqSnFWVNvzQWEx%2BTTw6%2Bcte8kss8ytuuQyMDuquKHFRgcHZjZAe1NgTxZOPofnMwCwGqKvTOrr50fGt1NT5Tx%2F1GbRxYgWXLfdYCDdsQACKs5JZuyPRjEnzqdtE9KbH8yMKBjVD3Bh9pwMTyMjK9QTCOZppriVHu731ch657k3OTeLWX1qcS9GVBvq79TwjvNqZgOP6eV1ndlWow4wC5wyKAJ2vqa3VVQMKz7a2eZyMmJ4JlRLHSurDkp8yUQJk4JpmF56JldZ0r%2B5MOrGtNEGOqUBGjgm9XkztWMEP2DpDIkHoasddGNhbyA9f30hAygC%2BU1m5xq8koy1SS%2B1fqdYkxSWh3RWTjIYGrHh24rXJ65P2D9NnSJbo3gOXojKqtxxItGzUukBjvqCqukaMphvomcxgm96407Oq2pFOUtqt2pAAgINVpuABxz3O7fPd5NDYI17eFquDUNqJ2NlP7fZIrsHLXatn5MlnfPJboMt88A2mQXL%2BSoy&X-Amz-Signature=53ace8d41f67d3e89a56690ec52e9a339c48fccfff4551df4ce94ae9b2a99ec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X43RM5IV%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T134856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGxbHXcg4OgNMK%2BIFGy9extEye60sBTSn2zk1DnJrMhdAiEA4HZRzOfbOqEpB%2BeEY5cux00ylZHI3%2FKUv%2B%2BGGCrJh%2FAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKyoPJ4yM6eII4w3wCrcAw12fboTJ4brV3BRBUdCPYXJOgm77uHX5tlB3YDbzesszT36ZYI8%2ByAPdYge%2BiQvP%2B1ZKrUd3h7PP5sTlVt%2FizRGhxPAPnI%2BTLaQ5VJ3o8ZLMjyXgLNuES%2Fj7WQK%2FPcJmwIxcyhticg2HKyZDpGhsKDPmV5fTLR95CiqbRtLjJ48iHBw0qRsscflPNkWJ%2BY6EkiqSSc1EerDG0mbFZ%2Fs5YdZpYrWEB%2FCBBM21yR%2FI1PZb9w8qZ%2FV0SsJJCkJXUBQe8G9k5T0biGaOifLgMLfZuvwsFd593z5whw1YeAawkXJ0hUHy1aabXZQLIFfQvg65p0AvrBf%2FzvG%2FGuLU%2FwGiqOLnvAR4IXWXC3ZjPeF8Qgk31pqSnFWVNvzQWEx%2BTTw6%2Bcte8kss8ytuuQyMDuquKHFRgcHZjZAe1NgTxZOPofnMwCwGqKvTOrr50fGt1NT5Tx%2F1GbRxYgWXLfdYCDdsQACKs5JZuyPRjEnzqdtE9KbH8yMKBjVD3Bh9pwMTyMjK9QTCOZppriVHu731ch657k3OTeLWX1qcS9GVBvq79TwjvNqZgOP6eV1ndlWow4wC5wyKAJ2vqa3VVQMKz7a2eZyMmJ4JlRLHSurDkp8yUQJk4JpmF56JldZ0r%2B5MOrGtNEGOqUBGjgm9XkztWMEP2DpDIkHoasddGNhbyA9f30hAygC%2BU1m5xq8koy1SS%2B1fqdYkxSWh3RWTjIYGrHh24rXJ65P2D9NnSJbo3gOXojKqtxxItGzUukBjvqCqukaMphvomcxgm96407Oq2pFOUtqt2pAAgINVpuABxz3O7fPd5NDYI17eFquDUNqJ2NlP7fZIrsHLXatn5MlnfPJboMt88A2mQXL%2BSoy&X-Amz-Signature=f00dcc3cf6b82632fec4ede133c2fa177ed5283f2c2b841746e29e0ed8cfdeec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







