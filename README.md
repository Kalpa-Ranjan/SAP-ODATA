



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYKB2S6Z%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T014620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIErK8JGtg8x4lXsG6r6bDAxHZ%2BXrTkXQhQLZX%2FFocowcAiBrWszVEDQRXzgquoa9YTbQuV9AExvvvUklkAXF3%2BqBtCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Az4%2Bfy81a1IAyaGKtwDHsX5dCM%2FLjWSf7DBQhv%2Fs2ByQAq4WLl29xQbd%2Foa%2B0YvDTm9uGj24oWxFBLD09b42UOXXaEHlAda7LmXO6NyRNT192nid7BW%2B1Y5oZ94FIWHYyFuAxF%2F65TJHWt%2Buh12NxMW3mxktPZIJKMeA2SANFm5OzuLDDVSyeWkwGSoJcNtFgBAzJksDGs3N%2Frq5YflJHB04rzuplE%2FRisiJDolGVqw2YVqWldQQD8z6yeghzWrldRsXVqTeD65x7tsueuqDvjnv2v30R5Np2Ovpjm82LT7be8QYOtjd5MKpTGTS03h84mJaYt986bJgvOyOw1Fsssrlk8nmzsG7tU%2BbDDv%2BbArcbnpNTC0EsaRAEhDko%2Fawf5JEnsHX%2B4IX%2BVyL2kz%2B4%2F0zoVAFn2FmaduBHaMXL6u6YqeAmCN%2FEh%2Bxa7Zu55Mi7CSf7TXjTJjmX7mFE7rIX1ja1lqBKWBTSCfgX5uw5IXsYFTv5%2BZctiID928wKFgrhFyTTKAb5ChCl%2BHot5BPFlQArdvpvf3DVX%2BQA8fSzHNBW47GITV0jph3vYgURxwk7K%2FSIFkM7rVpQ8BCABqn8hL4sdWXPD%2F%2FL9yczTj6Rsnzaq%2BIHkgE4ESLj%2B4SLL94Z08AeUg%2B%2BvtPZEwrLrizQY6pgEIjWxplIRo1EAQbGzGxAvTohySLSpWU1SYY0lXyzHWZel3aBoxuWk7jJYho4mY77agA82rU%2BldPvfCDyjADuxXjDWut%2BYX3SsHutpwbY3sc9pXKGEN3dH4AK4tPR3aODk754%2BpNz64jT%2B0WG%2BXDbElH6X3FRH5B2Hl8cB04J3tTiZEPga0YDC9gpto%2FEuxvWmNTMNW%2BG%2BgdrsJQaSBgj32wY%2FImt73&X-Amz-Signature=bf2f0324ff636b9f17384b55488f4db12a4b2932610f700656ad4858134e8482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYKB2S6Z%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T014620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIErK8JGtg8x4lXsG6r6bDAxHZ%2BXrTkXQhQLZX%2FFocowcAiBrWszVEDQRXzgquoa9YTbQuV9AExvvvUklkAXF3%2BqBtCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Az4%2Bfy81a1IAyaGKtwDHsX5dCM%2FLjWSf7DBQhv%2Fs2ByQAq4WLl29xQbd%2Foa%2B0YvDTm9uGj24oWxFBLD09b42UOXXaEHlAda7LmXO6NyRNT192nid7BW%2B1Y5oZ94FIWHYyFuAxF%2F65TJHWt%2Buh12NxMW3mxktPZIJKMeA2SANFm5OzuLDDVSyeWkwGSoJcNtFgBAzJksDGs3N%2Frq5YflJHB04rzuplE%2FRisiJDolGVqw2YVqWldQQD8z6yeghzWrldRsXVqTeD65x7tsueuqDvjnv2v30R5Np2Ovpjm82LT7be8QYOtjd5MKpTGTS03h84mJaYt986bJgvOyOw1Fsssrlk8nmzsG7tU%2BbDDv%2BbArcbnpNTC0EsaRAEhDko%2Fawf5JEnsHX%2B4IX%2BVyL2kz%2B4%2F0zoVAFn2FmaduBHaMXL6u6YqeAmCN%2FEh%2Bxa7Zu55Mi7CSf7TXjTJjmX7mFE7rIX1ja1lqBKWBTSCfgX5uw5IXsYFTv5%2BZctiID928wKFgrhFyTTKAb5ChCl%2BHot5BPFlQArdvpvf3DVX%2BQA8fSzHNBW47GITV0jph3vYgURxwk7K%2FSIFkM7rVpQ8BCABqn8hL4sdWXPD%2F%2FL9yczTj6Rsnzaq%2BIHkgE4ESLj%2B4SLL94Z08AeUg%2B%2BvtPZEwrLrizQY6pgEIjWxplIRo1EAQbGzGxAvTohySLSpWU1SYY0lXyzHWZel3aBoxuWk7jJYho4mY77agA82rU%2BldPvfCDyjADuxXjDWut%2BYX3SsHutpwbY3sc9pXKGEN3dH4AK4tPR3aODk754%2BpNz64jT%2B0WG%2BXDbElH6X3FRH5B2Hl8cB04J3tTiZEPga0YDC9gpto%2FEuxvWmNTMNW%2BG%2BgdrsJQaSBgj32wY%2FImt73&X-Amz-Signature=1cde709041628f1f37c4f4ce23b24402901c1c1ea69ebf6179e37646b4b80c92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







