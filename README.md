



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPEARFPP%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T125305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEEtSYuBFpo%2FtInj2Us%2FrGSoO4m8dUCdB9S%2FB8rftavKAiBVoMjX4QvR9z7ZYHzx6nZMJus9yF2QenMOFfqkjo%2Fnryr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMZmVZpzaMPYbvO%2F%2BsKtwDUFyD7Gwuf3iJZfPxdE4pTR1lHXeT8uR9koUd6XMHMiHdbESZXKLw9un81RaH49dQlkWMQdCdeou9Xf%2F7iqn4TWkLuuuz0bam%2FySLEFpW4PG9yFmHNGrYL8sQdhvXGoT4Sf9%2BnTev2ynm6tLNJ76SoyvcZ8FLAuFF7pi0RMC6ywmzmXJQkynfolGXVN55dwPrjSBvpu0%2FalAOlzT%2FybSrJLAz06DdpA5e3qyVquVN9lbIaFQe5Gr2Dncq4qjGwUUHLw%2B9OqsSrl32XmI0R7igY9kBx6guHIVQrZK52STAftmGgiSGjRBWwJmx7XgRGhVjkpTQ2xH1f1JQ2cvGowS%2B7BYrjdZUMKM80o4%2BvLCaC1nEizhUI0PjhXYci4%2FsX7BhRY3SNmuZpbaQZkE3HlVhA8ldOAgyA%2BCSZZAMBgnjWVsFz8GYAOqzu3ptRD90DPhplX2TbqpO27jWZC7c%2FTS7aNrnN3zT2CrwzyMX%2BGRpry5u3O4%2FeWFI85vBnvkEGCfIRIE9WeO8gV9VOdz9cW5lGsz65s7qnHDkSIagT46Qf%2FaF4oI7lM9NGomarBZpcTTiVr87GXYM8TSjGQVIIqo3b0ZdsvI9PivMqQjpHxQ4GL6ClgcW0LZopo16808w%2B4HMzAY6pgH58eoGM%2B8ucfCUuC4AR%2BeRGf3RBlc2wJpsjLrTJCA4GFpc9cv0U%2FWn11fasJhJP8%2Fr%2BAACNMt2Jhx6WtM9GOp4lhFeTwjRydJgvhF%2Fhsm5YZU5rlPRev%2FC1RC617d6AyZztvTHD3AICQ0Hj6rBYX0W3Kjt21zlCGNGBHxhxVFG43Ox9X%2BoNNlIMhbZT3WItHqpye9jYLJ%2BwkwSnl5Y6VowBdcTj5aC&X-Amz-Signature=8f0800e518f08fef9700d8d30d3ff1b022d6be39c64ba8bea88e0b0a68afc433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPEARFPP%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T125305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEEtSYuBFpo%2FtInj2Us%2FrGSoO4m8dUCdB9S%2FB8rftavKAiBVoMjX4QvR9z7ZYHzx6nZMJus9yF2QenMOFfqkjo%2Fnryr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMZmVZpzaMPYbvO%2F%2BsKtwDUFyD7Gwuf3iJZfPxdE4pTR1lHXeT8uR9koUd6XMHMiHdbESZXKLw9un81RaH49dQlkWMQdCdeou9Xf%2F7iqn4TWkLuuuz0bam%2FySLEFpW4PG9yFmHNGrYL8sQdhvXGoT4Sf9%2BnTev2ynm6tLNJ76SoyvcZ8FLAuFF7pi0RMC6ywmzmXJQkynfolGXVN55dwPrjSBvpu0%2FalAOlzT%2FybSrJLAz06DdpA5e3qyVquVN9lbIaFQe5Gr2Dncq4qjGwUUHLw%2B9OqsSrl32XmI0R7igY9kBx6guHIVQrZK52STAftmGgiSGjRBWwJmx7XgRGhVjkpTQ2xH1f1JQ2cvGowS%2B7BYrjdZUMKM80o4%2BvLCaC1nEizhUI0PjhXYci4%2FsX7BhRY3SNmuZpbaQZkE3HlVhA8ldOAgyA%2BCSZZAMBgnjWVsFz8GYAOqzu3ptRD90DPhplX2TbqpO27jWZC7c%2FTS7aNrnN3zT2CrwzyMX%2BGRpry5u3O4%2FeWFI85vBnvkEGCfIRIE9WeO8gV9VOdz9cW5lGsz65s7qnHDkSIagT46Qf%2FaF4oI7lM9NGomarBZpcTTiVr87GXYM8TSjGQVIIqo3b0ZdsvI9PivMqQjpHxQ4GL6ClgcW0LZopo16808w%2B4HMzAY6pgH58eoGM%2B8ucfCUuC4AR%2BeRGf3RBlc2wJpsjLrTJCA4GFpc9cv0U%2FWn11fasJhJP8%2Fr%2BAACNMt2Jhx6WtM9GOp4lhFeTwjRydJgvhF%2Fhsm5YZU5rlPRev%2FC1RC617d6AyZztvTHD3AICQ0Hj6rBYX0W3Kjt21zlCGNGBHxhxVFG43Ox9X%2BoNNlIMhbZT3WItHqpye9jYLJ%2BwkwSnl5Y6VowBdcTj5aC&X-Amz-Signature=225773703a175a497735234e653cfad5dfbc70273d407b37ea06d81c84353130&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







