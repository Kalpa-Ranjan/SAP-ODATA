



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA3NONYV%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T132130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCICeIc1DOHi0gDTUSGfAaEikLw5Py5%2FSRLNRUOWG9J%2FjiAiEAjF3PLAesl8zYXRmbMIL97lcuMFYyFb6YlYqQZw%2BQrWQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEFRW28PYMfaUoI9FircA83nYDzVTdbEkkKLmZIqLhQIUU%2BdOHwDj3Q2ovD9IPmmcLF%2FXJJlhPa4OLnlvVOwVQqAJP%2BTdSKRsJ8mnIAuHsLS9XFTH296VZB%2F5OeZivIJFgAxePzW9iXuDRvMynDZ0%2BAzbD%2FcimjOGJxZzE7Vwt0easdXyLfbxEN1yYIHc7Y%2B%2BGU5jUsgwdpnhx3%2FhrrvbRkf3T1KRR7UlitoTNIMLC97h8N677HTrTYDxorGtmjK9xTi6cB63rPo4zPWYHS9IOV6ASL7w%2Bmx810B3Z9TDSJwP2AMj6i9b7s6K%2BMnCOOjVZej8B%2FjhVFdA7lnHEPJCMIO%2FIl8Q%2Bj%2FQZhEJ0fVlksraRvbgJHpMKSjWzJrdB1jl6ujKjUDewJHEDqlVH67Uj15HqsoeViFFXFKD1Kz6fCnmc4fmf8rcrKdUaUjx%2FOyugiX6hKd%2F%2BqPsngwj0SsBU%2FW5V3wKcPyhGcEwuEpf8y4zNXsIsu7QihGTPCaAB%2FaLrAcBWz1iSdNaS0L63goQlJ5ABYxPEX3qSU5KnAiRncwQV03xTSFtxHjzkB8eOjqJ8Amf585iIzvMiQBcWjVvoWPCGkgLyY1N6bHJrys7SoSEHhFatC6aTnoTeB2XyM2t9B0faTsaAvqaHV4MM7J19IGOqUB9SzIqi2o4Suj%2BLCDpyemcUdUgo2kMDOXCwd9d5meOqhfi7XADaG9uIw47Hdmf6cL8exGm848K0BzPxyropMb5XgZGLY%2F0Fueyft%2B5ee%2BtHxuR0QnS7jdhyYnpISeD%2B01jNxPw4d4IfDKHUAqv22MDtuii6SgoReN0ueHH2AAwIX2CzNDl07bHtzQgmcEpP9aebani0KPJ7W1Kwu6g24E%2BMQmTPnH&X-Amz-Signature=cca76ec7c0712de1195473f9a0febf51573218b337994c5bf5e56f369b4a125d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA3NONYV%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T132130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCICeIc1DOHi0gDTUSGfAaEikLw5Py5%2FSRLNRUOWG9J%2FjiAiEAjF3PLAesl8zYXRmbMIL97lcuMFYyFb6YlYqQZw%2BQrWQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEFRW28PYMfaUoI9FircA83nYDzVTdbEkkKLmZIqLhQIUU%2BdOHwDj3Q2ovD9IPmmcLF%2FXJJlhPa4OLnlvVOwVQqAJP%2BTdSKRsJ8mnIAuHsLS9XFTH296VZB%2F5OeZivIJFgAxePzW9iXuDRvMynDZ0%2BAzbD%2FcimjOGJxZzE7Vwt0easdXyLfbxEN1yYIHc7Y%2B%2BGU5jUsgwdpnhx3%2FhrrvbRkf3T1KRR7UlitoTNIMLC97h8N677HTrTYDxorGtmjK9xTi6cB63rPo4zPWYHS9IOV6ASL7w%2Bmx810B3Z9TDSJwP2AMj6i9b7s6K%2BMnCOOjVZej8B%2FjhVFdA7lnHEPJCMIO%2FIl8Q%2Bj%2FQZhEJ0fVlksraRvbgJHpMKSjWzJrdB1jl6ujKjUDewJHEDqlVH67Uj15HqsoeViFFXFKD1Kz6fCnmc4fmf8rcrKdUaUjx%2FOyugiX6hKd%2F%2BqPsngwj0SsBU%2FW5V3wKcPyhGcEwuEpf8y4zNXsIsu7QihGTPCaAB%2FaLrAcBWz1iSdNaS0L63goQlJ5ABYxPEX3qSU5KnAiRncwQV03xTSFtxHjzkB8eOjqJ8Amf585iIzvMiQBcWjVvoWPCGkgLyY1N6bHJrys7SoSEHhFatC6aTnoTeB2XyM2t9B0faTsaAvqaHV4MM7J19IGOqUB9SzIqi2o4Suj%2BLCDpyemcUdUgo2kMDOXCwd9d5meOqhfi7XADaG9uIw47Hdmf6cL8exGm848K0BzPxyropMb5XgZGLY%2F0Fueyft%2B5ee%2BtHxuR0QnS7jdhyYnpISeD%2B01jNxPw4d4IfDKHUAqv22MDtuii6SgoReN0ueHH2AAwIX2CzNDl07bHtzQgmcEpP9aebani0KPJ7W1Kwu6g24E%2BMQmTPnH&X-Amz-Signature=19509f23a4920b0f39cf97954ec20ba82058d1486351d46c902f24c655a35c69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







