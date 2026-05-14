



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJDNMZH%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T083118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXWmz2y0DV%2F6lkb6LVuFy6J%2BLtVM8gvLlI8YuC1uOSzAIhANA45Obo640dv0S%2Fg%2BCTKstl2QbBdmIO7W0ikjkP%2BBWXKv8DCFcQABoMNjM3NDIzMTgzODA1IgxEGFQkDwkgDctYIOYq3AMilf5wM8fWXk%2FitwLse7A5WeB9V4WbEkR%2BrFQxc6feu2ZP%2FoLNXGt%2Fc%2F9S4kRbRaUL9YG0ZkJb7mm94UfZhzKfV95seOD6Lw%2FOOxdYpIZmDqBtnm09pvu0U5ZZJh1qpaEj4G7hi%2FyA0cBmXuKOzY6n2foxPtRlo3Pt6R%2BSGMcGQgN%2FEOr79ccaRYyeWh2AgBGlTPw19SQoAD1HVcPPc7ircu7ac1OtK3eTgp2HjWTQutLTqw%2FC4YwTQ2HtIkdE80LFj%2BVMLBeDzoQ%2BOmb38jyGAFT5o94LJIvASW6OUgKS1fBwu0Ljk7xutDCxETkEgyTJ62OQua182o%2Bci2Sl7MDFCnKM9kuTKeFenNr8WRPdwQwCwuVZnueeSVqlKBUXNpxHKbVi0t2FX4rfabgryH2470T6Eo9rAFIDaaWzUr2i3jdSHnIKPDSqqQ3QBbE%2F24dVkvBl%2FRRDdnDtnz3uo4NnhgfSCqbYVsNpEdr9yVnP8kA16MOF2JP%2Bb%2Blud%2BUg%2FCKdMzvZUlTWGsa9E%2FGIymCmxU6fyP%2FwetQm26ZK1B5yvL8BeocKLpv7%2Fxy0WpY1yBHhRg9eELpuY9KvJHjEx1PH2M4QHeXofSar06Ut%2F1rVJ8dvtdHnkZKyA6pazTCe0pXQBjqkAcFAFCkMHILLWQiaqNWVwpcEKj4uh%2B%2FOytyMOjVk6323SvnMqUiU7Qta3O%2BT%2FegiG0qah6FUPC%2FhBbM9LltrVinz21S%2FvRJoc0ixOLFWqEDgzuYh1uT2ZD5TXk94CmL8NjRBe1VkW7pmSXxDG5xGHcE4vkS0WEk8bQJZ%2FNf8gGXV9hEw2sO1sB6lleHf%2BUNf8TNJhI3xENRF%2F0kda2rLPrQCc7QS&X-Amz-Signature=aa4eef234543bb9c8a4876114d35b50e0d358a240723e17bdb5af4393dfde2a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJDNMZH%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T083118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXWmz2y0DV%2F6lkb6LVuFy6J%2BLtVM8gvLlI8YuC1uOSzAIhANA45Obo640dv0S%2Fg%2BCTKstl2QbBdmIO7W0ikjkP%2BBWXKv8DCFcQABoMNjM3NDIzMTgzODA1IgxEGFQkDwkgDctYIOYq3AMilf5wM8fWXk%2FitwLse7A5WeB9V4WbEkR%2BrFQxc6feu2ZP%2FoLNXGt%2Fc%2F9S4kRbRaUL9YG0ZkJb7mm94UfZhzKfV95seOD6Lw%2FOOxdYpIZmDqBtnm09pvu0U5ZZJh1qpaEj4G7hi%2FyA0cBmXuKOzY6n2foxPtRlo3Pt6R%2BSGMcGQgN%2FEOr79ccaRYyeWh2AgBGlTPw19SQoAD1HVcPPc7ircu7ac1OtK3eTgp2HjWTQutLTqw%2FC4YwTQ2HtIkdE80LFj%2BVMLBeDzoQ%2BOmb38jyGAFT5o94LJIvASW6OUgKS1fBwu0Ljk7xutDCxETkEgyTJ62OQua182o%2Bci2Sl7MDFCnKM9kuTKeFenNr8WRPdwQwCwuVZnueeSVqlKBUXNpxHKbVi0t2FX4rfabgryH2470T6Eo9rAFIDaaWzUr2i3jdSHnIKPDSqqQ3QBbE%2F24dVkvBl%2FRRDdnDtnz3uo4NnhgfSCqbYVsNpEdr9yVnP8kA16MOF2JP%2Bb%2Blud%2BUg%2FCKdMzvZUlTWGsa9E%2FGIymCmxU6fyP%2FwetQm26ZK1B5yvL8BeocKLpv7%2Fxy0WpY1yBHhRg9eELpuY9KvJHjEx1PH2M4QHeXofSar06Ut%2F1rVJ8dvtdHnkZKyA6pazTCe0pXQBjqkAcFAFCkMHILLWQiaqNWVwpcEKj4uh%2B%2FOytyMOjVk6323SvnMqUiU7Qta3O%2BT%2FegiG0qah6FUPC%2FhBbM9LltrVinz21S%2FvRJoc0ixOLFWqEDgzuYh1uT2ZD5TXk94CmL8NjRBe1VkW7pmSXxDG5xGHcE4vkS0WEk8bQJZ%2FNf8gGXV9hEw2sO1sB6lleHf%2BUNf8TNJhI3xENRF%2F0kda2rLPrQCc7QS&X-Amz-Signature=b8c132f4a7a9111935be99e8ee44d5aee44839709ae06614046ee66a4375105a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







