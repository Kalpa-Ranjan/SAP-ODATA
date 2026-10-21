



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ7XQSQH%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T180947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7oY%2FNVnuhdXn9TjD9iZJjsQxB5wtLbtsCM5isu7C62AiAalRVjxv0lt%2FAs0r%2FlaLlClsEnGYGBRsBJ35LKd11tfir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMsCkhhKH5abOnVHe%2FKtwDXxQZQGqISzHS91KmSKGwwsJzB3YeRZxBeqFiG1XWRnJEHQVKSDxzPxUyJbZ%2Ba7xhRkeVLz3hT5rTSF%2BXHPZAa3kAHd%2FBuq6V9YFaeMy491kVC3Nw1SwhXFcYgbI905DOj2k5A1lgVg5naIllFM8iV%2FsS87Eq5fFSUJWk7XSsytbHPaFlZl7mRu4YEB77kWNeZtJwXplbmiKPasCmIVpnBmq8H%2BUCX8yBuXjORefBElZ2ETPJdT9FA%2FeSFz4PM6Pno0RSTsz24qdv9ObE1L77q6N%2F%2FF8JVsxRVWnoCoiMj25TLM3B3YHEvT5j2FnTygbM3vIq36tWo%2FmJe1yA9atSmjauuzkdNMHbMHtfczByYXT8QnObju%2FbwiIDvQu8vtcZBI7R41TzLd4d437q1pbvA3Jk9hAj0%2FWIrirw4CCKtE1A5qhxBB%2F2wfS9vQd4tDML%2Fh3azAcQafkRjtTdM6TY2SROtrj0Afvp8%2Bmuc79cRVlcEDb0PaHw6VW3Jt4g5Olc31YCJHd9rmUz1gSsVI6M4rg8A2%2FbP1dsjD3qJfKY0DlWr1nqwagCAVKeCp%2BAZUiWt5o6ZVTWDGwkG3feJ4CEMcsmeFHD%2F6fg%2FVDJiSsc8r1JxjXrXqc%2FJNbPl20w%2BuHj1gY6pgHAjjkZn5%2FKFsIjaktT0p0F%2BUpG8LAaVWW%2FZHZQyWoSLsqRDFi3Sia12PMCx5Nj4cvTuoG6BrYgOG3SiztQn4NjPY8KuLa16fpn8v9nhLPLRnNKfUrKUh5gFtwWuGV7Edz%2BEMe%2FeeJFZtFMnuPVbUxKqTR8xyGnOLdROlWngGvhgrB2ZzBy%2Bav2HrnRVM0U%2FoDZJBrlarv6gJeBxeyDkrf6vRfygwUm&X-Amz-Signature=228ed486ee74c0aa3571272ebca85994912da2e2a2e0138694fc958da9d596df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ7XQSQH%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T180947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7oY%2FNVnuhdXn9TjD9iZJjsQxB5wtLbtsCM5isu7C62AiAalRVjxv0lt%2FAs0r%2FlaLlClsEnGYGBRsBJ35LKd11tfir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMsCkhhKH5abOnVHe%2FKtwDXxQZQGqISzHS91KmSKGwwsJzB3YeRZxBeqFiG1XWRnJEHQVKSDxzPxUyJbZ%2Ba7xhRkeVLz3hT5rTSF%2BXHPZAa3kAHd%2FBuq6V9YFaeMy491kVC3Nw1SwhXFcYgbI905DOj2k5A1lgVg5naIllFM8iV%2FsS87Eq5fFSUJWk7XSsytbHPaFlZl7mRu4YEB77kWNeZtJwXplbmiKPasCmIVpnBmq8H%2BUCX8yBuXjORefBElZ2ETPJdT9FA%2FeSFz4PM6Pno0RSTsz24qdv9ObE1L77q6N%2F%2FF8JVsxRVWnoCoiMj25TLM3B3YHEvT5j2FnTygbM3vIq36tWo%2FmJe1yA9atSmjauuzkdNMHbMHtfczByYXT8QnObju%2FbwiIDvQu8vtcZBI7R41TzLd4d437q1pbvA3Jk9hAj0%2FWIrirw4CCKtE1A5qhxBB%2F2wfS9vQd4tDML%2Fh3azAcQafkRjtTdM6TY2SROtrj0Afvp8%2Bmuc79cRVlcEDb0PaHw6VW3Jt4g5Olc31YCJHd9rmUz1gSsVI6M4rg8A2%2FbP1dsjD3qJfKY0DlWr1nqwagCAVKeCp%2BAZUiWt5o6ZVTWDGwkG3feJ4CEMcsmeFHD%2F6fg%2FVDJiSsc8r1JxjXrXqc%2FJNbPl20w%2BuHj1gY6pgHAjjkZn5%2FKFsIjaktT0p0F%2BUpG8LAaVWW%2FZHZQyWoSLsqRDFi3Sia12PMCx5Nj4cvTuoG6BrYgOG3SiztQn4NjPY8KuLa16fpn8v9nhLPLRnNKfUrKUh5gFtwWuGV7Edz%2BEMe%2FeeJFZtFMnuPVbUxKqTR8xyGnOLdROlWngGvhgrB2ZzBy%2Bav2HrnRVM0U%2FoDZJBrlarv6gJeBxeyDkrf6vRfygwUm&X-Amz-Signature=37d8c696d86bae0c611e6706304d1b7aa17a0f9fd81adea8656d85f286679756&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







