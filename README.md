



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH25MOI2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T125916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJIMEYCIQDVloCC%2BPTAmIGLbovukauwQVdwm1JgXt5%2F1blNAPzMLgIhAN8967fTsPslh2%2ByQ3dF1bWZ6fteMBrBxMVH9cWs9gB%2FKv8DCC4QABoMNjM3NDIzMTgzODA1Igw1c85DRFiTsh6buvoq3APC2NnVN8nB0aajEZOHmiwwrOzi7lFNBwjMlThFAiZf9NekD2S1PMLzzrce9yyP36rS3EybRX0pEaPdR5jRumPl4StphCFzKB5%2Bkg6VeD%2BsoE7EslQHKudjGnW8NkRlTgTwyDjQQ3lJgJLYSo7XlbDfdSq%2FKho5W%2BOZg6b5b5M%2BQn84xDwAf%2BkCQCbPaSi%2F7wE0R410vkVOt8LQDWXmvgiaYZrQy2z1aayo0quBhh%2BDLfqDum6CwLBkF6ieG6cjTjZ0lEvWWnXTN%2FHFUpFR%2BT5AcuqsRvvSH%2FocI%2FOEwhc9X%2FKpSBmBPH%2Bo6BSnPZW7Q3W6Zbya3Z8AE6PvXu6PvAfYAAkgD4nio4Fcb8mTX4ZJdjhkhP2uVHvHyPG0PxL2u9K8Ja4jYv4Q0J9%2BssSZpltYJfY%2BLvk31qOgLzn0gSUXRHgdr5rxj2%2FNpEnDafsfCIsmmSi3Nj6OPvdcrbfm49LorizZMTh5G5LZ3c5LKEbvLveqO6XeaWU3x6D44Jtmg8jFbbBRGy8sxlGUzyKRkFho3TX8ORCbWODNJKPpVeFtBee4gH5qm8DeyrBAdzi5gMl0BnevG8WWsZyOgc7NCfQevIDLbznsfGEF%2F0koUK5GGDwechY%2BScHwWEJ0zzDz2uPOBjqkAZfXLVOkXKo1qTbbXaTUfOgyWZ211luCITNjutUJZZLCrquSulI5JJOhLUYrqxKthFXdrLn1xb9BEoKLbktixRbaYqrG9TkAR16E%2B%2BU3lYFzqQNyQ0lV4diLF92Tc5hH1%2FUPS6KuAbPlzG3C34oKwQvQKZ8Fn1oakA%2BYV8cVqzHQ900W5L0G6QW8bJhChpeVRaekgjY7%2FBg9ZLCg%2F3%2F8occrjioE&X-Amz-Signature=080efc9c3d249510b0b6d038474e5ce6da356cf02af8791a25090afae1086ae4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH25MOI2%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T125916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJIMEYCIQDVloCC%2BPTAmIGLbovukauwQVdwm1JgXt5%2F1blNAPzMLgIhAN8967fTsPslh2%2ByQ3dF1bWZ6fteMBrBxMVH9cWs9gB%2FKv8DCC4QABoMNjM3NDIzMTgzODA1Igw1c85DRFiTsh6buvoq3APC2NnVN8nB0aajEZOHmiwwrOzi7lFNBwjMlThFAiZf9NekD2S1PMLzzrce9yyP36rS3EybRX0pEaPdR5jRumPl4StphCFzKB5%2Bkg6VeD%2BsoE7EslQHKudjGnW8NkRlTgTwyDjQQ3lJgJLYSo7XlbDfdSq%2FKho5W%2BOZg6b5b5M%2BQn84xDwAf%2BkCQCbPaSi%2F7wE0R410vkVOt8LQDWXmvgiaYZrQy2z1aayo0quBhh%2BDLfqDum6CwLBkF6ieG6cjTjZ0lEvWWnXTN%2FHFUpFR%2BT5AcuqsRvvSH%2FocI%2FOEwhc9X%2FKpSBmBPH%2Bo6BSnPZW7Q3W6Zbya3Z8AE6PvXu6PvAfYAAkgD4nio4Fcb8mTX4ZJdjhkhP2uVHvHyPG0PxL2u9K8Ja4jYv4Q0J9%2BssSZpltYJfY%2BLvk31qOgLzn0gSUXRHgdr5rxj2%2FNpEnDafsfCIsmmSi3Nj6OPvdcrbfm49LorizZMTh5G5LZ3c5LKEbvLveqO6XeaWU3x6D44Jtmg8jFbbBRGy8sxlGUzyKRkFho3TX8ORCbWODNJKPpVeFtBee4gH5qm8DeyrBAdzi5gMl0BnevG8WWsZyOgc7NCfQevIDLbznsfGEF%2F0koUK5GGDwechY%2BScHwWEJ0zzDz2uPOBjqkAZfXLVOkXKo1qTbbXaTUfOgyWZ211luCITNjutUJZZLCrquSulI5JJOhLUYrqxKthFXdrLn1xb9BEoKLbktixRbaYqrG9TkAR16E%2B%2BU3lYFzqQNyQ0lV4diLF92Tc5hH1%2FUPS6KuAbPlzG3C34oKwQvQKZ8Fn1oakA%2BYV8cVqzHQ900W5L0G6QW8bJhChpeVRaekgjY7%2FBg9ZLCg%2F3%2F8occrjioE&X-Amz-Signature=8e55b8fd4ff5ac1906eb3db6c3995825eb1cec0e9d326a8d2592a812c5970cb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







