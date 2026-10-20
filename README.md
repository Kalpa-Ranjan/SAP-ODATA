



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYUGLTWM%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T180913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEt6GUl6hN8ZpgsQZfB9acYHywk%2FH%2BzW%2Bpyq1CmelntdAiEA9nUs04HMYHW1Fw9UYrQdZ6ZelNeIpD7oZ%2FP58fyHUg8q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDI8WStv%2FHp%2FgJdFCWyrcA%2F1yEsDm1UFdt0J8bgcjEWu1pTof9zOr32AuFygi0zCCLR7Znmn2I2WQCj29mAr14%2BUbrkW8MUH62Ffz%2FAebG8Y8y33hCdEkOTPW9m9rxi%2B4dXWkO5MDchPKCS9RYGDYefgUhVUFCC1%2BHu3KKB%2Fyx%2Bah6%2FTYaEeV2c7e8DlQlpYIxKcoEebYLtsBcl6Seir7hrp037OJ3asuEyQXb25uiEivU0HtWnbtS80gdyo1CCa2vv0cqqAUM5ip%2Fs1DIKEnKelYz4ZowtWFuI2CPKHAe58hkNgRnHv9KmnAjaFJQEgkoVQ9yBrfBwAGDXLoROSExLguQO%2BlhZQGzPuv88yRopM0mNxBU19rcSMclr0Myi8%2FXD%2BI1TqpTgl4fYz7LmS%2FwYXxEWi8daV02CeEdTPy%2BRGEsK0OWB5d3bMFjjioGcYkElvVGrnAzIMZGQxu7RQ3UGdUFHv5AUVSH3gLTX1Mp4No46EFBMFDv%2F9oSoQubWVk9uWOClboLmQHyyQWYosk18wQ3k0wplmEkTw%2Bc8JwL9aE3BVdLOOzMa5AVoAJbYu%2FIzYEWCQylrCtHIatABQkcd7xpsf2VmJtSjBGJzSXtapi6StlBq0NQHDqWRRWK34R2VGZ768%2BZFV2ZJtuMLOw3tYGOqUBhpkNO4wH%2BO3z1PVW%2BSEJQ87VVZ2bAvEA%2BCZkPNODCdt06HJTxen7uNoI14RF3%2BoU%2B5XAkNwWH%2Bl%2F1t6eWMZwwlDyk02vUxBmjDuqEL8BxeM328yFo6AyI19YHo9Byi3uI5DBAGSYp3983HN0ZrUIBKCfRjQqVt8qzJnjwjLXjpNPOChyK84hn3q8UR8lXtx9dgKbIJNHeo%2B%2B2n3JjksUEw72wMnC&X-Amz-Signature=4ce5546bfda09458a2d6ca4959c1c1229e2d73d91d6017675fe83b31e57fb4f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYUGLTWM%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T180913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEt6GUl6hN8ZpgsQZfB9acYHywk%2FH%2BzW%2Bpyq1CmelntdAiEA9nUs04HMYHW1Fw9UYrQdZ6ZelNeIpD7oZ%2FP58fyHUg8q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDI8WStv%2FHp%2FgJdFCWyrcA%2F1yEsDm1UFdt0J8bgcjEWu1pTof9zOr32AuFygi0zCCLR7Znmn2I2WQCj29mAr14%2BUbrkW8MUH62Ffz%2FAebG8Y8y33hCdEkOTPW9m9rxi%2B4dXWkO5MDchPKCS9RYGDYefgUhVUFCC1%2BHu3KKB%2Fyx%2Bah6%2FTYaEeV2c7e8DlQlpYIxKcoEebYLtsBcl6Seir7hrp037OJ3asuEyQXb25uiEivU0HtWnbtS80gdyo1CCa2vv0cqqAUM5ip%2Fs1DIKEnKelYz4ZowtWFuI2CPKHAe58hkNgRnHv9KmnAjaFJQEgkoVQ9yBrfBwAGDXLoROSExLguQO%2BlhZQGzPuv88yRopM0mNxBU19rcSMclr0Myi8%2FXD%2BI1TqpTgl4fYz7LmS%2FwYXxEWi8daV02CeEdTPy%2BRGEsK0OWB5d3bMFjjioGcYkElvVGrnAzIMZGQxu7RQ3UGdUFHv5AUVSH3gLTX1Mp4No46EFBMFDv%2F9oSoQubWVk9uWOClboLmQHyyQWYosk18wQ3k0wplmEkTw%2Bc8JwL9aE3BVdLOOzMa5AVoAJbYu%2FIzYEWCQylrCtHIatABQkcd7xpsf2VmJtSjBGJzSXtapi6StlBq0NQHDqWRRWK34R2VGZ768%2BZFV2ZJtuMLOw3tYGOqUBhpkNO4wH%2BO3z1PVW%2BSEJQ87VVZ2bAvEA%2BCZkPNODCdt06HJTxen7uNoI14RF3%2BoU%2B5XAkNwWH%2Bl%2F1t6eWMZwwlDyk02vUxBmjDuqEL8BxeM328yFo6AyI19YHo9Byi3uI5DBAGSYp3983HN0ZrUIBKCfRjQqVt8qzJnjwjLXjpNPOChyK84hn3q8UR8lXtx9dgKbIJNHeo%2B%2B2n3JjksUEw72wMnC&X-Amz-Signature=7275e7d823374081ce966462072a0d11fab13d4990163b00c0dc49a38dcfb857&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







