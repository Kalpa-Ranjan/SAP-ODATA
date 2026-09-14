



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGECJGJ%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T002319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIDzNaCBP8tRGQxlvrR57jyeYbXdnAJbq8nl75OVZLhI%2BAiBTIFyFtdYXinq9c3MGi7I6FHL3w79ryc%2BFt88KCm%2FCGyqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpKZEvcE5Wjxrxd%2BkKtwDeskVUjEzPAbNA6spUqItr8FAFvKxjSvCVuQA5N%2F1unfWBYwC1jRkSdEIyiqy6M7xbkeZ8Tl%2FJPehHWqnVmJJVEzsMNDKCD%2F2%2FHXWZeovcM1SYCGE%2FgQbt7%2FhpnWC5hEi3ZqOeccSr82%2BN8%2B5pVNXeVnp%2Bh5xiRjhMKgXsoRB92WQSr0UCstEK18GYDXrsOBfEIcKvqqF10B1ZjxdyT%2BFegVsoCarRZx36EV1W76PD3UuVP3MR3aLlh9CWshWl8HcghlqZYXOXOvlEFaxiKzl7YZsLisEaG8bxHhQRVyIV4zLlUONZBKe6BbS7STgeOs6APgFHt1JQ9PqHyXgkjRxWwJb76wmfoPlou8s5Nu3hj8bicABY7e5sm7XQv107Xd0k7CEsqxIKTLjZhCnQWl3bAj4WIbt%2BkDZkDU7Mj2dbbfnCtgOxix704yuQtEjo3O0v1Mu806K3RZJxBsVy0BA3ZCpXU6Fudwx5hJfFQ0YanHy2WMKoebesxseC2uBqvM%2FUeYzkKpAIG8kLdgXZrGlhJkgDL4tyJeZxE9DTEO8urrWRAporv2SItwygsxYZ8BpKuDDsgDtvSOv6MVOM%2FhkLBlMZci5ctjj1Ix9zUQo%2FRbFxgpMTY%2BoDdc0oO0w%2Fuec1QY6pgFxoRQ3Fpy7ZDUb3HyxI3csrI0Dk2aZCCwVBoE5IRJPUVgpVTDhYzNgQa%2FOAMDCTYND0WZmRaKnjQKDTDm4fcvIW9DDCIOo8QCZfYzmNYQyNh4%2FxBr1ew43chOs8t%2Foc3RKeEhU%2FaE0l9L%2FhbGNmF39u%2BNdfQjjsNkLkgjDEHh7wnF%2BJpAoQBev781MQOWo%2BfNZcsqbODKCPFzMt6t0lyIyIx3FQcTw&X-Amz-Signature=925ccebb37d587cf7584639157b5e50705368d58996b860ed57bfb752d46a311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJGECJGJ%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T002319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIDzNaCBP8tRGQxlvrR57jyeYbXdnAJbq8nl75OVZLhI%2BAiBTIFyFtdYXinq9c3MGi7I6FHL3w79ryc%2BFt88KCm%2FCGyqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpKZEvcE5Wjxrxd%2BkKtwDeskVUjEzPAbNA6spUqItr8FAFvKxjSvCVuQA5N%2F1unfWBYwC1jRkSdEIyiqy6M7xbkeZ8Tl%2FJPehHWqnVmJJVEzsMNDKCD%2F2%2FHXWZeovcM1SYCGE%2FgQbt7%2FhpnWC5hEi3ZqOeccSr82%2BN8%2B5pVNXeVnp%2Bh5xiRjhMKgXsoRB92WQSr0UCstEK18GYDXrsOBfEIcKvqqF10B1ZjxdyT%2BFegVsoCarRZx36EV1W76PD3UuVP3MR3aLlh9CWshWl8HcghlqZYXOXOvlEFaxiKzl7YZsLisEaG8bxHhQRVyIV4zLlUONZBKe6BbS7STgeOs6APgFHt1JQ9PqHyXgkjRxWwJb76wmfoPlou8s5Nu3hj8bicABY7e5sm7XQv107Xd0k7CEsqxIKTLjZhCnQWl3bAj4WIbt%2BkDZkDU7Mj2dbbfnCtgOxix704yuQtEjo3O0v1Mu806K3RZJxBsVy0BA3ZCpXU6Fudwx5hJfFQ0YanHy2WMKoebesxseC2uBqvM%2FUeYzkKpAIG8kLdgXZrGlhJkgDL4tyJeZxE9DTEO8urrWRAporv2SItwygsxYZ8BpKuDDsgDtvSOv6MVOM%2FhkLBlMZci5ctjj1Ix9zUQo%2FRbFxgpMTY%2BoDdc0oO0w%2Fuec1QY6pgFxoRQ3Fpy7ZDUb3HyxI3csrI0Dk2aZCCwVBoE5IRJPUVgpVTDhYzNgQa%2FOAMDCTYND0WZmRaKnjQKDTDm4fcvIW9DDCIOo8QCZfYzmNYQyNh4%2FxBr1ew43chOs8t%2Foc3RKeEhU%2FaE0l9L%2FhbGNmF39u%2BNdfQjjsNkLkgjDEHh7wnF%2BJpAoQBev781MQOWo%2BfNZcsqbODKCPFzMt6t0lyIyIx3FQcTw&X-Amz-Signature=1131b15d7d4cbcee3826102b9aef40e2495d26c0b468c01382e7635a1792a440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







