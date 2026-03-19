



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JCXS2W6%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T065228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQCnK3llJ6M7SXkc16v8Y8M9AavoVENdAzKUIDIZLLnoVgIhAJkSV0oe0hhSLndXnVFTIi96sdLUEnr83p29SQoTsvH%2BKv8DCBcQABoMNjM3NDIzMTgzODA1IgwWQ0kerjkNgESkwYYq3AOXfKP9fQXlQOc9DYTKGpkSigTpEPEWnRJPCGOoBVrQi9b6k3hDHvhNyzHXviIRsFwYGwX0ZNAtQ4heTS%2FwgJ9W8yLAk8%2B2%2B3qks%2B8FZYyKVcsFhxHelAxml8p8oyj3Y9TdUvzXxqvcIKsKV95XK%2B9MDatKt4QQMRPDzIc1wIgRpNTVsQpM5G79H3rmDswnt0zvnFilaiFLIR1rHMpCBK5f2Q12YNFFlZbMSzEc9%2FVpNz95tSMBQIvYSDqLJpecIqF%2FuXFeyiSRfjjf6dHQ476PecOj9TgaZiReGnJH9zZWyZJhlAo%2BGCAN8S20sDQSpwsc15kkR3U%2BNUDytgtqDgth8An%2FWafY9TZm1yo98f7qifRWLh852SUcENGOgkQ4tBhQGA2W6XW8ZyzWjWaIIM4AXND3u1rc7oLa6alsRKeJeNzAp%2B0MSjAwJ%2Bt8RjFmbBthJAOBglMVkxBHKFWwSNPzkkojId3VeS3DCEQVyLiHqyUDp625VFfPPEvFI8P1AUHTGA2ntQWJyBjRoUAdzuoDQeh4l72PSuo33UdqFaHTT%2FM9MEGMQU3bheuPqmtYyPtpF9jUihQgM%2B7y1P6nxSEZ3W6xDUpnjpkQfdwbg8o8WUj%2Fs5MhA1lCo2wTLzD1o%2B7NBjqkAfNGjx1aUtuO7FIVyMYWA%2Bz0jAs7uD%2FPbZjfovOzwG2hfjCHtkl4blM0IoxbzNzTj7L821%2Fh%2FA%2BAKN3XhAi2FkJ3EvOWLg8q0n3yxWTx%2BtzDfbuwz%2FLsuwaMIPbxCOE4PMeCUF%2BwmC5Y3VQ3xdPG6mGzsRu8rkkJUq4E6iq%2F5LSQsGrbbX5GnR7imghc7YSi8jVWOZlQjn%2F4V5OpPSgQ0VvEtoOI&X-Amz-Signature=ad571ad069f26a3f7d7b397c7b13429ad6ff875ad0d207f51d946933bb804f6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JCXS2W6%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T065228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQCnK3llJ6M7SXkc16v8Y8M9AavoVENdAzKUIDIZLLnoVgIhAJkSV0oe0hhSLndXnVFTIi96sdLUEnr83p29SQoTsvH%2BKv8DCBcQABoMNjM3NDIzMTgzODA1IgwWQ0kerjkNgESkwYYq3AOXfKP9fQXlQOc9DYTKGpkSigTpEPEWnRJPCGOoBVrQi9b6k3hDHvhNyzHXviIRsFwYGwX0ZNAtQ4heTS%2FwgJ9W8yLAk8%2B2%2B3qks%2B8FZYyKVcsFhxHelAxml8p8oyj3Y9TdUvzXxqvcIKsKV95XK%2B9MDatKt4QQMRPDzIc1wIgRpNTVsQpM5G79H3rmDswnt0zvnFilaiFLIR1rHMpCBK5f2Q12YNFFlZbMSzEc9%2FVpNz95tSMBQIvYSDqLJpecIqF%2FuXFeyiSRfjjf6dHQ476PecOj9TgaZiReGnJH9zZWyZJhlAo%2BGCAN8S20sDQSpwsc15kkR3U%2BNUDytgtqDgth8An%2FWafY9TZm1yo98f7qifRWLh852SUcENGOgkQ4tBhQGA2W6XW8ZyzWjWaIIM4AXND3u1rc7oLa6alsRKeJeNzAp%2B0MSjAwJ%2Bt8RjFmbBthJAOBglMVkxBHKFWwSNPzkkojId3VeS3DCEQVyLiHqyUDp625VFfPPEvFI8P1AUHTGA2ntQWJyBjRoUAdzuoDQeh4l72PSuo33UdqFaHTT%2FM9MEGMQU3bheuPqmtYyPtpF9jUihQgM%2B7y1P6nxSEZ3W6xDUpnjpkQfdwbg8o8WUj%2Fs5MhA1lCo2wTLzD1o%2B7NBjqkAfNGjx1aUtuO7FIVyMYWA%2Bz0jAs7uD%2FPbZjfovOzwG2hfjCHtkl4blM0IoxbzNzTj7L821%2Fh%2FA%2BAKN3XhAi2FkJ3EvOWLg8q0n3yxWTx%2BtzDfbuwz%2FLsuwaMIPbxCOE4PMeCUF%2BwmC5Y3VQ3xdPG6mGzsRu8rkkJUq4E6iq%2F5LSQsGrbbX5GnR7imghc7YSi8jVWOZlQjn%2F4V5OpPSgQ0VvEtoOI&X-Amz-Signature=26e626993b4eb4ab55b3421c2b05a3ed96a1688de3204b6f3c9d58a88246ef9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







