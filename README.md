



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DYG3Z6D%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T125359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIDqSAWnVxVT35zXj%2FOpviZcFBI1H5eVIvO9eb1Z9oAPHAiAVpXnBd7DkSCzj7hGA%2BNmtonY2h3N7tWboh6tg1E8ZYSr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM28gy9%2Fi8JHe5K7v%2BKtwD8uhIt41cXTOaiuACy0okYhSfn3SkHaFC0tMx%2BteoF0BR9MECioJ4NMR5RN6SgwH20xCqE%2BbtLtS4ojzUgidcu4Ub05iyp8KpKWAt98qGQvnyIbyhEGJ6CuTjv7sBs7za6qTEk7wnkjQkpWKtiDribNhziWqiHFA7s2INc83Cxo2R2Atv05WvduGPwdEfLXxNI2UbQbWP817IzlTNNss22oIRY3O%2Fl9%2FFqwnwlPBuxo%2Fu72CGlD8g6%2BnWGDIlVWyKKgZ%2BOiLEDK%2BDqw8y7i7168bbInUf6Ru7QEspIeXzYNoWslALuW7lBKSNE5rPRdLg9N%2Bqw55pTtKKlhqg%2B%2BC4%2BAG5z%2B7mmSv7ZcrQu7f8%2Bp9f7tOSgiszJpnbxIwDqqv2SLhdor1NjJSq4k4FfvuFyCm%2FIAbdw%2BWD4gtomVfniA%2FgQfICYIeVwbsUrre%2Fh3tPdeujKivM1lJyRMYhV26N%2FxcMpWM6VC6zpP9PGyYl6c6uk0llLHc%2Bi%2FuOgArAGKeXOj26QIJ3vya6jcApGfGwIV0vDNqD6Lava0%2BJmYF1dzEq34gdJ2Ibmfc%2BeZfCVTGLTpNrd1y5WAoEHvOK7gVHp3rpd2hHb1TuHCguGqrLMn%2F62i5Btvklq48vzKgwwcLvzQY6pgERlK98YemPSj4D4T31XNbgX6Z7iu1gCOyLeisdIYYqTpEnm%2Fqz3%2FsiAaAs0KGoVJVJqmBRMN%2F2DiuRXC9GigbXNeADEcVOcIEa4Hc5xy%2BpowlLDvphqyTrQRT%2B5U%2FYkXn06t24t4%2BOwJrnLI2K17Bhs2Tu59Ne5lTIZcE1b2JcvCV9r2Z1%2FysI5sLY0Y02r%2FiNuxCoNailQHenOeOU%2BC4mD7BLVYD6&X-Amz-Signature=960fcd4205157f8a479c86f3306d9b0095e94e9f534b467d61233e1420f59fdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DYG3Z6D%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T125359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJGMEQCIDqSAWnVxVT35zXj%2FOpviZcFBI1H5eVIvO9eb1Z9oAPHAiAVpXnBd7DkSCzj7hGA%2BNmtonY2h3N7tWboh6tg1E8ZYSr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIM28gy9%2Fi8JHe5K7v%2BKtwD8uhIt41cXTOaiuACy0okYhSfn3SkHaFC0tMx%2BteoF0BR9MECioJ4NMR5RN6SgwH20xCqE%2BbtLtS4ojzUgidcu4Ub05iyp8KpKWAt98qGQvnyIbyhEGJ6CuTjv7sBs7za6qTEk7wnkjQkpWKtiDribNhziWqiHFA7s2INc83Cxo2R2Atv05WvduGPwdEfLXxNI2UbQbWP817IzlTNNss22oIRY3O%2Fl9%2FFqwnwlPBuxo%2Fu72CGlD8g6%2BnWGDIlVWyKKgZ%2BOiLEDK%2BDqw8y7i7168bbInUf6Ru7QEspIeXzYNoWslALuW7lBKSNE5rPRdLg9N%2Bqw55pTtKKlhqg%2B%2BC4%2BAG5z%2B7mmSv7ZcrQu7f8%2Bp9f7tOSgiszJpnbxIwDqqv2SLhdor1NjJSq4k4FfvuFyCm%2FIAbdw%2BWD4gtomVfniA%2FgQfICYIeVwbsUrre%2Fh3tPdeujKivM1lJyRMYhV26N%2FxcMpWM6VC6zpP9PGyYl6c6uk0llLHc%2Bi%2FuOgArAGKeXOj26QIJ3vya6jcApGfGwIV0vDNqD6Lava0%2BJmYF1dzEq34gdJ2Ibmfc%2BeZfCVTGLTpNrd1y5WAoEHvOK7gVHp3rpd2hHb1TuHCguGqrLMn%2F62i5Btvklq48vzKgwwcLvzQY6pgERlK98YemPSj4D4T31XNbgX6Z7iu1gCOyLeisdIYYqTpEnm%2Fqz3%2FsiAaAs0KGoVJVJqmBRMN%2F2DiuRXC9GigbXNeADEcVOcIEa4Hc5xy%2BpowlLDvphqyTrQRT%2B5U%2FYkXn06t24t4%2BOwJrnLI2K17Bhs2Tu59Ne5lTIZcE1b2JcvCV9r2Z1%2FysI5sLY0Y02r%2FiNuxCoNailQHenOeOU%2BC4mD7BLVYD6&X-Amz-Signature=577973594393002f4b06ba42baefd328abb0e23530f694715c2da0b1e2cbb4df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







