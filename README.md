



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGD366D%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T121059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDkc8PBKJ49axvj0kDcLmHk0lnwzZ%2BIsvPJ6vHy%2F3ypVgIhAJsHlTUZMNTfXABxZZMY5KTdch1PlEJpVF79aVlK0qFAKv8DCBoQABoMNjM3NDIzMTgzODA1Igwc3U0oPDHflF%2BqCUcq3APuCTDO1AOhDHzZ54EQuVJJ%2BP3YomICrWe103Wrc6mDi8lqajga7XUCk7H%2F%2BZ%2Ft%2FZ1tsnAQPedyFEXv8kZersww3%2F2KXZfQc%2Fy2FqFka5q7w9fgHPXXqh1E0FvALno6B%2FeQygnOKJrPNOBuF5NW2xAJ20GJY%2FpKxGBmOVz%2FIX2tdWUspEg9mK6j1LJXRD%2FUiIMFGy%2BnRdzfO2%2BNFrYB1L8PpiBxSmqN9A0DvfEL4OJvcQdhfAuicm4ez0IArNC5CqhX0Ft3XxYd%2Fo%2BJDg4lzrQA5AzPUZrBNmgjbqt3ToRuiaWkA1cnJ4UowTvfEDYNllK5faVAnvBWecQedmWdKEQAK6IISpH9j3FlckSGMAZW%2FJvDB1OGogqgbqjiPPZq0B6O1CykgEBF2j585AhBpRs%2F%2B4PAwhb5gpjn4knfIfTn3hvZPJ8v%2BeHkj0Rr2VT2DMw1gdIQyvbtvDVoNTO10569R7wKgxOUHbXni7I0i65rEi5W%2B%2FGS%2B8MQOxKdBAhQBTQnx1CUjJQwHuKwMcuSKnKB3nAgVM7LbgenrKSgoyWv03xFm77Gv%2BBDhR%2FwODYGMjnae39MjPMhroBVPqbLL9p6X%2FK6ifFw6lvWnXb6UYf6gyuoEf1wF56XqhtG3zCurOPVBjqkAdrd9TYYjBwSfJaz2cEc3SvlIcFv%2BMUjCeNEIkJanbrVwoUnlAM9Zv%2Bx8sXxuMOUViU8mIYjNg1IDaQ0E9FtZOu9hjNE3YgxsF00krHYOLP6LWIufNlhflgcmE4vFlcsHJYNm2gFhrb8lAsUSil6bOkDcXb7txnvcZI1fm6cUwYLANtKt8dO6xd5qgK7ovqpzgIyP3LieHerkrswVYyhdcttYtlS&X-Amz-Signature=0b7254ec4fc40fa0080ba4a44a7774320e2fe01543851fc5a6a64e507efe3ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FGD366D%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T121059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDkc8PBKJ49axvj0kDcLmHk0lnwzZ%2BIsvPJ6vHy%2F3ypVgIhAJsHlTUZMNTfXABxZZMY5KTdch1PlEJpVF79aVlK0qFAKv8DCBoQABoMNjM3NDIzMTgzODA1Igwc3U0oPDHflF%2BqCUcq3APuCTDO1AOhDHzZ54EQuVJJ%2BP3YomICrWe103Wrc6mDi8lqajga7XUCk7H%2F%2BZ%2Ft%2FZ1tsnAQPedyFEXv8kZersww3%2F2KXZfQc%2Fy2FqFka5q7w9fgHPXXqh1E0FvALno6B%2FeQygnOKJrPNOBuF5NW2xAJ20GJY%2FpKxGBmOVz%2FIX2tdWUspEg9mK6j1LJXRD%2FUiIMFGy%2BnRdzfO2%2BNFrYB1L8PpiBxSmqN9A0DvfEL4OJvcQdhfAuicm4ez0IArNC5CqhX0Ft3XxYd%2Fo%2BJDg4lzrQA5AzPUZrBNmgjbqt3ToRuiaWkA1cnJ4UowTvfEDYNllK5faVAnvBWecQedmWdKEQAK6IISpH9j3FlckSGMAZW%2FJvDB1OGogqgbqjiPPZq0B6O1CykgEBF2j585AhBpRs%2F%2B4PAwhb5gpjn4knfIfTn3hvZPJ8v%2BeHkj0Rr2VT2DMw1gdIQyvbtvDVoNTO10569R7wKgxOUHbXni7I0i65rEi5W%2B%2FGS%2B8MQOxKdBAhQBTQnx1CUjJQwHuKwMcuSKnKB3nAgVM7LbgenrKSgoyWv03xFm77Gv%2BBDhR%2FwODYGMjnae39MjPMhroBVPqbLL9p6X%2FK6ifFw6lvWnXb6UYf6gyuoEf1wF56XqhtG3zCurOPVBjqkAdrd9TYYjBwSfJaz2cEc3SvlIcFv%2BMUjCeNEIkJanbrVwoUnlAM9Zv%2Bx8sXxuMOUViU8mIYjNg1IDaQ0E9FtZOu9hjNE3YgxsF00krHYOLP6LWIufNlhflgcmE4vFlcsHJYNm2gFhrb8lAsUSil6bOkDcXb7txnvcZI1fm6cUwYLANtKt8dO6xd5qgK7ovqpzgIyP3LieHerkrswVYyhdcttYtlS&X-Amz-Signature=1cd15a8105afb15a6a734e22218950fb28b06940c10a9d41c08c0805f6959e85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







