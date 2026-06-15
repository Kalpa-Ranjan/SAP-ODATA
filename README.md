



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S437XDL%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T170717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBthu3DnMQZ%2FFBIgEFRwzQPKgEqG6J4HRU%2FcGSLeqz9KAiEAtyZLKHc4vaMoYnorNkOsPC3dtgQIIDvzJYYdZAXPF78q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDIaNjOK%2B4bFm%2BEuUlyrcAwT3GKYNaDoFP4JtlR5CI0vjMVdc0%2BAg7PrWnmtgeu8NrVqCKzzrqNdJWK1wzidnIhDQzRvF7vtPle%2Bf4D%2Fe%2BTc4WqMm%2BhsjcrNCb6n0vOMT5UMB%2BhMKUcEqp9f5iWQOvOUjimlLxQvj2K0LYtZVk7Ght3RvW42jfkIcKOclDbvuN5kaqEYEQDJmK67xSrTPDNBnScKm5xnecOkEB2s2Z1KLINew53WtSSPnIqsFF6Swqjbw8m4F59M7TQLgiPZdGu6q%2Fr38fYuXdZlvUx8IqgPifckWr6VnESyVY%2B0lcksrOSQx0nQJobhE6dgQwLvgfdz2l5%2FxErA3aaUoPtW2tM8gBCFyo8owwWPT1%2FNOATI66t716B%2BkNzAcPsQ6uVGyVa6hz6n%2BKqdYFhlvrSHp0yTiUvEsd4PuqEWc2AapvxLdUF2mwvRca63Wgs2PE6k9qM1Px8GA3PlkktHef3FWp31XYnsuRhyTmYxAxI94qtCutqSjNMN%2BHSoRQXNVJhnflIZ%2F%2Fhs5GCxf%2Fx2gViZa4%2FETaynw8%2FNgQ5JKOgWHjmphz8XHlfZxLh0sYEkvPKXQwJB%2BW9tSxCqXYtLm9VkT1oUUnL7AVlTEIM3KuUYRGQT9L14ZhzZTfljeoBxpMLXPwNEGOqUB8ipYJ0EKukTAoGGOUHAElUcH2AbXHZt189%2F6kKYwJ3dFqV4AxceWtJ8AsLrPYpnu9GaQVe8tSRLTERgYmu2xmB1Y5gp%2BtOkmZMNDurnxxfPqf7b%2Bmy0q8vO5NJw8q0IUM2aWWHJKOccERePsncME9HAbHKMBXMeCChGUngGmEFAtsZ7YRiSYswusuvmS%2BfpLPPpIf6XbZwxDuJVvGx2dRqe4D8NW&X-Amz-Signature=669a9c05d5355fdac0f441777eb10c7365afcd9a81931ddfd578682f1e0216a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S437XDL%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T170717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBthu3DnMQZ%2FFBIgEFRwzQPKgEqG6J4HRU%2FcGSLeqz9KAiEAtyZLKHc4vaMoYnorNkOsPC3dtgQIIDvzJYYdZAXPF78q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDIaNjOK%2B4bFm%2BEuUlyrcAwT3GKYNaDoFP4JtlR5CI0vjMVdc0%2BAg7PrWnmtgeu8NrVqCKzzrqNdJWK1wzidnIhDQzRvF7vtPle%2Bf4D%2Fe%2BTc4WqMm%2BhsjcrNCb6n0vOMT5UMB%2BhMKUcEqp9f5iWQOvOUjimlLxQvj2K0LYtZVk7Ght3RvW42jfkIcKOclDbvuN5kaqEYEQDJmK67xSrTPDNBnScKm5xnecOkEB2s2Z1KLINew53WtSSPnIqsFF6Swqjbw8m4F59M7TQLgiPZdGu6q%2Fr38fYuXdZlvUx8IqgPifckWr6VnESyVY%2B0lcksrOSQx0nQJobhE6dgQwLvgfdz2l5%2FxErA3aaUoPtW2tM8gBCFyo8owwWPT1%2FNOATI66t716B%2BkNzAcPsQ6uVGyVa6hz6n%2BKqdYFhlvrSHp0yTiUvEsd4PuqEWc2AapvxLdUF2mwvRca63Wgs2PE6k9qM1Px8GA3PlkktHef3FWp31XYnsuRhyTmYxAxI94qtCutqSjNMN%2BHSoRQXNVJhnflIZ%2F%2Fhs5GCxf%2Fx2gViZa4%2FETaynw8%2FNgQ5JKOgWHjmphz8XHlfZxLh0sYEkvPKXQwJB%2BW9tSxCqXYtLm9VkT1oUUnL7AVlTEIM3KuUYRGQT9L14ZhzZTfljeoBxpMLXPwNEGOqUB8ipYJ0EKukTAoGGOUHAElUcH2AbXHZt189%2F6kKYwJ3dFqV4AxceWtJ8AsLrPYpnu9GaQVe8tSRLTERgYmu2xmB1Y5gp%2BtOkmZMNDurnxxfPqf7b%2Bmy0q8vO5NJw8q0IUM2aWWHJKOccERePsncME9HAbHKMBXMeCChGUngGmEFAtsZ7YRiSYswusuvmS%2BfpLPPpIf6XbZwxDuJVvGx2dRqe4D8NW&X-Amz-Signature=889d57657b73dd8bf06e6ffc1b66ff6ab5b4d1c6353d8bc448b91fc5901f7726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







