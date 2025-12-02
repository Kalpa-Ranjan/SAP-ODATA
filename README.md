



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKA7BCIM%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T182611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCWH7068xPrEEl3d%2BB9h%2FxoVl%2FHZaw13NAn9IVbW%2B%2F68QIge0Yp4kxsNDUiTQPDXMBkh620M9wnjbho2zHfQXO7GTsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDIqBKNdejEOW%2B9uhEyrcA7K17JKvWIeSQia04RWcigmiO5qnamqH2%2BxBi3WD6eo111b2%2B1buedtUJN6LYuDy7z8bHiWKbiZHkcwu48rXYryKZ5m2VCRhj60AROPhazrKUfSbTKJOm1v23pk7YNl6qL5F40F6AjQSqig8%2FCp6ejHXKzHceTYblsPUOOFsLes5Ox4U3b3wJzo88ZsBWq2uGUuPdpKZ5CPjPpAqkWsNfO9HBmD7RTG7a8ll0BYaDLcEZtP%2BNoUYdMnZr%2Biym3GDjRcwUzQRNnHZKFswrZ0BczI6DrrWYjaNJGRYt47OV1QofMyJ%2BI%2BZ4T4KYsITqtrfFr7IYS5RgnbFIb3P14%2BrXDcjzp2znv0yBYVu3uO62WPMAEj%2F6lBOS2R%2FrAoPgMjot03aZLlXRZVZv7mj1mnTl3%2FphZXyneeuxEEV2%2FRJKK%2FjjymQlK5aKW7B1fQ8W1Gfq41d1L4qS8MjyscQ4o%2FgPYTZeGRcwEUPwkWs1bQK841fHeit%2FpuYAiIVUCol6Exfa%2BprQLAzwa6jDniF7qgCie6Lw%2B9%2Fhs33Rr0afjOI%2FnzddB%2BPPn0DEXbittwdb11%2BMURdJRKvs2ONjOF9ezJ63ke7%2BN0XKAJYjwxEBwVewlEyfpDXFly5em8t30M7MLjRvMkGOqUBCTh%2B%2F6NcjO7828KMa3yMPw1dTzKxT1EPRSbEInSTEQdhGVhSeb27t8CO1tXKh7e8WW5fdcRcd6CeM5JSUIp0YAwf1tYohhE7aqmA%2BjV6OSQeKnN9VZIaYjBj61o9NIMmrvWSXC6XlQxMp8V7N3DErfUaMWIliVM6%2Bz6r3swIqLnzBL2cNRc6HcoVzqmWMQ7bv%2F%2FBW%2B3WazE5Kv6stdPx%2B5twYW0r&X-Amz-Signature=b1a4b9efa527da854aee7045aac30f30069a449a23f93a4d25547aec03b20274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKA7BCIM%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T182611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCWH7068xPrEEl3d%2BB9h%2FxoVl%2FHZaw13NAn9IVbW%2B%2F68QIge0Yp4kxsNDUiTQPDXMBkh620M9wnjbho2zHfQXO7GTsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDIqBKNdejEOW%2B9uhEyrcA7K17JKvWIeSQia04RWcigmiO5qnamqH2%2BxBi3WD6eo111b2%2B1buedtUJN6LYuDy7z8bHiWKbiZHkcwu48rXYryKZ5m2VCRhj60AROPhazrKUfSbTKJOm1v23pk7YNl6qL5F40F6AjQSqig8%2FCp6ejHXKzHceTYblsPUOOFsLes5Ox4U3b3wJzo88ZsBWq2uGUuPdpKZ5CPjPpAqkWsNfO9HBmD7RTG7a8ll0BYaDLcEZtP%2BNoUYdMnZr%2Biym3GDjRcwUzQRNnHZKFswrZ0BczI6DrrWYjaNJGRYt47OV1QofMyJ%2BI%2BZ4T4KYsITqtrfFr7IYS5RgnbFIb3P14%2BrXDcjzp2znv0yBYVu3uO62WPMAEj%2F6lBOS2R%2FrAoPgMjot03aZLlXRZVZv7mj1mnTl3%2FphZXyneeuxEEV2%2FRJKK%2FjjymQlK5aKW7B1fQ8W1Gfq41d1L4qS8MjyscQ4o%2FgPYTZeGRcwEUPwkWs1bQK841fHeit%2FpuYAiIVUCol6Exfa%2BprQLAzwa6jDniF7qgCie6Lw%2B9%2Fhs33Rr0afjOI%2FnzddB%2BPPn0DEXbittwdb11%2BMURdJRKvs2ONjOF9ezJ63ke7%2BN0XKAJYjwxEBwVewlEyfpDXFly5em8t30M7MLjRvMkGOqUBCTh%2B%2F6NcjO7828KMa3yMPw1dTzKxT1EPRSbEInSTEQdhGVhSeb27t8CO1tXKh7e8WW5fdcRcd6CeM5JSUIp0YAwf1tYohhE7aqmA%2BjV6OSQeKnN9VZIaYjBj61o9NIMmrvWSXC6XlQxMp8V7N3DErfUaMWIliVM6%2Bz6r3swIqLnzBL2cNRc6HcoVzqmWMQ7bv%2F%2FBW%2B3WazE5Kv6stdPx%2B5twYW0r&X-Amz-Signature=87217741f20c278221bbfb93376f5f61e549b936ba3d4e64f30ee3b73a76786b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







