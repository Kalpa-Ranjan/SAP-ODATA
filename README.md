



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4BVRHIG%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T125637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5%2FhfsBaNrxV2NSLBATELc2cmeK86RAT4WI3nJqDZzUgIgA88GPiy%2BNFXTBt6nofwTlyQ9Ir8SbHpKQGy60pLcAwwq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDI8%2BBlZyRnuUFjJ5HircAwsqg4onPSKZRIdOLlAdJmK7Rpa4XEmo4nVejJr90bWphUlU%2FNdzbhAzlXs7fP9ORN4F%2FHviRV6RtVsmWgrjvI1rXjJD0JDET3yHcB2ZdZ0DiaMh%2BFw6ZBGrFnKqX1oc2A%2BpJVDR6IxoxAnflLSwxWppX8kHN22qQ%2BmuqJAV5b3u6iKRlia0NIn0Q3mbtmXODOYwr1%2F77rKXX7rtLeQsxvtYq5G2m6pCyObD8W1k7B5irRl1Cpb8uX0Q67a8Fk5wtUR88rveaDJz2%2Besx0G4Btjef42e9CCUK0ZqneQ7K5%2BWjFRnm71WJSVoCtci7%2FRGAf62kUpDwWJ9TpoDn47ePaKsA93piTz%2BJIrZyh4OaLJlW5TTFTWqn1xMmIYCRSlTDlucN6TifQ1zd6Z0KZaMGGUWjyDZ8bNvZc3TPE173vL7XUsFt7WyR4LjgWU88GtskPDdzmyqoJTi3t0oPahqa%2FY1I%2B9hkAyhGkwM8VIpwVaejj7LCKdYkReGoQ1kaFt7Q8dWXoG9TTq%2BCQrkuMHwCElr5I8cw7IKPZnvjE9B3M4O2HyiUWijMcdf4JBtl32%2BTY78eJEkeF%2FbhmpaHDdEVPzZztez8FmcH%2FVj8IzoLLxEUkQCKhOgaPqu6GuZMN7qhM4GOqUB3TpjYTg1j%2FqJcv2XDZ9YfpYDC78soEhcfkil1BijoPWzX6N0mP1WNKPaRjtohE9TeYqjcjgC4B6AXTiWr2ZpOyehl7dZ1J8IlwTkdGdsfzWYfOFDDcbuf0o%2B%2FnkPKgFuvjLA%2FAOe1yhAVaNi4w9LXr5axAQZl%2BXzGGT7pYWlQrVUiJMqYAM1135TZGD4DFqX8LechyxVMZmksGMew0%2FWwAEkyrVn&X-Amz-Signature=67f9c16b504299bb1101f94113bc734819b960299c41b0e07e967f769a29cbff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4BVRHIG%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T125637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5%2FhfsBaNrxV2NSLBATELc2cmeK86RAT4WI3nJqDZzUgIgA88GPiy%2BNFXTBt6nofwTlyQ9Ir8SbHpKQGy60pLcAwwq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDI8%2BBlZyRnuUFjJ5HircAwsqg4onPSKZRIdOLlAdJmK7Rpa4XEmo4nVejJr90bWphUlU%2FNdzbhAzlXs7fP9ORN4F%2FHviRV6RtVsmWgrjvI1rXjJD0JDET3yHcB2ZdZ0DiaMh%2BFw6ZBGrFnKqX1oc2A%2BpJVDR6IxoxAnflLSwxWppX8kHN22qQ%2BmuqJAV5b3u6iKRlia0NIn0Q3mbtmXODOYwr1%2F77rKXX7rtLeQsxvtYq5G2m6pCyObD8W1k7B5irRl1Cpb8uX0Q67a8Fk5wtUR88rveaDJz2%2Besx0G4Btjef42e9CCUK0ZqneQ7K5%2BWjFRnm71WJSVoCtci7%2FRGAf62kUpDwWJ9TpoDn47ePaKsA93piTz%2BJIrZyh4OaLJlW5TTFTWqn1xMmIYCRSlTDlucN6TifQ1zd6Z0KZaMGGUWjyDZ8bNvZc3TPE173vL7XUsFt7WyR4LjgWU88GtskPDdzmyqoJTi3t0oPahqa%2FY1I%2B9hkAyhGkwM8VIpwVaejj7LCKdYkReGoQ1kaFt7Q8dWXoG9TTq%2BCQrkuMHwCElr5I8cw7IKPZnvjE9B3M4O2HyiUWijMcdf4JBtl32%2BTY78eJEkeF%2FbhmpaHDdEVPzZztez8FmcH%2FVj8IzoLLxEUkQCKhOgaPqu6GuZMN7qhM4GOqUB3TpjYTg1j%2FqJcv2XDZ9YfpYDC78soEhcfkil1BijoPWzX6N0mP1WNKPaRjtohE9TeYqjcjgC4B6AXTiWr2ZpOyehl7dZ1J8IlwTkdGdsfzWYfOFDDcbuf0o%2B%2FnkPKgFuvjLA%2FAOe1yhAVaNi4w9LXr5axAQZl%2BXzGGT7pYWlQrVUiJMqYAM1135TZGD4DFqX8LechyxVMZmksGMew0%2FWwAEkyrVn&X-Amz-Signature=b3051f2222223fb136ae0c766d661a07adeb7c183ba4074e070fda9e7a476066&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







