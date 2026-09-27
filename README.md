



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IAG6HCP%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T180910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQCEMa7DZOxcKjwsigeLxhDNQNcQL2XcpzUYn5lw%2Fbbf4AIgErmGR6NTApXm7w3SvnPSKfs2xCejNwOlk1rqXBjaWa0q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDLaBIxmV58jME4ji9CrcA7WE%2Bw64A8m%2F3uz6wRB0cSSFdFLCIzJ529IWQBYIGsqS7xjn4EN4F7gKXsglUYL%2BwifExFlonZA9SE4MPCdN4%2B%2Fik80RWj8L9oryRcmTTIUSYONrRe8WR2Z4HutueKkV%2FSWLpPh%2Fx7FyKQ%2Byd%2F2%2F4gPDGwJRgBtH4KbqbEgUOtwn%2FveYfwg1GxsuujbeC3rrcu1PWL4c1AkoPtVlaEa7Zc0hoDcIV61JAuxxb6gkb5REMTqy2uuGAq7bqr3C0b0%2BMOquT952r0VQkub2ejsUi4JRAkxwFIlSOz8168O3lvjIlndv02hbfiZ0MIVQKMN%2B%2B42RmpPBq6H6Hc%2Bc1EI1uiu4oxvuOMUdfMhtUS0%2F3Si8vMLlpSKusiWMTaesYyDKCyDwN0N2SWKceFWuEWbJOCZTWJ03PMY1EvQQsGk2v2aWxTJ8ofrmWRiEjNrizIVcDWJ7ugdFrgzkrbhIrnJqU7uAUDuSdczKEiw%2Brg3RmaF7GDNgG%2FtlkzLHpa2W4qdof%2FcSnt%2FFjm8AKVkOb3aCl0fiycdO02QaXR7rg4khC84qcOn%2Ft1AWRchG46F7TpwYQhzLzukAnsH%2Ft%2Brr%2BBU7WW0NhMe%2BZ2fbHxC9g%2FIpXGnVy5zAfkYDzSjspJSJMOWO5dUGOqUBKt6aaRTwPhy3yaSgxsSyqPV879%2FEIRFMGymBxuSV7fBEQO8cn60dJLLwn%2BFs3GL9vAaUoS5ALixYxBfYkShGpMcnccWjeD3YU%2FEE47RuVd%2BlPvT261yIjnbODBXPtwX1clcPj6zgWM0U464ZGcktoPQlH9iVJmAM%2FL8ojmq9dTYWHRdKh83ZTSQtS24dCA1liCYY3hYE7pAvm%2F%2BcdDW1GTYUCCIz&X-Amz-Signature=c230bdd6764aefeffa0329f017ea98889c212028bce33f02a4c6dc762d7dc75d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IAG6HCP%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T180910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQCEMa7DZOxcKjwsigeLxhDNQNcQL2XcpzUYn5lw%2Fbbf4AIgErmGR6NTApXm7w3SvnPSKfs2xCejNwOlk1rqXBjaWa0q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDLaBIxmV58jME4ji9CrcA7WE%2Bw64A8m%2F3uz6wRB0cSSFdFLCIzJ529IWQBYIGsqS7xjn4EN4F7gKXsglUYL%2BwifExFlonZA9SE4MPCdN4%2B%2Fik80RWj8L9oryRcmTTIUSYONrRe8WR2Z4HutueKkV%2FSWLpPh%2Fx7FyKQ%2Byd%2F2%2F4gPDGwJRgBtH4KbqbEgUOtwn%2FveYfwg1GxsuujbeC3rrcu1PWL4c1AkoPtVlaEa7Zc0hoDcIV61JAuxxb6gkb5REMTqy2uuGAq7bqr3C0b0%2BMOquT952r0VQkub2ejsUi4JRAkxwFIlSOz8168O3lvjIlndv02hbfiZ0MIVQKMN%2B%2B42RmpPBq6H6Hc%2Bc1EI1uiu4oxvuOMUdfMhtUS0%2F3Si8vMLlpSKusiWMTaesYyDKCyDwN0N2SWKceFWuEWbJOCZTWJ03PMY1EvQQsGk2v2aWxTJ8ofrmWRiEjNrizIVcDWJ7ugdFrgzkrbhIrnJqU7uAUDuSdczKEiw%2Brg3RmaF7GDNgG%2FtlkzLHpa2W4qdof%2FcSnt%2FFjm8AKVkOb3aCl0fiycdO02QaXR7rg4khC84qcOn%2Ft1AWRchG46F7TpwYQhzLzukAnsH%2Ft%2Brr%2BBU7WW0NhMe%2BZ2fbHxC9g%2FIpXGnVy5zAfkYDzSjspJSJMOWO5dUGOqUBKt6aaRTwPhy3yaSgxsSyqPV879%2FEIRFMGymBxuSV7fBEQO8cn60dJLLwn%2BFs3GL9vAaUoS5ALixYxBfYkShGpMcnccWjeD3YU%2FEE47RuVd%2BlPvT261yIjnbODBXPtwX1clcPj6zgWM0U464ZGcktoPQlH9iVJmAM%2FL8ojmq9dTYWHRdKh83ZTSQtS24dCA1liCYY3hYE7pAvm%2F%2BcdDW1GTYUCCIz&X-Amz-Signature=b625079dd1503b5873922f801e93262ca3b71ad7d54508602492b7e5aa8aa788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







