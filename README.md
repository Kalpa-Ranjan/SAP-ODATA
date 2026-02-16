



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOFULZAJ%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T014740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIEi31BDAVGnkLXLITeS3A6kyX1pWmM1EiGwTX6g8q5UkAiEAnZOPcQ5Xr44syDMYK3fXYdjLOtcpv4HDog4%2F6Gekngsq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDLXTQulOHNvCmYZLyCrcA3l2DpywAJmsB4vsYQ8TwIsi7D2pnwunvqSzgAsG1VY31WHbR3B0Tlufb7Ri2tXb6ZYWj4fFfKKKRdaGhpOwlmic388jfbtUyyN4LoEL9UwHn2NUfHdNi5MYjkuYsCneimY3AcbjutJclJv8PVjl8ukGb4jhNAgsljQu3itoE8s1xWJpXXZ1NoL86%2FWztloG0D33K62teBOyuBl9gzazRZJlFvjP3UmMdjMwUK%2FFggTFEFOX1S97s396ytVtp6ClvM4nF4c1inOjEgGB0XbGUFuNx%2F02sYDAODL59s2N7wo1kZsiN8g%2F8R2PzSOLzW1ZUngHgsqOfofWfJ6uJyzssZVd51QNqA2RL05Qh3qkyq4BYxg2q8I9CWHGaDchg7X7hztmYpL4UBCjqBLkx5QTZyQPlQ76V1wqHmXPHRvOqj5iTFhJ7BlM9enF0pxI7%2FLU1q1biW75L2vvEu50INQw19DIZEbrW%2BiUJ%2FLcAlwvUCPsj8gRqUhjJq%2BeLjJl9VbWdkxM%2BQIOdaVpH0Ojf20DSyeNRhmVQPuShU5Gju4vZYfVMnwAgUZJSlxmOnh8t%2FY7dVUdiF26mPkpUuyc3E54ZZ17TAaMXswaHre%2FIJEWx36nPko%2F2lFEEzj5dETGMMTEycwGOqUBnHZXiF2TK6RSYoTqHRBPV9l%2FwDODEiMtAO6O0ehh%2BbMfZjMyefc5shP%2BoECj0XUSqXcMaJ1tX%2BCsCEe2xzapK8lrFs1sNbzpGN3QSfv%2FHE1dWgitEuOyOKg2ivYX54K0ypS3TWudlmMrzjC3F56FlY53IrbuC4fXZ3vz%2F1X1mahXplJP9F046fg3yAZBzfJ5QHqk0%2BmyvZTUSW7ISQJSSC5JxCDY&X-Amz-Signature=6183909bccfd4aee29fe63109f087abe173c83812c25b4c3e88b9a1320a53560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOFULZAJ%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T014740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIEi31BDAVGnkLXLITeS3A6kyX1pWmM1EiGwTX6g8q5UkAiEAnZOPcQ5Xr44syDMYK3fXYdjLOtcpv4HDog4%2F6Gekngsq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDLXTQulOHNvCmYZLyCrcA3l2DpywAJmsB4vsYQ8TwIsi7D2pnwunvqSzgAsG1VY31WHbR3B0Tlufb7Ri2tXb6ZYWj4fFfKKKRdaGhpOwlmic388jfbtUyyN4LoEL9UwHn2NUfHdNi5MYjkuYsCneimY3AcbjutJclJv8PVjl8ukGb4jhNAgsljQu3itoE8s1xWJpXXZ1NoL86%2FWztloG0D33K62teBOyuBl9gzazRZJlFvjP3UmMdjMwUK%2FFggTFEFOX1S97s396ytVtp6ClvM4nF4c1inOjEgGB0XbGUFuNx%2F02sYDAODL59s2N7wo1kZsiN8g%2F8R2PzSOLzW1ZUngHgsqOfofWfJ6uJyzssZVd51QNqA2RL05Qh3qkyq4BYxg2q8I9CWHGaDchg7X7hztmYpL4UBCjqBLkx5QTZyQPlQ76V1wqHmXPHRvOqj5iTFhJ7BlM9enF0pxI7%2FLU1q1biW75L2vvEu50INQw19DIZEbrW%2BiUJ%2FLcAlwvUCPsj8gRqUhjJq%2BeLjJl9VbWdkxM%2BQIOdaVpH0Ojf20DSyeNRhmVQPuShU5Gju4vZYfVMnwAgUZJSlxmOnh8t%2FY7dVUdiF26mPkpUuyc3E54ZZ17TAaMXswaHre%2FIJEWx36nPko%2F2lFEEzj5dETGMMTEycwGOqUBnHZXiF2TK6RSYoTqHRBPV9l%2FwDODEiMtAO6O0ehh%2BbMfZjMyefc5shP%2BoECj0XUSqXcMaJ1tX%2BCsCEe2xzapK8lrFs1sNbzpGN3QSfv%2FHE1dWgitEuOyOKg2ivYX54K0ypS3TWudlmMrzjC3F56FlY53IrbuC4fXZ3vz%2F1X1mahXplJP9F046fg3yAZBzfJ5QHqk0%2BmyvZTUSW7ISQJSSC5JxCDY&X-Amz-Signature=a0bbc921edc3128ad7b2d4a92a33062fcf2c814531d0e208ae2f813bdfebeade&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







