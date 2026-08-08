



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMGFGBZI%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T182850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8IBPE3f%2BiA2QC8yDRrakUQMQ6HIMnpz0E2fH2%2FHF1qgIhAMuTNCeS1tjaL0M%2Bu1lFrKunBCvBxSP6rXOXStwSoX4wKv8DCHMQABoMNjM3NDIzMTgzODA1IgzCV4vbO81ASBE1iioq3APWiQrNzR1I9BZWH9WnPioZABuxeWilaITk6GZaAog3jZRhEn%2BdRpQ2J6klXgpS%2BcnJoZfugPT0olsGcjva0GQP1CpPrtXTWEs4jfPNib2ueN47z%2BhshYWNoddElsKe6%2FngVuZV29DnFZG8ZN1Bl%2BIWnaaosbzUqNucq%2B8LAeBXXc5qN%2BSD5oDHIS6mTbLb%2F9TP%2B8ECT%2BcpMhqtQ4Qf4W6bOs3BjBl3x%2FK5NnnOSLp%2FpdbnlnPjI622%2FBktg4e3Q76RwcEMd%2BSu2UrT3IgfmpoU7xyNgHEHRZW1MPJdWuvwxyscvOoLkube9JHEnrzMk2IEKa2ewWPVf%2FrRWS604AyUOx5aeK9rw%2FCrnEJqwu8%2B%2Fjhte0cTkNiPjDASvZwFKheIuQOf0TUwaLKimF%2BYvC3e2n2FfJq%2FnTAqvA0yp3PexGA1OxuXPNMAOKfG85QTTkfOsrKukHzX4TQ3QlQ%2BBkn85xqusaFdzv5nru%2FDhyMmSdYH%2B4AUbZVi%2BAbSi83QUb0gIauu7oPvxTezBfLMFTWfCETNvZKHoAJp1I%2BCcRgdRTFullmbN9eDR4ZGmIw4S3JCtxJMP8sNxkbLWgPbxLYNHSOY8lbDvyuLRw5yk3KMMXK8OmRRm9CiGs5ZVDDZ0t3TBjqkAUR1HaInSU71UcvpszhnuD2ZgORl3E1cfeTqYi0j3oLHrc55oeeY6WuG5OMurrCujRT1w1Y%2FEm8XjBMEbisOQitVxqkTUMVODrFWCVgVJFDoaFc3AWinPznXvTpIh12BxUk8PEs0Zzc%2FPfirpTV6c96LDY4PUqiBwzATwG8XHdPK9yw6PVX4qKSj%2BgAQLmXG3dAsydBkdpHqcVQUC90SLLTNbf6c&X-Amz-Signature=4a31c1da7948886563f7cd0a2697bd2442924198718a2690941090a6dc03615e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMGFGBZI%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T182850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8IBPE3f%2BiA2QC8yDRrakUQMQ6HIMnpz0E2fH2%2FHF1qgIhAMuTNCeS1tjaL0M%2Bu1lFrKunBCvBxSP6rXOXStwSoX4wKv8DCHMQABoMNjM3NDIzMTgzODA1IgzCV4vbO81ASBE1iioq3APWiQrNzR1I9BZWH9WnPioZABuxeWilaITk6GZaAog3jZRhEn%2BdRpQ2J6klXgpS%2BcnJoZfugPT0olsGcjva0GQP1CpPrtXTWEs4jfPNib2ueN47z%2BhshYWNoddElsKe6%2FngVuZV29DnFZG8ZN1Bl%2BIWnaaosbzUqNucq%2B8LAeBXXc5qN%2BSD5oDHIS6mTbLb%2F9TP%2B8ECT%2BcpMhqtQ4Qf4W6bOs3BjBl3x%2FK5NnnOSLp%2FpdbnlnPjI622%2FBktg4e3Q76RwcEMd%2BSu2UrT3IgfmpoU7xyNgHEHRZW1MPJdWuvwxyscvOoLkube9JHEnrzMk2IEKa2ewWPVf%2FrRWS604AyUOx5aeK9rw%2FCrnEJqwu8%2B%2Fjhte0cTkNiPjDASvZwFKheIuQOf0TUwaLKimF%2BYvC3e2n2FfJq%2FnTAqvA0yp3PexGA1OxuXPNMAOKfG85QTTkfOsrKukHzX4TQ3QlQ%2BBkn85xqusaFdzv5nru%2FDhyMmSdYH%2B4AUbZVi%2BAbSi83QUb0gIauu7oPvxTezBfLMFTWfCETNvZKHoAJp1I%2BCcRgdRTFullmbN9eDR4ZGmIw4S3JCtxJMP8sNxkbLWgPbxLYNHSOY8lbDvyuLRw5yk3KMMXK8OmRRm9CiGs5ZVDDZ0t3TBjqkAUR1HaInSU71UcvpszhnuD2ZgORl3E1cfeTqYi0j3oLHrc55oeeY6WuG5OMurrCujRT1w1Y%2FEm8XjBMEbisOQitVxqkTUMVODrFWCVgVJFDoaFc3AWinPznXvTpIh12BxUk8PEs0Zzc%2FPfirpTV6c96LDY4PUqiBwzATwG8XHdPK9yw6PVX4qKSj%2BgAQLmXG3dAsydBkdpHqcVQUC90SLLTNbf6c&X-Amz-Signature=bddd43cc6b06e3a9ebc8b394dffdad9121469f99dca465ff0f3966ff6d480d8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







