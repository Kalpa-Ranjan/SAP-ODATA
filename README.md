



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQEOMI2N%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T075459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEK0kIOT7tAa20W2VTucSCFFcOmb2H6cCbNVyidSJ%2B0AIhAK%2FWe0eaQpds01f3pvlEEb4bY9Au%2Brn6s5M99w5mngpJKv8DCHAQABoMNjM3NDIzMTgzODA1IgwOHmw0S6uk%2FUjlPgsq3AOWY1VwYUnSx61%2FtyII4WZHi8EQ9399by%2FlWp5xePpjNlO6mI8Ey6K3GI%2Fi0s%2BDzqKV27w3V%2BwGhS8Om%2FhXDat5MeYJ4sagoHKb3L5oCnh5bbJDp6nhBJyNXm9j7UfHrpJE6z1WS5gnzw%2F%2FTXSxzS06oAjdcE2xoi6zJUx7BoDR%2BIUYQp9f31eH9MCP4UYYD3wjBNaGTe01St5q%2F8rezk%2BehrqPsZF3KwY4i%2FfaxmaxSARNGc4vMUl2wl%2FaJhNgKLTfV4fO9DTili9atCzjLyz%2FS3XBfoJbO9CmhqvYEtaj%2B91uAgMA0hpUeqZaRvKzHPLyGSyakPzZcxwpZY9k6VTJptxTw54BiYBCWd%2BkaHuKR4qIKwU7NXk5kQVcABcCbES7Yp7mOuTXl8whjg462%2B2JsCBkWcpzp6fawlKKjyZ4ei0YL6P46aiXvoMzhvo0QlXuCLP1SYGFN4B5hiBDY5H0A0F1YSedCDtM7tldopfWf4tGCk3kFcvNtVToMSfGtYqsEzbePmcRu%2FnDjGOmMq4lZa49TUi%2BywbCRAoE5QKeLRrGdroy9X9gsGq6U9MsV4hhqwYbq18H80FBPQsr2X31jPTRcxDwa%2FFDjRJmtq%2F6mQRzDGeMSDAXGB44wjD7mPLOBjqkAZatqnn0XICuY9wrqJ9VvtY2DSEpyiNr%2BKInI52%2FaRkQOL22iytoD%2FXcWsH30SblbgpLm4aB6SnikupqhLo0b7nk8N2%2F7dI80naETpEXX1%2FORWT62P9ZrVGcZYQNqQaCCsAnYZCp0RyW4NCuBX0bpFFB1iB7a0yAaHajS6X4f3%2B595eTzN4jjk%2F3K0kM5lvGZwgDkUmXYgMuD7fLO4b7bFGKCmmg&X-Amz-Signature=8407877f3f823b0bd849be8e05c41e3e8bdddf066e56fe6bcf50e399d4397894&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQEOMI2N%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T075459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEK0kIOT7tAa20W2VTucSCFFcOmb2H6cCbNVyidSJ%2B0AIhAK%2FWe0eaQpds01f3pvlEEb4bY9Au%2Brn6s5M99w5mngpJKv8DCHAQABoMNjM3NDIzMTgzODA1IgwOHmw0S6uk%2FUjlPgsq3AOWY1VwYUnSx61%2FtyII4WZHi8EQ9399by%2FlWp5xePpjNlO6mI8Ey6K3GI%2Fi0s%2BDzqKV27w3V%2BwGhS8Om%2FhXDat5MeYJ4sagoHKb3L5oCnh5bbJDp6nhBJyNXm9j7UfHrpJE6z1WS5gnzw%2F%2FTXSxzS06oAjdcE2xoi6zJUx7BoDR%2BIUYQp9f31eH9MCP4UYYD3wjBNaGTe01St5q%2F8rezk%2BehrqPsZF3KwY4i%2FfaxmaxSARNGc4vMUl2wl%2FaJhNgKLTfV4fO9DTili9atCzjLyz%2FS3XBfoJbO9CmhqvYEtaj%2B91uAgMA0hpUeqZaRvKzHPLyGSyakPzZcxwpZY9k6VTJptxTw54BiYBCWd%2BkaHuKR4qIKwU7NXk5kQVcABcCbES7Yp7mOuTXl8whjg462%2B2JsCBkWcpzp6fawlKKjyZ4ei0YL6P46aiXvoMzhvo0QlXuCLP1SYGFN4B5hiBDY5H0A0F1YSedCDtM7tldopfWf4tGCk3kFcvNtVToMSfGtYqsEzbePmcRu%2FnDjGOmMq4lZa49TUi%2BywbCRAoE5QKeLRrGdroy9X9gsGq6U9MsV4hhqwYbq18H80FBPQsr2X31jPTRcxDwa%2FFDjRJmtq%2F6mQRzDGeMSDAXGB44wjD7mPLOBjqkAZatqnn0XICuY9wrqJ9VvtY2DSEpyiNr%2BKInI52%2FaRkQOL22iytoD%2FXcWsH30SblbgpLm4aB6SnikupqhLo0b7nk8N2%2F7dI80naETpEXX1%2FORWT62P9ZrVGcZYQNqQaCCsAnYZCp0RyW4NCuBX0bpFFB1iB7a0yAaHajS6X4f3%2B595eTzN4jjk%2F3K0kM5lvGZwgDkUmXYgMuD7fLO4b7bFGKCmmg&X-Amz-Signature=1eb89b719d34c8145b4d2efb3f8b3f4256eb225aae41a71ba98e5b8a3561fddf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







