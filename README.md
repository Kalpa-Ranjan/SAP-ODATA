



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D6T2QOV%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T145258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFunffa7ROiPsaNFxyja1diJvmau9Ka2ZgwQcFnhH%2BOIAiB48YsPGRBDxe1toNppuEt8N9fGd9Uf0JcBVLHFbWQQ1iqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpfj06YszijaPt%2FuHKtwDhVb3BeLxMPYSAJJ5jv0V2rS%2BzJ%2BH8F7tmfXa1B2B5frmsuWZQ1hLzS5SLvLqbLJ7S5%2Bz3%2BJlHUFIUR6wA%2BDy3ViCs1Zmyve56i48kLI7CSqWhXdq7Dv9Rn4XANS2YhEpKe2y2vWN%2FxkINkbU6xfT6DyUChv3oJxRsXRAor%2B9BU8ukrKRYRajGNFujwAiizK8JKIoK1%2F9iRLSw%2FGPnEgw6Pi4SCBKzbeOT0SZHdbxYfigiHWKOMOqaiTxGQFNTotklPmDSA7viRSvKIjdzscRX4sZ15Fbg7HXg5NLGHYP76lJ8B64tADKKXt8%2FmUKiEu8Qi70FLhr1kgfZpXv02JToYA7gPHmMDssyGJopsCL8qS3A9694umxTy%2F%2FHWNzE2G36VyHPh%2B%2FLaKIGe67Xy5pyVbpdjLgkJ0MuM%2Br5EbjARjQWC6noLFOrYRuv1axuYFo%2BJ1JUyeUuis7CAkS%2B0%2BqpGUcInyH46vZN6iBRHmTKwPFinFZ%2FHJccBP4cLc4XT7MNqpMDpOkyRnL0mU4kEUzvGoyi0ba7wGFxtvFN5C2IcIGKX4IJoNtaX7oGfHOpPMp6NEEBkVYiBWxLUF2spkn2ZW82vgD7Ln6OmHkRPVloUOn7kfvMhZs44nFltkw06nV0QY6pgFjuPNuTSiKN8lIKwBVDPQH7SNi7ctUEriSxVBouMLey5CzB5vHAkiUW5GiQDu%2BUHMV%2BgxUAV3nwgSSFlCjAc3ePtE7MMIXbnJjLkglK4K3VSMWx52oenrSdcwJDJobNILatqXs35gTqPesdcFZ7nzAlkwk2HNdTq%2Bn%2FKmJJqaWU21h4cu%2BeVDyN2F22%2F%2Fm8JBGVE66sAanWLuzFdzVgUFrDRU1gzm4&X-Amz-Signature=39770d29d1703f8446866d34abb0987737f5ff36c611e05d832cfc05c618ca49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D6T2QOV%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T145259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFunffa7ROiPsaNFxyja1diJvmau9Ka2ZgwQcFnhH%2BOIAiB48YsPGRBDxe1toNppuEt8N9fGd9Uf0JcBVLHFbWQQ1iqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpfj06YszijaPt%2FuHKtwDhVb3BeLxMPYSAJJ5jv0V2rS%2BzJ%2BH8F7tmfXa1B2B5frmsuWZQ1hLzS5SLvLqbLJ7S5%2Bz3%2BJlHUFIUR6wA%2BDy3ViCs1Zmyve56i48kLI7CSqWhXdq7Dv9Rn4XANS2YhEpKe2y2vWN%2FxkINkbU6xfT6DyUChv3oJxRsXRAor%2B9BU8ukrKRYRajGNFujwAiizK8JKIoK1%2F9iRLSw%2FGPnEgw6Pi4SCBKzbeOT0SZHdbxYfigiHWKOMOqaiTxGQFNTotklPmDSA7viRSvKIjdzscRX4sZ15Fbg7HXg5NLGHYP76lJ8B64tADKKXt8%2FmUKiEu8Qi70FLhr1kgfZpXv02JToYA7gPHmMDssyGJopsCL8qS3A9694umxTy%2F%2FHWNzE2G36VyHPh%2B%2FLaKIGe67Xy5pyVbpdjLgkJ0MuM%2Br5EbjARjQWC6noLFOrYRuv1axuYFo%2BJ1JUyeUuis7CAkS%2B0%2BqpGUcInyH46vZN6iBRHmTKwPFinFZ%2FHJccBP4cLc4XT7MNqpMDpOkyRnL0mU4kEUzvGoyi0ba7wGFxtvFN5C2IcIGKX4IJoNtaX7oGfHOpPMp6NEEBkVYiBWxLUF2spkn2ZW82vgD7Ln6OmHkRPVloUOn7kfvMhZs44nFltkw06nV0QY6pgFjuPNuTSiKN8lIKwBVDPQH7SNi7ctUEriSxVBouMLey5CzB5vHAkiUW5GiQDu%2BUHMV%2BgxUAV3nwgSSFlCjAc3ePtE7MMIXbnJjLkglK4K3VSMWx52oenrSdcwJDJobNILatqXs35gTqPesdcFZ7nzAlkwk2HNdTq%2Bn%2FKmJJqaWU21h4cu%2BeVDyN2F22%2F%2Fm8JBGVE66sAanWLuzFdzVgUFrDRU1gzm4&X-Amz-Signature=dce4174f39aa1ffea0843a8a6be1163b80ab02d2f98c2b20b767cacbb8a5df59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







