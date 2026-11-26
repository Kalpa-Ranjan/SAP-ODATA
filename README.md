



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2M6ZR2U%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T060825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9bMsXiVvaU9FHQ3ZcqPEvC%2BnhYeqIySU4GyVjhnHzMAiEA8FurtUWMSl7O4fBLMAH2QV04D%2BGfjC%2B%2FhZKIdpOworYqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMch0s1C1QXRV%2BCnRCrcAzCQcPq4Ju5HG1sAGoKZtHPw9rAuhEkJyGXMBxHHC8xkoOQdlpYcqw7BdxCgg09TCsAZs0orOtUxBHiW66YNqUP3qHX5mx8cqBNsLmmwcT2fe6E1TOLPcF2NlXefbRXP1zkgmlJELf0vGL%2Bk5EG2%2B6k0JH1xmecL1M%2FYsRbXjcw9qqErvJuDO1zlwOXwpqgWYSCqXEj4jJVShspz%2F9ks5TF45L00zUxIoFVhqh5azRV8JF7ivn1Me9uH6ccKdyvFCpVf6hk%2FGPHq8dSchvpg9bJcVRZ5OUaqvio9ylpnJj0X0iPiXG836gTokW02PXEcBzjYr0e8N9MEiwo73xw7t8ZHBhUkgrGMG%2FiHOAWfKTng%2Fx3Yhvms41ZosZTrAn8uKxCkX2o%2BuKu0S%2Fx1LzOth7ZcKmXD1BFhTDzcYo7OnO4Zc9J3Lkh0%2BXMgmuA2k9Sb43BSRahNw31pQRQB53taXwrZ5iTwAS7V7wYKbK90Ii3SX3chZrxAP0wHheEVrSwnDt244XnIHNePTei5RoCeOi1nTdp%2FJXTLhUcOwW%2FWrLB%2F6Q6GQzpPV6JCczyMvkUDEIRtwsrO7b25hLrVyK9qLAtB%2Ba6XP38CakDNTStJIwjZta%2Bi4bPj29p1JdKvMOfwntgGOqUBf8kkwTzCxDcmQztKLJglCHK%2BArIdd%2B69jb%2ByJ3rlOHndS8uINZddukKmo3blJFU4oWej37SJ9j%2BggSxUI%2BrJNIbinEkG%2BuIFZzz4Sq9OKIKcpKgvMCWksqjYmRaSM5GdSSkRsU9OteIX878%2FNJbgEos%2F8oBmJggANA8tkMxTaFvrRhXEBdmpPe%2F1aZuNw8SDwxDvpC9BB8Y4xDeTmCZnTkPBasJQ&X-Amz-Signature=67a8936ad88de5dade3f3ae47aaa3ca0d24115ac6c0cc2863953b602d6edf650&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2M6ZR2U%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T060825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9bMsXiVvaU9FHQ3ZcqPEvC%2BnhYeqIySU4GyVjhnHzMAiEA8FurtUWMSl7O4fBLMAH2QV04D%2BGfjC%2B%2FhZKIdpOworYqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMch0s1C1QXRV%2BCnRCrcAzCQcPq4Ju5HG1sAGoKZtHPw9rAuhEkJyGXMBxHHC8xkoOQdlpYcqw7BdxCgg09TCsAZs0orOtUxBHiW66YNqUP3qHX5mx8cqBNsLmmwcT2fe6E1TOLPcF2NlXefbRXP1zkgmlJELf0vGL%2Bk5EG2%2B6k0JH1xmecL1M%2FYsRbXjcw9qqErvJuDO1zlwOXwpqgWYSCqXEj4jJVShspz%2F9ks5TF45L00zUxIoFVhqh5azRV8JF7ivn1Me9uH6ccKdyvFCpVf6hk%2FGPHq8dSchvpg9bJcVRZ5OUaqvio9ylpnJj0X0iPiXG836gTokW02PXEcBzjYr0e8N9MEiwo73xw7t8ZHBhUkgrGMG%2FiHOAWfKTng%2Fx3Yhvms41ZosZTrAn8uKxCkX2o%2BuKu0S%2Fx1LzOth7ZcKmXD1BFhTDzcYo7OnO4Zc9J3Lkh0%2BXMgmuA2k9Sb43BSRahNw31pQRQB53taXwrZ5iTwAS7V7wYKbK90Ii3SX3chZrxAP0wHheEVrSwnDt244XnIHNePTei5RoCeOi1nTdp%2FJXTLhUcOwW%2FWrLB%2F6Q6GQzpPV6JCczyMvkUDEIRtwsrO7b25hLrVyK9qLAtB%2Ba6XP38CakDNTStJIwjZta%2Bi4bPj29p1JdKvMOfwntgGOqUBf8kkwTzCxDcmQztKLJglCHK%2BArIdd%2B69jb%2ByJ3rlOHndS8uINZddukKmo3blJFU4oWej37SJ9j%2BggSxUI%2BrJNIbinEkG%2BuIFZzz4Sq9OKIKcpKgvMCWksqjYmRaSM5GdSSkRsU9OteIX878%2FNJbgEos%2F8oBmJggANA8tkMxTaFvrRhXEBdmpPe%2F1aZuNw8SDwxDvpC9BB8Y4xDeTmCZnTkPBasJQ&X-Amz-Signature=06536f1a9a6a03d70821ae742474bb2f078122a9f8dbf599317dac42bff3c97b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







