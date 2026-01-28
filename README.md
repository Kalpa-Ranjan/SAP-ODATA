



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6VINTQZ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T123848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETFFPZ1%2BNYa%2B2Ry5SEKKisdeJ1LUNaDgtIGcxyMm8ODAiEA%2BDRHjmgOQI%2FQbhzW8FwYu8fAhj62nlf9qUJ7EQXasiUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDOzU7HHnhK9%2BlFVvhircAzXVuBZQZ6GaT6i5dnnAK4GrLF8Cj1eLpzMzPuSdQhQ9DvQRy5zUReBY%2F4KKBzHEkwo%2FBHuVp%2BMKDZ8skc0CJ29E1ia%2FjaZ7qGBPt9CgfCCM4nPn8SiYuljPLEFpgXm7gHf79f6lHcXclEKrr6pj%2B16G5AAuE1bxSONnG5P6Ko8kgsNwbFCIPjdg7ykS5ToGCQy3LJV4Vbepkv1faeZ9awZHCVivxjBPYpilfwUyd%2FNcoRp77e7Mb%2FSBCLVuwWoFlAlOA2Z7NwdhSAimGOKNASoWQRIgaMt4WhhwCsC20tRAgvCvScmdYjrX6PZdf6LvmkNZzsCGppu1BJcG%2B%2FYWj%2BcF98s%2Ba6n5%2Bl6GhUKycn1fqQ6MOwe1nQ0WSkmKWQ0hJFIX31Af1zNSBMlhxaNVxISZkkF4ilRKD2%2BcIXsJ0%2Fcm70o5dhTp%2BwHovFisj5OZIpO7BjCBVOGePQpvaqrvAxaj1MpePrKNtK5kPv1ahrjibuge5KO7L5DzIH2AkaTGyCjiW2VB8Z%2BLOD7U5VuD4BKWivf2iEnBISPOc34jJ4c6Yz%2Bajnoq7tGblaMbI7tpVxWTQbrN3kk3xAPDu8xrQu%2Bh6887bRJRYAnub%2FxF1f8X1%2F18%2Fm5GlcbQ4iyTMOn358sGOqUBWm0LlnvYh4lTYj5NQN6dof2mCPHQ07s0I29IIJ3CFK0yZXrXTIG17zkOixsliaCen6tOQtIG42Kt%2Fz%2BB3bEM0cmlIUWT%2B26%2F47G1XoiGfL9Q1wzZAYixYXdylaKUHwJj505K9J5pLcMrsNYM2xNtQTbm0NReTIpgFU25AlRgDwf9xOHYp5ZlhCTFTaHKeHUYbOvKVPAvfNbS4EvEUMiILUm8Td65&X-Amz-Signature=5b6ac8e7552836e515cc2019cbe45b69b2826d279749a56a7418813edc0589a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6VINTQZ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T123848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETFFPZ1%2BNYa%2B2Ry5SEKKisdeJ1LUNaDgtIGcxyMm8ODAiEA%2BDRHjmgOQI%2FQbhzW8FwYu8fAhj62nlf9qUJ7EQXasiUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDOzU7HHnhK9%2BlFVvhircAzXVuBZQZ6GaT6i5dnnAK4GrLF8Cj1eLpzMzPuSdQhQ9DvQRy5zUReBY%2F4KKBzHEkwo%2FBHuVp%2BMKDZ8skc0CJ29E1ia%2FjaZ7qGBPt9CgfCCM4nPn8SiYuljPLEFpgXm7gHf79f6lHcXclEKrr6pj%2B16G5AAuE1bxSONnG5P6Ko8kgsNwbFCIPjdg7ykS5ToGCQy3LJV4Vbepkv1faeZ9awZHCVivxjBPYpilfwUyd%2FNcoRp77e7Mb%2FSBCLVuwWoFlAlOA2Z7NwdhSAimGOKNASoWQRIgaMt4WhhwCsC20tRAgvCvScmdYjrX6PZdf6LvmkNZzsCGppu1BJcG%2B%2FYWj%2BcF98s%2Ba6n5%2Bl6GhUKycn1fqQ6MOwe1nQ0WSkmKWQ0hJFIX31Af1zNSBMlhxaNVxISZkkF4ilRKD2%2BcIXsJ0%2Fcm70o5dhTp%2BwHovFisj5OZIpO7BjCBVOGePQpvaqrvAxaj1MpePrKNtK5kPv1ahrjibuge5KO7L5DzIH2AkaTGyCjiW2VB8Z%2BLOD7U5VuD4BKWivf2iEnBISPOc34jJ4c6Yz%2Bajnoq7tGblaMbI7tpVxWTQbrN3kk3xAPDu8xrQu%2Bh6887bRJRYAnub%2FxF1f8X1%2F18%2Fm5GlcbQ4iyTMOn358sGOqUBWm0LlnvYh4lTYj5NQN6dof2mCPHQ07s0I29IIJ3CFK0yZXrXTIG17zkOixsliaCen6tOQtIG42Kt%2Fz%2BB3bEM0cmlIUWT%2B26%2F47G1XoiGfL9Q1wzZAYixYXdylaKUHwJj505K9J5pLcMrsNYM2xNtQTbm0NReTIpgFU25AlRgDwf9xOHYp5ZlhCTFTaHKeHUYbOvKVPAvfNbS4EvEUMiILUm8Td65&X-Amz-Signature=840dcd7307a2b150a7f9311c6eeb293cc8549b634a28ae4b0ec5d11899701cd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







