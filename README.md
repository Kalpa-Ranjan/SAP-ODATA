



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XPEPQK%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T184348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDaemJAN%2FSyIse9zdWNnW3OWI%2BglKgdUvhVhkbsz%2BWcUAIhAKqb01GpMATzhZnrHQKDKDcob1rXcv%2FtDFAM6B0%2F1c%2FEKv8DCDIQABoMNjM3NDIzMTgzODA1Igydj1MnAyG3p4G%2F2Dwq3AMKLY%2FgqsMeG5z%2F6Ge7JXHFGaG3313HrT88nKRNCm0fWHF33gJHtJ223ltK3M13jJsMuJ0ja0B5I0PE%2FFzQ%2BZHfENQCL5E3ighMozThpRluvykW%2B5TtvQL%2BJYD7Kf3INMlVVYuh9JoU6wCoXfT4n%2Fz43iBDs9rgotd8jRV9a3Q3sTL9fgMIV9PfoJyZAXvB8bE%2ByrR8kpqfccdPtcGBxWXqOBW9ZEas7aZCPMLH41aeXcJ9L39noI94yphLrzQ5l5lIz2ZGKNjXxoq67rmhwcJOGz%2FdDX3n5LE%2Bx%2Fd7UzUiQew4BpWiNhBcCuqf%2FT6hJ6o5J56msnaVS0Qst8kBRMdcZEEBsNgSXT9Qd%2FdrkNQPYZv5iEZWpHlsGDE%2F5q4Rhxgj61rgXhtvboCVwRcsYCXFeDEiwPhkb4RYN5ia0GTTA6P%2Byanr15hqokT754LLpY9UvqfmiF%2B6Mzxk5Rw50P2XzYNS95fh4zyEyQUkgT%2B2Kn%2Bo%2BENuuI1GoiFrn4puXHdj%2ByYe%2FpwL16FhG7RBxgKVll53UZoBeYpA4%2FgThRaFOFmnU6agz7hH2bDq6QVCl5atjwa%2BHJwVg1DTLst3gAzarCX8%2FnpqOyELrZ1G9YxLumnSH933tnhAe1XUYzCJzuTOBjqkAVncMhoWnaEqHaCMmZ32agucv82PkmpxrNQRZWDgM1c06v0Hnc0N58S9aJrkJymGYU6QtLOjxngLtLg8nBXJmI61xUOOSRWJfUSNzPeVub86K%2Bne2974VK4WtdyHuBg1MATvdBbczcDh2gNHcVDuaLzFlzCHwSzPRhRApqKxh2Z%2F%2BQhXn0KRU0LD7KyrCnOeLfba%2BJf3e9hjQoOlbrH0NnHvrvCb&X-Amz-Signature=903af3ae5724b1a6f917c92851a37c98c8352b544c76f8b2d6e161c4fd3f9f63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XPEPQK%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T184348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDaemJAN%2FSyIse9zdWNnW3OWI%2BglKgdUvhVhkbsz%2BWcUAIhAKqb01GpMATzhZnrHQKDKDcob1rXcv%2FtDFAM6B0%2F1c%2FEKv8DCDIQABoMNjM3NDIzMTgzODA1Igydj1MnAyG3p4G%2F2Dwq3AMKLY%2FgqsMeG5z%2F6Ge7JXHFGaG3313HrT88nKRNCm0fWHF33gJHtJ223ltK3M13jJsMuJ0ja0B5I0PE%2FFzQ%2BZHfENQCL5E3ighMozThpRluvykW%2B5TtvQL%2BJYD7Kf3INMlVVYuh9JoU6wCoXfT4n%2Fz43iBDs9rgotd8jRV9a3Q3sTL9fgMIV9PfoJyZAXvB8bE%2ByrR8kpqfccdPtcGBxWXqOBW9ZEas7aZCPMLH41aeXcJ9L39noI94yphLrzQ5l5lIz2ZGKNjXxoq67rmhwcJOGz%2FdDX3n5LE%2Bx%2Fd7UzUiQew4BpWiNhBcCuqf%2FT6hJ6o5J56msnaVS0Qst8kBRMdcZEEBsNgSXT9Qd%2FdrkNQPYZv5iEZWpHlsGDE%2F5q4Rhxgj61rgXhtvboCVwRcsYCXFeDEiwPhkb4RYN5ia0GTTA6P%2Byanr15hqokT754LLpY9UvqfmiF%2B6Mzxk5Rw50P2XzYNS95fh4zyEyQUkgT%2B2Kn%2Bo%2BENuuI1GoiFrn4puXHdj%2ByYe%2FpwL16FhG7RBxgKVll53UZoBeYpA4%2FgThRaFOFmnU6agz7hH2bDq6QVCl5atjwa%2BHJwVg1DTLst3gAzarCX8%2FnpqOyELrZ1G9YxLumnSH933tnhAe1XUYzCJzuTOBjqkAVncMhoWnaEqHaCMmZ32agucv82PkmpxrNQRZWDgM1c06v0Hnc0N58S9aJrkJymGYU6QtLOjxngLtLg8nBXJmI61xUOOSRWJfUSNzPeVub86K%2Bne2974VK4WtdyHuBg1MATvdBbczcDh2gNHcVDuaLzFlzCHwSzPRhRApqKxh2Z%2F%2BQhXn0KRU0LD7KyrCnOeLfba%2BJf3e9hjQoOlbrH0NnHvrvCb&X-Amz-Signature=8e854a39f70758b554ec3ccdcee5620d0ed781cf90f6554c306fef149a4dc36a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







