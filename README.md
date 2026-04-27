



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3CRGHHW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T132825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkslgJPJjaZB7vW5uvN68wj9s6R1ojQ5gRIUdM%2Fe%2Bz8gIhAIW1B1LK1tMadF195Zh9fYjmptI%2BkfWUW7KnicZqwMJBKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdvGKb1589J06Y4T0q3AMPXMM3d2B4FrcMgywArPF2F07ATsUzk6DeRDkuBvxINI6hbO7EuPo7ZaMN1D0Z4Ew36b1OjzIbkYeg%2BuuLqtvNO60xxSEBXg7G9QyCL3XJ5jjX5OuL3xtKUcFSoM3QQ4tzkszGPFMuIUQbnzt%2FygcOVeMKqppKqywqQGc5PdKl0kqkU24hdKVspfK8mk9gUo7Eqwy9btYzXJE24QVnGVC3HqT5JlFziG0w%2FYX1wdulp88Lap0CXiq5a0llb3eQATSBrLvss55K%2B7Y1e2VVsoZ%2B4v0dJQPYRLTv6Nyc43Ljb56kbMRZ2LVNZZrWg%2FgqjUFFBrDaCT%2FP5NDihYGr53K8Y7iJ9mWyepl5xDPobfWS0DR3o3EfIN%2FD9DwCVhT25OLrG418Xx8dv7foOh4hNDvs%2BsmDyFPAlShshs%2BsRPfHMshRkRxOHyzWGTG1VrkFPdP9tjn9OeGO14KgK2xlZA3ex27zCmeUtF6N7ocLQsB860BDjz0%2B6t2MS%2BRN7KilfKSva%2BU5vrUZdx0eM%2BZsg%2FxcIk3zKwHpbpqxxHB91ZHSLy2onnaFdqNSsEZXv1iFZdE%2BoeFitLaI3utvHOTDJ%2FbIJLwCdwcxxSVwRgbKG0%2FI3BHkkMFuAZwLyMGA5zDvxL3PBjqkAXF7OV0MQt6xGxC%2FnXcLCXJwRtuYhTg9nkR7eGR7dyLbhSTPG%2FF6JzaIGQe7zCc6agI1HYHTMvWpb6TDOWqUjj5%2FE%2BGk2bxjrj24Qe%2BqeBm%2FG9Oli2tn6tqRbIY2GGZKGXImmlYQ49xXxRnT5vxemWYvhEkspDhFeYNgMbRxv6OIkhEQlpQlKjVMWKK8bPwdnu2LKBpYEl2HXWqzGnzW5SWQgNAL&X-Amz-Signature=16393c0c88dce452a48b7d48f66c65e551d81de7908ee2d1392148a08f6c11f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3CRGHHW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T132825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkslgJPJjaZB7vW5uvN68wj9s6R1ojQ5gRIUdM%2Fe%2Bz8gIhAIW1B1LK1tMadF195Zh9fYjmptI%2BkfWUW7KnicZqwMJBKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdvGKb1589J06Y4T0q3AMPXMM3d2B4FrcMgywArPF2F07ATsUzk6DeRDkuBvxINI6hbO7EuPo7ZaMN1D0Z4Ew36b1OjzIbkYeg%2BuuLqtvNO60xxSEBXg7G9QyCL3XJ5jjX5OuL3xtKUcFSoM3QQ4tzkszGPFMuIUQbnzt%2FygcOVeMKqppKqywqQGc5PdKl0kqkU24hdKVspfK8mk9gUo7Eqwy9btYzXJE24QVnGVC3HqT5JlFziG0w%2FYX1wdulp88Lap0CXiq5a0llb3eQATSBrLvss55K%2B7Y1e2VVsoZ%2B4v0dJQPYRLTv6Nyc43Ljb56kbMRZ2LVNZZrWg%2FgqjUFFBrDaCT%2FP5NDihYGr53K8Y7iJ9mWyepl5xDPobfWS0DR3o3EfIN%2FD9DwCVhT25OLrG418Xx8dv7foOh4hNDvs%2BsmDyFPAlShshs%2BsRPfHMshRkRxOHyzWGTG1VrkFPdP9tjn9OeGO14KgK2xlZA3ex27zCmeUtF6N7ocLQsB860BDjz0%2B6t2MS%2BRN7KilfKSva%2BU5vrUZdx0eM%2BZsg%2FxcIk3zKwHpbpqxxHB91ZHSLy2onnaFdqNSsEZXv1iFZdE%2BoeFitLaI3utvHOTDJ%2FbIJLwCdwcxxSVwRgbKG0%2FI3BHkkMFuAZwLyMGA5zDvxL3PBjqkAXF7OV0MQt6xGxC%2FnXcLCXJwRtuYhTg9nkR7eGR7dyLbhSTPG%2FF6JzaIGQe7zCc6agI1HYHTMvWpb6TDOWqUjj5%2FE%2BGk2bxjrj24Qe%2BqeBm%2FG9Oli2tn6tqRbIY2GGZKGXImmlYQ49xXxRnT5vxemWYvhEkspDhFeYNgMbRxv6OIkhEQlpQlKjVMWKK8bPwdnu2LKBpYEl2HXWqzGnzW5SWQgNAL&X-Amz-Signature=6dd98ba5c3f8f20e91f96b43a15fc3199258d496ff19bcbbfffe515420a1b417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







