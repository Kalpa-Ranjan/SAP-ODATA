



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5UZFEVJ%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T121103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBBF71ylTy6ymVKRdyjX%2B%2FDw5lN7yOlXZf3v0VW19o2DAiAbfxHM70yQRNwpYdWn3eLiPGsdu0VcGyZGS2TTUBl9jir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMLTljVLydZbFEFWRyKtwDD9UAFDefVW3qx72ol02%2BpjQ8OY2Ccy%2Bu6EBYfZTAQOVQpftRKTwjES%2FPGTiqxRimprIhElaCfONM0VoVmHqHr%2BUnyzTA%2FKDBFa8W%2BXDt6WYWQKpRTaXWiqG2M14itzBEamukbS0MySSJrwg2NMiXOXHbiurqFHWjO%2BQxrHntE6u7dFnH5F98BE65oTeiyR7Vip6WZQnLBAEoipPGWrl%2Bpeswr%2Bd9rXw0bH7qyWk8ryDLfUpL3QywlfelYS8EmFHx5YFz7wlHwDK7tGivbM7cTuR5wl5CfV0VNVEdc6rbBexXcT%2FDUQWzgjVF3ipX1DQDUbASg654%2B7jqMtHCDh5khJZIC8ZTQGon0jdpl1eYRy9fEoSfDTF1Qgs%2FLfpd5eH5vtCtNiNTnOS6QnQg8whOxknqvq6tQuURyargZU0M%2Fq3zFKKhItD%2BTQQ3U6W2fv3ohA2iTG2vhZjnAKN8HgyyQ2ffce490teTW%2FTLOALFqMZ8OdkEWTX8Whb4knBzc8girunCCWZDjJUPSeiBYFtHhUOxyChZltTX%2Bql1B%2FCSBvc6x%2BODR4iKv47W0pl3po0ArGk6TUJiwi0Pfe0TORkqYCz0tutgvZmsq0Z8JqTjXraJR9f4psoxZWb5ZnQwuumn1gY6pgGJkNwIKR1abvGrobaJxpTuVfv%2F3qNtuOmKxYV0sTukaNivH5%2FrAivZ46IFEWgQU542X5f3nFSha98brMO9bncnRy0wf%2Fqcoz%2FLQ%2BwGQcDP316lfPnrU3eXq06l1%2BBUK6ixnC9EF%2BYU4%2FdOIJl%2BH%2BjuD98dereMOyZxXOyUgPk6%2FXCIQHmrgJwl5RPPL%2BEv8ssJuL6homTM02TjhrYhhEps5wRcGxB9&X-Amz-Signature=d5514934b9a4cd40e6f81f618a12c47da635fb234ced4897da77d427aa814aa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5UZFEVJ%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T121103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBBF71ylTy6ymVKRdyjX%2B%2FDw5lN7yOlXZf3v0VW19o2DAiAbfxHM70yQRNwpYdWn3eLiPGsdu0VcGyZGS2TTUBl9jir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMLTljVLydZbFEFWRyKtwDD9UAFDefVW3qx72ol02%2BpjQ8OY2Ccy%2Bu6EBYfZTAQOVQpftRKTwjES%2FPGTiqxRimprIhElaCfONM0VoVmHqHr%2BUnyzTA%2FKDBFa8W%2BXDt6WYWQKpRTaXWiqG2M14itzBEamukbS0MySSJrwg2NMiXOXHbiurqFHWjO%2BQxrHntE6u7dFnH5F98BE65oTeiyR7Vip6WZQnLBAEoipPGWrl%2Bpeswr%2Bd9rXw0bH7qyWk8ryDLfUpL3QywlfelYS8EmFHx5YFz7wlHwDK7tGivbM7cTuR5wl5CfV0VNVEdc6rbBexXcT%2FDUQWzgjVF3ipX1DQDUbASg654%2B7jqMtHCDh5khJZIC8ZTQGon0jdpl1eYRy9fEoSfDTF1Qgs%2FLfpd5eH5vtCtNiNTnOS6QnQg8whOxknqvq6tQuURyargZU0M%2Fq3zFKKhItD%2BTQQ3U6W2fv3ohA2iTG2vhZjnAKN8HgyyQ2ffce490teTW%2FTLOALFqMZ8OdkEWTX8Whb4knBzc8girunCCWZDjJUPSeiBYFtHhUOxyChZltTX%2Bql1B%2FCSBvc6x%2BODR4iKv47W0pl3po0ArGk6TUJiwi0Pfe0TORkqYCz0tutgvZmsq0Z8JqTjXraJR9f4psoxZWb5ZnQwuumn1gY6pgGJkNwIKR1abvGrobaJxpTuVfv%2F3qNtuOmKxYV0sTukaNivH5%2FrAivZ46IFEWgQU542X5f3nFSha98brMO9bncnRy0wf%2Fqcoz%2FLQ%2BwGQcDP316lfPnrU3eXq06l1%2BBUK6ixnC9EF%2BYU4%2FdOIJl%2BH%2BjuD98dereMOyZxXOyUgPk6%2FXCIQHmrgJwl5RPPL%2BEv8ssJuL6homTM02TjhrYhhEps5wRcGxB9&X-Amz-Signature=f7344bbfa9fb0103a6de5fbac1677640a65751fcfe5024bf6895f675e29473cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







