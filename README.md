



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZUEYFEM%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T125015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDdCywkuBkW1K53eKNWZdBtCKrfw1DtV03b3oVSAeKkhQIhAKgwQl970x3dIV%2BWqKpm%2BzqGrepwaRFIjriKBSAJuIetKv8DCDQQABoMNjM3NDIzMTgzODA1IgzE3nc0fM96BK%2BwTmUq3AOAZwhK86isoBQc2A5iKS1FvoWuiSQUC5PV%2FzGS%2BqRlQHN4O7H3gCjrvr7r%2B%2B7PQ80mbgtj3j6F9080HGw1m7ac5gl%2FRFQ%2FheDrZS3bYGLYI2yuGwfnWh73BHizV8WOaU7IuUEVLlwjTmrP1VGUdGOwVNhUVuGifRliYLzMY6DKW%2FBdynDc7c%2FSD5ZIa7IkQMloB1GlBDVOFl5jjqyxank9r035riUzSvJkz8vhBRjJ3zxdSMn27Px0crLkbx2xdM3ozEUMurtQS%2FSeIU43kMH0DeAMr1yww5ZDg8T0%2Fo%2Br5QW7QQ4hb0PLU17L2kNXy945froJl19yUGvUGu6vmRqiV9pvFgThFfTkPDphQFxirAlfFRcFFUTI00WV8DIs4Sxxq6VcluwDTeHPZIdqrKjImQktkbSpQVNddrl5f5dxIGDBtKo6VovQn6CvcgSrii%2FaieDbQaBOjOllAE0aZbzuHeLd7gZAXb1TRN7ihICNSBJFldvJrqNV2a3sl7MKsTHs3lIz5LKrguskkPbSSGt5xHyTNC7smissGNiWZVRp%2B0Xrzqpanl2K%2FuTCLL5Khgz2wJRRMF3fiPf8g288YBCmBsnfun%2F%2Ffqmy7zUuCGM81hVaHYEs7pAsStCx4DCX2PTNBjqkAXrtIHsTFvVnQNm5LVWnNDPtOOFG7w6PVb%2FDVN7EZiO0CT3ofhw4vVhlTKSZP%2BinXZ4amjCK8ahHRYZXXWP6AmXY0Qjp7cC%2B5Hkw1yQJABx9L91eiSNEDmoQwrMGV%2FefsEtkbZ59eEKix2s2C72eo1ta36R7nWhipqQWXnPzBQ2lgvzPQ29SRsXDce%2BXxxAbs0yriz2jg9Xp8RErfybQE8s57VfT&X-Amz-Signature=46941545f99e0e372f8652a45224718b2fc8e82bd2e2bc655f89240916a935a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZUEYFEM%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T125015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDdCywkuBkW1K53eKNWZdBtCKrfw1DtV03b3oVSAeKkhQIhAKgwQl970x3dIV%2BWqKpm%2BzqGrepwaRFIjriKBSAJuIetKv8DCDQQABoMNjM3NDIzMTgzODA1IgzE3nc0fM96BK%2BwTmUq3AOAZwhK86isoBQc2A5iKS1FvoWuiSQUC5PV%2FzGS%2BqRlQHN4O7H3gCjrvr7r%2B%2B7PQ80mbgtj3j6F9080HGw1m7ac5gl%2FRFQ%2FheDrZS3bYGLYI2yuGwfnWh73BHizV8WOaU7IuUEVLlwjTmrP1VGUdGOwVNhUVuGifRliYLzMY6DKW%2FBdynDc7c%2FSD5ZIa7IkQMloB1GlBDVOFl5jjqyxank9r035riUzSvJkz8vhBRjJ3zxdSMn27Px0crLkbx2xdM3ozEUMurtQS%2FSeIU43kMH0DeAMr1yww5ZDg8T0%2Fo%2Br5QW7QQ4hb0PLU17L2kNXy945froJl19yUGvUGu6vmRqiV9pvFgThFfTkPDphQFxirAlfFRcFFUTI00WV8DIs4Sxxq6VcluwDTeHPZIdqrKjImQktkbSpQVNddrl5f5dxIGDBtKo6VovQn6CvcgSrii%2FaieDbQaBOjOllAE0aZbzuHeLd7gZAXb1TRN7ihICNSBJFldvJrqNV2a3sl7MKsTHs3lIz5LKrguskkPbSSGt5xHyTNC7smissGNiWZVRp%2B0Xrzqpanl2K%2FuTCLL5Khgz2wJRRMF3fiPf8g288YBCmBsnfun%2F%2Ffqmy7zUuCGM81hVaHYEs7pAsStCx4DCX2PTNBjqkAXrtIHsTFvVnQNm5LVWnNDPtOOFG7w6PVb%2FDVN7EZiO0CT3ofhw4vVhlTKSZP%2BinXZ4amjCK8ahHRYZXXWP6AmXY0Qjp7cC%2B5Hkw1yQJABx9L91eiSNEDmoQwrMGV%2FefsEtkbZ59eEKix2s2C72eo1ta36R7nWhipqQWXnPzBQ2lgvzPQ29SRsXDce%2BXxxAbs0yriz2jg9Xp8RErfybQE8s57VfT&X-Amz-Signature=dda73be7c0d923a8fe5c43a77c713213dd81e0076d69a2494b45483ed0fec7be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







