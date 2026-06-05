



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EWIE6VO%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T143748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFE4bCgdmpUZr0gm%2FhbkJoNaY5X6xG42pQdMEQZGtK8SAiEA0M0soV0zuWHdTMnBju20iKHfnC7cybHaKkmclKGLhXkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDFKaMKLiuS30qgYBJCrcA4NEaO1l%2BiSzeYPTfVf6byGrOrcVosr4XitVRmTQxnw9nPTZHowQCiJqeDPMc9yh9envP2N8T88FjMNP%2Fx%2FzTM4AUYA4%2BRf9KagAGdt6iToX4bI2kYVwNdqJ%2BzXHusi%2F6iI4d%2BadHM6gMdfdRuDVOQi1mJw4u4RUQ6uZqzqXqa6jb4C1CKHBZioSQDpWNfFbVowlLoAljkOkGV8x%2FvlBv8IHqOXVI534sn0KjTAA5beBWlLnDDWVfBRYwCNcvT2MsjzgYAi%2FWA3IcmMk3Ss7GPT3cci4HWucdJRG8qmQ%2FXauaYaG%2FYCcrtZRhTbH8VdQ9ShQXbA4x9YXpPZBTW3Rm8t07VvINET9t2o7UMysla1rXhb1NQkV2rvaex8oesPkZqPMhicyInKmQ6amygpccThXr1Dy44bEW9FcS2cIMoEPQq6pZ%2FVBYBspNA11V8xdjQL21xATO%2F%2ByPwy9%2BE2iUt6HPWUiff2nHP5t1mpAj0F4xeTV0I0f9FYmJXJPrMAO4qgNzZOp%2B9RHA%2BnQPAEZ29RIlVdkKitPUjXNUq4Pz6G3nDv9iiMfe7PtwuXL3JfMgcDqyJqAo2gU2nQQtA7xEt9zCsnMtHbGKSd3Y6Fyr6Pz06ySUi118rf4YQ5QMJeTi9EGOqUBVoGqBAEUXrMxZ2MAmTwa%2FObvaekfZwP9XWU8osJZWxi18ydaABBuVw1zdi1fs3tJa4S5vTNsEglk9jBJNzm2Z54JIJ5q4pKj9Es2kvs3ZSIrBHQ3Dg38ubUXPWixcKcLXp6ZbZrqKVv6PbrAYqel8ISBxyMTaFgV3SNJgpMgoRwCpkCl7fgfUzYU2wZ9n7ZdAw96GmMC1Y5YHgrlK%2FuTIK0523FN&X-Amz-Signature=f7b502143aac981b93117f12f923091bef089aaf071a8ff99eb75ef5908d5bb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EWIE6VO%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T143749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFE4bCgdmpUZr0gm%2FhbkJoNaY5X6xG42pQdMEQZGtK8SAiEA0M0soV0zuWHdTMnBju20iKHfnC7cybHaKkmclKGLhXkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDFKaMKLiuS30qgYBJCrcA4NEaO1l%2BiSzeYPTfVf6byGrOrcVosr4XitVRmTQxnw9nPTZHowQCiJqeDPMc9yh9envP2N8T88FjMNP%2Fx%2FzTM4AUYA4%2BRf9KagAGdt6iToX4bI2kYVwNdqJ%2BzXHusi%2F6iI4d%2BadHM6gMdfdRuDVOQi1mJw4u4RUQ6uZqzqXqa6jb4C1CKHBZioSQDpWNfFbVowlLoAljkOkGV8x%2FvlBv8IHqOXVI534sn0KjTAA5beBWlLnDDWVfBRYwCNcvT2MsjzgYAi%2FWA3IcmMk3Ss7GPT3cci4HWucdJRG8qmQ%2FXauaYaG%2FYCcrtZRhTbH8VdQ9ShQXbA4x9YXpPZBTW3Rm8t07VvINET9t2o7UMysla1rXhb1NQkV2rvaex8oesPkZqPMhicyInKmQ6amygpccThXr1Dy44bEW9FcS2cIMoEPQq6pZ%2FVBYBspNA11V8xdjQL21xATO%2F%2ByPwy9%2BE2iUt6HPWUiff2nHP5t1mpAj0F4xeTV0I0f9FYmJXJPrMAO4qgNzZOp%2B9RHA%2BnQPAEZ29RIlVdkKitPUjXNUq4Pz6G3nDv9iiMfe7PtwuXL3JfMgcDqyJqAo2gU2nQQtA7xEt9zCsnMtHbGKSd3Y6Fyr6Pz06ySUi118rf4YQ5QMJeTi9EGOqUBVoGqBAEUXrMxZ2MAmTwa%2FObvaekfZwP9XWU8osJZWxi18ydaABBuVw1zdi1fs3tJa4S5vTNsEglk9jBJNzm2Z54JIJ5q4pKj9Es2kvs3ZSIrBHQ3Dg38ubUXPWixcKcLXp6ZbZrqKVv6PbrAYqel8ISBxyMTaFgV3SNJgpMgoRwCpkCl7fgfUzYU2wZ9n7ZdAw96GmMC1Y5YHgrlK%2FuTIK0523FN&X-Amz-Signature=e0313efba5e680317f38f1b8cfec55148044b059f6b46d62e571e3dee7b7814f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







