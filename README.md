



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULVMIJFE%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T180905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIA3iOpwz%2FT0FZOnAN16w5bZiWKKWMWdcJBNtkBdxn7GhAiBAWxVLFygi9P86%2FImZ8oZmcy8x1CeMNmoh1%2Fcx5WVoeyr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMlWoqOAcfM27jKCYXKtwDnwZjBS8SxcCYMERorlEfxMe%2BJQWAtbrrirM96SvmcTiRWaUIVuuQh5IOBQNh5E7ci2MMLmJOrSbDrExDYIKbS%2BtXppZM7hXRpVuTjo06cD%2FflneK0gv4Q0b2Qhnplmf7R3%2FrbcGU5p31d18er2TWe%2FIyqzXYJ92FbtxO2w2udYzeEFFMEp0dFvy3uF2Go1n87tMIYgjhwhndqDaWTqifvtdhzHS9nAKADglhCGPiE20Rak71NbaiCSNL4DdejE%2Fdl9KRz3T3QZGZmEuu0FOMpoZyQCMGVqw9ya5pQHWRtp56bW9o8SMzUP9tRvHtXB15P14m%2FEUTrd4Wecq6P6XKQoF5HuONN4YrdNdoqJDKBuap1Hi9hOqDs9ByuEyryD2mV4vUEJC4J6fpStn6XVWETDTamxMdEW6GSMK7h%2Boyu81RcqAZyvWHzUXQ0z%2BDHCIk08scsarq22RGSQs37FprfR1%2FRW0BDNP8wi84JbU7aF7QNFBH9zhxP3m5TIHhDNVijBl1qJpm1Tm9z99Gk4mtctaysH98ilMBCmXxibLSMSjs7ER1sJo2%2FT1tIuZJV8I4%2Ba3W3DU%2B9VBp%2B1fUjonBntGPlNdbMqgxXxB%2BRpSzuBHyWutgaeVtNKgDx%2B4w3cj71AY6pgHBmNwnOHbNzRokqtOH8Hzl1U5h04konvkvoC01QIZsgo%2FvCav1RBpXoRIYVZRPDoHE83opyd7UuIFFb5pLIbL5yiowpZMqJ9ikqdUjRzLC4Eds04V6MPPEnMOeh00jNwmHfyKbmZ1IalrPna2lGqsomr0moWCrrYgStaj51S%2F6PFYOLIc8hzbsAJr1qoFdS2kFmYi1iML2sYRGGOCBZHQ%2Fi9THIwMH&X-Amz-Signature=aed7b591e18f4eb5f37d2ea20a2c9bfcb6fe15e38f956692fc81d7a8167b869a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULVMIJFE%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T180905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIA3iOpwz%2FT0FZOnAN16w5bZiWKKWMWdcJBNtkBdxn7GhAiBAWxVLFygi9P86%2FImZ8oZmcy8x1CeMNmoh1%2Fcx5WVoeyr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMlWoqOAcfM27jKCYXKtwDnwZjBS8SxcCYMERorlEfxMe%2BJQWAtbrrirM96SvmcTiRWaUIVuuQh5IOBQNh5E7ci2MMLmJOrSbDrExDYIKbS%2BtXppZM7hXRpVuTjo06cD%2FflneK0gv4Q0b2Qhnplmf7R3%2FrbcGU5p31d18er2TWe%2FIyqzXYJ92FbtxO2w2udYzeEFFMEp0dFvy3uF2Go1n87tMIYgjhwhndqDaWTqifvtdhzHS9nAKADglhCGPiE20Rak71NbaiCSNL4DdejE%2Fdl9KRz3T3QZGZmEuu0FOMpoZyQCMGVqw9ya5pQHWRtp56bW9o8SMzUP9tRvHtXB15P14m%2FEUTrd4Wecq6P6XKQoF5HuONN4YrdNdoqJDKBuap1Hi9hOqDs9ByuEyryD2mV4vUEJC4J6fpStn6XVWETDTamxMdEW6GSMK7h%2Boyu81RcqAZyvWHzUXQ0z%2BDHCIk08scsarq22RGSQs37FprfR1%2FRW0BDNP8wi84JbU7aF7QNFBH9zhxP3m5TIHhDNVijBl1qJpm1Tm9z99Gk4mtctaysH98ilMBCmXxibLSMSjs7ER1sJo2%2FT1tIuZJV8I4%2Ba3W3DU%2B9VBp%2B1fUjonBntGPlNdbMqgxXxB%2BRpSzuBHyWutgaeVtNKgDx%2B4w3cj71AY6pgHBmNwnOHbNzRokqtOH8Hzl1U5h04konvkvoC01QIZsgo%2FvCav1RBpXoRIYVZRPDoHE83opyd7UuIFFb5pLIbL5yiowpZMqJ9ikqdUjRzLC4Eds04V6MPPEnMOeh00jNwmHfyKbmZ1IalrPna2lGqsomr0moWCrrYgStaj51S%2F6PFYOLIc8hzbsAJr1qoFdS2kFmYi1iML2sYRGGOCBZHQ%2Fi9THIwMH&X-Amz-Signature=e9f5c4ea92a985cf09747c25a8af37107df0932a6ec64f0f0f57e4aefdeb03e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







