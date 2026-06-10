



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RIBMKNI%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T152115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIC4IM2zh7dRigznZtyAZRs97dlQicSnF4pRqA3QEzM%2FBAiEAn7Ckrw3LEbrW3FkV4xX1RYYYS7kf8ITFLrgq1aEZ6D4qiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM6a5ZX5MVllLQtrzSrcA4LqGy%2B40jaZPONCTldV7JfkUXkb7oVdAy1J1qPfx9Yf7jO1QiX%2BsJafE0hC4JYpaRIk%2FFKgyuzZjT%2B21f3KEnUo3TOZ6SuXUSAGDfem1RtIp%2BIznn1yDnceV7MrR3UHe7pkRced12SM0v%2BRAD%2BBiaaXU8fhJl9mGPvP9Z2ngF%2BpuosR09tESd2%2F%2BnsqJKkUZqtVrFINPtnrQw1D%2FyVpRqdR5PT9UrurHsRP3QZckoSx%2FaqcI8ZEWgV1deL7RSH58azKAK0%2B7C5OrIEwK8ZskYQk%2BC6g0X3zagh1OoWQtZgx28f7ShyaJ%2BiAy107ReoqgdZT3D7jQYY7MDh3MH9S1151o4hbYswBNgPUhZ53YpxSbp4jzx9ViFzRGc7%2BPNTW14Y9DDUYRSm6T90hwOX6Lg7fq7cG3Dt9w6v83jjpRVhbUFIAJmeMNaOqLW7TS07PVtAc5yHDvvXRsJrBbZKZYtHwwxpNdfCbXC8zGvoBcXEmwCKOZqvXdRFTqJ5rfatjE9RmxDImnu8D4YsXwnQsNnBGLemZiUKRpzaaUeTze%2B6cwQrvpwhWBH%2FBadYSUbRJbTk4ZLVSBW8fInkqOSFV5kOKT7XwLtiNT9G23x5P9neNZN%2FT9KFUY98A7BN4MMT1pdEGOqUBF8dMbsPGqUnw0odTSii2SfyU2ZhRVEHGNNsX5%2Fp9fkbC4gw5UqP9xep5fnOfvecDyCQrBLQgDgxOFzPhWZqryJLiAyV7VxNpOcpnjecr0d9pR4fW0N3hugr4kqhbVRyGVKCn%2FvUZ77yclHtlvA%2FeTNJzQa6eKdCBR9srRbk1DAEjgvBf7Jg3hNBgdYkyTPOwjjefaUvQ9iPuG1GmaywCvqGjDf71&X-Amz-Signature=1511bdc0775587cb4f4b207bb434b701ad8a0106116cd678a603e7bcef789c19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RIBMKNI%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T152116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIC4IM2zh7dRigznZtyAZRs97dlQicSnF4pRqA3QEzM%2FBAiEAn7Ckrw3LEbrW3FkV4xX1RYYYS7kf8ITFLrgq1aEZ6D4qiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM6a5ZX5MVllLQtrzSrcA4LqGy%2B40jaZPONCTldV7JfkUXkb7oVdAy1J1qPfx9Yf7jO1QiX%2BsJafE0hC4JYpaRIk%2FFKgyuzZjT%2B21f3KEnUo3TOZ6SuXUSAGDfem1RtIp%2BIznn1yDnceV7MrR3UHe7pkRced12SM0v%2BRAD%2BBiaaXU8fhJl9mGPvP9Z2ngF%2BpuosR09tESd2%2F%2BnsqJKkUZqtVrFINPtnrQw1D%2FyVpRqdR5PT9UrurHsRP3QZckoSx%2FaqcI8ZEWgV1deL7RSH58azKAK0%2B7C5OrIEwK8ZskYQk%2BC6g0X3zagh1OoWQtZgx28f7ShyaJ%2BiAy107ReoqgdZT3D7jQYY7MDh3MH9S1151o4hbYswBNgPUhZ53YpxSbp4jzx9ViFzRGc7%2BPNTW14Y9DDUYRSm6T90hwOX6Lg7fq7cG3Dt9w6v83jjpRVhbUFIAJmeMNaOqLW7TS07PVtAc5yHDvvXRsJrBbZKZYtHwwxpNdfCbXC8zGvoBcXEmwCKOZqvXdRFTqJ5rfatjE9RmxDImnu8D4YsXwnQsNnBGLemZiUKRpzaaUeTze%2B6cwQrvpwhWBH%2FBadYSUbRJbTk4ZLVSBW8fInkqOSFV5kOKT7XwLtiNT9G23x5P9neNZN%2FT9KFUY98A7BN4MMT1pdEGOqUBF8dMbsPGqUnw0odTSii2SfyU2ZhRVEHGNNsX5%2Fp9fkbC4gw5UqP9xep5fnOfvecDyCQrBLQgDgxOFzPhWZqryJLiAyV7VxNpOcpnjecr0d9pR4fW0N3hugr4kqhbVRyGVKCn%2FvUZ77yclHtlvA%2FeTNJzQa6eKdCBR9srRbk1DAEjgvBf7Jg3hNBgdYkyTPOwjjefaUvQ9iPuG1GmaywCvqGjDf71&X-Amz-Signature=ac04e86baf279062b2fe3de8aeb5532234d8cd481dbbf3e99010038e52f21306&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







