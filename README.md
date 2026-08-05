



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYGNLKJQ%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T135451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIG5KaAIVYfRSss6hJGbRcjHCqsO%2B5PTHhGli3e%2BlHRQwAiB28KfSlqe5qB4PYGU1koyYz26m%2FDQtJCn%2F7Tk3RmHjbyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMZ%2BWGaLSehR%2BhviCeKtwD%2FJAcpKs4hy57f6ljV%2FAm2ijpANzo1VkDxsdu%2BbR%2BlUBV9FESTgxI4YfjzI5xJ4ldlX82xPHWyxShpPihj%2FhEMNaOgqWO3QBbzXcP8u6w8FPD1Wgb2nyveG3xt5frnFT5zw3jGzyrgeKt4xu1jaPFFP%2FIAaWw5ZzZHXblXRWuMpv7RrIWwnNsDjdeGFNlq1jVebd0AMIX48BYIhhcy1mFP0jeEY36v%2Fgc%2Fmt2sjK35GNL6wW9UtTsg3YxeBgjJikq8cKihlajEJdgFWON78Yn0B%2F1a88%2BKa%2Fmirtg3hdgdn%2FXw0tSYwom25QiCB6isZsl1TcoTDGW5V75yk2XkMhXolAr2Ac70oOcBAbJNi8GtLobyG%2BjuduyNi96mDvMlekhFMib3LmhKYE9o1%2FF8UMY6IkOn2iLFhJLFbTVsPP%2Frd3l9MWdakUde3SeAhGrLjdmz3PxyPSz%2Fz0RkcI0V4%2BzWx1N4I9ldPoorHGeBdlVKkxReLCW%2FRs0sWv5gKp7A8NXLrOnLjlYPmbQPJ2vwXbDoGsSv5m%2F61jbV142gzVQGMqyY%2FKCmm%2F279rD5I1cql1jB6%2B9NakLR84JgiOYhOyzDv9%2F%2Bu24DAVXOApYHQzWhfXrSB4YjLEi%2FkRFroIw8%2BPM0wY6pgFaH1JZaJXQnfvGf%2Fhxb9pa%2FDlDakSifMZq%2FqzsZP%2B46H2n017L2cAdkN5Xr9yRcWIWOWSzLOn3p9dNy88z%2FCgwOqB4P6GBMxluCPHacfsEpUWqPJRCl5%2BGVZJ1bvEtdAT2hXMwa85%2B3j08f5yUmS4GxJZ38yBT1pZ68YlPz4C4%2FTZ3DmZd2wd7wXHlUcp3ILGeBuT75ogy7Sr6wYfz164XupRsJXAC&X-Amz-Signature=1837afc4033ecc83933e0dd637ee223bbe9e6c15085b105c4030084a25bb9ce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYGNLKJQ%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T135451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIG5KaAIVYfRSss6hJGbRcjHCqsO%2B5PTHhGli3e%2BlHRQwAiB28KfSlqe5qB4PYGU1koyYz26m%2FDQtJCn%2F7Tk3RmHjbyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMZ%2BWGaLSehR%2BhviCeKtwD%2FJAcpKs4hy57f6ljV%2FAm2ijpANzo1VkDxsdu%2BbR%2BlUBV9FESTgxI4YfjzI5xJ4ldlX82xPHWyxShpPihj%2FhEMNaOgqWO3QBbzXcP8u6w8FPD1Wgb2nyveG3xt5frnFT5zw3jGzyrgeKt4xu1jaPFFP%2FIAaWw5ZzZHXblXRWuMpv7RrIWwnNsDjdeGFNlq1jVebd0AMIX48BYIhhcy1mFP0jeEY36v%2Fgc%2Fmt2sjK35GNL6wW9UtTsg3YxeBgjJikq8cKihlajEJdgFWON78Yn0B%2F1a88%2BKa%2Fmirtg3hdgdn%2FXw0tSYwom25QiCB6isZsl1TcoTDGW5V75yk2XkMhXolAr2Ac70oOcBAbJNi8GtLobyG%2BjuduyNi96mDvMlekhFMib3LmhKYE9o1%2FF8UMY6IkOn2iLFhJLFbTVsPP%2Frd3l9MWdakUde3SeAhGrLjdmz3PxyPSz%2Fz0RkcI0V4%2BzWx1N4I9ldPoorHGeBdlVKkxReLCW%2FRs0sWv5gKp7A8NXLrOnLjlYPmbQPJ2vwXbDoGsSv5m%2F61jbV142gzVQGMqyY%2FKCmm%2F279rD5I1cql1jB6%2B9NakLR84JgiOYhOyzDv9%2F%2Bu24DAVXOApYHQzWhfXrSB4YjLEi%2FkRFroIw8%2BPM0wY6pgFaH1JZaJXQnfvGf%2Fhxb9pa%2FDlDakSifMZq%2FqzsZP%2B46H2n017L2cAdkN5Xr9yRcWIWOWSzLOn3p9dNy88z%2FCgwOqB4P6GBMxluCPHacfsEpUWqPJRCl5%2BGVZJ1bvEtdAT2hXMwa85%2B3j08f5yUmS4GxJZ38yBT1pZ68YlPz4C4%2FTZ3DmZd2wd7wXHlUcp3ILGeBuT75ogy7Sr6wYfz164XupRsJXAC&X-Amz-Signature=ac533a39e878364dbbac9780cef6ef4e4e266789d36235a7db994a9d6d9d1ed7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







