



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH7EW2OQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T123047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDM67m7J6g%2FmVXFuh0Ij0rbYeA3YVOeha4322Mwk4mBMwIhAKuJJaMDdGHktsFldTYjBwzkLzdSoxmduweXmtCJElIEKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFiiHcRsTMSwXLCVQq3ANRBnBfDbdx%2FQuSa%2Fiv8Q70HlgscBu9nCY0BInz4IQ6WKOrgV3VnK%2BbE66Cf6cG0bmzROUabG8nT81p3zfAaWT5yTbryrkJmVbG8JDWz95BkYuzc3p8tY02Wbb1rVCfqt4PjEiNMjLkeElJGxN%2BCA3kISjfc3%2BPIXltJ6aIT9%2FiZp5UWL%2BlU025U0hg0Of3MiiAZMFMCMR%2B0PI%2BvrjSlJiQrbxKQbNWAIm5kNXZJrOe7u7wRGOVmIw45mff1a1FYWQp406tS2In2TfKUzighvyP9yUzSHCU0luBJqa7L4rQ45%2B5l56KbX%2Fnln%2FK3FdEibcGmy4FPYU%2BK88oYhJqw%2FEid7dMcrxK%2BGEhE8nM85cJB41esp2koMrwLs7lXM57ibBx%2FNt0RDvmqN3RVPrP2c2R8FypId38qgYrN%2FPOWpEoS8L6wN%2B7Xzc1hjM1%2B9tDdIrtcDCCvXZoxRPAObXjfwgx7YU3O4SwDfp0%2B8dB%2BxeF1IlTylvD03CXFibQQOh4cmXdaa3u3vsmMSJyc2oTuQU01wsEfBD4u1sGUKySdEi8IZDlZjwA986NxOoLtByb%2BrXNzsiY1Tuxz5Ti29DHYVi0yfVfw63ZKq8OnC59wL6dHIc2LTvnHFsbcOq6TzDTxbfIBjqkAdyFdkXV0%2BWsksyDjBH6ObBrNo4BrOmrmLm9VKe8Ttty3d7F53p%2BhqawovESu5RQrpEA4%2BfHyLg0cXjBPAWv1GwEdO0v%2BkU4dGt7rEDt2pvR3zth9wnvHzKL%2BGyJkc1UfNaOpB4mU0cu2vWHr5zy5RYpxLknp2bapuCZ0sp8%2Fe0X9Q44MHQBM65veomOUYYmZLf9%2BDqA1KTWKtAodwRNvPvMEgI%2B&X-Amz-Signature=b2054de6f8be5f3ba0fdc3295ceb2e488614efc0da1a2e4daf475c9e30f6ea30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH7EW2OQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T123047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDM67m7J6g%2FmVXFuh0Ij0rbYeA3YVOeha4322Mwk4mBMwIhAKuJJaMDdGHktsFldTYjBwzkLzdSoxmduweXmtCJElIEKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFiiHcRsTMSwXLCVQq3ANRBnBfDbdx%2FQuSa%2Fiv8Q70HlgscBu9nCY0BInz4IQ6WKOrgV3VnK%2BbE66Cf6cG0bmzROUabG8nT81p3zfAaWT5yTbryrkJmVbG8JDWz95BkYuzc3p8tY02Wbb1rVCfqt4PjEiNMjLkeElJGxN%2BCA3kISjfc3%2BPIXltJ6aIT9%2FiZp5UWL%2BlU025U0hg0Of3MiiAZMFMCMR%2B0PI%2BvrjSlJiQrbxKQbNWAIm5kNXZJrOe7u7wRGOVmIw45mff1a1FYWQp406tS2In2TfKUzighvyP9yUzSHCU0luBJqa7L4rQ45%2B5l56KbX%2Fnln%2FK3FdEibcGmy4FPYU%2BK88oYhJqw%2FEid7dMcrxK%2BGEhE8nM85cJB41esp2koMrwLs7lXM57ibBx%2FNt0RDvmqN3RVPrP2c2R8FypId38qgYrN%2FPOWpEoS8L6wN%2B7Xzc1hjM1%2B9tDdIrtcDCCvXZoxRPAObXjfwgx7YU3O4SwDfp0%2B8dB%2BxeF1IlTylvD03CXFibQQOh4cmXdaa3u3vsmMSJyc2oTuQU01wsEfBD4u1sGUKySdEi8IZDlZjwA986NxOoLtByb%2BrXNzsiY1Tuxz5Ti29DHYVi0yfVfw63ZKq8OnC59wL6dHIc2LTvnHFsbcOq6TzDTxbfIBjqkAdyFdkXV0%2BWsksyDjBH6ObBrNo4BrOmrmLm9VKe8Ttty3d7F53p%2BhqawovESu5RQrpEA4%2BfHyLg0cXjBPAWv1GwEdO0v%2BkU4dGt7rEDt2pvR3zth9wnvHzKL%2BGyJkc1UfNaOpB4mU0cu2vWHr5zy5RYpxLknp2bapuCZ0sp8%2Fe0X9Q44MHQBM65veomOUYYmZLf9%2BDqA1KTWKtAodwRNvPvMEgI%2B&X-Amz-Signature=155f78a0228e5b74a2d667c761f56641b111803a57e8e2fcc33f8b86a43bd3da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







