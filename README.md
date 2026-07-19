



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R4OODSE%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T080709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmzz3LHAVAMT95bI9dbhPx324N55iZY4G4d0DByT5YSgIgfMN%2Bxi9BJzE6QtIZJ%2BsupzRRfKJu0ALkAA5towpuBb0qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhsGJNA%2Fgs4tHoLhSrcAzfqQEEz%2FBysV8BKX%2FcUg9Ff4PC%2F4IMs7SXQrWoWYsJ5rR%2Bqy%2BW9%2BfzegXFAfLzJQI848khOcibfNVsCECs05EeAOTiVzBpelm76p3zRpxr4qKaPd6PAqjVq1E%2FmZjZ41TdsbNiOSwSWAXOO%2BxsVT7AeD0hd64Kh7mFmwmeP5OokjEy6GdnFedsu%2FQg2eXISUG5uZogPXqVaa0ywsg438gFNvrMji0IZY6tEp4sbwCtftWR1e%2BJRcYydeq6oI4u5aRyyG%2FGTpsH%2BPtToxRHQ9fNC1sOk1waxLHqYVpP8otqxUFWaz6pqjvUKWHlZJHUrYBKlKOvQRPCtN%2FrU7uPbxXxHWfVbya5KKjcdo36IBrG1Sya0ndUaopZxF4%2Fra2Um0UYE5jvaX2xvsY41Gus0bmCbgDVME0IMX5iN3ymqKLpKyBIffaCj%2F1ixzizTAmFESo8EfjEKCf%2BgFCoIbTy%2B5JlgQ7caiso90hK7ED84xzf7gxEi6hVl3%2FfI0nilpwqAkY3RoifrKhx%2Fv%2FVw3lyQAzHhAjgffB1YbqE8JMIvRBYEBM4LOxox3JRtNVUJTFdO%2BGk8J38k8q%2FuV%2Fkjo3eXhZn8rYh3R5LbTTyOrRb84XwPfKbnOnwLY3wfqC16MJfq8dIGOqUBn5r6U%2F%2FISlR5VDG466KcAbHJePzU6CapgYklLx3Y5Dy2FacPbAeGdAh4seUuyM9flpmDPjV4UmotD%2BOpD74J%2BQwYiTPhupIy30QMPhdE5FYZgfZwu9O4lQ6LauFR0jqoTgF9jnE3l6MRGNBYxTHGIzGpz2JtGMhBlivLsjFk087B0SlEBYtBGtIOVKQHfEYSfA6QcwJWckiZ6aNdXnnXjZ4IRSkc&X-Amz-Signature=d9d646bb43ad51d1e17737125aea851a8e2b267d6a66633e820cfb39cd5e3700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R4OODSE%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T080709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmzz3LHAVAMT95bI9dbhPx324N55iZY4G4d0DByT5YSgIgfMN%2Bxi9BJzE6QtIZJ%2BsupzRRfKJu0ALkAA5towpuBb0qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhsGJNA%2Fgs4tHoLhSrcAzfqQEEz%2FBysV8BKX%2FcUg9Ff4PC%2F4IMs7SXQrWoWYsJ5rR%2Bqy%2BW9%2BfzegXFAfLzJQI848khOcibfNVsCECs05EeAOTiVzBpelm76p3zRpxr4qKaPd6PAqjVq1E%2FmZjZ41TdsbNiOSwSWAXOO%2BxsVT7AeD0hd64Kh7mFmwmeP5OokjEy6GdnFedsu%2FQg2eXISUG5uZogPXqVaa0ywsg438gFNvrMji0IZY6tEp4sbwCtftWR1e%2BJRcYydeq6oI4u5aRyyG%2FGTpsH%2BPtToxRHQ9fNC1sOk1waxLHqYVpP8otqxUFWaz6pqjvUKWHlZJHUrYBKlKOvQRPCtN%2FrU7uPbxXxHWfVbya5KKjcdo36IBrG1Sya0ndUaopZxF4%2Fra2Um0UYE5jvaX2xvsY41Gus0bmCbgDVME0IMX5iN3ymqKLpKyBIffaCj%2F1ixzizTAmFESo8EfjEKCf%2BgFCoIbTy%2B5JlgQ7caiso90hK7ED84xzf7gxEi6hVl3%2FfI0nilpwqAkY3RoifrKhx%2Fv%2FVw3lyQAzHhAjgffB1YbqE8JMIvRBYEBM4LOxox3JRtNVUJTFdO%2BGk8J38k8q%2FuV%2Fkjo3eXhZn8rYh3R5LbTTyOrRb84XwPfKbnOnwLY3wfqC16MJfq8dIGOqUBn5r6U%2F%2FISlR5VDG466KcAbHJePzU6CapgYklLx3Y5Dy2FacPbAeGdAh4seUuyM9flpmDPjV4UmotD%2BOpD74J%2BQwYiTPhupIy30QMPhdE5FYZgfZwu9O4lQ6LauFR0jqoTgF9jnE3l6MRGNBYxTHGIzGpz2JtGMhBlivLsjFk087B0SlEBYtBGtIOVKQHfEYSfA6QcwJWckiZ6aNdXnnXjZ4IRSkc&X-Amz-Signature=65b534ed91f38b6e78dab4187102c887b1d09b88e72ab28a5807af9533ffc6da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







