



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V77KIOAN%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T123558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICylTdZZI%2FpOfdfL%2BvEoS%2FdWyGbe9i%2BesD%2Fo%2BRA2cnUzAiB5TY0wgFGZfA6Q5HOZa%2F8KHMAHUovwhnMEl%2FYKtMRFEiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmuE%2F4ftafY21T6IdKtwDe11kpJATlEAYisg%2FwP9PZ%2FZNPtvfwBsyAP516P1NiWmh2cc%2FiZznsxco8KT%2FG4SsMFITjhGpvgkojYqXV7JRlhAsYRw4VeSewa5eEedOVwTp70mWmPc2sgg%2BndJwBgcKkHlE0uTBv4csFysdeeqXJJAWHSnIPhBPdijFnN9C2WqV51Dbab66ylkYIHT6yJP1DCBVRafaFoJp70hhQukS8hxf4TbWApQHOHRGhSi6kKfUicBD9G7pzI1BUg%2BJoPQt6b%2BGuiyAWGUtJK4u2U6ZU69Ui1sW2IjWaAmvLOAHBbc1b10jZLpaQLsuhrTE5UsiDn46ReNw8aW7N60%2F7fH8aFIlYBFM7H9%2Brzx%2BWvBXil3%2Bwc1HDEFPGP34zqyKsdd%2BW0b19REVouW27YQCzeUG0Y1KDfc1moTveVaTarErI%2BvpAFMK%2FXlOt%2FQdn59tB824ctAFkBeX%2FDgpoDk1JP0of7mx%2Bt897zFFJkWJAnaYgwf57kgoqo07G7%2FI87hEVx7JRdaExpKT2mOoUAYGNjkbQqrmri3iZ2NL2fUu1BPHAElv387Ob%2FFwElBwdUBJAhM5qWi0fLGg2tRTUYA6Bs8V0j%2Fx%2BwO3NZLX42ZaLv1AqK%2F2RuKArks5JMldo0gwgq6b1AY6pgGQ5riLlA7Gw7%2ByI5W1lz6x3ehw4tRvgHgi7VYHTlFBcWpIk1E3gV%2BrLSljyVzIZbHoN18Uswui0uUKhvCdu32bwxRdfJUco2%2FNx6%2FrmlkOS6dOE1gnnD2%2FW2MWr8zU%2Fno9qWyNf46IKOfjql9BPK%2BsPtbErhfGJd69KPja9rF6UEiZ8r8FMmVnBFaA%2Bu1V0Yq5lNQJSh3u%2Bz83COQh87b3K0ac56T%2B&X-Amz-Signature=dfd298a1c961cb3f8d3251ef5aa7d58cd00a69992f57370237518440022090bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V77KIOAN%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T123558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICylTdZZI%2FpOfdfL%2BvEoS%2FdWyGbe9i%2BesD%2Fo%2BRA2cnUzAiB5TY0wgFGZfA6Q5HOZa%2F8KHMAHUovwhnMEl%2FYKtMRFEiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmuE%2F4ftafY21T6IdKtwDe11kpJATlEAYisg%2FwP9PZ%2FZNPtvfwBsyAP516P1NiWmh2cc%2FiZznsxco8KT%2FG4SsMFITjhGpvgkojYqXV7JRlhAsYRw4VeSewa5eEedOVwTp70mWmPc2sgg%2BndJwBgcKkHlE0uTBv4csFysdeeqXJJAWHSnIPhBPdijFnN9C2WqV51Dbab66ylkYIHT6yJP1DCBVRafaFoJp70hhQukS8hxf4TbWApQHOHRGhSi6kKfUicBD9G7pzI1BUg%2BJoPQt6b%2BGuiyAWGUtJK4u2U6ZU69Ui1sW2IjWaAmvLOAHBbc1b10jZLpaQLsuhrTE5UsiDn46ReNw8aW7N60%2F7fH8aFIlYBFM7H9%2Brzx%2BWvBXil3%2Bwc1HDEFPGP34zqyKsdd%2BW0b19REVouW27YQCzeUG0Y1KDfc1moTveVaTarErI%2BvpAFMK%2FXlOt%2FQdn59tB824ctAFkBeX%2FDgpoDk1JP0of7mx%2Bt897zFFJkWJAnaYgwf57kgoqo07G7%2FI87hEVx7JRdaExpKT2mOoUAYGNjkbQqrmri3iZ2NL2fUu1BPHAElv387Ob%2FFwElBwdUBJAhM5qWi0fLGg2tRTUYA6Bs8V0j%2Fx%2BwO3NZLX42ZaLv1AqK%2F2RuKArks5JMldo0gwgq6b1AY6pgGQ5riLlA7Gw7%2ByI5W1lz6x3ehw4tRvgHgi7VYHTlFBcWpIk1E3gV%2BrLSljyVzIZbHoN18Uswui0uUKhvCdu32bwxRdfJUco2%2FNx6%2FrmlkOS6dOE1gnnD2%2FW2MWr8zU%2Fno9qWyNf46IKOfjql9BPK%2BsPtbErhfGJd69KPja9rF6UEiZ8r8FMmVnBFaA%2Bu1V0Yq5lNQJSh3u%2Bz83COQh87b3K0ac56T%2B&X-Amz-Signature=824d895f6a3cdb24180e226b71aa47f3825062e71deeeaddcba836c5813230a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







