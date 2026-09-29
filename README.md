



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJNJ7OSE%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T002221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDKRDWRNEGuIPfTgNkjagmSbNSHEwxJ%2FC%2B03s9mYXob6QIgKErPdShfl2M4GKpfdLxuBKfumHzgCysk20Vti6eYiO4q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDH3xWRyNCayDba7HSircAxNOvWyQ%2FnKcGx3HY%2BBTX0CVQl01uNou4S9j3p8NFw5pekosaWq1DD8gVEHnzd%2FO38QSOwmpIakUwVoQbXZYQqgHNyu1cmyBVzrVzdAzVkUO5gyDJFWStrszqEbvANbDohEro84U9fhriYd3y47e6TMJeI7KAKLyQBEx761y8aw6tAFtLmXCjoAInlBIxf6j7Q5Q4yrWHX1SRT3bnkJd0FOYpuVfS13smF%2FsHTJNdoxFN3SU39w3QGiSzyBZyly530EQkBYgurUP9E16Ffe9cgCIK%2B%2FVU6mWUoO9rYOBdqd78dHlOSZGcDxRXSQycJ5QRsoPJcHzbioEj5PqnvkE9iAejjeqKNS1%2B6cPwKwNmUUmuXiO%2Bshjl0Gi1usEh063l2%2Bzhg5MgMuIdifMvSKjNijxqAYZlCUH6Xf%2FKI9FneBR9MY5sA92mVCq26IGHeZ%2Bq6kF4%2B0hqJKfHmVs29ZI54NwVdoiQN0ZkKeC2lVTkFAmo1uwaUujxwC77amEU8VTYmhlWLpNH%2Fl7Xe0%2BWG4GBZAexrTyo0lUdOETVDLj2RlHaI6Sh25O67Uk7tIlKRyFPDJywPwiJdbIBMNssxR8LGM5VEja6cI4zM4eGXmTRLDq5tK6vafgQ3J%2B4vFPMJrw69UGOqUB4RRAIrd%2FPJhlJ2%2BRGKfV0FOYWKZqLZ06I8WGTeoKkWXvLeRXFYyi6g9%2BzKS8EIPwcsnAxK9I3gpmpsxWI%2BYpV%2F5mzwFrQM5Sg%2BOYc7Pn56am8bh%2FtNOsxiu%2Bac%2BGPUklKcHN9tKtQ%2FX%2Bg4AGQkeHdBLHqFLFlebDTVP89ONjfQir1XgzcNeIh%2FaxG8Pd%2B9KXd2woknu%2BPYOtElT3sIpqN6c7%2Fb6Q&X-Amz-Signature=1ff56092313f6b671a2fe141525832027d3065ca7b718d4df670def036a76bfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJNJ7OSE%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T002221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDKRDWRNEGuIPfTgNkjagmSbNSHEwxJ%2FC%2B03s9mYXob6QIgKErPdShfl2M4GKpfdLxuBKfumHzgCysk20Vti6eYiO4q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDH3xWRyNCayDba7HSircAxNOvWyQ%2FnKcGx3HY%2BBTX0CVQl01uNou4S9j3p8NFw5pekosaWq1DD8gVEHnzd%2FO38QSOwmpIakUwVoQbXZYQqgHNyu1cmyBVzrVzdAzVkUO5gyDJFWStrszqEbvANbDohEro84U9fhriYd3y47e6TMJeI7KAKLyQBEx761y8aw6tAFtLmXCjoAInlBIxf6j7Q5Q4yrWHX1SRT3bnkJd0FOYpuVfS13smF%2FsHTJNdoxFN3SU39w3QGiSzyBZyly530EQkBYgurUP9E16Ffe9cgCIK%2B%2FVU6mWUoO9rYOBdqd78dHlOSZGcDxRXSQycJ5QRsoPJcHzbioEj5PqnvkE9iAejjeqKNS1%2B6cPwKwNmUUmuXiO%2Bshjl0Gi1usEh063l2%2Bzhg5MgMuIdifMvSKjNijxqAYZlCUH6Xf%2FKI9FneBR9MY5sA92mVCq26IGHeZ%2Bq6kF4%2B0hqJKfHmVs29ZI54NwVdoiQN0ZkKeC2lVTkFAmo1uwaUujxwC77amEU8VTYmhlWLpNH%2Fl7Xe0%2BWG4GBZAexrTyo0lUdOETVDLj2RlHaI6Sh25O67Uk7tIlKRyFPDJywPwiJdbIBMNssxR8LGM5VEja6cI4zM4eGXmTRLDq5tK6vafgQ3J%2B4vFPMJrw69UGOqUB4RRAIrd%2FPJhlJ2%2BRGKfV0FOYWKZqLZ06I8WGTeoKkWXvLeRXFYyi6g9%2BzKS8EIPwcsnAxK9I3gpmpsxWI%2BYpV%2F5mzwFrQM5Sg%2BOYc7Pn56am8bh%2FtNOsxiu%2Bac%2BGPUklKcHN9tKtQ%2FX%2Bg4AGQkeHdBLHqFLFlebDTVP89ONjfQir1XgzcNeIh%2FaxG8Pd%2B9KXd2woknu%2BPYOtElT3sIpqN6c7%2Fb6Q&X-Amz-Signature=0958b139c8728a46c756e0ed2f097441b7119b2b889734f621039ac09510fbf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







