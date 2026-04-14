



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPCBX573%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T020427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFy%2By0awwmkdWEC4dz2pwCNOQsDciHDVPMGb1t2X2fx4AiEAl3pBoYAIuAAPsD6N242Nq7pO68pcV3msy3RDtWOUnBEqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGGKLV8vvxe8bsTwICrcA0LUkGuYZzZMvYMrFQpGZCaOHq5J%2FObVfdqzn5K0cYfj2UhBHXs%2FkBI15DCAowygeFVdX4UycVUzJX80nc4nytfylqKPV%2FinXEG73TUmJKKcxUHZOGfog9d8XTV5SksqLkuo0%2F2S6koIjsVS78AYLXDxNwYBWfDtxnAStzxVgVpIviyBvVfvRl91emRd1Eaq7NIT2mES%2BRL4invjEAY3iaKCeazil4kmHw5%2Fbi74AQCX3PgdmsJ0WPtwHxeaptwXIezospHMj7IBCnTR%2BdVt9Q9z%2B7a4pEeq%2FHJHGLuvxepLu0ulon%2BtlCsRP0PA%2FPWMisN62tJwsX8N8Bn665q05TRPfpNAu7On2yFAPnnXtyep624%2BD0wQbUS3W0xE%2B1G88YUnaVV%2F63VZ8VQVG8Z%2BBX7qr5tmgscFSqN8AQjzrqMwFi6Gx%2BY9msR3cRr%2BLZ8grdKC6qyG9GuEKLB6O3u3mAWe0Bj%2B53z10KpsqUj7h61wV%2BHQFngFJRfHnTeY5%2F8pjTkHCGAA%2B%2FbstX3cn3bGDU%2BFrbG%2Bhzk3kxU4vMydD%2BDCf0mUCXW90pbi3udt4yXPDaUEjGsxHd3CMZqiC6OnzL%2FOC%2F5M20mtwcqnhcQ3d1BIUl9b1x33buOdnPxKMLeX9s4GOqUB7cxu2nxO9bRbouqScvyqSFh6OW7zsjQiRNjFhI2F0sFZM0ZQ%2BQK3xCcugTzZpslfpK%2BbLMssLbaI436UB0VRnhWxU13CAZDNq%2FgyxsF4K1B%2Bs0yQGn6JsUYNA3raFKsaJ4BB7qIPfNyxq6MkA7%2BOnE%2FUHi94adaVJnB7EIo3qpIXb%2FT0NdEPxv9DAe8hOi7DWANnDQ0A6Fa4Vx%2BA8yZc1D%2FAE%2FEq&X-Amz-Signature=b0abdc13f485db063fd07fe98aa588b1b87659da343869b4649c057412720452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPCBX573%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T020427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFy%2By0awwmkdWEC4dz2pwCNOQsDciHDVPMGb1t2X2fx4AiEAl3pBoYAIuAAPsD6N242Nq7pO68pcV3msy3RDtWOUnBEqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGGKLV8vvxe8bsTwICrcA0LUkGuYZzZMvYMrFQpGZCaOHq5J%2FObVfdqzn5K0cYfj2UhBHXs%2FkBI15DCAowygeFVdX4UycVUzJX80nc4nytfylqKPV%2FinXEG73TUmJKKcxUHZOGfog9d8XTV5SksqLkuo0%2F2S6koIjsVS78AYLXDxNwYBWfDtxnAStzxVgVpIviyBvVfvRl91emRd1Eaq7NIT2mES%2BRL4invjEAY3iaKCeazil4kmHw5%2Fbi74AQCX3PgdmsJ0WPtwHxeaptwXIezospHMj7IBCnTR%2BdVt9Q9z%2B7a4pEeq%2FHJHGLuvxepLu0ulon%2BtlCsRP0PA%2FPWMisN62tJwsX8N8Bn665q05TRPfpNAu7On2yFAPnnXtyep624%2BD0wQbUS3W0xE%2B1G88YUnaVV%2F63VZ8VQVG8Z%2BBX7qr5tmgscFSqN8AQjzrqMwFi6Gx%2BY9msR3cRr%2BLZ8grdKC6qyG9GuEKLB6O3u3mAWe0Bj%2B53z10KpsqUj7h61wV%2BHQFngFJRfHnTeY5%2F8pjTkHCGAA%2B%2FbstX3cn3bGDU%2BFrbG%2Bhzk3kxU4vMydD%2BDCf0mUCXW90pbi3udt4yXPDaUEjGsxHd3CMZqiC6OnzL%2FOC%2F5M20mtwcqnhcQ3d1BIUl9b1x33buOdnPxKMLeX9s4GOqUB7cxu2nxO9bRbouqScvyqSFh6OW7zsjQiRNjFhI2F0sFZM0ZQ%2BQK3xCcugTzZpslfpK%2BbLMssLbaI436UB0VRnhWxU13CAZDNq%2FgyxsF4K1B%2Bs0yQGn6JsUYNA3raFKsaJ4BB7qIPfNyxq6MkA7%2BOnE%2FUHi94adaVJnB7EIo3qpIXb%2FT0NdEPxv9DAe8hOi7DWANnDQ0A6Fa4Vx%2BA8yZc1D%2FAE%2FEq&X-Amz-Signature=54ed4a3ac55a7813cd2e366b1050c754a5fa04b468c201225582fda064bb9eca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







