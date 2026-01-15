



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4GGROAU%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T011730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIHtDNh1yy7UvRBPoitzkG0gE7s7Vux%2BE0C0xKeW1iJNjAiBtriXGyZIzllHOnsVOa4p3GGpm5Qrdi5xzawvC5YaBNSr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMLt9Sz1f3dyKqHJjGKtwDKpKdmzr7Hgmfu8mepp6p0QySjphJTOg4Dq8U1IZIFn%2BHu1NexEucab9sN2D%2BcjfzLLjUIh0Wwf%2B5x9vQ4dAWrIRQ1S4bvQtHIt%2BK%2Feu2fB2xHFaXi7NHbfdEvfdMApgMDDhVEfKIQolB2BZ0xG7Kr5kWqj3UFsGp7oTqt3FR6JxKDQiclFEZmXu0WWUivIxS3%2BncNDpINpm62JaxDc4qgNY7r6X53qf7pHIq145p7qAj9wwJ2RGKVJT6%2FG3YrDRPGn4gHSRwPhoKwX4OiXgPNREXNlG4U5bTLh46Y0KhLBmOjgjClVHCoCtvY9KfKs%2BApBW9Iv0FtW3doLSN%2Bn9o393cTEyVvEzAsa7yQC2f4JGvfivR8KU6Ih5Znu4yNsHxmylpAuuyNI%2BODcUAZ947%2BeIgmqBfHcDP3JnU4nX7NXbM52cIwliw%2Br%2Fnt5H%2F3fzvLIGDqULZR5fTOlFFazK%2FbuoZ9oAmKNsj%2BcugG%2FE9Cy65SqS1fui3bPe54jDpzKkoWXgSQ7ejTwdHrarI38%2FTX3F4N%2FGPx09Ot7%2FT7mVfjwxozHHhF14V9sm%2BRfprPvBHLvJa38%2BGfOAm6Wy1AZba53u%2FIywpGWHsSnjfvzAeJzXO52kiTtnOORmWcpwwqOCgywY6pgGTYv2%2FTEazdQgpX85mZxPW2zWC77wI5vvplAJbcP%2B7rFAC2j8lgfJwpgDR1SSyQHPtiA1WFf6p185X%2FCrQmJlv6iHicEzHQR3AL6GAtQoUt8xeMWJi0wAHKdBJ%2BuecmR7YvgJnS8K6WLpOTOiTlWDT8VQnqy%2F6HZcf5sllusOBgzPELFTSCSvcC%2FDSL%2F2aNb1T0dCVXG1olVQzzjLjNY5U9OXytHw9&X-Amz-Signature=8c0ae209f235bd2f5e960d0c7588564406210b21b942eb4f72dca9712b31b5bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4GGROAU%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T011731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIHtDNh1yy7UvRBPoitzkG0gE7s7Vux%2BE0C0xKeW1iJNjAiBtriXGyZIzllHOnsVOa4p3GGpm5Qrdi5xzawvC5YaBNSr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMLt9Sz1f3dyKqHJjGKtwDKpKdmzr7Hgmfu8mepp6p0QySjphJTOg4Dq8U1IZIFn%2BHu1NexEucab9sN2D%2BcjfzLLjUIh0Wwf%2B5x9vQ4dAWrIRQ1S4bvQtHIt%2BK%2Feu2fB2xHFaXi7NHbfdEvfdMApgMDDhVEfKIQolB2BZ0xG7Kr5kWqj3UFsGp7oTqt3FR6JxKDQiclFEZmXu0WWUivIxS3%2BncNDpINpm62JaxDc4qgNY7r6X53qf7pHIq145p7qAj9wwJ2RGKVJT6%2FG3YrDRPGn4gHSRwPhoKwX4OiXgPNREXNlG4U5bTLh46Y0KhLBmOjgjClVHCoCtvY9KfKs%2BApBW9Iv0FtW3doLSN%2Bn9o393cTEyVvEzAsa7yQC2f4JGvfivR8KU6Ih5Znu4yNsHxmylpAuuyNI%2BODcUAZ947%2BeIgmqBfHcDP3JnU4nX7NXbM52cIwliw%2Br%2Fnt5H%2F3fzvLIGDqULZR5fTOlFFazK%2FbuoZ9oAmKNsj%2BcugG%2FE9Cy65SqS1fui3bPe54jDpzKkoWXgSQ7ejTwdHrarI38%2FTX3F4N%2FGPx09Ot7%2FT7mVfjwxozHHhF14V9sm%2BRfprPvBHLvJa38%2BGfOAm6Wy1AZba53u%2FIywpGWHsSnjfvzAeJzXO52kiTtnOORmWcpwwqOCgywY6pgGTYv2%2FTEazdQgpX85mZxPW2zWC77wI5vvplAJbcP%2B7rFAC2j8lgfJwpgDR1SSyQHPtiA1WFf6p185X%2FCrQmJlv6iHicEzHQR3AL6GAtQoUt8xeMWJi0wAHKdBJ%2BuecmR7YvgJnS8K6WLpOTOiTlWDT8VQnqy%2F6HZcf5sllusOBgzPELFTSCSvcC%2FDSL%2F2aNb1T0dCVXG1olVQzzjLjNY5U9OXytHw9&X-Amz-Signature=b5112bf38554f8ebdb8246394103b5b5178f74f0b5048b379d56a14a6544249e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







