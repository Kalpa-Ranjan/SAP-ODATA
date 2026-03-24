



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAIYOIH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T130053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDhFqW9V5C5h%2F%2BJEcsPvSvPNtdyFrykEzTgsdxl8PxY2AiBl63ySH%2FElYA7IuvRHxua7lQCtzSajZfmqQvJx7C%2FBvyqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkFXLv8D%2FfiAvZRghKtwDXXRP13N9zo6UvzWeKdIFHnG0CYCd1Q5VWiF1VwChZ3zDLjlcXTS8w5GZee8sl87DbESztjj13f8O4vJ9rV9cHNJWKRj2pKzF8RNtqqbBucZKxcsnIcQZ30WpVGLCk0sqx062ZoHctDS8Ehbkd793amFCnkA4nuN%2Fm0GEQRuQ%2Bz1tL9cLy00fRg3%2B4J%2BwkcwR4KOCbYh7T1gGPhXaOjZ9qTToSt8WzCBLQV3RAvkosexb8yNWCCj%2F0p6Yz06v6mBMNmmjQZdfB83jPro4aKsF7qTiD696snzeJNwn1QC5g82tZmekhUMb3ACLissgAH9CSMcbLeU2uIa9v7Ttui52gPIeF7%2F6cQY2wE5iVU%2BM5BBNy9xO6NUmo%2BKxrttYKKurpzdyHbXiRiCKId91bKisD7iAURW2gjxxSQV9rUEAptd90%2Bp4wn3p0TKHLHfCmpNzkV6Gy%2F8Qv2fvhTguotdvTHJXgDospTTHj1epljPYv%2BIM32h4p45vWUy9e2MwV%2BWnHVHtElsJg07QdP6cc71QViBtJPsO9CTV24qFRvk3qJmz3tJWe6ZxRdD1UGPXFzGnjlgjAI9tNxUe1jwd2BNbL0%2BH74eBeydk6jdWA9ua27iJrU0HcDMRKSHfiHQwwY2KzgY6pgGN%2BiwwqZifXXk%2Bli9TmFu5ZJvcEO9smXGRmChNWXsEspbcb7Dqkqm8cZ%2Bg3Lz8Tb%2BRjDTiliwH1E96uFxSKvpMqPCOlUx4UJYyLw1CCoqVWNyAvy%2F3TR1gQiTM7qls05Cql7s44SfOSgaFpFKmwg7DVHiLzCtimwNerH0tfkNhaG8Ekl4le%2B6jYhlNWCbBJsYTebIUWFygwivaLRto5yapqRC9WaYo&X-Amz-Signature=e9256a7b44b4dc5b9a6fa95df8b0ef3ed4b01883917e054d8c7c1fce677eaa8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAIYOIH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T130054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDhFqW9V5C5h%2F%2BJEcsPvSvPNtdyFrykEzTgsdxl8PxY2AiBl63ySH%2FElYA7IuvRHxua7lQCtzSajZfmqQvJx7C%2FBvyqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkFXLv8D%2FfiAvZRghKtwDXXRP13N9zo6UvzWeKdIFHnG0CYCd1Q5VWiF1VwChZ3zDLjlcXTS8w5GZee8sl87DbESztjj13f8O4vJ9rV9cHNJWKRj2pKzF8RNtqqbBucZKxcsnIcQZ30WpVGLCk0sqx062ZoHctDS8Ehbkd793amFCnkA4nuN%2Fm0GEQRuQ%2Bz1tL9cLy00fRg3%2B4J%2BwkcwR4KOCbYh7T1gGPhXaOjZ9qTToSt8WzCBLQV3RAvkosexb8yNWCCj%2F0p6Yz06v6mBMNmmjQZdfB83jPro4aKsF7qTiD696snzeJNwn1QC5g82tZmekhUMb3ACLissgAH9CSMcbLeU2uIa9v7Ttui52gPIeF7%2F6cQY2wE5iVU%2BM5BBNy9xO6NUmo%2BKxrttYKKurpzdyHbXiRiCKId91bKisD7iAURW2gjxxSQV9rUEAptd90%2Bp4wn3p0TKHLHfCmpNzkV6Gy%2F8Qv2fvhTguotdvTHJXgDospTTHj1epljPYv%2BIM32h4p45vWUy9e2MwV%2BWnHVHtElsJg07QdP6cc71QViBtJPsO9CTV24qFRvk3qJmz3tJWe6ZxRdD1UGPXFzGnjlgjAI9tNxUe1jwd2BNbL0%2BH74eBeydk6jdWA9ua27iJrU0HcDMRKSHfiHQwwY2KzgY6pgGN%2BiwwqZifXXk%2Bli9TmFu5ZJvcEO9smXGRmChNWXsEspbcb7Dqkqm8cZ%2Bg3Lz8Tb%2BRjDTiliwH1E96uFxSKvpMqPCOlUx4UJYyLw1CCoqVWNyAvy%2F3TR1gQiTM7qls05Cql7s44SfOSgaFpFKmwg7DVHiLzCtimwNerH0tfkNhaG8Ekl4le%2B6jYhlNWCbBJsYTebIUWFygwivaLRto5yapqRC9WaYo&X-Amz-Signature=d389c6bf3a61165b46c98f7ce3a789665008ffdacfa94589345d475baa602b4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







