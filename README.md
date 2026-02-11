



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UODBYIZP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T125830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyt6E8yHDbL4%2FFLK6QPJbE%2BCawnpX2gnOxHrZzgTiO6AiEAwB%2FjQZ8v5ZrDHvZNsgFEjVz4NyKcwG1vYvGIgbeP5ssqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXOmxaKSOUZt0nSdircAynwk7iZCcL24Kgweiydl92hAeptOUvaFCrlQMv36tavY3LwU5ycyYLvrI31%2FbKXkMTGvQY7FckE1936QTWlnrJ%2BgPrzKoCntQYKb7KvGbM40lDkrF7GzZgaaBQgPnGVnujUcVZXMvSvt9qMCkgq4urMMKoGI1YKEq7IULtpswUsDzHegCAxEBHRwbc5DmcMx7W4z2mE6qaiLN%2Fmg9z8fjBQRutUDNyK%2F4i4qj4rMdJMcoHvdMxSL3ks4EyPKRFbrykwEXoZcm7q%2FTJYaT8Sfl1zh9io7WffPV5eRR0UZ%2BfGjqH4L5wrG2%2F8lzkoY4eYiq4mWvve2clv0WkSouJoKNXgja6IJRlZz6nYreTHTwJ4u%2FJzEoPEUU6Pi1USk%2Fidz0SfwYtIt%2Bu9MJ9JYfuweLK%2FPVIwxn57QfvglBLFl%2Fv%2FLQyq%2BrxidNDudzk8C1%2FqKs2f0GunjOC1vCtSgPwjbH2iXN%2B7KuZjwuCV1yU%2BZalCWQDjpalLT141FOPiGSIb4hdVbL%2BSewCvnNklyX4%2F%2FAjdU61vY58GxtmXLdo%2FbIyOVCTXrdzDNtC4L6sh%2BCF%2Btle6TmkywEjKea8kZxb37GLM0uM%2FWe1js6mzbc0bjL%2Fw1B6NUBc0reYeWyUrMPvgscwGOqUB6PekSYaL3jC%2FRXDS3ggm5qVvCa5OI9jqQ7QEaK3gB%2BlcCNlHNgQaDJ2xtw5KXn6QoL9lDTAqzRYSBH0poEj83%2FP%2FXqiskQF6DtOqTrcO1H6mH9uJPIM7fBWjWUNEuh0J3G3NC7O6%2FTPo2lF54ZPik5nzwU3YY3iCmhWl4sZLeqKCn1aRlEo8vWyj9WfCexuL%2BTgQ0MBN4uHkLfMIshsi5sH9XgXP&X-Amz-Signature=55feac773db46e03349c0481cb020add6fa55e564b000cf86a2f0959e03bc52e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UODBYIZP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T125830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyt6E8yHDbL4%2FFLK6QPJbE%2BCawnpX2gnOxHrZzgTiO6AiEAwB%2FjQZ8v5ZrDHvZNsgFEjVz4NyKcwG1vYvGIgbeP5ssqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXOmxaKSOUZt0nSdircAynwk7iZCcL24Kgweiydl92hAeptOUvaFCrlQMv36tavY3LwU5ycyYLvrI31%2FbKXkMTGvQY7FckE1936QTWlnrJ%2BgPrzKoCntQYKb7KvGbM40lDkrF7GzZgaaBQgPnGVnujUcVZXMvSvt9qMCkgq4urMMKoGI1YKEq7IULtpswUsDzHegCAxEBHRwbc5DmcMx7W4z2mE6qaiLN%2Fmg9z8fjBQRutUDNyK%2F4i4qj4rMdJMcoHvdMxSL3ks4EyPKRFbrykwEXoZcm7q%2FTJYaT8Sfl1zh9io7WffPV5eRR0UZ%2BfGjqH4L5wrG2%2F8lzkoY4eYiq4mWvve2clv0WkSouJoKNXgja6IJRlZz6nYreTHTwJ4u%2FJzEoPEUU6Pi1USk%2Fidz0SfwYtIt%2Bu9MJ9JYfuweLK%2FPVIwxn57QfvglBLFl%2Fv%2FLQyq%2BrxidNDudzk8C1%2FqKs2f0GunjOC1vCtSgPwjbH2iXN%2B7KuZjwuCV1yU%2BZalCWQDjpalLT141FOPiGSIb4hdVbL%2BSewCvnNklyX4%2F%2FAjdU61vY58GxtmXLdo%2FbIyOVCTXrdzDNtC4L6sh%2BCF%2Btle6TmkywEjKea8kZxb37GLM0uM%2FWe1js6mzbc0bjL%2Fw1B6NUBc0reYeWyUrMPvgscwGOqUB6PekSYaL3jC%2FRXDS3ggm5qVvCa5OI9jqQ7QEaK3gB%2BlcCNlHNgQaDJ2xtw5KXn6QoL9lDTAqzRYSBH0poEj83%2FP%2FXqiskQF6DtOqTrcO1H6mH9uJPIM7fBWjWUNEuh0J3G3NC7O6%2FTPo2lF54ZPik5nzwU3YY3iCmhWl4sZLeqKCn1aRlEo8vWyj9WfCexuL%2BTgQ0MBN4uHkLfMIshsi5sH9XgXP&X-Amz-Signature=c863de1c6eadcf5cc44f73bb7d93da79e9463f28cdcb214c0fddedcec7877726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







