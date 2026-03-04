



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPQ267U6%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T184044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXZPPvzukzbZeB4ety7iediZT%2FUC98VYFAdlWi%2FKcukwIhAIFQYkQVv%2BoJ06tYwaA3P1gaCA%2FrK8KJr2a4NnChwSiEKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrkQjRzMEcb5HCgvEq3APqBZbJWtyR3WsIdUkuVT0NFQ2l44jpkLRehvIsuJeD%2BQZivantfwf4d13Hu262i4gwSxK%2FEsX80%2BkI44%2FvhvobHcAmXUuIJllmy%2BCL4GYiiLdI5v8cqHE9aB2bzglr4xIn67%2F4%2FA49GG4ee4zDHTCcPTADZzDjyB4UL0R6eHfQKFP7FYWXQ%2BuIbMXTlRk5mdTWGwLskYjSPQ0iQFU34Q3hRZXtr1XD3tmocrRtkqDBC3wtNf0YPgAXNlZs6W%2BUrAuywFAGEIC903bYW1bwje%2BuQtek1UmRj9Qzws0p5ecJTTn4U2Wlu1PU6f03FZwWSK2t8IetcpcFPsg2g9lJzbI2QVLCs1GwJVbICNfoIS9iok3UiCAqSa86BvMP%2BwF9nEJkTPTkhpwavvYbi0t31mdsD8kXsXFB4Gk6yKUfMT4UIY%2FRGUJflys2yQPjEE7%2FlLJq6HhhObEP03vH8wR2QJSjhwasQSunF9kpjHBRs6i3k%2B26bnblJcacU%2FrgvCugc2WaujwjFT0tKv1ZJLHQrOw8VcVaITNaebNQkn3BhxGlpau9%2B%2Bh0lPwzb7tEBpZuOjrNOAQb%2B1YP1%2F%2BlxI82SRrLKqmBc15rtElUmtqp1AW1BcUNOqFykoI4a9xgMTCD46HNBjqkASnNqHk96mbselndFNc2bJoj4T%2Fse9oLQrJ6D4uf0MrB49szFUmP%2Fbv9OEFqohPUqjrsaXXIfOFZ4d0rLvsdsWZd%2F8nzgx1FbhAQ59d4IwUygBNsbUvWwW2wtNpEz7mR2iSRXT78xjZxj0Q%2BPGJG0NDDDYmN3KSPrHFb3QaZIByMbNs0362YCR0DU1JA%2FDr6sfujQ%2FXwtbOmqfenFqi6Crz4DHUj&X-Amz-Signature=0b0530ce49d9692776ce95d09073d172c4394ac43d5a0ff9f83b0a1bc1a9a0fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPQ267U6%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T184045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXZPPvzukzbZeB4ety7iediZT%2FUC98VYFAdlWi%2FKcukwIhAIFQYkQVv%2BoJ06tYwaA3P1gaCA%2FrK8KJr2a4NnChwSiEKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrkQjRzMEcb5HCgvEq3APqBZbJWtyR3WsIdUkuVT0NFQ2l44jpkLRehvIsuJeD%2BQZivantfwf4d13Hu262i4gwSxK%2FEsX80%2BkI44%2FvhvobHcAmXUuIJllmy%2BCL4GYiiLdI5v8cqHE9aB2bzglr4xIn67%2F4%2FA49GG4ee4zDHTCcPTADZzDjyB4UL0R6eHfQKFP7FYWXQ%2BuIbMXTlRk5mdTWGwLskYjSPQ0iQFU34Q3hRZXtr1XD3tmocrRtkqDBC3wtNf0YPgAXNlZs6W%2BUrAuywFAGEIC903bYW1bwje%2BuQtek1UmRj9Qzws0p5ecJTTn4U2Wlu1PU6f03FZwWSK2t8IetcpcFPsg2g9lJzbI2QVLCs1GwJVbICNfoIS9iok3UiCAqSa86BvMP%2BwF9nEJkTPTkhpwavvYbi0t31mdsD8kXsXFB4Gk6yKUfMT4UIY%2FRGUJflys2yQPjEE7%2FlLJq6HhhObEP03vH8wR2QJSjhwasQSunF9kpjHBRs6i3k%2B26bnblJcacU%2FrgvCugc2WaujwjFT0tKv1ZJLHQrOw8VcVaITNaebNQkn3BhxGlpau9%2B%2Bh0lPwzb7tEBpZuOjrNOAQb%2B1YP1%2F%2BlxI82SRrLKqmBc15rtElUmtqp1AW1BcUNOqFykoI4a9xgMTCD46HNBjqkASnNqHk96mbselndFNc2bJoj4T%2Fse9oLQrJ6D4uf0MrB49szFUmP%2Fbv9OEFqohPUqjrsaXXIfOFZ4d0rLvsdsWZd%2F8nzgx1FbhAQ59d4IwUygBNsbUvWwW2wtNpEz7mR2iSRXT78xjZxj0Q%2BPGJG0NDDDYmN3KSPrHFb3QaZIByMbNs0362YCR0DU1JA%2FDr6sfujQ%2FXwtbOmqfenFqi6Crz4DHUj&X-Amz-Signature=01755c576148c1d2564dde3c1036c362710595e1d9b2ce77500524534fac5e1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







