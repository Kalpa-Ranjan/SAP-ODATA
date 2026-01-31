



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZNXBSO%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T123657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7iuWn%2B%2B1ktuG8TanUEAgOfXPzCdnkiooVgdrlbnuIyAIhAOB09L9Cc0xjA%2B%2FklOPQ4jiADS%2B5FBlJFGkWmb%2FN0p1tKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpnLt7hItpQeMB23oq3AMmWUn4bKQ%2B89mQQqbtr%2BG8gTb7mS151%2FvXMi%2FPsS6TMePJ218eZ%2BDP43PAOZl6hogSt6eMJ1K13AETcvAMg4ObBM38NFTS7TfqbR79uxcdGO5%2B7OUz%2FJQalsYHzZ%2BUuZAEVmcCpwroNatOZV%2FR9AKCPbGPlBR8beWJ3xawsvtEk7U1h26rCe6aaqRhHjplfjhKlMgppHOo1mbzE8WFLJ187P%2BNEAbk1MQlyod4ayY7L5cFXILVo0M0UyBr1PGvXlTe4HboV8mw8nPhP2o87bxKYJfVSrr6Wk1WPuWUreCJoReK5wDmBpeHJYN%2Fd%2BERN6uppHlSHMvCtN2Zfjg1hlN6M%2FhyeNM69PIq%2BhBi93piJsRSf701UM8FOeMdm5l3TkBON2l7ZRJBnTiII9nPs0TUYswCUlPR7cuwL7qIzHxsjAc9Z35AnJ%2BEzV0%2FCsq7RKd%2BNcAr1bownVGBTTk6peGojnzj6jDVbCiabZkHmUZA2YmBubvnBXPyy3tZZSFZXySUYkenXl5K%2FDr4GZDwxmykAn%2Fg9OYix4SlZFsn2OhVFA0wZ7aq8dAO6bGnApUUAZOSTQl%2FoJNul6Vdn9RT1hnpkYdAbrXdB2TQOvPiJIyG2ejKzlzcztsPJ8qhBzDKvffLBjqkAZfrVVFMFq%2Buk8sxUQGAPbMMMTrosyw8I%2BrQVt47dm3Rh329jR2c0mUZjTXEVIh9vgIDszef%2BYpzY5K2sxfo7k5Al5VjBedZK%2FEiXG6iA0T9jm4rK3OPpUgF0UusA9ENvhNqWB7f9AlulOapmFrSCIXWeHy%2BoehKMR9W%2Bjdh86wV2%2FhGcSp2oedumXgjsevjpzKIwzkxdHZqHnL3jI2d%2F3NItTyH&X-Amz-Signature=8fb095b9ffa4f5cd4ee15c88130b02e87c8459a8f8cb35fccfe919593e9d81e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZNXBSO%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T123657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7iuWn%2B%2B1ktuG8TanUEAgOfXPzCdnkiooVgdrlbnuIyAIhAOB09L9Cc0xjA%2B%2FklOPQ4jiADS%2B5FBlJFGkWmb%2FN0p1tKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpnLt7hItpQeMB23oq3AMmWUn4bKQ%2B89mQQqbtr%2BG8gTb7mS151%2FvXMi%2FPsS6TMePJ218eZ%2BDP43PAOZl6hogSt6eMJ1K13AETcvAMg4ObBM38NFTS7TfqbR79uxcdGO5%2B7OUz%2FJQalsYHzZ%2BUuZAEVmcCpwroNatOZV%2FR9AKCPbGPlBR8beWJ3xawsvtEk7U1h26rCe6aaqRhHjplfjhKlMgppHOo1mbzE8WFLJ187P%2BNEAbk1MQlyod4ayY7L5cFXILVo0M0UyBr1PGvXlTe4HboV8mw8nPhP2o87bxKYJfVSrr6Wk1WPuWUreCJoReK5wDmBpeHJYN%2Fd%2BERN6uppHlSHMvCtN2Zfjg1hlN6M%2FhyeNM69PIq%2BhBi93piJsRSf701UM8FOeMdm5l3TkBON2l7ZRJBnTiII9nPs0TUYswCUlPR7cuwL7qIzHxsjAc9Z35AnJ%2BEzV0%2FCsq7RKd%2BNcAr1bownVGBTTk6peGojnzj6jDVbCiabZkHmUZA2YmBubvnBXPyy3tZZSFZXySUYkenXl5K%2FDr4GZDwxmykAn%2Fg9OYix4SlZFsn2OhVFA0wZ7aq8dAO6bGnApUUAZOSTQl%2FoJNul6Vdn9RT1hnpkYdAbrXdB2TQOvPiJIyG2ejKzlzcztsPJ8qhBzDKvffLBjqkAZfrVVFMFq%2Buk8sxUQGAPbMMMTrosyw8I%2BrQVt47dm3Rh329jR2c0mUZjTXEVIh9vgIDszef%2BYpzY5K2sxfo7k5Al5VjBedZK%2FEiXG6iA0T9jm4rK3OPpUgF0UusA9ENvhNqWB7f9AlulOapmFrSCIXWeHy%2BoehKMR9W%2Bjdh86wV2%2FhGcSp2oedumXgjsevjpzKIwzkxdHZqHnL3jI2d%2F3NItTyH&X-Amz-Signature=086f4bf762106b7b3adbcaf1a653d61f9a168a1ef85a156ace9c1556a54f499f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







