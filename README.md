



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBWTWFPA%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T020623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC5SU6K40KW%2BH4FzMrx%2FBLp9Oq59OLmqzAh2bhqVz0PiQIhAPCfEVJlISnpBKxZ8%2FtFNmyU0y5ctC1aPGbecbg7z9TnKv8DCCsQABoMNjM3NDIzMTgzODA1IgyH88VHqfmZzmBhMboq3AN7tridqSO27kxO9P1i49ZtUzNQ43%2FyynFTzpetK%2BjUf%2FU0LlOOqXyyLS3NcGoMAA8HwRjIjf7UVhSU4SBY%2Fk6UmLnvzSfUcPd6I%2F86RmLnsFugvwQVW5ZxobewcpidjW52ZneR2wADLAnY3bfhYJhiTIzFi5rf5ltu7vQdCXWs2h5qF61LWuT%2F2aynbbCtugXVzEPLRyIRihfMRbYlebMjy8FeVA4XmFEDGFLkDy8E9CPaNLXZq5r91yRRybf2Z7QMEnYzZ3ILHOCVyseK3F%2BxJtEdCRVOEgf9Xp3flVv2G%2B8B1k9Tf9D4z24MItl7P0ugzBKbs0VmCRo%2BvgDtEOKXQU24EdtjzgAKR%2FKs%2F46bU7GQx%2BfnGK%2Fs1p6aCyT9iRBPcg7S4BT5IxsnmnzVIF%2FGeMiaH6G8a1JBv3n%2FafioPo%2BW0JC3l5rej4URhvwAfIWrBJXazZQWJ5zB13ga3G2GHEeBEZz23WhmUKW1vdUzyq6DFZquwcQYXQfaoOA7dpeoRs%2FnY%2BnTSOtZFTHkhhhSSiNDQHCAw0UKx%2Bpjv6E0leR5PUF4nfAEAFDPN8N4Y8oo7P9Z3ciWMsoRIjFg8st0aF0NoihnMf2%2FQW%2F2tdOKsvwOU%2FklX8fM52HlQTCZqpvPBjqkAU2ZGdwacDNMNhSG%2B2nP6QTVDIf0Ia3RRCAkODRjlTZWsjvGZlEDASWG8rwupPDnmWcHDqunPR0%2BLZLc%2BZEXZ5g2fL7DJMVD75qL5beem64s12Oe9UPny9h97M%2Bt4mq9WS0yfCJEpwJ2pNqc2UP382ZUYHy3oI3yDcF1pBIr3cEidZ7P7ZI2RNGimiiMjdaZa%2BFcedB02gAojNUzglj6BuF6yYdH&X-Amz-Signature=8223a59618dbad2f2e9f656e0583baca7eb78d77b9c77883c432d34bd8940969&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBWTWFPA%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T020623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC5SU6K40KW%2BH4FzMrx%2FBLp9Oq59OLmqzAh2bhqVz0PiQIhAPCfEVJlISnpBKxZ8%2FtFNmyU0y5ctC1aPGbecbg7z9TnKv8DCCsQABoMNjM3NDIzMTgzODA1IgyH88VHqfmZzmBhMboq3AN7tridqSO27kxO9P1i49ZtUzNQ43%2FyynFTzpetK%2BjUf%2FU0LlOOqXyyLS3NcGoMAA8HwRjIjf7UVhSU4SBY%2Fk6UmLnvzSfUcPd6I%2F86RmLnsFugvwQVW5ZxobewcpidjW52ZneR2wADLAnY3bfhYJhiTIzFi5rf5ltu7vQdCXWs2h5qF61LWuT%2F2aynbbCtugXVzEPLRyIRihfMRbYlebMjy8FeVA4XmFEDGFLkDy8E9CPaNLXZq5r91yRRybf2Z7QMEnYzZ3ILHOCVyseK3F%2BxJtEdCRVOEgf9Xp3flVv2G%2B8B1k9Tf9D4z24MItl7P0ugzBKbs0VmCRo%2BvgDtEOKXQU24EdtjzgAKR%2FKs%2F46bU7GQx%2BfnGK%2Fs1p6aCyT9iRBPcg7S4BT5IxsnmnzVIF%2FGeMiaH6G8a1JBv3n%2FafioPo%2BW0JC3l5rej4URhvwAfIWrBJXazZQWJ5zB13ga3G2GHEeBEZz23WhmUKW1vdUzyq6DFZquwcQYXQfaoOA7dpeoRs%2FnY%2BnTSOtZFTHkhhhSSiNDQHCAw0UKx%2Bpjv6E0leR5PUF4nfAEAFDPN8N4Y8oo7P9Z3ciWMsoRIjFg8st0aF0NoihnMf2%2FQW%2F2tdOKsvwOU%2FklX8fM52HlQTCZqpvPBjqkAU2ZGdwacDNMNhSG%2B2nP6QTVDIf0Ia3RRCAkODRjlTZWsjvGZlEDASWG8rwupPDnmWcHDqunPR0%2BLZLc%2BZEXZ5g2fL7DJMVD75qL5beem64s12Oe9UPny9h97M%2Bt4mq9WS0yfCJEpwJ2pNqc2UP382ZUYHy3oI3yDcF1pBIr3cEidZ7P7ZI2RNGimiiMjdaZa%2BFcedB02gAojNUzglj6BuF6yYdH&X-Amz-Signature=2acf1c908c4cd4d9aa11c67f2d4076099de422897976f4a574e8c3fab3bd5d0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







