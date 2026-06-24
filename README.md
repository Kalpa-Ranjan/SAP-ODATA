



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q44HYRX%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T085818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCICqIu%2BZwfO%2BQ00TkB7oZQNZi%2FYCn1fgwyFWitxwqoSyhAiEAvTR4NRSsmDMj%2B04hlOUcnDVatjLYDcKvjXsTIk8kkYMq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDAxcrn4aLIpk%2FAncTircA%2BOzLeH%2Fh3F3thrksX1cwWNbElPWu1dVjxutS7rff5Kni5PyoMRD3j%2FAdd6GJOFXbsWEy3npT8fumB0LlAQM3jy907%2Bzp8IDTSR3r%2FXFNHQI5PGBYuEtmpNOawom3EeBhv4ARkq5Xt59xM8G9tzS4UtZldCEhi4Y6WC8qOCmHTdvLuYJuDrhSbziKhUq%2FQxWUpxAXxiuUaPflNNuDTWM9XVOKP%2B9LH4msRJlo9t4qJjP2Kav9PUJdAAu2uo7MnFzWDd4oPkULaBlF1MHOul3RcckM9F8YDaL4tyAY2OM54IdDemIHU2vLe7bW8HxbSAtVUAEEEyCa0ip0pNayiza2JNewxSQP4FwYN%2FmJwE38tN9vbEUXw5uFF6RFZfSNt7SY28jpg%2BBcK40QUAQ8Twab6RWwCf1%2FXmJW%2BGK6H76swc3FI1kYFj9tBqv6ApAIUW%2F0bu2rFCi%2BSA70z4CYKXEgRieyM62R76A00tdjHm6sKyAsb483OB5UVedBkKu18Yew2s6CWQupnNCisalFD%2BQ8idq1%2BAM56lrr7wqb185yz9FV6hDlXpBx9j96yVG6i5UncUgVcwRVpd0vAsg41nzGeUoBW25Y0%2BgJtMjWOYKasuo8jLA9Iu%2BDWOScv8EMN6O7tEGOqUBZdZSARY4h8%2Bh02ewKlXmfmGlXxWawp20gvXVeAvpjKdDEX9SHgGq6vohp%2BApc2e3wbdz0Kie4q6KfmTQJ0uP8Z9X%2BmAvV86r6zssalRFt47jmvM%2BfE5Eto7hW8ERR56zJ4ecBgIcpC3ipxwZhCoPP%2BH0oEsiZ1GCSkINJp%2FR5yn4kMDP6%2BSIK3iGKh6f9Dr%2F2Dc%2FqwJWYkftLtkoq2ZJ6%2BbO8mLT&X-Amz-Signature=a2e698e94dadf429eef709e6a91c081989960ee87e0d9e250e4ba88612e8e589&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q44HYRX%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T085818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCICqIu%2BZwfO%2BQ00TkB7oZQNZi%2FYCn1fgwyFWitxwqoSyhAiEAvTR4NRSsmDMj%2B04hlOUcnDVatjLYDcKvjXsTIk8kkYMq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDAxcrn4aLIpk%2FAncTircA%2BOzLeH%2Fh3F3thrksX1cwWNbElPWu1dVjxutS7rff5Kni5PyoMRD3j%2FAdd6GJOFXbsWEy3npT8fumB0LlAQM3jy907%2Bzp8IDTSR3r%2FXFNHQI5PGBYuEtmpNOawom3EeBhv4ARkq5Xt59xM8G9tzS4UtZldCEhi4Y6WC8qOCmHTdvLuYJuDrhSbziKhUq%2FQxWUpxAXxiuUaPflNNuDTWM9XVOKP%2B9LH4msRJlo9t4qJjP2Kav9PUJdAAu2uo7MnFzWDd4oPkULaBlF1MHOul3RcckM9F8YDaL4tyAY2OM54IdDemIHU2vLe7bW8HxbSAtVUAEEEyCa0ip0pNayiza2JNewxSQP4FwYN%2FmJwE38tN9vbEUXw5uFF6RFZfSNt7SY28jpg%2BBcK40QUAQ8Twab6RWwCf1%2FXmJW%2BGK6H76swc3FI1kYFj9tBqv6ApAIUW%2F0bu2rFCi%2BSA70z4CYKXEgRieyM62R76A00tdjHm6sKyAsb483OB5UVedBkKu18Yew2s6CWQupnNCisalFD%2BQ8idq1%2BAM56lrr7wqb185yz9FV6hDlXpBx9j96yVG6i5UncUgVcwRVpd0vAsg41nzGeUoBW25Y0%2BgJtMjWOYKasuo8jLA9Iu%2BDWOScv8EMN6O7tEGOqUBZdZSARY4h8%2Bh02ewKlXmfmGlXxWawp20gvXVeAvpjKdDEX9SHgGq6vohp%2BApc2e3wbdz0Kie4q6KfmTQJ0uP8Z9X%2BmAvV86r6zssalRFt47jmvM%2BfE5Eto7hW8ERR56zJ4ecBgIcpC3ipxwZhCoPP%2BH0oEsiZ1GCSkINJp%2FR5yn4kMDP6%2BSIK3iGKh6f9Dr%2F2Dc%2FqwJWYkftLtkoq2ZJ6%2BbO8mLT&X-Amz-Signature=f216395291cc56a0eb2fbb4a42f00d931f7942486237c8349eebc457c48b8fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







