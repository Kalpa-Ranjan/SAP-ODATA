



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAFO7UKX%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T123833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCRfxSMYGn55dNNpH7WEQo%2BnZ0mxJstEmHJ0uEA6Qb3UQIhAKpgHX3Wxbr6iLQlYRyQtUQX011VuFTyjjwf%2FVhOxlD8KogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igys3aw%2FHoyLe5OY6xIq3APNP1nnCLGTjNMd2GOL49wSHwSYXTgbt3KPgEnIfKreT3z%2FZvs1FFEcQL3X%2FthDQjFoy5%2Bk6qd%2BJjxW7tPC47nNN%2BvqbnQzWDcGHFPCtfxf0DLdyUxoLr4%2F7JqvgdcC3xupb%2Bm5hSuEd9OvwAt9xiNuMs1A%2FRbrFyaNYam0crbrQD3eG%2BK4ol6hMv6TxOSjPXNgh7xAr4SeOjFr5IdvFM%2FvQOVjJW30BG6d0O8%2B%2FGKkL3XYr5CFpdzyZvLPdo%2BI7%2FOQdyYjVLU%2FrDeN2obkzqDotxSn4RT5T1Pj8S6PziMZtCsQ2K0NJYcijxfTAZfbSTsy%2Bye6mqYZfH9gzQ4jJaTfnH%2F4VOk%2FTk8edSUenhZl6mH%2BxkwFKHUP4KqMhHSJA7OY8%2BN3Iukqo8uMRmZiCtmEmhYw3tm2%2FDeDsKu5RVdVPqCr%2BLWw5BZ1%2FiTHU2PN5ldhLaWS7jHe6tkBlBIJBgSnLzTNDh8gni2vT%2FjbBZtsot7mEey86CNF4%2F1nFxyesr1I9bHYZAymcHAx04w%2B5XCosaSZObypWats6bwu39P3xcPYW16%2BOwZvJE72XYymO1U9Cey0ORpm%2B6VvBxxKOx9A%2FNKQnIK0jf5G3e6oAHcGr2BNba3a5r4nGRbkiTC96PzLBjqkAUPFtZqQ%2F7v3Su%2FUHZM9%2F3sOo3%2B%2BwkMXXsUcncmDwaGyPRFrVlJZs2m8zN%2BvvpRmvnPN3maG1k2gofyM7JWA5m05tcuRZ11DU2B9KNUUQoNs8eueRuV9bacfZAo1lZPXxYVxlKsWB7LMiriG47XvR6XKedNFzWuWM6dbvdQfRWI%2FlRTw43%2FtFkHyDwAGXHl%2FW8rU03YGizqVBEmrAzurzjTa7SXk&X-Amz-Signature=7d5dce51c3ffe63ddc4ef8e35d330f7d4603f33fb1b2d3d17830682df1156697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAFO7UKX%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T123833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCRfxSMYGn55dNNpH7WEQo%2BnZ0mxJstEmHJ0uEA6Qb3UQIhAKpgHX3Wxbr6iLQlYRyQtUQX011VuFTyjjwf%2FVhOxlD8KogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igys3aw%2FHoyLe5OY6xIq3APNP1nnCLGTjNMd2GOL49wSHwSYXTgbt3KPgEnIfKreT3z%2FZvs1FFEcQL3X%2FthDQjFoy5%2Bk6qd%2BJjxW7tPC47nNN%2BvqbnQzWDcGHFPCtfxf0DLdyUxoLr4%2F7JqvgdcC3xupb%2Bm5hSuEd9OvwAt9xiNuMs1A%2FRbrFyaNYam0crbrQD3eG%2BK4ol6hMv6TxOSjPXNgh7xAr4SeOjFr5IdvFM%2FvQOVjJW30BG6d0O8%2B%2FGKkL3XYr5CFpdzyZvLPdo%2BI7%2FOQdyYjVLU%2FrDeN2obkzqDotxSn4RT5T1Pj8S6PziMZtCsQ2K0NJYcijxfTAZfbSTsy%2Bye6mqYZfH9gzQ4jJaTfnH%2F4VOk%2FTk8edSUenhZl6mH%2BxkwFKHUP4KqMhHSJA7OY8%2BN3Iukqo8uMRmZiCtmEmhYw3tm2%2FDeDsKu5RVdVPqCr%2BLWw5BZ1%2FiTHU2PN5ldhLaWS7jHe6tkBlBIJBgSnLzTNDh8gni2vT%2FjbBZtsot7mEey86CNF4%2F1nFxyesr1I9bHYZAymcHAx04w%2B5XCosaSZObypWats6bwu39P3xcPYW16%2BOwZvJE72XYymO1U9Cey0ORpm%2B6VvBxxKOx9A%2FNKQnIK0jf5G3e6oAHcGr2BNba3a5r4nGRbkiTC96PzLBjqkAUPFtZqQ%2F7v3Su%2FUHZM9%2F3sOo3%2B%2BwkMXXsUcncmDwaGyPRFrVlJZs2m8zN%2BvvpRmvnPN3maG1k2gofyM7JWA5m05tcuRZ11DU2B9KNUUQoNs8eueRuV9bacfZAo1lZPXxYVxlKsWB7LMiriG47XvR6XKedNFzWuWM6dbvdQfRWI%2FlRTw43%2FtFkHyDwAGXHl%2FW8rU03YGizqVBEmrAzurzjTa7SXk&X-Amz-Signature=975c075be81f9b7ceed74728afedff9ea5b1566b1de15d48248f957dd929c350&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







