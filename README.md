



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XDHXNSN%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T025543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQD1ew6ysOqqRQ%2BAQT0PsVz6WvXWFLL4iGDjVN7NMtUiSAIgdp4bUmtomyDgkmQKfnLt85Qbxs4UFpbd81nAysEKmBgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcaJJodYCavh51OuyrcAyu77co6dYdJR%2BuUyeAgE20fVCu7vmEFveMbOCdIs69gR%2BN%2B0u8eps4IG3xcLSg9KlFMo7kq%2B3om43W4Hhzelsl%2BOyNtnziaVHL8d9Da0AS5JQZKkk0jTUZpjvp37yq7piSAloT5KQwDJ9SLEt8nZQGzq4GkgqQNvN52HDoSmuWmdNBoUAi9San50%2BSPZZJ07nlDje3WYEfqiT0sUD2Sb6pmUoMxmf4I0X8RvBxgazqW6ay7U%2FGlPpu2277pIq5wKQ6zwPeBF7lffHpFVUKKt1iGOboe%2FEwlLs8zMVN7IltFrXu74knR8GCVekRP35ocU%2B9KzhA3%2FLbEUzuQsod8ElefCy58YF8jy9izLv5KTbd0ol%2FaGl%2F96Ei45kNwaMjJPUAmQzptr5JmV0b9RdS9osO9CKlcjzIYKGLo52yyKxWYnkzkmGmClBkpajoVCMBu8CGOP1JWmuTJZMOi%2BkpXWlOLMfmdLagemcDksyivSjl5WdwnDhDyWVjdYO3w66c%2BqZDTNMu9LVQK5m1A78Mzsrr1rSG8Yd6vXu8qjHVs2sBuhHySPFeH66zK2Hp2dYWCYtldcwjzkip%2FJ5iQC3BFvACa9oh3%2FNCkGa2TUNZE1x6jfVpP%2BMSFQAjLQBnwMJmu7tAGOqUBmNjvtey4mGi3ZN9Flx9pRdn07ZB0ZBhDflYfFQIVIJ%2Ba0XQk3UaNIcgWomI%2BptZ9kQWuwOJutHhLcA43C5DoQ7X5ndYgs6qy9H8JAg98zgoL%2Fp4HHz8zCzlX9YKpQVtpBU0xrLKQmZ0Q0JDESef3qFK45YQRYBDWL3h0Mfx4%2BqZISFG0%2FaWrvX7Bw1s4A9WzmPV87lAnnKGG4hXx4tgH6eq1WvTE&X-Amz-Signature=b438d08de271d5c6fe9031db8f05113ae4e18824e13333cd585171cabbabb4a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XDHXNSN%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T025543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQD1ew6ysOqqRQ%2BAQT0PsVz6WvXWFLL4iGDjVN7NMtUiSAIgdp4bUmtomyDgkmQKfnLt85Qbxs4UFpbd81nAysEKmBgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcaJJodYCavh51OuyrcAyu77co6dYdJR%2BuUyeAgE20fVCu7vmEFveMbOCdIs69gR%2BN%2B0u8eps4IG3xcLSg9KlFMo7kq%2B3om43W4Hhzelsl%2BOyNtnziaVHL8d9Da0AS5JQZKkk0jTUZpjvp37yq7piSAloT5KQwDJ9SLEt8nZQGzq4GkgqQNvN52HDoSmuWmdNBoUAi9San50%2BSPZZJ07nlDje3WYEfqiT0sUD2Sb6pmUoMxmf4I0X8RvBxgazqW6ay7U%2FGlPpu2277pIq5wKQ6zwPeBF7lffHpFVUKKt1iGOboe%2FEwlLs8zMVN7IltFrXu74knR8GCVekRP35ocU%2B9KzhA3%2FLbEUzuQsod8ElefCy58YF8jy9izLv5KTbd0ol%2FaGl%2F96Ei45kNwaMjJPUAmQzptr5JmV0b9RdS9osO9CKlcjzIYKGLo52yyKxWYnkzkmGmClBkpajoVCMBu8CGOP1JWmuTJZMOi%2BkpXWlOLMfmdLagemcDksyivSjl5WdwnDhDyWVjdYO3w66c%2BqZDTNMu9LVQK5m1A78Mzsrr1rSG8Yd6vXu8qjHVs2sBuhHySPFeH66zK2Hp2dYWCYtldcwjzkip%2FJ5iQC3BFvACa9oh3%2FNCkGa2TUNZE1x6jfVpP%2BMSFQAjLQBnwMJmu7tAGOqUBmNjvtey4mGi3ZN9Flx9pRdn07ZB0ZBhDflYfFQIVIJ%2Ba0XQk3UaNIcgWomI%2BptZ9kQWuwOJutHhLcA43C5DoQ7X5ndYgs6qy9H8JAg98zgoL%2Fp4HHz8zCzlX9YKpQVtpBU0xrLKQmZ0Q0JDESef3qFK45YQRYBDWL3h0Mfx4%2BqZISFG0%2FaWrvX7Bw1s4A9WzmPV87lAnnKGG4hXx4tgH6eq1WvTE&X-Amz-Signature=e7fdf3beab71406573bb541864823774ba2241c12472fb40d31d28d1ad3f4b8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







