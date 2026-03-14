



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYYJU5IX%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T123928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBBuFEVzlg1corioqbv57fNv9UGNHb6GRKNrealh8FjAiBKnu90dIrn%2BahcoGAFyRhqrYpvhYtKDWPwmBs948Y8aCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaukx4ATVULdx8jC3KtwD73cAiEE4KSguT7fCSEmKVKdhsUv2dpGnJSbmAq9Fai0sRIuinUFC9srId05nJrVcTJNq83F7r7vAevPW77fTE2R1kXj4NyloLbEB8xr2KXDt64t1AD7HzDF9b6CsOURNRv%2FcDhE1Y%2F%2F2Tq2D1e4xmS3gcyxY5lxr%2FNHwqwa8yyyvJ3jv3xHXFFMd0ycaEXp7Ym6BLXngmyoe%2FMc7FEbdM7Op5nE74PURWhoT%2BP0jag%2FQSOVgIJ07efwTOhFZ8RzAk41EEKfr%2BiVKNM4G14XsFWQk9Y%2BbAlnStyP909N3mI75M7FJI4DSXivEa5OFrIici2hHHrw4qmH0cyw4wRsTC5PAhVCn9U6DW%2FdbHFKwWmaOeiMk2uAzWk5lDVv9oBnukLNVKdsxHnWq1EL4D4iMnjqrCsrq%2BSLCsjiMwE9wAdrrmRwKmhOP%2BmIloHzKLadidlg%2BXvdydk0Tto5zrN%2BdjihvhnuuBtFZ8zp5xUd%2FyzOkqhtM15tgMomLqXCZH%2BbkDdHlClMIfv8Z6GE7G2u1ihqQuCJaprA0PgYQLIARKYcBRCpqiZ3O%2FDTa%2B%2F6NahtAA8ZbjnuVwXbLifToAYEyKQCmel%2FBwetjWsxvD%2BELZts3ZsWn3ITJGLvFiuIwi6nVzQY6pgG%2BRzFiOz2LxaHLWz4%2BW1wDJ3ROyQ49s41PorKGMBcEC%2FunUTLMBEhZUoWbwusNnuWO8%2FHN9zf%2FwjlDKqDYHDr1Kh%2BuwL5gMTyWwK5JSCWZi6Zei5%2FA6SXDkpC8Awjp5b4eSecbdRQFGwo0pct6ORV4XeXxTMqKQBjbYLsbXnLrvWDbP7izeXhcM50X%2FO74AnSwwJ5RHjQRKWrAZU7%2BbCLIEI34zQ5m&X-Amz-Signature=d0f1637f1f560d78408897487366649a0bcc7807ae863191fb48ffb888c8a4d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYYJU5IX%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T123928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBBuFEVzlg1corioqbv57fNv9UGNHb6GRKNrealh8FjAiBKnu90dIrn%2BahcoGAFyRhqrYpvhYtKDWPwmBs948Y8aCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaukx4ATVULdx8jC3KtwD73cAiEE4KSguT7fCSEmKVKdhsUv2dpGnJSbmAq9Fai0sRIuinUFC9srId05nJrVcTJNq83F7r7vAevPW77fTE2R1kXj4NyloLbEB8xr2KXDt64t1AD7HzDF9b6CsOURNRv%2FcDhE1Y%2F%2F2Tq2D1e4xmS3gcyxY5lxr%2FNHwqwa8yyyvJ3jv3xHXFFMd0ycaEXp7Ym6BLXngmyoe%2FMc7FEbdM7Op5nE74PURWhoT%2BP0jag%2FQSOVgIJ07efwTOhFZ8RzAk41EEKfr%2BiVKNM4G14XsFWQk9Y%2BbAlnStyP909N3mI75M7FJI4DSXivEa5OFrIici2hHHrw4qmH0cyw4wRsTC5PAhVCn9U6DW%2FdbHFKwWmaOeiMk2uAzWk5lDVv9oBnukLNVKdsxHnWq1EL4D4iMnjqrCsrq%2BSLCsjiMwE9wAdrrmRwKmhOP%2BmIloHzKLadidlg%2BXvdydk0Tto5zrN%2BdjihvhnuuBtFZ8zp5xUd%2FyzOkqhtM15tgMomLqXCZH%2BbkDdHlClMIfv8Z6GE7G2u1ihqQuCJaprA0PgYQLIARKYcBRCpqiZ3O%2FDTa%2B%2F6NahtAA8ZbjnuVwXbLifToAYEyKQCmel%2FBwetjWsxvD%2BELZts3ZsWn3ITJGLvFiuIwi6nVzQY6pgG%2BRzFiOz2LxaHLWz4%2BW1wDJ3ROyQ49s41PorKGMBcEC%2FunUTLMBEhZUoWbwusNnuWO8%2FHN9zf%2FwjlDKqDYHDr1Kh%2BuwL5gMTyWwK5JSCWZi6Zei5%2FA6SXDkpC8Awjp5b4eSecbdRQFGwo0pct6ORV4XeXxTMqKQBjbYLsbXnLrvWDbP7izeXhcM50X%2FO74AnSwwJ5RHjQRKWrAZU7%2BbCLIEI34zQ5m&X-Amz-Signature=f7de7b60694518f2f2817e2fbb381582bd0655e0a16e857e3816923a6e0200d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







