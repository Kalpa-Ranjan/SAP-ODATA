



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTO4WTUJ%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T182600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5Ofx9OzMj0afdtYtpGB5zuvv%2B6HgkVPSP8vxhgczgGAiEAjajqNHTFDNlp29ITVOSdPfjpipC6XRipnMC86Yo4rr4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEmdUHXCNArOktU%2FmSrcA2E1x67Xlmnq%2BXYOfd6YT%2BaSQmBYUZk1X3a4U9ZgKhnCjF9cct6LSGsHAXwVk42HW1MPoRC9bdXRO6K0Xs6JMfJI7wzoLxkhdJ%2FCsEXnoU4dpDuEzMj5kcYK7M4xFyX8xNx7fdBoSD6v387pdKVB2mxc%2FvL03vKWX2AoIlbaMd7xoz4Dv07ZDsmnujdCGsr6qZGBvzpn1rUu3%2B9dV%2B8v%2FEe16UhCDzhsSpTbk%2FFmF1KSJfaJajbzBQle5eKXHBr4qVQnruDFVuVB9ZKWTShTpVOtWnzqP6WtLSwBLTdcy6lk%2FOnUI4bw7RJzVeKf%2B7Spaca3lakrqNkGunJdSNiNL%2FH2KkQQEdQIVIur4EI3KRV1MXLbSSOi2je%2Fz4L9DC1jrmFJNZ4tMJLNvADNGH3tiO5g6XcHK2uUlzJ3G%2BCSnc6JDQgvor1YtEkBlYs0FA1IQPm5cuiqSpjE0NY43CtJW6HwZzoBvcPPXyqbJx5xKvS2ibq5P1DXB%2FWmz1QHhLJjt8ofGfp0JO4908%2BqF31B7aStltgTJomf%2BT5OdtIJhRSo9hLS2bSeB1ReESZp4SyfFMF0HdkPnEobxw86dZXQH0A2gsuvo60tlhcuWNxptXJKvCAqxQDhl4%2FkDiuXMIufi8oGOqUBDsEjJ5ZEufClOcmpVTw%2FzNIQarDMKlXCwE73Ax82k90%2FhWl%2B2eqv6chdMXAt7P67tTwyueZfXZ7AoWjgUU0dS1X9Wl%2BnPL7xIDVqFkbAp%2FPQ6vT0vDPYo1hy2bwdOzTcHRiFWtJqYfQa4Eqg5Y%2FjobhmX88rwPNYUcj6E6iwf2U5%2BA%2B52B2%2FYXKkbjpcdtCoIXpj3pVHyJIsrYXgXc%2F6nfZevWUl&X-Amz-Signature=bc6baff4538a92615b202b7c0e6e100b8beb787b0b3903fc954a1491d1d02d50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTO4WTUJ%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T182600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5Ofx9OzMj0afdtYtpGB5zuvv%2B6HgkVPSP8vxhgczgGAiEAjajqNHTFDNlp29ITVOSdPfjpipC6XRipnMC86Yo4rr4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEmdUHXCNArOktU%2FmSrcA2E1x67Xlmnq%2BXYOfd6YT%2BaSQmBYUZk1X3a4U9ZgKhnCjF9cct6LSGsHAXwVk42HW1MPoRC9bdXRO6K0Xs6JMfJI7wzoLxkhdJ%2FCsEXnoU4dpDuEzMj5kcYK7M4xFyX8xNx7fdBoSD6v387pdKVB2mxc%2FvL03vKWX2AoIlbaMd7xoz4Dv07ZDsmnujdCGsr6qZGBvzpn1rUu3%2B9dV%2B8v%2FEe16UhCDzhsSpTbk%2FFmF1KSJfaJajbzBQle5eKXHBr4qVQnruDFVuVB9ZKWTShTpVOtWnzqP6WtLSwBLTdcy6lk%2FOnUI4bw7RJzVeKf%2B7Spaca3lakrqNkGunJdSNiNL%2FH2KkQQEdQIVIur4EI3KRV1MXLbSSOi2je%2Fz4L9DC1jrmFJNZ4tMJLNvADNGH3tiO5g6XcHK2uUlzJ3G%2BCSnc6JDQgvor1YtEkBlYs0FA1IQPm5cuiqSpjE0NY43CtJW6HwZzoBvcPPXyqbJx5xKvS2ibq5P1DXB%2FWmz1QHhLJjt8ofGfp0JO4908%2BqF31B7aStltgTJomf%2BT5OdtIJhRSo9hLS2bSeB1ReESZp4SyfFMF0HdkPnEobxw86dZXQH0A2gsuvo60tlhcuWNxptXJKvCAqxQDhl4%2FkDiuXMIufi8oGOqUBDsEjJ5ZEufClOcmpVTw%2FzNIQarDMKlXCwE73Ax82k90%2FhWl%2B2eqv6chdMXAt7P67tTwyueZfXZ7AoWjgUU0dS1X9Wl%2BnPL7xIDVqFkbAp%2FPQ6vT0vDPYo1hy2bwdOzTcHRiFWtJqYfQa4Eqg5Y%2FjobhmX88rwPNYUcj6E6iwf2U5%2BA%2B52B2%2FYXKkbjpcdtCoIXpj3pVHyJIsrYXgXc%2F6nfZevWUl&X-Amz-Signature=3fcdd0a7797c0d2a5f508d65b38d1ef04d8150345128d466fed51967de227a40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







