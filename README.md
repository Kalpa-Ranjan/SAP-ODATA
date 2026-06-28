



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632LWE7GN%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T084456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLdHmq1RxgGviU5ybmH6sRceippmVE1imiwqU9DxytzwIhAM3KvT6yaEu880YgljaKek7fe4pOsmKn3B%2BaKe05gDO3KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUcCsmOeZUOP61nMgq3AMOYtw6uc9lZ1ojK38e4wmGE9kB87CyHqfI73BZyOOM9fM9T9JgkXXflFJ8ZFsj0mMKaRNHDqGD2vV4OSrDRKXvWeleydj%2BR5QRCIkS5Effld%2FHnixp%2B1OXU87kHTapCdJqDvcWwFJlKxqY1bZI%2BmBHETy8YGe6dG%2B0T9oB4YBdfnmEEHk4M%2BTmpTMRwJMOVc0lkMMKNB5gheoqxq4s%2Bjmvf77CLRNHwB21whpGUHAaCnEObCoSNH6D3ptqP1yNrGLSmpx0Z%2B1BbJn6oZ%2BFjRHplKYKsOT%2BJ5SlouAZd%2ByUNRGlv2IQF20Ok%2B%2FRGGzSGZb66T9vuKPC8KAgcR6N9zHupqmuGvJijBY2IowFwVfU%2FYM%2BTgUPbZTcTpDjyYUPCro3C4jyN4gPx5%2FgPOb24VRdjrUNytcazdaLqFVWaaJnEIIKFLXB9eyxAktdEOYBqTDPre1HLMv01o7OKK%2BZnDJO%2FfR08pAerrFZVSeQkXkHTVLoHtKn%2Fo3eL2J6OTg1ABoRgaRj%2BWAFNhAw%2BcGqDJEg4k%2Bngzb9e%2Bn3qJA90E1bUJ9fsSJGmF7GeXutpInjBP8F3wYo5qbgx0bd0lbBM2CUm8WpBmvPJeMns7p1s505SnyMq%2FP5NLPT5uG1kDCr7ILSBjqkAX6Kf8jb2hpMQmhkTFxSCefRJDHrzDi9RP8qjoII5l%2FEysL1sDhDKhrFDrfGSEpew7%2FX0lQFiiZVuhcVZVehpWza5rmKsFg0gmje5XBNbftrBQp%2FWvRu7YBZlDCjJG1LlWUebpdyXVxGzPdmXoKqocpS3Cvk5mQH2MUq3hpycdxOoW%2BRcxi7yjCMC3Oe%2BwMTiu1mQ7owvgrqF75J%2B7GXeVPu1Fn2&X-Amz-Signature=862b789e227411f3ba44aedaf409f7ae6cf7cf595e278aa252789723897bb462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632LWE7GN%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T084457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLdHmq1RxgGviU5ybmH6sRceippmVE1imiwqU9DxytzwIhAM3KvT6yaEu880YgljaKek7fe4pOsmKn3B%2BaKe05gDO3KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUcCsmOeZUOP61nMgq3AMOYtw6uc9lZ1ojK38e4wmGE9kB87CyHqfI73BZyOOM9fM9T9JgkXXflFJ8ZFsj0mMKaRNHDqGD2vV4OSrDRKXvWeleydj%2BR5QRCIkS5Effld%2FHnixp%2B1OXU87kHTapCdJqDvcWwFJlKxqY1bZI%2BmBHETy8YGe6dG%2B0T9oB4YBdfnmEEHk4M%2BTmpTMRwJMOVc0lkMMKNB5gheoqxq4s%2Bjmvf77CLRNHwB21whpGUHAaCnEObCoSNH6D3ptqP1yNrGLSmpx0Z%2B1BbJn6oZ%2BFjRHplKYKsOT%2BJ5SlouAZd%2ByUNRGlv2IQF20Ok%2B%2FRGGzSGZb66T9vuKPC8KAgcR6N9zHupqmuGvJijBY2IowFwVfU%2FYM%2BTgUPbZTcTpDjyYUPCro3C4jyN4gPx5%2FgPOb24VRdjrUNytcazdaLqFVWaaJnEIIKFLXB9eyxAktdEOYBqTDPre1HLMv01o7OKK%2BZnDJO%2FfR08pAerrFZVSeQkXkHTVLoHtKn%2Fo3eL2J6OTg1ABoRgaRj%2BWAFNhAw%2BcGqDJEg4k%2Bngzb9e%2Bn3qJA90E1bUJ9fsSJGmF7GeXutpInjBP8F3wYo5qbgx0bd0lbBM2CUm8WpBmvPJeMns7p1s505SnyMq%2FP5NLPT5uG1kDCr7ILSBjqkAX6Kf8jb2hpMQmhkTFxSCefRJDHrzDi9RP8qjoII5l%2FEysL1sDhDKhrFDrfGSEpew7%2FX0lQFiiZVuhcVZVehpWza5rmKsFg0gmje5XBNbftrBQp%2FWvRu7YBZlDCjJG1LlWUebpdyXVxGzPdmXoKqocpS3Cvk5mQH2MUq3hpycdxOoW%2BRcxi7yjCMC3Oe%2BwMTiu1mQ7owvgrqF75J%2B7GXeVPu1Fn2&X-Amz-Signature=cdd5cd50690884404632cb0c76e099e3250c2337fc0dfc7a1d470a64463773db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







