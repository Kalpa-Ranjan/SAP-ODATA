



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF7USLIH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T191809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQDgbOAatXxdFVN9AXnS2zOLv10UwniuZKTJ9ICs%2BSgIQAIgf338IqXz3MzwGVIrbdypx%2B3h6XUbCjjgBP1cDFB%2FJt8q%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDFUYCNfPAN1g4FtW5SrcA23dyMpnFSQTxzrEzIrTqcfs6kFbeFa%2F1f79TUGYDg3xrAC649FXS0rspHNnJqkfXDmJRzE6T7bEhZjij2NDOULD6ZX2D%2Bn7EwVJ9%2FM4fhB1k%2BQGyxev7I8K2zglCvub4XurA6APRvqmjGx2jQA8nn3aBxwJQYHyX%2BO3nTnmUycZkRsDU6gxnFFA2PqDoXDKIJimpvXe9%2BfZDPxbzDUKSBAZs5dUU4miLLv1JX%2FGwqR0JoOBtLeqE%2B%2F3ODPw2e9Pd0JZ8U%2Fv5yuGR4IzfFsGk8b80dfYF5yOedlyh6pyVcc09yJU1WYabFMvWcWdvlWdY3vFaFfd%2BZffqskg4b77l%2BtsiKktG%2BXZGIZkNztlvtY2UYIISBHX0lb4D0ynYwpGTypJy4%2BBVTiswJza4AG56mbro4HttMZ8Joa6lwx7YXiIIv8xkCk0KT9tHPnEqMEi2DTg89%2BTKki%2BuVdsROg%2BsrZBvbEMgv9wvS0o%2BBDrwfimVZqC8hlKkTAZFcy%2F%2BPQsZ%2BjxvW57n0QlbRPA%2FMNSRDHpQlDbuobzjz4IFqCugwSiYatxLzOoskR0S3FbsXy9Y7M9FIu1zv9N%2BzbzVVas3CZQeLygfLajedfiCBYB7EtbK8BbjnyT8shFx96iMP7qutEGOqUBhj4plhbf%2FMeLhuKtfG3zP7%2BnVWLH5jfwiZnelY7%2FcT%2Bx8Sa18h4Pgx1ojBbexyWZqq73nw22Xsv50NhusmKQBKx0dCQ%2F0kzw4Nk4%2BRq6DsIqGhJ7dkvhguP%2FThPd0LieiYtCdPG53fdUFRymwqA%2Bwei8jJ7zg6fxZ9b%2FcuDX1h2RQiuMIFIB0BAKFeaCKAt73SSsomRmIdQILtvLD2vopLoKcczR&X-Amz-Signature=569a2ed8ecf73403443389fbd6fd01a7fd96ada94e77a04aee936ef48ef14036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF7USLIH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T191809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQDgbOAatXxdFVN9AXnS2zOLv10UwniuZKTJ9ICs%2BSgIQAIgf338IqXz3MzwGVIrbdypx%2B3h6XUbCjjgBP1cDFB%2FJt8q%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDFUYCNfPAN1g4FtW5SrcA23dyMpnFSQTxzrEzIrTqcfs6kFbeFa%2F1f79TUGYDg3xrAC649FXS0rspHNnJqkfXDmJRzE6T7bEhZjij2NDOULD6ZX2D%2Bn7EwVJ9%2FM4fhB1k%2BQGyxev7I8K2zglCvub4XurA6APRvqmjGx2jQA8nn3aBxwJQYHyX%2BO3nTnmUycZkRsDU6gxnFFA2PqDoXDKIJimpvXe9%2BfZDPxbzDUKSBAZs5dUU4miLLv1JX%2FGwqR0JoOBtLeqE%2B%2F3ODPw2e9Pd0JZ8U%2Fv5yuGR4IzfFsGk8b80dfYF5yOedlyh6pyVcc09yJU1WYabFMvWcWdvlWdY3vFaFfd%2BZffqskg4b77l%2BtsiKktG%2BXZGIZkNztlvtY2UYIISBHX0lb4D0ynYwpGTypJy4%2BBVTiswJza4AG56mbro4HttMZ8Joa6lwx7YXiIIv8xkCk0KT9tHPnEqMEi2DTg89%2BTKki%2BuVdsROg%2BsrZBvbEMgv9wvS0o%2BBDrwfimVZqC8hlKkTAZFcy%2F%2BPQsZ%2BjxvW57n0QlbRPA%2FMNSRDHpQlDbuobzjz4IFqCugwSiYatxLzOoskR0S3FbsXy9Y7M9FIu1zv9N%2BzbzVVas3CZQeLygfLajedfiCBYB7EtbK8BbjnyT8shFx96iMP7qutEGOqUBhj4plhbf%2FMeLhuKtfG3zP7%2BnVWLH5jfwiZnelY7%2FcT%2Bx8Sa18h4Pgx1ojBbexyWZqq73nw22Xsv50NhusmKQBKx0dCQ%2F0kzw4Nk4%2BRq6DsIqGhJ7dkvhguP%2FThPd0LieiYtCdPG53fdUFRymwqA%2Bwei8jJ7zg6fxZ9b%2FcuDX1h2RQiuMIFIB0BAKFeaCKAt73SSsomRmIdQILtvLD2vopLoKcczR&X-Amz-Signature=125f2c9cc83232bd445c5c106137e74929ade0dffef1336ba4b4c9dc100dddf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







