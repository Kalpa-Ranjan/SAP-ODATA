



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WENU34Z7%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T011710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB8n9Z8Jo8%2F0MsiS6%2Bu6anl9drbeFlaaWFDX1bFmR4tdAiBxSGbIEX747iGpjQAApXsYQQ8m5cibd4Ln9fHQBsZe3CqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw213If7a4rRDI%2BZKtwDV76rOgZpeVWcz3QzpRoRVvn4TrVaP%2B6%2FfSWiTT7BC8YSws2Brnbi1Rzmc0%2BBZP94ne0exbAX%2FaHtiIAsT8cyEkaeTUJNHnuC7q5rNTZg0QCrnGaqui3vdnLSgaz594EC6qhHeCgE7%2BOI53VFhVyx2AhZp6mXYEbVr3On2bm%2BJF7F1iZjJpo%2FzxyDWXhpUkbs%2FuTtZzw8YlNzMgYhfjqSYqmhb%2FrW7%2FPTTxAJAJta%2Fhkf0%2BCHJkRPWy7C5pIVDv7XsoKEmF8sXkpxcgV5QjWSWTOf%2FXNz0LIEAROKKSgh2JNIGfmqKF5K%2Bu3Gixl3d%2F%2Bv3ci9Dd5FSBeGOtIs5vooKYhhg79jrAMGqn1%2FmkkX5ess5eDAdli7zX5AvbjukkyWw4IehkbK9cVzlLWrw42N4vI5RX%2FS0o0oeX3ZvyTYhL7CYh9IM%2FQnblmceTVhlQpqRZA0yQdHxFSKF9c6V%2BltjYVc%2FBt4G31%2FfQ6cfL0waktpmFAg42fTCTjVbIFbbS%2FTlqnt%2BwPD6IL2AjyKXFMb0p%2B8A8003uS53koP5Mta8sONiUzGVB9e97kPVOi0oNwvC8zSsCc3wwf3VghBD%2BTE93iqTqReWW%2FYPmgB446KFmiCNfpy5QmP7%2Fxn23Qwj7XLygY6pgG60gk4L1Fd6oX90Wf%2BE9g6QFIzvhx7CVPqwms9cg4LK6LUk9FVNHsBZEcCvOQkOFTueMBLqEQTMY48QfVr78M7cwfM%2BTeG6zAdZugj7XjunAdDv34R7v0Ae6YhXqJ2fb94YK4gaFEFbWozO%2B77jkE7T7bIeC3QZoNpzXgQT%2BGTtsEFwfNksan5p8obmYOTGeTfdnqE7hTt%2Bq3w0NRG3vyj0HBGCFhK&X-Amz-Signature=fa778eaf4a5b50efe407af3e06c379527e7d198bea11913b1e92e0511c836f66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WENU34Z7%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T011710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB8n9Z8Jo8%2F0MsiS6%2Bu6anl9drbeFlaaWFDX1bFmR4tdAiBxSGbIEX747iGpjQAApXsYQQ8m5cibd4Ln9fHQBsZe3CqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLw213If7a4rRDI%2BZKtwDV76rOgZpeVWcz3QzpRoRVvn4TrVaP%2B6%2FfSWiTT7BC8YSws2Brnbi1Rzmc0%2BBZP94ne0exbAX%2FaHtiIAsT8cyEkaeTUJNHnuC7q5rNTZg0QCrnGaqui3vdnLSgaz594EC6qhHeCgE7%2BOI53VFhVyx2AhZp6mXYEbVr3On2bm%2BJF7F1iZjJpo%2FzxyDWXhpUkbs%2FuTtZzw8YlNzMgYhfjqSYqmhb%2FrW7%2FPTTxAJAJta%2Fhkf0%2BCHJkRPWy7C5pIVDv7XsoKEmF8sXkpxcgV5QjWSWTOf%2FXNz0LIEAROKKSgh2JNIGfmqKF5K%2Bu3Gixl3d%2F%2Bv3ci9Dd5FSBeGOtIs5vooKYhhg79jrAMGqn1%2FmkkX5ess5eDAdli7zX5AvbjukkyWw4IehkbK9cVzlLWrw42N4vI5RX%2FS0o0oeX3ZvyTYhL7CYh9IM%2FQnblmceTVhlQpqRZA0yQdHxFSKF9c6V%2BltjYVc%2FBt4G31%2FfQ6cfL0waktpmFAg42fTCTjVbIFbbS%2FTlqnt%2BwPD6IL2AjyKXFMb0p%2B8A8003uS53koP5Mta8sONiUzGVB9e97kPVOi0oNwvC8zSsCc3wwf3VghBD%2BTE93iqTqReWW%2FYPmgB446KFmiCNfpy5QmP7%2Fxn23Qwj7XLygY6pgG60gk4L1Fd6oX90Wf%2BE9g6QFIzvhx7CVPqwms9cg4LK6LUk9FVNHsBZEcCvOQkOFTueMBLqEQTMY48QfVr78M7cwfM%2BTeG6zAdZugj7XjunAdDv34R7v0Ae6YhXqJ2fb94YK4gaFEFbWozO%2B77jkE7T7bIeC3QZoNpzXgQT%2BGTtsEFwfNksan5p8obmYOTGeTfdnqE7hTt%2Bq3w0NRG3vyj0HBGCFhK&X-Amz-Signature=88699c992d2ef5a1f261b1661b4d512a79fdfd8e024e3b99d5f2b68b35810d2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







