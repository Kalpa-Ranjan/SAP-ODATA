



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF3HTZY6%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T032927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJGMEQCICqylGENGh%2FD1GFcT97n7qfAwhbSvIKXeDcwhCU%2FXLUUAiBxyJpaFCxFdmbP%2BQMiFWr%2F7llLSECY9SLJnYw4ycOf8Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMlCdk7jiv%2F0o4nC2EKtwD%2FD3smIqz4l3YWesRWph9GqG0DFaZ%2BTxX11IjGqaRapJCTyRGWKwaXaWEqfNVZLdGrec4uux%2Ft68vfhSicz8yAUGxVrG0lVknIeCu7jh2KbVZTPltrwQVO09b8JxwczicFJ4RDGZAJyEiyDftHuFsmdv3WMpHbKza6iRJzgy3iUf%2F%2FvJSRXc0CSldkPMCAXT5xhLpj8fEyaEkieOGp9%2BuWb1BKs1rKekjdpGcO2iAmCxsTElfPlhDtMz6JVrP2jb7K3ob%2BCvYtO2ISbVgGdHep3%2Bx8hPb29qiT6nPjkQdGEW51IkzxmktjBHvWM6jd89gqBc4JCyBRTFHfrIw%2BH2X8rb5%2FwsaFpRgjvwd82W17n8VxQN2sFDRr1juPR4o1ZrnJjxdOtnRi1AQz%2BcRQMoK7mk6xGBfYYynMu11eX7b2f8W2bYEjELVmwNiHO1yBBNqfkft%2FMcHn6EhczDhh50DMepND1TVX%2B89QJWvmj7H2NaeKnXNSh54G0WOWT1B6XZcjTNbuVeB7zp5CfJVA35JXW2DyxSDrqxNHUnCYQpKMqcVkUa386n%2BOJCYIbEReVqnj29RZ8SvB2trVgs75C4Z6e9ysTFMalb0hOj6u7BDi%2BYlwrdQ0qQGA2O2wd0w3Yf40AY6pgH1Cy0UbAHSQfds6prKjbvNZ%2BXeqRpzocwHELulo%2FgKfer3UkXbrWOLHKrOJuK9h0HXNciYiiHotGcKJiXEkoi%2FS2w3vazMFv%2F0pNORENzK5XU8t0mF%2FglHqfxZ5sBOr9xLcxAyERXQWqBlW6MTGu%2BtBTHumC2pt4CoHYDTqsqQrvWT2SpGyMBwUA2vZTiZ%2BI1wEyLrBSuuK9N4p3Tnh5vdVUaL9uxO&X-Amz-Signature=828196e93a4e1da52f3b711d52fd297e5d704bae5a6996755b198efdc7589299&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF3HTZY6%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T032927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJGMEQCICqylGENGh%2FD1GFcT97n7qfAwhbSvIKXeDcwhCU%2FXLUUAiBxyJpaFCxFdmbP%2BQMiFWr%2F7llLSECY9SLJnYw4ycOf8Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMlCdk7jiv%2F0o4nC2EKtwD%2FD3smIqz4l3YWesRWph9GqG0DFaZ%2BTxX11IjGqaRapJCTyRGWKwaXaWEqfNVZLdGrec4uux%2Ft68vfhSicz8yAUGxVrG0lVknIeCu7jh2KbVZTPltrwQVO09b8JxwczicFJ4RDGZAJyEiyDftHuFsmdv3WMpHbKza6iRJzgy3iUf%2F%2FvJSRXc0CSldkPMCAXT5xhLpj8fEyaEkieOGp9%2BuWb1BKs1rKekjdpGcO2iAmCxsTElfPlhDtMz6JVrP2jb7K3ob%2BCvYtO2ISbVgGdHep3%2Bx8hPb29qiT6nPjkQdGEW51IkzxmktjBHvWM6jd89gqBc4JCyBRTFHfrIw%2BH2X8rb5%2FwsaFpRgjvwd82W17n8VxQN2sFDRr1juPR4o1ZrnJjxdOtnRi1AQz%2BcRQMoK7mk6xGBfYYynMu11eX7b2f8W2bYEjELVmwNiHO1yBBNqfkft%2FMcHn6EhczDhh50DMepND1TVX%2B89QJWvmj7H2NaeKnXNSh54G0WOWT1B6XZcjTNbuVeB7zp5CfJVA35JXW2DyxSDrqxNHUnCYQpKMqcVkUa386n%2BOJCYIbEReVqnj29RZ8SvB2trVgs75C4Z6e9ysTFMalb0hOj6u7BDi%2BYlwrdQ0qQGA2O2wd0w3Yf40AY6pgH1Cy0UbAHSQfds6prKjbvNZ%2BXeqRpzocwHELulo%2FgKfer3UkXbrWOLHKrOJuK9h0HXNciYiiHotGcKJiXEkoi%2FS2w3vazMFv%2F0pNORENzK5XU8t0mF%2FglHqfxZ5sBOr9xLcxAyERXQWqBlW6MTGu%2BtBTHumC2pt4CoHYDTqsqQrvWT2SpGyMBwUA2vZTiZ%2BI1wEyLrBSuuK9N4p3Tnh5vdVUaL9uxO&X-Amz-Signature=2ac15336240c946224c2e29656efc467b7ad54a24667403e5300ea50cea47279&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







