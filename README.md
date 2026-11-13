



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4677UJH%2F20261113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261113T180458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPxNhUa6tsoFZIYlqREHgpbJh1cU4EHAVdfAy5fvF4UQIhAMm8AXTYd1QZBIxNcZJ0sTnH35UEFHeGPbNclU457ZHgKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx5zkaNN5W0dKH%2FJYq3APtG1%2BN5pHV9slE3i86M2%2Fst6PhsEpNDmMEJBJaVAFhiX4RyjSWg%2Fwpuy6G8r6iFTYeYAib%2FoJLb1H5ZP2g9%2B1V6JL3PO3FQGAWxl8M4vBELfz%2FD%2BRn4VPkEpWAnzepj2nD2gwsA%2BYO91RvGWpc5pYWNzaK9cT2maJChNgsH9F8Z3zTFRlpsrzRAAzD%2BH1oRrYHep4YLOhgZdihtL9dm%2BeFZCUGWbFmlVdG1XRYjc4bsDNQu4R%2BgS1GMDAJZysvAWFfbqBNwycjPvEqH%2FzsQnoP%2FIsVMkyCNhFKYIq%2B1ebtuM8Ai3azGwDLQRYPnQ3Cnsw%2B41%2Fp%2BOQ0PO%2FTwk%2FCxnibDhpYnTs7jLmnEidqx5t3wlm9ZTB09%2Flf9e0P3upyyHjnC8bBCropbIVoPHM%2BZCpH0voTgVVrx1tsPW6W2ea%2F0IfxpBAbG%2BGdR89V1Cw8hWKKzZHUbtMkTmiXpUuldV5KB1ghO4QJTeNkGjIObnJlUJZHohI6Z0bZ9eQ1rqPwQjwDRkhPlLdN4ZchJiCQygXIhbZLb7%2FZDuFglrIPca6UR802ujw3uipbd9oBhRXilEmNx1xEsGZnnu6%2BGHQafYgHODfE2HJeAPXsCOKEni%2FY6csKqG4ZMtBNhU1X9TCh9dzXBjqkAeM41XI%2BHL51xE93ONIN6gkZBL8v%2FAencN3VIXcF9%2FiVJhJT3cj87%2Br8hvH%2BsbYnpTHsEaGBC3aVJzs1pFi409XBaKmlDMe%2FLHpGvS3PYy5osBudZBNhqpmJFrQaHM%2FsX6L5cwPSiD1KnwJm1PCjpzDg5BmUZVLExVuDlUTBZuaKVhkM6yjtNtg%2BKXgud%2BfOgtTuOk58Ud8yNSk0u7fI%2Fj9wDhEL&X-Amz-Signature=8cfe076aeb751377493b57de2777cfa4d80a9e4b60e2fd27c24dd2d4132e88ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4677UJH%2F20261113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261113T180458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPxNhUa6tsoFZIYlqREHgpbJh1cU4EHAVdfAy5fvF4UQIhAMm8AXTYd1QZBIxNcZJ0sTnH35UEFHeGPbNclU457ZHgKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx5zkaNN5W0dKH%2FJYq3APtG1%2BN5pHV9slE3i86M2%2Fst6PhsEpNDmMEJBJaVAFhiX4RyjSWg%2Fwpuy6G8r6iFTYeYAib%2FoJLb1H5ZP2g9%2B1V6JL3PO3FQGAWxl8M4vBELfz%2FD%2BRn4VPkEpWAnzepj2nD2gwsA%2BYO91RvGWpc5pYWNzaK9cT2maJChNgsH9F8Z3zTFRlpsrzRAAzD%2BH1oRrYHep4YLOhgZdihtL9dm%2BeFZCUGWbFmlVdG1XRYjc4bsDNQu4R%2BgS1GMDAJZysvAWFfbqBNwycjPvEqH%2FzsQnoP%2FIsVMkyCNhFKYIq%2B1ebtuM8Ai3azGwDLQRYPnQ3Cnsw%2B41%2Fp%2BOQ0PO%2FTwk%2FCxnibDhpYnTs7jLmnEidqx5t3wlm9ZTB09%2Flf9e0P3upyyHjnC8bBCropbIVoPHM%2BZCpH0voTgVVrx1tsPW6W2ea%2F0IfxpBAbG%2BGdR89V1Cw8hWKKzZHUbtMkTmiXpUuldV5KB1ghO4QJTeNkGjIObnJlUJZHohI6Z0bZ9eQ1rqPwQjwDRkhPlLdN4ZchJiCQygXIhbZLb7%2FZDuFglrIPca6UR802ujw3uipbd9oBhRXilEmNx1xEsGZnnu6%2BGHQafYgHODfE2HJeAPXsCOKEni%2FY6csKqG4ZMtBNhU1X9TCh9dzXBjqkAeM41XI%2BHL51xE93ONIN6gkZBL8v%2FAencN3VIXcF9%2FiVJhJT3cj87%2Br8hvH%2BsbYnpTHsEaGBC3aVJzs1pFi409XBaKmlDMe%2FLHpGvS3PYy5osBudZBNhqpmJFrQaHM%2FsX6L5cwPSiD1KnwJm1PCjpzDg5BmUZVLExVuDlUTBZuaKVhkM6yjtNtg%2BKXgud%2BfOgtTuOk58Ud8yNSk0u7fI%2Fj9wDhEL&X-Amz-Signature=71987da73681fc445caeabf3dc3246621afcb32d364bc2e829e382c6112fd8d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







