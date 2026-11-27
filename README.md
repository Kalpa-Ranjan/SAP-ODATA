



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGT6PVBJ%2F20261127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261127T120732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDD4x2js9UwGvydmUnq3f%2BrZ2bULLAq4yJYXpemZhcLCwIgXMywplsnFVQ5e6UZgdQdEENwuzdGDInfkqLVxpbSj5QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnSCm2l9A7uuhcftSrcA7TvmM2mRUqw%2FqwgAbQTmzzU2ppA5zko%2B7lNGlX0xJX6nk2FIC07Gkp0B2%2BTg9XhIA7Pftlcr4rucv6jU7KJROFNlGuAWBrpgQ3x4ICIE63MOpmfq1wKdQys4GerOKReyofw9lyhvGvA7kIGG2GoaC2HWWdMvj8dy5y2QXl%2BnYspW2di0Fv8NlHmJZjhkIRHvm51eKUU1mCGM0YOm3jdhOcPGywcjuW8Qlmkqn2j78x1BBuk2%2BCdsYTTB7XcFkXJMg3qV8ePg33TJN1xTDaCpdpl1BuPilpszcWeMphcU%2FfNLzegyaynfIeLHn83y72WK56Tlam%2BoZheGCRNSqT%2F7sgC7aagSojNMqPHRJAy0kWlX4AXzFShwaWBsK9Z2P67gGJWS5qQfZqU9Qm5XtCf5SBih%2FMhiJtCyJpO%2FECxh4wg3Bcpdw1k2Mgd87FoJ6y0sCS0o%2FNZlYSwUoKDwxXp1aXYJnKw2xjaHA96JT7J65wzHPIS4OnQiNqPatKW5YG1QZCX%2BoRsIDBrc6qHPV2uGprd0WkYWzPfu2Hn6Vb1FTC2AgmA9SruuO2T0TZDTi0qIV2vZqbLQ%2FO1k%2Bb2%2Fjx996HDFylQJOVF6Ja%2Bz05ZBafCLotHdOy6lL5vErARMPyDpdgGOqUBQ0WuFS1tGVd83wnxJPOXdvAtK90BXzw1PPbNK4L9pQrU6RXVaJdn8vs8HAULhT6a4UHSd5wydswe97KJSEy0bzqLlkEoxPZ0zxIzL6MrZFVvVO3A%2BPn4tLGbRjZpAAqYXiowsQyFIQqrCDPwOaLoBb8JYEXPu6XBbzEoOkttkukSnnaT9veKaKqg78Mev8Ho3l4eL5Exa1%2FtMw3TPQ20ihdfWow2&X-Amz-Signature=5e0c85c3f66e3291e5cbc6da74b626a3b714f5f2afadcf293e229d50b2ed426d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGT6PVBJ%2F20261127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261127T120732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDD4x2js9UwGvydmUnq3f%2BrZ2bULLAq4yJYXpemZhcLCwIgXMywplsnFVQ5e6UZgdQdEENwuzdGDInfkqLVxpbSj5QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnSCm2l9A7uuhcftSrcA7TvmM2mRUqw%2FqwgAbQTmzzU2ppA5zko%2B7lNGlX0xJX6nk2FIC07Gkp0B2%2BTg9XhIA7Pftlcr4rucv6jU7KJROFNlGuAWBrpgQ3x4ICIE63MOpmfq1wKdQys4GerOKReyofw9lyhvGvA7kIGG2GoaC2HWWdMvj8dy5y2QXl%2BnYspW2di0Fv8NlHmJZjhkIRHvm51eKUU1mCGM0YOm3jdhOcPGywcjuW8Qlmkqn2j78x1BBuk2%2BCdsYTTB7XcFkXJMg3qV8ePg33TJN1xTDaCpdpl1BuPilpszcWeMphcU%2FfNLzegyaynfIeLHn83y72WK56Tlam%2BoZheGCRNSqT%2F7sgC7aagSojNMqPHRJAy0kWlX4AXzFShwaWBsK9Z2P67gGJWS5qQfZqU9Qm5XtCf5SBih%2FMhiJtCyJpO%2FECxh4wg3Bcpdw1k2Mgd87FoJ6y0sCS0o%2FNZlYSwUoKDwxXp1aXYJnKw2xjaHA96JT7J65wzHPIS4OnQiNqPatKW5YG1QZCX%2BoRsIDBrc6qHPV2uGprd0WkYWzPfu2Hn6Vb1FTC2AgmA9SruuO2T0TZDTi0qIV2vZqbLQ%2FO1k%2Bb2%2Fjx996HDFylQJOVF6Ja%2Bz05ZBafCLotHdOy6lL5vErARMPyDpdgGOqUBQ0WuFS1tGVd83wnxJPOXdvAtK90BXzw1PPbNK4L9pQrU6RXVaJdn8vs8HAULhT6a4UHSd5wydswe97KJSEy0bzqLlkEoxPZ0zxIzL6MrZFVvVO3A%2BPn4tLGbRjZpAAqYXiowsQyFIQqrCDPwOaLoBb8JYEXPu6XBbzEoOkttkukSnnaT9veKaKqg78Mev8Ho3l4eL5Exa1%2FtMw3TPQ20ihdfWow2&X-Amz-Signature=234eaae11e14c1dd47d7a3123d01cc15686b2eb054b0e17b79c41a6f776c2843&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







