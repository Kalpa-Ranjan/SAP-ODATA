



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHERIZG2%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T123640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBDX5EtfelUNNCkiWGtmE1E70xZckq%2Fi096AL1v2nf2tAiEAiO7%2Fbok5W7bW0%2FpM%2Fljsz4SsRILooKMTQtjGWxcmdyIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDNsZZDjxa3nEXhJO%2ByrcA0aFUVGvQt9%2BbdOWfFZwE8Y3PxaL78fljiYmPrOvU0CTBHXpK9rfwfLS%2FpWH62MbYML8WQrrvLNds4tqadAlkrv%2Fo0tR6GGpM5lyG2VBt2Y4bw0Of6Qb4vtfBKxGGiv%2F7vmcCG1bXNQtzlJin2C1nD2oSKjv6WsG7ErlcLxQrtLL8ktY4hQBN9QPKjQF29rZXF3dTziNm2ksruxyVWtWg%2F0xTExUAJ3Rbdvx1OQKUPJgSmITFiYKcGGEB3uWkBq3BOWCVRE0Dq1O1wzcHqC7HpOTIPQkKUTutIhp2QOd5SovZC3AcA%2FlRAS%2FR99sZEJ546mw%2B%2FiFM6DacUwmB%2BWb0ImpU3f5dNSxiEYVmhhZvJ33AsUIWbk5ug9%2BgLtXqiQGKQYhoj2KxiRtcCTY52cvxqn4tTHs2R0%2FOZyBKldThx9zJWYJ740GRlRUrmGcraMY44suOb7RCyikocTCmVzKiMAXoQt4Qd5i7vMWVUydLKM%2F5SdOhME4465UNn%2Fw8pQOxDsUMx4nuURX6qfWPlEpFtN6%2BwuCAdDFaAp3%2BTfnhIxBDnMFHY679e32irSTt%2FTZQjAlYjRd%2B6CUvondXHrT1%2Fd7kuRF%2BJiw9snz1CQ74ck3U7ULb9RMd3v7SP3bMP2NttQGOqUBxtBZftJRwT85wpJgg6DD0Sk8%2FjS8V%2FhWQDPVtxBr0fEq0UmROyLrmRQc%2B2XCcoh2vAP2B8naToBTQ4p5oQVtSIwQaZZ4Gu3JvzgKBOsoidA8Tv2U5bThAHhaxpqOnPO06kbY3UASIlkKJE%2FrYmOA54oawF7hMxKAqgnzX7GZpgGrlkPsmJXY52PCntq67Q7x%2FJjqizVgc6S4hKWuvKVS1dd0y0UI&X-Amz-Signature=0e1fa94c21890193a0c5719ec3158d45a72c33e1a7c0828f486d1eb85ba685a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHERIZG2%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T123640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBDX5EtfelUNNCkiWGtmE1E70xZckq%2Fi096AL1v2nf2tAiEAiO7%2Fbok5W7bW0%2FpM%2Fljsz4SsRILooKMTQtjGWxcmdyIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDNsZZDjxa3nEXhJO%2ByrcA0aFUVGvQt9%2BbdOWfFZwE8Y3PxaL78fljiYmPrOvU0CTBHXpK9rfwfLS%2FpWH62MbYML8WQrrvLNds4tqadAlkrv%2Fo0tR6GGpM5lyG2VBt2Y4bw0Of6Qb4vtfBKxGGiv%2F7vmcCG1bXNQtzlJin2C1nD2oSKjv6WsG7ErlcLxQrtLL8ktY4hQBN9QPKjQF29rZXF3dTziNm2ksruxyVWtWg%2F0xTExUAJ3Rbdvx1OQKUPJgSmITFiYKcGGEB3uWkBq3BOWCVRE0Dq1O1wzcHqC7HpOTIPQkKUTutIhp2QOd5SovZC3AcA%2FlRAS%2FR99sZEJ546mw%2B%2FiFM6DacUwmB%2BWb0ImpU3f5dNSxiEYVmhhZvJ33AsUIWbk5ug9%2BgLtXqiQGKQYhoj2KxiRtcCTY52cvxqn4tTHs2R0%2FOZyBKldThx9zJWYJ740GRlRUrmGcraMY44suOb7RCyikocTCmVzKiMAXoQt4Qd5i7vMWVUydLKM%2F5SdOhME4465UNn%2Fw8pQOxDsUMx4nuURX6qfWPlEpFtN6%2BwuCAdDFaAp3%2BTfnhIxBDnMFHY679e32irSTt%2FTZQjAlYjRd%2B6CUvondXHrT1%2Fd7kuRF%2BJiw9snz1CQ74ck3U7ULb9RMd3v7SP3bMP2NttQGOqUBxtBZftJRwT85wpJgg6DD0Sk8%2FjS8V%2FhWQDPVtxBr0fEq0UmROyLrmRQc%2B2XCcoh2vAP2B8naToBTQ4p5oQVtSIwQaZZ4Gu3JvzgKBOsoidA8Tv2U5bThAHhaxpqOnPO06kbY3UASIlkKJE%2FrYmOA54oawF7hMxKAqgnzX7GZpgGrlkPsmJXY52PCntq67Q7x%2FJjqizVgc6S4hKWuvKVS1dd0y0UI&X-Amz-Signature=850bf038839c149ba80c883775fd12938ef04297b0438598c6d397bea2956144&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







