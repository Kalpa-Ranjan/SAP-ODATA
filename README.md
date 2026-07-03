



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3SKMZCB%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T085436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQD6B21kLGIOlCZ4VLeyck6%2FSsK0DCq9f%2F4svAEc%2FrHcVgIhANf2KcOkCqHu1NiXqYozX8FrVL7gA3vRnZkUTj4OtJnRKv8DCAkQABoMNjM3NDIzMTgzODA1IgzBkZegRa%2Be2Yabw4Iq3APeNiE5AfmdQXt7lbhXd6IUFysqC%2FqJI6dQJ9ssl5oBxtVtj%2BRS%2FvKBlAA9AgJ2Cu7Y3eeNPFoHtvlVQk0EXCZxfc4%2FjV3qsVA37y6ORXxYq7wzTT69Fn3s5NyJDT%2FIi2pM2FivfjE5ykphEsbiTROozyWEU71iGypEYimJ6ZIRdT7urJ%2BHgoEvKKoWa81z84TXPxFwKbrzLMdq5rVW3khlBn1%2FRAek7XzIEdMOby5l0%2F0Cd%2Fg7VpY7bPciEKCOZRHANS4yzhPsH23IYp5Lh%2BqHDKaNeGWgaKtuRGY9zUFnVFaa%2Bqj6R%2Fax7hN7qkJWnJE%2BOD18SCYQMYqQs34jhfvnvRfEk05HVVIkvjDtRtVCRh7ejp9ED1xdneSif3JcFwnpbfjlKdFaAJ1%2B2nx2FECz3SoGco80OkcGpnv4oVBFEzpGlDxy5UTY4WtU6eb1Rkcu7G7VSkrEARhr3OZ3d2lG13GObJfrO5gSDKtqsqaltHSXPsxYkkrxbZ7C2Da2Gs4M52VCD5UwKEXkSjRfA1eActQwbJaOOGbxvpIXuWHMLnY3Wu3AD01kFb0gTifDOQBrGzgC3xYdOOhFHwOqv1QuDhsDp%2FKyqjdYEQGpIaMEefQGlQvpRxKEEorAhTDby53SBjqkAepZIlUS69rBVgLq4dBJ2KRk05%2BMq9craW%2Bp4gMFsrO9N6PC65lgG3FjxHpCWc%2FmW21LosTa5UP0v8KJF%2Fo3D9PuZm0nIQwuWNk%2FAEs1%2BvNJ1esEkQecHlp6PZYZcwTlhJYJFfWVyVcrI5892yWbIFK0DNvmjVxlqltfFcxXK1NrJ4prkq5oXKPS0osB28m67kOtUPQ8e5%2F6itkkvq97l1gFDoh6&X-Amz-Signature=ad49c64638440339c256dbe92bfccc70879ddeeac516c01e64e92033a0caf71d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3SKMZCB%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T085436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQD6B21kLGIOlCZ4VLeyck6%2FSsK0DCq9f%2F4svAEc%2FrHcVgIhANf2KcOkCqHu1NiXqYozX8FrVL7gA3vRnZkUTj4OtJnRKv8DCAkQABoMNjM3NDIzMTgzODA1IgzBkZegRa%2Be2Yabw4Iq3APeNiE5AfmdQXt7lbhXd6IUFysqC%2FqJI6dQJ9ssl5oBxtVtj%2BRS%2FvKBlAA9AgJ2Cu7Y3eeNPFoHtvlVQk0EXCZxfc4%2FjV3qsVA37y6ORXxYq7wzTT69Fn3s5NyJDT%2FIi2pM2FivfjE5ykphEsbiTROozyWEU71iGypEYimJ6ZIRdT7urJ%2BHgoEvKKoWa81z84TXPxFwKbrzLMdq5rVW3khlBn1%2FRAek7XzIEdMOby5l0%2F0Cd%2Fg7VpY7bPciEKCOZRHANS4yzhPsH23IYp5Lh%2BqHDKaNeGWgaKtuRGY9zUFnVFaa%2Bqj6R%2Fax7hN7qkJWnJE%2BOD18SCYQMYqQs34jhfvnvRfEk05HVVIkvjDtRtVCRh7ejp9ED1xdneSif3JcFwnpbfjlKdFaAJ1%2B2nx2FECz3SoGco80OkcGpnv4oVBFEzpGlDxy5UTY4WtU6eb1Rkcu7G7VSkrEARhr3OZ3d2lG13GObJfrO5gSDKtqsqaltHSXPsxYkkrxbZ7C2Da2Gs4M52VCD5UwKEXkSjRfA1eActQwbJaOOGbxvpIXuWHMLnY3Wu3AD01kFb0gTifDOQBrGzgC3xYdOOhFHwOqv1QuDhsDp%2FKyqjdYEQGpIaMEefQGlQvpRxKEEorAhTDby53SBjqkAepZIlUS69rBVgLq4dBJ2KRk05%2BMq9craW%2Bp4gMFsrO9N6PC65lgG3FjxHpCWc%2FmW21LosTa5UP0v8KJF%2Fo3D9PuZm0nIQwuWNk%2FAEs1%2BvNJ1esEkQecHlp6PZYZcwTlhJYJFfWVyVcrI5892yWbIFK0DNvmjVxlqltfFcxXK1NrJ4prkq5oXKPS0osB28m67kOtUPQ8e5%2F6itkkvq97l1gFDoh6&X-Amz-Signature=4a680d923e4e65031f2b9fd560f719c28de6b2e28c03956e068f0ca34c838996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







