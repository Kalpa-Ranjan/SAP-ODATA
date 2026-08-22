



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5LVI5PJ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T122729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVkWdLu7qEoiAkSCTWBDmITk6Had1%2BrM2i5mt%2BXA7%2B%2BAiAFLaAmHTMDjBsd1NKa7vuN4979VF3uWV8yU6onThZGaSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpB8qj8pYso4BhM5fKtwDkFxtdADaF8VW7NlFxH4RfWm0Z%2BYPqL3NY6im5iHD7mriulKHjlwXySQQJhR5OfsqHeKcv3dYlwZuGC5mlrWMh4vZtNlVash8TAPm9KvygbeIHtaUZGYEYL2hw%2F53xkaf1r0%2FsHGH6iADDi4ALYbbG0uRw6h4MmVOMPssGllVzyTkqhdmVtjm7X5ef%2FJhzNqgu5Pd1L3ZsnIUQf69gKnglIMK2XfEIaTFD6RxZMLwyEpHcNWPhxsBCi2WNFiQ8bvwX0KrhEz8hnFVOBfgC8H8yhMeWRdAOaGvE99HrSKyXER7cDcn%2B0YAwfBZufPgIZvXK7H534RIJKW%2BT3iChlcDGvTQgqSSipDwdgJkQou%2FzCHfsBDh7xEtuKhhlFVi24C4r4b%2F3FLSTLxtvp1R9DfCilVyyIUv3aW47iF2OqzmIXtgekgN7fBtCPbd7qCWoXkj4ii%2B8fj5dvFVviJDcbxoQPD2YBTo4THUB%2FVWHUFLcXN6IhXLA9K5C2jdhhJ763lggdRKU6FmJVVZsXdpDydrFXoKPtNrxp3%2BiP5IalQsXjf9oS35BeE4Ke%2BaxxyotB80GEUth4%2FVtHL8vxIHvF%2BwAm6nO%2Bs%2B4plta04riK8zJAEAfD0nVQ3uZ8vd30Mwmt%2Bl1AY6pgFQR5Pc1LFPvHnixq%2FFwyQgsnZwrleQePwTtTX%2FH%2ByGoZP1al2rw8GDh2WuirG5dZwQojFHyXnx5gY7Px7%2BuphyXPk0CaH5YXOvfWNbsAgWIeWyy5FOPM%2F510cYfq6bsc8iU3GscMI1QdEPD7WgzGrqmP2ZqfHvR7h%2Bt7wx8EDMRT0ds6oKS%2FoEvBARu92e9S4EIgWzUbBdmUCP9vWn%2FHn74wnmJyqI&X-Amz-Signature=7bb37625b72151c253db279c3b4c819c8e14b991a593bd61d7be932d93f7d0db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5LVI5PJ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T122730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVkWdLu7qEoiAkSCTWBDmITk6Had1%2BrM2i5mt%2BXA7%2B%2BAiAFLaAmHTMDjBsd1NKa7vuN4979VF3uWV8yU6onThZGaSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpB8qj8pYso4BhM5fKtwDkFxtdADaF8VW7NlFxH4RfWm0Z%2BYPqL3NY6im5iHD7mriulKHjlwXySQQJhR5OfsqHeKcv3dYlwZuGC5mlrWMh4vZtNlVash8TAPm9KvygbeIHtaUZGYEYL2hw%2F53xkaf1r0%2FsHGH6iADDi4ALYbbG0uRw6h4MmVOMPssGllVzyTkqhdmVtjm7X5ef%2FJhzNqgu5Pd1L3ZsnIUQf69gKnglIMK2XfEIaTFD6RxZMLwyEpHcNWPhxsBCi2WNFiQ8bvwX0KrhEz8hnFVOBfgC8H8yhMeWRdAOaGvE99HrSKyXER7cDcn%2B0YAwfBZufPgIZvXK7H534RIJKW%2BT3iChlcDGvTQgqSSipDwdgJkQou%2FzCHfsBDh7xEtuKhhlFVi24C4r4b%2F3FLSTLxtvp1R9DfCilVyyIUv3aW47iF2OqzmIXtgekgN7fBtCPbd7qCWoXkj4ii%2B8fj5dvFVviJDcbxoQPD2YBTo4THUB%2FVWHUFLcXN6IhXLA9K5C2jdhhJ763lggdRKU6FmJVVZsXdpDydrFXoKPtNrxp3%2BiP5IalQsXjf9oS35BeE4Ke%2BaxxyotB80GEUth4%2FVtHL8vxIHvF%2BwAm6nO%2Bs%2B4plta04riK8zJAEAfD0nVQ3uZ8vd30Mwmt%2Bl1AY6pgFQR5Pc1LFPvHnixq%2FFwyQgsnZwrleQePwTtTX%2FH%2ByGoZP1al2rw8GDh2WuirG5dZwQojFHyXnx5gY7Px7%2BuphyXPk0CaH5YXOvfWNbsAgWIeWyy5FOPM%2F510cYfq6bsc8iU3GscMI1QdEPD7WgzGrqmP2ZqfHvR7h%2Bt7wx8EDMRT0ds6oKS%2FoEvBARu92e9S4EIgWzUbBdmUCP9vWn%2FHn74wnmJyqI&X-Amz-Signature=50bb727c7cc99559f59eea83eb67dcbafc78a98dc8b426d2aafe7dcd3ecbc9e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







