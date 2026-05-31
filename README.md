



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657YYGVPI%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T190811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIDqVW6x2xX4h4JrfOyMxEo6ac1Tyi2%2BK%2Bps86RM9KgwZAiASZVGdp0bPTwQw4I9rvOWvOvUBTLwn9bPtKGcKijFpuyqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnhrCW4q7IquE0fj1KtwDh%2BuTGgIetp%2BJV18muqGj4Gm72PbKyjLVqqRQ0qSm4GRn8EM2ifwbLucqGe3ZnBwifzyDnE5t48qfJYChF6P9ck8cpArb%2FGB0zvVSeyTMlPOQn0sdKCqRxFa0zw9pM%2BL0UGh%2BmUi1cHu90JypkGyiw508GKeYtewAxCJp0A4EquWnwd9qFGf41cylXvgr1CmEnib%2BZpg9jniRjNuO3qGuOR5DEXakVSbaihaniv6o4thy6VIVPvbnHnhDlBJA%2BEbB1DmkXP3or7k1%2FL1GXhwKFGVr73bIeRqDJ%2FxAyaXmnAyXiQFe6cIMdtVU8Se9FvRMHlonMcubo8EFZkyJ8HY6utjqMcyJM8%2BJrZZGvP6Uh9aoAfxOcacCHOyOYa6xJG%2Fk4fpAGgxXEK50DBqe7Nd731agrdXg81FY2%2FxMHgA5vcVyU%2BJW01pxh8OfJjqgKxwOOZLZQWP4Ya0RTAX5t7gYAyR4ofvXk0ZvgyVgmQ5ji856ETOe7r0lxUX5eq1hOn6JNUkT5PO%2Bk%2FcWEMRGE94JMBCBkHi4wBYeiRAJ34cjSv9GYPPl3AID8whVFqHBX4QSMWwMviRNCfKb8X110L0h0YDaUcoaFKMltuz83X%2BKoERHbn4f7fx3kuTuggAwp9Hx0AY6pgEv33KYoQsogzgm7dzgTaRcbl6nziGQN0jzp1hxk6ggufARPCXQxx8eT%2BLsd%2F0Oc%2F9toPjnyX8uLJONk1iNqHf6MJBmgCQHJ%2BqzkSrp1yjgjwbAaU6GG%2FYikIg35OVDVIWBGOwh5r91Rm6YtN6oDM5gtuQInd%2F8Vk7Hs4KHzmgcM8cjgD%2BzUUSAhjXX8SnBBUr5N2ScZXMr6uOPu0QGEc4c%2F0PrOgPo&X-Amz-Signature=efecc72efb91b88f7b601b8e7d154c57e5603d609037d0c348dacc3d26d5a35e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657YYGVPI%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T190811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIDqVW6x2xX4h4JrfOyMxEo6ac1Tyi2%2BK%2Bps86RM9KgwZAiASZVGdp0bPTwQw4I9rvOWvOvUBTLwn9bPtKGcKijFpuyqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnhrCW4q7IquE0fj1KtwDh%2BuTGgIetp%2BJV18muqGj4Gm72PbKyjLVqqRQ0qSm4GRn8EM2ifwbLucqGe3ZnBwifzyDnE5t48qfJYChF6P9ck8cpArb%2FGB0zvVSeyTMlPOQn0sdKCqRxFa0zw9pM%2BL0UGh%2BmUi1cHu90JypkGyiw508GKeYtewAxCJp0A4EquWnwd9qFGf41cylXvgr1CmEnib%2BZpg9jniRjNuO3qGuOR5DEXakVSbaihaniv6o4thy6VIVPvbnHnhDlBJA%2BEbB1DmkXP3or7k1%2FL1GXhwKFGVr73bIeRqDJ%2FxAyaXmnAyXiQFe6cIMdtVU8Se9FvRMHlonMcubo8EFZkyJ8HY6utjqMcyJM8%2BJrZZGvP6Uh9aoAfxOcacCHOyOYa6xJG%2Fk4fpAGgxXEK50DBqe7Nd731agrdXg81FY2%2FxMHgA5vcVyU%2BJW01pxh8OfJjqgKxwOOZLZQWP4Ya0RTAX5t7gYAyR4ofvXk0ZvgyVgmQ5ji856ETOe7r0lxUX5eq1hOn6JNUkT5PO%2Bk%2FcWEMRGE94JMBCBkHi4wBYeiRAJ34cjSv9GYPPl3AID8whVFqHBX4QSMWwMviRNCfKb8X110L0h0YDaUcoaFKMltuz83X%2BKoERHbn4f7fx3kuTuggAwp9Hx0AY6pgEv33KYoQsogzgm7dzgTaRcbl6nziGQN0jzp1hxk6ggufARPCXQxx8eT%2BLsd%2F0Oc%2F9toPjnyX8uLJONk1iNqHf6MJBmgCQHJ%2BqzkSrp1yjgjwbAaU6GG%2FYikIg35OVDVIWBGOwh5r91Rm6YtN6oDM5gtuQInd%2F8Vk7Hs4KHzmgcM8cjgD%2BzUUSAhjXX8SnBBUr5N2ScZXMr6uOPu0QGEc4c%2F0PrOgPo&X-Amz-Signature=b4380807f536b4e1162bbfb27af46404278356bec3bf9e9c1ef694e5ebdf7b17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







