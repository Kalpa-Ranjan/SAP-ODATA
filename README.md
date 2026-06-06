



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCBEE2ML%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T024110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGlNTYO8XzGmp46pixnusCs2B%2BXGtgj7XEKLX8s6bJReAiEApLaSeOheKhCW5ZSa5COHVlaryVX9VyNGE3H9%2FU%2Fjmfwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDD%2FWhVnoT8%2Fj5o%2B6LCrcA8IiWZFjJ%2Bag2ZyirhB%2B4LNWqqCa898buJpnCR2vW6NzLL6pUGzu1O39bHthG92TFKwli39%2FyqSDX0m9nMtIVuWxM11lXhN0uIcJ%2Bs3XkFsi%2By5ffgyzcFb5IL03CenNHV3mxuFMQxeiA%2BhpM9MWxINRs0MtLgm68MFe0S4xtsoXrQZmq1USmTy6F%2FWrNj4nUQZo8mYlND0XvZOpq9tkhOoVkDsjqkq44yQlr1C%2FTwIKgMwt5JANJoDovW0nf2GezfP2DGRBAfr%2F1BODa%2FvOkMhoi6xaKLD1%2Bdu29w03C5u4Pc3Ub2oOvZJF24a%2Fl5TI%2FqHKVuqmGMu60C3SzNoJbuujwH77dN7sFb72I6OkOaYizIDSDEX3S459whS0bYHmOIMKk7RnjflkBbXJ4BkLbZTiiC0kjy5jMBaz0zYkne1btZ8Zj7W%2Ftj9UhTf8%2BfII6HDpxvN5fy%2BO8%2B0ygLgsDCEfgZzhOsFlsk8jqtLLa4%2FhMFNfqmWOfkIth2NDsnTDWXGiT5Xvr8lJdOZFQABHAecwS5mZMvfj89WBeqkq90lGu9BV%2BS6%2Bbj5tkFGoKI4rdjbI2xp3bZbPG7ZSp%2FhmB4WXUCC5YAdc1QtpXUyuTCB62mWhLDQjpDdw%2Be7JMLrrjdEGOqUBtpvqdct87r2RqP28iaknkDTfd0Ju7IMJNcO2s7tAXt%2FSHzRuvc6h%2FQiL223nTQs7tyK%2BLrOlljUcj8kq5TbOD%2FC%2B8OguEa4GVYWCfV%2FxuWmp5zekmkJjXkloUK4NaTAjGMS1PJfQ%2B%2FmXor6WReLe3INy3zJzFpJ0e4xmEQ4q%2Be%2BdGVI0UpCTl8Ap2B8fppfEN2dvHWpY8RDbP4NuvmC1XcCWLQbo&X-Amz-Signature=274963213ec9363440b08dbec6ac528ae854a034350d8df193150731452f72b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCBEE2ML%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T024110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGlNTYO8XzGmp46pixnusCs2B%2BXGtgj7XEKLX8s6bJReAiEApLaSeOheKhCW5ZSa5COHVlaryVX9VyNGE3H9%2FU%2Fjmfwq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDD%2FWhVnoT8%2Fj5o%2B6LCrcA8IiWZFjJ%2Bag2ZyirhB%2B4LNWqqCa898buJpnCR2vW6NzLL6pUGzu1O39bHthG92TFKwli39%2FyqSDX0m9nMtIVuWxM11lXhN0uIcJ%2Bs3XkFsi%2By5ffgyzcFb5IL03CenNHV3mxuFMQxeiA%2BhpM9MWxINRs0MtLgm68MFe0S4xtsoXrQZmq1USmTy6F%2FWrNj4nUQZo8mYlND0XvZOpq9tkhOoVkDsjqkq44yQlr1C%2FTwIKgMwt5JANJoDovW0nf2GezfP2DGRBAfr%2F1BODa%2FvOkMhoi6xaKLD1%2Bdu29w03C5u4Pc3Ub2oOvZJF24a%2Fl5TI%2FqHKVuqmGMu60C3SzNoJbuujwH77dN7sFb72I6OkOaYizIDSDEX3S459whS0bYHmOIMKk7RnjflkBbXJ4BkLbZTiiC0kjy5jMBaz0zYkne1btZ8Zj7W%2Ftj9UhTf8%2BfII6HDpxvN5fy%2BO8%2B0ygLgsDCEfgZzhOsFlsk8jqtLLa4%2FhMFNfqmWOfkIth2NDsnTDWXGiT5Xvr8lJdOZFQABHAecwS5mZMvfj89WBeqkq90lGu9BV%2BS6%2Bbj5tkFGoKI4rdjbI2xp3bZbPG7ZSp%2FhmB4WXUCC5YAdc1QtpXUyuTCB62mWhLDQjpDdw%2Be7JMLrrjdEGOqUBtpvqdct87r2RqP28iaknkDTfd0Ju7IMJNcO2s7tAXt%2FSHzRuvc6h%2FQiL223nTQs7tyK%2BLrOlljUcj8kq5TbOD%2FC%2B8OguEa4GVYWCfV%2FxuWmp5zekmkJjXkloUK4NaTAjGMS1PJfQ%2B%2FmXor6WReLe3INy3zJzFpJ0e4xmEQ4q%2Be%2BdGVI0UpCTl8Ap2B8fppfEN2dvHWpY8RDbP4NuvmC1XcCWLQbo&X-Amz-Signature=e8d3b875eb9660bef5f4cef5a433a60c28e1eaeceec04b182940e35039564bef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







