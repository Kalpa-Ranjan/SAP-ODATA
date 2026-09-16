



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOG4D5IL%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T180852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDo1LxFdfbLmgJiK%2BposEVHUPYm%2FbA%2FN6QsY%2BKzKqdVZgIgUIFTw%2FXM1Pgwd0S%2FLZvGCkWi1TI%2BlpUCVzSp%2BmysHqEq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDEbuBp0mqoXle%2ByYQCrcA0ug95SuiMjyBkZsky6o%2B5vMdSNyn0aR1WAlsoLKCmiRvyKQKjfQSx1UZA5kwea2pTE7WoSpfVOLfUqWOP3cCl7r8D0GUv6Ei5aekXQ0w1WtwS9g7qVlW3nCotcoYqieLtzPFqFYrqDXCEGEw2gM6qFOudz0P1GMwEgIxIUly1LaOPcpVNQ8QP0jJQe8UXPpoh4yQ8spxJp0cCr4oj4MpddYQjDoJVbyr6tfR%2BEkCHoMuIFgg0yhCgc5D%2BK%2FkC5hPSb3QWGZ4YOj5a2Zf2gizOm6WvmRhB3JtIJNMbAj7gMics18Sb2g7D3XxjFcjG37oFi1doRE5y8YYSD%2B6uOMoNbHVMKkKi%2BGQlOGU6RZP%2BqFNvxyHeTpOxA2eUVuCBhFK1U%2BQDF1mMm%2ByIoPFt3TRGUipYSHc2hGixtOL%2BEA8mjzZQ5eJsIw2%2Bd3uiS6th1FvjTdJQAnQsFSM%2Fqfb0zqwoNDru8p0ysg35aMe2G5deRnrOC4QsH0DHKe2ChzqOI6Rh5O2qQo52fupkaE5RL4q3JRDYRJmjxcd%2FyY%2FAmddOs6xLmowy7p1CDCSFDgQtxmh2fFsTTB%2Fur0Rej60jB6ifca5eyRrKsLi4a0LZmYN5zE3xKQ8pmRMknwWMoRMOaeq9UGOqUBbgzZGF%2FJ8d3VlymDvkmRTByyuANRaztLq9JYpIW4XTHENqwESEfjr6yohuePv%2B%2BDljlawcKOpH850yb4x%2BhPYjzP1CS6PPK4juGmFHVgE0J4soj9DM3DS%2BvXEo53GBp4SKZAdg6L%2B%2BXcghEDLEyvc8rfpQ%2FADO38UQdQftqaa0irBA1P7Q2RKYfnSrib4kSX0xWLCXCiGU%2BWT4YOEqqNAlTwgSaA&X-Amz-Signature=d956ec7a5fa0aa97af680528b1336b5a54fcc9cb3d5f75088e3af1b32a81e3a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOG4D5IL%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T180852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDo1LxFdfbLmgJiK%2BposEVHUPYm%2FbA%2FN6QsY%2BKzKqdVZgIgUIFTw%2FXM1Pgwd0S%2FLZvGCkWi1TI%2BlpUCVzSp%2BmysHqEq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDEbuBp0mqoXle%2ByYQCrcA0ug95SuiMjyBkZsky6o%2B5vMdSNyn0aR1WAlsoLKCmiRvyKQKjfQSx1UZA5kwea2pTE7WoSpfVOLfUqWOP3cCl7r8D0GUv6Ei5aekXQ0w1WtwS9g7qVlW3nCotcoYqieLtzPFqFYrqDXCEGEw2gM6qFOudz0P1GMwEgIxIUly1LaOPcpVNQ8QP0jJQe8UXPpoh4yQ8spxJp0cCr4oj4MpddYQjDoJVbyr6tfR%2BEkCHoMuIFgg0yhCgc5D%2BK%2FkC5hPSb3QWGZ4YOj5a2Zf2gizOm6WvmRhB3JtIJNMbAj7gMics18Sb2g7D3XxjFcjG37oFi1doRE5y8YYSD%2B6uOMoNbHVMKkKi%2BGQlOGU6RZP%2BqFNvxyHeTpOxA2eUVuCBhFK1U%2BQDF1mMm%2ByIoPFt3TRGUipYSHc2hGixtOL%2BEA8mjzZQ5eJsIw2%2Bd3uiS6th1FvjTdJQAnQsFSM%2Fqfb0zqwoNDru8p0ysg35aMe2G5deRnrOC4QsH0DHKe2ChzqOI6Rh5O2qQo52fupkaE5RL4q3JRDYRJmjxcd%2FyY%2FAmddOs6xLmowy7p1CDCSFDgQtxmh2fFsTTB%2Fur0Rej60jB6ifca5eyRrKsLi4a0LZmYN5zE3xKQ8pmRMknwWMoRMOaeq9UGOqUBbgzZGF%2FJ8d3VlymDvkmRTByyuANRaztLq9JYpIW4XTHENqwESEfjr6yohuePv%2B%2BDljlawcKOpH850yb4x%2BhPYjzP1CS6PPK4juGmFHVgE0J4soj9DM3DS%2BvXEo53GBp4SKZAdg6L%2B%2BXcghEDLEyvc8rfpQ%2FADO38UQdQftqaa0irBA1P7Q2RKYfnSrib4kSX0xWLCXCiGU%2BWT4YOEqqNAlTwgSaA&X-Amz-Signature=0572cffaed8d9a48cef37517a0d85fd4061418a8d7fbb157f8cd0291b4867fab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







