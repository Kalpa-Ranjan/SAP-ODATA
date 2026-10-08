



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MWCAXVH%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T180951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCmO8khfPcU7w4eF4aVUlBdk%2B1jtajGC8G6jeivnzzlWAIgOqt0u2qPFU9KGUtczlw00XevYsHJgUS24OPWmex5PMwq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDOU1WhefXuzhOJN78CrcAzN%2F4iXg%2BX43AKg8J2b0X554FyC45ToWgDfCBkIhMQSuRcfoXSWUhPatZ2eaadHRSldQdRVvZJFu91D6%2F6OEoTMzzXHNhT3n8Y%2BCmL51T%2BNOJ66VrcHQHg5mhAXnK1BXEOAnsQEDwXyhpYP4JKkMJkhLFsvYKcQssRvWolL1tt9%2FY2zPzm0E8XAFEcOmkAod3feopAAJLYOy%2BQ%2Fmx%2BZFBNuNMwKnJ18yq7pGD3lZdlR%2FYXeeBlcCwfVy6i8ndW8x07fRgbUPNt4YWYKxrT9ADUAsgfmgOMmyqjGeS1720V%2BB%2BpoZl7dmUISmM%2F5s%2BW%2BEw8FAj9x3t34MVcxUAexRHjyzWd0AEfbTLc7AkGsRT%2FH94G0wFvqrvN0wosjNIsdlfQ0m6js87DAcXb3yU3cPfdCifEHVuOfPKLX7RMy%2BcDmgOZKhIQX8X8MR61Xj0%2BiFwCujUnEg1wRtC0FAYSv5BGxoCvguwQZFeLdL6Vwq8tKvxUyYXsZeIT%2BMdpkDvLG6Fp3gS%2BLsHxLAXqX507ivgK44Ln61b9ToRXBp2sEbJfrKXpHMC6aXZcHGUFB%2F4SAMJKu2pEv5jpXux0nwS%2BmqZdzeuRo47barVo97fV1cmL7M9vTjEOrbmB9MPQn0MOfxntYGOqUBSDUC7K51E6ejHiq4u0T2bxP0ow6dQzRE4e%2BI7xSKJJQ0gVIxju4hRryIlDz3WBliP%2FlKIrpApgXElrfu3CaU%2FKAucdTAwKku7%2Fwd9tTwNfqzHvXP37r6ShGnEWQc1CHZ0RUaD%2BCbTThoeN9WrNRCza7ZuJGDs15ZSq3fQlhGN1hN7npdpYzlpkPMlJs24nF6wtNkAQjIZS0RftE%2FBlev4O1cqkgP&X-Amz-Signature=eadf5a6669940d1a4cc83c864dedb8a00cef1955e3f7ae5a00b8648805b0f21a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MWCAXVH%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T180951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCmO8khfPcU7w4eF4aVUlBdk%2B1jtajGC8G6jeivnzzlWAIgOqt0u2qPFU9KGUtczlw00XevYsHJgUS24OPWmex5PMwq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDOU1WhefXuzhOJN78CrcAzN%2F4iXg%2BX43AKg8J2b0X554FyC45ToWgDfCBkIhMQSuRcfoXSWUhPatZ2eaadHRSldQdRVvZJFu91D6%2F6OEoTMzzXHNhT3n8Y%2BCmL51T%2BNOJ66VrcHQHg5mhAXnK1BXEOAnsQEDwXyhpYP4JKkMJkhLFsvYKcQssRvWolL1tt9%2FY2zPzm0E8XAFEcOmkAod3feopAAJLYOy%2BQ%2Fmx%2BZFBNuNMwKnJ18yq7pGD3lZdlR%2FYXeeBlcCwfVy6i8ndW8x07fRgbUPNt4YWYKxrT9ADUAsgfmgOMmyqjGeS1720V%2BB%2BpoZl7dmUISmM%2F5s%2BW%2BEw8FAj9x3t34MVcxUAexRHjyzWd0AEfbTLc7AkGsRT%2FH94G0wFvqrvN0wosjNIsdlfQ0m6js87DAcXb3yU3cPfdCifEHVuOfPKLX7RMy%2BcDmgOZKhIQX8X8MR61Xj0%2BiFwCujUnEg1wRtC0FAYSv5BGxoCvguwQZFeLdL6Vwq8tKvxUyYXsZeIT%2BMdpkDvLG6Fp3gS%2BLsHxLAXqX507ivgK44Ln61b9ToRXBp2sEbJfrKXpHMC6aXZcHGUFB%2F4SAMJKu2pEv5jpXux0nwS%2BmqZdzeuRo47barVo97fV1cmL7M9vTjEOrbmB9MPQn0MOfxntYGOqUBSDUC7K51E6ejHiq4u0T2bxP0ow6dQzRE4e%2BI7xSKJJQ0gVIxju4hRryIlDz3WBliP%2FlKIrpApgXElrfu3CaU%2FKAucdTAwKku7%2Fwd9tTwNfqzHvXP37r6ShGnEWQc1CHZ0RUaD%2BCbTThoeN9WrNRCza7ZuJGDs15ZSq3fQlhGN1hN7npdpYzlpkPMlJs24nF6wtNkAQjIZS0RftE%2FBlev4O1cqkgP&X-Amz-Signature=4fecf8fda95b8d56f1256ed4548dad8d9ccf58ed25a0c6816daa65e8626fc1bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







