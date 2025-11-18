



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PZ5BH5T%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T011231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4ogi8V%2BeHzbS4s%2FssHUU2zPqxaeGINzsbeufg0pZkXAiEA4rabzLLfCnqHhJA%2BVTUdlNXbH06ii99QaNHbY5WN4xAqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKEs%2BCAlr0qNUhabCrcAwdZ3%2F0hek51PJE6qYH0SjcPiDksRKcIg4fKsP0JvuNKuG1sRfowJGnCu6D%2BTpd4WPpPn7TWTXuUsx6hmTTPapAfkQiZJI2oSgHzNXl4Oev96eyx9MXLDn7VbhMJO3Q4AeamD%2FdxlWWNhV0tTxojeM4D5o003D%2FMlEJg1dKGOl9n5r%2FlDGXjEIKR%2B45mMtuL9t57zTCROIl9BqU1%2B0K62m0bEgVay2bdviZ8MUR6qJfHJNaiPCB78YowPirDUBtnmidb8qUYPcL1W5mOzxMzsK02se45WMwGQK1NrsgbB%2BX2t2tOsTmuZx5b5Vt3jA%2FLjiVFKWU5u1T9neN9tVMbncZ8HbFAzXTi%2FZFLHtEDnmPAMBATUn0umWI%2FoatckxQkSzCCFV8Zh66U0jh%2Ft7bk0UFIC9GNF1eC9PY50K02C3c3DUJVjXXDHf1X5pi0DWbeqCdnNr%2BB93CUr%2FgfitGGJv%2FkQ18zK7g7OGGuM41PX7jJedoDQYPfONWdk68VGxFil6jh1Xi84iYyilvGiIurKRP33i4MIynQbmR8N7XZwPIZhmWDrIPjbv1jDZn%2FolP0SssYVL52MgOpYjJHIdlqrBJ%2FgvNciO8lwmc9B8B3jvNDqlwzWE4wFriIBDCsMJzy7sgGOqUBtW9RyN2lN%2FVURjfqCYsW9vmykfogpjC06CF5iFG1XjL7Oake%2BBWOIWiLGXue1iKvRpVRNaD0D8EfgRJBz6cXtJ%2Bh3FXbL8DGsu5ggvSoGpCsOuQs2Nczuk2gKWLCv3O1twKxg5UrtFdprRhaR2up6%2F%2BLKgbtLLy1OPWJpU8NKYJq1LuaRQH4VwIQTzo6bZdQ7S0klPjG%2BYYtohaIuOg4mXMtoeA9&X-Amz-Signature=182b42e5b77312cb0562a853cb8a382b7edf263c63469a8cbd7e90f8ff8089d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PZ5BH5T%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T011232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4ogi8V%2BeHzbS4s%2FssHUU2zPqxaeGINzsbeufg0pZkXAiEA4rabzLLfCnqHhJA%2BVTUdlNXbH06ii99QaNHbY5WN4xAqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKEs%2BCAlr0qNUhabCrcAwdZ3%2F0hek51PJE6qYH0SjcPiDksRKcIg4fKsP0JvuNKuG1sRfowJGnCu6D%2BTpd4WPpPn7TWTXuUsx6hmTTPapAfkQiZJI2oSgHzNXl4Oev96eyx9MXLDn7VbhMJO3Q4AeamD%2FdxlWWNhV0tTxojeM4D5o003D%2FMlEJg1dKGOl9n5r%2FlDGXjEIKR%2B45mMtuL9t57zTCROIl9BqU1%2B0K62m0bEgVay2bdviZ8MUR6qJfHJNaiPCB78YowPirDUBtnmidb8qUYPcL1W5mOzxMzsK02se45WMwGQK1NrsgbB%2BX2t2tOsTmuZx5b5Vt3jA%2FLjiVFKWU5u1T9neN9tVMbncZ8HbFAzXTi%2FZFLHtEDnmPAMBATUn0umWI%2FoatckxQkSzCCFV8Zh66U0jh%2Ft7bk0UFIC9GNF1eC9PY50K02C3c3DUJVjXXDHf1X5pi0DWbeqCdnNr%2BB93CUr%2FgfitGGJv%2FkQ18zK7g7OGGuM41PX7jJedoDQYPfONWdk68VGxFil6jh1Xi84iYyilvGiIurKRP33i4MIynQbmR8N7XZwPIZhmWDrIPjbv1jDZn%2FolP0SssYVL52MgOpYjJHIdlqrBJ%2FgvNciO8lwmc9B8B3jvNDqlwzWE4wFriIBDCsMJzy7sgGOqUBtW9RyN2lN%2FVURjfqCYsW9vmykfogpjC06CF5iFG1XjL7Oake%2BBWOIWiLGXue1iKvRpVRNaD0D8EfgRJBz6cXtJ%2Bh3FXbL8DGsu5ggvSoGpCsOuQs2Nczuk2gKWLCv3O1twKxg5UrtFdprRhaR2up6%2F%2BLKgbtLLy1OPWJpU8NKYJq1LuaRQH4VwIQTzo6bZdQ7S0klPjG%2BYYtohaIuOg4mXMtoeA9&X-Amz-Signature=6db207aad31b090577ecf237c815a838046eea940b0fb6160da36868edd58e16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







