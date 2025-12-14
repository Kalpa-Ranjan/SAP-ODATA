



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636RM6YW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T062333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCxjBmi0T%2FSg%2BJqnbGPMyjmSLzaYDS3WKb7%2Bd84ei7quAIgAa17LBw6yFjVTWM0peI0Ar8sajNUt4anAcG%2F381NUn0q%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDK79F4BKyuQBx8ZKHSrcA3Yob23vDdZbhBxyi%2BP6QlU4oNMPFH%2FNFmIuDL8EaQospxZENqEFNfefEZ8ECK9pUttiXeClPA7KeCjTC%2FA531tV5K9sLwV98gh%2FcPAPAtq2j4zmtVoOnasCAlyLUJZr5rJgaS%2Fn3xNa%2F2BJCz9he0K4g2ldrXEuxKHdXite4nPoEFgVgsZgZBnGLk2bq%2FzL4QzyTTw6jW8LnHSiOCHlSwyg7qFek2x6WApGLV5fCVjk4UZJnl2eO%2FWKIb17woJcnPdOMdz3TthfHWGIGHFgQp4JF9NwIrDk%2BJtIHg3TQn49bjvtJ2gl5J%2FO%2Bhgw4PeTOqzhLmjQiLdov5rck9r26BmXXwuMF0VvX%2F2jLnVxGnKHkPZxCja4ckGNun5yaoNVQzxNIYkG2YS2Zw5RiIrAGpu37BGdt0yMn0gpMNKDdtG%2FCrAMRoGsQ%2FQpZAKz34CEiTcg8LgvLbssjo1YlupLwFf%2BxaiQ%2F2JY0riTivo8Yo552ECx%2FkPJvW0gFx11%2FZ0wO8Eurkkwz3QISihra44ImGNQfGGjgh6edrztW21sKBeqHOGVuSOUjbKFKLySSd%2Bhm1a3sfT8BY3wlxhNfDpEQOniKFiV2JgCsYZ7nSKxRM2o9U3EMjmSqd4LWkjxMKum%2BckGOqUBe3%2F7oDAEbaYg2hOEOShjeUiutfl48I7sTPE8q0Z8Db4QtWbUd61jsne3fKdorWBeU%2B%2FaQSEIvM2UOXeZ28TTG3xncunr3G%2BKBwoxnazhmwlHv4duBcYYGFtVkxMVIksW1DJ%2BlTsml7OVKu2%2BPhC4qWFiKhUfOeaw58ehtmU0Ksj9WquGtFHOVc1DB1oz4FkgMPWZ2jh8gmrMaNaCMIHA1DkEQXSq&X-Amz-Signature=4a5da469e2b9da610e580082f58d25e610929d8fb760a42660f1ffefe06e0078&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636RM6YW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T062333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQCxjBmi0T%2FSg%2BJqnbGPMyjmSLzaYDS3WKb7%2Bd84ei7quAIgAa17LBw6yFjVTWM0peI0Ar8sajNUt4anAcG%2F381NUn0q%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDK79F4BKyuQBx8ZKHSrcA3Yob23vDdZbhBxyi%2BP6QlU4oNMPFH%2FNFmIuDL8EaQospxZENqEFNfefEZ8ECK9pUttiXeClPA7KeCjTC%2FA531tV5K9sLwV98gh%2FcPAPAtq2j4zmtVoOnasCAlyLUJZr5rJgaS%2Fn3xNa%2F2BJCz9he0K4g2ldrXEuxKHdXite4nPoEFgVgsZgZBnGLk2bq%2FzL4QzyTTw6jW8LnHSiOCHlSwyg7qFek2x6WApGLV5fCVjk4UZJnl2eO%2FWKIb17woJcnPdOMdz3TthfHWGIGHFgQp4JF9NwIrDk%2BJtIHg3TQn49bjvtJ2gl5J%2FO%2Bhgw4PeTOqzhLmjQiLdov5rck9r26BmXXwuMF0VvX%2F2jLnVxGnKHkPZxCja4ckGNun5yaoNVQzxNIYkG2YS2Zw5RiIrAGpu37BGdt0yMn0gpMNKDdtG%2FCrAMRoGsQ%2FQpZAKz34CEiTcg8LgvLbssjo1YlupLwFf%2BxaiQ%2F2JY0riTivo8Yo552ECx%2FkPJvW0gFx11%2FZ0wO8Eurkkwz3QISihra44ImGNQfGGjgh6edrztW21sKBeqHOGVuSOUjbKFKLySSd%2Bhm1a3sfT8BY3wlxhNfDpEQOniKFiV2JgCsYZ7nSKxRM2o9U3EMjmSqd4LWkjxMKum%2BckGOqUBe3%2F7oDAEbaYg2hOEOShjeUiutfl48I7sTPE8q0Z8Db4QtWbUd61jsne3fKdorWBeU%2B%2FaQSEIvM2UOXeZ28TTG3xncunr3G%2BKBwoxnazhmwlHv4duBcYYGFtVkxMVIksW1DJ%2BlTsml7OVKu2%2BPhC4qWFiKhUfOeaw58ehtmU0Ksj9WquGtFHOVc1DB1oz4FkgMPWZ2jh8gmrMaNaCMIHA1DkEQXSq&X-Amz-Signature=31a69e6fdc1c1fc53055bc50ac8ce9042d5db086dcb99e0de01e5e7807cf5186&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







