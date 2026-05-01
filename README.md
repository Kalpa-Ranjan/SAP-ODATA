



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q6RWDB4%2F20260501%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260501T130925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDCxFJvMO7FeNW%2BvRT%2BMaUxcjsOB2yXt8LoKyfznisKBQIhAP9yWjNuD2vvs9A2jHx29O3BjY3sozQqk2uJsLqHeKF6Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxmdQOgVjuRQIUnJpcq3APG5hgguX2JGGWp3x358fHOpuSjLd5xJqTN0UVOWyt4b7ZCIXNtc4jeTd0jtKyHArkP32zO8f35Kdkuq0gKPkNtGC1UQYn6Tf3BdD9cMV2aqyIRCn7Fv5n0LlVpB2snFIv3TqrnoNXGDoIeWudfbuaQLlVZ9%2Ftuc%2B3QR8eK4LEA8i0ruY53DNB3ZYauyRdfQgxV91gDAl%2BCWBEsNpdvRjHY0nZHg5AOjm7%2FU1PcXVKYxRUdcSlLWlyMOFHgW7ebYS5Q7nZ7%2BA9Mlwx8KthqEkv9dlEkRcLMp5WZM9xBdsJPUGmHCyLCUnivfmeaoGlcGueCL2ipbyg4ZKjJuQRjsLnPjWPVYpTYBxSYsbOHSXfZrrRx9PiG6N9ovdpwW%2Brh5wu2XFpN76ia9h7C4a6b8J6JapJqiM6FTH4pnR6RSyz8OgodOFzPTOhVlIxWhgHM3S1Lk7yUKnXoJ5GAsNEP4Z6PKvkONKvhTgV3c%2FJpSH%2BZbwCyp19igMrHiDU8iOs1NkDy1UZbD4AoCz0JxM2lCBrkrbc9V5nRwi6o1h8jIkmoDpdl1FDIuEq6yuezuwq5LY2W4pCDGD0alE6c9ZmZV6eUHXhNqttLhO5RdBMZWKY04YOaTBXGQLgm%2FDRkxjDEv9LPBjqkAZre1zpWiqwI%2F0UAagxoAFfr25Jx7reaJENFXiLZX3Ghs1BkrGG%2BAw%2B4oWbqB0HFRq1Twf6oYPDhK6hKJ3ek9FMSJi%2BufHxKNbpLcrnwNXHnoYTIfC3%2BxCQP1gjcurQFuL9Xfzc%2B7UNgJXPSWEn5OvHrgmU8Q95nxvYOUYXpebRMlejV7FRmK3Brgj1FzIqb4pOin4G%2ByPuGygeKaABMm%2BbPY4Ym&X-Amz-Signature=4bee777d62a09648cdd68311d7211acec60649565cab6a9be736917ac86368bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q6RWDB4%2F20260501%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260501T130925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDCxFJvMO7FeNW%2BvRT%2BMaUxcjsOB2yXt8LoKyfznisKBQIhAP9yWjNuD2vvs9A2jHx29O3BjY3sozQqk2uJsLqHeKF6Kv8DCCYQABoMNjM3NDIzMTgzODA1IgxmdQOgVjuRQIUnJpcq3APG5hgguX2JGGWp3x358fHOpuSjLd5xJqTN0UVOWyt4b7ZCIXNtc4jeTd0jtKyHArkP32zO8f35Kdkuq0gKPkNtGC1UQYn6Tf3BdD9cMV2aqyIRCn7Fv5n0LlVpB2snFIv3TqrnoNXGDoIeWudfbuaQLlVZ9%2Ftuc%2B3QR8eK4LEA8i0ruY53DNB3ZYauyRdfQgxV91gDAl%2BCWBEsNpdvRjHY0nZHg5AOjm7%2FU1PcXVKYxRUdcSlLWlyMOFHgW7ebYS5Q7nZ7%2BA9Mlwx8KthqEkv9dlEkRcLMp5WZM9xBdsJPUGmHCyLCUnivfmeaoGlcGueCL2ipbyg4ZKjJuQRjsLnPjWPVYpTYBxSYsbOHSXfZrrRx9PiG6N9ovdpwW%2Brh5wu2XFpN76ia9h7C4a6b8J6JapJqiM6FTH4pnR6RSyz8OgodOFzPTOhVlIxWhgHM3S1Lk7yUKnXoJ5GAsNEP4Z6PKvkONKvhTgV3c%2FJpSH%2BZbwCyp19igMrHiDU8iOs1NkDy1UZbD4AoCz0JxM2lCBrkrbc9V5nRwi6o1h8jIkmoDpdl1FDIuEq6yuezuwq5LY2W4pCDGD0alE6c9ZmZV6eUHXhNqttLhO5RdBMZWKY04YOaTBXGQLgm%2FDRkxjDEv9LPBjqkAZre1zpWiqwI%2F0UAagxoAFfr25Jx7reaJENFXiLZX3Ghs1BkrGG%2BAw%2B4oWbqB0HFRq1Twf6oYPDhK6hKJ3ek9FMSJi%2BufHxKNbpLcrnwNXHnoYTIfC3%2BxCQP1gjcurQFuL9Xfzc%2B7UNgJXPSWEn5OvHrgmU8Q95nxvYOUYXpebRMlejV7FRmK3Brgj1FzIqb4pOin4G%2ByPuGygeKaABMm%2BbPY4Ym&X-Amz-Signature=e5ae5cb1c600ab72de392c7c53707901118c2655b60a79aa30d93624ae51eed5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







