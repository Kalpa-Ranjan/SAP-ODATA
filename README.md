



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIW6G7AK%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T001440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDRRexuXHzQq80lPkd982Se2LwAxmLVHBy%2F08t78%2F76lQIhAP7GY13r2F7QWV4PHliKji6WwjECgsOhI%2BrhPwOSuuk7KogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezVFChVYjZzhPxJwq3AMSGqXhTMqFtJGxJ4m%2Fc4Up3X%2Bpktmxwik7v0W6t5EofAXJ8dLvqrUfULtDQX3OTjhVto73p51PUeYMz%2Frba%2BFczpd32QShlyEOGGEZ0Nb4ZXw8rSyyxAjS1oV6DL9l6lKxT5yYnYXUBB2U%2BWjyy4FS7Tac5OcUuv2bm8viPR7%2B%2BnGq0NO5g2RBHwVakStojlwwLgRcZm3WxlMDot5oZzPksapqeU487%2BxU%2FqYT4eZXwsPQBCELHcx0kie0eCGIjXHVIe2%2BL25KKXwaRV%2Bp2ammC3l59YKLQW24m%2BAXp2SY1CeOU2oLKJw0ysVz8tdBkVh7NW5wC%2BIZH9Bzd9gzkUG36n3cxkF5YvS0e%2FV1lt8rnMkyv0jM1E4VChd81biDNweryVzVQndYjGcssVGXup%2F4ABaKCaY42SZBF3%2FSs4xgOIEVJkHyRUKuVOoqyku3Nkpj22M%2Bdt9ioG3Hc05qU7iisPZErxRiLv4FxAarcG%2B66inBUaSH0mUUI0Uj360Lu6Vg%2FKbDNLDJXdtxsQH3Th%2FZzPSWUD0mZqDG74eDLbgjy9%2BIYMXFRDGASTBxJ%2Fv0gg4eXgdZWTS8T86ByjYo6QJIxnuM0fqSCd0xkg3XEjLhHILCuNTTJ5ixo0f0ljCe4L7XBjqkAZUp%2B4vCUAnyOLrShn%2Bp2u7Zng%2B8PZ%2FoaOmh1YEWd6B1GWPEGIfObAP5PxQlZmUj1QqgHrEWy1xHV3zaVjLRjoNs6pQf8UQ%2BYDny%2FGNbMGR7GwqnIO4DjXlbaJ152xC%2B0aB7UT2AIWiOKGktWw1VY3J6PlZEyuyOYS%2F4o7Q20oxUQn8%2BWrTJIwgFGTMY0l1VMY72OTMRI9cE2JaBqKrvyCMzryqi&X-Amz-Signature=392d5c5ebd42e932ee62a30770aeffafa978211e41e4865faf336c178f196af5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIW6G7AK%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T001440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQDRRexuXHzQq80lPkd982Se2LwAxmLVHBy%2F08t78%2F76lQIhAP7GY13r2F7QWV4PHliKji6WwjECgsOhI%2BrhPwOSuuk7KogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyezVFChVYjZzhPxJwq3AMSGqXhTMqFtJGxJ4m%2Fc4Up3X%2Bpktmxwik7v0W6t5EofAXJ8dLvqrUfULtDQX3OTjhVto73p51PUeYMz%2Frba%2BFczpd32QShlyEOGGEZ0Nb4ZXw8rSyyxAjS1oV6DL9l6lKxT5yYnYXUBB2U%2BWjyy4FS7Tac5OcUuv2bm8viPR7%2B%2BnGq0NO5g2RBHwVakStojlwwLgRcZm3WxlMDot5oZzPksapqeU487%2BxU%2FqYT4eZXwsPQBCELHcx0kie0eCGIjXHVIe2%2BL25KKXwaRV%2Bp2ammC3l59YKLQW24m%2BAXp2SY1CeOU2oLKJw0ysVz8tdBkVh7NW5wC%2BIZH9Bzd9gzkUG36n3cxkF5YvS0e%2FV1lt8rnMkyv0jM1E4VChd81biDNweryVzVQndYjGcssVGXup%2F4ABaKCaY42SZBF3%2FSs4xgOIEVJkHyRUKuVOoqyku3Nkpj22M%2Bdt9ioG3Hc05qU7iisPZErxRiLv4FxAarcG%2B66inBUaSH0mUUI0Uj360Lu6Vg%2FKbDNLDJXdtxsQH3Th%2FZzPSWUD0mZqDG74eDLbgjy9%2BIYMXFRDGASTBxJ%2Fv0gg4eXgdZWTS8T86ByjYo6QJIxnuM0fqSCd0xkg3XEjLhHILCuNTTJ5ixo0f0ljCe4L7XBjqkAZUp%2B4vCUAnyOLrShn%2Bp2u7Zng%2B8PZ%2FoaOmh1YEWd6B1GWPEGIfObAP5PxQlZmUj1QqgHrEWy1xHV3zaVjLRjoNs6pQf8UQ%2BYDny%2FGNbMGR7GwqnIO4DjXlbaJ152xC%2B0aB7UT2AIWiOKGktWw1VY3J6PlZEyuyOYS%2F4o7Q20oxUQn8%2BWrTJIwgFGTMY0l1VMY72OTMRI9cE2JaBqKrvyCMzryqi&X-Amz-Signature=02b1c2f8d9b35cb91e9bfdb1d4cf2feddbd416e0217d007bdec54bf1e366b360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







