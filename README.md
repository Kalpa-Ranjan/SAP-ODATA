



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZB2M74%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T191713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDgyad5l0ImJVPAQbv07RAKIKoeWD4dyH2lTL%2BTYrlSkAiA%2FesOnnSoWDyoQ%2Fm04xFV3OwlhNbUFqmtantaoArNjxSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMYuah0sJUNNHdo0aFKtwDpfPsUC2Ay7ZOK5%2FUkdCNoxWFMsRAnrVjHctJs02VjX6T6dZo0SrADUAuLBHhKgCdwmFItzTBLqMkZDqWl2K%2BC0A5ZA8RoXBwa47kK5JBh9CwbldgcyNgVUPajUH00OmXSiz%2B86%2F7dwOqQBkKNX4FfYlglTw%2FkaC9X7kkxHq5jusbi%2FVAfbmQ%2BA1Ji6CQldCTIiyHz6qMHCE1qhujbjv%2B2NidITLJV4TviKYsFhKIcOJGJT71wgKErQkb8n%2FTIVwo93InfQ91p2eLrDh0H6tXjRJHn5oejy7ri1gVgabPT0RTVZ9t7ZvLpS3nHVD9g2MGZgbVGUT3UBDzKY0x1k39k59Gs%2BJ2vK%2FuvoUnr%2BCRvRqmGotuvW5Zq2UBtARZufK%2Bf%2FEhJdby8mLqaZ2LNKaLlu7NP3V8lBIunRfWLfpTx6fYiRgDq8m7jfvUyElWSDPTiYd0M0CW8rDi4desRfNnNC6T0NllOrgOPEEoUZ%2FEwLWXmteXdONqU%2B6VZpPEoO4chdztzFpuOog49PAbzklVQeNq1rcJcaIs%2BIDRZbYqO8COS1n7LE8Fg5TwmOOasp7ospCGcJNaCeOekTJRHdy%2BczfTzP1nzjJFcSxB8F7KgICIHuuCq%2Bc9n9rzzs8w88q20QY6pgHEM64CsCPc6EW%2BitbWye37T4Pr38g6CTt3PA15XAaodrG5b5zVvu35kaMCPEv6Ypat0Nfbt55YUnYpdBZCktobqgBMZD2WLRSMWUIOXMFG2ygj%2FsGhcdq4F1UH%2B20gjfyZNS%2F4LJ9eWGoqNzbyVj7fgmtCU%2BCh935bxqwUiovLCDOsptPt%2BwWjkbX3pv%2B821reaibCv4yMuZt%2BK9eKgU3z4cjm5xiS&X-Amz-Signature=192b2e96f67a10e761521061996864cfa6b3f73b607a6f773dc40ae54cd98301&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZB2M74%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T191714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDgyad5l0ImJVPAQbv07RAKIKoeWD4dyH2lTL%2BTYrlSkAiA%2FesOnnSoWDyoQ%2Fm04xFV3OwlhNbUFqmtantaoArNjxSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMYuah0sJUNNHdo0aFKtwDpfPsUC2Ay7ZOK5%2FUkdCNoxWFMsRAnrVjHctJs02VjX6T6dZo0SrADUAuLBHhKgCdwmFItzTBLqMkZDqWl2K%2BC0A5ZA8RoXBwa47kK5JBh9CwbldgcyNgVUPajUH00OmXSiz%2B86%2F7dwOqQBkKNX4FfYlglTw%2FkaC9X7kkxHq5jusbi%2FVAfbmQ%2BA1Ji6CQldCTIiyHz6qMHCE1qhujbjv%2B2NidITLJV4TviKYsFhKIcOJGJT71wgKErQkb8n%2FTIVwo93InfQ91p2eLrDh0H6tXjRJHn5oejy7ri1gVgabPT0RTVZ9t7ZvLpS3nHVD9g2MGZgbVGUT3UBDzKY0x1k39k59Gs%2BJ2vK%2FuvoUnr%2BCRvRqmGotuvW5Zq2UBtARZufK%2Bf%2FEhJdby8mLqaZ2LNKaLlu7NP3V8lBIunRfWLfpTx6fYiRgDq8m7jfvUyElWSDPTiYd0M0CW8rDi4desRfNnNC6T0NllOrgOPEEoUZ%2FEwLWXmteXdONqU%2B6VZpPEoO4chdztzFpuOog49PAbzklVQeNq1rcJcaIs%2BIDRZbYqO8COS1n7LE8Fg5TwmOOasp7ospCGcJNaCeOekTJRHdy%2BczfTzP1nzjJFcSxB8F7KgICIHuuCq%2Bc9n9rzzs8w88q20QY6pgHEM64CsCPc6EW%2BitbWye37T4Pr38g6CTt3PA15XAaodrG5b5zVvu35kaMCPEv6Ypat0Nfbt55YUnYpdBZCktobqgBMZD2WLRSMWUIOXMFG2ygj%2FsGhcdq4F1UH%2B20gjfyZNS%2F4LJ9eWGoqNzbyVj7fgmtCU%2BCh935bxqwUiovLCDOsptPt%2BwWjkbX3pv%2B821reaibCv4yMuZt%2BK9eKgU3z4cjm5xiS&X-Amz-Signature=753c26ca617e45b4009fe9ae595c8e6c534fb8e6e8e2efa7c7592207f16636a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







