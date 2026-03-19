



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4WJMAGQ%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T185114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQCt4DUhnorg0X5KrO26169fN7LwjezcpL%2B%2FMryJBa6SsgIhAKYgEL6%2BGWyAQ1C7behUxbkl8ypR5XcaNtogF%2FEGLYxsKv8DCCMQABoMNjM3NDIzMTgzODA1IgzSMspXLw%2BLt8srUa8q3ANzdTfrwQJl81Mh83Zdo4eZ5LlWUjC2yVM5uySgmEDUA29eUag%2Bm86pS8gvp3QUTde9q1cXzUaxaTWatqdBwuoCtBobmkU0fcK4YWsAU2l08KiKL2yPq6dopSZeZ8j0IbuLcDN%2Fj%2FG%2FEoOKhxqPPoLcXlANkgzi%2FxJz7PndnXMDFqXXvKmsNipP%2BnmOofNrCXS8cnR6HPtPL35X%2FWT8gvIjdpQpb3kbMoX3e8zCBLkRY66ZveSUXaBBhmj9Tyh8XQN0XPw1WqlCxLeXAuywPGSvp57dF480viffDipkPpi6zPu51WNzS1mQ6KA%2BSDGeKmGO8lvPIeCjHtjesj%2BRYmeZXokMxZ96lR%2FyOXmhxDuwhhCJNTP2yh%2FdVpwjGIFgz8fepwQi1Z8Ob24AFNPaM2yWkOx4pMFCFWxGC0pRNhKkbCCYmLMtU%2BjH7yUsTfph5L9kTX2YTvLUoD4%2BKa3nIyBGlKTrVuLDe3npdzQaiC90aw%2Fli7OIB68i88MNQ%2Bt3IAXaP0bBprwtDgIfPodFDRPF%2B9HVgrhlNS8EkKJXHrw04tIqpURG5KnQkOIlZZoXWAmsU8uAZOGY3NXk%2BgfS3ce4BOGyRYefBLAnh0tmUAEa1wpggdt3eZVMcWzjjDDD%2BvDNBjqkAckL7VrOVhqrVmbt87o43hapIF4wFYj8wc0T1yE2y6XLVZvftsq0uc6dg0%2FQsRHvkg78lxTCzS%2BsZ8XOSMOvf9FZfmHq%2FX6MMSHlxrthSfWdSlZ0Mkax5HaIuQLrdyK3dUPyikk1S8JomOiN170kGi1%2F0MY9nEpzaG%2BCsQL8JzW6nyHfzpMbdSqHXmxeInDLupj%2FICUvY6PEuAv9aGDPUuSMxjJI&X-Amz-Signature=a43c31d49d1170c68322662c2f660cde893dd2e893f092c11a1b1a9d2f8a63ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4WJMAGQ%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T185114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQCt4DUhnorg0X5KrO26169fN7LwjezcpL%2B%2FMryJBa6SsgIhAKYgEL6%2BGWyAQ1C7behUxbkl8ypR5XcaNtogF%2FEGLYxsKv8DCCMQABoMNjM3NDIzMTgzODA1IgzSMspXLw%2BLt8srUa8q3ANzdTfrwQJl81Mh83Zdo4eZ5LlWUjC2yVM5uySgmEDUA29eUag%2Bm86pS8gvp3QUTde9q1cXzUaxaTWatqdBwuoCtBobmkU0fcK4YWsAU2l08KiKL2yPq6dopSZeZ8j0IbuLcDN%2Fj%2FG%2FEoOKhxqPPoLcXlANkgzi%2FxJz7PndnXMDFqXXvKmsNipP%2BnmOofNrCXS8cnR6HPtPL35X%2FWT8gvIjdpQpb3kbMoX3e8zCBLkRY66ZveSUXaBBhmj9Tyh8XQN0XPw1WqlCxLeXAuywPGSvp57dF480viffDipkPpi6zPu51WNzS1mQ6KA%2BSDGeKmGO8lvPIeCjHtjesj%2BRYmeZXokMxZ96lR%2FyOXmhxDuwhhCJNTP2yh%2FdVpwjGIFgz8fepwQi1Z8Ob24AFNPaM2yWkOx4pMFCFWxGC0pRNhKkbCCYmLMtU%2BjH7yUsTfph5L9kTX2YTvLUoD4%2BKa3nIyBGlKTrVuLDe3npdzQaiC90aw%2Fli7OIB68i88MNQ%2Bt3IAXaP0bBprwtDgIfPodFDRPF%2B9HVgrhlNS8EkKJXHrw04tIqpURG5KnQkOIlZZoXWAmsU8uAZOGY3NXk%2BgfS3ce4BOGyRYefBLAnh0tmUAEa1wpggdt3eZVMcWzjjDDD%2BvDNBjqkAckL7VrOVhqrVmbt87o43hapIF4wFYj8wc0T1yE2y6XLVZvftsq0uc6dg0%2FQsRHvkg78lxTCzS%2BsZ8XOSMOvf9FZfmHq%2FX6MMSHlxrthSfWdSlZ0Mkax5HaIuQLrdyK3dUPyikk1S8JomOiN170kGi1%2F0MY9nEpzaG%2BCsQL8JzW6nyHfzpMbdSqHXmxeInDLupj%2FICUvY6PEuAv9aGDPUuSMxjJI&X-Amz-Signature=23ab05e184c1f5ebe58d432bb09899bd60f7f437a929ed165cbf36f571715f2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







