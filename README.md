



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FXBVAV%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T093149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIANytVtTX1JpNBtvyoBIou2rxlM5CEMycXZ0Tzq5z6wVAiARYGPkez4nM8l9Dca7h5DRZTbp74jn7%2F2nlPLAMj9p9Cr%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIMQp89Ma2zZ%2Fn0LiqEKtwDmm8dpg1VytU41o763ZFEIOWTTQJTkEwJX9IzcNaCU5cN5juTAEYCVC88HWeWCOj9xpxOIs5nS19mmdwS4JUIE2FL9e1h6SKO2flXBUtGuiKCGNSbiCy7f4pX2CQHnEhB%2B1A%2B4FhmHUXIvtYc0wqPfNb4XU8r4%2F39KLuMp72oShitb%2BRHIvphfiBCh3ObwDYe4kWIA4wgS6P5KIfZzcRqIWjTAZ21ksN2DeHIaf1rS%2FENTjKTIoq3HF%2B5%2B6PogiyGnnbD7nK8B81q7NGZuPlfo2%2Bu%2FS89j9Wkpx6AbwEz0h22ZD5JCmbPu4z6frejJvgN04lCw8dpjjz8Z9hkd6ZxrF4hqIjTQQpU8QuVbOpDhzoP%2F4bpkGR07bjjvqSIKI8pzCZs4n9nYqObiTyKqelu55M%2FTao%2BykuMk29pr26Ufrh8ub0QV7CyR4q696aHWVLgc5ogfJelhOCKFHggOc3Cxp%2FmfqS%2B87wNn%2BoqFKrziMGRHzoXLHO%2FSVTX%2F2Ihjnfr4nF%2BADF4tqLGd1e7DeCbfOzYmSY0SFFVtjRsnN%2FxdkVIJrxn%2F19eeQA1x9309DTyr2qu5bSAz43vAckB81BenIQchMMnE61lBfp2pzojAbZuR1fKtYfi%2FAps6sgwu4iz0gY6pgGusD83QIBKYLk%2BW0p2vm9Bf8qke2yAVkERZ1FaB2AJKeGIr4gIypf8lagm6aduQSqY%2BBFBbe%2FU4K2mUUhNhztpoJhDqWaKICJyZCeLIarUfxhDEq9sHww%2Foo8rBsa94SjmCXl2BMfKIZMtoz8x71fSYOX64Sx3cflUictLHQxJJ7PhSpr0QYJ8nYAXagyg5mUhhxsuw%2BsSTh9Y2d1scnoherHf3Gx%2F&X-Amz-Signature=52e63fb3dc35aa5b3aae63985140bcde5ad363253330dde6df6b2ebd6da6f145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FXBVAV%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T093150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIANytVtTX1JpNBtvyoBIou2rxlM5CEMycXZ0Tzq5z6wVAiARYGPkez4nM8l9Dca7h5DRZTbp74jn7%2F2nlPLAMj9p9Cr%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIMQp89Ma2zZ%2Fn0LiqEKtwDmm8dpg1VytU41o763ZFEIOWTTQJTkEwJX9IzcNaCU5cN5juTAEYCVC88HWeWCOj9xpxOIs5nS19mmdwS4JUIE2FL9e1h6SKO2flXBUtGuiKCGNSbiCy7f4pX2CQHnEhB%2B1A%2B4FhmHUXIvtYc0wqPfNb4XU8r4%2F39KLuMp72oShitb%2BRHIvphfiBCh3ObwDYe4kWIA4wgS6P5KIfZzcRqIWjTAZ21ksN2DeHIaf1rS%2FENTjKTIoq3HF%2B5%2B6PogiyGnnbD7nK8B81q7NGZuPlfo2%2Bu%2FS89j9Wkpx6AbwEz0h22ZD5JCmbPu4z6frejJvgN04lCw8dpjjz8Z9hkd6ZxrF4hqIjTQQpU8QuVbOpDhzoP%2F4bpkGR07bjjvqSIKI8pzCZs4n9nYqObiTyKqelu55M%2FTao%2BykuMk29pr26Ufrh8ub0QV7CyR4q696aHWVLgc5ogfJelhOCKFHggOc3Cxp%2FmfqS%2B87wNn%2BoqFKrziMGRHzoXLHO%2FSVTX%2F2Ihjnfr4nF%2BADF4tqLGd1e7DeCbfOzYmSY0SFFVtjRsnN%2FxdkVIJrxn%2F19eeQA1x9309DTyr2qu5bSAz43vAckB81BenIQchMMnE61lBfp2pzojAbZuR1fKtYfi%2FAps6sgwu4iz0gY6pgGusD83QIBKYLk%2BW0p2vm9Bf8qke2yAVkERZ1FaB2AJKeGIr4gIypf8lagm6aduQSqY%2BBFBbe%2FU4K2mUUhNhztpoJhDqWaKICJyZCeLIarUfxhDEq9sHww%2Foo8rBsa94SjmCXl2BMfKIZMtoz8x71fSYOX64Sx3cflUictLHQxJJ7PhSpr0QYJ8nYAXagyg5mUhhxsuw%2BsSTh9Y2d1scnoherHf3Gx%2F&X-Amz-Signature=094093d20f04a144aa0b9aa95debc121b0db789c8bb3daf042d51ee77246524e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







