



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWJ6R7N3%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T123529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmlbX9gGFs5Odp00MmhBfAKjTxtwG5q2cWLg%2B9Sg5sLgIgMvu8xBSWlvMnHPNnzwpIWzJDrApo4aNYqCg9I%2B4svMUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFG9otQPlSK328sjxCrcA0%2FuoVxZe9Q5qB5x6jyGOgRor1qLusMBDfMRzr9Mz1KvboWwkAQ0GD1QBrppw%2B5VG6SVC2aOvoAonMxke%2BHvuGRWSgT4MhS4ncImA113KmA2d5poHFHEhgggCzQVrb6H8g1gP6CKV%2Fw%2BMZe%2F3o%2BzkgYuXpnFWEbZqXTPgst78IoXEP3K4kAAriaG9%2BvK%2BAamI45LJPhAnPBA%2F5TPAXV8fPBEzjtXoivVW38uG9P8uyiW93Jm%2BYRLe5TkzO2y2hEOj3OH5M2RjL5htcKljFb8mSLQJSBpn04StROxOL5tsnj2xvllXYlYXcqu6IGVBZ0iKakJ%2BSQ%2BnxJGPS769Lbx3PLBAhSK5YXZ1u2Mcf1T%2BpLG6GSeiljj%2BqbOgzCz4%2F5Oh8PQhZ1r7t6xuWYoX8YsN%2BcsWwiuklOtPxAjyqr%2BvlJ5Cn%2BzJkrmeC6O%2Fc4jigFrrZnPnq9kYbAR8BTdrQxJIQ1gBhtE3UafLCqMZjhFMnRpXpSUgltvIlfTR1lD09CafYE6nNZ9IjDI7YYHSBHr%2BE6HjwlG%2FReBFbwkC5w92s4ddQ9wWnQWhzXp7S0qKIywQMAaEIGHKhGGzEG1rb0gsEFdn2e2qmBOm5Z8iFpUfbR1isz9AfaIN%2FuyOUWDMKT888oGOqUBO4xEwvppkapOh1E934SUwio0FP0La5Hb%2FUxJEwONWz6nsMiT1iDsCK9127WfTusN0YD6UI6Wsanl6P1Zuw3LhEBldFFsk2r0To9WgsxMtpJkauCDOYeSDZJnLEeW0kODolqnCVXD5YEfONyvk119zHpkt%2BlZHhzpyFMG3TYTM46C4jWtBMM1yt8dJZJXG7SJ0TMeQCUnN%2BeDnOHeaKE52C3Pa8U0&X-Amz-Signature=f9de9550af42cf930e94f02f8d563ed3578f45f311436bc034873882305d3990&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWJ6R7N3%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T123530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmlbX9gGFs5Odp00MmhBfAKjTxtwG5q2cWLg%2B9Sg5sLgIgMvu8xBSWlvMnHPNnzwpIWzJDrApo4aNYqCg9I%2B4svMUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFG9otQPlSK328sjxCrcA0%2FuoVxZe9Q5qB5x6jyGOgRor1qLusMBDfMRzr9Mz1KvboWwkAQ0GD1QBrppw%2B5VG6SVC2aOvoAonMxke%2BHvuGRWSgT4MhS4ncImA113KmA2d5poHFHEhgggCzQVrb6H8g1gP6CKV%2Fw%2BMZe%2F3o%2BzkgYuXpnFWEbZqXTPgst78IoXEP3K4kAAriaG9%2BvK%2BAamI45LJPhAnPBA%2F5TPAXV8fPBEzjtXoivVW38uG9P8uyiW93Jm%2BYRLe5TkzO2y2hEOj3OH5M2RjL5htcKljFb8mSLQJSBpn04StROxOL5tsnj2xvllXYlYXcqu6IGVBZ0iKakJ%2BSQ%2BnxJGPS769Lbx3PLBAhSK5YXZ1u2Mcf1T%2BpLG6GSeiljj%2BqbOgzCz4%2F5Oh8PQhZ1r7t6xuWYoX8YsN%2BcsWwiuklOtPxAjyqr%2BvlJ5Cn%2BzJkrmeC6O%2Fc4jigFrrZnPnq9kYbAR8BTdrQxJIQ1gBhtE3UafLCqMZjhFMnRpXpSUgltvIlfTR1lD09CafYE6nNZ9IjDI7YYHSBHr%2BE6HjwlG%2FReBFbwkC5w92s4ddQ9wWnQWhzXp7S0qKIywQMAaEIGHKhGGzEG1rb0gsEFdn2e2qmBOm5Z8iFpUfbR1isz9AfaIN%2FuyOUWDMKT888oGOqUBO4xEwvppkapOh1E934SUwio0FP0La5Hb%2FUxJEwONWz6nsMiT1iDsCK9127WfTusN0YD6UI6Wsanl6P1Zuw3LhEBldFFsk2r0To9WgsxMtpJkauCDOYeSDZJnLEeW0kODolqnCVXD5YEfONyvk119zHpkt%2BlZHhzpyFMG3TYTM46C4jWtBMM1yt8dJZJXG7SJ0TMeQCUnN%2BeDnOHeaKE52C3Pa8U0&X-Amz-Signature=07fa0dc71122803570a9237c0b8e126f34d98a46e960a044788b76ba2635649a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







