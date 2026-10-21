



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N2N32TO%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T001901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHmp%2BWVMuJSN7XbExTZ1IZFZ%2BN63cYk9yj4PwvbH3f%2FeAiBzj1Ni04NempT3i7vOg5mTnL6gm9XvcTJLTy%2F3Tz5%2Fmir%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMe%2FpCZnPp%2BTQWv3oaKtwD4vEmR2ltGlZT2f%2BPORqWHtAgVBddhG2y0ywqLLaYXhHuAMmbenzsHg6hLLs6wEaW05yhp%2BCDBSFs%2BcmrFzqs1Wmyy5liJweB70%2F9VLWCfkaYtkOm3hFEKjElepcS0fr22NS8l9DmBx0LTkE0XC2xCiC3S2zkmpfZfsP0fw6JVtS3wJ5jjTnBTL0t9549hFg93Se3VZdB%2FW2xvGZCLRqNqicjCbv9o7yMBLjpBrD3sE4rwQDFW6lk5prClDeuWkHJNLd5KeRQ2C185K7h9al04bnIcAkKeuErEy2L1pmp1KMd5tcEmpti6vRBEzIdxLIg%2BZK%2FfGstpKDQCD5Zq1WPMK%2F9QW31%2FqnFcpbXw0of7bL1XsSQN2tWfKMcVklHXPG09yYazxvnEa8k2BsDb%2Beosf91qnlf%2Fx%2BguYKwd%2FnBDR1NFMP1ZOUxv8bYfvxkEBZLftbWWZpp8bvU6g%2BypyJ7ZSo2Yumk8THUtLSJNfr0yQfKOePJBnZyKecotuHG87n2J76BSpDJmhjT%2Bzb5JYoxZNWJeBUQW6%2F6vlax3%2Fxx45VvQ9UgAZBmIEkWF3yORfxsYIuNwVdFIUFNtmpsXrBtlBJktuU%2B298Op4seh3AXuPFeCJ1xYFPmUzFhwgow6Mnf1gY6pgE7yd7wdHSTu%2Fda1daisdL3ZJlUa9j9PcZm%2F2kPMkNmtRkWy56JpeOEU0zvedFwj7HkseF89gm8%2FzaxgVHHAXfHTQaILJuFYElqmcBEZex76JLFf5hEd6%2BqfdmpcN3nfslXTkyp8jkZXjWFbpgh1%2BFuu0r2AugbQYS0dIcQhBbBmCSqpoATSLGBbBdzKpTSve9uwFjqTkgBlX2u7AsHboAMPI6G3r1G&X-Amz-Signature=c6088e25ea176632167ecc7ecbb320569b184cffaacbaf45301c1a51056ac5c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N2N32TO%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T001901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHmp%2BWVMuJSN7XbExTZ1IZFZ%2BN63cYk9yj4PwvbH3f%2FeAiBzj1Ni04NempT3i7vOg5mTnL6gm9XvcTJLTy%2F3Tz5%2Fmir%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMe%2FpCZnPp%2BTQWv3oaKtwD4vEmR2ltGlZT2f%2BPORqWHtAgVBddhG2y0ywqLLaYXhHuAMmbenzsHg6hLLs6wEaW05yhp%2BCDBSFs%2BcmrFzqs1Wmyy5liJweB70%2F9VLWCfkaYtkOm3hFEKjElepcS0fr22NS8l9DmBx0LTkE0XC2xCiC3S2zkmpfZfsP0fw6JVtS3wJ5jjTnBTL0t9549hFg93Se3VZdB%2FW2xvGZCLRqNqicjCbv9o7yMBLjpBrD3sE4rwQDFW6lk5prClDeuWkHJNLd5KeRQ2C185K7h9al04bnIcAkKeuErEy2L1pmp1KMd5tcEmpti6vRBEzIdxLIg%2BZK%2FfGstpKDQCD5Zq1WPMK%2F9QW31%2FqnFcpbXw0of7bL1XsSQN2tWfKMcVklHXPG09yYazxvnEa8k2BsDb%2Beosf91qnlf%2Fx%2BguYKwd%2FnBDR1NFMP1ZOUxv8bYfvxkEBZLftbWWZpp8bvU6g%2BypyJ7ZSo2Yumk8THUtLSJNfr0yQfKOePJBnZyKecotuHG87n2J76BSpDJmhjT%2Bzb5JYoxZNWJeBUQW6%2F6vlax3%2Fxx45VvQ9UgAZBmIEkWF3yORfxsYIuNwVdFIUFNtmpsXrBtlBJktuU%2B298Op4seh3AXuPFeCJ1xYFPmUzFhwgow6Mnf1gY6pgE7yd7wdHSTu%2Fda1daisdL3ZJlUa9j9PcZm%2F2kPMkNmtRkWy56JpeOEU0zvedFwj7HkseF89gm8%2FzaxgVHHAXfHTQaILJuFYElqmcBEZex76JLFf5hEd6%2BqfdmpcN3nfslXTkyp8jkZXjWFbpgh1%2BFuu0r2AugbQYS0dIcQhBbBmCSqpoATSLGBbBdzKpTSve9uwFjqTkgBlX2u7AsHboAMPI6G3r1G&X-Amz-Signature=51429eccb03aab7ca49e5b2cef46d2e90a4b569269157e3cfa76b1259ad63333&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







