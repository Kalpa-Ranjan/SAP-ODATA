



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT4V7A5Q%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T015905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIE4sm0xTqnCD%2F5ncEHJs6qPf6C8C%2FU%2Berma4%2BY2EA0nVAiEA5WwNb9LKx0cEgDrXSpF2le3fNaDSOCr23skoMmyVESYq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDD1%2BxPMlpXjek7nBWyrcA2lBlkHqnUOyoUhAVvz4hSaqZ8hXd%2F%2F1j8dPdKLrSONo%2B0l1ThoZER0Fsb7%2BWhLIkr7SNas7FdHJDg9WeKdzCOsRdT6gYqZRVVD3DZezPDilVvc01iBDwrSO4Yv9HHhh3ng3crVRueGbh2rrZ5IhzU8QKSnlK7rhHp%2BHSxdbT6i35WwRqOCJ%2FqXwLP3myTTFUNzd%2BxxLftCmqyjyohmI2CiOUEPXD2vbXq09U6JwdEPjCCscEtyFjVtj2ZFOVIJYZ0bPVVrc6cdutVOjkl5rbj%2BTxHiiddxOykMOwskqUGdRAgMDMDFhLFbMT0lQSIAydAYsqJ1oVO4m4HMA7YtK3%2Bf%2FTiya7Yawfa78O60St%2BfDMv7JU2WEy0NMc40GMWpnDu4%2FAZo0GNdDR6NxyunUA7KUEvJ2VGo7rX8ogDFn4n5fzOfmTIpzhgeCUjLujqBUGSSV1mk5o3jRFJNVZ1mfTP2w9Qmd7iunMyHcVvxhwAF893HVEo8SRSsQP2c0yvG8pH0LiWdEBA8Tqy72eg2Q4vwnlcbP8C5%2FwWhTbBfHIzyxm%2BAapgnLC5yVCkrb4aoerXtlxJyj%2FVMlbXGXd54LYuFusFRqrtz63sq9gsYOB%2FcvzW%2B459lVL4kPKsjcMPTWoc4GOqUBzkYV3MTyrdvt9faMUJzJsPs%2BPvsJT%2BkD5O%2BS9ZCKLh9Xi3z1oeCUsaT2awi3xmSjKZyc0slVzt4SDrzuXtxSW3DX4HXQGCd7oj83avrL2iz7GrXjYdCrPNPRT9P9AkUdv5Byp1INujIdM4sv%2Bhn4TvKdQXKz3ITN7OqxEpz6ot8rjJRXdPcAF810h7U4uugf%2BeXM4bMtbN5TNougC1ifAq6fk%2BLJ&X-Amz-Signature=067ae7c7a529d0d6954777ffe7c7df5816a3673592fff1c06eabe5f7e911f918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT4V7A5Q%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T015906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIE4sm0xTqnCD%2F5ncEHJs6qPf6C8C%2FU%2Berma4%2BY2EA0nVAiEA5WwNb9LKx0cEgDrXSpF2le3fNaDSOCr23skoMmyVESYq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDD1%2BxPMlpXjek7nBWyrcA2lBlkHqnUOyoUhAVvz4hSaqZ8hXd%2F%2F1j8dPdKLrSONo%2B0l1ThoZER0Fsb7%2BWhLIkr7SNas7FdHJDg9WeKdzCOsRdT6gYqZRVVD3DZezPDilVvc01iBDwrSO4Yv9HHhh3ng3crVRueGbh2rrZ5IhzU8QKSnlK7rhHp%2BHSxdbT6i35WwRqOCJ%2FqXwLP3myTTFUNzd%2BxxLftCmqyjyohmI2CiOUEPXD2vbXq09U6JwdEPjCCscEtyFjVtj2ZFOVIJYZ0bPVVrc6cdutVOjkl5rbj%2BTxHiiddxOykMOwskqUGdRAgMDMDFhLFbMT0lQSIAydAYsqJ1oVO4m4HMA7YtK3%2Bf%2FTiya7Yawfa78O60St%2BfDMv7JU2WEy0NMc40GMWpnDu4%2FAZo0GNdDR6NxyunUA7KUEvJ2VGo7rX8ogDFn4n5fzOfmTIpzhgeCUjLujqBUGSSV1mk5o3jRFJNVZ1mfTP2w9Qmd7iunMyHcVvxhwAF893HVEo8SRSsQP2c0yvG8pH0LiWdEBA8Tqy72eg2Q4vwnlcbP8C5%2FwWhTbBfHIzyxm%2BAapgnLC5yVCkrb4aoerXtlxJyj%2FVMlbXGXd54LYuFusFRqrtz63sq9gsYOB%2FcvzW%2B459lVL4kPKsjcMPTWoc4GOqUBzkYV3MTyrdvt9faMUJzJsPs%2BPvsJT%2BkD5O%2BS9ZCKLh9Xi3z1oeCUsaT2awi3xmSjKZyc0slVzt4SDrzuXtxSW3DX4HXQGCd7oj83avrL2iz7GrXjYdCrPNPRT9P9AkUdv5Byp1INujIdM4sv%2Bhn4TvKdQXKz3ITN7OqxEpz6ot8rjJRXdPcAF810h7U4uugf%2BeXM4bMtbN5TNougC1ifAq6fk%2BLJ&X-Amz-Signature=b8f605b20f9a9d9b33bd4944c2016f9e74657eec4e853448c3568670a35402f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







