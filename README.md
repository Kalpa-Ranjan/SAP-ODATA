



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4JFMTIS%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T192200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsboTjZXf%2B05Je0XXBRizkFfVnRbtN2QeZ%2FwSh3IJIBAiEA%2BW9oZu87C6D0vTTc4pfv74tLMUKeVUvctGUr8k5Iz60q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDMLSU2GywhwIvbVs4ircAyUDA2A%2BzgTcU1K9sq3Wx9tA4kcQ%2F2S4nTek8NCMVWDrCQUaz33fLimx3Loh%2BqaejwD63GboLlvs5kwZqPmLGFf%2BnB5vlF0U0tAKZrrd6TM%2Bmqj1bVRMSxKKqK2okXsjeQKFEldnBsP7iYCxb6T7TC%2BpLv8JiZWafE5%2BeRFAtdEsa%2BfOWjH5c%2FLWcC1e0LsKtLXRvOKKs%2BytVBeRxA1zBAJrSY7ZGIRVwstutHLf2VVxFAVqyjDGwNX%2BsN2sg6riB8br8yFOAaX8hnFucizDTcNj3jXzN5FFDBseSEdy05JH%2Bf5j31AnCzcfXTj%2BShXXlHZJizgweYSZ3vW21SHSvCkLYi0Mu6WF6G1REZpGrL3d7usKcMho6gqk9Jh3A8%2BB7pz3FYJA6VhBRT4Sg%2B0x95LwU9uadmUX5zfoxIADXh4Hl%2BLs0e%2BGxklJcx928uOpJPsfldpOfID9TgvSK%2BJ6HTfcVlW1LWFQxTRj6vPnKH2Sqa9w1bGUPLdIbNBPCN5XJmqdCCVBOP0Iuo%2FpKLY8kGW2GIb2zgSQ6R3r1Db81kF1aH2NGQ7CtYZkc%2BdK3uBcCtEee9jtGYEO2O86iiglIcZ6bPDRvihFWbvOM475BJxNTML16yryc88QUvaUML2o0tAGOqUBD3pQ%2FTiYO0XV4%2B5pL5oZw%2FGbp1iTKRXAjCDJbCRE8O2bUNXEHzdoD7%2FTmUbsAwtMZQfL4Wowd%2F72tSunrtjHGn427MvipwlJsKK%2Bs6QQ2s4aCDDdnDjVno%2FEYE5EM43shxz6MFnSazA2Er7JMtK41dD7j8CBMJFLCq0dBb7PxB08XEMUhNpsacm7gu3x0Tf6bjowHq0FzCl6zdg7tAh5cr4OT%2B%2Bf&X-Amz-Signature=adeda1708c184912b410d3a700238de2687e34976dc3a500da9a73d158265dec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4JFMTIS%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T192200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsboTjZXf%2B05Je0XXBRizkFfVnRbtN2QeZ%2FwSh3IJIBAiEA%2BW9oZu87C6D0vTTc4pfv74tLMUKeVUvctGUr8k5Iz60q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDMLSU2GywhwIvbVs4ircAyUDA2A%2BzgTcU1K9sq3Wx9tA4kcQ%2F2S4nTek8NCMVWDrCQUaz33fLimx3Loh%2BqaejwD63GboLlvs5kwZqPmLGFf%2BnB5vlF0U0tAKZrrd6TM%2Bmqj1bVRMSxKKqK2okXsjeQKFEldnBsP7iYCxb6T7TC%2BpLv8JiZWafE5%2BeRFAtdEsa%2BfOWjH5c%2FLWcC1e0LsKtLXRvOKKs%2BytVBeRxA1zBAJrSY7ZGIRVwstutHLf2VVxFAVqyjDGwNX%2BsN2sg6riB8br8yFOAaX8hnFucizDTcNj3jXzN5FFDBseSEdy05JH%2Bf5j31AnCzcfXTj%2BShXXlHZJizgweYSZ3vW21SHSvCkLYi0Mu6WF6G1REZpGrL3d7usKcMho6gqk9Jh3A8%2BB7pz3FYJA6VhBRT4Sg%2B0x95LwU9uadmUX5zfoxIADXh4Hl%2BLs0e%2BGxklJcx928uOpJPsfldpOfID9TgvSK%2BJ6HTfcVlW1LWFQxTRj6vPnKH2Sqa9w1bGUPLdIbNBPCN5XJmqdCCVBOP0Iuo%2FpKLY8kGW2GIb2zgSQ6R3r1Db81kF1aH2NGQ7CtYZkc%2BdK3uBcCtEee9jtGYEO2O86iiglIcZ6bPDRvihFWbvOM475BJxNTML16yryc88QUvaUML2o0tAGOqUBD3pQ%2FTiYO0XV4%2B5pL5oZw%2FGbp1iTKRXAjCDJbCRE8O2bUNXEHzdoD7%2FTmUbsAwtMZQfL4Wowd%2F72tSunrtjHGn427MvipwlJsKK%2Bs6QQ2s4aCDDdnDjVno%2FEYE5EM43shxz6MFnSazA2Er7JMtK41dD7j8CBMJFLCq0dBb7PxB08XEMUhNpsacm7gu3x0Tf6bjowHq0FzCl6zdg7tAh5cr4OT%2B%2Bf&X-Amz-Signature=03d77fc92d7f19d20d4a7841603e2409679df8ed1d33943d2642d06ef9346dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







