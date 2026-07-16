



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UBDB3H3%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T020558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHr2p0f2L4RyV7VWcBklq2getWM6Bfmth67MTqJdHBd8AiEAiYRatgp6T9kOKMCO1lcaEBbDCya2iKcUCt4HanbItPoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDJJhRq8MhqR7pwZtoircA7F8P%2BKf1xbnjOfpUXHkSVCKS4rldBJLQwvSl69yP0yMJEXnhc5lAuO2uDW6qx%2BkxMrNkglcWJykNVGw7QbEPUZLFa9YaeEdZBT6wGJ%2FgPodGpvLp4RsvFxTO7f5O5Gx%2Fm%2Fhm0HoKhAFnd2uUsMrwISxqwnY47zlhgRFQZxUgvnbfVH9XLjpjDgPQakie9scU4lLBc9wDR6w1a91EeJwcohKPkHU7GCAlcUFOs7xVMrpl9M8u%2B%2ByKnvGq0OwBMpeURVDWxG%2FObAO7sEdH6rhDmG7MCz1NaIlT%2FdMfcbg7qTQn5bLXDPUH%2FPdm9pV%2FRZiiGpgjKlRD1879Es3G4QXoGHn1cf%2Bn9VL%2Bj4Sm7tbQtiHW5Rb8x4e717jBBjhILN7KFawR7dJaF%2FtuSx9xfmPZXigJ8XDGAfseik7aTzrJUR0mk%2F8%2BhqBY7NhbmTRKX88MaGCSagAF3FWRqWDWCCpVWi8c07CeIYuYNPxfWE1w4t4zAkFMkENsZaRbIOKf9vNeXu9UW3ujIxL1tpO3ycChhtViNa4y1wSI%2Ba2AeSTDknMWrpQScX%2FFMYKwgJbpNGp6%2FS5a624Ivki2OD73RK1Bu8rsPctW5MtivnxFD1m3yaxsJVOeQ6fMqW9A5NtMJDD4NIGOqUB8TMJObdVl8pns9a9hwAM1LReAINGbneoWDS3SOIVk7hnKhw9A8lEPLc5MABxSp0lqmLH9MqpdaUiapEMtVGvdCW998IyXineEo8u54FFTOP2qA%2BITzlqC6I7O7T2yqNLMsWTHmsMidcL5KPtZggzoS80Ag%2BJ6HsV1THvDfSbZRSYNhMDy9abLQF3TqR8MM8nfG%2B2Epmicelqd2cHFp9BaYpcZbBg&X-Amz-Signature=117c6c638ede9d4d19580cfeec40db998b26912611ef9c3b428e75faa3dbc1a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UBDB3H3%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T020558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHr2p0f2L4RyV7VWcBklq2getWM6Bfmth67MTqJdHBd8AiEAiYRatgp6T9kOKMCO1lcaEBbDCya2iKcUCt4HanbItPoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDJJhRq8MhqR7pwZtoircA7F8P%2BKf1xbnjOfpUXHkSVCKS4rldBJLQwvSl69yP0yMJEXnhc5lAuO2uDW6qx%2BkxMrNkglcWJykNVGw7QbEPUZLFa9YaeEdZBT6wGJ%2FgPodGpvLp4RsvFxTO7f5O5Gx%2Fm%2Fhm0HoKhAFnd2uUsMrwISxqwnY47zlhgRFQZxUgvnbfVH9XLjpjDgPQakie9scU4lLBc9wDR6w1a91EeJwcohKPkHU7GCAlcUFOs7xVMrpl9M8u%2B%2ByKnvGq0OwBMpeURVDWxG%2FObAO7sEdH6rhDmG7MCz1NaIlT%2FdMfcbg7qTQn5bLXDPUH%2FPdm9pV%2FRZiiGpgjKlRD1879Es3G4QXoGHn1cf%2Bn9VL%2Bj4Sm7tbQtiHW5Rb8x4e717jBBjhILN7KFawR7dJaF%2FtuSx9xfmPZXigJ8XDGAfseik7aTzrJUR0mk%2F8%2BhqBY7NhbmTRKX88MaGCSagAF3FWRqWDWCCpVWi8c07CeIYuYNPxfWE1w4t4zAkFMkENsZaRbIOKf9vNeXu9UW3ujIxL1tpO3ycChhtViNa4y1wSI%2Ba2AeSTDknMWrpQScX%2FFMYKwgJbpNGp6%2FS5a624Ivki2OD73RK1Bu8rsPctW5MtivnxFD1m3yaxsJVOeQ6fMqW9A5NtMJDD4NIGOqUB8TMJObdVl8pns9a9hwAM1LReAINGbneoWDS3SOIVk7hnKhw9A8lEPLc5MABxSp0lqmLH9MqpdaUiapEMtVGvdCW998IyXineEo8u54FFTOP2qA%2BITzlqC6I7O7T2yqNLMsWTHmsMidcL5KPtZggzoS80Ag%2BJ6HsV1THvDfSbZRSYNhMDy9abLQF3TqR8MM8nfG%2B2Epmicelqd2cHFp9BaYpcZbBg&X-Amz-Signature=af31fbc948a02138cd0b70444b909ce6fb783758dabc86013b8d9af1d8861475&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







