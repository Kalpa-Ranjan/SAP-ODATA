



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GXFUDG4%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T020559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfD1m%2BDInVyt0UjKzqBzZmcJCyV5myvq56%2BlBRAY%2BZZgIhALXCDfEaikWEk%2BwRpEcr%2FX3idUWEoAl2EQoaUuqDB%2BiDKv8DCEsQABoMNjM3NDIzMTgzODA1IgwkIDV2iFjyIotQMbIq3APo5s4ZBDBQ84WwnfsffuvoHVZYMO9%2FlAAW3PqHf%2FvvMeBX96XO1rGnp3QYopAAhDwHVtRiaJsnLM6Mep11Z%2F%2B%2BvFQ%2F9oNmRlsKGaFReXfWFbOCHujf1hbP5eSdyd4N7JrI61na8%2Fsh4QOupXoKniTZ5awOBuzo4T3TMow%2BDofhqRzVHtPKUypo1%2Fwm3T4GkSJjmcY4tdrl8hTrt7YekK%2BSGrdEDm2KqcHe7d6waGvqrNECjCHzRbjSEmFP%2B3E3z9A2gCnVtkJZ7KlR1O%2BkZq6KnZFEc9hPGP1tdeH4TpMt0hEMycq%2BOXFgVvPLfaleWSZLIiAa5kYI2R8vtavuMit3VjVtXcrBkUMua5hR6ZDli5dwKICHYh2pwxVfAokOzIXhd4LvnPBaMEAZCzWC3wHad%2FXddLRemf%2FQqh5VgJTOy2xwXrY8x55aWBDF%2BsyQKHHfcjKHjghv52QfdSSan7f%2BlwH5CUQ44hJs1yIZGyAtegzfuXG4UIKO99QLx4FLYpKIz1IPRWQiK03zfo%2F5J6uR0lUl9ek0JGvWH1gvs7sc4bcxpn8JAwwMfvM5RC9ak9ErHY2Hkdpq36tEq65KWTZnB5LtGBskQLejfXcVCaM%2F7cErf4zXiZ7My%2BhKxDDZ7LHOBjqkAclqpSuhZUwXdEcnD3%2FQ6pvQHZ%2BEfl2T2jwTb%2F5M720HJil69QViolcCVZmyX4oLFYbXePmIhFUXeSq0GDCeWgFeAvRJPwlo5%2Fw%2BfSEpdS%2FMx1nNZGKo2DQvcT6jJqxKMNEHmos6JsEFjfZLcO2khDN4UBj4q6U9WMY7%2FSWaNqcWMgGyr2lI%2FLp6ufESDl%2F%2B3ZOCzgFb4H%2BhuO8eR%2FYvLjXqT90E&X-Amz-Signature=8ea0e15fb0f1f13714b4bf4a1f7bb8c8b0699b3cf4f2ad8dcaa635735984b274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GXFUDG4%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T020559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfD1m%2BDInVyt0UjKzqBzZmcJCyV5myvq56%2BlBRAY%2BZZgIhALXCDfEaikWEk%2BwRpEcr%2FX3idUWEoAl2EQoaUuqDB%2BiDKv8DCEsQABoMNjM3NDIzMTgzODA1IgwkIDV2iFjyIotQMbIq3APo5s4ZBDBQ84WwnfsffuvoHVZYMO9%2FlAAW3PqHf%2FvvMeBX96XO1rGnp3QYopAAhDwHVtRiaJsnLM6Mep11Z%2F%2B%2BvFQ%2F9oNmRlsKGaFReXfWFbOCHujf1hbP5eSdyd4N7JrI61na8%2Fsh4QOupXoKniTZ5awOBuzo4T3TMow%2BDofhqRzVHtPKUypo1%2Fwm3T4GkSJjmcY4tdrl8hTrt7YekK%2BSGrdEDm2KqcHe7d6waGvqrNECjCHzRbjSEmFP%2B3E3z9A2gCnVtkJZ7KlR1O%2BkZq6KnZFEc9hPGP1tdeH4TpMt0hEMycq%2BOXFgVvPLfaleWSZLIiAa5kYI2R8vtavuMit3VjVtXcrBkUMua5hR6ZDli5dwKICHYh2pwxVfAokOzIXhd4LvnPBaMEAZCzWC3wHad%2FXddLRemf%2FQqh5VgJTOy2xwXrY8x55aWBDF%2BsyQKHHfcjKHjghv52QfdSSan7f%2BlwH5CUQ44hJs1yIZGyAtegzfuXG4UIKO99QLx4FLYpKIz1IPRWQiK03zfo%2F5J6uR0lUl9ek0JGvWH1gvs7sc4bcxpn8JAwwMfvM5RC9ak9ErHY2Hkdpq36tEq65KWTZnB5LtGBskQLejfXcVCaM%2F7cErf4zXiZ7My%2BhKxDDZ7LHOBjqkAclqpSuhZUwXdEcnD3%2FQ6pvQHZ%2BEfl2T2jwTb%2F5M720HJil69QViolcCVZmyX4oLFYbXePmIhFUXeSq0GDCeWgFeAvRJPwlo5%2Fw%2BfSEpdS%2FMx1nNZGKo2DQvcT6jJqxKMNEHmos6JsEFjfZLcO2khDN4UBj4q6U9WMY7%2FSWaNqcWMgGyr2lI%2FLp6ufESDl%2F%2B3ZOCzgFb4H%2BhuO8eR%2FYvLjXqT90E&X-Amz-Signature=80af4f933d7d405058504e55e416e869d2ec2b389b10a5566d4174db7610af85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







