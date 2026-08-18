



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4NJCDM3%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T005442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICyWpR32mkwOjyoO20jsMXQIl7RKr2kqDONVD%2BxGOdB8AiEAz3vKDJt2s30w2sJEOHkJfaAotf20wz90muzMoyaRWT4q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDH%2BxoW2Rl0lIFSVg1ircAxS%2FxZxcVKS03HesvnI7U55PtUElwLazrR1ra184fJU8QnpBQ87DQH6Ns%2BsRuffIUV8aDCI1o19RvuHBKP%2BHMcPpL0kZzUA%2FD0AhF65ql0WeScamPjayTf%2F181cXmSKUeRspb%2FsZx6SXuPfmBMsz0OSIxchlXODDerJfQjMDAlYLTUtz6gO32nt57q9y3cFcsD2yz7k8oHryw%2BN7u0VQZnnMTAMdhtEFqnwtD7OPBu15NqYM6FOHw021et76ZF5lO4kIS%2FTzkcEYcgBnLHrRAYpXy3sE4X2HjZ2YfbgPV7pp7%2Bbg%2FG5G%2F1S%2ByRgjzFpXdEag8xOQvbzq1Ee609IKvUsAZ%2BtnBYJtpQDg1%2BY%2BEvHqE7Xse6DibEZlVCwup8WZPUyS8hiDK2Mstk2TjLbeL8WJWrAVddg94YRgX2hoLeAdkRxiXzqhgLNMYRlJyYYNDJhpDACMp616IrRJNDUHFa4xXt8vt5HMotqjgCkvaW0R7Co735NtNof5vfmeUg5F7ks4vJ468ZdnG4i7PnWldpVkAwUqgYZ0ju2LgwRWj2DIEkWEIK%2BeS4%2BoR1hztIXsoo23NqAX6OQMaInxm5gxviFL%2B4kBCfN2X4QxzMZCat9PHrLKC47G8QalpYZuMNmbjtQGOqUBeayPqQR665p0bY4Sy7vAZuf7B%2F%2FQbfbjgL9eUz%2BrQcTlEdt%2BNz8RN0sh823LT6GWhDB5XoKKLz1rkv1LqVwu1uSTo7wJZfoe%2FQT4PGAbBGcH5XyMGBH1IwanjyVa6A3y108stFBpjzDtILNKatRUVk9PxVtze7ufr2ttMhRxiVYOHQm%2FJCIGB9tBpslLJL25Qd7Guyz0DqHo0K18e3N3j0v5%2BJYK&X-Amz-Signature=b2a835477bbdff7f4c8bd080e09c4952d04d62d843b4c0f6cd04c4971ebec290&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4NJCDM3%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T005442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICyWpR32mkwOjyoO20jsMXQIl7RKr2kqDONVD%2BxGOdB8AiEAz3vKDJt2s30w2sJEOHkJfaAotf20wz90muzMoyaRWT4q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDH%2BxoW2Rl0lIFSVg1ircAxS%2FxZxcVKS03HesvnI7U55PtUElwLazrR1ra184fJU8QnpBQ87DQH6Ns%2BsRuffIUV8aDCI1o19RvuHBKP%2BHMcPpL0kZzUA%2FD0AhF65ql0WeScamPjayTf%2F181cXmSKUeRspb%2FsZx6SXuPfmBMsz0OSIxchlXODDerJfQjMDAlYLTUtz6gO32nt57q9y3cFcsD2yz7k8oHryw%2BN7u0VQZnnMTAMdhtEFqnwtD7OPBu15NqYM6FOHw021et76ZF5lO4kIS%2FTzkcEYcgBnLHrRAYpXy3sE4X2HjZ2YfbgPV7pp7%2Bbg%2FG5G%2F1S%2ByRgjzFpXdEag8xOQvbzq1Ee609IKvUsAZ%2BtnBYJtpQDg1%2BY%2BEvHqE7Xse6DibEZlVCwup8WZPUyS8hiDK2Mstk2TjLbeL8WJWrAVddg94YRgX2hoLeAdkRxiXzqhgLNMYRlJyYYNDJhpDACMp616IrRJNDUHFa4xXt8vt5HMotqjgCkvaW0R7Co735NtNof5vfmeUg5F7ks4vJ468ZdnG4i7PnWldpVkAwUqgYZ0ju2LgwRWj2DIEkWEIK%2BeS4%2BoR1hztIXsoo23NqAX6OQMaInxm5gxviFL%2B4kBCfN2X4QxzMZCat9PHrLKC47G8QalpYZuMNmbjtQGOqUBeayPqQR665p0bY4Sy7vAZuf7B%2F%2FQbfbjgL9eUz%2BrQcTlEdt%2BNz8RN0sh823LT6GWhDB5XoKKLz1rkv1LqVwu1uSTo7wJZfoe%2FQT4PGAbBGcH5XyMGBH1IwanjyVa6A3y108stFBpjzDtILNKatRUVk9PxVtze7ufr2ttMhRxiVYOHQm%2FJCIGB9tBpslLJL25Qd7Guyz0DqHo0K18e3N3j0v5%2BJYK&X-Amz-Signature=3a309e9693f99926312c82ce9b83143f020c7e7b823decc8c1ec4850f1440acf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







