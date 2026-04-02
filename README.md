



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXEWUC37%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T015336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1vWXKyt1AejI2%2B%2BkMV8DFHEAiuNvq6U061ElPdeySSAIhAJEoZqqXnrFwy38TOT7PfXZZ0EFZoo7vXm8iS3CZcFCpKv8DCGIQABoMNjM3NDIzMTgzODA1IgytN770hU%2BOPaYI8mkq3APQE4Ox4dZ%2F33Z0qEsJGVtoUEtHvjB4F9XaV9NpqAddCHqtzafboRElh3HwfCiRZPnMY7K%2FNJpxhpMJqUvNibuBYcsVclR6qHtHP8%2BZ3D3yU7SSeyoXks1ix0xP973XTr7AYY1PW8Ey%2B%2BlSjUAd84QYIiNCJQeORuilzXAS08UHn5dQiD2h3kXOpTLdHZoqMr%2F87nBZ9bhjiBcW0Y4zQFaDgV0ObJfwLccXtADxCRBawuPE67o2R%2Bz%2Bs2ADSJU02PPnINnkSQrNL%2FxT8dzaBUfd1PKG6c6IxwOy9O9TVOSJc6lxUUN8J1nbNVhqjkdLAK%2FN3122mVDpY6v4g2GqBgnhOe4sF6xX7gnhWkQqNP1CTSWjW3WCLOwf2ZwNfmh9kOTxL8m46EZaFOGvPaLftv2BII4oVcm8euEYKP7bMREKpGG7HV9Q1B9y3qtp4M2MK%2BiMCGUcasRei0yv5k2PjA%2FbgsJ%2FY184E6APtLx90kVkkqNzy0LiRHJhGXO7%2FWGogOr9PTwcjcy2z2GQmWFs0c90Jyyog3uBuAH30rsHXjTxt6EuJjgqVe4pMzXGD4YNWdqiLp10DGICplqdxrlFOWXSrKRWjyfv0StpVkhDtC6hZZ4CHukCNvf%2BstoI5TC9irfOBjqkAaoDhOkHCXKYRGqp%2BFTxDmYmXEvpBHltL%2BPN7sukQ543kxKyziHUVrRz4tOKv7NffnEygrHNm4yv19SuSozqY3urx1J4upi1LQ2W9C2tv5kvvlleq0TiOjTAGuHW6xeydpdlvoh8dijUjeRQ3jowwdVZxeeCLHbcJJ%2FOk%2BG8m5xSPZSdn9pDYqq5KgJ7SCcCqz%2BMm5EBgm4W%2BbkxhuHnwC3am7%2F8&X-Amz-Signature=4e7ea57f32ab780fa2fc8c43d3303904533d7097f152c3c9fa7fa858b5ae134b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXEWUC37%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T015337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1vWXKyt1AejI2%2B%2BkMV8DFHEAiuNvq6U061ElPdeySSAIhAJEoZqqXnrFwy38TOT7PfXZZ0EFZoo7vXm8iS3CZcFCpKv8DCGIQABoMNjM3NDIzMTgzODA1IgytN770hU%2BOPaYI8mkq3APQE4Ox4dZ%2F33Z0qEsJGVtoUEtHvjB4F9XaV9NpqAddCHqtzafboRElh3HwfCiRZPnMY7K%2FNJpxhpMJqUvNibuBYcsVclR6qHtHP8%2BZ3D3yU7SSeyoXks1ix0xP973XTr7AYY1PW8Ey%2B%2BlSjUAd84QYIiNCJQeORuilzXAS08UHn5dQiD2h3kXOpTLdHZoqMr%2F87nBZ9bhjiBcW0Y4zQFaDgV0ObJfwLccXtADxCRBawuPE67o2R%2Bz%2Bs2ADSJU02PPnINnkSQrNL%2FxT8dzaBUfd1PKG6c6IxwOy9O9TVOSJc6lxUUN8J1nbNVhqjkdLAK%2FN3122mVDpY6v4g2GqBgnhOe4sF6xX7gnhWkQqNP1CTSWjW3WCLOwf2ZwNfmh9kOTxL8m46EZaFOGvPaLftv2BII4oVcm8euEYKP7bMREKpGG7HV9Q1B9y3qtp4M2MK%2BiMCGUcasRei0yv5k2PjA%2FbgsJ%2FY184E6APtLx90kVkkqNzy0LiRHJhGXO7%2FWGogOr9PTwcjcy2z2GQmWFs0c90Jyyog3uBuAH30rsHXjTxt6EuJjgqVe4pMzXGD4YNWdqiLp10DGICplqdxrlFOWXSrKRWjyfv0StpVkhDtC6hZZ4CHukCNvf%2BstoI5TC9irfOBjqkAaoDhOkHCXKYRGqp%2BFTxDmYmXEvpBHltL%2BPN7sukQ543kxKyziHUVrRz4tOKv7NffnEygrHNm4yv19SuSozqY3urx1J4upi1LQ2W9C2tv5kvvlleq0TiOjTAGuHW6xeydpdlvoh8dijUjeRQ3jowwdVZxeeCLHbcJJ%2FOk%2BG8m5xSPZSdn9pDYqq5KgJ7SCcCqz%2BMm5EBgm4W%2BbkxhuHnwC3am7%2F8&X-Amz-Signature=0aa8a213173f7a2644df931ee36260a8ebd90b52939bf51b09f1541de453a266&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







