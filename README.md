



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMPPMZQG%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDH3Jls%2F2iLoDnia7fBvuZGgzLAYKkJmJOcODMl%2Fz1YNQIgZEivAfAaZ4PgB5Rzt2iFLCPM71Qc%2FLeHxdw9k7f9gMIq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDC47xXQ6QXouCEFAyircA4gV1BKxKc%2FA1cw%2FzZ%2BXnwX1VDKb3g8CKCmYLLloL8k8eDTeMzKtfwkFnq5ElH7oGn9t4DMupnprmkVcF6AYgwkOs8SP2e04iAeD9vnYty0qs0Z20XjPZ2j8SpNp%2BlNADYv1BCOHA4V2D1HZNlTpVgDiWY095x%2BTgydKOZF8CyqbBv9i1xCFWz7PC%2FsdAt3n4NYdwWSVqDP5V3Lf%2Bo7jPXo01CT1ZInHzu%2FXUALMplFeP10eKzFz%2F1VzdpYGeY1beDwDBuiHpUam5w7u9L9XZ75al8TyD2j%2BWNuWKGndW2RD97Bbsw6Pj4cBk%2BGI9JnuUCus3MiI%2FzrhjnlK2es3jJdvfEvPlpyxCkE5SVlBvyKwrRX2GOqMe0Y4uW2o9iO%2BEckTHuUqcMo6GuIdTiKd1ECaEuiQQdi4XLiVOp7Y9XmN9wF4ApC2NMNSDeyz9MEWN1ga7yDmsIWmP8%2BoLCK9O4lDYiUgKcDjCneZacSDMa1Pi%2Bsud7vUg0byrIcorfqXN8s1AQ0DAxrRqdY3ct300xydfDTFjcR%2Br4%2BS9Zz3ikBTJuNROUrmwocB2hT7zuT0we9tZWNR6sQuC%2BSH8T4d5Zt%2BPAgfsepaGPPw9mWazYLHLcStFqCNjfAERKZtMKa7odIGOqUBS%2BBzLpil%2FSlj7sjkeMfOMgSkHnsf0FS8%2Bu5AvXRrI%2FHAvgSxfGtgkJdfzLDvi%2B9Ja8dDpSGdj7hp7HSGLl0eXDGL%2FAzZsuppjI3e8s4rkiOiaokrfALByMj1AiHMyfYneM1%2FEZxSCEXqvjbwkJM2uR87uipuzhMaeJvvyPPlDzT%2BYDyfMFMSSsmHIgrFzA793xutt6AJlL5kQ%2B1oJsSkBN3OVmdV&X-Amz-Signature=47a85aac100de47c4e48906e935bb0ed47e750b363d9c7c54ace717d01b2ba64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMPPMZQG%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDH3Jls%2F2iLoDnia7fBvuZGgzLAYKkJmJOcODMl%2Fz1YNQIgZEivAfAaZ4PgB5Rzt2iFLCPM71Qc%2FLeHxdw9k7f9gMIq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDC47xXQ6QXouCEFAyircA4gV1BKxKc%2FA1cw%2FzZ%2BXnwX1VDKb3g8CKCmYLLloL8k8eDTeMzKtfwkFnq5ElH7oGn9t4DMupnprmkVcF6AYgwkOs8SP2e04iAeD9vnYty0qs0Z20XjPZ2j8SpNp%2BlNADYv1BCOHA4V2D1HZNlTpVgDiWY095x%2BTgydKOZF8CyqbBv9i1xCFWz7PC%2FsdAt3n4NYdwWSVqDP5V3Lf%2Bo7jPXo01CT1ZInHzu%2FXUALMplFeP10eKzFz%2F1VzdpYGeY1beDwDBuiHpUam5w7u9L9XZ75al8TyD2j%2BWNuWKGndW2RD97Bbsw6Pj4cBk%2BGI9JnuUCus3MiI%2FzrhjnlK2es3jJdvfEvPlpyxCkE5SVlBvyKwrRX2GOqMe0Y4uW2o9iO%2BEckTHuUqcMo6GuIdTiKd1ECaEuiQQdi4XLiVOp7Y9XmN9wF4ApC2NMNSDeyz9MEWN1ga7yDmsIWmP8%2BoLCK9O4lDYiUgKcDjCneZacSDMa1Pi%2Bsud7vUg0byrIcorfqXN8s1AQ0DAxrRqdY3ct300xydfDTFjcR%2Br4%2BS9Zz3ikBTJuNROUrmwocB2hT7zuT0we9tZWNR6sQuC%2BSH8T4d5Zt%2BPAgfsepaGPPw9mWazYLHLcStFqCNjfAERKZtMKa7odIGOqUBS%2BBzLpil%2FSlj7sjkeMfOMgSkHnsf0FS8%2Bu5AvXRrI%2FHAvgSxfGtgkJdfzLDvi%2B9Ja8dDpSGdj7hp7HSGLl0eXDGL%2FAzZsuppjI3e8s4rkiOiaokrfALByMj1AiHMyfYneM1%2FEZxSCEXqvjbwkJM2uR87uipuzhMaeJvvyPPlDzT%2BYDyfMFMSSsmHIgrFzA793xutt6AJlL5kQ%2B1oJsSkBN3OVmdV&X-Amz-Signature=963e6908b171d437c181c6b2db0f1441da1b618aa3705da0c3b520ffc1c8ed5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







