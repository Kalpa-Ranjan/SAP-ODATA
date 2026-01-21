



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCM5WE2F%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T062922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd9SeNDHE%2BAI4irmJMIw%2BhqmTtibB6YL%2B9%2BVSBrfQVqQIhANyc6mtvyhawAHENGplhNVp3qoZa1MUVEU1Iq936d4thKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVpiMUUPEAvtsMmUIq3AM8evF9e9efyX9C0GFICZNpyI1M2rz47K8vHpaepOzvJTu3cuJkhrmyTSIhir5jZuAWNyz9shZOxZ53mmzX2SE8mCHSzH3RShSv8FjviwO3GALANc209ekvj0hlD1evfidSStd%2Bt8A4wnI3I3shRTMEUVF5kwJiSHmq7ObZ165dUneXYQc1giDJBzI9OwjDFPFeNSQgT6Wi7YKy37GCmJ0WRtIttSSe2%2FlVcepq654dpDZx%2FF7NvH5aF%2FQ5aRUWS58MZlhGIEEv3iu2QXEf6DOyMQoYgDaTlLNbnzQxuLUJs3a9B6hSe%2FigrgVPmaZ5R9qMNvYKW9xG4Lk7KnkWkPAZqr%2B93KYGbdOQpMB5Gc6T6cN1miIV9jZtJy31g%2BMReGpDdin7XA969onWwW8f1k0euU9UBbpqui%2FIqg4ddqPAzkw4%2Fv0q4JHtCn539DE2P6491nE3kWXSu%2FTLKNfmNb9caLAs6UQ9UQivnGNOH85%2Brsl2UiPlCubfB3vFV08O1e9cyDzfM7vWpnXQFYsGpIm7CXC%2B5uEPrDCltK84VyhcGhLT%2FfDvRFHeETxkNDnakMlyxle7m88Mbgv55Jc5sSIDwqZ9TFZqyG1AP25bbr6IKbWimaaftnQkWOOpKjCGzsHLBjqkAZjSA5BdgDT2W9HErzloRGhzDRjhQzxo9KzPY8bC%2FLUaxI63rQFu5yhncYDHJLTiDJzJlBAQ0XFWeVYlx0L%2F5HtxCscADyVEAp5Gdtu4u5bFtA0jgmgTmAmmLrcs8tS58vD8i4sTBrYVZqeOHJqlXWy5jMgfmALJuybajX080o6iRaCIovjwQrAcdktiMxgvXJdLLE9kes8ZSNqDUfGeo1ukJxsK&X-Amz-Signature=edef03c57afad6a02fd76d53ef3dba37451b92a3b51634ab7a07781cb83c1d95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCM5WE2F%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T062922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd9SeNDHE%2BAI4irmJMIw%2BhqmTtibB6YL%2B9%2BVSBrfQVqQIhANyc6mtvyhawAHENGplhNVp3qoZa1MUVEU1Iq936d4thKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVpiMUUPEAvtsMmUIq3AM8evF9e9efyX9C0GFICZNpyI1M2rz47K8vHpaepOzvJTu3cuJkhrmyTSIhir5jZuAWNyz9shZOxZ53mmzX2SE8mCHSzH3RShSv8FjviwO3GALANc209ekvj0hlD1evfidSStd%2Bt8A4wnI3I3shRTMEUVF5kwJiSHmq7ObZ165dUneXYQc1giDJBzI9OwjDFPFeNSQgT6Wi7YKy37GCmJ0WRtIttSSe2%2FlVcepq654dpDZx%2FF7NvH5aF%2FQ5aRUWS58MZlhGIEEv3iu2QXEf6DOyMQoYgDaTlLNbnzQxuLUJs3a9B6hSe%2FigrgVPmaZ5R9qMNvYKW9xG4Lk7KnkWkPAZqr%2B93KYGbdOQpMB5Gc6T6cN1miIV9jZtJy31g%2BMReGpDdin7XA969onWwW8f1k0euU9UBbpqui%2FIqg4ddqPAzkw4%2Fv0q4JHtCn539DE2P6491nE3kWXSu%2FTLKNfmNb9caLAs6UQ9UQivnGNOH85%2Brsl2UiPlCubfB3vFV08O1e9cyDzfM7vWpnXQFYsGpIm7CXC%2B5uEPrDCltK84VyhcGhLT%2FfDvRFHeETxkNDnakMlyxle7m88Mbgv55Jc5sSIDwqZ9TFZqyG1AP25bbr6IKbWimaaftnQkWOOpKjCGzsHLBjqkAZjSA5BdgDT2W9HErzloRGhzDRjhQzxo9KzPY8bC%2FLUaxI63rQFu5yhncYDHJLTiDJzJlBAQ0XFWeVYlx0L%2F5HtxCscADyVEAp5Gdtu4u5bFtA0jgmgTmAmmLrcs8tS58vD8i4sTBrYVZqeOHJqlXWy5jMgfmALJuybajX080o6iRaCIovjwQrAcdktiMxgvXJdLLE9kes8ZSNqDUfGeo1ukJxsK&X-Amz-Signature=bca470221276948b71258e3e92da4f0a0c5f5f12f2c3e72a60277de24460b92b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







