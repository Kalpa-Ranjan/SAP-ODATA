



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6Y7LYGQ%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T001132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIDZ%2B9MRaE6xNqa6HIzyCh%2FzqE%2BNKFbQZMDzlLG%2F0%2FQNCAiBUgx1QnXUPxyYBPpBCyxvaByE%2FjWiRuHd8K6qlw1N7RiqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcGsUaWBYtTXNR4TDKtwDA8JTVLyomP54ooiPvb%2FmMlP09BlyFuOpYBANK719AceOFVvQYN8e1l9F8%2BnfcFEDLJza6K2dP52QRbKYcQetnl4wa8WN%2BA2k5Bi7HzcldBfj56pkRFO3w7CPQ%2BiT%2F96PwuSKxFta4362IvatSkMHj3yt%2BVFHO0E%2Fzr%2BYUctOG4gWoGlQQ606r4nipYdO4S3BlqC%2FA1Xb%2FBt%2BNhyvYX3b8bj%2BSqOx%2B2WXdNoBQ7ZOe%2FI1ObTMB4qS60zwQTVnXS9hckNhsH3XDHN3A54l7UnZ%2FlsY70nRkOKg%2Bpei24uIQRcwP7z%2FixrjHq7zARmasw%2BDpOXO8%2BA1oHBgmwh6bB1Oe5JAM07ISfnKANIqMkwF7%2BFyjud4rQeKgCnYeS4DyBZMeXuVCMH5%2BDdzInqiWr%2BWF1AmRVh%2BmVJb1WAldHqySfTQZCpVXnk7HNrSRFwteX%2FEJhC%2B0FjxLVmW%2Bi4klfZflIqYPFlxHzLt3zTHnkDDLGx7QlztqSaIV%2BeKWSq5DWenOlSkfmVX38ButmnhgjKzja%2FLAXor7CYdx9Lx1crbNUyztYgogILmqJVGVZlUAXS8lUalRSCEtq1h4mtwoS76dpw8Mp3lmXvBcm5a7ZHEjiSnkzBU9Uw1n8c8xk4wqre51wY6pgFhLhRGSgWPX0QP0oohHdgXuTtOpP8pjQ9JdJdHIdTkAu%2BKruxFLTo0oOgQ4RmHr0eNHGrX8u%2FkcjyXoexrWdJo4UJIP1uN3EYWZDIUILFPelmaDhgmBka8WPS%2BlKiEtW2YBVxmy%2FPrMghjSOJxbuDzDvYN%2Br83Vr0IiLLHF6zTqeSq5KO%2Fs5BJf07GUsvvlRWVxIQGG242atk5S3LIelbRy%2Fj9uoRC&X-Amz-Signature=d2665a98beef4a39856f136caa849ac7255f074735f71e7f3497b09159f9095c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6Y7LYGQ%2F20261107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261107T001132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIDZ%2B9MRaE6xNqa6HIzyCh%2FzqE%2BNKFbQZMDzlLG%2F0%2FQNCAiBUgx1QnXUPxyYBPpBCyxvaByE%2FjWiRuHd8K6qlw1N7RiqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcGsUaWBYtTXNR4TDKtwDA8JTVLyomP54ooiPvb%2FmMlP09BlyFuOpYBANK719AceOFVvQYN8e1l9F8%2BnfcFEDLJza6K2dP52QRbKYcQetnl4wa8WN%2BA2k5Bi7HzcldBfj56pkRFO3w7CPQ%2BiT%2F96PwuSKxFta4362IvatSkMHj3yt%2BVFHO0E%2Fzr%2BYUctOG4gWoGlQQ606r4nipYdO4S3BlqC%2FA1Xb%2FBt%2BNhyvYX3b8bj%2BSqOx%2B2WXdNoBQ7ZOe%2FI1ObTMB4qS60zwQTVnXS9hckNhsH3XDHN3A54l7UnZ%2FlsY70nRkOKg%2Bpei24uIQRcwP7z%2FixrjHq7zARmasw%2BDpOXO8%2BA1oHBgmwh6bB1Oe5JAM07ISfnKANIqMkwF7%2BFyjud4rQeKgCnYeS4DyBZMeXuVCMH5%2BDdzInqiWr%2BWF1AmRVh%2BmVJb1WAldHqySfTQZCpVXnk7HNrSRFwteX%2FEJhC%2B0FjxLVmW%2Bi4klfZflIqYPFlxHzLt3zTHnkDDLGx7QlztqSaIV%2BeKWSq5DWenOlSkfmVX38ButmnhgjKzja%2FLAXor7CYdx9Lx1crbNUyztYgogILmqJVGVZlUAXS8lUalRSCEtq1h4mtwoS76dpw8Mp3lmXvBcm5a7ZHEjiSnkzBU9Uw1n8c8xk4wqre51wY6pgFhLhRGSgWPX0QP0oohHdgXuTtOpP8pjQ9JdJdHIdTkAu%2BKruxFLTo0oOgQ4RmHr0eNHGrX8u%2FkcjyXoexrWdJo4UJIP1uN3EYWZDIUILFPelmaDhgmBka8WPS%2BlKiEtW2YBVxmy%2FPrMghjSOJxbuDzDvYN%2Br83Vr0IiLLHF6zTqeSq5KO%2Fs5BJf07GUsvvlRWVxIQGG242atk5S3LIelbRy%2Fj9uoRC&X-Amz-Signature=b933d8253957345da9d054f43b8aa952d594d6354e3900f79e74143681008812&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







