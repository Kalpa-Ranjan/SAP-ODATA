



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEXCGAGH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQC%2BxNwu4Z7q0zeAW1TyvzoKLKFs6CbWjZ%2F5cR8M%2BO2qKQIhANaSAOBsYNAWow5yYck40WfRZjM8ny0xozX%2Bf3wj53i5Kv8DCDsQABoMNjM3NDIzMTgzODA1IgyrLUItYcyETEKKOp8q3ANseuhrTCGs4LgCcZaKu%2BuqP7wwL1BJfndByuWk5m5oYDUsFvCY1P1kny55D6VgwkZkuko2DoH4NUkYMgNAZ6EyBDvSLQLcnhS9zyhI%2BHojns9brFj4hHI7DCNbLwuWXvDbORrWvGTFFazrdzgxvmL00ALDpYJyMN5k0qALDPFL%2FhwnoQMcHQvdTbHKR0PbLl5g3muYiC9afY%2BznBrdI%2BT92QAQWkHRqsGyeryTI30726WfC0dmq0QWomCMy%2BPasN0Y2gD9Kj37Zp3A3c2jhfn9CQqytxk332LpJbfIm9am0zX%2F4BKcKf55WcwLa8Ig0FixX2%2FFxr2uh0Z7nlY76HpFb1zLWO%2BHRdVwHC4zSkxQByRXfPGGwDzOh12vaQ4Tp%2FvLyo4kvW6mbA%2B1altySzbQNk9bYyblN0Wk3MLJzY1V61j3QP4w9%2FzJkeSgQOBecfULQFCapsyAUpIahqR0pGxMynFxMTd356TKftUOe4PRI6lp3nuQYVRvHV15sRFGoRdmIpgT6W0U3EUbH9pwjnFNVB%2FK3mvmzziTvLPOIt19S1fqy%2B%2FOE6NVuhKzniuZazjewzgVnNdREVLnHzu6x7C093XulLgt4W7R8hrYH8p%2FaZK%2BRYhp430D%2FZsbjzDVnbjRBjqkAY3LdAi2e7I%2F8ssVYcYMhnzXjPJQI%2FMjdRMZJ8eAwIeHotSbOHuhwAXdO0l3gkQy9IyEhmyjq%2BSUQylJXSqR3Y%2B91Optp%2F%2F3pyC%2Fy2AQwCBBvH30i0ZamZeW6Di0h77Qqc87eoIhLYOl0PmykhPxNg5mkARkBFcO44d8upu5IeTQSObo3Up26qpIJRpfI0fLlv11xAEz8eqZgIu2dDGRBk1hHb3G&X-Amz-Signature=cae4e3de792cc082dae2e4e006451149cbf6963e0ef97ebbb8c9de27957eac9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEXCGAGH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQC%2BxNwu4Z7q0zeAW1TyvzoKLKFs6CbWjZ%2F5cR8M%2BO2qKQIhANaSAOBsYNAWow5yYck40WfRZjM8ny0xozX%2Bf3wj53i5Kv8DCDsQABoMNjM3NDIzMTgzODA1IgyrLUItYcyETEKKOp8q3ANseuhrTCGs4LgCcZaKu%2BuqP7wwL1BJfndByuWk5m5oYDUsFvCY1P1kny55D6VgwkZkuko2DoH4NUkYMgNAZ6EyBDvSLQLcnhS9zyhI%2BHojns9brFj4hHI7DCNbLwuWXvDbORrWvGTFFazrdzgxvmL00ALDpYJyMN5k0qALDPFL%2FhwnoQMcHQvdTbHKR0PbLl5g3muYiC9afY%2BznBrdI%2BT92QAQWkHRqsGyeryTI30726WfC0dmq0QWomCMy%2BPasN0Y2gD9Kj37Zp3A3c2jhfn9CQqytxk332LpJbfIm9am0zX%2F4BKcKf55WcwLa8Ig0FixX2%2FFxr2uh0Z7nlY76HpFb1zLWO%2BHRdVwHC4zSkxQByRXfPGGwDzOh12vaQ4Tp%2FvLyo4kvW6mbA%2B1altySzbQNk9bYyblN0Wk3MLJzY1V61j3QP4w9%2FzJkeSgQOBecfULQFCapsyAUpIahqR0pGxMynFxMTd356TKftUOe4PRI6lp3nuQYVRvHV15sRFGoRdmIpgT6W0U3EUbH9pwjnFNVB%2FK3mvmzziTvLPOIt19S1fqy%2B%2FOE6NVuhKzniuZazjewzgVnNdREVLnHzu6x7C093XulLgt4W7R8hrYH8p%2FaZK%2BRYhp430D%2FZsbjzDVnbjRBjqkAY3LdAi2e7I%2F8ssVYcYMhnzXjPJQI%2FMjdRMZJ8eAwIeHotSbOHuhwAXdO0l3gkQy9IyEhmyjq%2BSUQylJXSqR3Y%2B91Optp%2F%2F3pyC%2Fy2AQwCBBvH30i0ZamZeW6Di0h77Qqc87eoIhLYOl0PmykhPxNg5mkARkBFcO44d8upu5IeTQSObo3Up26qpIJRpfI0fLlv11xAEz8eqZgIu2dDGRBk1hHb3G&X-Amz-Signature=4ffd7e7ea56adb939db8baca02a6ccca5b9f455616a5105251ca0ba252b4401b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







