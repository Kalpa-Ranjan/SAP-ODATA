



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TINZPOY%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T190541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCUw1OJvLszMQZM6zjTvz3Qby5nZVO8EBla6tgkKsJkTwIgEpw9SAY1mlZZFDRHQLQ95lKAlzTVdOxKefhbMnkMGVQqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJp7vXXysWsdsQeGEyrcAxah%2BvF1MSwnKabOQiIKin11w0zLYtkEAf%2Bbr2uyG6SacDhpxZp2oEPT3eLnXGDH0R1UV1guJQl8f4BCfzOKAssi8eFvW8LfM4CaY3AfGvE232xSs4xuvZpXod6Ek0ufCxvB0Jfg6L2uA0ucTwgccmaW0i%2ByU4B6HoAKHBp4zozIYdnad1TCZATsIX1F0PiERo5RFkl5MJbEEnS0Vz6FaOiXDUDiT%2FvkOQYL9wJTAgwiOILu3DPT0xwmDXxqMTF4P9ELCpmnlAyFd4J%2Fm2N2c0nBK64U8Fv1vxaw7%2BZs3nlYTh01lo22Ci2rcSpOjyS4AB8wux7MapFkk%2BC9M%2BwHPQjYLoY9x5iqCrXogY6FlnwZ5UXSpjs%2B7Llidnyw9Do7PgJeNvYJi0LKMctw16xQxGN0QKNgUGrozaHVeIzbS%2F%2FamiW7WwA1QVGYurivFrc5PeNNwypUwrIQ6Qd8WoApdITfo3ZjRsVeBQrSd2zkfB%2Bgb9jQaYGlFr3MrRdqqYmSwCk7fj0jqSdAnLuwt2KwuOEnQ9QdpmHuaSnJRHgPfumlQnq0Focj68XU17FMgtRXbG9Yn9so33VmarPCDwga33MDDxcerg8nO3%2BQNrodHab%2FYZ7uDjgrQHJnO5b2MOPvg9MGOqUBC35V3Gz4Q%2BdtZb3hWcFHDWb0%2BKQbjwJ9APbyvSyVoE%2FcRcyQt5Iu2dDDiH4AnG5QTclhMOFZ9rRIPmZZEubox2T1KbLyCSkHwas6CQ4ON1LPyIBUAUwahquV4RnfwG85bsF41zUXsfYTty%2BFnfPTyLaA%2F8oysG6gX5PjeciCwq9eM37PWS5NGOh%2FWQy4RD1XL0tjEQEcYfYijMrOXRAhrUbh%2FgQV&X-Amz-Signature=b9597ecaa29060c3e1c1a0900ea02d8dbb1da1b555ad92c1b2226fda7b52d343&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TINZPOY%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T190541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCUw1OJvLszMQZM6zjTvz3Qby5nZVO8EBla6tgkKsJkTwIgEpw9SAY1mlZZFDRHQLQ95lKAlzTVdOxKefhbMnkMGVQqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJp7vXXysWsdsQeGEyrcAxah%2BvF1MSwnKabOQiIKin11w0zLYtkEAf%2Bbr2uyG6SacDhpxZp2oEPT3eLnXGDH0R1UV1guJQl8f4BCfzOKAssi8eFvW8LfM4CaY3AfGvE232xSs4xuvZpXod6Ek0ufCxvB0Jfg6L2uA0ucTwgccmaW0i%2ByU4B6HoAKHBp4zozIYdnad1TCZATsIX1F0PiERo5RFkl5MJbEEnS0Vz6FaOiXDUDiT%2FvkOQYL9wJTAgwiOILu3DPT0xwmDXxqMTF4P9ELCpmnlAyFd4J%2Fm2N2c0nBK64U8Fv1vxaw7%2BZs3nlYTh01lo22Ci2rcSpOjyS4AB8wux7MapFkk%2BC9M%2BwHPQjYLoY9x5iqCrXogY6FlnwZ5UXSpjs%2B7Llidnyw9Do7PgJeNvYJi0LKMctw16xQxGN0QKNgUGrozaHVeIzbS%2F%2FamiW7WwA1QVGYurivFrc5PeNNwypUwrIQ6Qd8WoApdITfo3ZjRsVeBQrSd2zkfB%2Bgb9jQaYGlFr3MrRdqqYmSwCk7fj0jqSdAnLuwt2KwuOEnQ9QdpmHuaSnJRHgPfumlQnq0Focj68XU17FMgtRXbG9Yn9so33VmarPCDwga33MDDxcerg8nO3%2BQNrodHab%2FYZ7uDjgrQHJnO5b2MOPvg9MGOqUBC35V3Gz4Q%2BdtZb3hWcFHDWb0%2BKQbjwJ9APbyvSyVoE%2FcRcyQt5Iu2dDDiH4AnG5QTclhMOFZ9rRIPmZZEubox2T1KbLyCSkHwas6CQ4ON1LPyIBUAUwahquV4RnfwG85bsF41zUXsfYTty%2BFnfPTyLaA%2F8oysG6gX5PjeciCwq9eM37PWS5NGOh%2FWQy4RD1XL0tjEQEcYfYijMrOXRAhrUbh%2FgQV&X-Amz-Signature=510b59e3c6a14b92088481ec66b939187b0fa123a75916e5ba3869f0765d6a76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







