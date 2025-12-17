



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPMCUDVW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T123546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI0p2RZvw81bjEEIpe03EEcqxPBy4z7CZekFW433I50gIhAMbuMWu3L7aLhKwJrsLEOK9F9yekC1pug9cE7YAHogDsKv8DCH0QABoMNjM3NDIzMTgzODA1IgxjxZzYCqHMnAO9A7Aq3AMUsuXSq8qnyb9xntlJc45EI8adJ3FnOvEFm%2FRh%2Fo2PdwwMucY%2Fy4jXIZpXGAB3ETuxl4ESzxamQ9%2F6ZeKSr87RdlWH1%2FrZm9tDDeCzx1J%2BR%2Bc38KseH9fYUtVv05AL5ycXSViCXQZ%2B6JjGmCvogVJ1YwiZKgjcvtzqASjjbOWXco3Hkinp6AgzmtjEgJRzjheZbLn90IQ5DuPKOULFHEXlWLlqAthNY5ZgSPIfp4cU9nllO5Peya7Z4Uv1ZjAlrTjNrxdbIeV9onL0bQpgMAz9%2FDmCVaVlz7bjojVLHn21gk%2BRJ32OpQJ2OuMyOKbUSfMyM5mGpgZApycXqRzIxril%2BiFXYum6CSJhAh9PzXTB%2FAKGE%2BB5eqTHupeyBM5byv5j46UjBnspTMXR%2FVJi1NA2vWayjmPJgnW0GI1ZpbN74ZT4ouw1C6%2BsLYMLBqMELktK6SSzimIDPDJR6Z%2F60UXS0oz%2Bd1HhxDmugAXmfYD3OaV6DR581seiXU7EroTRc4pekzA0GBqBi1Z3f09AZOeCAZaHdmm7q2Qg98ZvVCF5gCO2E4gvLTannq%2Fh4PUyWQheRiVCQG3paWdbL6%2F1duZgQWB0YtEF1l0sUrs6c7yX5fH13%2BIeuTDj15WHnDCPq4rKBjqkAQIONWV19yUQ5Dj3xhJ8fqrl1QpWnnOotuMGWgSDRFOhpVDZ11XcPbYUcNY850fv05w%2FrWOvC%2FHukAUfFJK%2FH0OQTXw5Vfc7hhYhxAIa5qeuZJhr%2F7b2AVxFhUduOXddzL9dy4ThqQf3rF5ci9PSHB00hplNXmNegpYhg1W6Eyn%2BDfu9dco8KpF3VTWsH1up%2F9bcnVscliQaYp78rxaYhAXCDIj%2B&X-Amz-Signature=e42b03df43e679fed86324b48c02b0e0dd463e6ebe5c90038329820b9d0bc28d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPMCUDVW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T123546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI0p2RZvw81bjEEIpe03EEcqxPBy4z7CZekFW433I50gIhAMbuMWu3L7aLhKwJrsLEOK9F9yekC1pug9cE7YAHogDsKv8DCH0QABoMNjM3NDIzMTgzODA1IgxjxZzYCqHMnAO9A7Aq3AMUsuXSq8qnyb9xntlJc45EI8adJ3FnOvEFm%2FRh%2Fo2PdwwMucY%2Fy4jXIZpXGAB3ETuxl4ESzxamQ9%2F6ZeKSr87RdlWH1%2FrZm9tDDeCzx1J%2BR%2Bc38KseH9fYUtVv05AL5ycXSViCXQZ%2B6JjGmCvogVJ1YwiZKgjcvtzqASjjbOWXco3Hkinp6AgzmtjEgJRzjheZbLn90IQ5DuPKOULFHEXlWLlqAthNY5ZgSPIfp4cU9nllO5Peya7Z4Uv1ZjAlrTjNrxdbIeV9onL0bQpgMAz9%2FDmCVaVlz7bjojVLHn21gk%2BRJ32OpQJ2OuMyOKbUSfMyM5mGpgZApycXqRzIxril%2BiFXYum6CSJhAh9PzXTB%2FAKGE%2BB5eqTHupeyBM5byv5j46UjBnspTMXR%2FVJi1NA2vWayjmPJgnW0GI1ZpbN74ZT4ouw1C6%2BsLYMLBqMELktK6SSzimIDPDJR6Z%2F60UXS0oz%2Bd1HhxDmugAXmfYD3OaV6DR581seiXU7EroTRc4pekzA0GBqBi1Z3f09AZOeCAZaHdmm7q2Qg98ZvVCF5gCO2E4gvLTannq%2Fh4PUyWQheRiVCQG3paWdbL6%2F1duZgQWB0YtEF1l0sUrs6c7yX5fH13%2BIeuTDj15WHnDCPq4rKBjqkAQIONWV19yUQ5Dj3xhJ8fqrl1QpWnnOotuMGWgSDRFOhpVDZ11XcPbYUcNY850fv05w%2FrWOvC%2FHukAUfFJK%2FH0OQTXw5Vfc7hhYhxAIa5qeuZJhr%2F7b2AVxFhUduOXddzL9dy4ThqQf3rF5ci9PSHB00hplNXmNegpYhg1W6Eyn%2BDfu9dco8KpF3VTWsH1up%2F9bcnVscliQaYp78rxaYhAXCDIj%2B&X-Amz-Signature=c3fe782bf892b8f15c0d85947154ca9294a7b3d8027860669ad8fe4c6992458d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







