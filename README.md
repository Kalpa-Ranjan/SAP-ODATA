



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WBNCD2G%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T062116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIF%2FWvsWy3EdNSWvtYuRv2m30MRAqw9Z9Vpmjef6OUqXgAiB36s2FtluGvpS0kFwnfVsXuu0fHOu0LZsl%2FzRNid2alCqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdGgBNNp3lmC0dKdiKtwD89TEeE25jnEnEjPm2kECaydXZlUCjkvRlEeVD4Sm4eJCQuuo8iClkzbbRevnUlwwNc4GIJp1xJAZR0HPDdvkQzLW%2FPAOSJ5NNZ%2BWUts3UElq8qo88PlD7HPRENKAyvAy6sq8q0X5Z7K6QKuFwLTk9GJOV3C3kp9EuJCHosHwHD%2BqTxNrkgSK8zvyA1JCFy9z5LNJtRBcYgj9kR2LZ0whJ82Za2NPlyJTm63RtTTayUS7KXZJe4iENtvogxiW9jHfqB%2FUePBxWR85zPUnoTJ1v8Bw5Wbis4MGyOfjbqhbxbkDCU4EvwFjOIGB45sS32wmnkTp5S8%2Fr8bCwWlF5ceItVpBRy6xSK6mRufw%2F905bkW%2BruR2NUL32lP3SUzPmcDYIYcYvy%2BMjDe8ISaXFPWwJmd1D3dRwXiQws%2BKvhr28xdho25LO02m7HLoQsV6xZKh4VCt72TyyDniTGqyX5VqaJ4yar6JbjFlZSdj221V0pVQJMIqrwAYS1DNYwNiwF7zPD5uTp6Z46IzVjaXjGqHS6qJtAKfqTSV7nUCKMYKv3QuhIToJ97Aqlvl5EVUPp4ssGwBcZEy%2Fa%2BMUeei0V5YpvA3RqY95Rh1wAKeCiBvDZhQNB3tJjwufnKvrAYw9YPAyAY6pgHeplXt62V3G1Rmdd02De4vopVRvmQxgCSXyfeyI%2BvLinUQm2mj6h%2FO6brqBonwIlKanaY9Pm5chCve2TfP07lL%2FMOujE8ENHeuIkvqc6t7hLqYd2lZFt3rVuwaQ%2BXHSgt9dPDvm8p1Y9RwzQk%2Fq3iBRJm6sLGHcBg8CYh9MJZsn1Fnw7%2BsGnocqpNnWGSgrhVM3WhTRdt9hvGUODdXDMTCXvsxmHT6&X-Amz-Signature=2d34b5b67db9648c8344161faa99cfb6332ff87421cb86c795cbbc9cfb90be45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WBNCD2G%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T062116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIF%2FWvsWy3EdNSWvtYuRv2m30MRAqw9Z9Vpmjef6OUqXgAiB36s2FtluGvpS0kFwnfVsXuu0fHOu0LZsl%2FzRNid2alCqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdGgBNNp3lmC0dKdiKtwD89TEeE25jnEnEjPm2kECaydXZlUCjkvRlEeVD4Sm4eJCQuuo8iClkzbbRevnUlwwNc4GIJp1xJAZR0HPDdvkQzLW%2FPAOSJ5NNZ%2BWUts3UElq8qo88PlD7HPRENKAyvAy6sq8q0X5Z7K6QKuFwLTk9GJOV3C3kp9EuJCHosHwHD%2BqTxNrkgSK8zvyA1JCFy9z5LNJtRBcYgj9kR2LZ0whJ82Za2NPlyJTm63RtTTayUS7KXZJe4iENtvogxiW9jHfqB%2FUePBxWR85zPUnoTJ1v8Bw5Wbis4MGyOfjbqhbxbkDCU4EvwFjOIGB45sS32wmnkTp5S8%2Fr8bCwWlF5ceItVpBRy6xSK6mRufw%2F905bkW%2BruR2NUL32lP3SUzPmcDYIYcYvy%2BMjDe8ISaXFPWwJmd1D3dRwXiQws%2BKvhr28xdho25LO02m7HLoQsV6xZKh4VCt72TyyDniTGqyX5VqaJ4yar6JbjFlZSdj221V0pVQJMIqrwAYS1DNYwNiwF7zPD5uTp6Z46IzVjaXjGqHS6qJtAKfqTSV7nUCKMYKv3QuhIToJ97Aqlvl5EVUPp4ssGwBcZEy%2Fa%2BMUeei0V5YpvA3RqY95Rh1wAKeCiBvDZhQNB3tJjwufnKvrAYw9YPAyAY6pgHeplXt62V3G1Rmdd02De4vopVRvmQxgCSXyfeyI%2BvLinUQm2mj6h%2FO6brqBonwIlKanaY9Pm5chCve2TfP07lL%2FMOujE8ENHeuIkvqc6t7hLqYd2lZFt3rVuwaQ%2BXHSgt9dPDvm8p1Y9RwzQk%2Fq3iBRJm6sLGHcBg8CYh9MJZsn1Fnw7%2BsGnocqpNnWGSgrhVM3WhTRdt9hvGUODdXDMTCXvsxmHT6&X-Amz-Signature=c4f8bc138951933b71dc2d9ea110faa4cddc3db57ab43aa6e8c314ef43c24914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







