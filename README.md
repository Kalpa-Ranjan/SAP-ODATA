



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT5B4MYW%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T025651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChQcntXmP7CCJUMkNJSS5wG73NjuzSWZbeYbRJlMo7TgIgQMMxQMzDjCJk2PXAnBhO45NpTl73SrIgHtiXN%2FiYd28qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGp3loICYfZueiUoByrcA2V1FIo%2BrgdcbaObIDsJKZ3WfkM2EUAm1A%2FiMMSdpg5qIFSgbBYyknFk2tGPDO30zXyEGWG8Yj4pSf%2FbN29nv%2B%2BoFXEeJmVniWqSTHR0fX%2FDJAXrtxSEDwLPnkV%2FBlVNyIPeRSQ830lWJSGqEcgMA4BvD%2BBfeHQcv9mchJSBPdGYshTZa8PCZkFHy0w30Wsnuio6YtVRbUb75zdm7P6wILk4oUiLWUdqSXgl3xeEeDaMiJvWx90Mxwh12pCkBasjkAeeZQCnXiysfNGl6WCFDQXKsIOVjNzbLzI92DZ9mM6qPkGrK9%2Ffz8i7Wc%2F65OFj%2FRk%2BSUYlP1DuXJUCwII4bOljnTDOzmaSOdL2FcmmuJHhEx2uYg7scXgHls7jSCyuzRWOcPoDyCLAmAfUoL4cm%2Fn2cZ%2BVYj7vP0%2Bhc9HzwLq7EvwljRqsDvYJjThuJ3vJ%2BNDh9U7scEyU9byRDgd0QxxTgTC6NXoYVDI0h5Yt0PqBIAkZylVntq8rIB64QVdY6I4YD9aEJCuLLmiUYFzx07ARwYfxfzH3Kcrbp0Um9Wfli3KxI6SH%2BfbbZg6YyCAws1XfWYeNRHxEgG4u7PFTuxroWVSKKSr2TArvbi2ZhGjEwQ9Nezacbd3G8IIEMIy1h9IGOqUBxDzi%2BAZwI6f6utrhGXADOdgCJ137SCJbvaL6se6b0WbRylZZhWozXpYz4RpCPt4UbMq6oVDpieY2xQvTkzqMh5%2B4YQembd24TV2u7Ekd6GuG1T9FjORqquitFtFcT6%2B5PMA0qUFIHc1w0HJhwjDaew2neAQHqLU8QcC6zWpf56OVnsmDT5HZq8mLupmBF8oTAb1%2FBEUrxQZ%2BKMf4dfnQI3OdyP0y&X-Amz-Signature=c74ac88a695d1ef15246715d8ff12878346a75c3d7df23ac6011c2d679fbd531&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT5B4MYW%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T025651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChQcntXmP7CCJUMkNJSS5wG73NjuzSWZbeYbRJlMo7TgIgQMMxQMzDjCJk2PXAnBhO45NpTl73SrIgHtiXN%2FiYd28qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGp3loICYfZueiUoByrcA2V1FIo%2BrgdcbaObIDsJKZ3WfkM2EUAm1A%2FiMMSdpg5qIFSgbBYyknFk2tGPDO30zXyEGWG8Yj4pSf%2FbN29nv%2B%2BoFXEeJmVniWqSTHR0fX%2FDJAXrtxSEDwLPnkV%2FBlVNyIPeRSQ830lWJSGqEcgMA4BvD%2BBfeHQcv9mchJSBPdGYshTZa8PCZkFHy0w30Wsnuio6YtVRbUb75zdm7P6wILk4oUiLWUdqSXgl3xeEeDaMiJvWx90Mxwh12pCkBasjkAeeZQCnXiysfNGl6WCFDQXKsIOVjNzbLzI92DZ9mM6qPkGrK9%2Ffz8i7Wc%2F65OFj%2FRk%2BSUYlP1DuXJUCwII4bOljnTDOzmaSOdL2FcmmuJHhEx2uYg7scXgHls7jSCyuzRWOcPoDyCLAmAfUoL4cm%2Fn2cZ%2BVYj7vP0%2Bhc9HzwLq7EvwljRqsDvYJjThuJ3vJ%2BNDh9U7scEyU9byRDgd0QxxTgTC6NXoYVDI0h5Yt0PqBIAkZylVntq8rIB64QVdY6I4YD9aEJCuLLmiUYFzx07ARwYfxfzH3Kcrbp0Um9Wfli3KxI6SH%2BfbbZg6YyCAws1XfWYeNRHxEgG4u7PFTuxroWVSKKSr2TArvbi2ZhGjEwQ9Nezacbd3G8IIEMIy1h9IGOqUBxDzi%2BAZwI6f6utrhGXADOdgCJ137SCJbvaL6se6b0WbRylZZhWozXpYz4RpCPt4UbMq6oVDpieY2xQvTkzqMh5%2B4YQembd24TV2u7Ekd6GuG1T9FjORqquitFtFcT6%2B5PMA0qUFIHc1w0HJhwjDaew2neAQHqLU8QcC6zWpf56OVnsmDT5HZq8mLupmBF8oTAb1%2FBEUrxQZ%2BKMf4dfnQI3OdyP0y&X-Amz-Signature=5cef0e7bb1d747442325604e531806e3e7d8cf61b2fdb7cec23eb66d6477c7c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







