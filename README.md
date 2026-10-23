



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF6J67NJ%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T002033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICCTm7M4FWi2UglRR5DHtJLaSlinl0inbazRs681j5BUAiEAm%2B7FLaiF2BneGBrAHZlOj0MPexUaLh%2FHbjsW7H9JUZcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIa%2F4%2FctTSsro%2F8v8ircAzKtBy1MWlSHVFFs14Dh60Vq7zqVsZAC0lWUbqVrmU9A6uJSbCe8Vpl8nWAxHno6G%2F%2FXoEfOCvhXdUGxHp10noBPeg8kFBLoqUMeoVuBxx6KHsJelVIjOkICODT1X4RpXdFJ3jq8XFu9iWBkj4i7JYoc4KBqAqXMc%2Fh7VSu7cowQGLaqNpdAFSsv6LV%2BQ%2FxM02Bg7mnNJ9pb8BgJ8JOtGAnRK2D7hwL8QmaWdwtWcX5Zd0Rr5su0%2BzKpidMgmsAkXn5Cxlyhov33etA9mDPE54pvL%2FDvDWS2onalLlVpkjbqsDF0w7nB4p8S8T8x7CPjlwXklc0ZLTlJQGYm986FgMJLdqXhEIzu%2FKtR2qXv4bz4HluqcCxPi5b24WqNjeIlbvxHryHn6XaFnR8HuInJLlneWjaz7Nxe8y6EBde7jsnWPvWbqrg9WWjAKGIalfGSXWvGtamDt79RlsY9S5Q0DfJT2e%2B1nUd4nHTKpaNBGAhoQwR0ptnpvLGW5sY645AZrspdJZT41J4hG0IcKNjN1SKhg%2FhwyArStA1cOn8pEqQ1039JWuRDEbBdWctW3o%2FYX0tNSYK2PYDsmg8%2Flfz1K%2B6t88RtElDKG%2FIeh932UqA0WRLbwK%2FStVC6kfEHMLim6tYGOqUBvjjpzy3CdSZe1xpAj%2FMDI0MIF8B0xrTU7hZlS4w9bLDdD6BY1hMuMEdav9xT5uZvYPLQFYsF5v0HTZCnFmhHbK2%2F5QBRDswgqRd%2FHZdX552w%2BNIp6ti2Bh7S%2FP20LLRkRr4mKRJ3NqsTaI2r42MO%2BQ9iuk6C4qEgu546AEPZ%2B92vcmQjP4kXLPLriPjwIGcPHFz%2Bo4T1dApVzvb4q2FlDqjdxEqK&X-Amz-Signature=e5dbebdcc256bc8732ddfe4ccc724e1d0d7ee6d964e6df4a036de99af485c869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF6J67NJ%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T002033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICCTm7M4FWi2UglRR5DHtJLaSlinl0inbazRs681j5BUAiEAm%2B7FLaiF2BneGBrAHZlOj0MPexUaLh%2FHbjsW7H9JUZcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIa%2F4%2FctTSsro%2F8v8ircAzKtBy1MWlSHVFFs14Dh60Vq7zqVsZAC0lWUbqVrmU9A6uJSbCe8Vpl8nWAxHno6G%2F%2FXoEfOCvhXdUGxHp10noBPeg8kFBLoqUMeoVuBxx6KHsJelVIjOkICODT1X4RpXdFJ3jq8XFu9iWBkj4i7JYoc4KBqAqXMc%2Fh7VSu7cowQGLaqNpdAFSsv6LV%2BQ%2FxM02Bg7mnNJ9pb8BgJ8JOtGAnRK2D7hwL8QmaWdwtWcX5Zd0Rr5su0%2BzKpidMgmsAkXn5Cxlyhov33etA9mDPE54pvL%2FDvDWS2onalLlVpkjbqsDF0w7nB4p8S8T8x7CPjlwXklc0ZLTlJQGYm986FgMJLdqXhEIzu%2FKtR2qXv4bz4HluqcCxPi5b24WqNjeIlbvxHryHn6XaFnR8HuInJLlneWjaz7Nxe8y6EBde7jsnWPvWbqrg9WWjAKGIalfGSXWvGtamDt79RlsY9S5Q0DfJT2e%2B1nUd4nHTKpaNBGAhoQwR0ptnpvLGW5sY645AZrspdJZT41J4hG0IcKNjN1SKhg%2FhwyArStA1cOn8pEqQ1039JWuRDEbBdWctW3o%2FYX0tNSYK2PYDsmg8%2Flfz1K%2B6t88RtElDKG%2FIeh932UqA0WRLbwK%2FStVC6kfEHMLim6tYGOqUBvjjpzy3CdSZe1xpAj%2FMDI0MIF8B0xrTU7hZlS4w9bLDdD6BY1hMuMEdav9xT5uZvYPLQFYsF5v0HTZCnFmhHbK2%2F5QBRDswgqRd%2FHZdX552w%2BNIp6ti2Bh7S%2FP20LLRkRr4mKRJ3NqsTaI2r42MO%2BQ9iuk6C4qEgu546AEPZ%2B92vcmQjP4kXLPLriPjwIGcPHFz%2Bo4T1dApVzvb4q2FlDqjdxEqK&X-Amz-Signature=7166ea902ea0626b6e62cdef61e153fb4c3ae5ed1a267255eae30618610eb817&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







