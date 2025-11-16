



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS746SBN%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T011717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7DmrO5hjx%2B2pf7XHbedMu10KdUeoMgOmHspfFkvPbAgIgHojlK3FuCqEY3nbSfrIppq2Z3XsF8To0S%2Fov4%2BfQA78qiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG357WlIYhFaaNibdSrcA0gjK5lHWW8yPdPCZuB2txEOK%2F7%2Bv7v6lgYv1F%2Ffvt15RcY6svsJdE2WEAN03chh5E3NGOWL92igMT66m%2BcsK%2BHe9oJ3P4tQ0wPpaHfzwMihk%2B%2FCQQxMpMiv%2BiFqvs0JsO672xhAWoHRzpdaJjgrXOvGMTIoOqIwmcLylQQycq%2F8YnnLeguCOgVFjc1TczG2I0b7CnW8uITufn5Q%2BA3yAO4x6MieYRFlYxURFKiXfXyLWvB6It%2Fs6fB0ilUx2WoaxFcoxeAQxNrsllgizUFnRa%2BXabSx5ijom5pJT8yvgHsdA0JQbSvm1IpH%2BB%2BxqFDXQ7mTVtZ6TRftr%2BoUN4XdOqWjR6YSdeBq0%2BHyec6bznKoCNHMz5BZdCHZHZn8frNeL2syPk0kGL%2BYYamJ%2BfQGGYOb8hsgvXdOQWGX8TX3EI6QeWrp3mxLjoZEzdimGk8rTtqUH4kF70X6xvbF2izu5nHGcUdkXLK0brRCUM2mArH%2F8c1%2FIobaI2%2FkrFBi6fFLMC56WrdTv7ZhO0W6E%2F2m06Otmja3Tb4ULb1fCESTenJN%2FKb1QsC%2BBGaN%2BPZjVfhBDXbZne1cJUHTJzmcXaSWjj7Hlp9m8RrtLwckFp6LIdp339KJ6Y7DAWRvpC%2B%2FMLzS48gGOqUBKWqRxYnPCRZtm2xQp3ANukSABPuod5y%2Bv19Xk1fmVDapUvWYP2yDONMYLJBWILp%2FgJaD7jdCIP284ceqVxDs%2B7%2BcHQkHPul2jxzviqiZIyeTXrivlZu1hCIg6ImQlR5REowRANMrV2E%2Bra5BSOw713gw%2FV3HIwMfNIJeeNqTXwy9aZUG1xEa%2F9DfL4IVBIIvJax4U2KsgsLThAyoFu2PheRMEio0&X-Amz-Signature=7d2de897c1f012f68c35f73616c92b1a09aad446aa7172c7935a3d4e0af6819b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS746SBN%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T011717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7DmrO5hjx%2B2pf7XHbedMu10KdUeoMgOmHspfFkvPbAgIgHojlK3FuCqEY3nbSfrIppq2Z3XsF8To0S%2Fov4%2BfQA78qiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG357WlIYhFaaNibdSrcA0gjK5lHWW8yPdPCZuB2txEOK%2F7%2Bv7v6lgYv1F%2Ffvt15RcY6svsJdE2WEAN03chh5E3NGOWL92igMT66m%2BcsK%2BHe9oJ3P4tQ0wPpaHfzwMihk%2B%2FCQQxMpMiv%2BiFqvs0JsO672xhAWoHRzpdaJjgrXOvGMTIoOqIwmcLylQQycq%2F8YnnLeguCOgVFjc1TczG2I0b7CnW8uITufn5Q%2BA3yAO4x6MieYRFlYxURFKiXfXyLWvB6It%2Fs6fB0ilUx2WoaxFcoxeAQxNrsllgizUFnRa%2BXabSx5ijom5pJT8yvgHsdA0JQbSvm1IpH%2BB%2BxqFDXQ7mTVtZ6TRftr%2BoUN4XdOqWjR6YSdeBq0%2BHyec6bznKoCNHMz5BZdCHZHZn8frNeL2syPk0kGL%2BYYamJ%2BfQGGYOb8hsgvXdOQWGX8TX3EI6QeWrp3mxLjoZEzdimGk8rTtqUH4kF70X6xvbF2izu5nHGcUdkXLK0brRCUM2mArH%2F8c1%2FIobaI2%2FkrFBi6fFLMC56WrdTv7ZhO0W6E%2F2m06Otmja3Tb4ULb1fCESTenJN%2FKb1QsC%2BBGaN%2BPZjVfhBDXbZne1cJUHTJzmcXaSWjj7Hlp9m8RrtLwckFp6LIdp339KJ6Y7DAWRvpC%2B%2FMLzS48gGOqUBKWqRxYnPCRZtm2xQp3ANukSABPuod5y%2Bv19Xk1fmVDapUvWYP2yDONMYLJBWILp%2FgJaD7jdCIP284ceqVxDs%2B7%2BcHQkHPul2jxzviqiZIyeTXrivlZu1hCIg6ImQlR5REowRANMrV2E%2Bra5BSOw713gw%2FV3HIwMfNIJeeNqTXwy9aZUG1xEa%2F9DfL4IVBIIvJax4U2KsgsLThAyoFu2PheRMEio0&X-Amz-Signature=ab6020b418cbb6a8064473e8ca38b72f15c3e6db163d80c060ab30d239f54070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







