



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWQOI3N%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T022612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJ5%2FJb6QCepXuuFVGXuWPoB41lNa6Uq0QrSsg8DaaX3AiEA176ZgcQqht9IPxl16POBoIIl5RxcuA1chGs8LFPBE4QqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPxTQ9BS68govJ21HCrcAyJ030ZAn8rjwZdTBoQ4%2B8H%2FBKrtI26ZZzigwd8HEQmUMv2tZ2SM%2FObOBAi%2BPUkw2c3SbCNoYjQJWtiUU9oggHfwmtLJwDx5GRHZ2z2NaUmvet91dODWLFPNeg3IcRZmPAh35O3IaKMrKTIGLQcYsT0XTDfT0Wu3O3AylthyS3rpzxUGlslUox6QZPTPLRD2DYnNRct700qIGaUmhO1NH7rNcD%2F2gOvtDK%2B9Cw1753hZtVWkqSrFh3kuDPyqnTYnU8eYre1l8%2B9PI8NvwOCeVGKoIsLC9oR7RosaLh5K%2BYXT%2FXmL8MEKlFRh5aFx68piKfSKooZsaaYRpU8sc1FwtSpImB%2FPGZV75Aj58ajJnA2vA7npMSMpJ%2FVoqZ4JCRntoHxteG6MERNt6gIzQKNvJArzmYCd5RvhjOvoqqaLoVrXWGs91R0jcnHpQPdCqovLEJPtUNFcK8Lqw3zbe%2Ba9bt9WLTos5IR30LreZRujLGZHvYkeV7GKtdkHTna2O4K58SJQtDdXb%2BSrduvqhR9X3QwnCpaLUkJ%2F%2BqAsoY%2FHyVZmqyF6fw6dmcaugyFIfj%2BVZ%2Bu3tPAwZUjmR5qj%2BgpIkEiICFvdGlP%2BA5usjkGgzJHEyWpOP%2B7wix7SinjTMI%2Bw6s8GOqUBBMSFysTRBnaIRlToD6lnqWkRmS6QMiiyGX85BZ864PU7lHQA8HNtONfpoUlNptc03s7XQWhGwhZUo26kGOrcfA3y9zJhP%2Bsl1x7b3CCAysHDp2wr6SG8ZazGMck3d18Nc2feeXUKUnh2vvuaMbLME6Ef2Z6PWZ9gKQPJpZYMWTrRIvyH2ggW0ik68Lsst%2FNagymSyh2yQMPLf%2FeWAOTNIcQ1jdor&X-Amz-Signature=2661974ae08470add9df94727a362aad0522fb26bf4f174b136867a38e0ddca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWQOI3N%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T022612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJ5%2FJb6QCepXuuFVGXuWPoB41lNa6Uq0QrSsg8DaaX3AiEA176ZgcQqht9IPxl16POBoIIl5RxcuA1chGs8LFPBE4QqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPxTQ9BS68govJ21HCrcAyJ030ZAn8rjwZdTBoQ4%2B8H%2FBKrtI26ZZzigwd8HEQmUMv2tZ2SM%2FObOBAi%2BPUkw2c3SbCNoYjQJWtiUU9oggHfwmtLJwDx5GRHZ2z2NaUmvet91dODWLFPNeg3IcRZmPAh35O3IaKMrKTIGLQcYsT0XTDfT0Wu3O3AylthyS3rpzxUGlslUox6QZPTPLRD2DYnNRct700qIGaUmhO1NH7rNcD%2F2gOvtDK%2B9Cw1753hZtVWkqSrFh3kuDPyqnTYnU8eYre1l8%2B9PI8NvwOCeVGKoIsLC9oR7RosaLh5K%2BYXT%2FXmL8MEKlFRh5aFx68piKfSKooZsaaYRpU8sc1FwtSpImB%2FPGZV75Aj58ajJnA2vA7npMSMpJ%2FVoqZ4JCRntoHxteG6MERNt6gIzQKNvJArzmYCd5RvhjOvoqqaLoVrXWGs91R0jcnHpQPdCqovLEJPtUNFcK8Lqw3zbe%2Ba9bt9WLTos5IR30LreZRujLGZHvYkeV7GKtdkHTna2O4K58SJQtDdXb%2BSrduvqhR9X3QwnCpaLUkJ%2F%2BqAsoY%2FHyVZmqyF6fw6dmcaugyFIfj%2BVZ%2Bu3tPAwZUjmR5qj%2BgpIkEiICFvdGlP%2BA5usjkGgzJHEyWpOP%2B7wix7SinjTMI%2Bw6s8GOqUBBMSFysTRBnaIRlToD6lnqWkRmS6QMiiyGX85BZ864PU7lHQA8HNtONfpoUlNptc03s7XQWhGwhZUo26kGOrcfA3y9zJhP%2Bsl1x7b3CCAysHDp2wr6SG8ZazGMck3d18Nc2feeXUKUnh2vvuaMbLME6Ef2Z6PWZ9gKQPJpZYMWTrRIvyH2ggW0ik68Lsst%2FNagymSyh2yQMPLf%2FeWAOTNIcQ1jdor&X-Amz-Signature=2d937d97471a2e79f30f3cafc4f180657e36edf9d5ba3e6bae426156a4f1d6d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







