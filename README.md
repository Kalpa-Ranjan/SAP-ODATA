



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXTPNXIA%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T121107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQDPBKU8upT4Rq0U1lHaImDuP3EhuQ36NGUdtdBPExsR%2FwIhAK8hXtawQ7Zd8p1e8SJwqYRhHN32aNE0Wj%2Bl5Mcpo497KogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR0Pm1uC1EKXumXM8q3AOT3qBcv3l7UlGP7zu7mmsC96DY4rcbVVMs5srE8WVYUwFj6gbwvt2yDPUzUDp1yydxdLYMFXYpqh7G1pv6BRrvb3Vi73mRD5sUIEtuAg1SUf1uPVzrtqTzv8uqGJ77nJ1%2B9xn1uDuWBGRUeCBxy8%2FF6ybO9yfsLN%2BYf5hf7rmK6NOdgL8H46oXTGyEzi8DICLCI4l2Xr7GfNMU8MtMNhrutpeKYYvQ99Pa5v5fiQOsa%2BU1dzI7a2%2FHg85zxx9Vo8Vv4BEFuQTLZITbSKASlnDiufS7UuricvL0mwM4wDNnYb3YsqObBX%2BLJUn9Lnfha9dIGp%2BSdONWhZZpqg1kEjEnS6mw3YcEAxQ%2BROJ9oPV2V6ZrQVyjRd5S9Ah5GZrhDncXUhnL6orZLLNkgued6t4p2FswtNGxDenYsVPuZF5krDfg%2FrudFB4XqBn2n9tpG4LrHDDjcXXBWuvVegvjK4HVVs5sFEu6rYxfJsHv%2Bss8bbKHVLRPoej36E4MI5SVMsdw6Ie%2BbesYuWwNeFYhL6uNG851c8RB%2BColL1Cl6Dwn2H2odenxRID3rfR%2BYfRt84dKxumCb%2FyZAbUrX6XdN9zBPffM8c%2BVdVeMb0a2qYyzsjJLIiSuG5BYquydHTDO3KTVBjqkATViqSl67K2nYMXagP%2FTpvfNQJruUPH3sAsHgFibdEJ1durMJQ%2FliuqdbNSxaXTGVfV2Szi2uzgHRiAXa7b7b%2FTajsaq7cCVHhbOGb%2BrqyaS5WlKjuiK0JxSISHD0wgvuDxulSE2KK9vwgnKZHg9X741Jz%2B1a9%2BxVUZfZ8PThspc709k6k7RKTmyGdyTqK%2FePkVASYG0SqCopaJvH4szZEtpdmWn&X-Amz-Signature=6ae5ce452dcb25bd72c1cda2e7e2f1a20955d6f633a97c13e091da7b2eb664aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXTPNXIA%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T121107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQDPBKU8upT4Rq0U1lHaImDuP3EhuQ36NGUdtdBPExsR%2FwIhAK8hXtawQ7Zd8p1e8SJwqYRhHN32aNE0Wj%2Bl5Mcpo497KogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR0Pm1uC1EKXumXM8q3AOT3qBcv3l7UlGP7zu7mmsC96DY4rcbVVMs5srE8WVYUwFj6gbwvt2yDPUzUDp1yydxdLYMFXYpqh7G1pv6BRrvb3Vi73mRD5sUIEtuAg1SUf1uPVzrtqTzv8uqGJ77nJ1%2B9xn1uDuWBGRUeCBxy8%2FF6ybO9yfsLN%2BYf5hf7rmK6NOdgL8H46oXTGyEzi8DICLCI4l2Xr7GfNMU8MtMNhrutpeKYYvQ99Pa5v5fiQOsa%2BU1dzI7a2%2FHg85zxx9Vo8Vv4BEFuQTLZITbSKASlnDiufS7UuricvL0mwM4wDNnYb3YsqObBX%2BLJUn9Lnfha9dIGp%2BSdONWhZZpqg1kEjEnS6mw3YcEAxQ%2BROJ9oPV2V6ZrQVyjRd5S9Ah5GZrhDncXUhnL6orZLLNkgued6t4p2FswtNGxDenYsVPuZF5krDfg%2FrudFB4XqBn2n9tpG4LrHDDjcXXBWuvVegvjK4HVVs5sFEu6rYxfJsHv%2Bss8bbKHVLRPoej36E4MI5SVMsdw6Ie%2BbesYuWwNeFYhL6uNG851c8RB%2BColL1Cl6Dwn2H2odenxRID3rfR%2BYfRt84dKxumCb%2FyZAbUrX6XdN9zBPffM8c%2BVdVeMb0a2qYyzsjJLIiSuG5BYquydHTDO3KTVBjqkATViqSl67K2nYMXagP%2FTpvfNQJruUPH3sAsHgFibdEJ1durMJQ%2FliuqdbNSxaXTGVfV2Szi2uzgHRiAXa7b7b%2FTajsaq7cCVHhbOGb%2BrqyaS5WlKjuiK0JxSISHD0wgvuDxulSE2KK9vwgnKZHg9X741Jz%2B1a9%2BxVUZfZ8PThspc709k6k7RKTmyGdyTqK%2FePkVASYG0SqCopaJvH4szZEtpdmWn&X-Amz-Signature=8ee116d50d5bb4c07ae45cdb9995d357213f0d0754b052502f48511172ce6b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







