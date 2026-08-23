



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RINUE3N2%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T063101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFZDO56%2F16H1zoKVbI%2By5Ya1wrHM6fwgQ3SYAEeAhKr8AiBltjKYroTrczhg%2FREmAEeIw9lISzWhJ8vgRbWuQbd9oSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGs3jF4nJhgxwDFY4KtwDiXRgeprFk%2F%2BU%2FVEG4oPZ%2BRwxn0n87U2IXYu4ZDGSVSkXUKwafDFQOza8%2Fmt1hhI1LoDIxH5VTkk4IY2tfAv056N8WzOI%2F33dakyObE4Zfsb3Yqflf7P%2BRA947vb3dXfLVCPjlIb5wOup0OBjiJI2gLlWTHncem9wuaVA03dhBVqrD9rrIMTKG1TCewb6Oe1mOkvtoUb3lNJZ3yE5dsOGSM8rKgQR5p1%2BT7HcI%2BVo8t%2BFSIjsXUCu1Q7b9SYcG8w9feOSje6t%2B50ia24Z4phgpYgdAJfM9V7mljw%2B%2BeD6PFE04eWD%2FhbP5b276MX4Cm1jB5RqoUKqrjeszWSlHEwylwb8w40HRyazeOs1PqhCEFVa6nwbO70xgmHcAyRLDo%2BwV7Kf82Mv%2Byt%2F211FCg2cZ4uqOi%2BqkJfDBxjTUlXkXRRbESTkbr1d9NZGI3uM011ojpUlCQmoOhuLwTVCB9G52LRtfIBGwIcP4KI%2FCpS3q52AcbJiXyX5v3ZqmlNG1Diu7bJgDp%2FuPS%2BsrDb6Jw5aS3E55JMgkF7dJqox93byL%2BEy19YwzQ6d5E%2BRfT4lZSqsGh%2Fp1TaJDormj%2FXHSTv%2B%2FXJlJyF2%2FshKSE%2BHNZcrxTmEERwHLadVNcV6yO8wxrWp1AY6pgHcvWJkoU%2FFrw38ouN3S7D%2F1uzh2O%2BIsvYW97CS0cBRI8IvUt4F9EMrwRwSOKgijqJnE0x69IrRZRJp10xHoywHwo05Czgxeb3fyaQXDP7%2FAZo6T6EaATTcqqrfZlDQT5Z4U41KEpFJ3gdSyJDYhTrv6wGdgOSLAW8bU9XpMZtLkSCRoS%2Fjj3SQEpRK4b%2B28dnuMiXdZVLq%2FrDCJSGoNG%2Bi%2BkxOQhEg&X-Amz-Signature=648db4d9643ec9596799708826cc68fe899f26836c6e119931f48d88709668ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RINUE3N2%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T063101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFZDO56%2F16H1zoKVbI%2By5Ya1wrHM6fwgQ3SYAEeAhKr8AiBltjKYroTrczhg%2FREmAEeIw9lISzWhJ8vgRbWuQbd9oSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGs3jF4nJhgxwDFY4KtwDiXRgeprFk%2F%2BU%2FVEG4oPZ%2BRwxn0n87U2IXYu4ZDGSVSkXUKwafDFQOza8%2Fmt1hhI1LoDIxH5VTkk4IY2tfAv056N8WzOI%2F33dakyObE4Zfsb3Yqflf7P%2BRA947vb3dXfLVCPjlIb5wOup0OBjiJI2gLlWTHncem9wuaVA03dhBVqrD9rrIMTKG1TCewb6Oe1mOkvtoUb3lNJZ3yE5dsOGSM8rKgQR5p1%2BT7HcI%2BVo8t%2BFSIjsXUCu1Q7b9SYcG8w9feOSje6t%2B50ia24Z4phgpYgdAJfM9V7mljw%2B%2BeD6PFE04eWD%2FhbP5b276MX4Cm1jB5RqoUKqrjeszWSlHEwylwb8w40HRyazeOs1PqhCEFVa6nwbO70xgmHcAyRLDo%2BwV7Kf82Mv%2Byt%2F211FCg2cZ4uqOi%2BqkJfDBxjTUlXkXRRbESTkbr1d9NZGI3uM011ojpUlCQmoOhuLwTVCB9G52LRtfIBGwIcP4KI%2FCpS3q52AcbJiXyX5v3ZqmlNG1Diu7bJgDp%2FuPS%2BsrDb6Jw5aS3E55JMgkF7dJqox93byL%2BEy19YwzQ6d5E%2BRfT4lZSqsGh%2Fp1TaJDormj%2FXHSTv%2B%2FXJlJyF2%2FshKSE%2BHNZcrxTmEERwHLadVNcV6yO8wxrWp1AY6pgHcvWJkoU%2FFrw38ouN3S7D%2F1uzh2O%2BIsvYW97CS0cBRI8IvUt4F9EMrwRwSOKgijqJnE0x69IrRZRJp10xHoywHwo05Czgxeb3fyaQXDP7%2FAZo6T6EaATTcqqrfZlDQT5Z4U41KEpFJ3gdSyJDYhTrv6wGdgOSLAW8bU9XpMZtLkSCRoS%2Fjj3SQEpRK4b%2B28dnuMiXdZVLq%2FrDCJSGoNG%2Bi%2BkxOQhEg&X-Amz-Signature=ad82fad270956e469cfe04c13f3750597ba16dce7ed0674e908d135bc297e5e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







