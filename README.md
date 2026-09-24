



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SORH2KBE%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T002004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIFYsr1hcSHpkMyFXvmq6%2B4BO%2FpVkAR46ox5YzNLzFDoUAiEA4l0yDVlXvIiO7YOFr9qRADg%2F%2FV0mRm%2Bj5MZ%2BxkCYZDkqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHy41vSREofFf4B5HyrcA0f1P38a%2FbtRX%2FBrI4YzKzC2X2nfY3%2BwgU35DiZNDt4%2B%2BQq4chSUUgUq13FWH9qpVzVRktdGORYJsrS2ybhzHCxNNnoOs1jPTTG9xw9aHVAzNpogzrSIJHZO%2BwD9MUEcLiyIKqI5c7W%2BVNkFIts5q8F%2B8r97xAUyIVQV0Yz7rJ0UC8s7DQyWNLwJSFyHl9RHeiLTIn1LmkBwDUHdixxr8gcq%2BQR7V1NOKAd1j1EfVLHsZ2yZNIfM69WJwl%2FpwCtqfuS6N1COsGmpRt7jVSPKdLXW3UwCu%2BMlD%2BdJmjH4HolrzdOyZOayK2B0ohYJ8RzE0%2FGN6er%2BeY6LNWI%2BwDggjh9gkfWKWchkVKUyuA6fZbMFL4Bkc15eTFnMdhZVbJKr7Ly2svIWJwyJyVbl9Drzpumx07Wdt%2BGJvjaYg63UtBp%2BOwxBrqEfKuu2ENjN3duLy9T2Z%2FM8P8eKAtcokHLOGqOXcCiOhb%2FW7wlKaC7F1GVblY%2FpzSveLNyPCwRltopXBWXfb80I5bmxp9ycFms34Gmrb40DksRLks1GJ%2FKOwqw0sjVhspdvyoND36%2FYuCnvsfBTQgFBkwL1WZE6woY9OjAOSv313lvUifx%2FDXDIHioGgHo05PTKcFR%2BMMWvMLvO0dUGOqUBEtQeXPaHbdg23MFNVDfjzA0CGjkWjRMJusphkNzqoyPYK4LCwKNX%2B1HB0WxuCOHTeDlo7tmEy8LZMO3gZ7QdKnf78zxIQ2Fx2uz%2Bm%2Bh43YGy1Us%2BEOdcB0L5wGrbshR6xc0OTmViB06os3IFlOl5aA1w0il96zbTTIcRYpY28g2RW8WfaEOV5JvL8veu%2F2fI32bvNHTvupZJryce%2F3yb5sjNMXBf&X-Amz-Signature=ab7ef8fbf285dbdc3d0e4383a4205ec5c91b67f8e1aab1e8462960717ab062c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SORH2KBE%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T002004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIFYsr1hcSHpkMyFXvmq6%2B4BO%2FpVkAR46ox5YzNLzFDoUAiEA4l0yDVlXvIiO7YOFr9qRADg%2F%2FV0mRm%2Bj5MZ%2BxkCYZDkqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHy41vSREofFf4B5HyrcA0f1P38a%2FbtRX%2FBrI4YzKzC2X2nfY3%2BwgU35DiZNDt4%2B%2BQq4chSUUgUq13FWH9qpVzVRktdGORYJsrS2ybhzHCxNNnoOs1jPTTG9xw9aHVAzNpogzrSIJHZO%2BwD9MUEcLiyIKqI5c7W%2BVNkFIts5q8F%2B8r97xAUyIVQV0Yz7rJ0UC8s7DQyWNLwJSFyHl9RHeiLTIn1LmkBwDUHdixxr8gcq%2BQR7V1NOKAd1j1EfVLHsZ2yZNIfM69WJwl%2FpwCtqfuS6N1COsGmpRt7jVSPKdLXW3UwCu%2BMlD%2BdJmjH4HolrzdOyZOayK2B0ohYJ8RzE0%2FGN6er%2BeY6LNWI%2BwDggjh9gkfWKWchkVKUyuA6fZbMFL4Bkc15eTFnMdhZVbJKr7Ly2svIWJwyJyVbl9Drzpumx07Wdt%2BGJvjaYg63UtBp%2BOwxBrqEfKuu2ENjN3duLy9T2Z%2FM8P8eKAtcokHLOGqOXcCiOhb%2FW7wlKaC7F1GVblY%2FpzSveLNyPCwRltopXBWXfb80I5bmxp9ycFms34Gmrb40DksRLks1GJ%2FKOwqw0sjVhspdvyoND36%2FYuCnvsfBTQgFBkwL1WZE6woY9OjAOSv313lvUifx%2FDXDIHioGgHo05PTKcFR%2BMMWvMLvO0dUGOqUBEtQeXPaHbdg23MFNVDfjzA0CGjkWjRMJusphkNzqoyPYK4LCwKNX%2B1HB0WxuCOHTeDlo7tmEy8LZMO3gZ7QdKnf78zxIQ2Fx2uz%2Bm%2Bh43YGy1Us%2BEOdcB0L5wGrbshR6xc0OTmViB06os3IFlOl5aA1w0il96zbTTIcRYpY28g2RW8WfaEOV5JvL8veu%2F2fI32bvNHTvupZJryce%2F3yb5sjNMXBf&X-Amz-Signature=d278f580cc4a95cbd3acd27e59c8b8ad261147ba68d2806afef1264175e1b8fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







