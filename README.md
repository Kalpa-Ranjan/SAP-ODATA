



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5YGTBSQ%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T021409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuF0MGy7%2F%2FUbfyHAYztX1IheX%2FiyOSVdnFwZYYmppEsgIgWjvHn8nP14CSP5Cyd7Pdg1VxpUydXiiJVT%2FqlVh%2FkecqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOiElFcJUxtzhN9r4SrcAwurOiHNF8FYtb3RRbCRaIbxA4K6uuUacr%2BSmDtGiibG1hlb2BCu5%2B9BjmD%2Bx%2FoxuK6ubXP1dGLVFEj8F8z2A3uPNBpdpUeT%2F7xajPy5buWHZsKu6lGj58l7A2uIcFBYrhr%2Fy2cli9QiAbpH35t9%2BrINMPjrqpRRjSqNLUYQWBz%2FiuhppzC%2FN2bAxClshYSlIR0MVf9Q4AK4vmi8mO53TrslgN4QRN%2ByOvgEJ3kJvucPQrqE0cgtXJFsGTyUKQHIQfq%2FmTUv6Vk1CZM9ui%2B5uqb1vWsS9XegmJZoq%2B1gTxrryEtESEPhcf2GilyyPAxawZVl9v%2FYpuCaMyq9B8%2F9uk5hoETyXAn2lCbRsG%2F4eX6OoMAP%2F2Cu0%2BBHVBMKOCP4dKaI7l67%2BudMbLLDCEd9V5M7L7vkaxBstEuBmOscc2o7FBkU5p%2B14wwtF57txHbLvJbwWJDvC21OiQ48atZbgZJAgcCKYCtjnXHroXL6Op%2F%2FdthZ%2BzX69%2FKSKkAvKFe9V3JXO5EBPmSSmyGXBWp1ssKslfgLrSo6ozgXM5uF4PzHaCYTqN0F0YCzuMlGBlgAgr9soNSw0gy882Kv4FcfeJnl%2BEipnmIWgKPI3fCTkZrDGe4ZTy4D7%2FWHQOo5MJPyr9MGOqUBcIsZEUfZqK4w5qjQMo9EpC9jGUbfbGYZe60KhfF9KjelQGqW7VkwlTBTQ5PrCDfXGX6x9w7uP37oLNyPUobJWVYI5XPOuPHasjVySSU%2FR4gZclZDwVRxmjOgfeAm%2BoPPT2Ji5d1o6L9Ajs87hWWkC%2BGTisEfZqMzuFA5pZkqP%2B9gpOyVMUhYh2n2oyxs9XWlvhVNTyupVBUJHU%2B2HJpqvHJoMkbR&X-Amz-Signature=2d563770f2114af022ff58616fc3a919be1584e5f671aed53e5846a29fc44948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5YGTBSQ%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T021409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuF0MGy7%2F%2FUbfyHAYztX1IheX%2FiyOSVdnFwZYYmppEsgIgWjvHn8nP14CSP5Cyd7Pdg1VxpUydXiiJVT%2FqlVh%2FkecqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOiElFcJUxtzhN9r4SrcAwurOiHNF8FYtb3RRbCRaIbxA4K6uuUacr%2BSmDtGiibG1hlb2BCu5%2B9BjmD%2Bx%2FoxuK6ubXP1dGLVFEj8F8z2A3uPNBpdpUeT%2F7xajPy5buWHZsKu6lGj58l7A2uIcFBYrhr%2Fy2cli9QiAbpH35t9%2BrINMPjrqpRRjSqNLUYQWBz%2FiuhppzC%2FN2bAxClshYSlIR0MVf9Q4AK4vmi8mO53TrslgN4QRN%2ByOvgEJ3kJvucPQrqE0cgtXJFsGTyUKQHIQfq%2FmTUv6Vk1CZM9ui%2B5uqb1vWsS9XegmJZoq%2B1gTxrryEtESEPhcf2GilyyPAxawZVl9v%2FYpuCaMyq9B8%2F9uk5hoETyXAn2lCbRsG%2F4eX6OoMAP%2F2Cu0%2BBHVBMKOCP4dKaI7l67%2BudMbLLDCEd9V5M7L7vkaxBstEuBmOscc2o7FBkU5p%2B14wwtF57txHbLvJbwWJDvC21OiQ48atZbgZJAgcCKYCtjnXHroXL6Op%2F%2FdthZ%2BzX69%2FKSKkAvKFe9V3JXO5EBPmSSmyGXBWp1ssKslfgLrSo6ozgXM5uF4PzHaCYTqN0F0YCzuMlGBlgAgr9soNSw0gy882Kv4FcfeJnl%2BEipnmIWgKPI3fCTkZrDGe4ZTy4D7%2FWHQOo5MJPyr9MGOqUBcIsZEUfZqK4w5qjQMo9EpC9jGUbfbGYZe60KhfF9KjelQGqW7VkwlTBTQ5PrCDfXGX6x9w7uP37oLNyPUobJWVYI5XPOuPHasjVySSU%2FR4gZclZDwVRxmjOgfeAm%2BoPPT2Ji5d1o6L9Ajs87hWWkC%2BGTisEfZqMzuFA5pZkqP%2B9gpOyVMUhYh2n2oyxs9XWlvhVNTyupVBUJHU%2B2HJpqvHJoMkbR&X-Amz-Signature=48ddf9d84236ca9fc64cc75faec1909bb4c96d3807af592ba84292e28c74b1e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







