



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X43RMFRN%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T064021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiuZuvn9KTDQUiwNsO7zj5RV15BcJ0mMPvC3g8S%2BlZOgIgSgFncHEE%2BvhEAQP9BpurMdXfTx13ce2AEjnBDmM1LxYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPFWfXLSEtCfliHm0yrcA9wuBqv%2FcqLw5siSSH1lw2gy3rXurUNqQnd8nh%2B9tVC%2BA9pgPfPLQCElT1isBMSf8yv%2BwqgPbTR%2FhUqQnI6U4NmYJgvMsOfBY6HfYDY3H%2Fo9U6ggFJnoNBs7AWnbDJ8EZvPpiQr6sBr%2Fgo8jSF1ZkNyEOyMJfhIC3v88sj5LSuBwDKurgLP6%2FwJxMuAL%2BSe1M%2Fd0ifRCMj%2B%2BwMiL391XnUxQNR6gcM2ro3foCu03riVuDKpTxYW3PMwxr6Vj%2BYStpFkaMFHnudmRPHR1e6wJnK9s6noxFivjzjC78fWt9YV9aeRMiYWG0FnOlK99tB5s57KhBAcpiJ5HYXx6lndF8e0uGo0rGa4ZiYL339%2B6WuqPhSILJJp0rwF7jfj4vDUkq%2FFHryh436kOfXn7BjSMGRp223GPc%2B1eM%2Bbk6UV%2BB%2Bvxj2e06R0FtZ6k%2FpaXnKuz%2BGKOMB46BuKalpCAYTi3nUv3%2B3eNgBHvt4aHgOEFMbaspOIJHaFXNvxgEuR7inJzPlXfvObZ3cXMW41jfYbgkw44EWsMq3rV838HJG12DFT7JkptpgD%2Fhqezf%2Bb4o063JBuv3Dtid5mqDH1X1RYmip%2F%2FMI6Dfw0R%2B1DZ5WTRuIuPeRWu2P35MQt7VY0%2BMMfF6swGOqUB%2F04mMZwMn1KqPaFe60SqRsQCAt3aoMrSa3T8dCys3qnuphXmWtvIthxQUPUzAWJK6Q3424CPivlqRH%2Bzyn8MIEXwPJAx4NVlqRR22zzrCzcR5d8KSW%2Fvy5t3MVD4iFF8yHIVmJ7KfX%2FNyLCIZVBGobymPgzgbNk8ixULymcZLVtVFjRmXMN8zYKn0C6I1ZukliZ3Sw8asMwCiUWpGZS7H%2BGFoXPl&X-Amz-Signature=2c3ef17dfc162db67f4d6bdfd1f8c1b26b09ac5b7f096d30dca2c29d7a5c6abc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X43RMFRN%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T064021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiuZuvn9KTDQUiwNsO7zj5RV15BcJ0mMPvC3g8S%2BlZOgIgSgFncHEE%2BvhEAQP9BpurMdXfTx13ce2AEjnBDmM1LxYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPFWfXLSEtCfliHm0yrcA9wuBqv%2FcqLw5siSSH1lw2gy3rXurUNqQnd8nh%2B9tVC%2BA9pgPfPLQCElT1isBMSf8yv%2BwqgPbTR%2FhUqQnI6U4NmYJgvMsOfBY6HfYDY3H%2Fo9U6ggFJnoNBs7AWnbDJ8EZvPpiQr6sBr%2Fgo8jSF1ZkNyEOyMJfhIC3v88sj5LSuBwDKurgLP6%2FwJxMuAL%2BSe1M%2Fd0ifRCMj%2B%2BwMiL391XnUxQNR6gcM2ro3foCu03riVuDKpTxYW3PMwxr6Vj%2BYStpFkaMFHnudmRPHR1e6wJnK9s6noxFivjzjC78fWt9YV9aeRMiYWG0FnOlK99tB5s57KhBAcpiJ5HYXx6lndF8e0uGo0rGa4ZiYL339%2B6WuqPhSILJJp0rwF7jfj4vDUkq%2FFHryh436kOfXn7BjSMGRp223GPc%2B1eM%2Bbk6UV%2BB%2Bvxj2e06R0FtZ6k%2FpaXnKuz%2BGKOMB46BuKalpCAYTi3nUv3%2B3eNgBHvt4aHgOEFMbaspOIJHaFXNvxgEuR7inJzPlXfvObZ3cXMW41jfYbgkw44EWsMq3rV838HJG12DFT7JkptpgD%2Fhqezf%2Bb4o063JBuv3Dtid5mqDH1X1RYmip%2F%2FMI6Dfw0R%2B1DZ5WTRuIuPeRWu2P35MQt7VY0%2BMMfF6swGOqUB%2F04mMZwMn1KqPaFe60SqRsQCAt3aoMrSa3T8dCys3qnuphXmWtvIthxQUPUzAWJK6Q3424CPivlqRH%2Bzyn8MIEXwPJAx4NVlqRR22zzrCzcR5d8KSW%2Fvy5t3MVD4iFF8yHIVmJ7KfX%2FNyLCIZVBGobymPgzgbNk8ixULymcZLVtVFjRmXMN8zYKn0C6I1ZukliZ3Sw8asMwCiUWpGZS7H%2BGFoXPl&X-Amz-Signature=3876131bf04df2412f33ede1ce3185921623afa57448a708f037645fc76695d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







