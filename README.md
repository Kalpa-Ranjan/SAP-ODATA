



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCH54UOF%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T011220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHGLAyOyMJJ2XxrFCAXC9MTv29nIg5iEB8Mm6BzMHMgAiEAoaYNxv9gz%2Bv0cmu4iTfS%2BjVirRUdKS0FnFeBeyJkTTUq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDETYxUABUaxJWwZ3dSrcA45oh0WokT503GczlgxASTMW62yb3xSm4sOg94%2FGj3yTCO4O1fxbPv3O0coLN0mYUSfpfiX79tjbxrzm6K4oZ4Kn7H%2Fz5z7%2B3dVRM0ZLSWkACNjSXPFNdLzUGLqXHmlswmu8ooZ%2FqyXwsC%2FUNb2LfteKwtNCsFIbztBxyr2WznHq5HcIRbMwL13IGP5CwJW%2F%2FbGaNe79PJm6680hcBaiSxMjnHLNzfIElVLr9a3FqKWFQoAeIrFqJNLWNjHiAZtF%2FGnuFumEDJQJtDCQLZbFwEMK%2Ba6lTPkv5MbKyuxiVNiSnq%2Folnx%2F9RuNDhs8qH4UqVKnIcUY5%2Ba0%2Fo9G8ZbX98AdRvzp7lzIWPcRgOdUEucDtBRmlL9rnVbDYc7nNw0Zow2Yw7l7FxVdp7aObuYZ0Oc96ax8w7pyJmSeRW4Dh483qj80NOt6%2BigT90EXqpDx4ojtE97k8Xq4EgybIG6oEVfNrt9W87ECbjL9zFcSl236wQCL2EEByMaJDQhibNeh36heU6RV2uTBvET3pObnofsn5i26X2i6rnTZ%2F02seX7meXaAwLLrmZBm6l1jOTLzohyQK1O3G4R%2BFH%2Fd6%2BGPqr5%2BRDZYQu3xIuisACzriDxKfpR7lhFg12NkB4rRMObKk8kGOqUB4DRMl45ihm%2Bj%2F70GSq8FJugAbty7bdhPBRnRmFI%2FsrXnUmDFQ5vlLWTepgjA6zOixM%2FKw50nAbsVnjxrDIuaG6AE%2Ftj4YA8%2F6eMXJwaaavT48l7G0zGRQD5EGg6AyXtim9r08jV52TrEkmTe5JWXTfEj%2BS0flAej%2F1MXBVpTKhAqgherhyA%2F%2BxYKduNejampkhZOsj3Bwm7U3aO1bBx%2B85A4GvMS&X-Amz-Signature=bde8e6d6dd17af5550a650d59a1435cdd8e022784e0b90bfa14a53d09e5a0b5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCH54UOF%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T011221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHGLAyOyMJJ2XxrFCAXC9MTv29nIg5iEB8Mm6BzMHMgAiEAoaYNxv9gz%2Bv0cmu4iTfS%2BjVirRUdKS0FnFeBeyJkTTUq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDETYxUABUaxJWwZ3dSrcA45oh0WokT503GczlgxASTMW62yb3xSm4sOg94%2FGj3yTCO4O1fxbPv3O0coLN0mYUSfpfiX79tjbxrzm6K4oZ4Kn7H%2Fz5z7%2B3dVRM0ZLSWkACNjSXPFNdLzUGLqXHmlswmu8ooZ%2FqyXwsC%2FUNb2LfteKwtNCsFIbztBxyr2WznHq5HcIRbMwL13IGP5CwJW%2F%2FbGaNe79PJm6680hcBaiSxMjnHLNzfIElVLr9a3FqKWFQoAeIrFqJNLWNjHiAZtF%2FGnuFumEDJQJtDCQLZbFwEMK%2Ba6lTPkv5MbKyuxiVNiSnq%2Folnx%2F9RuNDhs8qH4UqVKnIcUY5%2Ba0%2Fo9G8ZbX98AdRvzp7lzIWPcRgOdUEucDtBRmlL9rnVbDYc7nNw0Zow2Yw7l7FxVdp7aObuYZ0Oc96ax8w7pyJmSeRW4Dh483qj80NOt6%2BigT90EXqpDx4ojtE97k8Xq4EgybIG6oEVfNrt9W87ECbjL9zFcSl236wQCL2EEByMaJDQhibNeh36heU6RV2uTBvET3pObnofsn5i26X2i6rnTZ%2F02seX7meXaAwLLrmZBm6l1jOTLzohyQK1O3G4R%2BFH%2Fd6%2BGPqr5%2BRDZYQu3xIuisACzriDxKfpR7lhFg12NkB4rRMObKk8kGOqUB4DRMl45ihm%2Bj%2F70GSq8FJugAbty7bdhPBRnRmFI%2FsrXnUmDFQ5vlLWTepgjA6zOixM%2FKw50nAbsVnjxrDIuaG6AE%2Ftj4YA8%2F6eMXJwaaavT48l7G0zGRQD5EGg6AyXtim9r08jV52TrEkmTe5JWXTfEj%2BS0flAej%2F1MXBVpTKhAqgherhyA%2F%2BxYKduNejampkhZOsj3Bwm7U3aO1bBx%2B85A4GvMS&X-Amz-Signature=eb9e52d017560fb070a5d95144f7e23bb4b558ab6384066f7f97cb54d226c436&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







