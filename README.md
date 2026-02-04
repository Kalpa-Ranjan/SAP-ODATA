



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NQ3NAQG%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T124806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCID10mwy1kOuc42LmoCH95yCWilhzqfaigBI9FgyZuU%2BMAiArnX30COhL5ApvpLyvvH4hd%2B90SV3y3F9UwMN3eZ%2FxCCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMdm5lQS1aSZC1iYILKtwDB%2F1KLj25h8mAjY1vG8OHvEKoURvFSqkXv61ZFJGTujoNR1ecQFsfHANm1JToW9A5rlJ%2B%2FaYvkm3KO7nJuiWOt7XKTmeMejulM0EuNYfWFbYsdqq6RjiyKeGJJfxyC5Kf2nnJrdacgJz3CpTOxZxHkzBI7%2FoBuvQ5jV8TiEaFCZza8urgr16tm2y7FHhlNdy%2Bts4wfyUypDr7SzVODiAPiy4mWO%2FdKnzWbsnaUbL0RAT9zFrCMTsBVA3xAEKsIcUnQnVkKKtXOTjAGCHQDTvWXz509vTzGIcRG594L4UOutgWpIZl9gZ0EzQ6wS63SzM5X4pRrewFnczYh51QailNv458GXpRbBJG5cP6eHMOsi9WtavX0qJ%2FU%2B0CqXhQAj9aHi7zZ1qV5UjzUQgk6stwOZ45xo6tmFL0hamFXe4hojMHLknMJevBNLavn%2F4O%2FD4NMIt5tCXHTbmP6PJxtZu7ZUiz1nxhLjtu2W4NESaT%2B%2FNOCDCqj4Mjjci1lLgF%2F24ZiBkPNcMlT%2BfICZa6wLJ7CgJvv391olwO3Q9SuwTiAu%2BzVrXs9P51YrBeQmDiIIsLgwJKKbZ3NIdqhCVobXh7TfW%2B%2BTJpuibe5dSdVXuvH8nRMh1GMS3Q9A7%2BS2Qwl%2ByMzAY6pgGxm0g%2BBY81Y9Lu6p%2BkXpSK9OxVQqiFxQdelEhbhATHsqHsrxaAQOxagGLY3vXa0Ur1RvF%2FyS4McNQBxUpxjb4UfGOfXNBzDySqxPqcBkvuVvv3KUUV5YbD978KcY8vy2vmMg1B6%2F%2Bazd8t2pimQ8o7XSMVcWoC9MCBY1H79hv5ngrapM7KjU9VcmvXGs4pIgGStt9aW0Hc%2BOGAnAs304IFcD85gcKZ&X-Amz-Signature=7a39cad0456245d3d3502462a6c25b4a1cba215160bdbc179ca483e6cc069467&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NQ3NAQG%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T124806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCID10mwy1kOuc42LmoCH95yCWilhzqfaigBI9FgyZuU%2BMAiArnX30COhL5ApvpLyvvH4hd%2B90SV3y3F9UwMN3eZ%2FxCCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMdm5lQS1aSZC1iYILKtwDB%2F1KLj25h8mAjY1vG8OHvEKoURvFSqkXv61ZFJGTujoNR1ecQFsfHANm1JToW9A5rlJ%2B%2FaYvkm3KO7nJuiWOt7XKTmeMejulM0EuNYfWFbYsdqq6RjiyKeGJJfxyC5Kf2nnJrdacgJz3CpTOxZxHkzBI7%2FoBuvQ5jV8TiEaFCZza8urgr16tm2y7FHhlNdy%2Bts4wfyUypDr7SzVODiAPiy4mWO%2FdKnzWbsnaUbL0RAT9zFrCMTsBVA3xAEKsIcUnQnVkKKtXOTjAGCHQDTvWXz509vTzGIcRG594L4UOutgWpIZl9gZ0EzQ6wS63SzM5X4pRrewFnczYh51QailNv458GXpRbBJG5cP6eHMOsi9WtavX0qJ%2FU%2B0CqXhQAj9aHi7zZ1qV5UjzUQgk6stwOZ45xo6tmFL0hamFXe4hojMHLknMJevBNLavn%2F4O%2FD4NMIt5tCXHTbmP6PJxtZu7ZUiz1nxhLjtu2W4NESaT%2B%2FNOCDCqj4Mjjci1lLgF%2F24ZiBkPNcMlT%2BfICZa6wLJ7CgJvv391olwO3Q9SuwTiAu%2BzVrXs9P51YrBeQmDiIIsLgwJKKbZ3NIdqhCVobXh7TfW%2B%2BTJpuibe5dSdVXuvH8nRMh1GMS3Q9A7%2BS2Qwl%2ByMzAY6pgGxm0g%2BBY81Y9Lu6p%2BkXpSK9OxVQqiFxQdelEhbhATHsqHsrxaAQOxagGLY3vXa0Ur1RvF%2FyS4McNQBxUpxjb4UfGOfXNBzDySqxPqcBkvuVvv3KUUV5YbD978KcY8vy2vmMg1B6%2F%2Bazd8t2pimQ8o7XSMVcWoC9MCBY1H79hv5ngrapM7KjU9VcmvXGs4pIgGStt9aW0Hc%2BOGAnAs304IFcD85gcKZ&X-Amz-Signature=4c7cb48ff2aa6c15ef8d663bfb672a97eff010f05034e34836f92ad2e85752e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







