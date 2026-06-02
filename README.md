



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSFVHWD5%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T101315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIHri9kXtLFewXiwL3Sh6X9klRGC6WG7p%2Bk%2B79bLaqiFlAiEAjiIRiCdqJCafl3RLxNVQuhKf0cAYuGw54WjrXHSg4mIq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDI8U%2FiHu7Ud7DsUe7ircA1HR8lv%2FV4wMSkvt5x12BpY91q4rLRT0i7kCIJfq7696QwV7wGk5iCB93ekqBh%2FLjXknbQpQMgbo4xH%2FFPgImRBm3NaYfqXOfF5RD6MnfdlXtFacu6oS76ShMnwpFpHkOLLpZP708RGXBuEn%2BCXEzE6b5ux8wr71mwqTu302eISDZS1IYkkJQ04eTOFjCzMddleJJ7emaUHWHwa86daw0ORKpmB1Si4yJYsKBfve90gM6y7to7MXcwpKbWOcapHqCpvLe6TtnrdweTADT0jBHAJHqabUlytHsrhUEGdWQvQ4MsebOM4CBtGcjxbjhB8Pwkkg3Z45pgu1rwPB8qDzS1O8yyfrsq%2FyMFj8fCvIlxgFUWxOVy8s49uumrMmXTvImkqWOP5VIhH8tu4qaWRjoy7rMVvl0VrsB%2BoOB7yfqkWI0ZgbwZpER3HkcymvMbxvbyxlCCo26yRN633X6tu9V%2BsB5jY8pGkrzxOjp7dNO8ZdJqJnY4tgHIxT11Qu%2BcMLeOX0TKr29qBh5pEkXREJmslG4qiYnUuyk5kFO%2BwXQlLS7kL%2FvB%2FLxvChnGIKPAgagysRjgGDgcTZUQF7b9gI6u8xX6x48zEjGHUGvp379TltgAtMjX07nsgF3gRaMLG5%2BtAGOqUBRpadv4IqZ1cndwWslqUngNBAkcgZ6%2F98lE41T2YDh3HS3pI5yjkc8FafY8sjsj%2BMRqQ78FXgRjE3RULqpvfW2xDLETxdZYodDiGwVN4UrmjdhN0pGCqkeJvjQHRdWt4Z%2FJ7RKplN7qpIJPNW5U14NzQZP3L50IM5E1gLSSKtDlJHQbxNBdsXj1jXT1divv0QYbD2LrmzfX9pNNa16c51ea4kk5Wa&X-Amz-Signature=80656a1f32f9f2239a5ed7ba6794920f522eb232eeb1716c5c50dbe2d6677726&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSFVHWD5%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T101315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIHri9kXtLFewXiwL3Sh6X9klRGC6WG7p%2Bk%2B79bLaqiFlAiEAjiIRiCdqJCafl3RLxNVQuhKf0cAYuGw54WjrXHSg4mIq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDI8U%2FiHu7Ud7DsUe7ircA1HR8lv%2FV4wMSkvt5x12BpY91q4rLRT0i7kCIJfq7696QwV7wGk5iCB93ekqBh%2FLjXknbQpQMgbo4xH%2FFPgImRBm3NaYfqXOfF5RD6MnfdlXtFacu6oS76ShMnwpFpHkOLLpZP708RGXBuEn%2BCXEzE6b5ux8wr71mwqTu302eISDZS1IYkkJQ04eTOFjCzMddleJJ7emaUHWHwa86daw0ORKpmB1Si4yJYsKBfve90gM6y7to7MXcwpKbWOcapHqCpvLe6TtnrdweTADT0jBHAJHqabUlytHsrhUEGdWQvQ4MsebOM4CBtGcjxbjhB8Pwkkg3Z45pgu1rwPB8qDzS1O8yyfrsq%2FyMFj8fCvIlxgFUWxOVy8s49uumrMmXTvImkqWOP5VIhH8tu4qaWRjoy7rMVvl0VrsB%2BoOB7yfqkWI0ZgbwZpER3HkcymvMbxvbyxlCCo26yRN633X6tu9V%2BsB5jY8pGkrzxOjp7dNO8ZdJqJnY4tgHIxT11Qu%2BcMLeOX0TKr29qBh5pEkXREJmslG4qiYnUuyk5kFO%2BwXQlLS7kL%2FvB%2FLxvChnGIKPAgagysRjgGDgcTZUQF7b9gI6u8xX6x48zEjGHUGvp379TltgAtMjX07nsgF3gRaMLG5%2BtAGOqUBRpadv4IqZ1cndwWslqUngNBAkcgZ6%2F98lE41T2YDh3HS3pI5yjkc8FafY8sjsj%2BMRqQ78FXgRjE3RULqpvfW2xDLETxdZYodDiGwVN4UrmjdhN0pGCqkeJvjQHRdWt4Z%2FJ7RKplN7qpIJPNW5U14NzQZP3L50IM5E1gLSSKtDlJHQbxNBdsXj1jXT1divv0QYbD2LrmzfX9pNNa16c51ea4kk5Wa&X-Amz-Signature=ddfd9da4cee55dedfe80b626d160a8f7a4472ad0280f57a54bf5d149b1d0fb4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







