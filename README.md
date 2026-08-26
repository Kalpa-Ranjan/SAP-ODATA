



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KKAZE5R%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T063754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHy7V1YLgrFafWelktzD0xrqgNvF%2B6OrrzcIX%2FWX8jnaAiEAvDgFbcSQO0PCu2SizYTmajPNMDxD7J2nUruCcT3%2BZpwq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDBo23QJ%2FsQnzq6KuPyrcAyZSl4RowNfhrR%2BwlrPgK2tBwz%2F3pVdofziDWG6yLnEjqCk7%2BVkWKUuYVC02OboYM280yQmgfJgmZq%2BWBbf6ksf0eZ%2FZ8eVpOsTQPfQLKtKTrhZ2JMii1vdGjSO7FfMXAQBm9oNKViDh8MO56apjElaYjhOWCmHMn0qFT0cz2ODR%2B2r5pnTGkMwYB8aakjshs8n9HiHLYzCEihC%2FToeAPAWoBI%2FHW%2ByZr1Id9KDAHCwoHGKbpWyE0U8tSf2whaLazo8co%2B2KCWHs7ms48dd8QCC9lfq6D%2BuA7Xy%2FJMtaCAjAki9Or7vf2tUT6vLs7ujferDnYLplBCAuiN3xfDlcDBDo5iV5AJfOFF9ORuuJc0hn05nhJa3ilFQpnmrvyB9BORZebUFdHDuDhjGYx0GvtluBelP8lHJlzW4WOgX4FattZ5ffcpEYcFuBDF5MXoakZieM6dw076ijU74zeYJkWp3TJJRgJt1hIwYxVZqqcHovZIX85MpI9VHAyf4rIOYHbTiyg4xQ2fHIQPLs8JzowPEXB%2F4xPbvjYcSSe2YJnWs%2FTrWvN0ThBr8mlm%2Bw0yZAkPYWGINrx0SB3e%2FJVnelSyc3Lid2l%2FAoQ0At1vOptuxb1lTmU%2BgDUW1YG3jMMO7XudQGOqUB76d6U41BDVRLHIQ96DJP3JMKEHFhbdvYk4gjHotPGZQjEblhzLdtEF%2BjqMcLXkHQdXU48z6Dz7HRZAKIdXWzfhsrBirmmoHsS1tMyxN5xrPhD9mP%2BwUH0cCt%2BZHqUqHGbYCoBpN%2F%2FgHhYi2WFqMMXDGCr3OIrPjcAWWXodGU4vDG6K%2BA9HQqH3pn%2BZ6mKETDk%2FZMX%2BsgwDUi0Mz9B50NaVSD71C0&X-Amz-Signature=be9fdbfef614285efa208cc0a837d40e34b0365d66a9c239566bc1844c227260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KKAZE5R%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T063754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHy7V1YLgrFafWelktzD0xrqgNvF%2B6OrrzcIX%2FWX8jnaAiEAvDgFbcSQO0PCu2SizYTmajPNMDxD7J2nUruCcT3%2BZpwq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDBo23QJ%2FsQnzq6KuPyrcAyZSl4RowNfhrR%2BwlrPgK2tBwz%2F3pVdofziDWG6yLnEjqCk7%2BVkWKUuYVC02OboYM280yQmgfJgmZq%2BWBbf6ksf0eZ%2FZ8eVpOsTQPfQLKtKTrhZ2JMii1vdGjSO7FfMXAQBm9oNKViDh8MO56apjElaYjhOWCmHMn0qFT0cz2ODR%2B2r5pnTGkMwYB8aakjshs8n9HiHLYzCEihC%2FToeAPAWoBI%2FHW%2ByZr1Id9KDAHCwoHGKbpWyE0U8tSf2whaLazo8co%2B2KCWHs7ms48dd8QCC9lfq6D%2BuA7Xy%2FJMtaCAjAki9Or7vf2tUT6vLs7ujferDnYLplBCAuiN3xfDlcDBDo5iV5AJfOFF9ORuuJc0hn05nhJa3ilFQpnmrvyB9BORZebUFdHDuDhjGYx0GvtluBelP8lHJlzW4WOgX4FattZ5ffcpEYcFuBDF5MXoakZieM6dw076ijU74zeYJkWp3TJJRgJt1hIwYxVZqqcHovZIX85MpI9VHAyf4rIOYHbTiyg4xQ2fHIQPLs8JzowPEXB%2F4xPbvjYcSSe2YJnWs%2FTrWvN0ThBr8mlm%2Bw0yZAkPYWGINrx0SB3e%2FJVnelSyc3Lid2l%2FAoQ0At1vOptuxb1lTmU%2BgDUW1YG3jMMO7XudQGOqUB76d6U41BDVRLHIQ96DJP3JMKEHFhbdvYk4gjHotPGZQjEblhzLdtEF%2BjqMcLXkHQdXU48z6Dz7HRZAKIdXWzfhsrBirmmoHsS1tMyxN5xrPhD9mP%2BwUH0cCt%2BZHqUqHGbYCoBpN%2F%2FgHhYi2WFqMMXDGCr3OIrPjcAWWXodGU4vDG6K%2BA9HQqH3pn%2BZ6mKETDk%2FZMX%2BsgwDUi0Mz9B50NaVSD71C0&X-Amz-Signature=cf56c3383d32e36041d38c0e1ce808da13b5cc37854842f27cb0326dc6a448be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







