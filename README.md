



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYDBFCZG%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T191709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoveYaYw0UF2Kn1iLekHdqql12x4PZH90%2F9RNHxrq59AiBr9kG5Lm2ZrmfHpcoRhbRJtxgFRQKb4qD4FsA06wIjSiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMChbfDv47U1Sv7IP8KtwDJ4s9qwOnGGYLs20sFjcLLUs9V6%2BsAFXjHqAAB%2B6qKx4eTtfFKlEeqdNC%2BVjOUyzDIY3qLpWZw9jjqo6DuVpa%2BiMEwZf%2F0QoCEWJMu2z0Q%2FJIdX3uVPiu1J8bhJrDRvNqRl%2BB4%2BheWiEdMIH8n%2FbjfnkpoYt79u4SgZWDav2cF246ChEO%2FxaUWOAKf5TsMe2I0v1h1UPsdZa0R9Wz5WCMjaOJQTzpJWXDAdpdaJcAHPlHmd2miX3PwluGfh%2F8vX%2FLDBntsoT39EiKxeahFL9n3WeR%2Fe0bN1G7iKcwFbfXGcXNUCRl6%2FW1RARRkE7OSEezQoHb6e7kpeLqNU%2FjAZEi%2BCfMx4TJibcV7OCT8tYwjtzsdpmhJrZ6JouMbbEL1L10YSR8y%2FR46k89VgLRuYhqHkL3e75xLCDNO%2Bj1hOLF26%2FzWaU7W5oP0H3WwS8StwLep%2BRxduMYi1lRA90VRin3BOP%2BhH18IjGSQCMOaY4VnZXXrJG8vfUbv%2FvhWFA83co2M00FUn66vIS1DnXX%2Fkj0Owwz9SWcPkPJYq7UMtEvB0RNSZYqwZqg9MnqoaKmVQcshackZy2H8M84ebR%2BluHuYIVuVLVAKz%2Fm3emkd1%2Fegvht9E7QuK6jXKzeWoAw0LOu0wY6pgG6L8Ruuvd7N%2FvD1JLgZ10WKjVwkilUMtulZfkONkkPrAD3PM0SbMXPakuUriqqYmpOKaRu%2B7rvuNZBfo5YxLX7xUaopNgfzsQbJ80DoLtojCN%2BhENjMQHg2Gh7NNApvnfmZ478YfvDVHUmAKHXCUOkrtYZBCFfpUMnHsQ5e1Y9eRTRoy5ryUICg6XFGsBRtq%2BYMv9EmZYle9voy%2BiF5LFNB8nsKxaP&X-Amz-Signature=6b0e755831356e7e54223e721f1b2e10aca4297e792d583aafb824ee22d26c5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYDBFCZG%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T191709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoveYaYw0UF2Kn1iLekHdqql12x4PZH90%2F9RNHxrq59AiBr9kG5Lm2ZrmfHpcoRhbRJtxgFRQKb4qD4FsA06wIjSiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMChbfDv47U1Sv7IP8KtwDJ4s9qwOnGGYLs20sFjcLLUs9V6%2BsAFXjHqAAB%2B6qKx4eTtfFKlEeqdNC%2BVjOUyzDIY3qLpWZw9jjqo6DuVpa%2BiMEwZf%2F0QoCEWJMu2z0Q%2FJIdX3uVPiu1J8bhJrDRvNqRl%2BB4%2BheWiEdMIH8n%2FbjfnkpoYt79u4SgZWDav2cF246ChEO%2FxaUWOAKf5TsMe2I0v1h1UPsdZa0R9Wz5WCMjaOJQTzpJWXDAdpdaJcAHPlHmd2miX3PwluGfh%2F8vX%2FLDBntsoT39EiKxeahFL9n3WeR%2Fe0bN1G7iKcwFbfXGcXNUCRl6%2FW1RARRkE7OSEezQoHb6e7kpeLqNU%2FjAZEi%2BCfMx4TJibcV7OCT8tYwjtzsdpmhJrZ6JouMbbEL1L10YSR8y%2FR46k89VgLRuYhqHkL3e75xLCDNO%2Bj1hOLF26%2FzWaU7W5oP0H3WwS8StwLep%2BRxduMYi1lRA90VRin3BOP%2BhH18IjGSQCMOaY4VnZXXrJG8vfUbv%2FvhWFA83co2M00FUn66vIS1DnXX%2Fkj0Owwz9SWcPkPJYq7UMtEvB0RNSZYqwZqg9MnqoaKmVQcshackZy2H8M84ebR%2BluHuYIVuVLVAKz%2Fm3emkd1%2Fegvht9E7QuK6jXKzeWoAw0LOu0wY6pgG6L8Ruuvd7N%2FvD1JLgZ10WKjVwkilUMtulZfkONkkPrAD3PM0SbMXPakuUriqqYmpOKaRu%2B7rvuNZBfo5YxLX7xUaopNgfzsQbJ80DoLtojCN%2BhENjMQHg2Gh7NNApvnfmZ478YfvDVHUmAKHXCUOkrtYZBCFfpUMnHsQ5e1Y9eRTRoy5ryUICg6XFGsBRtq%2BYMv9EmZYle9voy%2BiF5LFNB8nsKxaP&X-Amz-Signature=b51f071b6365d6e7005cdd32f02ce08c383993e5ae70d16703a57b3da694dce1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







