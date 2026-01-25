



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVNJZTGK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T182340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIA1xwtp5Fnfq7xoUKJ3MqyxIqti1wQQxHA6Qw3pcVnScAiBi3qU5DwNCGnn3oK%2FltsPT5OBiHTDGBMufg6MJSfY7ESr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMJnelUCYhgJz2gfMiKtwDk0Zq5JbBL99mP9TaqJA0GcP%2F8%2BiIdlyC%2FnjMCf5RIetIDK9p%2FH5RpgVBT4arjm1qd%2BBkV3Qw%2Fv%2FHfHImmxgcy3wDOtk4Ccr%2B4RZW7BiXm2bC%2Bo6utXg65RMXg%2FBzLnJDT6NCVvtj6zWRJkQveHerRhdgu8nqk0hX2HXaSTl9i84XoBao1sStpYxgWhJZKwqqZBmcokxKoJTK%2Bhu1ue3HVHbz3auDrYn3oq22erRB5gUStGvuYp9mDCvC2JKha1jlnHeU029NB1gFAWo6R03Y5Z1RmkFdczzL%2FH4%2FMNo%2FB0xO2ATtZx%2BZPtEHbmtuCfcw6lYJ3Pq7yuEh3YTi8KsCaCq%2F%2BYvBpaTkwHglmdtQtWdACskpsQY50%2Bl3XOL9cPugWBYDqyGFlte9ytx%2F8XSZZ3BqzRdHWo0YBQ1F39mm%2Fn1NXrS6Efyy%2BpD10BIh7Mu7tiD%2FLU6ulxYs9mtw9O%2BcdQgaRF1m3Maam4pe3pzubxmm78gd09yWGVtxVK%2BRke2Q949pWLvwYcodS1BbTpvVvcLImvs9cKbuDCJBiyC40UAobYnhclOYndfLKe6duYFYHtifkeRxT99UPysj5y6JZHp0wVab1NX9hbtI%2B69Wf37%2FyIAD2eYhAQBLmoIwmfnYywY6pgFBpk5IcLOrLGZT7JXW9bZG38CB213YQXfvEgi%2FsNaiXR0TAsRIIX8MJcvkMw19QofYkxGE%2BNH30lHbeW9md9gyWDZ5%2F53kjeWVfPDZoUrHMuRynMwm72rmwAQV7haQg3vvu%2BuOEJy0jff%2FrnQ6%2FZegjb3qffAl%2FeAYXOlJ9xTnvvOHUyahX5PuSQwHoCYQk%2FT2%2FncxzV2mhOeCGNVkQgZvnkOI8E8g&X-Amz-Signature=0d0fb4bfa754fd16e080a7730df4b02cc82937bb50eb9fc4bfd3935a821f6854&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVNJZTGK%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T182340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIA1xwtp5Fnfq7xoUKJ3MqyxIqti1wQQxHA6Qw3pcVnScAiBi3qU5DwNCGnn3oK%2FltsPT5OBiHTDGBMufg6MJSfY7ESr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMJnelUCYhgJz2gfMiKtwDk0Zq5JbBL99mP9TaqJA0GcP%2F8%2BiIdlyC%2FnjMCf5RIetIDK9p%2FH5RpgVBT4arjm1qd%2BBkV3Qw%2Fv%2FHfHImmxgcy3wDOtk4Ccr%2B4RZW7BiXm2bC%2Bo6utXg65RMXg%2FBzLnJDT6NCVvtj6zWRJkQveHerRhdgu8nqk0hX2HXaSTl9i84XoBao1sStpYxgWhJZKwqqZBmcokxKoJTK%2Bhu1ue3HVHbz3auDrYn3oq22erRB5gUStGvuYp9mDCvC2JKha1jlnHeU029NB1gFAWo6R03Y5Z1RmkFdczzL%2FH4%2FMNo%2FB0xO2ATtZx%2BZPtEHbmtuCfcw6lYJ3Pq7yuEh3YTi8KsCaCq%2F%2BYvBpaTkwHglmdtQtWdACskpsQY50%2Bl3XOL9cPugWBYDqyGFlte9ytx%2F8XSZZ3BqzRdHWo0YBQ1F39mm%2Fn1NXrS6Efyy%2BpD10BIh7Mu7tiD%2FLU6ulxYs9mtw9O%2BcdQgaRF1m3Maam4pe3pzubxmm78gd09yWGVtxVK%2BRke2Q949pWLvwYcodS1BbTpvVvcLImvs9cKbuDCJBiyC40UAobYnhclOYndfLKe6duYFYHtifkeRxT99UPysj5y6JZHp0wVab1NX9hbtI%2B69Wf37%2FyIAD2eYhAQBLmoIwmfnYywY6pgFBpk5IcLOrLGZT7JXW9bZG38CB213YQXfvEgi%2FsNaiXR0TAsRIIX8MJcvkMw19QofYkxGE%2BNH30lHbeW9md9gyWDZ5%2F53kjeWVfPDZoUrHMuRynMwm72rmwAQV7haQg3vvu%2BuOEJy0jff%2FrnQ6%2FZegjb3qffAl%2FeAYXOlJ9xTnvvOHUyahX5PuSQwHoCYQk%2FT2%2FncxzV2mhOeCGNVkQgZvnkOI8E8g&X-Amz-Signature=115b2c6d968183ef3e233de47b44fbec9d85450c85085f867af6eb3cbf3d95b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







