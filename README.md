



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6YNVZWS%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T071601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIB4YppbDR36tIbGqLmRb46%2BmRtg1tY%2Bo%2FVZSUcxC6LxbAiBm5SVZehIQcei9W1aawcxjoiTZnk0wuDvjL1gO6kVieiqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqRIreLIHtE72rj01KtwD1XCbQBI6ZqGOnIr636k8d5z%2FrmCpNxdvVIhGSadvd0Gj24FbQGHk0dxltPECjrXU9R5FnUcmbeIrR7%2F9Hl%2Bp2FQVuyUUDdcMA4GCQsh%2BB7nZfDLru8yroBYHdnTJAtCILT0q769ejVGGdeQbsnP6a2OA1LRcAZZAOiNv09t6ef5GpknUYGYXpQnMUHmYMHloX0S8HToaYupdIaKPm4ySzm1C%2FBFtCfCZ4NuVTqp1P%2Fqg51%2FJEc1TM3%2FG74VMl7lwQ4RWN8UbqLu0y%2ByMCbXsnVQcz3v1m15DRvzQdWRI4aVNXoLp5GkDjnw7wqr%2BiQEeVedniYstc60Fq%2FCyLk0sE79qFsvddfhSP8dowmdkhWyrHYR0od8lU7UHIY%2Bb7hKcHII%2FsUaPPjOVPmfGiGhXRaSGcfUHliQRG%2FBceT7AA1iZ%2BjdfjdpANWqcNAVhBSWMsL2ob9rxPRxhlDkGV2FYTsRWihmR6EsA2qOTzdYY8R6w97lCJVlIp8WRrPst%2BGwXynxvzUYQxNsssfv4kffYd7O6RWd5aCCb58t6oq6ajf1dykakuGao1%2BqUkVGDBWx5qeV1ng5LjZiCjEGn9aIdnU5lWm4bMNP0CP7dmrI3c7QRGUMTBgMxH%2Ff8fJ0wh9360wY6pgH7DF8RZbLiqwS6oBhGoSk59%2BwYoGklLJ%2FvTez96zTBl0y%2FW07gocRvYJtQYZwUdzowF0B1DoKMPBOULSeTLHwGnLo1%2BRUst6%2FCcoZG15sHfRjaMqdelHNsCYiw1PKrkZP8kDsVFB63kFyMzBTHWlPf5mKgppbRpj9PnmU%2BoC%2FOCNPtwoqv9a3gity5%2BQ6X%2B5OBo%2FSxBf7weucYki9SaPFinQrFp7Gc&X-Amz-Signature=e04aa0ace41be552df6474b693f891192c790cabfc65a58b038cd7056e2ec836&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6YNVZWS%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T071601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIB4YppbDR36tIbGqLmRb46%2BmRtg1tY%2Bo%2FVZSUcxC6LxbAiBm5SVZehIQcei9W1aawcxjoiTZnk0wuDvjL1gO6kVieiqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqRIreLIHtE72rj01KtwD1XCbQBI6ZqGOnIr636k8d5z%2FrmCpNxdvVIhGSadvd0Gj24FbQGHk0dxltPECjrXU9R5FnUcmbeIrR7%2F9Hl%2Bp2FQVuyUUDdcMA4GCQsh%2BB7nZfDLru8yroBYHdnTJAtCILT0q769ejVGGdeQbsnP6a2OA1LRcAZZAOiNv09t6ef5GpknUYGYXpQnMUHmYMHloX0S8HToaYupdIaKPm4ySzm1C%2FBFtCfCZ4NuVTqp1P%2Fqg51%2FJEc1TM3%2FG74VMl7lwQ4RWN8UbqLu0y%2ByMCbXsnVQcz3v1m15DRvzQdWRI4aVNXoLp5GkDjnw7wqr%2BiQEeVedniYstc60Fq%2FCyLk0sE79qFsvddfhSP8dowmdkhWyrHYR0od8lU7UHIY%2Bb7hKcHII%2FsUaPPjOVPmfGiGhXRaSGcfUHliQRG%2FBceT7AA1iZ%2BjdfjdpANWqcNAVhBSWMsL2ob9rxPRxhlDkGV2FYTsRWihmR6EsA2qOTzdYY8R6w97lCJVlIp8WRrPst%2BGwXynxvzUYQxNsssfv4kffYd7O6RWd5aCCb58t6oq6ajf1dykakuGao1%2BqUkVGDBWx5qeV1ng5LjZiCjEGn9aIdnU5lWm4bMNP0CP7dmrI3c7QRGUMTBgMxH%2Ff8fJ0wh9360wY6pgH7DF8RZbLiqwS6oBhGoSk59%2BwYoGklLJ%2FvTez96zTBl0y%2FW07gocRvYJtQYZwUdzowF0B1DoKMPBOULSeTLHwGnLo1%2BRUst6%2FCcoZG15sHfRjaMqdelHNsCYiw1PKrkZP8kDsVFB63kFyMzBTHWlPf5mKgppbRpj9PnmU%2BoC%2FOCNPtwoqv9a3gity5%2BQ6X%2B5OBo%2FSxBf7weucYki9SaPFinQrFp7Gc&X-Amz-Signature=a8f2a0972b25b1161f9c942d91fa58b35951c07f1a2cffe2714c117f9eb63ec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







