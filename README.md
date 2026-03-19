



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDMTAJRY%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T015125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCa2IyUmvIOkB8RgqiNsUaZdvXX9Q6AQwpyPxdENOy66wIgWc0mB7D6HOLrdUKpDRGWK%2BvvMP9Uo9Nn8o5Y4ebPqiUq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDI3kRgGWLN9CzXI53SrcA7zYd56945qbxcQGUgwVwMwleFYCYk8yopHx%2F2qajbNFIkuWLLeDb5LhG%2Bd0KoGfw2J%2BOKGlyptzwVRagx2GwQmf%2FvuIyP8%2B2oveFZSN7bv%2B36pQT3jB2eSlMO8%2FDef0r7QXIqPZRe1bfvuJ9Bjik3lK06HjakEPIZamglDDeYfoYDHCyHK0Ebk3B9tA6AAbZJ1AI2CsjXbT08bz19wQFH7HrX%2BbrZ0z574xSo71uEFh6pJE7X9VvNIfoIsLPvBWQcJZLhn8ZlAXIPfjvA4qfflbnNDaLv0w7xElpmqwGg5c5P6V3LHb5IF3T9V8XeLDLy949Ba9hkVpQXC8hPR7kWrMIj%2BiRGP6krWgaS9r6FNv7M%2BmSYOaOQxn6kQaoJrLltOM9upHiUPaMki8opSJnK%2FxcZaeItYMzvMsoV%2B%2FzqddlF%2FbrnIFL2BBO9E%2FQN34hw5miHFFHnxIKTcnC5jW70XEWyzUZX%2F%2FBeya%2F%2BIYHjzPYTWTgLYJQOp5tovAlm5wGilgBLpwc%2FNdxI5GvDTOVbVEhHOoL6JOR4ClFTOLRAqpTT%2FbHA71Xf%2FJVhRrSErw3izV0PGFydsooBs25ov%2B2pBOoESOGyDjieIgX8erax2phS9oPPGTGD4dYqDWMJOV7c0GOqUBq96ORyTBOwm%2Bfi1BGZS0Fcf24V2nAcSPHFBkrYcbjVCdH4HaMNbF0Tb2Wbd5M0ae38w9T5wbdN4xz8fsRJtOWO4Zhi6Pvk76DsvfjvXu4efqrdraGUzBi0fC65xC12%2BN57BdWjNQZ%2Bcd0drINSnAzpJWbKE9eFV9txSevhI%2BylhtUgiN2juWMzd7aL3CAiE1n5zfwgnnaLTHQw9iot5jmCbMx3s0&X-Amz-Signature=0c10387f53d05d25948fa09f3ab807762bf240a8e36141b6550deda18931228e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDMTAJRY%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T015125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCa2IyUmvIOkB8RgqiNsUaZdvXX9Q6AQwpyPxdENOy66wIgWc0mB7D6HOLrdUKpDRGWK%2BvvMP9Uo9Nn8o5Y4ebPqiUq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDI3kRgGWLN9CzXI53SrcA7zYd56945qbxcQGUgwVwMwleFYCYk8yopHx%2F2qajbNFIkuWLLeDb5LhG%2Bd0KoGfw2J%2BOKGlyptzwVRagx2GwQmf%2FvuIyP8%2B2oveFZSN7bv%2B36pQT3jB2eSlMO8%2FDef0r7QXIqPZRe1bfvuJ9Bjik3lK06HjakEPIZamglDDeYfoYDHCyHK0Ebk3B9tA6AAbZJ1AI2CsjXbT08bz19wQFH7HrX%2BbrZ0z574xSo71uEFh6pJE7X9VvNIfoIsLPvBWQcJZLhn8ZlAXIPfjvA4qfflbnNDaLv0w7xElpmqwGg5c5P6V3LHb5IF3T9V8XeLDLy949Ba9hkVpQXC8hPR7kWrMIj%2BiRGP6krWgaS9r6FNv7M%2BmSYOaOQxn6kQaoJrLltOM9upHiUPaMki8opSJnK%2FxcZaeItYMzvMsoV%2B%2FzqddlF%2FbrnIFL2BBO9E%2FQN34hw5miHFFHnxIKTcnC5jW70XEWyzUZX%2F%2FBeya%2F%2BIYHjzPYTWTgLYJQOp5tovAlm5wGilgBLpwc%2FNdxI5GvDTOVbVEhHOoL6JOR4ClFTOLRAqpTT%2FbHA71Xf%2FJVhRrSErw3izV0PGFydsooBs25ov%2B2pBOoESOGyDjieIgX8erax2phS9oPPGTGD4dYqDWMJOV7c0GOqUBq96ORyTBOwm%2Bfi1BGZS0Fcf24V2nAcSPHFBkrYcbjVCdH4HaMNbF0Tb2Wbd5M0ae38w9T5wbdN4xz8fsRJtOWO4Zhi6Pvk76DsvfjvXu4efqrdraGUzBi0fC65xC12%2BN57BdWjNQZ%2Bcd0drINSnAzpJWbKE9eFV9txSevhI%2BylhtUgiN2juWMzd7aL3CAiE1n5zfwgnnaLTHQw9iot5jmCbMx3s0&X-Amz-Signature=b7437341c687e21e7be0a41ba7c50a4a6b4313d53a141d3276b4b659df1ff49b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







