



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OHIPS%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T130853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCf1TOo7Vg8OHmbCNKsre4wy1u7lJkq0EXuKw2jFi0z%2BwIhAKYQb3Hq1P5FOwhkIKFKcgU0KIdCOhvlibVvLG9bT0q0KogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwr%2Fjbg%2BhxaYoXznU8q3APAKpqmxZMO5%2FJXBgMTqWiy9vb%2Bn3fWIWcb0PaZPzFq1wQ1S1yrmnGcJGWduv%2FHr3sIKQ5zMxkncn5jrn6rq0O4SbyvDvC0eIxDBdUXDNJQ7N%2F3nfqkuxvJzFd%2B6jZe392u%2BqxjIA%2BTYyZJcwoAHzpFdpyda7ZE%2Bnqwqy9IeSvNRUrYdjDN2xLEYIDHkH8IZeLZ0r9YtnBMKAJ1MejB%2BZlxVa4978ER9LbKS2JdGXUwUZK0VJq6W4FcmZXa34nw%2BxFgNGsYHe1Hmc9tc280Ya9RoqCH%2FBHUutcWS2axkt6nhzEiY%2Ffs87MtwxmOMWZH2l9HoQGyOa2GekEs3mFJ6dbQIC92a%2FAlNruIRMh3FRv92LwYo2yow0Q5sumcyzuNmen5gQDEivhttEkcMcoz1uU1qA8%2B3AgsTtoai741XeA9nmVNPvyrW4kACOrKqU8H3HGb%2FW5ndAjDS7U8IdMjJojycl0NH13GAQKm5zQnj2BYrbHhyBAf3gfBVM1miI7XmjtTOCLlLDxGw1zrwb6CS1MIDJkFIJ%2BBU8l%2BjEiCeSWla%2FHLj7bjYlxNSFymdGS6BOutWIMZGrsF3s9f1t9AZlwt6dgI%2FFRUBNT%2FCHKLN2r1PpeiL4pVzrjJgpq6czDSgtTOBjqkAUHg8%2BNuAUbo8zoO0zWr3MXdCvBVHIknFgx7L5v3G2D2XsU91aBg0cTS7H2YhmyEAbzrza9la6xtWQ9WUFMmmOyPkAUsb00hzeJsxiXywKg2JfySWuHMiSCwuHj0MkKjZJOAalFJsc4BkVcXauIzxNqMNYE9IMFf4rbSSTuTFpdPnmRXoxFMNimy%2BqRVJdSu%2FfBN%2BmvUvTm2d3TI7mjf3lA9wfb6&X-Amz-Signature=a3aaae8fe1a65d82302dcfb71123773550470586464ef88c58374d6a13ae78f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y6OHIPS%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T130854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCf1TOo7Vg8OHmbCNKsre4wy1u7lJkq0EXuKw2jFi0z%2BwIhAKYQb3Hq1P5FOwhkIKFKcgU0KIdCOhvlibVvLG9bT0q0KogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwr%2Fjbg%2BhxaYoXznU8q3APAKpqmxZMO5%2FJXBgMTqWiy9vb%2Bn3fWIWcb0PaZPzFq1wQ1S1yrmnGcJGWduv%2FHr3sIKQ5zMxkncn5jrn6rq0O4SbyvDvC0eIxDBdUXDNJQ7N%2F3nfqkuxvJzFd%2B6jZe392u%2BqxjIA%2BTYyZJcwoAHzpFdpyda7ZE%2Bnqwqy9IeSvNRUrYdjDN2xLEYIDHkH8IZeLZ0r9YtnBMKAJ1MejB%2BZlxVa4978ER9LbKS2JdGXUwUZK0VJq6W4FcmZXa34nw%2BxFgNGsYHe1Hmc9tc280Ya9RoqCH%2FBHUutcWS2axkt6nhzEiY%2Ffs87MtwxmOMWZH2l9HoQGyOa2GekEs3mFJ6dbQIC92a%2FAlNruIRMh3FRv92LwYo2yow0Q5sumcyzuNmen5gQDEivhttEkcMcoz1uU1qA8%2B3AgsTtoai741XeA9nmVNPvyrW4kACOrKqU8H3HGb%2FW5ndAjDS7U8IdMjJojycl0NH13GAQKm5zQnj2BYrbHhyBAf3gfBVM1miI7XmjtTOCLlLDxGw1zrwb6CS1MIDJkFIJ%2BBU8l%2BjEiCeSWla%2FHLj7bjYlxNSFymdGS6BOutWIMZGrsF3s9f1t9AZlwt6dgI%2FFRUBNT%2FCHKLN2r1PpeiL4pVzrjJgpq6czDSgtTOBjqkAUHg8%2BNuAUbo8zoO0zWr3MXdCvBVHIknFgx7L5v3G2D2XsU91aBg0cTS7H2YhmyEAbzrza9la6xtWQ9WUFMmmOyPkAUsb00hzeJsxiXywKg2JfySWuHMiSCwuHj0MkKjZJOAalFJsc4BkVcXauIzxNqMNYE9IMFf4rbSSTuTFpdPnmRXoxFMNimy%2BqRVJdSu%2FfBN%2BmvUvTm2d3TI7mjf3lA9wfb6&X-Amz-Signature=72d0a0fb0ae78ff02ad0c055438487f1d9cc8687692e4934ab4b4f27c4dfcc9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







