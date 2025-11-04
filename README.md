



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQUE62H%2F20251104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251104T011149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEs7fPJEKMWwoXFwZvrLnN715MXBgDX24A69NEgIo%2FvwIhAIxmxASMb5%2BRG2frZ%2BNXOT2yko3rFNbRdZbJt45o2JsWKv8DCGoQABoMNjM3NDIzMTgzODA1IgzyQTcN4KftmqOg%2Bl4q3AP8bVtK4sSy6H5c%2F7UNO%2Fa753QKPizjQ0kotJz8jbHruByHqylbBZQbHuw%2F0EietqSFakx4PXvDydssl8LVY9EL1cT9EcPnMMpmI0lsqya0eabLeqbLTc3LdThdD0CuW6ytEU2rUrmCHsdDnpsDkrRZulAZopJg8S5QLQHzbtsujLjAI93RzKqr0vpCV70N0AILoOS4rReC9WTYrzJKrV7CVYSiN%2FVtaVTyVQxv7qFPpH6zwVwxy1n8NbRsK4JzOy5E3ThHNSty5nmkb4%2FWGCgVxCtHNu%2FtQmjpY1yvmd7WO03ANI%2FqH4j4IEy1hzJ6GytmWQFvtb7Usw3gNkXu1Z26OrUY0oZcBjEJVtOLWSGA7arBN7nyyfsi5v6bAG6Ysuii9E5V0Ngql4vSsUBTCn65hQfryyCSRbHq4%2BCHhlbFI9KLSwK1YOwPPHe933XMPDpVnP9WlNL7X036cfVm83uMbc4LaA7iz%2Bgx8ZNIXJ3iyk%2BPQ%2BgGr9UwjNRv2UdZuZBUsyiLmCvRcm60PZaTd6PygthbqhuloqG%2FCfyiikD3JI1bnNn3bvHqok4SXgTX3IO27%2BOopuqY7WidRzNBgQ30ireyCG1xWhNpTq7KBPvvzbj6QPbA2Cnm2zagQDCckqXIBjqkAZltjfNQQxslEWke3IRPbwvwOjZ3v%2Fqo1cSYoGqtqg74oXje1SuDlZYpEy3DP8nzFPv87E2yGqTbL%2BAqmmOCBIbmpTyupIi2BRcyHP5uB4QUdOUHufhFPqidRCwQijoWtF5nA%2BIv5d7oZKytECyR4vV8ALaoDbbeWbFpw47BFymBhuZCzrpoZsMyhyYC3B5fcT3Y0%2FqE3Z4HOeUbAb4%2F02OXf2f%2B&X-Amz-Signature=e521f58807297577b221ec6c3e8dcd4bcaaf95ddd70a45fb5d6ab99235ba8811&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQUE62H%2F20251104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251104T011149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEs7fPJEKMWwoXFwZvrLnN715MXBgDX24A69NEgIo%2FvwIhAIxmxASMb5%2BRG2frZ%2BNXOT2yko3rFNbRdZbJt45o2JsWKv8DCGoQABoMNjM3NDIzMTgzODA1IgzyQTcN4KftmqOg%2Bl4q3AP8bVtK4sSy6H5c%2F7UNO%2Fa753QKPizjQ0kotJz8jbHruByHqylbBZQbHuw%2F0EietqSFakx4PXvDydssl8LVY9EL1cT9EcPnMMpmI0lsqya0eabLeqbLTc3LdThdD0CuW6ytEU2rUrmCHsdDnpsDkrRZulAZopJg8S5QLQHzbtsujLjAI93RzKqr0vpCV70N0AILoOS4rReC9WTYrzJKrV7CVYSiN%2FVtaVTyVQxv7qFPpH6zwVwxy1n8NbRsK4JzOy5E3ThHNSty5nmkb4%2FWGCgVxCtHNu%2FtQmjpY1yvmd7WO03ANI%2FqH4j4IEy1hzJ6GytmWQFvtb7Usw3gNkXu1Z26OrUY0oZcBjEJVtOLWSGA7arBN7nyyfsi5v6bAG6Ysuii9E5V0Ngql4vSsUBTCn65hQfryyCSRbHq4%2BCHhlbFI9KLSwK1YOwPPHe933XMPDpVnP9WlNL7X036cfVm83uMbc4LaA7iz%2Bgx8ZNIXJ3iyk%2BPQ%2BgGr9UwjNRv2UdZuZBUsyiLmCvRcm60PZaTd6PygthbqhuloqG%2FCfyiikD3JI1bnNn3bvHqok4SXgTX3IO27%2BOopuqY7WidRzNBgQ30ireyCG1xWhNpTq7KBPvvzbj6QPbA2Cnm2zagQDCckqXIBjqkAZltjfNQQxslEWke3IRPbwvwOjZ3v%2Fqo1cSYoGqtqg74oXje1SuDlZYpEy3DP8nzFPv87E2yGqTbL%2BAqmmOCBIbmpTyupIi2BRcyHP5uB4QUdOUHufhFPqidRCwQijoWtF5nA%2BIv5d7oZKytECyR4vV8ALaoDbbeWbFpw47BFymBhuZCzrpoZsMyhyYC3B5fcT3Y0%2FqE3Z4HOeUbAb4%2F02OXf2f%2B&X-Amz-Signature=1082dd3a91266a8637f3017da463e719b35a659d6ba9fa20404d168bd0e772ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







