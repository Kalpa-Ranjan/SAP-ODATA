



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU3J4SX4%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCNym%2By8zS6HRx2IO3FfafpPJC0RYXdeVrKy3laXfELbwIhAPNQZ2t6NQWecZvB81fpxMmHjpwVPVOwdmsm4JhbJEaJKv8DCDMQABoMNjM3NDIzMTgzODA1IgyXJjBi88UftfZs0oEq3ANBHD88TXqnRFGIxeW2Fw7xuyXc%2F%2BFwbv5xrpyw5y2Zh9F6wePM7czs6%2B51TvbSDrY%2BQQvstrHC7Y6gHdrBO%2F4nFMYNObWGZt7giUqSgD0yMyEC4V7eNhHXalxLEFcuJCE0y4QxkWsD0CjbWhbv4Djq2wXV3ij3iRehDu%2F0rJDs8WL3E99MCVWp4ZTe0JY%2BG%2B93EKJDVD5U4ZBf9t6nq7AuvMq35KUQnK%2Fg4yIOtHg2aCsfAqp1erCKwpzyqcXCeFQDosISvXKrqA8mHq%2BAOrpBahU%2BZri8yNmThmEHBk7m8L7UY1lWLwWl2lCeHmtZxPVnQ0lsoiQ2KZDS2eZsf%2FFOslILZIy1NdhATEgerPRO9Y592MxwH01%2BHzCAOOywyWG1SRLGuGEJBTyLyoW4WRR23UQvGG5wY7EDxN3dIn4NwuyNkVjwQS8403HziX2DAAFy7158QP%2BfEfApb7qeZm9arcLFh7SaPaTCi7OudQgyGu%2FSXmuyoVA%2FGi3H1YIquVRii4mDtsoxdQyR4a5VFJ%2Bje8omS7d%2BDVOywiaPZo6WpWgmAixJg8865fEAY1evK%2FdrUodYxYccfn0mhaXhZ8tWG9l1O07tomYXEYEVTIRBSrIOy7qSl5k0bB0szjDPm%2F7QBjqkAQW6T79XJ5O76XiGS0SzASoY%2F5Mh%2FC7B1ku4xTXWm0ibsKZLLlDknNzd8kI5tm6P3y6CQ%2BPhuomKXLlHjTrVa0gvu9ytszqsIY7Iq6JmlENyu8rjyBDi2coUIM9a8wjktD8gkVMYdPKHCvQu2ofg6VIKO2SZQ%2Byr2rFkIwGynyx3%2BbYDD1S37GVlLbxTfM43B8T0tvkdXRAJgIxy7MWCmPmw0jH5&X-Amz-Signature=9f61cc76dbc76022a49490d2e9c2cc2e803c1aeae942eb8926c1f28487744a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU3J4SX4%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCNym%2By8zS6HRx2IO3FfafpPJC0RYXdeVrKy3laXfELbwIhAPNQZ2t6NQWecZvB81fpxMmHjpwVPVOwdmsm4JhbJEaJKv8DCDMQABoMNjM3NDIzMTgzODA1IgyXJjBi88UftfZs0oEq3ANBHD88TXqnRFGIxeW2Fw7xuyXc%2F%2BFwbv5xrpyw5y2Zh9F6wePM7czs6%2B51TvbSDrY%2BQQvstrHC7Y6gHdrBO%2F4nFMYNObWGZt7giUqSgD0yMyEC4V7eNhHXalxLEFcuJCE0y4QxkWsD0CjbWhbv4Djq2wXV3ij3iRehDu%2F0rJDs8WL3E99MCVWp4ZTe0JY%2BG%2B93EKJDVD5U4ZBf9t6nq7AuvMq35KUQnK%2Fg4yIOtHg2aCsfAqp1erCKwpzyqcXCeFQDosISvXKrqA8mHq%2BAOrpBahU%2BZri8yNmThmEHBk7m8L7UY1lWLwWl2lCeHmtZxPVnQ0lsoiQ2KZDS2eZsf%2FFOslILZIy1NdhATEgerPRO9Y592MxwH01%2BHzCAOOywyWG1SRLGuGEJBTyLyoW4WRR23UQvGG5wY7EDxN3dIn4NwuyNkVjwQS8403HziX2DAAFy7158QP%2BfEfApb7qeZm9arcLFh7SaPaTCi7OudQgyGu%2FSXmuyoVA%2FGi3H1YIquVRii4mDtsoxdQyR4a5VFJ%2Bje8omS7d%2BDVOywiaPZo6WpWgmAixJg8865fEAY1evK%2FdrUodYxYccfn0mhaXhZ8tWG9l1O07tomYXEYEVTIRBSrIOy7qSl5k0bB0szjDPm%2F7QBjqkAQW6T79XJ5O76XiGS0SzASoY%2F5Mh%2FC7B1ku4xTXWm0ibsKZLLlDknNzd8kI5tm6P3y6CQ%2BPhuomKXLlHjTrVa0gvu9ytszqsIY7Iq6JmlENyu8rjyBDi2coUIM9a8wjktD8gkVMYdPKHCvQu2ofg6VIKO2SZQ%2Byr2rFkIwGynyx3%2BbYDD1S37GVlLbxTfM43B8T0tvkdXRAJgIxy7MWCmPmw0jH5&X-Amz-Signature=cc881ecbc18ca8f86425d78a46622fab8d777d89b51c0e7bed1f0819366f8a41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







