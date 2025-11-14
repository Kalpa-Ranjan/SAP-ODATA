



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXYAZM7X%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T011246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCagfRE7z56AkyOb3cquvYGfImVYCJtT6hTSqxe%2B1fk%2FwIhAO8Z1xFq%2Fds6iH3SnlKfL6DAWxKCoNq5wTLcVWFQeWUUKv8DCFkQABoMNjM3NDIzMTgzODA1Igxe3%2F6kT7opOG2eTCgq3APvEZyHFxBDRQiEoOFvWGcZPq%2BAoGPqpN7TI2UEltHQEXnsk9KuLKebrlDGCBLUF0U7J5Ixvead4h%2BRRIXL4Pjl3%2BnQGpN%2Fdyt2ziWY4eCJYjtDsX3GeE0MZJsOsgBh5vlG47wsmzDwkeDzv3VQ8rqtafe2eozcG1a6Qch6VyWCYlofdO5pxNK9sP2IkKvOME6Gj8P2BjCPsaxoXpkHuzYAJCtOInb8waQsDAnWuGLakjO6tAWkFjOPmbr0rrJfVZvsJfbcVwr6iuF5vC5rinpt4HpLwKXRii5oRHSM9Id1k4HL9QHOmFwSczhyGKTS4L4VekjCbztf19BIhdCzoUrxzhLxrNOR80T29XBYV1uML7Q6sVbRVOO%2FR%2F46aHJ7%2BTQF9OhrgemEMKpVQADegm3acier%2FSUoKkwUJRSbjx1xOeoUKQwxzbCf41LQpSzHrIjWsflhBiw92%2F%2F0jXxTV3cXWAhs9xwhHYsISS2dUZog7XfvCUSqAxxBB%2B813TXOh9kmTx2ZSa%2FPiNApqYl%2FGRm58gULJGfIAthWb8LBOXwqyAGgEnFPCqTZpBW3M9aqOkFH%2B3EllapxkysMmB9n2Rum6%2Bsy5R1VtmTkR2gzc%2Bc3LB9c2bCwqih8IXbf5zCV59nIBjqkAaSsA99qrHorsHQhB2mnP9OcoJGYegTdyTTMRUAA%2FqLDIHyhpgUu1b4bHSLnZYOyQ129hm4w%2Bbm62q1mzoSc1TuM4CJ1B%2B4DucZEUnqhYvVvCAZYAPIHwE2aPUqjDmF2NjyIY79KNVnPZ7WFaQ2IOfWSUTBdlk%2FmKJVd463eb3ipVEftDaLq%2FWsw7iD5ZsGHcPwgO%2Fkx9UBRytomhyLNkaJZXUgj&X-Amz-Signature=e4f825f448fad0df1889b4ea7ee0f4eb50bb58fc2932189fc87fd3c24dda75c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXYAZM7X%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T011247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCagfRE7z56AkyOb3cquvYGfImVYCJtT6hTSqxe%2B1fk%2FwIhAO8Z1xFq%2Fds6iH3SnlKfL6DAWxKCoNq5wTLcVWFQeWUUKv8DCFkQABoMNjM3NDIzMTgzODA1Igxe3%2F6kT7opOG2eTCgq3APvEZyHFxBDRQiEoOFvWGcZPq%2BAoGPqpN7TI2UEltHQEXnsk9KuLKebrlDGCBLUF0U7J5Ixvead4h%2BRRIXL4Pjl3%2BnQGpN%2Fdyt2ziWY4eCJYjtDsX3GeE0MZJsOsgBh5vlG47wsmzDwkeDzv3VQ8rqtafe2eozcG1a6Qch6VyWCYlofdO5pxNK9sP2IkKvOME6Gj8P2BjCPsaxoXpkHuzYAJCtOInb8waQsDAnWuGLakjO6tAWkFjOPmbr0rrJfVZvsJfbcVwr6iuF5vC5rinpt4HpLwKXRii5oRHSM9Id1k4HL9QHOmFwSczhyGKTS4L4VekjCbztf19BIhdCzoUrxzhLxrNOR80T29XBYV1uML7Q6sVbRVOO%2FR%2F46aHJ7%2BTQF9OhrgemEMKpVQADegm3acier%2FSUoKkwUJRSbjx1xOeoUKQwxzbCf41LQpSzHrIjWsflhBiw92%2F%2F0jXxTV3cXWAhs9xwhHYsISS2dUZog7XfvCUSqAxxBB%2B813TXOh9kmTx2ZSa%2FPiNApqYl%2FGRm58gULJGfIAthWb8LBOXwqyAGgEnFPCqTZpBW3M9aqOkFH%2B3EllapxkysMmB9n2Rum6%2Bsy5R1VtmTkR2gzc%2Bc3LB9c2bCwqih8IXbf5zCV59nIBjqkAaSsA99qrHorsHQhB2mnP9OcoJGYegTdyTTMRUAA%2FqLDIHyhpgUu1b4bHSLnZYOyQ129hm4w%2Bbm62q1mzoSc1TuM4CJ1B%2B4DucZEUnqhYvVvCAZYAPIHwE2aPUqjDmF2NjyIY79KNVnPZ7WFaQ2IOfWSUTBdlk%2FmKJVd463eb3ipVEftDaLq%2FWsw7iD5ZsGHcPwgO%2Fkx9UBRytomhyLNkaJZXUgj&X-Amz-Signature=256285d3c3d177a88339d5d21c716c321ee3969fb863583d10d1c82bf8fdd908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







