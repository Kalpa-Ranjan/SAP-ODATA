



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NSUU7AB%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T121249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC1LcrJQhHekvapvdGyNSpsvNG3Jw%2F5VlR%2F6r3LzrlG1AIhAMkPaTxVgR6x9FLbMbOQDcppVZuKHNAwhi4ngg0GbC9xKv8DCAwQABoMNjM3NDIzMTgzODA1Igzku81huG41qnNjBTkq3AMzius%2B4%2B8yLcG1GLIDqz3lw6tWo7wbYzIGhWYE%2BOEyT%2BSCrFDe6iGJ7OPOq%2BADNrka%2B114aapb%2FGH4CdA%2BIibJ0yz9sD8mcWk9vRHo50KjxHpx1JC3e4V4r%2FZtWZ16Pq%2FbU%2Fw1ekpfxDGiqP2UlPmg%2BU9nODYHm70TMCIoRil%2BjQ7Z%2F5y7T%2FcxFdJ4Uohta8%2B6ZTJbslu1PVskBOYU9ofQQagjj4mj21LuiScG6UFp1nBCAZFBeUXTlqjio%2B4n8Sp3D%2BVX%2BbR2rEjhvdSLTQ9mwOFZUvdk86cZaWdv%2Bhc6sh%2FY00DwOTRIQA4wQm6fw%2FmH1e1C88z9BVqp7%2BB8eTZ%2B5ItRFEdqVHxQgshWXgVDTg2O0O3bjU4e5Yp2855ryIvChA8VQG7ZrjAvXGHIC5Y4kgeZE4GSgCg2x5cDxa1zOpGngD8t5ve%2FfbjrFq9X5e%2B4YRns%2BloYNMblnDBR6Bae4vP4rgnxDwSK7T6FTJJ%2F7juXk3TsbAFex6nwRzd5%2FWfzKOgoq8MT8Z6mub%2BDovmLk%2BjpH1SVYhJGeKhYZnbGvq2oiyqm2AIDUqn0RoeYBoGZroYMkxu1hMyo0Udebm8iMTbuIPwcKJ2Sr%2FptvmbkHIt62JIqLbfOmm4gtTC13pjWBjqkAaZ8Clz%2FY%2FzFQdFvcuKG3tHR4ZWWTlqtSHXadU328p5C1%2FboHuxoCqlBiYE93NXYXhN103CuJqH0TEyVXi8vJrv2rxWdie22xu2plFhCIO1Ycg2ml1WDhCZmWsWB9KUaxue3pXHd4vUVbdWUxR%2Fmxhr%2BWYpkAoVaOpf6%2F%2B40Nbspq653LHiOhEIcX6cveX7Nh3l3HMs47s351iFjMMeTLYLrS2e4&X-Amz-Signature=1fd7fd8deabd254f4aeb8d08b5d966ef8930e6486e3412b3183d536741120669&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NSUU7AB%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T121249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC1LcrJQhHekvapvdGyNSpsvNG3Jw%2F5VlR%2F6r3LzrlG1AIhAMkPaTxVgR6x9FLbMbOQDcppVZuKHNAwhi4ngg0GbC9xKv8DCAwQABoMNjM3NDIzMTgzODA1Igzku81huG41qnNjBTkq3AMzius%2B4%2B8yLcG1GLIDqz3lw6tWo7wbYzIGhWYE%2BOEyT%2BSCrFDe6iGJ7OPOq%2BADNrka%2B114aapb%2FGH4CdA%2BIibJ0yz9sD8mcWk9vRHo50KjxHpx1JC3e4V4r%2FZtWZ16Pq%2FbU%2Fw1ekpfxDGiqP2UlPmg%2BU9nODYHm70TMCIoRil%2BjQ7Z%2F5y7T%2FcxFdJ4Uohta8%2B6ZTJbslu1PVskBOYU9ofQQagjj4mj21LuiScG6UFp1nBCAZFBeUXTlqjio%2B4n8Sp3D%2BVX%2BbR2rEjhvdSLTQ9mwOFZUvdk86cZaWdv%2Bhc6sh%2FY00DwOTRIQA4wQm6fw%2FmH1e1C88z9BVqp7%2BB8eTZ%2B5ItRFEdqVHxQgshWXgVDTg2O0O3bjU4e5Yp2855ryIvChA8VQG7ZrjAvXGHIC5Y4kgeZE4GSgCg2x5cDxa1zOpGngD8t5ve%2FfbjrFq9X5e%2B4YRns%2BloYNMblnDBR6Bae4vP4rgnxDwSK7T6FTJJ%2F7juXk3TsbAFex6nwRzd5%2FWfzKOgoq8MT8Z6mub%2BDovmLk%2BjpH1SVYhJGeKhYZnbGvq2oiyqm2AIDUqn0RoeYBoGZroYMkxu1hMyo0Udebm8iMTbuIPwcKJ2Sr%2FptvmbkHIt62JIqLbfOmm4gtTC13pjWBjqkAaZ8Clz%2FY%2FzFQdFvcuKG3tHR4ZWWTlqtSHXadU328p5C1%2FboHuxoCqlBiYE93NXYXhN103CuJqH0TEyVXi8vJrv2rxWdie22xu2plFhCIO1Ycg2ml1WDhCZmWsWB9KUaxue3pXHd4vUVbdWUxR%2Fmxhr%2BWYpkAoVaOpf6%2F%2B40Nbspq653LHiOhEIcX6cveX7Nh3l3HMs47s351iFjMMeTLYLrS2e4&X-Amz-Signature=5692b091be4e4836cd4df4a213bb5a22b174a4a56897eccfb83aa58d1d65be13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







