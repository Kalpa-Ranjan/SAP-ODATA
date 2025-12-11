



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDK4TVWK%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T062650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQD%2BrllLVbw3vpos%2BPG%2FgTtHXvP3LQAhiWQRU2IWZlE5IgIhALB%2BQ8E5HGz%2FefXeJWeTHq5t3HpDl%2FL4JDYS27ZjuuKRKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrGqsPbto7B9Htdskq3AMVtEjTTV%2BTh%2BQl2IgyTwuZRskLeD9EoQAZqYRj61wPPyeCmzpTCxpofNpGRY0l4DXXGqmenlTAAwkF%2BG%2FxLk6%2FYA%2F7muXHEqkze1fLYTOdORQijZYumc4oz6URSBx2KY1CcMioQT%2BapO5svQN3dVZI0%2BwylUKMnmdnjHSWrMQXrPqJhXsSJ6gQLCEvXrrCmbcK%2FPAHfE6z7G6bbkuZlXjy7jfBPUBCrA93XxZMaGuZNI4SR6ni6Ft0iXD9dfqSM0SugMG5bKoYiCJucrrLCMjbbtLBR6O5%2BfmhFUlDa8I2DnGo66ZGEx9ekjQgAywUzdZ2MGCu2NGL24ckBmL0QbCJmUZad%2F%2FV1qql91qNKvY0WpSrJr5tKllkqT9no3zWvCpT4TboubP0VBWYJgLwsQtPLuC4MhbjVZdbcwNnzj5dfUf%2FhtFXqSxg%2BPrzHmJz%2FKEnjgJzPBAg5nCni45p7Vnkwg8a9s66Khyf3%2BE07058kEdONGipP6NWXy0KHw0rgMS4BOwYFj3BGZMUml%2BJOMptPgMXTQMSQhJ5W3OF7KowqkwDuwAGqNYfWjX2RfOUCmBHgNsQDAnPt8FU1TdFfrlm33%2FkjmZKV1uzw%2BeK1WSpHHDBnXAX9s5qWAVtajCyxOnJBjqkAbMICWDLPYHAQXqsKGj6dmF47vMn%2BV5UXDNQnJ%2BUAmPsw6bdJWsTMDA3HZyg0N%2F9dxB27EDG3QtPV0icopuvMGr2ApS%2FWFU9%2BL1DCG6TZGDpZ%2BdbetaMcywFAn8MonNJK%2FNa3yEyy8Wj2keBg2M7E4YnAcMwphfBD44p6bWh6ZwQVxxSI7FwdEkFSBwZ89Zq0rXWnjuWewSNhkzYLHqYYm7Ce3Kx&X-Amz-Signature=3c4ccfcf99bd3a0ff259900058312953cf269be19c9c0624ca4d2e0bbdff4b8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDK4TVWK%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T062650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQD%2BrllLVbw3vpos%2BPG%2FgTtHXvP3LQAhiWQRU2IWZlE5IgIhALB%2BQ8E5HGz%2FefXeJWeTHq5t3HpDl%2FL4JDYS27ZjuuKRKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrGqsPbto7B9Htdskq3AMVtEjTTV%2BTh%2BQl2IgyTwuZRskLeD9EoQAZqYRj61wPPyeCmzpTCxpofNpGRY0l4DXXGqmenlTAAwkF%2BG%2FxLk6%2FYA%2F7muXHEqkze1fLYTOdORQijZYumc4oz6URSBx2KY1CcMioQT%2BapO5svQN3dVZI0%2BwylUKMnmdnjHSWrMQXrPqJhXsSJ6gQLCEvXrrCmbcK%2FPAHfE6z7G6bbkuZlXjy7jfBPUBCrA93XxZMaGuZNI4SR6ni6Ft0iXD9dfqSM0SugMG5bKoYiCJucrrLCMjbbtLBR6O5%2BfmhFUlDa8I2DnGo66ZGEx9ekjQgAywUzdZ2MGCu2NGL24ckBmL0QbCJmUZad%2F%2FV1qql91qNKvY0WpSrJr5tKllkqT9no3zWvCpT4TboubP0VBWYJgLwsQtPLuC4MhbjVZdbcwNnzj5dfUf%2FhtFXqSxg%2BPrzHmJz%2FKEnjgJzPBAg5nCni45p7Vnkwg8a9s66Khyf3%2BE07058kEdONGipP6NWXy0KHw0rgMS4BOwYFj3BGZMUml%2BJOMptPgMXTQMSQhJ5W3OF7KowqkwDuwAGqNYfWjX2RfOUCmBHgNsQDAnPt8FU1TdFfrlm33%2FkjmZKV1uzw%2BeK1WSpHHDBnXAX9s5qWAVtajCyxOnJBjqkAbMICWDLPYHAQXqsKGj6dmF47vMn%2BV5UXDNQnJ%2BUAmPsw6bdJWsTMDA3HZyg0N%2F9dxB27EDG3QtPV0icopuvMGr2ApS%2FWFU9%2BL1DCG6TZGDpZ%2BdbetaMcywFAn8MonNJK%2FNa3yEyy8Wj2keBg2M7E4YnAcMwphfBD44p6bWh6ZwQVxxSI7FwdEkFSBwZ89Zq0rXWnjuWewSNhkzYLHqYYm7Ce3Kx&X-Amz-Signature=b2df271ead810e9592b9e5a34eee3ba85e86468d5203be99c429bfd088066a77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







