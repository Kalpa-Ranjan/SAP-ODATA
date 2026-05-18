



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6ODNATX%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T095152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGE9%2BFCgNZsFtptcZNulUdDs4dngM%2FFesjQQbfQ0qSvHAiEAigYuLEFhJhTL3Antrp8TqwmCHu1IVoDNZztMBKev3TIqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF2OCxTACW49hcwx5SrcAwU4JQiKj1bGJcMjlQHF6zNHOujDdOjb3ta2Wl9Wv5rdHSg2AoRvGnLEqhusqxwJ1v6y4Hr6lf1Dub3wCnLefVDaYiCti3yhW%2FP9CNA2MdnKIQ6degm4rU8mo0o6kJABIj5rAGeYbw3Jc0XfWn1ySuV3GVXNtVpqvc4DtYFNjgqslKiiY1IzyFxbwg5Hd03wKMlFg4wmzOHpl8Uf88XqxiaL1XsT2EJeeV2TDaFui9vxll5xjLzsXoy5ByGet%2FjVQrTa%2BBFGf08SVFM%2BEZCiiIuDCbwU8e3yLQTdKN8oREsz4fbjixMhjqw1gfdKYk4CV5dbcJjGo1BWLuBu33OURH%2B6sabfVBr9hAqsb1hlPvWzd%2BR9tV6fjO1zoYHZuIS%2FSZ9HpJNA8aHelIMPnPSvPNQLIxyjmdgAC3vjgK1HelkifW2cDFO%2FZ%2BR78X7hdua6YcFKSa8aMESmAPwcVYoZ5bCtAcoyWfGidLiFkIQexu1gLuu9nM%2BHB3zzbCDvjSXM1jabUfueZE6nXCzmQrvbvD93rOnN%2FS%2BYgtq6g4Ck%2FEAcx1PwGRGRWI4QYK%2FATJpl3X1MTRrQ7b3rvLJ6b2nUZa%2BZkM2wSXQR6PaYs5fxDsgfYjPZzS%2BLt4fi2p%2BBMNyhq9AGOqUBLnv8S6YLODizHvCvoLkD2hvYR%2Fx9GC0iGtkdK7Tgdhpz4JROFTDljlkTFRoqar9E%2BJhYXKGIweX8zBkhBtiYN2zFouI%2Fx74nSxtGr%2B0HIFlrhhCn%2BGt72hhk%2FFjQxrrjfGr8lEB9WQlGJz94aZnHcJMAZ6uli3jfm6wIm80yxAJebcwv51bJw5KIvixyZfS%2FtoA1D6b0e1ovZrW7gou4QxS5lE%2Bk&X-Amz-Signature=3d364b075caad461f8ba73a7fee48fd6a954ea7550a13de27abf1403650b7e98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6ODNATX%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T095152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGE9%2BFCgNZsFtptcZNulUdDs4dngM%2FFesjQQbfQ0qSvHAiEAigYuLEFhJhTL3Antrp8TqwmCHu1IVoDNZztMBKev3TIqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF2OCxTACW49hcwx5SrcAwU4JQiKj1bGJcMjlQHF6zNHOujDdOjb3ta2Wl9Wv5rdHSg2AoRvGnLEqhusqxwJ1v6y4Hr6lf1Dub3wCnLefVDaYiCti3yhW%2FP9CNA2MdnKIQ6degm4rU8mo0o6kJABIj5rAGeYbw3Jc0XfWn1ySuV3GVXNtVpqvc4DtYFNjgqslKiiY1IzyFxbwg5Hd03wKMlFg4wmzOHpl8Uf88XqxiaL1XsT2EJeeV2TDaFui9vxll5xjLzsXoy5ByGet%2FjVQrTa%2BBFGf08SVFM%2BEZCiiIuDCbwU8e3yLQTdKN8oREsz4fbjixMhjqw1gfdKYk4CV5dbcJjGo1BWLuBu33OURH%2B6sabfVBr9hAqsb1hlPvWzd%2BR9tV6fjO1zoYHZuIS%2FSZ9HpJNA8aHelIMPnPSvPNQLIxyjmdgAC3vjgK1HelkifW2cDFO%2FZ%2BR78X7hdua6YcFKSa8aMESmAPwcVYoZ5bCtAcoyWfGidLiFkIQexu1gLuu9nM%2BHB3zzbCDvjSXM1jabUfueZE6nXCzmQrvbvD93rOnN%2FS%2BYgtq6g4Ck%2FEAcx1PwGRGRWI4QYK%2FATJpl3X1MTRrQ7b3rvLJ6b2nUZa%2BZkM2wSXQR6PaYs5fxDsgfYjPZzS%2BLt4fi2p%2BBMNyhq9AGOqUBLnv8S6YLODizHvCvoLkD2hvYR%2Fx9GC0iGtkdK7Tgdhpz4JROFTDljlkTFRoqar9E%2BJhYXKGIweX8zBkhBtiYN2zFouI%2Fx74nSxtGr%2B0HIFlrhhCn%2BGt72hhk%2FFjQxrrjfGr8lEB9WQlGJz94aZnHcJMAZ6uli3jfm6wIm80yxAJebcwv51bJw5KIvixyZfS%2FtoA1D6b0e1ovZrW7gou4QxS5lE%2Bk&X-Amz-Signature=c53e6149250e31070e540d4b65f365d99acd69a8e118e696bbd8a4ba925768c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







