



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXQUNRBT%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T011037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKJTyLHznzxsxJQ9x1KPpuCRvgWqYT1PZZfidKBOgT9gIhALOOP%2FO6FvrzPXQPP88Qzy39Eg%2Bn0EfRrqVTN2MI8y0DKv8DCGEQABoMNjM3NDIzMTgzODA1IgxLrUrHaM6zPVxxcXkq3AOkrR5u1DnVtd9dKLQpZAWY5N87vENZ6AeVznlx%2BFHaGvzQqfDXirTQj1m8aUZcpFRD0GbnScE61twGq0ebI7dAVbsXxhzn54a%2F9FY4TJszuwZxrXkoMchQ45ssSsch98XsjvTH2eBuF2zZ2KnVKvVZU%2BuxZ81PHfcMYpvmkQMWOcfhiolAgwk0Ob1708Jvn1xx6cvdnmSdAWRGCf4DIJPhHvJOLeNGjVb8YvWsYDQCq3dlrJ7gapNhX18TMo2rfi7cg9Oxsx3s8Nv4JfJKQU4lBEFvIvDxvqCR0mW8b7NuZzKowfE2hX6PHmuXTcxgAIzw2c%2F2yYY2MGzPysJsV2FP0H2mXXvQsBUWQ44NBokWiBtTTqq12LXGHpDEdvpvmqAbbDes0T6TNjOD5Vwiqh2PNjQ%2BLYGB2nuX1Nh0qYDwGiHm5AG%2FbsglxmTUTU3Hq8UatGt4aHIR%2B4qdTXuzj1hsw3Qtc0Cw2HHjBBhpfsqNtI7nIEoufrisQ8xSoDf7SEccL5S1m7zsT4D9uwTdpj%2FlFH%2Fu5IDL7uJjmAclRYAO06BeHHrXj1NAT1hifmUtpHba6PHGCsdVYsSi%2F9fNaKcwQ%2Fy4sjQb7kf8OFj0qChZIAv6ch63p4ribRZRszDb7NnTBjqkAeZeftLoKdW%2FC6ySDXOTSpcfVZMAIz7HwHr4n8E6Ohy5EZgAFgLgz7oJOJ%2BXjkU5q6oktTwZSuNja839ZKJZAJlUoA6NSMjceVHv0I12lS2i8QFvyQMjZMPRWd%2FKilTeYbLwtLz9R%2BH4YU1kFm7uyGRk6ggG9Oxwu9JpJMmHbwTPsOAN7nQhWwaaUWWIqcmOJefhR51R3vDWH5k7pcRpATHuJwU2&X-Amz-Signature=a76679baef90c5fe2fa2a7c55a7fe8844c2ef06d0621b7e6336c24e576fb9ca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXQUNRBT%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T011037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKJTyLHznzxsxJQ9x1KPpuCRvgWqYT1PZZfidKBOgT9gIhALOOP%2FO6FvrzPXQPP88Qzy39Eg%2Bn0EfRrqVTN2MI8y0DKv8DCGEQABoMNjM3NDIzMTgzODA1IgxLrUrHaM6zPVxxcXkq3AOkrR5u1DnVtd9dKLQpZAWY5N87vENZ6AeVznlx%2BFHaGvzQqfDXirTQj1m8aUZcpFRD0GbnScE61twGq0ebI7dAVbsXxhzn54a%2F9FY4TJszuwZxrXkoMchQ45ssSsch98XsjvTH2eBuF2zZ2KnVKvVZU%2BuxZ81PHfcMYpvmkQMWOcfhiolAgwk0Ob1708Jvn1xx6cvdnmSdAWRGCf4DIJPhHvJOLeNGjVb8YvWsYDQCq3dlrJ7gapNhX18TMo2rfi7cg9Oxsx3s8Nv4JfJKQU4lBEFvIvDxvqCR0mW8b7NuZzKowfE2hX6PHmuXTcxgAIzw2c%2F2yYY2MGzPysJsV2FP0H2mXXvQsBUWQ44NBokWiBtTTqq12LXGHpDEdvpvmqAbbDes0T6TNjOD5Vwiqh2PNjQ%2BLYGB2nuX1Nh0qYDwGiHm5AG%2FbsglxmTUTU3Hq8UatGt4aHIR%2B4qdTXuzj1hsw3Qtc0Cw2HHjBBhpfsqNtI7nIEoufrisQ8xSoDf7SEccL5S1m7zsT4D9uwTdpj%2FlFH%2Fu5IDL7uJjmAclRYAO06BeHHrXj1NAT1hifmUtpHba6PHGCsdVYsSi%2F9fNaKcwQ%2Fy4sjQb7kf8OFj0qChZIAv6ch63p4ribRZRszDb7NnTBjqkAeZeftLoKdW%2FC6ySDXOTSpcfVZMAIz7HwHr4n8E6Ohy5EZgAFgLgz7oJOJ%2BXjkU5q6oktTwZSuNja839ZKJZAJlUoA6NSMjceVHv0I12lS2i8QFvyQMjZMPRWd%2FKilTeYbLwtLz9R%2BH4YU1kFm7uyGRk6ggG9Oxwu9JpJMmHbwTPsOAN7nQhWwaaUWWIqcmOJefhR51R3vDWH5k7pcRpATHuJwU2&X-Amz-Signature=047e636710edfdc393d0858d3aefeb5f88a32a43a144f116a787654e7506e8b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







