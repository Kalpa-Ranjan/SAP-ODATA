



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OO6RQ6S%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T143738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCICt7T%2F0ydSztMw7My0EwBnOjxnqnmn41rODGi9HIT8YgAiEAxujDYXoefGCxxFeUF7h8a9nQDdGrORqkUtyxvaw1J2sq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNx6o3PSM1%2F2JdQvJircA6eWLLm0O9uxWTBkicOo%2ByfDubgTGIBEAwiD97wSzRLj52b%2FN29nGT9ia9wHJzFNfxNEWQ6w7fFCZKt7voF7VgQ6GDIFooM7d45xXBOmqIOMMSWdpmeufdocmV4nkaX3c%2FKRypsBOXsFBDoEa6Cv8s93nVOrPkB85Lk65UWFvQ0Phfxg5j1CZO3mNyMoYbVjl7j5KfZrwr%2B5Qok56yTOuGQ%2Bqxo3yy3wXXekIdQpP9o0haS%2FaVs6%2B0Z%2FQlUBujDVFl1qjfV7ZpskwEWwf93DZKCYwHk7FTnwwAxbLAzJrIPQcJZO2fzPF3UyH30n%2B65yQmCkXmtd%2BaiBVLA0O0xKal6meXJ%2FvYF5TVsafUrCAsHk1lguOG6p%2BnHJ5zzy5kHdN5BA7FNpaB%2FnU%2B8a6LrV70Mma0kYZ3vbFzlpKdcncEyTWuRKoyZyCh3Gp4Sx1spfbJbjP2wXSl08QpfvV6sjsb69SAqKBSXUPI3FQpk0ckzike9ZaiwUg%2BAdbaMb01sfaAW98DgKhNlqinHqXQiBC30izFl5APumhMEHZ7r%2FgUnniCYihEADBPyCIAsobYSUFV5Vv9F2SPet2b71xVIBR45JYnt%2BF7ziD6OPGUIqlyPhhPZTxbzRcnVEhl6OMP6v6tEGOqUBRk1%2FnHIPStfgQyyEiGhnvdKqr1TzzT1JubZebqMcVMfrimXdr%2B%2BTVreFXOmlxM2GN0L6VW0Cm34YwAI%2BbOU92JoZzCnULLec4NUuwo7mxNtMpR7Ngb2QMcwLEiY6%2FgfDcB8Rdq%2FK2aRw4VIWN%2F7IoXKZkE7ct5iqaBue50%2FXLxgP6tYCOO2Iatik4nuLzUqx2wrsUvGY42YmcGK6ntEVCeUMOg9H&X-Amz-Signature=41fb01bfc4b5177ed30292a6502103b32e5d900cf3952b8460ee54c5341e71d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OO6RQ6S%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T143738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCICt7T%2F0ydSztMw7My0EwBnOjxnqnmn41rODGi9HIT8YgAiEAxujDYXoefGCxxFeUF7h8a9nQDdGrORqkUtyxvaw1J2sq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNx6o3PSM1%2F2JdQvJircA6eWLLm0O9uxWTBkicOo%2ByfDubgTGIBEAwiD97wSzRLj52b%2FN29nGT9ia9wHJzFNfxNEWQ6w7fFCZKt7voF7VgQ6GDIFooM7d45xXBOmqIOMMSWdpmeufdocmV4nkaX3c%2FKRypsBOXsFBDoEa6Cv8s93nVOrPkB85Lk65UWFvQ0Phfxg5j1CZO3mNyMoYbVjl7j5KfZrwr%2B5Qok56yTOuGQ%2Bqxo3yy3wXXekIdQpP9o0haS%2FaVs6%2B0Z%2FQlUBujDVFl1qjfV7ZpskwEWwf93DZKCYwHk7FTnwwAxbLAzJrIPQcJZO2fzPF3UyH30n%2B65yQmCkXmtd%2BaiBVLA0O0xKal6meXJ%2FvYF5TVsafUrCAsHk1lguOG6p%2BnHJ5zzy5kHdN5BA7FNpaB%2FnU%2B8a6LrV70Mma0kYZ3vbFzlpKdcncEyTWuRKoyZyCh3Gp4Sx1spfbJbjP2wXSl08QpfvV6sjsb69SAqKBSXUPI3FQpk0ckzike9ZaiwUg%2BAdbaMb01sfaAW98DgKhNlqinHqXQiBC30izFl5APumhMEHZ7r%2FgUnniCYihEADBPyCIAsobYSUFV5Vv9F2SPet2b71xVIBR45JYnt%2BF7ziD6OPGUIqlyPhhPZTxbzRcnVEhl6OMP6v6tEGOqUBRk1%2FnHIPStfgQyyEiGhnvdKqr1TzzT1JubZebqMcVMfrimXdr%2B%2BTVreFXOmlxM2GN0L6VW0Cm34YwAI%2BbOU92JoZzCnULLec4NUuwo7mxNtMpR7Ngb2QMcwLEiY6%2FgfDcB8Rdq%2FK2aRw4VIWN%2F7IoXKZkE7ct5iqaBue50%2FXLxgP6tYCOO2Iatik4nuLzUqx2wrsUvGY42YmcGK6ntEVCeUMOg9H&X-Amz-Signature=0d0051fc8277529826a20027135bf1de8d001d2261dfd2262316c7f717eba239&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







