



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V4BYOP4%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T022848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgtG9L3GlnbcG8qaEYl4DB2N2cwTHsX1Y5Ni0lefG%2BTwIgNJ9hhqiO4w9L9eH%2BewNx4kHPe6IM2tOT1jOVgbT5tjkqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXt4IDovqK0TpUhDyrcA3zGrYrL9aIM5wpByrKIDBKInP%2BHFC%2B%2FC%2FsjN2M7cCbZ4mClu2DBmhTXeFcc%2BVNLr2Pk4NoEVN1gIdGuNPazgsSSGfuZATou30sO0ZlbE7uvRi7jUas4%2BqoGgPVh4804Xy0eFPLesQ1sVpcZ3v6wscNF3%2BtmOh2izr29eJPGA0%2B5sWLs4vpyvWd%2BBytdd75itn%2FVWxr1syJhbHM8XJ2kZb58QV9hT3jM7P8y5HJDMltJ5ehRCuJpNpV06CjqdITsDg5W27ElqdA8Q6VTWX%2BRsxHOefAOnQN17J0pEzXqAiy5jhSHhQhm2tAn9Leb%2BgbxLSQ3CN%2F8uekMfUD88b6xOdVmZQcSx0JaDJXVx9fWUxgCX6MwFGv0gnd1%2FWWuKsIBk5a0gsDGFwI0qpVGbnR96j3LZQuxMzbJxMUvA1QsSleg15cdBLfTZ%2BCeCiPJKMq0Ckp5%2FmVsGHvAUQMY8QkyMEN8%2Bu4dKLY2YYGiAvavRxw3lNHEj2wUBQ79zToobC%2Fb2JHpCQPQCB1VbRu0VPXNHSeIac4cuVE3boovLpzSAq9r8%2BDV6U4zYZvtIOhXIlgpYIMHFv799%2Fe1pcqlQIUNmv0CSX2IOBn5tR8OgKvvYn23joUriBAE4AEN0XWOMO2DvNIGOqUBC3k8U7fjRpFgqYex8h%2BXXJtHpyn4f9jKnbDPyGCWVBj4LqXNBiXXqXSTqmG2%2FshwYj%2FP4W0YskLFF9NnqOWb2aLisOYoGcUlrhx9c4OWFzxKa4iNdg5wffSp0nRwyyqcLPf%2FqT0Oin8vfUfX1Dpmap2HCMhnqsyK9bsn2sFw90lp7U4PfWX%2BR28hTnckAdVEIkGg8CtogBcNJlGfzHH4JjKZMT0m&X-Amz-Signature=46d044fb9a1f03c2d605b4548d1c9807fc49dfef1b0102157d28376808a4e7ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V4BYOP4%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T022848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgtG9L3GlnbcG8qaEYl4DB2N2cwTHsX1Y5Ni0lefG%2BTwIgNJ9hhqiO4w9L9eH%2BewNx4kHPe6IM2tOT1jOVgbT5tjkqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXt4IDovqK0TpUhDyrcA3zGrYrL9aIM5wpByrKIDBKInP%2BHFC%2B%2FC%2FsjN2M7cCbZ4mClu2DBmhTXeFcc%2BVNLr2Pk4NoEVN1gIdGuNPazgsSSGfuZATou30sO0ZlbE7uvRi7jUas4%2BqoGgPVh4804Xy0eFPLesQ1sVpcZ3v6wscNF3%2BtmOh2izr29eJPGA0%2B5sWLs4vpyvWd%2BBytdd75itn%2FVWxr1syJhbHM8XJ2kZb58QV9hT3jM7P8y5HJDMltJ5ehRCuJpNpV06CjqdITsDg5W27ElqdA8Q6VTWX%2BRsxHOefAOnQN17J0pEzXqAiy5jhSHhQhm2tAn9Leb%2BgbxLSQ3CN%2F8uekMfUD88b6xOdVmZQcSx0JaDJXVx9fWUxgCX6MwFGv0gnd1%2FWWuKsIBk5a0gsDGFwI0qpVGbnR96j3LZQuxMzbJxMUvA1QsSleg15cdBLfTZ%2BCeCiPJKMq0Ckp5%2FmVsGHvAUQMY8QkyMEN8%2Bu4dKLY2YYGiAvavRxw3lNHEj2wUBQ79zToobC%2Fb2JHpCQPQCB1VbRu0VPXNHSeIac4cuVE3boovLpzSAq9r8%2BDV6U4zYZvtIOhXIlgpYIMHFv799%2Fe1pcqlQIUNmv0CSX2IOBn5tR8OgKvvYn23joUriBAE4AEN0XWOMO2DvNIGOqUBC3k8U7fjRpFgqYex8h%2BXXJtHpyn4f9jKnbDPyGCWVBj4LqXNBiXXqXSTqmG2%2FshwYj%2FP4W0YskLFF9NnqOWb2aLisOYoGcUlrhx9c4OWFzxKa4iNdg5wffSp0nRwyyqcLPf%2FqT0Oin8vfUfX1Dpmap2HCMhnqsyK9bsn2sFw90lp7U4PfWX%2BR28hTnckAdVEIkGg8CtogBcNJlGfzHH4JjKZMT0m&X-Amz-Signature=5f15a88e3d322aa4d9dc29d72349b415d20deb09a993c3151be98a8a847cdc00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







