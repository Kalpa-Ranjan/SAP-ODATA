



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633VR5DLU%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T132111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIELWYElwVKTtyNEkiD6uQLDAsvnG3gpvKH%2B%2B7SCiw44EAiEApuriqDJJ0g1tDShIVSlK2q%2BpIHw9boEZ48x9s74RPAcqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz5kqn45oEH8V4P9yrcA944m05DdZ7jXJGWUDiw9o9o%2BF7GeJihpjV2j1Pqw1mx25%2BxTnqTjvuQeOTwZFeP7KTEZ5%2FaVh1qCgVu8ZDBLS0HqYjSR9FcJjFSzQ0YIc62XAN0CjEsnI7uzTiA3WE7OJipORV9vCopxnjmPn%2BNzzBr938gFw0S5sAiaQx6%2F%2B53TFVCwoUSC9PQZZdSzSI3uSjSYltbT%2Bl8l89afI3uYpqCMAwQtnFRD21Ul9P8bOQjyDYxAduo0g8A5amVKRRfilqOzKM5bRHj%2B%2FsdD5NHu0ZR4XKewYTfPm3u5j979Qv%2B6jO32WsISXLtmZF6rNnncW%2F3NhZcuZSXvKQFaeQyVWG6Ybx4KWahYD0at72ozF4TV7zN3FE4pR4h5uZTDNjL8PxwWq6YvqBusw9M2NOb1C%2FG1b1ajDGHk2Trwbd6gKHdWtwH3ohUT13GOP72uAYm8esyrpaHdex%2FebGvA17uxezs70Lm6cIz5Wl17alImGyRa0xgVOG%2BwAAkUxDELy7v6QdfTe%2B8moKQieDDQplc7N9J8qezWq2%2FewmYSdW2uAHRyTt96cTbtX%2Fnd5qLHG%2B4VISVtqUm5qXirjsAKc9U4Axfnoeog87IOOt7mWyQXQ30R8eh7fe9SEWLjJVvMIy7988GOqUBV1JbRWS2R2RwyKl%2FSs54nIIFvppuyeImQEyAj7fSCRD6oh4irekjpUP3bOSuRLvgwCfbLxpjHotKIW7gI1WIawZFWJ284yBYt4og1R6zXC%2BtlQWKBzMAnAKfRqAcK0LuSD5P3mduE8E0i2g%2FuYQeXkvdnwHalzCnXLyHh1LMdQ5tQ%2Fs3X5ked7caAFVRUb0HN3yI%2BelvjE60S0eODdCsrO9fhL7h&X-Amz-Signature=6a47f86623008e35f0a28d00b8678005020c6c48209707d0de047946fd0920d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633VR5DLU%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T132111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIELWYElwVKTtyNEkiD6uQLDAsvnG3gpvKH%2B%2B7SCiw44EAiEApuriqDJJ0g1tDShIVSlK2q%2BpIHw9boEZ48x9s74RPAcqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz5kqn45oEH8V4P9yrcA944m05DdZ7jXJGWUDiw9o9o%2BF7GeJihpjV2j1Pqw1mx25%2BxTnqTjvuQeOTwZFeP7KTEZ5%2FaVh1qCgVu8ZDBLS0HqYjSR9FcJjFSzQ0YIc62XAN0CjEsnI7uzTiA3WE7OJipORV9vCopxnjmPn%2BNzzBr938gFw0S5sAiaQx6%2F%2B53TFVCwoUSC9PQZZdSzSI3uSjSYltbT%2Bl8l89afI3uYpqCMAwQtnFRD21Ul9P8bOQjyDYxAduo0g8A5amVKRRfilqOzKM5bRHj%2B%2FsdD5NHu0ZR4XKewYTfPm3u5j979Qv%2B6jO32WsISXLtmZF6rNnncW%2F3NhZcuZSXvKQFaeQyVWG6Ybx4KWahYD0at72ozF4TV7zN3FE4pR4h5uZTDNjL8PxwWq6YvqBusw9M2NOb1C%2FG1b1ajDGHk2Trwbd6gKHdWtwH3ohUT13GOP72uAYm8esyrpaHdex%2FebGvA17uxezs70Lm6cIz5Wl17alImGyRa0xgVOG%2BwAAkUxDELy7v6QdfTe%2B8moKQieDDQplc7N9J8qezWq2%2FewmYSdW2uAHRyTt96cTbtX%2Fnd5qLHG%2B4VISVtqUm5qXirjsAKc9U4Axfnoeog87IOOt7mWyQXQ30R8eh7fe9SEWLjJVvMIy7988GOqUBV1JbRWS2R2RwyKl%2FSs54nIIFvppuyeImQEyAj7fSCRD6oh4irekjpUP3bOSuRLvgwCfbLxpjHotKIW7gI1WIawZFWJ284yBYt4og1R6zXC%2BtlQWKBzMAnAKfRqAcK0LuSD5P3mduE8E0i2g%2FuYQeXkvdnwHalzCnXLyHh1LMdQ5tQ%2Fs3X5ked7caAFVRUb0HN3yI%2BelvjE60S0eODdCsrO9fhL7h&X-Amz-Signature=1d8d6e0afb645a0553f6339f6d586b6c8f5e4c0c9a9b75685c980d017bbdbb15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







