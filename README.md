



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AG6CTNL%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T011331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHH2NYjOR5MlyQVznIXZsOHwxrKVcCrtQ9I9NKafV97nAiAwtPgx7CzEv3tV6eoldS5tgacIrO5yHYoUpBXgIA48MiqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDWfSrUx4NZxbHz%2FjKtwDPjDI2hTRX83lxbUEYxFghA3la5gvHdK9jAULXCdWW6v%2BzaXFrmTIfhlbRIWj1xbTXlBIWHZfYOsOlffLFzxzMtTfLJOmjlM7BtNneqQrMcwIh7SSgHnBR%2BLLeZ7xUnvft8amsuc3Gqpy%2BnKnzJBKWgN%2FXsDIV72O6NOHQfX3lb8kbFHODVoyJHzLuRDLer1GA0cBXG4adePXNey2g83MDpORUqRV8hD4wBaEVNkja17dHlWl7k%2FS7EGtkniv41w%2FORUc5z4oUYUy3u2ljBfdyQ%2FWfIPWVoPV5JGLZa%2BZE40qRWZXphFmYzuOUHdRNmOLUVl%2Bt7b0n9LsxQM1pl%2Bwrnc9Mh9ayFDXzSpcAqE%2BgpkW3VJhB6RO0er1VlIc%2BrMU83hy8%2FS1Z0%2Fj8tLktc8yftxqcCY8qbOE4SSj7xc2TmQwojlW2mNF0tfn51cRJw0ZUdpT1gZT2eB8%2BA1iFcc4IW7UfThOROZ6oLWsq%2FnxInypDCHsvjsepQDJMkzIbWXUjN0n5J%2FcMQ%2Fbt9CSzfz6N8rkNriK7GKtrQFcPbmFjVZJYP25FxCZ6VT%2FNGfwv4TJhyi3msTlMSTurko2T%2BIXb1cm56%2FY%2BydhT4g3STE%2BKM58dwNkxdzv9ubutNcw%2F%2BDpyAY6pgG0qr0KlZB2aCBl2qwFqls5XrudGqPII36tj8lO0wBt0SMdy379Jf%2BhInEgrhlIxqPZUeWjRb6VQC1iloEFO0V%2F5hKnnEBdNHoWfJrkVYZlFwzhxko82auM5kGU2%2F4mr6cXwM1JrRmvE26vvsfskd668L%2Fk6DB%2BpTZOBAISknTksNfLjb1an0hzSjk0pYrH%2BXnr%2FMUFd25uYeprO1HaMp6C6gzI7qHQ&X-Amz-Signature=198b8c475121cb1cb29032d750313cef8ee35f7433d73e52726a4fceb252d7f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AG6CTNL%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T011331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHH2NYjOR5MlyQVznIXZsOHwxrKVcCrtQ9I9NKafV97nAiAwtPgx7CzEv3tV6eoldS5tgacIrO5yHYoUpBXgIA48MiqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDWfSrUx4NZxbHz%2FjKtwDPjDI2hTRX83lxbUEYxFghA3la5gvHdK9jAULXCdWW6v%2BzaXFrmTIfhlbRIWj1xbTXlBIWHZfYOsOlffLFzxzMtTfLJOmjlM7BtNneqQrMcwIh7SSgHnBR%2BLLeZ7xUnvft8amsuc3Gqpy%2BnKnzJBKWgN%2FXsDIV72O6NOHQfX3lb8kbFHODVoyJHzLuRDLer1GA0cBXG4adePXNey2g83MDpORUqRV8hD4wBaEVNkja17dHlWl7k%2FS7EGtkniv41w%2FORUc5z4oUYUy3u2ljBfdyQ%2FWfIPWVoPV5JGLZa%2BZE40qRWZXphFmYzuOUHdRNmOLUVl%2Bt7b0n9LsxQM1pl%2Bwrnc9Mh9ayFDXzSpcAqE%2BgpkW3VJhB6RO0er1VlIc%2BrMU83hy8%2FS1Z0%2Fj8tLktc8yftxqcCY8qbOE4SSj7xc2TmQwojlW2mNF0tfn51cRJw0ZUdpT1gZT2eB8%2BA1iFcc4IW7UfThOROZ6oLWsq%2FnxInypDCHsvjsepQDJMkzIbWXUjN0n5J%2FcMQ%2Fbt9CSzfz6N8rkNriK7GKtrQFcPbmFjVZJYP25FxCZ6VT%2FNGfwv4TJhyi3msTlMSTurko2T%2BIXb1cm56%2FY%2BydhT4g3STE%2BKM58dwNkxdzv9ubutNcw%2F%2BDpyAY6pgG0qr0KlZB2aCBl2qwFqls5XrudGqPII36tj8lO0wBt0SMdy379Jf%2BhInEgrhlIxqPZUeWjRb6VQC1iloEFO0V%2F5hKnnEBdNHoWfJrkVYZlFwzhxko82auM5kGU2%2F4mr6cXwM1JrRmvE26vvsfskd668L%2Fk6DB%2BpTZOBAISknTksNfLjb1an0hzSjk0pYrH%2BXnr%2FMUFd25uYeprO1HaMp6C6gzI7qHQ&X-Amz-Signature=b9f987df6e1aa816a887a885a00ce93a5653037d9cf41da20cc8ce2884301ea9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







