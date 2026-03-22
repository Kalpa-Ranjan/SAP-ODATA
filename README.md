



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFW6QPDC%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T123956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAex0tqLD7vUsG84oSFdMNQcKf89n%2FZxjNWeoutIcofnAiBc%2Fvb%2BWLZSEFxCsqmYBeST%2FnZIG7GgkbCtbAch1TDXsir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMVWucEOX2bxiT5bf7KtwDsUytJtrDCD5IxlXsxOMPGr6DdQIpDVpqYettv%2FQsUbGgeSsh6icMCLIDEXLGlBJe5cxfoifrxBb1xPn%2Bpfs5VVf7ANIym%2FMXOhkp7zwd0e3vBJcyWy7QDDOGP1%2BrxPTsppqhPMicxLNupYB9yfPdzuwB2LJvEj3jXHstI5kt9iD0Iit0pG1khXTqO3%2BI5%2F4WUUMbVkgZdEQu9c6yMc9Yc52PiE5%2FIFwiHyyA2CVhrE9NgzNO9CiM9lzD63jeW2x6m1ZDzmPbAEhCa7amvfATKcwk3M8P%2FS4flXS5xsCVNHPaskXk0yFTWksiB50PPt%2BbfD4WKCCQd%2FyQrIbfTEMdRl%2FIz1vHesM3HkKU9oKLKhrevYk3K952gfpPS3ms%2FNgpHfS5DMVwSo46Kuo8y5QNY1Eb1om2jGqbvEV2H3tX%2FbtQqa3fj7l2boTcMcGuVXtKk1WrAqTlkbfa45SK8j2hA0qBzMsPo1a4e35KreyFs6W0%2Fh1sioFt3UDhRt8kUrhZsiiZePFTrsUFkazwWwxA890%2FtqR8oextt5uQj2paCPFIpawiNxMAep%2BGG%2By%2BH1yZlosIMGx5RyIyJWq1cunHwm9F2gYZqlvlxPqzBz0HFyCtASFQxs01TB%2BxymUwtKL%2BzQY6pgFusDHlyybdP75A%2BBa0xpo16nqz5rMDQW9n6PnUdnjdCehHpJRq%2Bfa0XmKl6qTDzfdB6CZVBeME7SlHWvWxNX4HWZR2IPQ0GWXNnw4isgBhrXh3oyU8Gqqnr52itHCiYKW0FVl6aQOT4CLV9cz%2FbhwnYkuyAHEtlQRf0bRWJd0LETdBxTsdUw78bM0HKNbCaO3QxQXoZ%2FaPyRcWFBPM%2Be2GZky5LeB7&X-Amz-Signature=c15b06da451be707a3070075b03b454301a833b41aa693f5bf2badb24e819ed9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFW6QPDC%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T123956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAex0tqLD7vUsG84oSFdMNQcKf89n%2FZxjNWeoutIcofnAiBc%2Fvb%2BWLZSEFxCsqmYBeST%2FnZIG7GgkbCtbAch1TDXsir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMVWucEOX2bxiT5bf7KtwDsUytJtrDCD5IxlXsxOMPGr6DdQIpDVpqYettv%2FQsUbGgeSsh6icMCLIDEXLGlBJe5cxfoifrxBb1xPn%2Bpfs5VVf7ANIym%2FMXOhkp7zwd0e3vBJcyWy7QDDOGP1%2BrxPTsppqhPMicxLNupYB9yfPdzuwB2LJvEj3jXHstI5kt9iD0Iit0pG1khXTqO3%2BI5%2F4WUUMbVkgZdEQu9c6yMc9Yc52PiE5%2FIFwiHyyA2CVhrE9NgzNO9CiM9lzD63jeW2x6m1ZDzmPbAEhCa7amvfATKcwk3M8P%2FS4flXS5xsCVNHPaskXk0yFTWksiB50PPt%2BbfD4WKCCQd%2FyQrIbfTEMdRl%2FIz1vHesM3HkKU9oKLKhrevYk3K952gfpPS3ms%2FNgpHfS5DMVwSo46Kuo8y5QNY1Eb1om2jGqbvEV2H3tX%2FbtQqa3fj7l2boTcMcGuVXtKk1WrAqTlkbfa45SK8j2hA0qBzMsPo1a4e35KreyFs6W0%2Fh1sioFt3UDhRt8kUrhZsiiZePFTrsUFkazwWwxA890%2FtqR8oextt5uQj2paCPFIpawiNxMAep%2BGG%2By%2BH1yZlosIMGx5RyIyJWq1cunHwm9F2gYZqlvlxPqzBz0HFyCtASFQxs01TB%2BxymUwtKL%2BzQY6pgFusDHlyybdP75A%2BBa0xpo16nqz5rMDQW9n6PnUdnjdCehHpJRq%2Bfa0XmKl6qTDzfdB6CZVBeME7SlHWvWxNX4HWZR2IPQ0GWXNnw4isgBhrXh3oyU8Gqqnr52itHCiYKW0FVl6aQOT4CLV9cz%2FbhwnYkuyAHEtlQRf0bRWJd0LETdBxTsdUw78bM0HKNbCaO3QxQXoZ%2FaPyRcWFBPM%2Be2GZky5LeB7&X-Amz-Signature=d9ddd7eee3d992bd94ecabf6b479ff8692d7e33eb0fdde335770e8c778ae6b21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







