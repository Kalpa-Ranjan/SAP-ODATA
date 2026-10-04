



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYKHA3FC%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T010253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRtPhCGZjcPeODRstgzpnRfFHNbqK8MALUaHArAMJphAIhAIb%2FOjkxobSOnw%2B6ZjmJpZMxhmnZC01PkoYlrwwpLfD3KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0vRRGvMswBnw%2BrWUq3ANl9uhN41zqQ9SNzOlCAVcOa4gEXyDJxLqdcGEHCLkQ5LO10isGWv27eYk8%2BZGWE4cIKKVWCsYZgwyo0skiiG562nf%2F4DtYm%2FUEEJoH2Cpdt0ckuE%2B7H7QQcBoKZhGDQMDIzIN88D1dmYKo%2F6PmL%2Fnt6WOpk6Yqe3XTBEN9rF7%2BT1gwUJl5MdKFR4SZqP8CoraxkY%2FUJfomGaVMSn76s9CIxugXbCX4ZAYZdhOvzkST%2BqQr05HJSvgthETJcjFvIsZnEGI9p7gkz0cpM2221PS0Ha893nns6JY5FGw0hhK3NHZChHwn4rNHKSeAB%2Bp2wWMnzbFgRK8JMtqxEjRzetfzZp6fxmQuVYJlJi%2BpBRhNvpzTdaWgVVyCrgm17EAEtErAsfwTFuCjj3Bfm29XkC88ceuArMo8R44vzmbvnE%2FN%2BWv9LSn3cgvVXCzqy3G82h3gZl0fk%2BDBlKZtxVHMUUAIE%2FuS8ztKknXY7Vb95Qy4DYe4BqlqT2NoEma%2BdjaMIEJmuV59nJbfctV97ioCifiKFbhHvgfz5y1eqPhNHIMwbF5SNN2n8spE8AGY%2BwyD5ugEJCxGpx%2FeJjHhfQtXvc09A4J75ur4e%2Fwy1u%2BjySRgKe7XhDKXf%2BARdlKBwTCvqobWBjqkAVkc7NKw%2BLvv9Lt5qvPkqEkHlnzTOHrUait3F%2FO2K7ybIxQqY8nespoeMmXRGcs2ZCxssZwFK1Wevq8%2B5l4ywI2iQPhNL1F2fohgt8Lkwi%2FEB3B0qPmj%2BnITJEihyod6tK5GspvjVivCDyHfOaJDpExKHEQ8aYJwiF6AnribSV2VsLhNkWf4e5vl9wiR1I4%2FI2VbJRjtgcyNIw7bPFocbey4UFmq&X-Amz-Signature=e985958e3879482aa35277e530dbdbace400b13853b5fe4db95a97619d4dece8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYKHA3FC%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T010253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRtPhCGZjcPeODRstgzpnRfFHNbqK8MALUaHArAMJphAIhAIb%2FOjkxobSOnw%2B6ZjmJpZMxhmnZC01PkoYlrwwpLfD3KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0vRRGvMswBnw%2BrWUq3ANl9uhN41zqQ9SNzOlCAVcOa4gEXyDJxLqdcGEHCLkQ5LO10isGWv27eYk8%2BZGWE4cIKKVWCsYZgwyo0skiiG562nf%2F4DtYm%2FUEEJoH2Cpdt0ckuE%2B7H7QQcBoKZhGDQMDIzIN88D1dmYKo%2F6PmL%2Fnt6WOpk6Yqe3XTBEN9rF7%2BT1gwUJl5MdKFR4SZqP8CoraxkY%2FUJfomGaVMSn76s9CIxugXbCX4ZAYZdhOvzkST%2BqQr05HJSvgthETJcjFvIsZnEGI9p7gkz0cpM2221PS0Ha893nns6JY5FGw0hhK3NHZChHwn4rNHKSeAB%2Bp2wWMnzbFgRK8JMtqxEjRzetfzZp6fxmQuVYJlJi%2BpBRhNvpzTdaWgVVyCrgm17EAEtErAsfwTFuCjj3Bfm29XkC88ceuArMo8R44vzmbvnE%2FN%2BWv9LSn3cgvVXCzqy3G82h3gZl0fk%2BDBlKZtxVHMUUAIE%2FuS8ztKknXY7Vb95Qy4DYe4BqlqT2NoEma%2BdjaMIEJmuV59nJbfctV97ioCifiKFbhHvgfz5y1eqPhNHIMwbF5SNN2n8spE8AGY%2BwyD5ugEJCxGpx%2FeJjHhfQtXvc09A4J75ur4e%2Fwy1u%2BjySRgKe7XhDKXf%2BARdlKBwTCvqobWBjqkAVkc7NKw%2BLvv9Lt5qvPkqEkHlnzTOHrUait3F%2FO2K7ybIxQqY8nespoeMmXRGcs2ZCxssZwFK1Wevq8%2B5l4ywI2iQPhNL1F2fohgt8Lkwi%2FEB3B0qPmj%2BnITJEihyod6tK5GspvjVivCDyHfOaJDpExKHEQ8aYJwiF6AnribSV2VsLhNkWf4e5vl9wiR1I4%2FI2VbJRjtgcyNIw7bPFocbey4UFmq&X-Amz-Signature=fdea228738cff6d392f2b547706e14ca538c97d99a93c6053c35bf76a21a57ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







