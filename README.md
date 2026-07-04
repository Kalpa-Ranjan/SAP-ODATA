



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIDD5TBR%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T082930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDfvzwyzUCb%2F0WkX8vzmXqCoBFPNJ%2BukVjPnMYkJ0WMgAIgGvJg1rrWQUrmEfZXQOcqS798dF1RaWKRYntrVrsaIe4q%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDKCNtl9g9qS%2FNh2mvCrcAyXzjM8ByB1rv5%2BOhNn3uNvpJi5fil3qTatH1LL6W6G1Fjk%2FRVhSh0Qoc7pWGOA%2FPq4jLZj9gNVLhrrBfqb%2BKTjHySA8K%2FUGZsc5VHeI2x1W6g29BKEgWnll8u00z6dBB5wbNh9OnN7sQdjb%2FfjWMe0v%2FrQtutYCHofIHAKz0fJd%2FLtOdNfu0BA8XR%2FucTJa54KD5R74ioPpSFSuILVqdkF%2BmM27CaQHHO9CZnhbYk9qSecTRqCHYYlMgMo91aJrXipXfmNEKJ1vAzcDP8UL5QvoyM2%2BFC7LNSvHe%2BHb8mD8jRbjgByQCNVuOn9ZMB8By2wpkrIUqAv%2B5bBSSoQYPb2AuTxv9htTZ1W0Q4vMSLWxZZhzdZSsHwQBuCYv56A%2Ft8CwUDn2PWz%2Ftc3a%2FJxFqgczbEQJDxQzV29GucNEEGzFGolrBoLpa9jzMwJBite0B3Wa69s4qt4E8vlU7UP0BJadbBbcimCfQnUTqNRA%2B99mjkQjLEP0BzuBmrWpPW8zeEINBFat83wuGPthCYYgrWwc9pfnIwmxaOKYm8hTZOZodE%2F4yXWElUWuX%2FZ56YU7i2VFArprOb7DFWmRnm90XfsmaO4%2B5P9TOx5PbeVd1DUJW0jn6Y5GkcQ0yfpAMMH1otIGOqUBd63OHgSuVwf2abikki1zI87NSvKveMrNdeOGf3VFAqP5v9fIxwDu11Mte0EXQym4rN5MO2tKZ8SVEhl14lyn7EeVYdIJo6kRoagqIsA8nQsT4IVgC3keqM3s8D6mfbr5mb3jr48TVS3aJuV2USyBQhTe3g3FSYznVLwjRTS9vahoZV38WWtvFVpFCnxnqkYJdXxhwYlQoLphsPkaZGR%2BRg080KA%2B&X-Amz-Signature=6affeedbcf8be414cbca93dc27b6f0421741e59c51bea2782a9a62a775e32cb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIDD5TBR%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T082930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDfvzwyzUCb%2F0WkX8vzmXqCoBFPNJ%2BukVjPnMYkJ0WMgAIgGvJg1rrWQUrmEfZXQOcqS798dF1RaWKRYntrVrsaIe4q%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDKCNtl9g9qS%2FNh2mvCrcAyXzjM8ByB1rv5%2BOhNn3uNvpJi5fil3qTatH1LL6W6G1Fjk%2FRVhSh0Qoc7pWGOA%2FPq4jLZj9gNVLhrrBfqb%2BKTjHySA8K%2FUGZsc5VHeI2x1W6g29BKEgWnll8u00z6dBB5wbNh9OnN7sQdjb%2FfjWMe0v%2FrQtutYCHofIHAKz0fJd%2FLtOdNfu0BA8XR%2FucTJa54KD5R74ioPpSFSuILVqdkF%2BmM27CaQHHO9CZnhbYk9qSecTRqCHYYlMgMo91aJrXipXfmNEKJ1vAzcDP8UL5QvoyM2%2BFC7LNSvHe%2BHb8mD8jRbjgByQCNVuOn9ZMB8By2wpkrIUqAv%2B5bBSSoQYPb2AuTxv9htTZ1W0Q4vMSLWxZZhzdZSsHwQBuCYv56A%2Ft8CwUDn2PWz%2Ftc3a%2FJxFqgczbEQJDxQzV29GucNEEGzFGolrBoLpa9jzMwJBite0B3Wa69s4qt4E8vlU7UP0BJadbBbcimCfQnUTqNRA%2B99mjkQjLEP0BzuBmrWpPW8zeEINBFat83wuGPthCYYgrWwc9pfnIwmxaOKYm8hTZOZodE%2F4yXWElUWuX%2FZ56YU7i2VFArprOb7DFWmRnm90XfsmaO4%2B5P9TOx5PbeVd1DUJW0jn6Y5GkcQ0yfpAMMH1otIGOqUBd63OHgSuVwf2abikki1zI87NSvKveMrNdeOGf3VFAqP5v9fIxwDu11Mte0EXQym4rN5MO2tKZ8SVEhl14lyn7EeVYdIJo6kRoagqIsA8nQsT4IVgC3keqM3s8D6mfbr5mb3jr48TVS3aJuV2USyBQhTe3g3FSYznVLwjRTS9vahoZV38WWtvFVpFCnxnqkYJdXxhwYlQoLphsPkaZGR%2BRg080KA%2B&X-Amz-Signature=b7d1f0adc973ad9f8d189a8a4fabffc6c9006b3020a7be6dacac7501a1bab57d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







