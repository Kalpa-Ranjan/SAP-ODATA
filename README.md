



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFGFQKIP%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T120608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCaCSG7stHnvx0dBd87iYHDH1ZF3bSFnrrYLNauCGqnrQIgbYkTH8KdsPDttYxADDICVHnk1wzzpO7WM6nAc4MPiSoqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIv7ZJVge0dod%2FeVBCrcAwfrvZ64N0XG0aGP7TtUA2WeV6PX%2BeyCFLcpbYEJ5kRRXVafDyQYAIV8OWsbTEVCV2MHirJhYWVY34ak617OrdoZXuLD2V9ZEVVbpIKN4tw1lcwfVUZLZYPNRy2%2FZCGkQw3jgylgIsPIwOryD4QY6UQ%2F54mMft%2FQ%2BbaUBLWXkoCm3Jwg1Hjy%2F4Z6e5u0X0uRfVvbp3thc%2FAr3jDUiC%2B4797L93rZQdaHprO1UWeXCThq4C3T1SC9ev4jb6MYlKqiDL6AXc60%2BPRHKapdEm5tIor3zMnQQgnYM6St1Fgd14JKKPUxC7OvdqFghgPewrEBwLF7D70olaWAx7mvf1zWB3WjDvVpQRFTUGm3zJLB%2FwkI7Hn7CggLkxTk8gu5B7Koyq5Vb2xIRX6M15rfVvu%2Fg6TXXinbUcnrhL7MTNj29aCiVClva%2BHO3%2Fb46WkQNCi2obF6JN5t0IcxGHddl0I22tz47bEzUv7rbEdEJB289R35Ig%2F7wABkPvafWE6HjcGlGShZCQuWFLHJDwtBEUTGAWxaFPadA63jY94bnT0kVf%2BQ0TEPBt19eyNCA2qdZYWqcoVA3OOkxOfb1F%2FlSFcjij1m%2BvkwIcGNFfVlUNJzy9av%2BOrnwiI19B4J6PqLMIXbu9cGOqUBHEflF92viqIZVq9i6r4GDIysrGxmQmycQ8c6B1%2FCUdh2wKS49mrQs%2FFypkLzyTLagfxVYYjPd1XP%2FsQWyVMDE6jx8YLUqeq5Tj3%2BqhmFcBmBEVfExmv0TIwJ76xJ%2FzZWdzVufjP%2FBKuyqLLF0pJGERA9tQm19svbaXgh1wEGHuNt3y3nvTRczbem%2Bu9AnRmc24xZtHtnrCS7Uepi%2Bfu%2BfY1v0%2FIp&X-Amz-Signature=9bc734c77842a081673fd30413dbbe6178b28c7002b03e546282190c8c48eacf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFGFQKIP%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T120608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQCaCSG7stHnvx0dBd87iYHDH1ZF3bSFnrrYLNauCGqnrQIgbYkTH8KdsPDttYxADDICVHnk1wzzpO7WM6nAc4MPiSoqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIv7ZJVge0dod%2FeVBCrcAwfrvZ64N0XG0aGP7TtUA2WeV6PX%2BeyCFLcpbYEJ5kRRXVafDyQYAIV8OWsbTEVCV2MHirJhYWVY34ak617OrdoZXuLD2V9ZEVVbpIKN4tw1lcwfVUZLZYPNRy2%2FZCGkQw3jgylgIsPIwOryD4QY6UQ%2F54mMft%2FQ%2BbaUBLWXkoCm3Jwg1Hjy%2F4Z6e5u0X0uRfVvbp3thc%2FAr3jDUiC%2B4797L93rZQdaHprO1UWeXCThq4C3T1SC9ev4jb6MYlKqiDL6AXc60%2BPRHKapdEm5tIor3zMnQQgnYM6St1Fgd14JKKPUxC7OvdqFghgPewrEBwLF7D70olaWAx7mvf1zWB3WjDvVpQRFTUGm3zJLB%2FwkI7Hn7CggLkxTk8gu5B7Koyq5Vb2xIRX6M15rfVvu%2Fg6TXXinbUcnrhL7MTNj29aCiVClva%2BHO3%2Fb46WkQNCi2obF6JN5t0IcxGHddl0I22tz47bEzUv7rbEdEJB289R35Ig%2F7wABkPvafWE6HjcGlGShZCQuWFLHJDwtBEUTGAWxaFPadA63jY94bnT0kVf%2BQ0TEPBt19eyNCA2qdZYWqcoVA3OOkxOfb1F%2FlSFcjij1m%2BvkwIcGNFfVlUNJzy9av%2BOrnwiI19B4J6PqLMIXbu9cGOqUBHEflF92viqIZVq9i6r4GDIysrGxmQmycQ8c6B1%2FCUdh2wKS49mrQs%2FFypkLzyTLagfxVYYjPd1XP%2FsQWyVMDE6jx8YLUqeq5Tj3%2BqhmFcBmBEVfExmv0TIwJ76xJ%2FzZWdzVufjP%2FBKuyqLLF0pJGERA9tQm19svbaXgh1wEGHuNt3y3nvTRczbem%2Bu9AnRmc24xZtHtnrCS7Uepi%2Bfu%2BfY1v0%2FIp&X-Amz-Signature=d49bd1fcfbd9c4c7d29bf55b6938fb796b3dd03fe25d0985e39d17456afd85a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







