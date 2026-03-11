



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GZRIHYF%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T125014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtp%2FUCynmoBUcufUSxGXMn4o4typrgKzeYpotgrD%2FLzQIhAOXtnI7T4w5faORM6zaEJOzn4rlSNxU0SQ4SjPdqbpx%2BKv8DCF4QABoMNjM3NDIzMTgzODA1IgyHe2W%2Fkx4IXePO0P8q3ANETAc%2FsbMZXcUpN%2FxMZpWJZkksut8Zyj4ffyRl0be99WCg9gCjOIxeDKoyQ5xJIUqFafzF4NvqmqB9fpyOHZNtTqS%2F3iIEDzEQAAl4i09Ightq42Mo%2BqH8i%2FYrSsWhlo5iA801NV7qIk0e07NBM7MqhdO5z0tslZt4UWFHhthUiD159rpBGPXwNWwhPFVSTsKwXr00EIU1KnoQUPabvGWkguxAB0GXJF4cbuUzeNWc2XmVacPG7TsgRrl8o1%2F8cviP%2BFNgSOJTAsk7D6wIcZBUI9NmfHLCEjm262vTJhmy%2F%2B8nPc8h7GM%2BUP9uGd%2F38OQqc%2B5LGzhyMu66SMDk%2FMuIfmRBpaYzl2NxF4%2BHrQJBQidn95tjPlOC9jZ7GDFoJAR5EXNdEXKk5FtdBW3E7gyhaBcOoibpBHl7t4t2AHpZ2H7TnOewCBTqI290Z6blop71nHRWh8nM7lamnQlHReIj9H7y5hWWHbG9tZ0CuPXdkdpG4RFCrkLBwnaIc7RsfQJjY5Gzhtga2PK4%2BofC9jXt3FWZk53MW%2BOJb5DcNd2FjUZFh%2F4vKpIQbhR3pXh%2FwGxEANDeP1BVlHQz6ethbJn4960ByR48qrlTFwAgxAyMooxsLYNUAYZDPctuSzDVycXNBjqkAWCsnMQ76RMPmwfK7quDkwir3vgEkaodsOSeFoqxlQbLsrq96lXvyLZhQfjgIrvt0SJvVUfZM7lIr8dJqwVkvOfiNx%2F%2Fz%2FRF%2Bosnm7YDBTTPY2IZoNa4A%2B%2FkbnqbwHu0plWiNYYBA6peMD30ycM3qBfl%2FNa0HnWtqjpjRYQB1Nk6LkRoAdE%2FlsxyHnbpL3T%2BGlumzp%2BmZxbXIzqWmae9MblVZTVr&X-Amz-Signature=c81239cd8a859c1d39664ccb50d5cf2421d75580cecc072f2d60b6210e16a366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GZRIHYF%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T125014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtp%2FUCynmoBUcufUSxGXMn4o4typrgKzeYpotgrD%2FLzQIhAOXtnI7T4w5faORM6zaEJOzn4rlSNxU0SQ4SjPdqbpx%2BKv8DCF4QABoMNjM3NDIzMTgzODA1IgyHe2W%2Fkx4IXePO0P8q3ANETAc%2FsbMZXcUpN%2FxMZpWJZkksut8Zyj4ffyRl0be99WCg9gCjOIxeDKoyQ5xJIUqFafzF4NvqmqB9fpyOHZNtTqS%2F3iIEDzEQAAl4i09Ightq42Mo%2BqH8i%2FYrSsWhlo5iA801NV7qIk0e07NBM7MqhdO5z0tslZt4UWFHhthUiD159rpBGPXwNWwhPFVSTsKwXr00EIU1KnoQUPabvGWkguxAB0GXJF4cbuUzeNWc2XmVacPG7TsgRrl8o1%2F8cviP%2BFNgSOJTAsk7D6wIcZBUI9NmfHLCEjm262vTJhmy%2F%2B8nPc8h7GM%2BUP9uGd%2F38OQqc%2B5LGzhyMu66SMDk%2FMuIfmRBpaYzl2NxF4%2BHrQJBQidn95tjPlOC9jZ7GDFoJAR5EXNdEXKk5FtdBW3E7gyhaBcOoibpBHl7t4t2AHpZ2H7TnOewCBTqI290Z6blop71nHRWh8nM7lamnQlHReIj9H7y5hWWHbG9tZ0CuPXdkdpG4RFCrkLBwnaIc7RsfQJjY5Gzhtga2PK4%2BofC9jXt3FWZk53MW%2BOJb5DcNd2FjUZFh%2F4vKpIQbhR3pXh%2FwGxEANDeP1BVlHQz6ethbJn4960ByR48qrlTFwAgxAyMooxsLYNUAYZDPctuSzDVycXNBjqkAWCsnMQ76RMPmwfK7quDkwir3vgEkaodsOSeFoqxlQbLsrq96lXvyLZhQfjgIrvt0SJvVUfZM7lIr8dJqwVkvOfiNx%2F%2Fz%2FRF%2Bosnm7YDBTTPY2IZoNa4A%2B%2FkbnqbwHu0plWiNYYBA6peMD30ycM3qBfl%2FNa0HnWtqjpjRYQB1Nk6LkRoAdE%2FlsxyHnbpL3T%2BGlumzp%2BmZxbXIzqWmae9MblVZTVr&X-Amz-Signature=2ec19f22bfe94a2ca7cf18a90df8dbd46cd6bd3eb3443784b96d21184cbfb118&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







