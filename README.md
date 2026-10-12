



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB7T3D2I%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T121643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0b09XhiJeGN9pkkuxCDKGsW6hgkb0t6tbyNdH5PYAkAIhAKr0LV70Q%2BqOhzu0L%2FTAijpGXWoHQx3s9%2B%2FDsG%2BcanGlKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmWZ%2FFLbnnWEsOLTgq3AOOhUdJ9QXzlp8q16O0oYfQDVPuI93%2F09m57RlRHrUurJ7WtZLgRcHIoaA4mG0WaLzFcwaL5opHND3mKZnA%2Bm3%2BJYLvCl2jQbhNNfdBaQlzVdzQ1rZLV4LLiSktpf0l7vvkIy9TnWEnXJa%2B74%2F4H6GFGXmSONSaXXUW0u1nRM5O6rWEqLeVRM9Ld%2BajdD2EILjs0406%2F%2BSvAacUUzGBVPNUAkdFcm%2FhYr6k6a66qegw2dRNLb8yDMxIopL1BpB0LNGaZmNYCDyMlj9KXZwq%2F1xwERZoXY1bOENHIpHrBmx78Jl4vI8PDL3pcTAut9GjYsEfSQkoPtdV8fX9SzX6UAaCSXVZ40fP9AzkrjU5QvNzejdluj6fXHVffuAvSAKsjMXrTPng1EjF84bLFxGi%2FycQJmo9AjYuT4GEZURImLUHuTw%2B1WeTWLC6IHSZk%2FJQvCUXt5sIzqssjosyN1gNJfDH37RHA1chfFO%2BYT2P3iHok1AZ1KY%2FRwsB%2FpCFELVyWfitZOuW8y9bK0k2P5C4CiQiRsgiecCMOzfkMDRTd9SZYNG8w%2F%2BH0jWOG2gFie6mjk3%2BRDv2igtj5FMBYhWTy5gd4waPDXlcezOg696O66UGRjImzzrEJHLONFNrXDCk7rLWBjqkAQB6L6g8c6zVd5%2BPcy9dB%2BRb0DjACDIfq7iI5euKYV5JJfUK%2FJElm756kbzRIdN5vFqWcYIE%2F3vT0aBgq2fSInNEhlXzeJQjhoCcBv7kzF9hvN3OzbdQB8BOlISna1x1gEykPjHGRhK7f009zNm%2FPKLOTAAp7gf8TaVoZ5GZULxT02nnNwNkSaJh46s82tTKFJr8FWeeLK%2B5PnCbUFZ0SMb3hfKy&X-Amz-Signature=cde7d8a3110b7f3c41133a286ce0930cc611290e51eea67f53016500615fc151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB7T3D2I%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T121643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0b09XhiJeGN9pkkuxCDKGsW6hgkb0t6tbyNdH5PYAkAIhAKr0LV70Q%2BqOhzu0L%2FTAijpGXWoHQx3s9%2B%2FDsG%2BcanGlKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmWZ%2FFLbnnWEsOLTgq3AOOhUdJ9QXzlp8q16O0oYfQDVPuI93%2F09m57RlRHrUurJ7WtZLgRcHIoaA4mG0WaLzFcwaL5opHND3mKZnA%2Bm3%2BJYLvCl2jQbhNNfdBaQlzVdzQ1rZLV4LLiSktpf0l7vvkIy9TnWEnXJa%2B74%2F4H6GFGXmSONSaXXUW0u1nRM5O6rWEqLeVRM9Ld%2BajdD2EILjs0406%2F%2BSvAacUUzGBVPNUAkdFcm%2FhYr6k6a66qegw2dRNLb8yDMxIopL1BpB0LNGaZmNYCDyMlj9KXZwq%2F1xwERZoXY1bOENHIpHrBmx78Jl4vI8PDL3pcTAut9GjYsEfSQkoPtdV8fX9SzX6UAaCSXVZ40fP9AzkrjU5QvNzejdluj6fXHVffuAvSAKsjMXrTPng1EjF84bLFxGi%2FycQJmo9AjYuT4GEZURImLUHuTw%2B1WeTWLC6IHSZk%2FJQvCUXt5sIzqssjosyN1gNJfDH37RHA1chfFO%2BYT2P3iHok1AZ1KY%2FRwsB%2FpCFELVyWfitZOuW8y9bK0k2P5C4CiQiRsgiecCMOzfkMDRTd9SZYNG8w%2F%2BH0jWOG2gFie6mjk3%2BRDv2igtj5FMBYhWTy5gd4waPDXlcezOg696O66UGRjImzzrEJHLONFNrXDCk7rLWBjqkAQB6L6g8c6zVd5%2BPcy9dB%2BRb0DjACDIfq7iI5euKYV5JJfUK%2FJElm756kbzRIdN5vFqWcYIE%2F3vT0aBgq2fSInNEhlXzeJQjhoCcBv7kzF9hvN3OzbdQB8BOlISna1x1gEykPjHGRhK7f009zNm%2FPKLOTAAp7gf8TaVoZ5GZULxT02nnNwNkSaJh46s82tTKFJr8FWeeLK%2B5PnCbUFZ0SMb3hfKy&X-Amz-Signature=d25c05b2aa3d03e8200e1a9755690ec14ece511844fcb35fffc2bd0c13cc6707&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







