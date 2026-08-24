



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JILLXX7%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T064409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCoHJwFI6FVlT%2F4daMmV96J71GxJ%2FgFcHbmmEieWhe0UwIhAKYonBTV2nA5gbz0YY6tYHzGHek7r8IJiCDJRAaceacuKogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhkngHEstx8aT7RNIq3AMP%2FseVlEhjQ0PebAZBBx0Lyyzyst2q0Hjwt1xGdtnzUxIT6MPze9QsaY5YQVY9RjGqvaTasLxumk4WmWApF%2BczXvnMAOrIxxxaBXBMMmaGzvAQkKtazbCADWk%2BBCjmGPqLnpv0ZqvLutpu0XMLcsLwB72shTY4gpuhfPKFns7TQUwvX6dKlCLwlKednsf%2BjhpQqYAzd7G8D5kmV8fd1Rp2uIkzD3XH5yBokdefjVoPard9Ahvbrlz3vHcpZ31c3rg26bPu56nWM%2FALnCcFNE4aGyJdbMnAwtVLrxjICeAMes4kCjFbLldkPu%2BhTlxUCaCClf1EWBjBFjapnwnU2EV3twVBKnSzZP6nT7qx1%2BvD5uIOgANjFENGe05X88QkSSOfWwi8xzWgBTYb8Ecb7I9y8Ugg98HX7WrHZRSs5BjrgGRX2BbiyBx%2FoaIUzU78UR9bzVDxrNz9VHAyvEGo%2F%2B9N6qVh8fmxfwLClfu5idOX9%2F5PlvVt50H2F1bldIszhmqJBvYp%2BImqW0yEkQBlvop4uVCQXCkY6oFyRr1zeB3G8EdxhkQqrN0vCTJfZfkHGr3Bc7zsNztvg9GB%2B6T84FtKFgKyPCuhiUwSw%2FeILEaVejmz1viOUekIIfyqlDDhoa%2FUBjqkAUipVg7B3joMarCxj%2B%2FvkYccC%2FS3pEnJdLZdUllv17rq2OHkt6oZtkIf%2Bv9WYA3LqtgueUZGq693JmVzs9hGp6pwxFOLozK0dsIgft18fpiisOEtkEJtW1aaIKDVVg3vRD17kWpnYNOGdNstUhf2eLm4YeKnqbLAAs3UB2SpNbJKkWSJtVelJfLTYjAt2ooDac54FdSaaFuP6sY2DXfRW6XRPRU7&X-Amz-Signature=bdb4bd1dd6e64a6bf2464890eba3b92dd5dac8e9d0af69c5d096fa3e0b2a947f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JILLXX7%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T064409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCoHJwFI6FVlT%2F4daMmV96J71GxJ%2FgFcHbmmEieWhe0UwIhAKYonBTV2nA5gbz0YY6tYHzGHek7r8IJiCDJRAaceacuKogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhkngHEstx8aT7RNIq3AMP%2FseVlEhjQ0PebAZBBx0Lyyzyst2q0Hjwt1xGdtnzUxIT6MPze9QsaY5YQVY9RjGqvaTasLxumk4WmWApF%2BczXvnMAOrIxxxaBXBMMmaGzvAQkKtazbCADWk%2BBCjmGPqLnpv0ZqvLutpu0XMLcsLwB72shTY4gpuhfPKFns7TQUwvX6dKlCLwlKednsf%2BjhpQqYAzd7G8D5kmV8fd1Rp2uIkzD3XH5yBokdefjVoPard9Ahvbrlz3vHcpZ31c3rg26bPu56nWM%2FALnCcFNE4aGyJdbMnAwtVLrxjICeAMes4kCjFbLldkPu%2BhTlxUCaCClf1EWBjBFjapnwnU2EV3twVBKnSzZP6nT7qx1%2BvD5uIOgANjFENGe05X88QkSSOfWwi8xzWgBTYb8Ecb7I9y8Ugg98HX7WrHZRSs5BjrgGRX2BbiyBx%2FoaIUzU78UR9bzVDxrNz9VHAyvEGo%2F%2B9N6qVh8fmxfwLClfu5idOX9%2F5PlvVt50H2F1bldIszhmqJBvYp%2BImqW0yEkQBlvop4uVCQXCkY6oFyRr1zeB3G8EdxhkQqrN0vCTJfZfkHGr3Bc7zsNztvg9GB%2B6T84FtKFgKyPCuhiUwSw%2FeILEaVejmz1viOUekIIfyqlDDhoa%2FUBjqkAUipVg7B3joMarCxj%2B%2FvkYccC%2FS3pEnJdLZdUllv17rq2OHkt6oZtkIf%2Bv9WYA3LqtgueUZGq693JmVzs9hGp6pwxFOLozK0dsIgft18fpiisOEtkEJtW1aaIKDVVg3vRD17kWpnYNOGdNstUhf2eLm4YeKnqbLAAs3UB2SpNbJKkWSJtVelJfLTYjAt2ooDac54FdSaaFuP6sY2DXfRW6XRPRU7&X-Amz-Signature=02ea1505fe5c0ad38382c742ab9d61db7a59eb4f017b4f002e453e634c056fab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







