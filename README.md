



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPMBUWER%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T063200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIBAILX3i1%2B%2F9eK9F5dELGNIm2rRCJ1q6XI94vkUCr5aZAiBZ0PWrUha2ZMcs%2BtCCWTJxmca9dMntJNPS3srULXOtDyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMYQb3Wrh3LD9Zw1LfKtwD%2FiXO6%2BNnCpUNYX%2F6qDHg1JU5EbUcPY7imewKpNIqnFTsdFzbR54m2okgazEqAq47z4Q3RdlTG3ZUF%2B%2Bs1meRPqEWr7XC9VN40qTNszJjzsnBLEMgVyhXWDk1uRZ17frgEE6O5V1HfrxPqeP%2Fs5DdlpJbi%2Btu0N5BF2I%2FPT9lxqNkJjQp%2BzyP5Lgs7NhI8lM3uYCug4e0WIgQhyY7TT4KJctt3NusiyfM8XScz2WKkKo6IsWiFL81TWJbLFWP8UsudsbDg3j5kXaxgGBLZrpWZ2GKa378R1mmSIPai%2Fz%2Biv5OMzjIMG4oOlbyQrLjmIf0ZA3y9uWYb8vcCawsLg5Hk0zPHemXfIcfoNM5dIsE89NALVzR0ey863T%2B0AQ%2BOD6FrjdjLxUtQrJeYV88fO6CTrP3bhBjwqy%2B1C6wcWpj3at6Vef9bkxqs91GVafAm7mBnZhcynr0WNccQWIdhqoCi0ZRIgMOnYwyTSoKfhEieGPgOnP9lUF1cNUOu7pVBourwf315yPIHHj%2BTzT7REXt3VSNTNpo0gb0neo%2FgY3lMRSsSmR9uM%2F19X9xg1cqdomzp0QnYuX8FNUIxMSSu2cRb7c%2Fz5wKJU%2ByAzD%2FWgers5avM%2FobR39seA3h32gwxLPtygY6pgFJjuDtM8DCgOspuk1xmeIToNkVWlZWUL%2FkAP7G6%2FacodV6Utfxd5Nc3Ys%2BjJpFF3Es4yKbAneOABh3fPIxHpSuSbFhiWtZ24ZE8x1RtGO%2FCuAQRUw9rGfIlxAXyP%2BGZ%2BLu9IQlFYEBtENVqjvwOJjWPVE21fPS%2Bz8rYTHK7AM0wdaraQES7FMwRc6hP050nX3MUtKG7Cr2OLj%2FffHKCC0dfmbsr7CH&X-Amz-Signature=7f3a1ce6278c3ad9c50d453a887c29d3f406ec9336d90c47b45ddb0ae5e7dfd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPMBUWER%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T063201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIBAILX3i1%2B%2F9eK9F5dELGNIm2rRCJ1q6XI94vkUCr5aZAiBZ0PWrUha2ZMcs%2BtCCWTJxmca9dMntJNPS3srULXOtDyr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMYQb3Wrh3LD9Zw1LfKtwD%2FiXO6%2BNnCpUNYX%2F6qDHg1JU5EbUcPY7imewKpNIqnFTsdFzbR54m2okgazEqAq47z4Q3RdlTG3ZUF%2B%2Bs1meRPqEWr7XC9VN40qTNszJjzsnBLEMgVyhXWDk1uRZ17frgEE6O5V1HfrxPqeP%2Fs5DdlpJbi%2Btu0N5BF2I%2FPT9lxqNkJjQp%2BzyP5Lgs7NhI8lM3uYCug4e0WIgQhyY7TT4KJctt3NusiyfM8XScz2WKkKo6IsWiFL81TWJbLFWP8UsudsbDg3j5kXaxgGBLZrpWZ2GKa378R1mmSIPai%2Fz%2Biv5OMzjIMG4oOlbyQrLjmIf0ZA3y9uWYb8vcCawsLg5Hk0zPHemXfIcfoNM5dIsE89NALVzR0ey863T%2B0AQ%2BOD6FrjdjLxUtQrJeYV88fO6CTrP3bhBjwqy%2B1C6wcWpj3at6Vef9bkxqs91GVafAm7mBnZhcynr0WNccQWIdhqoCi0ZRIgMOnYwyTSoKfhEieGPgOnP9lUF1cNUOu7pVBourwf315yPIHHj%2BTzT7REXt3VSNTNpo0gb0neo%2FgY3lMRSsSmR9uM%2F19X9xg1cqdomzp0QnYuX8FNUIxMSSu2cRb7c%2Fz5wKJU%2ByAzD%2FWgers5avM%2FobR39seA3h32gwxLPtygY6pgFJjuDtM8DCgOspuk1xmeIToNkVWlZWUL%2FkAP7G6%2FacodV6Utfxd5Nc3Ys%2BjJpFF3Es4yKbAneOABh3fPIxHpSuSbFhiWtZ24ZE8x1RtGO%2FCuAQRUw9rGfIlxAXyP%2BGZ%2BLu9IQlFYEBtENVqjvwOJjWPVE21fPS%2Bz8rYTHK7AM0wdaraQES7FMwRc6hP050nX3MUtKG7Cr2OLj%2FffHKCC0dfmbsr7CH&X-Amz-Signature=43397376cd3ddfb1d580c476d50ac23bf3e0f096cfa2d33598b373677eb6ceb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







