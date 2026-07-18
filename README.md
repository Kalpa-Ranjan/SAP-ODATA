



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FJWMHQF%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T015831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh0SGG5hp1s5p7Jtd3uUVd4Ngd%2BUg9MtRYIly06xhnEAIhAMBZP79MkldhtiCc1x7lPmwPj%2B9BnQ0GRZtLRhpqiWh2Kv8DCGoQABoMNjM3NDIzMTgzODA1IgyOSLR1Lm%2FZNVnUGDYq3APcu1E%2FEHWqy2E%2BELiDn0VywGZBPwPP4ZCvVPdfXPT3%2Fe3bChXm9ZVWqMcfkR1o4ZCdmpW%2FF2x6b5W3nZE0z4O1ZBPBq5Eq8QhgTb3IAlSSypDVMVX840AQcssLaa2JK4A%2BvY42gvEJApuERivmznodMhqXPVAomZ%2FEHAHTAGgjwPfzuEDqi%2F%2FBT1pu%2BPZSyMY7wwU73HYRcm1LBJb2zhvQv7JVWNnnF5aT3ab3OXSsL4i%2FbDZgvTFAleWK5%2F8jeG924g681q97j5B1JG7XUgUli%2B32VzI2jo4U3N1Tl9SGtCEcQji%2FIzo%2Bp3FksWjMLJvwkwF1pTYXgCWSe%2BOAMpWNeEcAgKTqcoP5L8E83AAgORkjp8K1mMIpHadcAmf8xrq6R2cQo0UUQBuXuiSTHrPP%2F41k1TgvbMolJ0ewG%2FajWn8F2gzBA4NANSAgf7Vwg9Ur3Sg6hZGpkQCNRly1lGxK6Lq7OyaEiaStNWAncBJuTYftFnPlysK2Tx6lEe118eJvuLJn1eFYaTJVLOv43obUEspzgk0yE1Nj1YyJm1GY9olOsW9DAZ%2FamPXkWCEV0vAu5Fz934JW1aGhfr32bqz26xQAlcUleUM1Q9YHPEvfBrTjFpuVa%2FhS0Z0VNTC4pevSBjqkAe0t35xVHMV%2F48kZAwZ6qitiYzzb%2BivuhyZR9u2JD9cK84asFWwmjcUpG1T7lESPOHb6VGrdqk%2B4K0a2WL4tQgJl4xkayoyGYEA6C5XAI13s5zDfSCnRFwj78%2B%2B7E7BdQpgK%2FyXjYkmakmY4cVgioj3EIvshTBIfj2SylBhm%2F8726RO9bQrAARj2whounktIS8BL3N2oWADHlfViUKXfGjMqIAvO&X-Amz-Signature=90a66df53a3a0e314c818573e47b4b4f00f8e7d7c710947357ae3da374bd32de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FJWMHQF%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T015831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh0SGG5hp1s5p7Jtd3uUVd4Ngd%2BUg9MtRYIly06xhnEAIhAMBZP79MkldhtiCc1x7lPmwPj%2B9BnQ0GRZtLRhpqiWh2Kv8DCGoQABoMNjM3NDIzMTgzODA1IgyOSLR1Lm%2FZNVnUGDYq3APcu1E%2FEHWqy2E%2BELiDn0VywGZBPwPP4ZCvVPdfXPT3%2Fe3bChXm9ZVWqMcfkR1o4ZCdmpW%2FF2x6b5W3nZE0z4O1ZBPBq5Eq8QhgTb3IAlSSypDVMVX840AQcssLaa2JK4A%2BvY42gvEJApuERivmznodMhqXPVAomZ%2FEHAHTAGgjwPfzuEDqi%2F%2FBT1pu%2BPZSyMY7wwU73HYRcm1LBJb2zhvQv7JVWNnnF5aT3ab3OXSsL4i%2FbDZgvTFAleWK5%2F8jeG924g681q97j5B1JG7XUgUli%2B32VzI2jo4U3N1Tl9SGtCEcQji%2FIzo%2Bp3FksWjMLJvwkwF1pTYXgCWSe%2BOAMpWNeEcAgKTqcoP5L8E83AAgORkjp8K1mMIpHadcAmf8xrq6R2cQo0UUQBuXuiSTHrPP%2F41k1TgvbMolJ0ewG%2FajWn8F2gzBA4NANSAgf7Vwg9Ur3Sg6hZGpkQCNRly1lGxK6Lq7OyaEiaStNWAncBJuTYftFnPlysK2Tx6lEe118eJvuLJn1eFYaTJVLOv43obUEspzgk0yE1Nj1YyJm1GY9olOsW9DAZ%2FamPXkWCEV0vAu5Fz934JW1aGhfr32bqz26xQAlcUleUM1Q9YHPEvfBrTjFpuVa%2FhS0Z0VNTC4pevSBjqkAe0t35xVHMV%2F48kZAwZ6qitiYzzb%2BivuhyZR9u2JD9cK84asFWwmjcUpG1T7lESPOHb6VGrdqk%2B4K0a2WL4tQgJl4xkayoyGYEA6C5XAI13s5zDfSCnRFwj78%2B%2B7E7BdQpgK%2FyXjYkmakmY4cVgioj3EIvshTBIfj2SylBhm%2F8726RO9bQrAARj2whounktIS8BL3N2oWADHlfViUKXfGjMqIAvO&X-Amz-Signature=45123c3318c180bbe8ef860b603efa406104f72f9a9878df781804257f51389e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







