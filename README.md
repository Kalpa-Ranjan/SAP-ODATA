



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6LO7RBV%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T123616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIBASbVVLtiAue1nHwNSXjaRXXWAY1vBXqI9w%2F6Jr8xTPAiAxgohvbD%2BIH4J78PKGaOu%2BvFjnXwsPfctGLRfMZyDADCr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMH%2FSZ8jY771EmglnfKtwD84Uq5kex3FeVrIvIEnwqJNLGmTrwjsVNv8HBpowAGtU9Kghuh0jcOC0%2FkU5rYQrsSyYQrTyCKXm3E6l1hrq1BlqN66A7l6oP7JU8PNpXGHuHVkcnaS9aChxbpuwBdo7h%2Bx7rnlmJdYYAfhxd8sC6Yi7KgNkNISLLUxlZ%2FDAEqiE%2FnkoMRKQEGlOTCr8TwK34eWM9PEpa%2Bl9JojgeZ%2F%2FtT7LlEWOrNWXfR6DIjA7eG0aDu7kNYTJdiR34vA%2F0eQJh4OOACD2M3ODzRiNXh%2BoJ1QY5sU%2FZ1F3o51rkqMwBnK2%2BR%2Fpx6jbef1JOMh49laVDGWtmHRLVy6dGbaDDRNdhA4BrfZ667Ovwo1aT6bJyC3Rpa3wdH%2FLw41oEm%2BQF2cIU7An5QeAz619EZ55RAHszQCXZHNKZgbpxbBTyineDOwHjPdEZwQGnXbtSYluTSByck4X4%2FdoeeojySJXAXopORL57IuJh5ZqL9j2jZQXqoGTZTwjpABBfVQcr4p9Ov%2Bl%2BL3Q29n%2BRbGxNaSoxRSmGgbwwsrXE%2BkdiZHbPit%2BByoOkfHDhAxBYMEuml1A16jkim6EToumCEqsThl%2FMS2oW1yLioPZh4Kuo6LJoYjFJlVcoSBicj%2B3HKHn9GiMwzrejywY6pgEGRh3EeDUoE0x%2B155p60ZcJwHrY64MjFQMpZ27zCUPz%2Fw%2BLTVUeAKwT8syCjxE7QLeJbP%2BlN2iHpHWwjuU5GhriIC6Tr4zILoapAbLN2R70GafUCtrUyJrBoPTDm0YvRFtWnDGRakACrvX5x%2BRYkv%2FKG4OwPzIFWv1GSBIsJ%2Foe4hCCxgROrVuZpv02Dg1JSv2CnScBxDrqa9ZVSJpqeHFmPo4%2Funi&X-Amz-Signature=ac69cd3deace27201158666a5969d28d87db0d41b04028dbf9b7d611b6bc0768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6LO7RBV%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T123616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIBASbVVLtiAue1nHwNSXjaRXXWAY1vBXqI9w%2F6Jr8xTPAiAxgohvbD%2BIH4J78PKGaOu%2BvFjnXwsPfctGLRfMZyDADCr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMH%2FSZ8jY771EmglnfKtwD84Uq5kex3FeVrIvIEnwqJNLGmTrwjsVNv8HBpowAGtU9Kghuh0jcOC0%2FkU5rYQrsSyYQrTyCKXm3E6l1hrq1BlqN66A7l6oP7JU8PNpXGHuHVkcnaS9aChxbpuwBdo7h%2Bx7rnlmJdYYAfhxd8sC6Yi7KgNkNISLLUxlZ%2FDAEqiE%2FnkoMRKQEGlOTCr8TwK34eWM9PEpa%2Bl9JojgeZ%2F%2FtT7LlEWOrNWXfR6DIjA7eG0aDu7kNYTJdiR34vA%2F0eQJh4OOACD2M3ODzRiNXh%2BoJ1QY5sU%2FZ1F3o51rkqMwBnK2%2BR%2Fpx6jbef1JOMh49laVDGWtmHRLVy6dGbaDDRNdhA4BrfZ667Ovwo1aT6bJyC3Rpa3wdH%2FLw41oEm%2BQF2cIU7An5QeAz619EZ55RAHszQCXZHNKZgbpxbBTyineDOwHjPdEZwQGnXbtSYluTSByck4X4%2FdoeeojySJXAXopORL57IuJh5ZqL9j2jZQXqoGTZTwjpABBfVQcr4p9Ov%2Bl%2BL3Q29n%2BRbGxNaSoxRSmGgbwwsrXE%2BkdiZHbPit%2BByoOkfHDhAxBYMEuml1A16jkim6EToumCEqsThl%2FMS2oW1yLioPZh4Kuo6LJoYjFJlVcoSBicj%2B3HKHn9GiMwzrejywY6pgEGRh3EeDUoE0x%2B155p60ZcJwHrY64MjFQMpZ27zCUPz%2Fw%2BLTVUeAKwT8syCjxE7QLeJbP%2BlN2iHpHWwjuU5GhriIC6Tr4zILoapAbLN2R70GafUCtrUyJrBoPTDm0YvRFtWnDGRakACrvX5x%2BRYkv%2FKG4OwPzIFWv1GSBIsJ%2Foe4hCCxgROrVuZpv02Dg1JSv2CnScBxDrqa9ZVSJpqeHFmPo4%2Funi&X-Amz-Signature=e817aaf9b32bd195d0e8f664fa634d1292c2070bcc52f3fe1d9f1f9998cb1b9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







