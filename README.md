



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO5F5TWS%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T200943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQDoem43uxTexcRszkXcowEQoLlHmB8bAkxlc37s%2FIJBqQIhAOrryGQwv80AsMRH%2BEYcDyRwC%2FElhVKl7hoIKVG78fAeKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzdac78GbvuIHR%2FWTEq3AMm6x86OTcXNr3GMRRwE9eC4nsv7jwSIPFsglUoKsGXzRoD%2Ftgw1e7IZj59Bs2nM6jBhdEwlAstOeQmLESGTzXCLD9CGfCIRjwPqzGAhEKQEPc3olcvWzp4CMgP%2FiJYNBXHy%2FgGEzIWYSutsnic1wsHGdBcKgCxtokW%2Bbid1iiplOssGLjo9Y9kWvggStJ8%2Fcpj%2FSxfsDQR5d1ZHsfwZQAUIRrnA3DwcjHOnDJfXLsp%2B0ew3%2FSzW2LJ7Y0q2CqwGXAvoOWYukp4JLFovivy%2FDOYN1kYSn%2Bqt2paIktypH3oRvmgA59it31zo80uxvXcdTt3RRGKF16v4Ouvm3UD1Cczh7ouRBMKVy8L4WwbLvClU6XJRGzqaN%2Bnf9G%2F7gCgcj9GRRScvhGWcwJmjvzyaSE0QhGxj3Lfe977%2BDSxuJOMnLwZa2%2F7l8C3wtjr959W8%2BQJ8qo26CTk%2F4AeN9OI62Rjz0KmeJbphHxJ1zCvuyRBaaVysn0sY7hjEhc4sbcDDDRbMld5scjBl%2BsvEX0FWQN4IpPToTBP%2B6CTLMfy353HLry6%2FBj%2F%2FSTm%2BgJqNFnRZW97%2BNJLhBUz0%2BRx0N7Ii%2F559lbLu2NzBWsSwLD6g0ApxLiXB%2BZjRVRA%2BNl%2BszCBvuzUBjqkATezbjuKwVg7LaUQZIoFtCj6u7rPQZ9SIZmGMjL5SiqPYsz4MNYX7hms%2BczgHhUHnpjNLCp5czmPVjp8zq%2FqUmJAQUR5Nb7dqpic4oVkMxDAn6rom6bHruT1v5fKEGRKJzNp%2B%2BBGoSNUgmTf%2FsCaDsJFDcHscIn2l%2F2QBKmCMDZ5OYCNLIuqa6BywxDM32%2BmQD91cGAzQp6udD735BTikBSEJCCE&X-Amz-Signature=90c7081cd2e37f2975b0da3d91a2896d78711a4826ff8e1483ba0fa625629237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO5F5TWS%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T200943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQDoem43uxTexcRszkXcowEQoLlHmB8bAkxlc37s%2FIJBqQIhAOrryGQwv80AsMRH%2BEYcDyRwC%2FElhVKl7hoIKVG78fAeKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzdac78GbvuIHR%2FWTEq3AMm6x86OTcXNr3GMRRwE9eC4nsv7jwSIPFsglUoKsGXzRoD%2Ftgw1e7IZj59Bs2nM6jBhdEwlAstOeQmLESGTzXCLD9CGfCIRjwPqzGAhEKQEPc3olcvWzp4CMgP%2FiJYNBXHy%2FgGEzIWYSutsnic1wsHGdBcKgCxtokW%2Bbid1iiplOssGLjo9Y9kWvggStJ8%2Fcpj%2FSxfsDQR5d1ZHsfwZQAUIRrnA3DwcjHOnDJfXLsp%2B0ew3%2FSzW2LJ7Y0q2CqwGXAvoOWYukp4JLFovivy%2FDOYN1kYSn%2Bqt2paIktypH3oRvmgA59it31zo80uxvXcdTt3RRGKF16v4Ouvm3UD1Cczh7ouRBMKVy8L4WwbLvClU6XJRGzqaN%2Bnf9G%2F7gCgcj9GRRScvhGWcwJmjvzyaSE0QhGxj3Lfe977%2BDSxuJOMnLwZa2%2F7l8C3wtjr959W8%2BQJ8qo26CTk%2F4AeN9OI62Rjz0KmeJbphHxJ1zCvuyRBaaVysn0sY7hjEhc4sbcDDDRbMld5scjBl%2BsvEX0FWQN4IpPToTBP%2B6CTLMfy353HLry6%2FBj%2F%2FSTm%2BgJqNFnRZW97%2BNJLhBUz0%2BRx0N7Ii%2F559lbLu2NzBWsSwLD6g0ApxLiXB%2BZjRVRA%2BNl%2BszCBvuzUBjqkATezbjuKwVg7LaUQZIoFtCj6u7rPQZ9SIZmGMjL5SiqPYsz4MNYX7hms%2BczgHhUHnpjNLCp5czmPVjp8zq%2FqUmJAQUR5Nb7dqpic4oVkMxDAn6rom6bHruT1v5fKEGRKJzNp%2B%2BBGoSNUgmTf%2FsCaDsJFDcHscIn2l%2F2QBKmCMDZ5OYCNLIuqa6BywxDM32%2BmQD91cGAzQp6udD735BTikBSEJCCE&X-Amz-Signature=e6bd57be4ded06b9a910a5ec5845d9b11964d7cdceb711e97994d26ae5ae4cae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







