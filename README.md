



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFAPM2WF%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T092514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmszoUOmRta88jz4Jbsp7NcWrMWFSfS59uJanfBC1xHAiAkCBdj7jvEdNjbOQ91mZdreXMJEUjhlwp2keij3b41JyqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQsrxMpsCCm9XsiyJKtwDAXI0aq12fQ2KQ4irbCfEWR69BZSCpEPD0Qq%2FNKb%2BGPGcgEEkGR%2BwGPyK7i0Pq5sk8hPOmyxzfUr5KdkcMuQPCrpn%2B%2B4bXFVGVXeYPZ1wxz%2FK6kpFhnXrOklqLlDqeqaNLzp3dlzlwo3bgUr7yGj6H1xZtDteecXfi4Hhn9ToPXTUSs6LFn7oY65GtqBL%2F8bF99OMZfYfX6M4BoGMueQM%2BXwRk7Z1w3V1OfiVqY27J1ufv%2BZEvNJm4nUtRDlea8JWjnGrsOJvPzX%2Btm7%2BdLDRxWy9JWIZQrM5sAplTaWqhQUXX%2BRaipXTMlKFcD3lDPsnuRYUOWl6Pv1knnQv9C%2BPQjSVvbRMOanwmfRh6flkdIXAaaLrSICdEd2KPN4ZsGdYkGuN8YviPY4FdMJgwrWCyW9hDR7ZHSmYTZXxZrngU1aOHX8n%2B6W1kwa6dRePyEdqbQ%2BGCJbGwWKgryE1Z8xexQiNEaULRnKbDIz%2BJksbia4N2T7%2Br%2B%2FsHsYnEKQ9Bima0wT7fBjCoQsIoORHEIsu3pp4E5JCI%2FvVvYpmYN%2BaJ6jAiU6BsQsPMZb6IuAo2r79pGQNkCoycg3JjygomWDpK%2BnuWPBgTJSSHmPx3K2KmrGI4H7MkurLzYod7OUwgsnC0gY6pgH76pUh4lyGPsha34jUMEagsRP9jeK7fiewdwR7pZTpX6h9%2Ba1PrQIWHGvaY%2B2zZch9DnL%2BThNh5PuzESTRmvt7y3q3pSovS4z1ZUaSslFCEDpvl70vQ2PA7xFy8qgAhBiYdVjzbDjIiJWAoZB160YCnQLdWxaKDaWgLuWtjYbIYlJTjgP6HUgExzOxuLY7DjcOXcJGM%2FrmdCpkl7dM7NkpYbTwwOBB&X-Amz-Signature=1c783ed60cd050f6fc89855dc6ae3c84cdf2c30a6df657115c5a920824396aa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFAPM2WF%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T092514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmszoUOmRta88jz4Jbsp7NcWrMWFSfS59uJanfBC1xHAiAkCBdj7jvEdNjbOQ91mZdreXMJEUjhlwp2keij3b41JyqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQsrxMpsCCm9XsiyJKtwDAXI0aq12fQ2KQ4irbCfEWR69BZSCpEPD0Qq%2FNKb%2BGPGcgEEkGR%2BwGPyK7i0Pq5sk8hPOmyxzfUr5KdkcMuQPCrpn%2B%2B4bXFVGVXeYPZ1wxz%2FK6kpFhnXrOklqLlDqeqaNLzp3dlzlwo3bgUr7yGj6H1xZtDteecXfi4Hhn9ToPXTUSs6LFn7oY65GtqBL%2F8bF99OMZfYfX6M4BoGMueQM%2BXwRk7Z1w3V1OfiVqY27J1ufv%2BZEvNJm4nUtRDlea8JWjnGrsOJvPzX%2Btm7%2BdLDRxWy9JWIZQrM5sAplTaWqhQUXX%2BRaipXTMlKFcD3lDPsnuRYUOWl6Pv1knnQv9C%2BPQjSVvbRMOanwmfRh6flkdIXAaaLrSICdEd2KPN4ZsGdYkGuN8YviPY4FdMJgwrWCyW9hDR7ZHSmYTZXxZrngU1aOHX8n%2B6W1kwa6dRePyEdqbQ%2BGCJbGwWKgryE1Z8xexQiNEaULRnKbDIz%2BJksbia4N2T7%2Br%2B%2FsHsYnEKQ9Bima0wT7fBjCoQsIoORHEIsu3pp4E5JCI%2FvVvYpmYN%2BaJ6jAiU6BsQsPMZb6IuAo2r79pGQNkCoycg3JjygomWDpK%2BnuWPBgTJSSHmPx3K2KmrGI4H7MkurLzYod7OUwgsnC0gY6pgH76pUh4lyGPsha34jUMEagsRP9jeK7fiewdwR7pZTpX6h9%2Ba1PrQIWHGvaY%2B2zZch9DnL%2BThNh5PuzESTRmvt7y3q3pSovS4z1ZUaSslFCEDpvl70vQ2PA7xFy8qgAhBiYdVjzbDjIiJWAoZB160YCnQLdWxaKDaWgLuWtjYbIYlJTjgP6HUgExzOxuLY7DjcOXcJGM%2FrmdCpkl7dM7NkpYbTwwOBB&X-Amz-Signature=e3d2b2cd222ae2a50057f34ba2c58cd3968939c5e43c43039ddc9f681dafb219&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







