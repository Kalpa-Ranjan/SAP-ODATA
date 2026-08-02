



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIV7KOW%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T130831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDWKQn30%2FLTlL37GVOde0MJl8V%2F2zSXqGA3%2FUqHLvaLnQIhAN1BtUmqEdco%2BXOcxT1JCDLAMjxcgORrH1BkU7ZSahPxKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTboajc1pUzSX6O4Uq3ANT7Mnv%2FcEA4Amg4xA7%2BUYpL4dLm%2BwtfQ0ipQBM3uGZOWVD8iHdoj20UygrCEvkpfsOPKjA%2FSrTdSKdVhUJCnf7%2BwH4LMwrnq2%2FsIKWol0%2BLiBvk8IbnHeBOnP5IT6n%2FekX5Gjzssc6Iduz4TfuP%2BNSi0UFcXcqEQhQcHIxgxdE1F8g%2FptcX4diuyzlEQYXiIRguednBHCyFVsJKQFOXUl6I2LpBXmeq0IxsyABMwxuDW0g2KDm36g205n0%2BaPK5IQwG%2F3k8Ez38UafvoR%2FwIRarRuYX7sppkPvP6weULc%2B8cLFdiwTBsBYz4qeOQCaoPCtG8OMUQf0o3ZUHEKINKLzSc7NDYJg0m2yckKqdtaVm83dEhE96xmQzmqdcxZnj15F%2BfbNkOwJ5tkwy9SiJ14wdGjRMeENlpJH5PqUxaoqZ10jLFwURBSiTAi3mYc3InbArmeID%2F5aZ6ygv7rxUZizZodAYMuMV%2Fck%2BnGJmkNojt2o3ov%2FZBzKgiNphipU5SQ2K5hoOkndIwJOl7P1xXr0nMS8tZmP3HLaLVNDBXAPonc1YVYOFKNLMqet5Cf88ay7cIKDXn6EeSGW0R1MS5n511G%2BPY1foehuezRrcJCYQFVi7orLe0a3n1OC3zDr8rvTBjqkARO2mHR%2BkKd3OVz1i%2Fy3mM2Dc5POE4tAikbaU6%2FYq6grAfdtvc25Z59QDX4IlK7tT6jQV5GPvTD%2Fu6JENw0Z2wrQaOScmbiTAYeiv3TQPP1s2F6OLa1fWXUkI9oNALROI7qoSBp7kNlQ3BGWzCjtZg08LPPmiB3B4dDczp87YgzRhf8p2JT77JXCE3dHAIyNNuKswd4U8B%2BTjdIcUdeSna8ON8AN&X-Amz-Signature=9aed28cea9b2fd98691bdae981b131da735d0a1f4e84a77b2bb185575bd4528b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIV7KOW%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T130831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDWKQn30%2FLTlL37GVOde0MJl8V%2F2zSXqGA3%2FUqHLvaLnQIhAN1BtUmqEdco%2BXOcxT1JCDLAMjxcgORrH1BkU7ZSahPxKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTboajc1pUzSX6O4Uq3ANT7Mnv%2FcEA4Amg4xA7%2BUYpL4dLm%2BwtfQ0ipQBM3uGZOWVD8iHdoj20UygrCEvkpfsOPKjA%2FSrTdSKdVhUJCnf7%2BwH4LMwrnq2%2FsIKWol0%2BLiBvk8IbnHeBOnP5IT6n%2FekX5Gjzssc6Iduz4TfuP%2BNSi0UFcXcqEQhQcHIxgxdE1F8g%2FptcX4diuyzlEQYXiIRguednBHCyFVsJKQFOXUl6I2LpBXmeq0IxsyABMwxuDW0g2KDm36g205n0%2BaPK5IQwG%2F3k8Ez38UafvoR%2FwIRarRuYX7sppkPvP6weULc%2B8cLFdiwTBsBYz4qeOQCaoPCtG8OMUQf0o3ZUHEKINKLzSc7NDYJg0m2yckKqdtaVm83dEhE96xmQzmqdcxZnj15F%2BfbNkOwJ5tkwy9SiJ14wdGjRMeENlpJH5PqUxaoqZ10jLFwURBSiTAi3mYc3InbArmeID%2F5aZ6ygv7rxUZizZodAYMuMV%2Fck%2BnGJmkNojt2o3ov%2FZBzKgiNphipU5SQ2K5hoOkndIwJOl7P1xXr0nMS8tZmP3HLaLVNDBXAPonc1YVYOFKNLMqet5Cf88ay7cIKDXn6EeSGW0R1MS5n511G%2BPY1foehuezRrcJCYQFVi7orLe0a3n1OC3zDr8rvTBjqkARO2mHR%2BkKd3OVz1i%2Fy3mM2Dc5POE4tAikbaU6%2FYq6grAfdtvc25Z59QDX4IlK7tT6jQV5GPvTD%2Fu6JENw0Z2wrQaOScmbiTAYeiv3TQPP1s2F6OLa1fWXUkI9oNALROI7qoSBp7kNlQ3BGWzCjtZg08LPPmiB3B4dDczp87YgzRhf8p2JT77JXCE3dHAIyNNuKswd4U8B%2BTjdIcUdeSna8ON8AN&X-Amz-Signature=e11c134d9c8c9ac4d3b49aeb85703fd5b85bd3c7ed3e6b23aa70a39b45fc5555&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







