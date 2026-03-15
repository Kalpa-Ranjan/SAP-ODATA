



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCB2X2KC%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T015707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDSBfqJSwn9v0Z34cxOjQ%2Fhf9huDgCvBcG6RA1MlNYF7AiAw4LmnWi%2BH5mF9ReM%2B8oNa9eG5vfLVkOdHuehf17RlAyqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEDMr2oRXjQgTgt0bKtwDgkd436gqfWl5ZC0wSkiQBajOJNs7cubqtfN%2BgtDpEictx%2FQPdbGgQtrpCXm0Qd12aoH0ZtKiK1aDRN9DMn0rS3MLkKlKB0eWOsiiFUrd3DNsk2BTFLKF5j1k%2BZZqEIn1xx02%2FwpTpeLeB1QigrPkHDYCdK8PK0lbM9HyHV5O%2BMmpKxeADMjGxtgUpVS5XKqwhEvSbjNLc%2B%2BMVn8oOLiwCfR%2BVD%2Blv0nrQ50C0T4tymSe%2F2dGsveNyncxTaXu9FRxhK7nu%2BBIKwvhOpvJMNgzQ6T6en32HIP8D%2BlbtM50GeXePUXWGI2MbwyetPbDopqm%2FPURkOVmJad%2FAffje7GuxQ4%2BcDc2jekga8BehrTHnV42IU2jOWvLtzR4pcgC2FVsrlF5w1R5C%2B37TRa0SoprTf19FXHQ86ZunCPvkOU0hLzgfNXqcJqXy1mfv0ug0u9zjWmp1KUdrK9y058FUDjmGzz2YJPH76utnYD1QM03sVKDDXq4aZTa2s4wSW1IehdieO4RU5OvthkrPcTSI3o%2Fo59HoM9NCEyBpfArkzKA7fbNNsYjlz7otAJixyUFhAAr8SqIC0GZYA62%2B4MCubmTvVrxXjTZ2wMSvWo33ABOMumW28BJT0YpxYc4TPQw%2F4%2FYzQY6pgG0ZcVf80nuZDeLJ0GsstTo5olPic7mbiQLDclOBNX3exWk8FrlAYV%2BhqU55J7OE3JqtuDCcaJvC9Qgh9luZHu3RV0%2B9mANh9I8rdgNBd%2Bm3zrR6oa3pN2JFo9vw2cIB9HhevDDzI1d2VfeLDXsXUYGtO5WoeKz7pTkPgT0YwEmRXx7gMRYZLYFg4eacLn66bBt50%2FLnB%2BaWSZqo9Rb%2Bw7pyq9NgP4s&X-Amz-Signature=af682b648f0682f4faaf4ee97894feaaa7f7fb82f3cbaf0f659c3078e177074a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCB2X2KC%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T015707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDSBfqJSwn9v0Z34cxOjQ%2Fhf9huDgCvBcG6RA1MlNYF7AiAw4LmnWi%2BH5mF9ReM%2B8oNa9eG5vfLVkOdHuehf17RlAyqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEDMr2oRXjQgTgt0bKtwDgkd436gqfWl5ZC0wSkiQBajOJNs7cubqtfN%2BgtDpEictx%2FQPdbGgQtrpCXm0Qd12aoH0ZtKiK1aDRN9DMn0rS3MLkKlKB0eWOsiiFUrd3DNsk2BTFLKF5j1k%2BZZqEIn1xx02%2FwpTpeLeB1QigrPkHDYCdK8PK0lbM9HyHV5O%2BMmpKxeADMjGxtgUpVS5XKqwhEvSbjNLc%2B%2BMVn8oOLiwCfR%2BVD%2Blv0nrQ50C0T4tymSe%2F2dGsveNyncxTaXu9FRxhK7nu%2BBIKwvhOpvJMNgzQ6T6en32HIP8D%2BlbtM50GeXePUXWGI2MbwyetPbDopqm%2FPURkOVmJad%2FAffje7GuxQ4%2BcDc2jekga8BehrTHnV42IU2jOWvLtzR4pcgC2FVsrlF5w1R5C%2B37TRa0SoprTf19FXHQ86ZunCPvkOU0hLzgfNXqcJqXy1mfv0ug0u9zjWmp1KUdrK9y058FUDjmGzz2YJPH76utnYD1QM03sVKDDXq4aZTa2s4wSW1IehdieO4RU5OvthkrPcTSI3o%2Fo59HoM9NCEyBpfArkzKA7fbNNsYjlz7otAJixyUFhAAr8SqIC0GZYA62%2B4MCubmTvVrxXjTZ2wMSvWo33ABOMumW28BJT0YpxYc4TPQw%2F4%2FYzQY6pgG0ZcVf80nuZDeLJ0GsstTo5olPic7mbiQLDclOBNX3exWk8FrlAYV%2BhqU55J7OE3JqtuDCcaJvC9Qgh9luZHu3RV0%2B9mANh9I8rdgNBd%2Bm3zrR6oa3pN2JFo9vw2cIB9HhevDDzI1d2VfeLDXsXUYGtO5WoeKz7pTkPgT0YwEmRXx7gMRYZLYFg4eacLn66bBt50%2FLnB%2BaWSZqo9Rb%2Bw7pyq9NgP4s&X-Amz-Signature=ef4d8983c10cbef24a64ec535d90556b82e9efb6eb14be0338b13d544e632a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







