



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLZM2ODY%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIF3ZySsXMSDxO1sJihF4N61t2spJtE6lc0X6zJDChe6AAiBjlhE7QbabKMun9lOW0g7py%2BSjhR2GNTlJQYV0ikguwSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpVSjyaRGaD8dykTbKtwDi2wGb5EoFIB3EYi42LsQ8FYFxcc0Olq0Wfiw4d0Zr97Xcq270Z5Tq%2BlDb3%2FlCcbBoyOqk%2BbI8ogPeAARE%2FqJBvvgGiAxgtV2x0w1empd6cjX%2F%2FpClTAyaDfGCfTnwSCpLtuwD0KY8b7N0vH2p292YQvwyjSOkQac27v08DxKEGZnECkCz7rIM9md2NdsAceWekM5SPxrHfzVJR698e34hreJmUADSE0USqMBy1YaYl32VYpUfEKfyAC17ban0csL4T436SgDxM5fOkwkkzN6gjVjaEkGNlA78i1xBdrv9RxXEldZsOyQGJiejlk5rpTI2SGtumiyvcXfRDkotqlbq%2FG%2BF5v0hURK%2Bz2wSeqOssEL8dGfBtOSkqfHhfQ3FqKjG12WF%2BueuidMc%2F4C2Vonz8BkTEr5qYX3S4rCUOj%2BdEfmGN%2B90ZxcEvp8fIu268t4qk0Mp38rNMEcMphvWa%2FD6QE%2B1N%2BUjalFnw8czEof197XDM%2FkLUGLlqpqnCqBcguPzxqF6Ttbh%2BbTj6VN%2FrbZ27ELYx1M4nviBrCiR63phBEC3AwO%2BKExBb1F7Q%2F%2FOG7Yoju6tH1EEfF8s%2BOkEQpD3XIHudYq9s3EU9ZRcNyIp5iZcfl9bYvg06eNfREwvNjFywY6pgEgvDtfHcXKWjyLgWJo11H2bLExEbgogcDUi2%2BTsdbnzmxYblli0GB5n4BTDgn1F1kuXAgLN7CcQUvfFmOh81e5XBvj%2F7lUhylWoNR1gZ7DCfkO9s2FY9Esno5rrXgqKxApomx%2Bfkz%2Fw7qFLp9zq3tTj2ghDv8v7GjIrdmqfb8Ih%2FS7GjLE2i0j3slHZCUYRaOV3klfIkt%2FuAsm7T9PU%2FnHL6e%2B8qBY&X-Amz-Signature=b0b3d2164dccbb39877ba705fcc1f332227432d639d974106955f1e449a8e53e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLZM2ODY%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIF3ZySsXMSDxO1sJihF4N61t2spJtE6lc0X6zJDChe6AAiBjlhE7QbabKMun9lOW0g7py%2BSjhR2GNTlJQYV0ikguwSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpVSjyaRGaD8dykTbKtwDi2wGb5EoFIB3EYi42LsQ8FYFxcc0Olq0Wfiw4d0Zr97Xcq270Z5Tq%2BlDb3%2FlCcbBoyOqk%2BbI8ogPeAARE%2FqJBvvgGiAxgtV2x0w1empd6cjX%2F%2FpClTAyaDfGCfTnwSCpLtuwD0KY8b7N0vH2p292YQvwyjSOkQac27v08DxKEGZnECkCz7rIM9md2NdsAceWekM5SPxrHfzVJR698e34hreJmUADSE0USqMBy1YaYl32VYpUfEKfyAC17ban0csL4T436SgDxM5fOkwkkzN6gjVjaEkGNlA78i1xBdrv9RxXEldZsOyQGJiejlk5rpTI2SGtumiyvcXfRDkotqlbq%2FG%2BF5v0hURK%2Bz2wSeqOssEL8dGfBtOSkqfHhfQ3FqKjG12WF%2BueuidMc%2F4C2Vonz8BkTEr5qYX3S4rCUOj%2BdEfmGN%2B90ZxcEvp8fIu268t4qk0Mp38rNMEcMphvWa%2FD6QE%2B1N%2BUjalFnw8czEof197XDM%2FkLUGLlqpqnCqBcguPzxqF6Ttbh%2BbTj6VN%2FrbZ27ELYx1M4nviBrCiR63phBEC3AwO%2BKExBb1F7Q%2F%2FOG7Yoju6tH1EEfF8s%2BOkEQpD3XIHudYq9s3EU9ZRcNyIp5iZcfl9bYvg06eNfREwvNjFywY6pgEgvDtfHcXKWjyLgWJo11H2bLExEbgogcDUi2%2BTsdbnzmxYblli0GB5n4BTDgn1F1kuXAgLN7CcQUvfFmOh81e5XBvj%2F7lUhylWoNR1gZ7DCfkO9s2FY9Esno5rrXgqKxApomx%2Bfkz%2Fw7qFLp9zq3tTj2ghDv8v7GjIrdmqfb8Ih%2FS7GjLE2i0j3slHZCUYRaOV3klfIkt%2FuAsm7T9PU%2FnHL6e%2B8qBY&X-Amz-Signature=426232266b9b606b0576f762572852a32d07b6c5d1bf6678ebe249cc7470150e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







