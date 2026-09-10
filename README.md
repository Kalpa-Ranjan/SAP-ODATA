



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNVEKSJG%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T180918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9vIPVne%2BKfRyoRpzyFnP18qdz1Him%2BGQaQk1vEjVd3AiA%2BZvkN8CBna%2BERulypTeLQsPj0xX62LPiSY0k%2BO2hmGyqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzpcysk%2BztE%2FydFsHKtwDFEMKkqbfMcIk8A98GJ3yUAajklnQZWJ%2FnhTejJv7ngMOefscW37x162sDKDr03tzaGEemXg5IWrA4ND8yDz92GBCXDWsSQTLeOUFcnMxgzOd%2BIUjeL%2Bgl%2BQAhbyt1Zq%2FUmGp8uuzegwgcL1pqwKOZ0qqZe4LBoND%2Fo5hcyh%2FZt3D9JUjq5MKGMsAk56%2Fq6YPRpf5JmV9pAHJ8sAES1zxMhfvYZZ2KMxw17hWkFavSwt5GH9Upq%2F1lLvpIR9QYRqG7E68V7ZpkhI1AJhyQoug2B73owJ8v7jQze4SBgudsvgvwoEWM6J%2FAIaTfdc%2FilyVj8DR6A0SnFcUxH0YB%2Byutq5Yi%2FdrlelzvSGRUx1%2FThaQuLQncW1P7jDBw7OhD%2FpK0GJRBW9jA93FMSmC%2BeE%2FJroeQDnf3f1D28%2Ffwb4O0g6AuTVz07%2F0pRhv%2BDXX5frFIt5%2B4CCoW%2Fo1KYqE%2FxqlucXzXcJWK8l9WIIRvukEbjHNFnrl%2FIPpjs1NuwDduNeoqjz4%2FIAcXaDbvQY4GePPo4j8Swk6dsdguzGBCSoE%2BSrjufSg%2FCngD9UA9OHpFgRV50ikNjMqgWOy%2B672EgADtDCbBIhPiiCQhd0wDvW%2F1lgwR9uwffZsE80Twu0wotuK1QY6pgFZqC9lvKIqmHWTLSSB78pwMeFLJP27X317TmZfQw%2FAQ8ZoTVpVgeAXiCQzGs84oVkrYIH9rpZSPXic8qsUhr3fSjAR6yW99n6AhkDoqY6fPS2HGKfJhJwrczujjjOv7dJ%2BY9wIusAf%2Fin%2Fm7Oc1w5y7vIkLK2afbdK9iPFWqOElWMfpZ8dDLb8l4JzhdvHEtkgLKfSX5MS3KPwMCgBC86Uf5MCerb4&X-Amz-Signature=dc6c06b8caa81aa7e597c1296413a6fa50bbbea3b0278ff856bc8b74733681b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNVEKSJG%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T180918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9vIPVne%2BKfRyoRpzyFnP18qdz1Him%2BGQaQk1vEjVd3AiA%2BZvkN8CBna%2BERulypTeLQsPj0xX62LPiSY0k%2BO2hmGyqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzpcysk%2BztE%2FydFsHKtwDFEMKkqbfMcIk8A98GJ3yUAajklnQZWJ%2FnhTejJv7ngMOefscW37x162sDKDr03tzaGEemXg5IWrA4ND8yDz92GBCXDWsSQTLeOUFcnMxgzOd%2BIUjeL%2Bgl%2BQAhbyt1Zq%2FUmGp8uuzegwgcL1pqwKOZ0qqZe4LBoND%2Fo5hcyh%2FZt3D9JUjq5MKGMsAk56%2Fq6YPRpf5JmV9pAHJ8sAES1zxMhfvYZZ2KMxw17hWkFavSwt5GH9Upq%2F1lLvpIR9QYRqG7E68V7ZpkhI1AJhyQoug2B73owJ8v7jQze4SBgudsvgvwoEWM6J%2FAIaTfdc%2FilyVj8DR6A0SnFcUxH0YB%2Byutq5Yi%2FdrlelzvSGRUx1%2FThaQuLQncW1P7jDBw7OhD%2FpK0GJRBW9jA93FMSmC%2BeE%2FJroeQDnf3f1D28%2Ffwb4O0g6AuTVz07%2F0pRhv%2BDXX5frFIt5%2B4CCoW%2Fo1KYqE%2FxqlucXzXcJWK8l9WIIRvukEbjHNFnrl%2FIPpjs1NuwDduNeoqjz4%2FIAcXaDbvQY4GePPo4j8Swk6dsdguzGBCSoE%2BSrjufSg%2FCngD9UA9OHpFgRV50ikNjMqgWOy%2B672EgADtDCbBIhPiiCQhd0wDvW%2F1lgwR9uwffZsE80Twu0wotuK1QY6pgFZqC9lvKIqmHWTLSSB78pwMeFLJP27X317TmZfQw%2FAQ8ZoTVpVgeAXiCQzGs84oVkrYIH9rpZSPXic8qsUhr3fSjAR6yW99n6AhkDoqY6fPS2HGKfJhJwrczujjjOv7dJ%2BY9wIusAf%2Fin%2Fm7Oc1w5y7vIkLK2afbdK9iPFWqOElWMfpZ8dDLb8l4JzhdvHEtkgLKfSX5MS3KPwMCgBC86Uf5MCerb4&X-Amz-Signature=57f39321bdb8f45323e84d09c2515358ea823d833d5b71425532bb10c0393e1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







