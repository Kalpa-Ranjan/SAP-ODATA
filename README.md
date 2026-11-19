



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M66FK55%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T001250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDWct8Pujdxd9Q2rVFBExdR4wy6Fs5cKvtFcv7VlobqqgIgeW6Wd3iM6QFjWWrbDVDIQifVYUWhMKJZUHEvOe2oTzoq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDD5L4gPy3OhSbs6zgSrcA36MhjmaCye7T%2FtbGxwx%2B9xhB%2BAkSelI0v8D%2F2sekP4YjzHGMP1CHkFiN%2BXW97viasIV3rF9%2BMiIBtpA%2BmtXkZSCtXaQCgzGO%2FjbW6k9lraW3En11kSilgrPC8U3%2BPzZQAJCT0IuLbKbWvoTC6ZkRMU3Bzl9%2FeQyOafKkdnDDf8xrMzTUl2Rfy0iz3i2xiQfiop%2BhQpfB6ahD0l96XYZBsfbM7x8ft7o2TH7t6RfG4zs0SRq7n38l2Z26pgM9tCHdVLBDl5TQe2nk0vA0oGpadptE%2BiXLiqzlNV90OpepBqRVFOxuS8ZY85HiUIUjS2MQVfwFHV1DkJ9hM%2FPgWOMqwBjqkYOmUpG62vboYF6niE7x1JsavnOoUYNwrr9kXNsFlWDk6CncWgmTQ0Dz%2FSpKLRL6NqG7R4QZlMwmbk4DDtOVcNek23baDtBpA7xBL2Yr7agzxafAu5pJGF0ejpEDkBQKNjkUoT783mEXVct%2FAJt1IVhZ%2FxQSJb9p25jMmHLOeTM1dYMADL2KBpP%2FKpYJZMT15FTt98C194iSGJa81R6P2OoWta%2B%2FvndH03iwJ9MPQR6FLMYJ1wsv6faBJbDDsrUemSj3uKXR7XmC4pjqOx5fjMrYgEGw22TDuUPMJnH%2BNcGOqUBnI0I1%2BRuXBAa64ekhxEIcdsbLvQThloPi9QYNbAWmlnFuWFjBYL8A1omNa%2FU9aULpXW2UQ8elnFjqm3roDYddYC2jklLZfAXQeryNE42u1fmLIIiKZX3s6qqJP3fvZdJmCk7MjDddXTImsdpZMAmsrmkO4%2BNQ5YsjKCLS0HHdbGl1Em7%2B9VbNWQ6TBQ90Bf1zh80vvuF2Ijx4qYxDR3um4p5ldAM&X-Amz-Signature=788992755bdacfdb3465bfa8c8882897f36f44083b5e942bf04839e76c6cb1d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M66FK55%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T001250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDWct8Pujdxd9Q2rVFBExdR4wy6Fs5cKvtFcv7VlobqqgIgeW6Wd3iM6QFjWWrbDVDIQifVYUWhMKJZUHEvOe2oTzoq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDD5L4gPy3OhSbs6zgSrcA36MhjmaCye7T%2FtbGxwx%2B9xhB%2BAkSelI0v8D%2F2sekP4YjzHGMP1CHkFiN%2BXW97viasIV3rF9%2BMiIBtpA%2BmtXkZSCtXaQCgzGO%2FjbW6k9lraW3En11kSilgrPC8U3%2BPzZQAJCT0IuLbKbWvoTC6ZkRMU3Bzl9%2FeQyOafKkdnDDf8xrMzTUl2Rfy0iz3i2xiQfiop%2BhQpfB6ahD0l96XYZBsfbM7x8ft7o2TH7t6RfG4zs0SRq7n38l2Z26pgM9tCHdVLBDl5TQe2nk0vA0oGpadptE%2BiXLiqzlNV90OpepBqRVFOxuS8ZY85HiUIUjS2MQVfwFHV1DkJ9hM%2FPgWOMqwBjqkYOmUpG62vboYF6niE7x1JsavnOoUYNwrr9kXNsFlWDk6CncWgmTQ0Dz%2FSpKLRL6NqG7R4QZlMwmbk4DDtOVcNek23baDtBpA7xBL2Yr7agzxafAu5pJGF0ejpEDkBQKNjkUoT783mEXVct%2FAJt1IVhZ%2FxQSJb9p25jMmHLOeTM1dYMADL2KBpP%2FKpYJZMT15FTt98C194iSGJa81R6P2OoWta%2B%2FvndH03iwJ9MPQR6FLMYJ1wsv6faBJbDDsrUemSj3uKXR7XmC4pjqOx5fjMrYgEGw22TDuUPMJnH%2BNcGOqUBnI0I1%2BRuXBAa64ekhxEIcdsbLvQThloPi9QYNbAWmlnFuWFjBYL8A1omNa%2FU9aULpXW2UQ8elnFjqm3roDYddYC2jklLZfAXQeryNE42u1fmLIIiKZX3s6qqJP3fvZdJmCk7MjDddXTImsdpZMAmsrmkO4%2BNQ5YsjKCLS0HHdbGl1Em7%2B9VbNWQ6TBQ90Bf1zh80vvuF2Ijx4qYxDR3um4p5ldAM&X-Amz-Signature=7e698399f979f04670262facb168a837c336e68a29c012809e787c725b65608e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







