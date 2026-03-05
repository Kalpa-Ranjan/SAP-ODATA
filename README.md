



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SINNXUOE%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T014449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEJ2bMc2vYBXWKt7FP%2FCgC73x4g52JHPGIEWda2UygeCAiEA7gz4CmVN7wohoMF7%2BsV3MBCwyrmEl%2FtEjts29VCpFawqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwqmXgHCUN9ZLO6AyrcA8mJ3%2BhQnMqe5bAHzmxMFmuFKbWu2Kwm5eSLeaqv4kYnIwd7nWwpbFpT6pha4E8y6UwsAYllwLuMZ0z4E3PasSryryxU6MYcuwHVcm26VmLSZRLJ5rcMNq5Zt8Jz%2BpmS93UGcBJXF4rYabqeH3ULRrWqO5OiuMUsZs7bMBJs%2Fj2e9zHwZU1o05XO53hge7P%2B4xqtZOU2pyZ%2FTowDp559FcWaqOGH1ABnMJ9Pnn4THVin%2FAnGVRZWuXyE7hzcvEhcJeTGIms1eXTL3a1MIOeEjPQXM1IctJMDhuBlYqWgcT2hRsC%2FkMyhzjBX5LZnMrku6WpzImNrGW%2F5SwvaPv9dbN9YOT4q7QhFvkU0f9WJYKSgkNADdpFT5%2Fi2Xw36COw6zeIzKZmoRJNeysLsKjSw1P%2BrZ3fC4Fd%2F6ENgbqpiGGNxT29yRNEro0mSFS4B2MQD3jsGfZT0zk6fycve10q6Lf9ystsRPxJct%2FBIuiMOFvd943JKHh4jHe9OeHB3IFmk3yW05cSreE0j3CQmkyES4d74BtdAxc6ktrHPiI3X1LnQjv8RZ5pVW%2Bn29lChPkh6A2zPzBaxoytaHq2JeNl9j7EcESwSM3a10eZ1gjIXtH3P3cT2iVZvwq27ngmqMNKxo80GOqUBmDuuMDTCPlTfzhFDgOtT7Rp2hzZLDp1LHkL767256cANq1cip%2BxD4VA054XDG7v5sGyDQGOViS4uACJuZZS4YTA5QzQf1A4WEYBfV%2FGXvkPrdLE%2Fy78acYcDUf3YFy5egAkduCrom7SfwGNlhpI0yrR8afz8WNiWjyyQfAzM2%2BY3P9IXasj3secFDBG8VI7ED2QVXYAFPtR2HYhCAIbDaer3EiYW&X-Amz-Signature=061f5f037e0d44ac30fb355796dddc6f2ccea31c0daf8e3135898782b22b34fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SINNXUOE%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T014449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEJ2bMc2vYBXWKt7FP%2FCgC73x4g52JHPGIEWda2UygeCAiEA7gz4CmVN7wohoMF7%2BsV3MBCwyrmEl%2FtEjts29VCpFawqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwqmXgHCUN9ZLO6AyrcA8mJ3%2BhQnMqe5bAHzmxMFmuFKbWu2Kwm5eSLeaqv4kYnIwd7nWwpbFpT6pha4E8y6UwsAYllwLuMZ0z4E3PasSryryxU6MYcuwHVcm26VmLSZRLJ5rcMNq5Zt8Jz%2BpmS93UGcBJXF4rYabqeH3ULRrWqO5OiuMUsZs7bMBJs%2Fj2e9zHwZU1o05XO53hge7P%2B4xqtZOU2pyZ%2FTowDp559FcWaqOGH1ABnMJ9Pnn4THVin%2FAnGVRZWuXyE7hzcvEhcJeTGIms1eXTL3a1MIOeEjPQXM1IctJMDhuBlYqWgcT2hRsC%2FkMyhzjBX5LZnMrku6WpzImNrGW%2F5SwvaPv9dbN9YOT4q7QhFvkU0f9WJYKSgkNADdpFT5%2Fi2Xw36COw6zeIzKZmoRJNeysLsKjSw1P%2BrZ3fC4Fd%2F6ENgbqpiGGNxT29yRNEro0mSFS4B2MQD3jsGfZT0zk6fycve10q6Lf9ystsRPxJct%2FBIuiMOFvd943JKHh4jHe9OeHB3IFmk3yW05cSreE0j3CQmkyES4d74BtdAxc6ktrHPiI3X1LnQjv8RZ5pVW%2Bn29lChPkh6A2zPzBaxoytaHq2JeNl9j7EcESwSM3a10eZ1gjIXtH3P3cT2iVZvwq27ngmqMNKxo80GOqUBmDuuMDTCPlTfzhFDgOtT7Rp2hzZLDp1LHkL767256cANq1cip%2BxD4VA054XDG7v5sGyDQGOViS4uACJuZZS4YTA5QzQf1A4WEYBfV%2FGXvkPrdLE%2Fy78acYcDUf3YFy5egAkduCrom7SfwGNlhpI0yrR8afz8WNiWjyyQfAzM2%2BY3P9IXasj3secFDBG8VI7ED2QVXYAFPtR2HYhCAIbDaer3EiYW&X-Amz-Signature=6ddb842d30eda307ec1d3c56ba2ae5e593d727429bf765b76dd983181ae21c75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







