



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYYIFVLR%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBnjSiMVCtVIw0Otq5moutxrfiSDVSKCR5rfBSHLvhoQIhAKNaDMaM9t8M4KIlp%2BU4tVJ7lueeR8izYUHcrS82pqmPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqBEq3IUkHeTnl0wgq3AOQruiDOUrpq7qV%2FfMvSSYMBvRD31xt7agUf7SY5hwpJlUl3a3bayZHGrC3pzBPsg%2FIkb99XSw1led1cgz0v9tkmzJeWRL%2BYD4384z2L194GLXDWgV2ya4aIft29CgYAjXWgm7NgjTKTEvzkyK5MnzKlZ1uLKWV6acSEvSECq3NrHp7AbHVtf74YlcT3cQsLpnK6ziToqZho4DD42eZYyudXNZvxf3QGmI85LD%2FlUHb4ca3PETQDwzUNcN2hAdytZ4JqYWK9wlS6BVigaDrsQgH6odIDKnU6l6N86ol7oHIxGu1MhnJxXGv3u8zxfJmUmkNT4gQZkgOHP9SYzdw731%2FLaXW%2BaH3zqRFagW6zgBY%2BG%2B5D7EIfGV7Cclo9zF6gPbSMWUxFFJ%2F4VMKbaVUtL0op%2FVl%2FkQVD%2F6tyQNggdkMYQCDTMsdi9eZcywrdH3rZuUyCCJfpA%2BDJz%2F7Feqj9M%2FeI%2BIdA9HoqeReCrZqpnmWSA8TDxdXzQhYHrnXOtHfLMGXhzVzRBdAIZ2QjEU8r%2BSZ4fVqeuLBAyHuLGTCMzKQI4iRcF2yO8AHS1H7nmusJl4eLrUYZY08IEQ%2BXaKfzEJHmWfUdoa2aT03I3LVx7wietfCt%2BNdgvg2hlwfkDCx%2B7HPBjqkAcqVIciGSYTS2I544l%2BnLpy0gdMAmvUn%2Fi3awwa1dGh7nwi9wpVpuXs%2BatMNaghrHOsI5gzwbeQKRvqV3QEcP7XctqBeMbb5jOQePrbfHUn2ZjJS6tcfxtNZmISIVQmO8aQbxA7fYQcbPMXt7uzRgkmCkbp970G5lfdLrhLNiKRInacFhHn0OZlCoWOMSqhfQsqxVu5%2FESpETdJ6TIFH%2FEDj9D4g&X-Amz-Signature=5c00fcc371568d651ec6c47a689183d611690f97621b805af1a701fe3dddd0bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYYIFVLR%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBnjSiMVCtVIw0Otq5moutxrfiSDVSKCR5rfBSHLvhoQIhAKNaDMaM9t8M4KIlp%2BU4tVJ7lueeR8izYUHcrS82pqmPKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqBEq3IUkHeTnl0wgq3AOQruiDOUrpq7qV%2FfMvSSYMBvRD31xt7agUf7SY5hwpJlUl3a3bayZHGrC3pzBPsg%2FIkb99XSw1led1cgz0v9tkmzJeWRL%2BYD4384z2L194GLXDWgV2ya4aIft29CgYAjXWgm7NgjTKTEvzkyK5MnzKlZ1uLKWV6acSEvSECq3NrHp7AbHVtf74YlcT3cQsLpnK6ziToqZho4DD42eZYyudXNZvxf3QGmI85LD%2FlUHb4ca3PETQDwzUNcN2hAdytZ4JqYWK9wlS6BVigaDrsQgH6odIDKnU6l6N86ol7oHIxGu1MhnJxXGv3u8zxfJmUmkNT4gQZkgOHP9SYzdw731%2FLaXW%2BaH3zqRFagW6zgBY%2BG%2B5D7EIfGV7Cclo9zF6gPbSMWUxFFJ%2F4VMKbaVUtL0op%2FVl%2FkQVD%2F6tyQNggdkMYQCDTMsdi9eZcywrdH3rZuUyCCJfpA%2BDJz%2F7Feqj9M%2FeI%2BIdA9HoqeReCrZqpnmWSA8TDxdXzQhYHrnXOtHfLMGXhzVzRBdAIZ2QjEU8r%2BSZ4fVqeuLBAyHuLGTCMzKQI4iRcF2yO8AHS1H7nmusJl4eLrUYZY08IEQ%2BXaKfzEJHmWfUdoa2aT03I3LVx7wietfCt%2BNdgvg2hlwfkDCx%2B7HPBjqkAcqVIciGSYTS2I544l%2BnLpy0gdMAmvUn%2Fi3awwa1dGh7nwi9wpVpuXs%2BatMNaghrHOsI5gzwbeQKRvqV3QEcP7XctqBeMbb5jOQePrbfHUn2ZjJS6tcfxtNZmISIVQmO8aQbxA7fYQcbPMXt7uzRgkmCkbp970G5lfdLrhLNiKRInacFhHn0OZlCoWOMSqhfQsqxVu5%2FESpETdJ6TIFH%2FEDj9D4g&X-Amz-Signature=78ec976e0abfabd3fca4399d290d816629f491b0db9a36f4ddfcd48e4033786b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







