



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF4B635G%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpRjADpJiyZct7MkoRX4fa20OvJ4RGq1mvqbie2E7MSAIgB8N%2B%2BQQMdCnXT7ORlne8G04wyf2IM0qiEGwgnlh08Z4q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJNiOBZ0Cg9VBfuO9CrcA0UtjEk5yBt34p4zqPKwr4ODEoZ6aKDewsulEUjh9asmH%2BhlUnUFkHPTzxCtIwyUI%2FL3O7he9sQ95RO3CQZfNSzIjJJL9P1exZeXaEDCgxdLW1aPw8hO2SJJC9r9aM7QbkEZCmXmSILnI9rqt7ubmwNWlH3BsNLTh3bUdLUaKVN5Wkr95FrEpYD7jLu%2FuZUNA5xbyggcg5iwyJXKpj6OiiYzWhunj0%2F5grG2tsRgWs2JUSaP%2BmFAXMXcZ80yu%2BarazkU75F9jZEGhiX0xpG%2B9bPzCIpYZXXSt8lZKl68emfpkZeLWZnQTsl%2FwBi4mneJDtxsALZ2UZsLg7jFklYY7PXs8IkIj2dZEQKF3%2BrhX%2FaWQ4OjwLoEGLf7V8JpEP9ocum1SX5qmXu1zbM6xC6ivuVkoMsy2JY94coitzsTBcN44OxZg%2F2DuPwQe6%2F%2FMdg8iRCBQTjKzPkYkZWiCS7WEjtnyUcQ%2FU4sdbb4tUl%2FkARapRBN2r4YcqmrIZk7kqQzt7oGd6xdeakHPP4VOEgXKfBAcWKDC3M3cNAq%2Fj7lG8%2BzRt2xGbGaJgJanE%2FLGvg8fkRd6OMiLxbWq4Zf%2FubGoEwdbufVMx%2B8ARtNZddQN%2F%2B2fuLdwoydgScdYVF%2FMNWvm9AGOqUB45fVsv8O13CWeSkzZDTOfKWVrcgPYhXrZcNK%2Br834kpsomjPh46PIpGD3yUDYO%2FA3YlwRojuS9F5g43%2BgJPCL%2BP7u4UIUAG7G4PRnxwgq0ZM%2BlfL0595iv3YvYYdQJvI%2Bi%2FWdPi%2FjK13ktquSIV9o2GPXiGG1D7%2BC94PyOLQlERAlZ1mXfjVwl7%2BADwuLktoJIACaoduuok8F%2B9vweVZvjf19BJi&X-Amz-Signature=4400d1aefec8f7206b817273ef2f5b2fce9c106c0a32c0ce2d27416a3002a7e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF4B635G%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpRjADpJiyZct7MkoRX4fa20OvJ4RGq1mvqbie2E7MSAIgB8N%2B%2BQQMdCnXT7ORlne8G04wyf2IM0qiEGwgnlh08Z4q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJNiOBZ0Cg9VBfuO9CrcA0UtjEk5yBt34p4zqPKwr4ODEoZ6aKDewsulEUjh9asmH%2BhlUnUFkHPTzxCtIwyUI%2FL3O7he9sQ95RO3CQZfNSzIjJJL9P1exZeXaEDCgxdLW1aPw8hO2SJJC9r9aM7QbkEZCmXmSILnI9rqt7ubmwNWlH3BsNLTh3bUdLUaKVN5Wkr95FrEpYD7jLu%2FuZUNA5xbyggcg5iwyJXKpj6OiiYzWhunj0%2F5grG2tsRgWs2JUSaP%2BmFAXMXcZ80yu%2BarazkU75F9jZEGhiX0xpG%2B9bPzCIpYZXXSt8lZKl68emfpkZeLWZnQTsl%2FwBi4mneJDtxsALZ2UZsLg7jFklYY7PXs8IkIj2dZEQKF3%2BrhX%2FaWQ4OjwLoEGLf7V8JpEP9ocum1SX5qmXu1zbM6xC6ivuVkoMsy2JY94coitzsTBcN44OxZg%2F2DuPwQe6%2F%2FMdg8iRCBQTjKzPkYkZWiCS7WEjtnyUcQ%2FU4sdbb4tUl%2FkARapRBN2r4YcqmrIZk7kqQzt7oGd6xdeakHPP4VOEgXKfBAcWKDC3M3cNAq%2Fj7lG8%2BzRt2xGbGaJgJanE%2FLGvg8fkRd6OMiLxbWq4Zf%2FubGoEwdbufVMx%2B8ARtNZddQN%2F%2B2fuLdwoydgScdYVF%2FMNWvm9AGOqUB45fVsv8O13CWeSkzZDTOfKWVrcgPYhXrZcNK%2Br834kpsomjPh46PIpGD3yUDYO%2FA3YlwRojuS9F5g43%2BgJPCL%2BP7u4UIUAG7G4PRnxwgq0ZM%2BlfL0595iv3YvYYdQJvI%2Bi%2FWdPi%2FjK13ktquSIV9o2GPXiGG1D7%2BC94PyOLQlERAlZ1mXfjVwl7%2BADwuLktoJIACaoduuok8F%2B9vweVZvjf19BJi&X-Amz-Signature=6d54884fd8e9d1e0515d7a7075b9b36977ca9b2bc0cef2c2f29e45d042f6f709&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







