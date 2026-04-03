



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAR7UGF4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T125327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwJE1obNLngdGsCDa7yZVLHfS0CdvjDYgmwgW382vCOwIhAL8M1m35TbbGFfOUf7dbel17pA%2Fhnd24K4zqp02oKb6GKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw44z3ivHTIOIRJ4kcq3AMwh6JYOO9bN71m2UGrsFK0qpiZPpHICjbWInFjyykRteh9qZUT%2BcU52yatqSZwLIC6ZkX1dYcHO5BdMk9zDcjEytDoEvpD2xoY%2BDUyo5Dc%2FkpQhpVZ79u8VXWr%2B9KU2g5F9XiVz5rPFjw8nuK6BLQW1GFBI0dH%2FGFZEbAPLN3g3r3HF%2F9rbtTOIEwBzampQoK9CbsE3m%2BJ8rK1sniIGkViMvAnx16IiKLjgdoWfzgxzbozMNKxtsGCpwGwkcTWvFvw%2Bh5ebHHVLCfU6IinqkTQW16nAbHl9uoFnogrN5SaI2mDUBjPE8guF3hiHqr1mufNac7YZLybWR7zdATyHRH4sCiPHo32L4AWDDupZFppbVIn9PHY8VDP6V1boFL8kgrcBrfuSl%2FZA5Ascu9a9ZG3YpOOBi91l6482MVSWiEZhx3OwxapchRKm%2BrY9Q808kdMSnJzwKNESGMJmyj6Slb%2FmrELzL312Aj3x8IrzLcRE%2BZSNmBRvAbieDOtcxm%2BQYVeas4DgTlV4w%2FB8%2FcabXf5AJdRZKQKmJW%2F%2FD4TEYT6iV9aVl%2Bewx0pzJs2MFf2uKcNbcEktjRjWyvnUQ5yDqLOnY%2BllCXPuUp%2B%2FE3qiZtAHXecqI2Xz6D0mXNtaTDy4b7OBjqkAScgmtM7iZsGfRT3H8tl4AG0Z4AJLpBtiS1HvbMn4wIiQKsu3HmzeYaqfZ5ZnX%2BUTP78uA%2FQhsCmSUCymxUFUo9w26cTOMc1jmEcN%2FRKrTA%2FCbNetD6ehkqjnLnKzt8cQJuGxfmXe4J9gXgUAkfk3gTz909vXeO%2BQ3d7pcKwN4%2F6GMqhEEvWIOCHkJXIU3kdbJGMmIyuk8FS9S1m4ASwLANCyruN&X-Amz-Signature=fda0e2502099cccec0d96a7a26f466559689bb3426a4e8cbe58b83e0741da248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAR7UGF4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T125328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwJE1obNLngdGsCDa7yZVLHfS0CdvjDYgmwgW382vCOwIhAL8M1m35TbbGFfOUf7dbel17pA%2Fhnd24K4zqp02oKb6GKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw44z3ivHTIOIRJ4kcq3AMwh6JYOO9bN71m2UGrsFK0qpiZPpHICjbWInFjyykRteh9qZUT%2BcU52yatqSZwLIC6ZkX1dYcHO5BdMk9zDcjEytDoEvpD2xoY%2BDUyo5Dc%2FkpQhpVZ79u8VXWr%2B9KU2g5F9XiVz5rPFjw8nuK6BLQW1GFBI0dH%2FGFZEbAPLN3g3r3HF%2F9rbtTOIEwBzampQoK9CbsE3m%2BJ8rK1sniIGkViMvAnx16IiKLjgdoWfzgxzbozMNKxtsGCpwGwkcTWvFvw%2Bh5ebHHVLCfU6IinqkTQW16nAbHl9uoFnogrN5SaI2mDUBjPE8guF3hiHqr1mufNac7YZLybWR7zdATyHRH4sCiPHo32L4AWDDupZFppbVIn9PHY8VDP6V1boFL8kgrcBrfuSl%2FZA5Ascu9a9ZG3YpOOBi91l6482MVSWiEZhx3OwxapchRKm%2BrY9Q808kdMSnJzwKNESGMJmyj6Slb%2FmrELzL312Aj3x8IrzLcRE%2BZSNmBRvAbieDOtcxm%2BQYVeas4DgTlV4w%2FB8%2FcabXf5AJdRZKQKmJW%2F%2FD4TEYT6iV9aVl%2Bewx0pzJs2MFf2uKcNbcEktjRjWyvnUQ5yDqLOnY%2BllCXPuUp%2B%2FE3qiZtAHXecqI2Xz6D0mXNtaTDy4b7OBjqkAScgmtM7iZsGfRT3H8tl4AG0Z4AJLpBtiS1HvbMn4wIiQKsu3HmzeYaqfZ5ZnX%2BUTP78uA%2FQhsCmSUCymxUFUo9w26cTOMc1jmEcN%2FRKrTA%2FCbNetD6ehkqjnLnKzt8cQJuGxfmXe4J9gXgUAkfk3gTz909vXeO%2BQ3d7pcKwN4%2F6GMqhEEvWIOCHkJXIU3kdbJGMmIyuk8FS9S1m4ASwLANCyruN&X-Amz-Signature=c65192f2fdcdc16694ebd35741361aca49465b09857832b02a6b770a665d02c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







