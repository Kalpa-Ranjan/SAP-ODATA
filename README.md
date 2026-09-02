



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H7LQ75V%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T102632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQKJKjBQJ94ozUvDINEhCw0Rq%2Fgczwljro4SkRcwjjRwIgXuszaRmB4HDi71Ti12TXbF5Tj4SvqQbj9fwHWl7PI6YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpWKUv67xNQZs0D0SrcA3JEARUjmuiQBxHf0j2UjWCr%2Be%2B30s3U4yfKwYnlr%2Fx29k%2F64mRCo%2FJ8Hptk3uOgeZNxwLQuKJTsHFPGwen2503UpQCTaCWKZ1g9ChmAvwtqWTWPlGVSHOZvATHIsGcGXN2VRqoLOpyqyUCfQ61%2Fp%2B74xKd0jEXjlnZ52DfDa2Ia6Mh1tSpmR%2FvOb6FdCT23N4n1TlSuQIgYbk6e1XhYuCQ2JmObAvMZzlJEwESvQ5%2FdvD21nSomTctMFFu5koZvoe0JhIPIGwez%2F8J6d8m2sqP0tydg1Ka4KWZPV%2FGj62tiH8Oq9QhNu3kkT%2BcTjB62BJm0pVJcQKsquiliRiCgwFSS1Hiyssaw4ltEsuGgesMsxdzZh84j6KodzGyfQEMEzkNPF5%2BbGv0v7B2dFZwHcDQzwMbr92ObUgguV9njHSq9fdx6oAhe5l%2FfytBPxbbgvhea3X2cHUcb8PBwtcOvW4a%2BkWTL6WvraKZIJKSC9RZjSpiU4R%2BudQiiO1TTuaX8%2B69SE%2BKLruXSYIJEbHQGpnl%2BThcq7zdn%2FIEKtf5qHmWSMbnwoPPvkG93X8Ib0U3Cy4ySZLLImu25hschif7WJqz12WW9dBbOtkxqvA5S3L9B%2B1QBVTasbpCxU%2BYmMK%2Bs39QGOqUBT%2FRwd8XBf%2FC0VCYVd%2FMK4SkU9d4fDlWvDOauSty9xbEKvbbNnme%2FAe1NCU3md9R7%2FbUl1ZEeyslZ2R1kd74%2B3aLOfzpal3mJBzoNxwgJh0ezR7pAwl7oSuE7EvU1NFIfNUTXhjvgEy%2F1V9Kasky3oyXkZ7uZXGm8t6LxoEm037BavO9mmULUiUbm%2Fh87IKgHYvA6KpE1rIEc5tH42GloKZE%2Flis2&X-Amz-Signature=97d6bf129407929b64fbb89caefaee914d4f386c2a35f8fa8d0559d9a9d07782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H7LQ75V%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T102632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQKJKjBQJ94ozUvDINEhCw0Rq%2Fgczwljro4SkRcwjjRwIgXuszaRmB4HDi71Ti12TXbF5Tj4SvqQbj9fwHWl7PI6YqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpWKUv67xNQZs0D0SrcA3JEARUjmuiQBxHf0j2UjWCr%2Be%2B30s3U4yfKwYnlr%2Fx29k%2F64mRCo%2FJ8Hptk3uOgeZNxwLQuKJTsHFPGwen2503UpQCTaCWKZ1g9ChmAvwtqWTWPlGVSHOZvATHIsGcGXN2VRqoLOpyqyUCfQ61%2Fp%2B74xKd0jEXjlnZ52DfDa2Ia6Mh1tSpmR%2FvOb6FdCT23N4n1TlSuQIgYbk6e1XhYuCQ2JmObAvMZzlJEwESvQ5%2FdvD21nSomTctMFFu5koZvoe0JhIPIGwez%2F8J6d8m2sqP0tydg1Ka4KWZPV%2FGj62tiH8Oq9QhNu3kkT%2BcTjB62BJm0pVJcQKsquiliRiCgwFSS1Hiyssaw4ltEsuGgesMsxdzZh84j6KodzGyfQEMEzkNPF5%2BbGv0v7B2dFZwHcDQzwMbr92ObUgguV9njHSq9fdx6oAhe5l%2FfytBPxbbgvhea3X2cHUcb8PBwtcOvW4a%2BkWTL6WvraKZIJKSC9RZjSpiU4R%2BudQiiO1TTuaX8%2B69SE%2BKLruXSYIJEbHQGpnl%2BThcq7zdn%2FIEKtf5qHmWSMbnwoPPvkG93X8Ib0U3Cy4ySZLLImu25hschif7WJqz12WW9dBbOtkxqvA5S3L9B%2B1QBVTasbpCxU%2BYmMK%2Bs39QGOqUBT%2FRwd8XBf%2FC0VCYVd%2FMK4SkU9d4fDlWvDOauSty9xbEKvbbNnme%2FAe1NCU3md9R7%2FbUl1ZEeyslZ2R1kd74%2B3aLOfzpal3mJBzoNxwgJh0ezR7pAwl7oSuE7EvU1NFIfNUTXhjvgEy%2F1V9Kasky3oyXkZ7uZXGm8t6LxoEm037BavO9mmULUiUbm%2Fh87IKgHYvA6KpE1rIEc5tH42GloKZE%2Flis2&X-Amz-Signature=d4f9485283fcf5128a63d8fb53ec5faeae666894b3130a29f36540487bdfc1b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







