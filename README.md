



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YENA5T5Y%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T183618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDGrkZfq8jGYnorJcX84likQv3fHasWL0ghkJvCHsW9pwIhAN6Ixjw0FS0tpOn7i5BkpxPxdyejLBpVc%2FUsRvvVKhHhKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6bFKx1rSuVmNTfZUq3AN2q8SeQTEz26MSHLTKQjhKmfR9mdqyjDNLrb5EGNyU3HGJ2pO%2FBTbhb7vztZoowMVOW80BReCL%2BJvIlJxLnLBN%2BZaBgclDZWnhyqOUhwvfWkJwYSqfAWjlY%2BV9J7ZNyTZqquy0Yh%2BOU9PvDlwDdrhAe235FmK1VknOFNjkJMFXrAgZgWQDrsgft5%2BnRM7z56gDvG2lCTXVI2JqWH22C2mJxC7oKCLBSBKyFkMp1Ke8rLUsNy8jjc2gmQ5Ltc33nM%2BdSjK2FriacD1cBmm96f15vQeuxrcOhunMUctNq6C%2F2llP0GbOfGQe%2BVP3oY3wxfh98RBqowGBZOtH1u7yMwwkqTIiiGQdX9YXAekMuEK%2B6%2FClVyZrV3nsuJXmq%2BDzw60IeQFmhVP1eP7hrzXUxpqvUWvU5G4y%2FE9QUFMBHravGpmPwV%2Fk8Od9CFoqXq%2FRmX0rJyUpnJx3eJZyzkcKq%2BaYYRPvk6cdI1i%2Bitq9NnmfJ2q0qlYmYFwJUQLu8extGMJZoza3FX%2FT%2BfESON9eQQjLwy%2B2bzg5PIkCn5JtgQqk5AfLDaw0vuLZ9bgMnFrhjhGciQmHRV9GRn82OCLjxUCfc6aK8NroSi5HKK3ZOKSFJyjIlkWaNsHtmqsBZDDYxIPMBjqkAbgIMDeaSdINDsKnFNMEUu%2BPNVey79dk8QbRgHCpZfmSdKYrvC9UUyDLbaQDsY0z5rkRFNP0dn5DE4fwO%2BiIvyuEaFDPZQDiu%2F0ynBKG0Mxj9iRNbGar%2Bp9xE9YmnAfU25jC9moKRQVePCOFSfEZwKtkWFaILenOPngO7TlPtX%2B150QMnrH%2FICmhkAsVVGlFaxt9hE0HU1MxDg6byKVABaLBuZFS&X-Amz-Signature=7849fa28ff28f2165f9f2f3353fbd7b5bb5aaee11fd07f88910be85765839c50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YENA5T5Y%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T183618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDGrkZfq8jGYnorJcX84likQv3fHasWL0ghkJvCHsW9pwIhAN6Ixjw0FS0tpOn7i5BkpxPxdyejLBpVc%2FUsRvvVKhHhKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6bFKx1rSuVmNTfZUq3AN2q8SeQTEz26MSHLTKQjhKmfR9mdqyjDNLrb5EGNyU3HGJ2pO%2FBTbhb7vztZoowMVOW80BReCL%2BJvIlJxLnLBN%2BZaBgclDZWnhyqOUhwvfWkJwYSqfAWjlY%2BV9J7ZNyTZqquy0Yh%2BOU9PvDlwDdrhAe235FmK1VknOFNjkJMFXrAgZgWQDrsgft5%2BnRM7z56gDvG2lCTXVI2JqWH22C2mJxC7oKCLBSBKyFkMp1Ke8rLUsNy8jjc2gmQ5Ltc33nM%2BdSjK2FriacD1cBmm96f15vQeuxrcOhunMUctNq6C%2F2llP0GbOfGQe%2BVP3oY3wxfh98RBqowGBZOtH1u7yMwwkqTIiiGQdX9YXAekMuEK%2B6%2FClVyZrV3nsuJXmq%2BDzw60IeQFmhVP1eP7hrzXUxpqvUWvU5G4y%2FE9QUFMBHravGpmPwV%2Fk8Od9CFoqXq%2FRmX0rJyUpnJx3eJZyzkcKq%2BaYYRPvk6cdI1i%2Bitq9NnmfJ2q0qlYmYFwJUQLu8extGMJZoza3FX%2FT%2BfESON9eQQjLwy%2B2bzg5PIkCn5JtgQqk5AfLDaw0vuLZ9bgMnFrhjhGciQmHRV9GRn82OCLjxUCfc6aK8NroSi5HKK3ZOKSFJyjIlkWaNsHtmqsBZDDYxIPMBjqkAbgIMDeaSdINDsKnFNMEUu%2BPNVey79dk8QbRgHCpZfmSdKYrvC9UUyDLbaQDsY0z5rkRFNP0dn5DE4fwO%2BiIvyuEaFDPZQDiu%2F0ynBKG0Mxj9iRNbGar%2Bp9xE9YmnAfU25jC9moKRQVePCOFSfEZwKtkWFaILenOPngO7TlPtX%2B150QMnrH%2FICmhkAsVVGlFaxt9hE0HU1MxDg6byKVABaLBuZFS&X-Amz-Signature=393a9a8a8b97bc27c237dde01ecd6a663dbcd657ac8519def9795fea92b6cb2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







