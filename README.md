



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WCW77KO%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T120712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBalF7OtANglhzZDmo1kYkpN7rVfd%2FKd6J1uPdCPQOBQIgSEzM6VjYVlAi2XDLB%2BNru1Dv5VRS3FHrAT3jkijUYKQqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtQvLkXf6NziXKlbCrcAwfH%2BZ0I1Fu6xtO9w8O4ZB3YUstNu%2FWN13QAXpaFIItIOZEJG0Mx2wIeyh9g0W%2FlgDx%2BUAjFj%2BJUeS62NKXu3%2Bc0HDbj%2BkQvFhT0nAEBxEGX1ze25Dt2oJlo4EUZpAfqlmzqbPesNnQ%2F5bb%2BMHzpzv875vJeI7wgca6CwLxVC3YJCLRDQyLYf0NKylceGIikrsTgaZJl%2F3VF5bQzyTpoLCxTlMWqacYB%2B%2FyfU1YrrOFEU2NJHvZ5LrhIEYeKtNZ72LUT2H43wsT7I1VMYNE8w47oDAE7q5J2v0vAjsfXXQiAXPHaNNYfIp5Rf3lw73YZCqo3djnMMYaxbjLbG8%2FX0h508MZfUxj%2BkFquXxeqkifjOD6xI8GFVwVhVq8sX1KPdoqsucaIU1jlg4x%2BX2PpDEHBsHlJLQPzqmm1YTFP8aFNo0ysKLcvOd6UKG3ebJiKr6cyp0Yg9o7mCZwOjQrLLhkqJ977mr6bP%2FXWez%2FvpscPOFOyap2l7zOAufPkzPdS0PetKjJXbUjxzLPCQ8ycqWWnc3rg8DCPdvt6CtvCxz%2BN6pLlrSmuJoe7EBE2%2BQHhi9n%2FJOCJgBS8Bh9%2FApmc40vuqOJ6mY1OSlkFZfQUzxdXSOs0iLYkBUjcdeQOMMKzrNcGOqUBx01%2BstRLlGDed14h2uvVAQxfapE1BFzJiGCr9ViXPeM%2FFun0oqPjgOANfThdIIVVqP9PNLoqx9rSIVe1nhB0Vts2yZoO0JQGPYJBC5D7R%2FXg7fGP8vvoGTLLWgBDML82SR%2B3iL8O11FnZ%2FuNP%2BEh4IVeeC7xyqJoQ99fMpfi5PNjC2ppJ%2FkZQp0DlSDZRRhoAuD59w8sn27UHQK1IksA30e6F9SB&X-Amz-Signature=11d9d39d35b5a552bb89a5d210eb22c7d042db8f2523dfcd1f2d9c54578926b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WCW77KO%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T120712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBalF7OtANglhzZDmo1kYkpN7rVfd%2FKd6J1uPdCPQOBQIgSEzM6VjYVlAi2XDLB%2BNru1Dv5VRS3FHrAT3jkijUYKQqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtQvLkXf6NziXKlbCrcAwfH%2BZ0I1Fu6xtO9w8O4ZB3YUstNu%2FWN13QAXpaFIItIOZEJG0Mx2wIeyh9g0W%2FlgDx%2BUAjFj%2BJUeS62NKXu3%2Bc0HDbj%2BkQvFhT0nAEBxEGX1ze25Dt2oJlo4EUZpAfqlmzqbPesNnQ%2F5bb%2BMHzpzv875vJeI7wgca6CwLxVC3YJCLRDQyLYf0NKylceGIikrsTgaZJl%2F3VF5bQzyTpoLCxTlMWqacYB%2B%2FyfU1YrrOFEU2NJHvZ5LrhIEYeKtNZ72LUT2H43wsT7I1VMYNE8w47oDAE7q5J2v0vAjsfXXQiAXPHaNNYfIp5Rf3lw73YZCqo3djnMMYaxbjLbG8%2FX0h508MZfUxj%2BkFquXxeqkifjOD6xI8GFVwVhVq8sX1KPdoqsucaIU1jlg4x%2BX2PpDEHBsHlJLQPzqmm1YTFP8aFNo0ysKLcvOd6UKG3ebJiKr6cyp0Yg9o7mCZwOjQrLLhkqJ977mr6bP%2FXWez%2FvpscPOFOyap2l7zOAufPkzPdS0PetKjJXbUjxzLPCQ8ycqWWnc3rg8DCPdvt6CtvCxz%2BN6pLlrSmuJoe7EBE2%2BQHhi9n%2FJOCJgBS8Bh9%2FApmc40vuqOJ6mY1OSlkFZfQUzxdXSOs0iLYkBUjcdeQOMMKzrNcGOqUBx01%2BstRLlGDed14h2uvVAQxfapE1BFzJiGCr9ViXPeM%2FFun0oqPjgOANfThdIIVVqP9PNLoqx9rSIVe1nhB0Vts2yZoO0JQGPYJBC5D7R%2FXg7fGP8vvoGTLLWgBDML82SR%2B3iL8O11FnZ%2FuNP%2BEh4IVeeC7xyqJoQ99fMpfi5PNjC2ppJ%2FkZQp0DlSDZRRhoAuD59w8sn27UHQK1IksA30e6F9SB&X-Amz-Signature=a214b10572bf1d5f8ea0c81b22ec64101a6f6b07a04dc398d4ee59aad61a206b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







