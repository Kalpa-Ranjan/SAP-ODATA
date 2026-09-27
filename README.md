



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N7GWHHC%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T002417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQC1wx4EZLwmAHJy20MDi%2BP%2Bjrzl94odkvKQTGog6i%2FJbQIhAIdYKk56r3Mi6wgIUD8bL2Co9icW16LkLbf7c0GQ8lhLKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7EWay8eID2BFTobEq3ANMJ7jo3Kt75CayKd8WaoqZE08olPSTcOFizyGfJnYXV%2BjorBp53uKr87VxeA1oYryUY%2FhQYG2cyloMF4DNz6hL4a2uY%2FP9H%2Fx6aUT%2B0q1PJCWPcTozj9fSF142USd05I7fGU7j8Ua5D8FXymB5ftjmPc6gefdtumpHdyzZ%2B%2Fk43EkatcMtULwKtwW57edHG8g7NQb9UIcZuF%2BeVUhoIKf4l6QsAyqXYV7jZrGXmpVJ4LmpYtVvaJQ6qPNcMMci7PCchPkq1xxKZS7Z8jD%2Bwp3KaXgRFH0X6zggVEuROrby7OfPUJWsDZhZ4Ur9WLQYYD3r1UopJ51QPfV8YUDCEdSLa9YnSX2ynYXGwvrSa3hHWpuTaQAYoCoqJWNbi9pY2UjdkjD3k9HcnDEKGHMPvWffUHLJ6QX0k2PMBP542Z2dPSzP0Yw7yywAdrpFPpA3X0oQpLpZK6vFytYmGDFRSCDQ2721kVjzqDIPJhwHXuik00MzUXtD0NfuHKC99woyXcyERZDdbFo23MWq1JojkblGktkVVIKdk72wzmOUmpR3WcAiNKPQWUW%2FOaij%2BHXbopZjtjhDE%2FurPc%2BGc7KQtABU6ZBWqgMHQ9UksJlnwe48pJu1aiuzkMXTvxNItzDzo%2BHVBjqkATRqEjBzVPyVzbL1sN7gEqpjVEExOIAN88vNmC%2Bnbf%2FGtXLUhixh5EiIEadDBYg5E1OekvRadngexf7s%2B2%2BIi8LqHSGX4BfbQpoLXgD%2FIzN7d%2BjlKUH6qR1XxHK0aarIUqkafhkXcWIVbDeicoYvPXJnZLSQ1ejRhH2DbdngfRigZb4tkukybw7khSrrr%2FyqtAhI9bmbSb4MIUnwdilEjbEW1sTZ&X-Amz-Signature=051543c8b6000022ed14888476c001ba54d49f8a9c623f327a67ab55f5813a45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N7GWHHC%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T002417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQC1wx4EZLwmAHJy20MDi%2BP%2Bjrzl94odkvKQTGog6i%2FJbQIhAIdYKk56r3Mi6wgIUD8bL2Co9icW16LkLbf7c0GQ8lhLKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7EWay8eID2BFTobEq3ANMJ7jo3Kt75CayKd8WaoqZE08olPSTcOFizyGfJnYXV%2BjorBp53uKr87VxeA1oYryUY%2FhQYG2cyloMF4DNz6hL4a2uY%2FP9H%2Fx6aUT%2B0q1PJCWPcTozj9fSF142USd05I7fGU7j8Ua5D8FXymB5ftjmPc6gefdtumpHdyzZ%2B%2Fk43EkatcMtULwKtwW57edHG8g7NQb9UIcZuF%2BeVUhoIKf4l6QsAyqXYV7jZrGXmpVJ4LmpYtVvaJQ6qPNcMMci7PCchPkq1xxKZS7Z8jD%2Bwp3KaXgRFH0X6zggVEuROrby7OfPUJWsDZhZ4Ur9WLQYYD3r1UopJ51QPfV8YUDCEdSLa9YnSX2ynYXGwvrSa3hHWpuTaQAYoCoqJWNbi9pY2UjdkjD3k9HcnDEKGHMPvWffUHLJ6QX0k2PMBP542Z2dPSzP0Yw7yywAdrpFPpA3X0oQpLpZK6vFytYmGDFRSCDQ2721kVjzqDIPJhwHXuik00MzUXtD0NfuHKC99woyXcyERZDdbFo23MWq1JojkblGktkVVIKdk72wzmOUmpR3WcAiNKPQWUW%2FOaij%2BHXbopZjtjhDE%2FurPc%2BGc7KQtABU6ZBWqgMHQ9UksJlnwe48pJu1aiuzkMXTvxNItzDzo%2BHVBjqkATRqEjBzVPyVzbL1sN7gEqpjVEExOIAN88vNmC%2Bnbf%2FGtXLUhixh5EiIEadDBYg5E1OekvRadngexf7s%2B2%2BIi8LqHSGX4BfbQpoLXgD%2FIzN7d%2BjlKUH6qR1XxHK0aarIUqkafhkXcWIVbDeicoYvPXJnZLSQ1ejRhH2DbdngfRigZb4tkukybw7khSrrr%2FyqtAhI9bmbSb4MIUnwdilEjbEW1sTZ&X-Amz-Signature=91741ee82a87e7dde077a77d94d2061c83d8d21ae2b378f862d60246c9303b43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







