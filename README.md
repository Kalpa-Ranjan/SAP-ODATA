



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ6VRJXX%2F20261105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261105T120718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAN2eGyS0SL0wP1FyLGTPW1tULBf%2BzcStzWIH0Edn0t6AiEAsZfnG6dFsqkMtfWv4VH7gP2wQHMisBgTR%2FoDeRy%2Frn0qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDIR4twq86BrHiAzgircA6Gcc4yHWCL1zIIE5tnxCcmBJdE39tSo%2F5v3JbTynUUIaeKOqBC6yUQDUGuNFhnOcjA1QhaecD%2F1KeF4ScG7G9S2AdKQX3BBCjh1o1Fo1eavNVGbwbx72OBT1OEaE1yhMJO4X4lmh1QzsfBJeInfD4uohkUIGhiwviKPj%2BSfFD93ceRxHTE7tk4dKK75%2FrTyncgTjH%2Bn%2BwPNyia69ruV4%2BRAL9lJRI2vEwh6N5c0JGNwdecIIGznMtUXkt1iXSrXcBaltkPaRo9sTqd0HxPJv1WYmJ1bfxtezqb4A3lJvO6ev2tDcHOuzb0jpDX4YjpRn5hvE3nhh9XemYwIpNVYAavF0fNRZ3xnrjb%2Bcpj4GfywU37G5gRYIXXl92LsnbG%2B2mX2loX%2FVpGe%2BbRtfXtqspLLUppHujbyUkitv5H%2BJSXpqsgPEE4m%2FbDbjDnuQeNV1hsukwWJxkNlvQ4lmbQHSEIxxJh2cpns2l3NghrrSUay7p1AWYkt8SZ1FJVoiuk6HRNUJleWBKooKJUsO8BCIvGkozOyfDXa7ZwbgIsmN8Z8VSE7DcmaKLn%2BChs4SwNUQM6%2FnWHB%2BIiw0j3GNg%2Fo95sxb4DHDUTqCzqbDmmTX50boHTR8n1Pvsml24zHMOPBsNcGOqUBIl5sGreneMcvoO7LMmGBtFiAuO0tbFoP6%2FLUoiIpXlPZku28eOFSzdR4oMN1jerOTcnvk3SNkVZlBK4vQk8fJG62d%2B7vMvG%2FtwvYnJCKITQF%2Bcld5aZ8xhwsElqq8z0GMLtAvSToM%2BwVJ8Y3SDSXyZ4gHrd0hF2xi36VrNQlHVFxW3yR4jbgInSyi1irVT548m%2BZmhMx4olOLTkf2B080VKcuH52&X-Amz-Signature=14565e29886f44b1612c423f76a1291bc2ce42e0da271835e1255345ff984094&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ6VRJXX%2F20261105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261105T120718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAN2eGyS0SL0wP1FyLGTPW1tULBf%2BzcStzWIH0Edn0t6AiEAsZfnG6dFsqkMtfWv4VH7gP2wQHMisBgTR%2FoDeRy%2Frn0qiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDIR4twq86BrHiAzgircA6Gcc4yHWCL1zIIE5tnxCcmBJdE39tSo%2F5v3JbTynUUIaeKOqBC6yUQDUGuNFhnOcjA1QhaecD%2F1KeF4ScG7G9S2AdKQX3BBCjh1o1Fo1eavNVGbwbx72OBT1OEaE1yhMJO4X4lmh1QzsfBJeInfD4uohkUIGhiwviKPj%2BSfFD93ceRxHTE7tk4dKK75%2FrTyncgTjH%2Bn%2BwPNyia69ruV4%2BRAL9lJRI2vEwh6N5c0JGNwdecIIGznMtUXkt1iXSrXcBaltkPaRo9sTqd0HxPJv1WYmJ1bfxtezqb4A3lJvO6ev2tDcHOuzb0jpDX4YjpRn5hvE3nhh9XemYwIpNVYAavF0fNRZ3xnrjb%2Bcpj4GfywU37G5gRYIXXl92LsnbG%2B2mX2loX%2FVpGe%2BbRtfXtqspLLUppHujbyUkitv5H%2BJSXpqsgPEE4m%2FbDbjDnuQeNV1hsukwWJxkNlvQ4lmbQHSEIxxJh2cpns2l3NghrrSUay7p1AWYkt8SZ1FJVoiuk6HRNUJleWBKooKJUsO8BCIvGkozOyfDXa7ZwbgIsmN8Z8VSE7DcmaKLn%2BChs4SwNUQM6%2FnWHB%2BIiw0j3GNg%2Fo95sxb4DHDUTqCzqbDmmTX50boHTR8n1Pvsml24zHMOPBsNcGOqUBIl5sGreneMcvoO7LMmGBtFiAuO0tbFoP6%2FLUoiIpXlPZku28eOFSzdR4oMN1jerOTcnvk3SNkVZlBK4vQk8fJG62d%2B7vMvG%2FtwvYnJCKITQF%2Bcld5aZ8xhwsElqq8z0GMLtAvSToM%2BwVJ8Y3SDSXyZ4gHrd0hF2xi36VrNQlHVFxW3yR4jbgInSyi1irVT548m%2BZmhMx4olOLTkf2B080VKcuH52&X-Amz-Signature=dd5e0c8918a13ddfa928458c8a7d1c94fa4189888116e3e60fee82ed0dae56d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







