



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634E2GI7S%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T123823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAEfeP9B7cMa0w8IehkdSuYBn2%2BjD3exf6XQEu2l223iAiBdonWyZHKjP7VMSwiiIl3p09t1whioH7GAqUqHzI78pir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMoimvidkKq8OeMZyLKtwDj9C9BgZSrgIDAqMk6Pp3GSoPJadhUSGMXfQtMhTkAaFTWIZmgHjAQvFjycezGrO0%2Ff0GR94219l3k4LG0yyPq4%2FqwOq7YMW%2F36EST93hLQekf7Z91N08akTgjMhWAdXmUsdV8Yv32ed6%2FGrXLaw1Z9pZ%2Buc%2B4APDlINeXnvzdmR9E%2Fr%2FA3r3Cd88fetPGMgQml9%2FXwjHUhg7%2BvYwA%2BSh4fRZCSyuhB3nwm4t65KJKmqir7C8kEI%2FCXF9WcwozgilGDs9hqIG0%2FHKHj0%2BATJ1xBK%2BeEK6IgTCaTOwiELdfQIIXAMGwR7qj9xljmbgPoQJowFMGkb4gesPguWY1hs2cuiuZASwnLQozMGMB44cfScXPcicFn0CrA0c05aWJL8ZaL0ahkQNEDMpBsBWsgNyVuBDSG5ZJRHozDbmxqXphTh95qNH6abf6DcWJUJZG%2FeFD46FBbsHsYBRjzlToneIbOQ7993sm%2FVPH1jI5LSUGaJbF%2FzNbtAdjQHqyvxbRZXIzFQn%2FmVpv2lZIruxQM0HMh56ee3WjRGd3pIjoTEE%2BKlgSYtxao1uEZnuGWIG2MbdJvvW%2BwdGwHPwmswRmJdJUd7GfzMX9%2B6RqzqZP3KkQRz1XEN1%2BVDS8AsTfgQw%2F%2FGgzAY6pgGMrNnRfNoEXBCd5CQ%2BKUHigWSJGhNCXvwO3uHbLHSo6vrO%2BpZw05bedr1YGUC8vYFgdk%2BXPsUXEsCHad90xyEyO2k9053JYCtgcUALPSgsWVGNxv2Yg3oZmw5FmX17xpDxVUgIrguvfybYC2MVb%2BUvHC7JU1eUWFhix7SyWkNGyevQhQxfNjKRXHQHdtI5YypCiJU9UMSCDtFFmeV2%2BSdO3EkxeNLP&X-Amz-Signature=d158ceaa2f45d5dbf7de9e88dc18586aa868cc6e2186761fb53cc303f5f8dbcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634E2GI7S%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T123823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAEfeP9B7cMa0w8IehkdSuYBn2%2BjD3exf6XQEu2l223iAiBdonWyZHKjP7VMSwiiIl3p09t1whioH7GAqUqHzI78pir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMoimvidkKq8OeMZyLKtwDj9C9BgZSrgIDAqMk6Pp3GSoPJadhUSGMXfQtMhTkAaFTWIZmgHjAQvFjycezGrO0%2Ff0GR94219l3k4LG0yyPq4%2FqwOq7YMW%2F36EST93hLQekf7Z91N08akTgjMhWAdXmUsdV8Yv32ed6%2FGrXLaw1Z9pZ%2Buc%2B4APDlINeXnvzdmR9E%2Fr%2FA3r3Cd88fetPGMgQml9%2FXwjHUhg7%2BvYwA%2BSh4fRZCSyuhB3nwm4t65KJKmqir7C8kEI%2FCXF9WcwozgilGDs9hqIG0%2FHKHj0%2BATJ1xBK%2BeEK6IgTCaTOwiELdfQIIXAMGwR7qj9xljmbgPoQJowFMGkb4gesPguWY1hs2cuiuZASwnLQozMGMB44cfScXPcicFn0CrA0c05aWJL8ZaL0ahkQNEDMpBsBWsgNyVuBDSG5ZJRHozDbmxqXphTh95qNH6abf6DcWJUJZG%2FeFD46FBbsHsYBRjzlToneIbOQ7993sm%2FVPH1jI5LSUGaJbF%2FzNbtAdjQHqyvxbRZXIzFQn%2FmVpv2lZIruxQM0HMh56ee3WjRGd3pIjoTEE%2BKlgSYtxao1uEZnuGWIG2MbdJvvW%2BwdGwHPwmswRmJdJUd7GfzMX9%2B6RqzqZP3KkQRz1XEN1%2BVDS8AsTfgQw%2F%2FGgzAY6pgGMrNnRfNoEXBCd5CQ%2BKUHigWSJGhNCXvwO3uHbLHSo6vrO%2BpZw05bedr1YGUC8vYFgdk%2BXPsUXEsCHad90xyEyO2k9053JYCtgcUALPSgsWVGNxv2Yg3oZmw5FmX17xpDxVUgIrguvfybYC2MVb%2BUvHC7JU1eUWFhix7SyWkNGyevQhQxfNjKRXHQHdtI5YypCiJU9UMSCDtFFmeV2%2BSdO3EkxeNLP&X-Amz-Signature=a54c5da437595faf810380b5502b34b644e8f84f0ad93f857ec07c45c6e93283&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







