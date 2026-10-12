



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTJ5HBQN%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T180919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9%2FKV6phDBdpHqTninbfIxOIK47yQ0oOYUuzk4KdoOqAiEAgE%2F7ZWLWE2VvGERwHIwk7QyyHi9M8ix1vToBzF3Ta28qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLdzmadd8ZBxb%2FeICircA0dcSLFhRfFQhDr6otzAn5YR68vKIDd713Luy1xiyBWlH60m0HaQs2vJKZQm%2BVDovGGUqnY%2B8fAih%2FXd6fvd4oVf8jc1I7upFMZifmWbuuROcTXn7hG%2F82DEhNMAsazQBmr4YPU7MfrZgLEYMlf1LDo%2BOTI7W7N7bfKhlccZxcrV4LzQyLEz4oHMXPSveFvbyohR4yTZJWSYVIicQ7f48fyf9ba4SuPu4uF%2BXHQLrJg4Pqzr03XKuxx%2BtyeZtuGs1rPZoI%2BB1nLgPPzpdWLEfOGq%2Fx4KePkKdc85kfOEshyimTZnm3bzgeQYecOmkNNE2SPB1BLFGVSOoG%2BO5nT9CVT9zYnXM4pgkHSONOcIbv5jCTjl2L61SOh54OBTNktY7nFUJ1pUCM3OK%2BWQ7hc2wzynRZ7D9jwgca5w0nlT53BNdON1aCEZ2wxNVYzhNoJ4C8UuOCpfx2JNzMWjgYgJj2zQYS%2F209%2FFHYRB32mzot0PgKrsyIkd29xdxjadVMvfYF1uS%2FLsQXO%2FxUltL0VfzjGdCwJLH0iXU4XuqyVTVJQ0UQH4LwLe%2F0L1WVsqhagKUI5vrtloxtRX4nUqMFVlfRfmyBw6nsYwhkpqy%2BPGOJINbDuBjBJBH5CusZUYMNmatNYGOqUBJb7CDP4vGVFOMNCUS5jaWgJHlzJmxvpSZU9SpNvfnLmr1HS9oeGgoidaHerVZUXyAA%2B%2BSoJF09er9Mi8dIWhgmyQdrwA9Tz9aAVI1DJOYJzdZtvRtvIXq0OXVWdorSWBcX6rDkj0UuhBdIJPyJ3uNxC4O8pNaurkoAqiYWTL%2B%2BTB2%2BddlqAOt1Z9pfJsyEHvly0DPJjB1230T60L%2BOSxDU6tP1gP&X-Amz-Signature=f31daa5937b1738d2c7654241464eb53b08fc118f358e6118f895f95e84aa7f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTJ5HBQN%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T180920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9%2FKV6phDBdpHqTninbfIxOIK47yQ0oOYUuzk4KdoOqAiEAgE%2F7ZWLWE2VvGERwHIwk7QyyHi9M8ix1vToBzF3Ta28qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLdzmadd8ZBxb%2FeICircA0dcSLFhRfFQhDr6otzAn5YR68vKIDd713Luy1xiyBWlH60m0HaQs2vJKZQm%2BVDovGGUqnY%2B8fAih%2FXd6fvd4oVf8jc1I7upFMZifmWbuuROcTXn7hG%2F82DEhNMAsazQBmr4YPU7MfrZgLEYMlf1LDo%2BOTI7W7N7bfKhlccZxcrV4LzQyLEz4oHMXPSveFvbyohR4yTZJWSYVIicQ7f48fyf9ba4SuPu4uF%2BXHQLrJg4Pqzr03XKuxx%2BtyeZtuGs1rPZoI%2BB1nLgPPzpdWLEfOGq%2Fx4KePkKdc85kfOEshyimTZnm3bzgeQYecOmkNNE2SPB1BLFGVSOoG%2BO5nT9CVT9zYnXM4pgkHSONOcIbv5jCTjl2L61SOh54OBTNktY7nFUJ1pUCM3OK%2BWQ7hc2wzynRZ7D9jwgca5w0nlT53BNdON1aCEZ2wxNVYzhNoJ4C8UuOCpfx2JNzMWjgYgJj2zQYS%2F209%2FFHYRB32mzot0PgKrsyIkd29xdxjadVMvfYF1uS%2FLsQXO%2FxUltL0VfzjGdCwJLH0iXU4XuqyVTVJQ0UQH4LwLe%2F0L1WVsqhagKUI5vrtloxtRX4nUqMFVlfRfmyBw6nsYwhkpqy%2BPGOJINbDuBjBJBH5CusZUYMNmatNYGOqUBJb7CDP4vGVFOMNCUS5jaWgJHlzJmxvpSZU9SpNvfnLmr1HS9oeGgoidaHerVZUXyAA%2B%2BSoJF09er9Mi8dIWhgmyQdrwA9Tz9aAVI1DJOYJzdZtvRtvIXq0OXVWdorSWBcX6rDkj0UuhBdIJPyJ3uNxC4O8pNaurkoAqiYWTL%2B%2BTB2%2BddlqAOt1Z9pfJsyEHvly0DPJjB1230T60L%2BOSxDU6tP1gP&X-Amz-Signature=0cbbae3c8ccdddca519d79242ffccc7d0654a9975af0ceb5cf1d367fc07691ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







