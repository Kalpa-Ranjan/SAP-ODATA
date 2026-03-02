



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA5JKGWD%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T065119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK5rsXt2OUkZ0HT60ksaA0N5fQG3u7beAjtcEFLKMjrAIgGdCqQyDOl%2FqmR1mLLluJqAOOM5OeXkJB2%2BJZJscm%2BO4qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvyr2r%2F0s9VmD6SpyrcA8GQd3A0zJfJrbVQ%2FsMNcQM3YizKQQm70RRQxFN8ZHyEC4thAicEaRjNmf5Xau8KrFGkaNuSjmHvSHJfX9%2FyCmStG2eA0EB3nW%2BLXUFlOdzv1cl43WYyGtaUOIudGwY1xWlrE4w8K8tkohT19Zm6BP4sTil6oRu5qTr4j%2B%2FoMb7DQpwR9KrCi%2B77wMbn%2FCkRqzrRcOgOui5XY%2F6FNo4FQR0CZufDFyBQjzdGel2a4qgG2kkC7Y7GdHGammhW78PNSsGQpXlnYd0XP3GVEyjKXT4RiRPpnpmpY%2BsFsRCSWa6XawyIWDFphv%2FevExz3lK3ENMPPEmORaPdTv25alVeWDjp96Cg7mcB6XEYwFVy%2BBUrpwh%2FterlN5iGnvOSrG5avXR4Ziw3Ci3OVEokEnuiaekEuFPT%2BqCQOssCUu%2Fjg8IVwnHaWcJnZUu%2BNd8QRQB82BQUp88bvbfJtzmNLhDUiZVMTVlRDY3VXo0cQUxnL32cSz77IGVNFx3sN3SdsFYHzcfRIP2CqqBtsIMHHaaDq2t3lXzfDSniRzl7tywzcxUUd2Q3o7ybIuBOLqEi39LWHxlNWZvR7fsVEFokhPERe9Wz9vZP4Q4PP7kHeD41GDy34NV8EmP09o0BQeeeMN7glM0GOqUBPTCbCnkBbq3n20LdUAjuLpk%2Fze2n%2BtXu5KvjgfnkwfzcBlvJpjdWHGaAu906rD2GxCuDtMaOMkMkiYsTk3jfmWUMroZgY7dFB2Yvc8xgKNw75viCpeMD0TpbSCHTHRavFPybAC%2BrA6yoB1gEhnSO1wG59ZOtppujnasrm9suj2dMMi4wrmTx%2B7j7vKkQstI2m9afsHy4QZ%2BxO9slFLX%2BRkLZxIl9&X-Amz-Signature=4177cfc02a088038c3f8dd6b8779ae5441a66af348eaafce522c51f7e484d1f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA5JKGWD%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T065119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK5rsXt2OUkZ0HT60ksaA0N5fQG3u7beAjtcEFLKMjrAIgGdCqQyDOl%2FqmR1mLLluJqAOOM5OeXkJB2%2BJZJscm%2BO4qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvyr2r%2F0s9VmD6SpyrcA8GQd3A0zJfJrbVQ%2FsMNcQM3YizKQQm70RRQxFN8ZHyEC4thAicEaRjNmf5Xau8KrFGkaNuSjmHvSHJfX9%2FyCmStG2eA0EB3nW%2BLXUFlOdzv1cl43WYyGtaUOIudGwY1xWlrE4w8K8tkohT19Zm6BP4sTil6oRu5qTr4j%2B%2FoMb7DQpwR9KrCi%2B77wMbn%2FCkRqzrRcOgOui5XY%2F6FNo4FQR0CZufDFyBQjzdGel2a4qgG2kkC7Y7GdHGammhW78PNSsGQpXlnYd0XP3GVEyjKXT4RiRPpnpmpY%2BsFsRCSWa6XawyIWDFphv%2FevExz3lK3ENMPPEmORaPdTv25alVeWDjp96Cg7mcB6XEYwFVy%2BBUrpwh%2FterlN5iGnvOSrG5avXR4Ziw3Ci3OVEokEnuiaekEuFPT%2BqCQOssCUu%2Fjg8IVwnHaWcJnZUu%2BNd8QRQB82BQUp88bvbfJtzmNLhDUiZVMTVlRDY3VXo0cQUxnL32cSz77IGVNFx3sN3SdsFYHzcfRIP2CqqBtsIMHHaaDq2t3lXzfDSniRzl7tywzcxUUd2Q3o7ybIuBOLqEi39LWHxlNWZvR7fsVEFokhPERe9Wz9vZP4Q4PP7kHeD41GDy34NV8EmP09o0BQeeeMN7glM0GOqUBPTCbCnkBbq3n20LdUAjuLpk%2Fze2n%2BtXu5KvjgfnkwfzcBlvJpjdWHGaAu906rD2GxCuDtMaOMkMkiYsTk3jfmWUMroZgY7dFB2Yvc8xgKNw75viCpeMD0TpbSCHTHRavFPybAC%2BrA6yoB1gEhnSO1wG59ZOtppujnasrm9suj2dMMi4wrmTx%2B7j7vKkQstI2m9afsHy4QZ%2BxO9slFLX%2BRkLZxIl9&X-Amz-Signature=d0c26ef9fba7cf2a4f896a4d825b1394c35009fd5558cef3c1062e3bee5801ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







