



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YTPVPD5%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T182538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHoU7KLCglpz%2Bx8vtY1qlNWoh%2FX%2B7g591fVSfVECOOwIgWVel3o33mhkTQKz3LiWHDWHq5O1g6lXhNh5B0nvDUgYqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLIL9nhMJY9MJlh9SCrcAw4dUEaZ9V0QGX4TV76WHj6Ap3PZXek6GR%2BHN22VxeWYqQPMavArloLscmWjJ%2Bsf8xYVBrMcFVUVQPEBHxWi86EFC5K4qLt37XshY8e%2FnYcq3RPi3eI3cizR4yxxzG9z8TaJJ1LchLOI5xK4gXrv5EPT13gWbFzvyCWD6WHHejJqsLVD34Fqj%2BhGVpzfnaN4LZBEgeie1h%2FupG7ImyeK4OyMPp2H4DdzdjdkDWc4ty2q%2BOJTBjIKDSdwTWrcP8VhNz5tEQU6toXmIRd9ixyu1QIjJqjFTRHWeFw8oRA1BF83%2FyVZQGzm9oBq8HARfmydCGEPqe9fo2Li4%2F8G4hBSi7qiQd2tnMTlrImWK3F%2FdwKbR%2F2fMpvuI8g%2FAjIpm7Dw4WR%2FGkA5IOinuQf0gXwO8mciDC%2B%2F70CKV%2F6dKoSeuSu1jHX3qYpQhGuR25G11tGb8ZPe3Q5pMxKZ3z7Q0rssxvCj7kVd7RfTfXJK1%2Fkq588k%2BkT8vBG9HY4vAFXRj7TVs%2Feol3ngDSSH7BuhBltzr8ozne5g0ucyRTDvFooYazI6CPaVNWNfgv7X94ozlQ94H37dgEl3pkmU61jGPstRwrS%2F3%2Fl5FpXENTbo4mHyL9pAL%2BW5gcJPHw7hQo7XMOaNhcsGOqUBxaMcY0z1KQdwEx68KK%2FWuCxtKPQjxoDCxgEyvWiMHap9QulKoh%2F3fcb0job4Z0p1pn5cCjyuHmoAxE%2FaDtOumedRqb7H%2FvVQ3N7msd6395U7RiJ6%2FAVbd2uv9LcxaKzPrCv%2F9s8GqQMiZhZwLvj2X7bKvN1%2Bah79NN%2FVjtlbf8CyG02hH5urqylwitpDwSGYWR%2FrE%2BphjCVPQBrIwliWNbtZ0xpE&X-Amz-Signature=5d2ca6d1ec46ba62b91ea19e4be529eb8aaac7bd0821ed4fbde58124376f2071&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YTPVPD5%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T182538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHoU7KLCglpz%2Bx8vtY1qlNWoh%2FX%2B7g591fVSfVECOOwIgWVel3o33mhkTQKz3LiWHDWHq5O1g6lXhNh5B0nvDUgYqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLIL9nhMJY9MJlh9SCrcAw4dUEaZ9V0QGX4TV76WHj6Ap3PZXek6GR%2BHN22VxeWYqQPMavArloLscmWjJ%2Bsf8xYVBrMcFVUVQPEBHxWi86EFC5K4qLt37XshY8e%2FnYcq3RPi3eI3cizR4yxxzG9z8TaJJ1LchLOI5xK4gXrv5EPT13gWbFzvyCWD6WHHejJqsLVD34Fqj%2BhGVpzfnaN4LZBEgeie1h%2FupG7ImyeK4OyMPp2H4DdzdjdkDWc4ty2q%2BOJTBjIKDSdwTWrcP8VhNz5tEQU6toXmIRd9ixyu1QIjJqjFTRHWeFw8oRA1BF83%2FyVZQGzm9oBq8HARfmydCGEPqe9fo2Li4%2F8G4hBSi7qiQd2tnMTlrImWK3F%2FdwKbR%2F2fMpvuI8g%2FAjIpm7Dw4WR%2FGkA5IOinuQf0gXwO8mciDC%2B%2F70CKV%2F6dKoSeuSu1jHX3qYpQhGuR25G11tGb8ZPe3Q5pMxKZ3z7Q0rssxvCj7kVd7RfTfXJK1%2Fkq588k%2BkT8vBG9HY4vAFXRj7TVs%2Feol3ngDSSH7BuhBltzr8ozne5g0ucyRTDvFooYazI6CPaVNWNfgv7X94ozlQ94H37dgEl3pkmU61jGPstRwrS%2F3%2Fl5FpXENTbo4mHyL9pAL%2BW5gcJPHw7hQo7XMOaNhcsGOqUBxaMcY0z1KQdwEx68KK%2FWuCxtKPQjxoDCxgEyvWiMHap9QulKoh%2F3fcb0job4Z0p1pn5cCjyuHmoAxE%2FaDtOumedRqb7H%2FvVQ3N7msd6395U7RiJ6%2FAVbd2uv9LcxaKzPrCv%2F9s8GqQMiZhZwLvj2X7bKvN1%2Bah79NN%2FVjtlbf8CyG02hH5urqylwitpDwSGYWR%2FrE%2BphjCVPQBrIwliWNbtZ0xpE&X-Amz-Signature=cf123d9641afe54efe1543d246ad3610e13da6f9e10b3026fa3fdf7ca86f3bbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







