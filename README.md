



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGZP5W3L%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T005726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCq7DXQiHBxxhdD29%2B9KF8sNfMvMPKJbf%2BtyP4K6a%2FH3AIhAO0twWKNgIxLqorod5stEDOZEUU2XJDQlmy609GlfFRcKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF4lmpfK0VNjRF8yMq3AO9ALKpGLCh9N3P6u99jxvKnVeSvSQDTooORB5UoM2xVK9DLEg%2FE3jZbC%2BIPYQfMzEAfjuQAYUNG%2FIG3x%2FNaqriwy0apN1EPv9fDg0eATVA37W9GyswQGkvYfPOyL1f0Vm0QrwFy238UrrB1AhB4hXBHXS2oPuR1HCB%2F76G2pQ7AXIQLZ025tFyNEjYo5X50lrC1qYTX0HmihYRjVKds%2FI8IA8VboJ1ruF4Hn0qMakXjxCPrYYaQeR2k3ws2LRMRdQ6xFaLFjQ%2FT1BRYAL7M83cgwNIi3I7qYy3WM30hLsXfzNZ0UbqtH68CubbpyC9%2F4e%2BULLPrwEAnQECI3%2F8%2FgYAt2RRqxnuFqioGOSHrBEpXG30xYN2SlnzwaD%2B2JuszoOH6Gq2Vl0vzaQryNy1myj2Qe3OkYKYNfEPWd4SV1fqhwFz1JXzWRDndh0tswkvjgQplpgl%2FeWjm1%2BptCSwDT2Mt0%2BVUjL7wleCmBmopOWwsTfY%2B9Dwxl0WbcBKBVeqnr3fc9pJCXOFFmplZcgRUGQO6HpN12hMnOaGT5WOau0gWnAgiSgJGm6iMIMMixJWt%2Byy8zg%2FZ60ngcrCkadM8KAgsG6QhHU7oXRfQ7cXIYkq71iz%2B5UJsVT3%2B4%2B%2FkDDRgq7UBjqkAWsnymIoiMpqGntX%2F5Zj2UiFbB3C5YgTu6b68bvoPpGi0jnDbl19vgFux%2F4nlqwSyFgDd28bJnEhA0N5LqTe7axOpnc3OIadiurGGajsozcDjxwy43%2BvQzYbW70%2F4H1NLOpfwGG9qin0xzcPrhiiWFEztoKQdaaQ9B4OTNh7dWe65ejD0xWZgdSo4%2BLlA8reWyAo4kEhzhmIt2AE5DbAil%2BsHPSN&X-Amz-Signature=17195eefb8e9e88430f672bd6c76e63d15f8ef88bd75154aac9f63ea20fb282f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGZP5W3L%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T005726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCq7DXQiHBxxhdD29%2B9KF8sNfMvMPKJbf%2BtyP4K6a%2FH3AIhAO0twWKNgIxLqorod5stEDOZEUU2XJDQlmy609GlfFRcKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF4lmpfK0VNjRF8yMq3AO9ALKpGLCh9N3P6u99jxvKnVeSvSQDTooORB5UoM2xVK9DLEg%2FE3jZbC%2BIPYQfMzEAfjuQAYUNG%2FIG3x%2FNaqriwy0apN1EPv9fDg0eATVA37W9GyswQGkvYfPOyL1f0Vm0QrwFy238UrrB1AhB4hXBHXS2oPuR1HCB%2F76G2pQ7AXIQLZ025tFyNEjYo5X50lrC1qYTX0HmihYRjVKds%2FI8IA8VboJ1ruF4Hn0qMakXjxCPrYYaQeR2k3ws2LRMRdQ6xFaLFjQ%2FT1BRYAL7M83cgwNIi3I7qYy3WM30hLsXfzNZ0UbqtH68CubbpyC9%2F4e%2BULLPrwEAnQECI3%2F8%2FgYAt2RRqxnuFqioGOSHrBEpXG30xYN2SlnzwaD%2B2JuszoOH6Gq2Vl0vzaQryNy1myj2Qe3OkYKYNfEPWd4SV1fqhwFz1JXzWRDndh0tswkvjgQplpgl%2FeWjm1%2BptCSwDT2Mt0%2BVUjL7wleCmBmopOWwsTfY%2B9Dwxl0WbcBKBVeqnr3fc9pJCXOFFmplZcgRUGQO6HpN12hMnOaGT5WOau0gWnAgiSgJGm6iMIMMixJWt%2Byy8zg%2FZ60ngcrCkadM8KAgsG6QhHU7oXRfQ7cXIYkq71iz%2B5UJsVT3%2B4%2B%2FkDDRgq7UBjqkAWsnymIoiMpqGntX%2F5Zj2UiFbB3C5YgTu6b68bvoPpGi0jnDbl19vgFux%2F4nlqwSyFgDd28bJnEhA0N5LqTe7axOpnc3OIadiurGGajsozcDjxwy43%2BvQzYbW70%2F4H1NLOpfwGG9qin0xzcPrhiiWFEztoKQdaaQ9B4OTNh7dWe65ejD0xWZgdSo4%2BLlA8reWyAo4kEhzhmIt2AE5DbAil%2BsHPSN&X-Amz-Signature=ff4138928d96f3231783af286321821de50d3e93cd75d9d2d5f56e67026898b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







