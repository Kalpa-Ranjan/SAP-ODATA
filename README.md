



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5FHJMS3%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T074951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCNACJbgdOGimeL%2BGfJ%2F4fBaAL6GrS0%2FHEeQupC%2BEctqwIgMMC6hJ15na9aSaW98wHYRVYekokI3nE07At3xNcwFOwqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZkIXjYXV%2FQOZRfeSrcA3VE%2FmZqlBBpkvoMcwZY6poaxXAnaKcp3h79YOsM1SOXV%2B8PR%2FzV4ChGSfo6AcfuJ1MH4tNauNhX3czzdTiI0JY4z4vYK3LlJ4FjCTFON5UVRTcmoo6OCnixXpKkQTv5dJdFPhyeXIIu8SSaxuy7nwCfitBbjvfNCD3dFzkf7KHv%2F7vnhEnQfbXHxj1GHO6NsdlmGD2Hf0Q9fdR7MDBHIFVm006KcYwGyHtnHUB1PtFC%2F3KJFkAYKMfDjr7ysLXVXtoeiwS35ckRPTwfN%2Bsop43lEUaY1NVZhoh2mTFjL4AadDQI89jJA9taBgKxUjWtv%2BIBbX26QENmkSCdYkvk1AuZMEiNI5hmPL%2BJToAjyd0ETEkSyWPxigqaMqbsFl4HSwgPTGFpnO%2FHlAhg3RsKMcq31%2FvWG9SUtmHwXV59zLcdFa8gXpM76l59I1KSe%2BOrWAYISFsyfsGPEfwJXVMQ55SF10Bt4g0H5hXVSdGssTyaOe08iwgNX9lmkxtEzkxJxzTFZxx0O9X833491h9dQJD8qQrrEGRIsobkX0dP3WIVUe1EZDU1ONawIp76dQ%2FhxrBkkh2h84i0xuTG%2FFfEIJfUVpkRglEjcB7Kd80l%2FQUYRzE%2FVsqOYX0BIVupML23%2B88GOqUBjfM03G0f4LxuuVMdKJPYRNY2DPHDNExa%2BSYz%2B4JQPGYdLv3f0RyxqZHVLK0d6ZWxwE5K2eyx0Zz4LU6edjRUS56L%2F2vytQWykf4u1oST6PKeMmT2MbsktZn1XZihcbKhL4FLkR75sr1DyxTFzgbED7aMESTmYhsKYuAOJNBnXurxmbj0Bf%2FC9oDd1sxGvJi30%2F6TAz7Tw%2B1hSCIqch3GZgQICpgS&X-Amz-Signature=2b14269c018871458c53aedf1e39a5019ec94098f5da0d4fcf310c823f3c1eb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5FHJMS3%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T074952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCNACJbgdOGimeL%2BGfJ%2F4fBaAL6GrS0%2FHEeQupC%2BEctqwIgMMC6hJ15na9aSaW98wHYRVYekokI3nE07At3xNcwFOwqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZkIXjYXV%2FQOZRfeSrcA3VE%2FmZqlBBpkvoMcwZY6poaxXAnaKcp3h79YOsM1SOXV%2B8PR%2FzV4ChGSfo6AcfuJ1MH4tNauNhX3czzdTiI0JY4z4vYK3LlJ4FjCTFON5UVRTcmoo6OCnixXpKkQTv5dJdFPhyeXIIu8SSaxuy7nwCfitBbjvfNCD3dFzkf7KHv%2F7vnhEnQfbXHxj1GHO6NsdlmGD2Hf0Q9fdR7MDBHIFVm006KcYwGyHtnHUB1PtFC%2F3KJFkAYKMfDjr7ysLXVXtoeiwS35ckRPTwfN%2Bsop43lEUaY1NVZhoh2mTFjL4AadDQI89jJA9taBgKxUjWtv%2BIBbX26QENmkSCdYkvk1AuZMEiNI5hmPL%2BJToAjyd0ETEkSyWPxigqaMqbsFl4HSwgPTGFpnO%2FHlAhg3RsKMcq31%2FvWG9SUtmHwXV59zLcdFa8gXpM76l59I1KSe%2BOrWAYISFsyfsGPEfwJXVMQ55SF10Bt4g0H5hXVSdGssTyaOe08iwgNX9lmkxtEzkxJxzTFZxx0O9X833491h9dQJD8qQrrEGRIsobkX0dP3WIVUe1EZDU1ONawIp76dQ%2FhxrBkkh2h84i0xuTG%2FFfEIJfUVpkRglEjcB7Kd80l%2FQUYRzE%2FVsqOYX0BIVupML23%2B88GOqUBjfM03G0f4LxuuVMdKJPYRNY2DPHDNExa%2BSYz%2B4JQPGYdLv3f0RyxqZHVLK0d6ZWxwE5K2eyx0Zz4LU6edjRUS56L%2F2vytQWykf4u1oST6PKeMmT2MbsktZn1XZihcbKhL4FLkR75sr1DyxTFzgbED7aMESTmYhsKYuAOJNBnXurxmbj0Bf%2FC9oDd1sxGvJi30%2F6TAz7Tw%2B1hSCIqch3GZgQICpgS&X-Amz-Signature=441654af9b86ff08800e24e80e12a527054933bdb323c505f82f5a72c786422f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







