



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T277XPJC%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T001914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIGkDXNipN%2B6C1iOF1zf14XtUI5WjaDINZH4odYNZ9DFgAiEAuVg8D1DmmMKPEh%2FXSlwLujU%2FGn4Ax7CeYlCz%2FHawWj4qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1HYv%2FUm7gE56HSsyrcA7YPJ9gI9eonu58Jadjy4xjO4AQNe06lR8IukmGTvgsNtnjy0FlH2a3RtNcO3j6zKk0WHXNfrQ9VHH2T1Tu7qADmMfTKnse8ZvuU7xLpLj8w3Tu82lGdKm66Dt2iSWmVfxpsdFiIunMIwzZdJR514d6RWZdXbNNdkGwQeLEABiBkOhUuQnyiinTuMiZNKT5KhEsXtuyMWBy1OkMDqOylyg4IffVX5L%2FWLHMPHDHOo3oLJvbWJYV4d3UpR%2B9%2B3phaQEh0rwIukSbWjVPx24PR9n5Hiop56KVfqxuXH%2BKPkXgVdfNo7mapOxvGXnHRgd2X95sWpjj6%2FsKxB0g6LMg5%2FFfSvPWmUSE%2FRZibgIbhYo9Not9OxotR0LSutRYt%2FmbOTIyBVhBzo3Q0%2FbJxOYPkM4XEoHdSjvCaCvBbsrC6Msw%2BaMpTAtCPMGKGWYlvnSaFUXJN%2FBunXd9b7gYCBsIehsn8CYuBxoPhvWYLru8sPTBCtuXy8KWmMX8kEl95hY3yrFdy9tWahmEMHCtdv5VnMjAAj5Lv7Yyxeb0Glm2dc5BTwEirf6df3jRypMoFiG29g5kCqVVTg59RcZjx2gAs%2FIMOiUZCbTvfl3pSqQcZjycyW9VeJGJEgP16MEMRMLnU%2F9YGOqUBu632tG4ALOfnfBuPXOJbWbKoXWaSuS708V5ygXJ%2FYtJzMBuRhvoR59hffTby9a6NIzAjmBU%2F0khM6Ey8si0%2FGt9C2lvro9%2BAqCuRy0GR1KuWqfIyHWJb%2BSGX6jIkS5MPxSCGKSZh1aRECQWoQZ6AU2ngCTDOmwDEYAw1H0T2QjaM7dzKcJjZoT25ulWAzYkiLDQuzrjfrqoAn0m71rVDkTorOy3t&X-Amz-Signature=7ce7f5851b19e5f8a461b0a66c922ba3d183be5f6bf1237589e3be2a8c212c37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T277XPJC%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T001914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIGkDXNipN%2B6C1iOF1zf14XtUI5WjaDINZH4odYNZ9DFgAiEAuVg8D1DmmMKPEh%2FXSlwLujU%2FGn4Ax7CeYlCz%2FHawWj4qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1HYv%2FUm7gE56HSsyrcA7YPJ9gI9eonu58Jadjy4xjO4AQNe06lR8IukmGTvgsNtnjy0FlH2a3RtNcO3j6zKk0WHXNfrQ9VHH2T1Tu7qADmMfTKnse8ZvuU7xLpLj8w3Tu82lGdKm66Dt2iSWmVfxpsdFiIunMIwzZdJR514d6RWZdXbNNdkGwQeLEABiBkOhUuQnyiinTuMiZNKT5KhEsXtuyMWBy1OkMDqOylyg4IffVX5L%2FWLHMPHDHOo3oLJvbWJYV4d3UpR%2B9%2B3phaQEh0rwIukSbWjVPx24PR9n5Hiop56KVfqxuXH%2BKPkXgVdfNo7mapOxvGXnHRgd2X95sWpjj6%2FsKxB0g6LMg5%2FFfSvPWmUSE%2FRZibgIbhYo9Not9OxotR0LSutRYt%2FmbOTIyBVhBzo3Q0%2FbJxOYPkM4XEoHdSjvCaCvBbsrC6Msw%2BaMpTAtCPMGKGWYlvnSaFUXJN%2FBunXd9b7gYCBsIehsn8CYuBxoPhvWYLru8sPTBCtuXy8KWmMX8kEl95hY3yrFdy9tWahmEMHCtdv5VnMjAAj5Lv7Yyxeb0Glm2dc5BTwEirf6df3jRypMoFiG29g5kCqVVTg59RcZjx2gAs%2FIMOiUZCbTvfl3pSqQcZjycyW9VeJGJEgP16MEMRMLnU%2F9YGOqUBu632tG4ALOfnfBuPXOJbWbKoXWaSuS708V5ygXJ%2FYtJzMBuRhvoR59hffTby9a6NIzAjmBU%2F0khM6Ey8si0%2FGt9C2lvro9%2BAqCuRy0GR1KuWqfIyHWJb%2BSGX6jIkS5MPxSCGKSZh1aRECQWoQZ6AU2ngCTDOmwDEYAw1H0T2QjaM7dzKcJjZoT25ulWAzYkiLDQuzrjfrqoAn0m71rVDkTorOy3t&X-Amz-Signature=74091ec0052c3154d14bf2aa160f1542a62f602396e6412af6ff988619bef259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







