



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643U76ZNK%2F20261122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261122T180511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGerJFtKLEsAEJcG3WsUJDrGkh%2Fdz3Zm4TRLJCQrxST7AiEAt%2FUWis55P9BeSyef8iZ%2BXsK7PWVROZ9HNEtsI9Bkcx4q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDFsETLfj6E575eSQVircAzet4dE2Ui6tXbMbC47WKukrfSrvHSR5vHdP5lO2zil7rbYfku3jPG3xYo%2F83szcceelT70VDq%2FMF8wcM7L6pHTjSnuq%2Bmcb2tCwKYiOpUpXg8iWq3kuduZzFvmCe1Jdf3Cg%2B%2BKo3hQvm98d4gUb%2BCs0FhdO5kQme5GMkrSZZAwPzekS4JgxDceRpTiuxw9UhKYLpr%2BZ2OAoTTHgS1sazzpQ09We%2FUFiD8DC1TQW0XgG8PaG%2F4tkI6tVBRwHcE5Xx6f8Die3t%2B40NPPYO35DRfg5MNXjxXKpvxrbc%2B8nnnTcaof74GTiGVfF2ihSKQAwvpnXR9G%2BXB3Cz4zROjMtkyiMWIZEfpc5YWckpWJHpiaZ%2FiN0R7vcLSNCWPH%2FDxRwkmLZJMVMxOys%2Fn7%2Bg2iyj17cSUluY%2F1grn1g%2BRd%2Ftt5sEaG%2BK%2Bol6BCnJ0V%2FJiqDF4%2FPHbvg0J5jNI7Y8dsxkBUQI4PLMExrOisPHItPyqpWp9bGaFaEQDm4b2jTFiFTv0AXJPH8CMTzKx4QNVDxiTHSPwQ38TFIyHHVmw8LTAdjOLRrffXs4dNJydkOeCupXvffrq3fS%2FDZJovPeuV4VtWbETmlkUM%2FY2%2FtDooNoqx%2FhOG9rbqJCfgR9EVeMN%2FEjNgGOqUBUL49%2Bxp5K4Ww%2B9jzPDxgWyu%2BZNd0AjzMRp3bqLXPHUtpyhowftS8Qv4fQ7PDocblFOzMZVMBocievxX%2FpamQU%2FZSSIlPY4N3s2Y7kx8EM%2B%2F%2Fb5FF5fWrhlTPh74qYXdYRGTB8VRqA1igXzaeUwcyUhzaG2frSMfiWBcP%2BpL8tqGk8iKm40vQaH4YIDvDJQtOMuCMhsD0l3sBHOJVqxVBsdwWzcOu&X-Amz-Signature=8850a8f0b623ac886cc592bdf120d4e6dde7dba31b5b7d378e7a437a0f68bd3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643U76ZNK%2F20261122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261122T180511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGerJFtKLEsAEJcG3WsUJDrGkh%2Fdz3Zm4TRLJCQrxST7AiEAt%2FUWis55P9BeSyef8iZ%2BXsK7PWVROZ9HNEtsI9Bkcx4q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDFsETLfj6E575eSQVircAzet4dE2Ui6tXbMbC47WKukrfSrvHSR5vHdP5lO2zil7rbYfku3jPG3xYo%2F83szcceelT70VDq%2FMF8wcM7L6pHTjSnuq%2Bmcb2tCwKYiOpUpXg8iWq3kuduZzFvmCe1Jdf3Cg%2B%2BKo3hQvm98d4gUb%2BCs0FhdO5kQme5GMkrSZZAwPzekS4JgxDceRpTiuxw9UhKYLpr%2BZ2OAoTTHgS1sazzpQ09We%2FUFiD8DC1TQW0XgG8PaG%2F4tkI6tVBRwHcE5Xx6f8Die3t%2B40NPPYO35DRfg5MNXjxXKpvxrbc%2B8nnnTcaof74GTiGVfF2ihSKQAwvpnXR9G%2BXB3Cz4zROjMtkyiMWIZEfpc5YWckpWJHpiaZ%2FiN0R7vcLSNCWPH%2FDxRwkmLZJMVMxOys%2Fn7%2Bg2iyj17cSUluY%2F1grn1g%2BRd%2Ftt5sEaG%2BK%2Bol6BCnJ0V%2FJiqDF4%2FPHbvg0J5jNI7Y8dsxkBUQI4PLMExrOisPHItPyqpWp9bGaFaEQDm4b2jTFiFTv0AXJPH8CMTzKx4QNVDxiTHSPwQ38TFIyHHVmw8LTAdjOLRrffXs4dNJydkOeCupXvffrq3fS%2FDZJovPeuV4VtWbETmlkUM%2FY2%2FtDooNoqx%2FhOG9rbqJCfgR9EVeMN%2FEjNgGOqUBUL49%2Bxp5K4Ww%2B9jzPDxgWyu%2BZNd0AjzMRp3bqLXPHUtpyhowftS8Qv4fQ7PDocblFOzMZVMBocievxX%2FpamQU%2FZSSIlPY4N3s2Y7kx8EM%2B%2F%2Fb5FF5fWrhlTPh74qYXdYRGTB8VRqA1igXzaeUwcyUhzaG2frSMfiWBcP%2BpL8tqGk8iKm40vQaH4YIDvDJQtOMuCMhsD0l3sBHOJVqxVBsdwWzcOu&X-Amz-Signature=df9ba402fc5a536df57874f99d4b4e7056ede88208be412cfcd1649c91d2511a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







