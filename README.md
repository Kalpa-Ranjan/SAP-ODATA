



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GY5T5W%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T012839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIHFahW%2F8xwsvsU3ynFuxRjLKiMKSA%2FCOtEhXvZbK%2FxBDAiAU4B8r%2BMmZrnHnpray7dNeKT16sYl9R2KdqM7VQK2VByr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIM4EzHjwFRWDOtqmMFKtwDfSTuiblM%2Bl0QkpRZFGMQPgAZfD1A8MTBXpU4BBHXHjNGWy0ks90MEV9l2zuDWhALvR9KOz2s%2BY1ZafbUAkyKpBkgJPEpr%2FT3vlkIBulgsI1wWH9Kc%2BS1yqu8ebn3LKOUW19QGZQLvZshGdYWxFLgta%2BavdPu4MxtbmatccISYDV6Nb0VVYLzASPEOUPHQ2GaNH5kbGCAyrcRg8iM4IylS4up7WTQ5a2BHD4mhtKs%2BhnywTVurSQmxsp1rO5j5gW45xr4EM7d3Y5UiGjLFdzx0%2FcNGwb4dQDL37LWCkdMArnhJ6576IzTtFK%2FV8nGsA1u6eJF3g0mQad0lrxjv%2BZVy3hydw%2BKkV8OWnSfS74xTeaZuQnMcLmg%2BYAmJJ4oJO5CXVja2vIEeoP776KIidGmXTJXdhr4eUjzaqXxZo0xnW5mmpSwPsRj6Gpy37iY2eJ1XuUwX1T2DIXqqEfZjQFxpZ%2FU80YcTXOpoG31btsphm0HVSXdMLEPlU%2FxcNg6vTk9Yzs7%2BjKQjAlCWhDTJlIJUz771jPUcW%2Buz7i4ubvPYw7%2BNWXSlb8cOp6XNFtAaUeJbCWcqIK8A7fGkfb0GDBm1kLjLv3sxDlL2H3%2FzF1o6gDzldXQ%2FFOTYHSqLocwyOW9zQY6pgHfp62uZn%2BiUhuLNJ3XeALHih8lF7RvnDrrBjxgk%2B4Yl8kEUeGKAx9%2FcCmdOgsH8v2sKcOVwIWb3R3F6vTEQXyM3WJX4Ada2YwWrk%2B%2BkpkIGp7No0bZ%2BFhh4Bv4J9JctJVCp8FW6%2BqXbrAl0FrURPeymAjicWQIq2lwlYyu7%2FSa%2FlS9zxev%2FEbZ3SKAME5QJmsRcPjp5itjvQuw2im%2FFPPRtvTENf3J&X-Amz-Signature=11fb98a90fe8faedba474d3247f364c5430a7331286bd255f13e222d5e4f7804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GY5T5W%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T012839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIHFahW%2F8xwsvsU3ynFuxRjLKiMKSA%2FCOtEhXvZbK%2FxBDAiAU4B8r%2BMmZrnHnpray7dNeKT16sYl9R2KdqM7VQK2VByr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIM4EzHjwFRWDOtqmMFKtwDfSTuiblM%2Bl0QkpRZFGMQPgAZfD1A8MTBXpU4BBHXHjNGWy0ks90MEV9l2zuDWhALvR9KOz2s%2BY1ZafbUAkyKpBkgJPEpr%2FT3vlkIBulgsI1wWH9Kc%2BS1yqu8ebn3LKOUW19QGZQLvZshGdYWxFLgta%2BavdPu4MxtbmatccISYDV6Nb0VVYLzASPEOUPHQ2GaNH5kbGCAyrcRg8iM4IylS4up7WTQ5a2BHD4mhtKs%2BhnywTVurSQmxsp1rO5j5gW45xr4EM7d3Y5UiGjLFdzx0%2FcNGwb4dQDL37LWCkdMArnhJ6576IzTtFK%2FV8nGsA1u6eJF3g0mQad0lrxjv%2BZVy3hydw%2BKkV8OWnSfS74xTeaZuQnMcLmg%2BYAmJJ4oJO5CXVja2vIEeoP776KIidGmXTJXdhr4eUjzaqXxZo0xnW5mmpSwPsRj6Gpy37iY2eJ1XuUwX1T2DIXqqEfZjQFxpZ%2FU80YcTXOpoG31btsphm0HVSXdMLEPlU%2FxcNg6vTk9Yzs7%2BjKQjAlCWhDTJlIJUz771jPUcW%2Buz7i4ubvPYw7%2BNWXSlb8cOp6XNFtAaUeJbCWcqIK8A7fGkfb0GDBm1kLjLv3sxDlL2H3%2FzF1o6gDzldXQ%2FFOTYHSqLocwyOW9zQY6pgHfp62uZn%2BiUhuLNJ3XeALHih8lF7RvnDrrBjxgk%2B4Yl8kEUeGKAx9%2FcCmdOgsH8v2sKcOVwIWb3R3F6vTEQXyM3WJX4Ada2YwWrk%2B%2BkpkIGp7No0bZ%2BFhh4Bv4J9JctJVCp8FW6%2BqXbrAl0FrURPeymAjicWQIq2lwlYyu7%2FSa%2FlS9zxev%2FEbZ3SKAME5QJmsRcPjp5itjvQuw2im%2FFPPRtvTENf3J&X-Amz-Signature=0a804adebaf89faa9482690b93c9f4c5da72e5e40298806fe7cda9bb1d6f9fee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







