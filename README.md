



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUXGTXTQ%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T082641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6O7uuLCYEwEKEIJn0FKTVypwTMnDREZLZhb1l%2FVblCgIhAMdebLzdVkxjH75utvc1j%2FUEq6UtiHOboF63GrzNswI0KogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6Hm6VKmK%2BQQ8e3mkq3APe%2BYc365LwZ43D6uicVGkD%2FALSH2goYFhE2KzJNmmUxvRhSC%2BfQPRNlPI%2BYX9jGpADCRa1uMzVn3Ekx%2FlIH%2BUEHjqQBVY54CYC4idoVQrFoHQ3kCsLw%2BekUs4B9ZEnnKPFyMYbSIFWAujdkRKQzdaq1Xq6i2hJXQ3cFAHvbJWD2L0QTEF3lPoevlqLviz8LHPekvjRnZL9OumGCjmLqw3pHQ54K4dVK4p3Ep7fV7IS2e7JDLSOCrc0vbYmpqBKdt%2FSBzh7zd7oNGZ2gt3Ky5ZShVkBguH2h66Rlw%2FgGB1dN%2B0QNrVgdUCO7bLTHuE%2BCGO1QttFDNxp95ncKoNnoH1NlDdZ2YBWIxJW8LMgPnp0LoO6NIVBGEQoS4DTtrymUp10KwGQXk5BY0wewapmb1we4jKCwHPt0QtiXxTUpfOMhash3X4WL3lKzZFH9NXQxcqjGMZ5Ofk3NBC0id6cuW3AwUn82Z7GPIo55t3G5rNLv%2FuJ%2Bj4gBT%2BvmWfN1DKzlMaBSHzYylF49fZAU1ccYqzYXaXjm4%2Fw6g0QGkBhdaJm60MkIMZhX5mfjd8J1oAtiA%2Fmm%2FvGacyLiZJhy0yFIsBMflpDmOzG2%2F%2BOn8FPKXEqtSpHE%2BOaKmAqDcMPxTDZ2%2FDPBjqkAZk8IQya17cmIVyZkzyw4bjgzsaD%2FwJIfwi6fNe8B9bkr9Go0W6GuSeF89gcghD20e9u6Le%2F9WEJKAYZVJGX2LqTdI8oUqrsUUqn0qDYN7yZyZtVzjMiBuGh843OYqZcdyZS%2BTZRz2Drs62F6kSK7YUpyI2f%2Fl9HEvFKLMEepwN1aTDqY9W3nUYA8etiDDalfRpSB4MojvFJU%2FLAEFnpdysCgM%2FH&X-Amz-Signature=54b3bdd0a51de06333ca686a1fc27c93d778c370b15e805bd1ad84e79be2aa46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUXGTXTQ%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T082641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6O7uuLCYEwEKEIJn0FKTVypwTMnDREZLZhb1l%2FVblCgIhAMdebLzdVkxjH75utvc1j%2FUEq6UtiHOboF63GrzNswI0KogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6Hm6VKmK%2BQQ8e3mkq3APe%2BYc365LwZ43D6uicVGkD%2FALSH2goYFhE2KzJNmmUxvRhSC%2BfQPRNlPI%2BYX9jGpADCRa1uMzVn3Ekx%2FlIH%2BUEHjqQBVY54CYC4idoVQrFoHQ3kCsLw%2BekUs4B9ZEnnKPFyMYbSIFWAujdkRKQzdaq1Xq6i2hJXQ3cFAHvbJWD2L0QTEF3lPoevlqLviz8LHPekvjRnZL9OumGCjmLqw3pHQ54K4dVK4p3Ep7fV7IS2e7JDLSOCrc0vbYmpqBKdt%2FSBzh7zd7oNGZ2gt3Ky5ZShVkBguH2h66Rlw%2FgGB1dN%2B0QNrVgdUCO7bLTHuE%2BCGO1QttFDNxp95ncKoNnoH1NlDdZ2YBWIxJW8LMgPnp0LoO6NIVBGEQoS4DTtrymUp10KwGQXk5BY0wewapmb1we4jKCwHPt0QtiXxTUpfOMhash3X4WL3lKzZFH9NXQxcqjGMZ5Ofk3NBC0id6cuW3AwUn82Z7GPIo55t3G5rNLv%2FuJ%2Bj4gBT%2BvmWfN1DKzlMaBSHzYylF49fZAU1ccYqzYXaXjm4%2Fw6g0QGkBhdaJm60MkIMZhX5mfjd8J1oAtiA%2Fmm%2FvGacyLiZJhy0yFIsBMflpDmOzG2%2F%2BOn8FPKXEqtSpHE%2BOaKmAqDcMPxTDZ2%2FDPBjqkAZk8IQya17cmIVyZkzyw4bjgzsaD%2FwJIfwi6fNe8B9bkr9Go0W6GuSeF89gcghD20e9u6Le%2F9WEJKAYZVJGX2LqTdI8oUqrsUUqn0qDYN7yZyZtVzjMiBuGh843OYqZcdyZS%2BTZRz2Drs62F6kSK7YUpyI2f%2Fl9HEvFKLMEepwN1aTDqY9W3nUYA8etiDDalfRpSB4MojvFJU%2FLAEFnpdysCgM%2FH&X-Amz-Signature=97d1809ae57bb728e5b62d1807aaaac9340e32b8b5e0985709eb09b3700dce80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







