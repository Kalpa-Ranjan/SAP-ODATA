



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q5YUE6E%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T062546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJIMEYCIQCbeKqiQ%2Fgwic6wnmYIPXpMZ129X5Lb3wJKWAxNXOPIzQIhAJLzuceaSx0VZMdNkbh3POpcxLZrGt%2FSvnKCnUOTTKjuKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYOYBaKo%2BwA%2BXp1tMq3AMXHkXP%2FTpsXU7SPinagZj%2FasUjdFTFui%2F6UhPznpYW74lFqqn%2FoOMw%2BTtq%2BDK7hKkNbvROfPDDsH7sqyPZAwh%2Fqtb%2F%2FI2IDD40OgGjGLoWyJyIaWGHoFj8lpm7nEMU6mjenfPg54P2eQ9TP9GKOVH7hdrSQ38QdyTlPGdVHdrmD068DavFkYgB92zPg%2F42BRw5S2J1u%2BpSzet%2Bbq9xh0z9SSZCM%2BXKgF3mr252KgtABKc73uleMFKSG7SDqloebqO3Weoq6O4ZFzbjb185g5mIxXlFQD7J%2BgTLoBWjITt%2Be%2B%2BRwEhwGNLuXh0bRh9TMs7DB4YOgmtu9ioFgN9oDHOrsyZce7rYzo2Lhm%2BQcLcqo%2FoIyju5yZ%2FdNBdsPX7GtcQiTw9otI2SfWQ5%2BQM4whprdm4j1%2BU%2B8JRAv2c2OqstFaR%2FMF3CEtm3k%2Fo5%2BsCKkJ6Hotq4IWYBrBmsIAx8AJEr%2BYsSOs0UEAVuojU%2BgFbjlrhkY1FeAgmo0Mm5NsDjYvAazQB%2FaLhDfhtiEdcD%2F87h6e7%2FAaPEpyTAtgd1GzMf9w8S5Y7aUeQX1m2AFoCy%2BNrTvArBBqRXn6ZeAAFFl%2B31mqCchwE9jZFXbRBzvI93YSyQd7kpYS9ZTsXYSDDxzsXIBjqkAR4jFdnJzqg0vmtXu8h4hX%2FIFgiQV7DO8iTl09F8kCaukhhEfxt55WCCvE8Jx66PtpL1PkqXbxrobc6xDDdLXQXKXxRpUJHMJSlNArnmxugTOZPk3Rvvt1gT2UATzG6eh7GKZVYbXkvwF%2Ft7fCzBHqsegcqB5%2BTilc7YaDx1C6OORg9d30zx9Q6o10d4TDC5y8aI%2BUdzISLsDA9yY6%2Fuh3MkNS8a&X-Amz-Signature=ae848125c5d7e8e2edcf324e73349b3835ef411acc5e1b814e2e05e5677f28af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q5YUE6E%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T062546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJIMEYCIQCbeKqiQ%2Fgwic6wnmYIPXpMZ129X5Lb3wJKWAxNXOPIzQIhAJLzuceaSx0VZMdNkbh3POpcxLZrGt%2FSvnKCnUOTTKjuKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYOYBaKo%2BwA%2BXp1tMq3AMXHkXP%2FTpsXU7SPinagZj%2FasUjdFTFui%2F6UhPznpYW74lFqqn%2FoOMw%2BTtq%2BDK7hKkNbvROfPDDsH7sqyPZAwh%2Fqtb%2F%2FI2IDD40OgGjGLoWyJyIaWGHoFj8lpm7nEMU6mjenfPg54P2eQ9TP9GKOVH7hdrSQ38QdyTlPGdVHdrmD068DavFkYgB92zPg%2F42BRw5S2J1u%2BpSzet%2Bbq9xh0z9SSZCM%2BXKgF3mr252KgtABKc73uleMFKSG7SDqloebqO3Weoq6O4ZFzbjb185g5mIxXlFQD7J%2BgTLoBWjITt%2Be%2B%2BRwEhwGNLuXh0bRh9TMs7DB4YOgmtu9ioFgN9oDHOrsyZce7rYzo2Lhm%2BQcLcqo%2FoIyju5yZ%2FdNBdsPX7GtcQiTw9otI2SfWQ5%2BQM4whprdm4j1%2BU%2B8JRAv2c2OqstFaR%2FMF3CEtm3k%2Fo5%2BsCKkJ6Hotq4IWYBrBmsIAx8AJEr%2BYsSOs0UEAVuojU%2BgFbjlrhkY1FeAgmo0Mm5NsDjYvAazQB%2FaLhDfhtiEdcD%2F87h6e7%2FAaPEpyTAtgd1GzMf9w8S5Y7aUeQX1m2AFoCy%2BNrTvArBBqRXn6ZeAAFFl%2B31mqCchwE9jZFXbRBzvI93YSyQd7kpYS9ZTsXYSDDxzsXIBjqkAR4jFdnJzqg0vmtXu8h4hX%2FIFgiQV7DO8iTl09F8kCaukhhEfxt55WCCvE8Jx66PtpL1PkqXbxrobc6xDDdLXQXKXxRpUJHMJSlNArnmxugTOZPk3Rvvt1gT2UATzG6eh7GKZVYbXkvwF%2Ft7fCzBHqsegcqB5%2BTilc7YaDx1C6OORg9d30zx9Q6o10d4TDC5y8aI%2BUdzISLsDA9yY6%2Fuh3MkNS8a&X-Amz-Signature=626a48ff96f9fa2012f0bab0f10d117ceefadf03b021bc21e567f7d7594081d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







