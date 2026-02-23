



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663YST7OC%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T014806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDGEDKEsr1NMQaa716kICZkHMYu3bh9MMfgBf7g%2BCdScAIgB1D0cc7Ake8MwYTJ7I8OuhBpTzwxPRx6NzSzO04SMCAqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZDtMJ%2BOaJeGgpdTircA%2Fc7nj%2Fgjms2C%2BKJiHpj%2FJI54ckR52uNvUJGa8MHIBUmgnmrWOTIi6KvE8oix2UZLpjPyg2NBZxeOKAnAyh932h%2Fq4Yv5fHyPZ%2BU4j%2FbKWsbM3%2FjOrjVzPc9zpbjrVTEZ9%2BlNji74rnv7Wa5xu31MnHHKfk2IyRJ3DAL2ERuYZX2%2FN7A9HAFq6X8Wp%2Fbs1%2Bmd3Or%2Bc92cePUhJsIyPBBSWk3%2BtK8GuWY6PQyrhhCCYRW13IK4UlGFSYZwlSqsb2CJtlsFHxILA2Tw84yzMoJrQbJB6LTGtofOR%2FU%2FClMHwmFC96BW3ATr67VLbfBCm58%2FDajHc6Q9kI2wXoydfK02Z0kOd%2BAnED8M7KJGWdiFuHITY0y3AQSdnabLOJ%2FG33wKJA6towY4r6LBqKklvGP0IhzSc4T4mKBMSd46guwyjdCxYQHIgZa6F8OoabooutAGKzQdECxt1QdNOUdsBAlw8a%2FDLaUZj%2F%2B2KVevVFZMyFWXfCHCbKqKwRUdBnzugKzttk7ULK0%2Ft2Ts0yRNAmL9IqYQfbfDEv3kbvQznt9QiNqtwOerDc1QpphP%2FSNqMRej%2BN%2B7SkG3CJammHoIdM4nuI0iHNfrFW%2F%2FRPn6jhmMIP82X9Wsq9mjoSzu%2FRBMLDD7swGOqUBG2DI05Gb2TD1mP9Z46qzazFxGp%2B2Bqq0GChoIlU65ca60WRpZB0RYO0pP5ouAtoDmU%2BpfV05FoxZBZEvvTNTdUON28aqQCAWRKkH24kvPKmY0CojEOtuDANSpess3rJzxkLjlY%2FyiW2X%2FNg5EHc5k4RNWUROW0zS6aGE%2B%2FdBtzlDVsnr6xS1UUNN5S%2BhdSCZOAu1V%2F64c2yM55iM2O9D9qrSI3Ws&X-Amz-Signature=c814eb7adcf03cfee4c557f931b2bfb8560f30d0589271541fde16b50a1da7b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663YST7OC%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T014806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDGEDKEsr1NMQaa716kICZkHMYu3bh9MMfgBf7g%2BCdScAIgB1D0cc7Ake8MwYTJ7I8OuhBpTzwxPRx6NzSzO04SMCAqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZDtMJ%2BOaJeGgpdTircA%2Fc7nj%2Fgjms2C%2BKJiHpj%2FJI54ckR52uNvUJGa8MHIBUmgnmrWOTIi6KvE8oix2UZLpjPyg2NBZxeOKAnAyh932h%2Fq4Yv5fHyPZ%2BU4j%2FbKWsbM3%2FjOrjVzPc9zpbjrVTEZ9%2BlNji74rnv7Wa5xu31MnHHKfk2IyRJ3DAL2ERuYZX2%2FN7A9HAFq6X8Wp%2Fbs1%2Bmd3Or%2Bc92cePUhJsIyPBBSWk3%2BtK8GuWY6PQyrhhCCYRW13IK4UlGFSYZwlSqsb2CJtlsFHxILA2Tw84yzMoJrQbJB6LTGtofOR%2FU%2FClMHwmFC96BW3ATr67VLbfBCm58%2FDajHc6Q9kI2wXoydfK02Z0kOd%2BAnED8M7KJGWdiFuHITY0y3AQSdnabLOJ%2FG33wKJA6towY4r6LBqKklvGP0IhzSc4T4mKBMSd46guwyjdCxYQHIgZa6F8OoabooutAGKzQdECxt1QdNOUdsBAlw8a%2FDLaUZj%2F%2B2KVevVFZMyFWXfCHCbKqKwRUdBnzugKzttk7ULK0%2Ft2Ts0yRNAmL9IqYQfbfDEv3kbvQznt9QiNqtwOerDc1QpphP%2FSNqMRej%2BN%2B7SkG3CJammHoIdM4nuI0iHNfrFW%2F%2FRPn6jhmMIP82X9Wsq9mjoSzu%2FRBMLDD7swGOqUBG2DI05Gb2TD1mP9Z46qzazFxGp%2B2Bqq0GChoIlU65ca60WRpZB0RYO0pP5ouAtoDmU%2BpfV05FoxZBZEvvTNTdUON28aqQCAWRKkH24kvPKmY0CojEOtuDANSpess3rJzxkLjlY%2FyiW2X%2FNg5EHc5k4RNWUROW0zS6aGE%2B%2FdBtzlDVsnr6xS1UUNN5S%2BhdSCZOAu1V%2F64c2yM55iM2O9D9qrSI3Ws&X-Amz-Signature=a95f4b6a1d2001855e08a679783b8107ca1a23f05aa2621853a053606ca6082e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







