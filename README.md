



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA2XD6OV%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T151824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGkrg0X9De4MMou7kVfmo8sflRHgqg0vtrMKVzYtON4gIgVCi5BBqWbBKQ9KvIVqVRP4ekLIBn0qyGVjvWrkgBFzcqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7wjdntskKiSEVGQyrcA7dPV5BtYNy%2FqvB07TWE5xalIlrbHTgVNrXJ79dMtmYXNn13i9Ou5jtTlF%2FO9YI59ydank9Dk0JeE1JfOOU6teUjeAK5neRCqOY19nL%2Frt5WjiIu%2FveNfOz7CJla9xJOY6FyZdQkQcfK1GRwP6VGuvfB550KZffLwoBx0vk70HyuVNJGUi7fac043HTj%2F4N3sTDT%2F089bh2%2F1%2FQQtSAVINAL1FkTx4An72HNAyY6wRKJcmBGixDWLlFk7HhIMZh5w%2F4Mn4farBasbPCXmlGSxdCuLEfbtL6YepzhJCAA4H0VUpWXPHntITk6hps%2B%2BHnzvFv9Ovhork55%2BLB7j%2FVZIcBdMQtpGxJI4E5x1UaEJSQPAT6JPF9B5sszWw1FEUY7lxWVNRc39lFea%2FGuJwZKo%2BWxyA6filQYCIBVZlID%2BfB%2BIiXFJrkrlvNCBtRhkzJ26JYHbRuANcrZR56IfLQneWpnKOO9LBDyIyfGMfg3Old2M5soClc40CrVn13aZTuLMfBh8fPKrTxAYrM34yvmMCaC%2FMmFzQwyOIQRhGc977fGEYMk%2BwGuDONprcqsRYR%2BbA8L1%2FqluqcB4Qgw3dVCYm4vjhWXRTW2srEBorlITUe08fWS%2BR%2FFxoddaM%2FlMNPNrNAGOqUB%2BdMOUjkd1dM9Y5BFBTTndtIt4OM9l9JrHkORThfAtJ%2BnT%2Ffkg3C5sPQbg4rZ9UmSGBXfEvv%2Bge3U3xtY7ZBXFcIwH49%2FN6TL9KNmzjGlychxWDgfaZF4iyV9YmEbP%2FQU3UpV5xf8o7M4zcdc1GdLusgk%2F%2Bc311lV0H7SvmMC8QAZSi96VDnmlljnmkgFBw%2FWKdD7rqKdzTs5T99NdggmqKw1oE6s&X-Amz-Signature=890d0992620bbbafca3a9d8680a9799a29b22b0751f1095142605b8c6516f036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA2XD6OV%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T151824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGkrg0X9De4MMou7kVfmo8sflRHgqg0vtrMKVzYtON4gIgVCi5BBqWbBKQ9KvIVqVRP4ekLIBn0qyGVjvWrkgBFzcqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7wjdntskKiSEVGQyrcA7dPV5BtYNy%2FqvB07TWE5xalIlrbHTgVNrXJ79dMtmYXNn13i9Ou5jtTlF%2FO9YI59ydank9Dk0JeE1JfOOU6teUjeAK5neRCqOY19nL%2Frt5WjiIu%2FveNfOz7CJla9xJOY6FyZdQkQcfK1GRwP6VGuvfB550KZffLwoBx0vk70HyuVNJGUi7fac043HTj%2F4N3sTDT%2F089bh2%2F1%2FQQtSAVINAL1FkTx4An72HNAyY6wRKJcmBGixDWLlFk7HhIMZh5w%2F4Mn4farBasbPCXmlGSxdCuLEfbtL6YepzhJCAA4H0VUpWXPHntITk6hps%2B%2BHnzvFv9Ovhork55%2BLB7j%2FVZIcBdMQtpGxJI4E5x1UaEJSQPAT6JPF9B5sszWw1FEUY7lxWVNRc39lFea%2FGuJwZKo%2BWxyA6filQYCIBVZlID%2BfB%2BIiXFJrkrlvNCBtRhkzJ26JYHbRuANcrZR56IfLQneWpnKOO9LBDyIyfGMfg3Old2M5soClc40CrVn13aZTuLMfBh8fPKrTxAYrM34yvmMCaC%2FMmFzQwyOIQRhGc977fGEYMk%2BwGuDONprcqsRYR%2BbA8L1%2FqluqcB4Qgw3dVCYm4vjhWXRTW2srEBorlITUe08fWS%2BR%2FFxoddaM%2FlMNPNrNAGOqUB%2BdMOUjkd1dM9Y5BFBTTndtIt4OM9l9JrHkORThfAtJ%2BnT%2Ffkg3C5sPQbg4rZ9UmSGBXfEvv%2Bge3U3xtY7ZBXFcIwH49%2FN6TL9KNmzjGlychxWDgfaZF4iyV9YmEbP%2FQU3UpV5xf8o7M4zcdc1GdLusgk%2F%2Bc311lV0H7SvmMC8QAZSi96VDnmlljnmkgFBw%2FWKdD7rqKdzTs5T99NdggmqKw1oE6s&X-Amz-Signature=9dd8be3b69b89fc3d17b6da0a1529fe7393186ac8ba18ac502781584f84b46c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







