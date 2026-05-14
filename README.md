



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QACOCET5%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T193950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuPK5ELzv2lzx0Ckaf8QZ8PO2huBrS%2BtwSavofFAyYHAiEAu9v5wawRK7u5Bw07qR9kZt3xgNFE%2BeC1tAvG41xcz38q%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDF%2FI0cf3e4DZezvu4yrcA3xnwj2FL5KBniUDPJjH2fFgToVmcNKHO0kUzuwnrHakqet%2BsqT6KrvCoKkFThjXGF1SlJ30cTpKBWrHAQ%2FRqcm8zDPXAjH4fL7B7SRWOxri%2FaPAZI%2BTGWPUEG68%2B2QGw97gNsN0CYiIPNK5zx%2F%2FmdI2LHa2cEWPZlEHlWILLR2y66Fi3uYLY3C6f5lLS%2FCGCLIM0wqNhCsVlmZ%2BipKz5Zr%2BJNRY%2Fi5%2BVOH9Csbf9j6pHnTbEQsbGRR1iCCz9IifEKtc7xRi37n6%2BxbKVnQbqg9bnX3BptuUFrXmaFQUTvZ9l88wCHKDzZNI0MpD5lokCeIDWBGaNOkGKt%2BCId0PVUsb3ekSXiCtcsGM%2F7%2FFfy0nsMf0BLyUTgWQP03STIJ1YdBIYvIp60PcASV7E4hraitq5YlVDdNi%2Bs4vAWl0qrG1hGYMeeGRQP1Oa0pk97ebOm8U74jcnh5Fxn34ZTfvba3FFojoxlfXTQ549bspnLwe5qq61tV1UqAxotS4E1HU5fyZw6FJkkmKiTN5VNoReNvIyKZPJWeOxVym%2BqBpstY4aWJtxxuwC%2BG6avw1o0rIf1KD%2BFOJv191d5EwcqCVufni7vHp%2FCg1vmt7uzPs6e7b71MesgfYMLsSZrmdMMvFmNAGOqUBl0mncUyhlAkrEsz5IohqernRPaQKKC8uIGM%2BWB9SiJvCZ3ZY7g0xMlg7EcGWzGHGpO8a2F6Dz%2BtorBCDizZiksuXurNshKRkOCbnRwYcBbxr5MmvmQ0UXp5JO5urNH2TsrL2jO%2Fb9TC%2FNsrr7dWGot2jereMtWM9zm2Hx8uAbc7I%2B6x1ATrcwUyCyGvQnVE2WpwCJtwLpeFdnS92mzMp3Fp%2BqwC6&X-Amz-Signature=c5b4eb4e620ec65d70d70a31685b7666c77619308e09464f1527dca836c7a9ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QACOCET5%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T193950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuPK5ELzv2lzx0Ckaf8QZ8PO2huBrS%2BtwSavofFAyYHAiEAu9v5wawRK7u5Bw07qR9kZt3xgNFE%2BeC1tAvG41xcz38q%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDF%2FI0cf3e4DZezvu4yrcA3xnwj2FL5KBniUDPJjH2fFgToVmcNKHO0kUzuwnrHakqet%2BsqT6KrvCoKkFThjXGF1SlJ30cTpKBWrHAQ%2FRqcm8zDPXAjH4fL7B7SRWOxri%2FaPAZI%2BTGWPUEG68%2B2QGw97gNsN0CYiIPNK5zx%2F%2FmdI2LHa2cEWPZlEHlWILLR2y66Fi3uYLY3C6f5lLS%2FCGCLIM0wqNhCsVlmZ%2BipKz5Zr%2BJNRY%2Fi5%2BVOH9Csbf9j6pHnTbEQsbGRR1iCCz9IifEKtc7xRi37n6%2BxbKVnQbqg9bnX3BptuUFrXmaFQUTvZ9l88wCHKDzZNI0MpD5lokCeIDWBGaNOkGKt%2BCId0PVUsb3ekSXiCtcsGM%2F7%2FFfy0nsMf0BLyUTgWQP03STIJ1YdBIYvIp60PcASV7E4hraitq5YlVDdNi%2Bs4vAWl0qrG1hGYMeeGRQP1Oa0pk97ebOm8U74jcnh5Fxn34ZTfvba3FFojoxlfXTQ549bspnLwe5qq61tV1UqAxotS4E1HU5fyZw6FJkkmKiTN5VNoReNvIyKZPJWeOxVym%2BqBpstY4aWJtxxuwC%2BG6avw1o0rIf1KD%2BFOJv191d5EwcqCVufni7vHp%2FCg1vmt7uzPs6e7b71MesgfYMLsSZrmdMMvFmNAGOqUBl0mncUyhlAkrEsz5IohqernRPaQKKC8uIGM%2BWB9SiJvCZ3ZY7g0xMlg7EcGWzGHGpO8a2F6Dz%2BtorBCDizZiksuXurNshKRkOCbnRwYcBbxr5MmvmQ0UXp5JO5urNH2TsrL2jO%2Fb9TC%2FNsrr7dWGot2jereMtWM9zm2Hx8uAbc7I%2B6x1ATrcwUyCyGvQnVE2WpwCJtwLpeFdnS92mzMp3Fp%2BqwC6&X-Amz-Signature=18083310e21bac9419609b11aa1750fb3e44122f79ed566228f5ea388eb323d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







