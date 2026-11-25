



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBDY6PF5%2F20261125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261125T120731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv9FgVrBLPwsiuGkIvKkgKRr6kmsn%2B%2FewYTxe7BRDtHAIgK94OxCcYj%2Ff6M8Huz5a7igvaM%2FLp97%2BdfxzH%2Be0txOwqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeci0BQmsVQsZYiXCrcAybebFQqOPByYOR3EV8CRi8AsxAv9ScAqNKN0t5f3SWazonv1wfDZccQP5D9v7KTGAlZMraMq16ycbQxg5%2Fi9TbtLYA9AOhKEAgyHqiyW5Mk%2Byr2F3zpjheEda%2B6kGNatP9R8D17Z64eVwz75RuGkCd2Hrm2DdPyekS1nlZh558MaduCCJpSsowZ9POAwr48LhjLLL2CXHvd6q%2FG87xlYIXUvEFCski0QY5f8zlfjuT%2BO940DasWcotkMPSc%2Fm%2BXMhSk64uFGdXnnbVxDfgX95QLWdFqDmyI9Y8A2BCXit0yNav933IiJKcz%2FHXyZcpjejUenEksdLw%2FndXZ2%2BBrvQj1YzxWWQ1q2d89zv04YFELz%2BTl%2F4pkt6j2wBxa%2Bdrkd%2Ba%2BygCgW3J%2BXk9%2FAPn9bS8XsJQRtXTZ6xy6Qeushogl9SOqmiexEbJGqr%2BSgS%2F51nnwE7AbfXocNnceE%2Bmx7LJqo51ttBFj9lR8mOIBe7Ts4JVZLNBeNQWH4V9qoKgOcd2XMGRKLEWpCDdeGT64cX24pjD3jtztMFijurmFPYX8ZmHg3o2jVUF97gJ6Z5TiRqRzCWmYgTGE%2B7D6UAEQ75aQBOTZoQv4naq7ezMQN0fCq2nHI9x4ekBrdj76MJnWmtgGOqUB%2B3P3TctFqssSBy8wPl76v0jUViixnjJkfLmCimpb75knSqB9buuNxW42GAbJQzJNlc7qHySsLIVzlsuQOY6aMckHq0j%2BLZuLpozFKQfg%2Fl1wu9fe374hMWGO6qKn211Y61V%2Bc2plNj2wfrecZjNp9sxJhFsQhDpFlxkFtpnyyJJRPo5I4Ro5H6qvwTiMmsU%2FyUdKD%2FeGesXI2dxdZOD8StNk0wC9&X-Amz-Signature=82c6053b47d203ebf3b208ce70422599ea44d7ee338cfed9051c01a024c9eb64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBDY6PF5%2F20261125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261125T120732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCv9FgVrBLPwsiuGkIvKkgKRr6kmsn%2B%2FewYTxe7BRDtHAIgK94OxCcYj%2Ff6M8Huz5a7igvaM%2FLp97%2BdfxzH%2Be0txOwqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeci0BQmsVQsZYiXCrcAybebFQqOPByYOR3EV8CRi8AsxAv9ScAqNKN0t5f3SWazonv1wfDZccQP5D9v7KTGAlZMraMq16ycbQxg5%2Fi9TbtLYA9AOhKEAgyHqiyW5Mk%2Byr2F3zpjheEda%2B6kGNatP9R8D17Z64eVwz75RuGkCd2Hrm2DdPyekS1nlZh558MaduCCJpSsowZ9POAwr48LhjLLL2CXHvd6q%2FG87xlYIXUvEFCski0QY5f8zlfjuT%2BO940DasWcotkMPSc%2Fm%2BXMhSk64uFGdXnnbVxDfgX95QLWdFqDmyI9Y8A2BCXit0yNav933IiJKcz%2FHXyZcpjejUenEksdLw%2FndXZ2%2BBrvQj1YzxWWQ1q2d89zv04YFELz%2BTl%2F4pkt6j2wBxa%2Bdrkd%2Ba%2BygCgW3J%2BXk9%2FAPn9bS8XsJQRtXTZ6xy6Qeushogl9SOqmiexEbJGqr%2BSgS%2F51nnwE7AbfXocNnceE%2Bmx7LJqo51ttBFj9lR8mOIBe7Ts4JVZLNBeNQWH4V9qoKgOcd2XMGRKLEWpCDdeGT64cX24pjD3jtztMFijurmFPYX8ZmHg3o2jVUF97gJ6Z5TiRqRzCWmYgTGE%2B7D6UAEQ75aQBOTZoQv4naq7ezMQN0fCq2nHI9x4ekBrdj76MJnWmtgGOqUB%2B3P3TctFqssSBy8wPl76v0jUViixnjJkfLmCimpb75knSqB9buuNxW42GAbJQzJNlc7qHySsLIVzlsuQOY6aMckHq0j%2BLZuLpozFKQfg%2Fl1wu9fe374hMWGO6qKn211Y61V%2Bc2plNj2wfrecZjNp9sxJhFsQhDpFlxkFtpnyyJJRPo5I4Ro5H6qvwTiMmsU%2FyUdKD%2FeGesXI2dxdZOD8StNk0wC9&X-Amz-Signature=1d5caf5f222c2c588cf13171e9b5db020139a9d502171f8bb636832d2c9da085&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







