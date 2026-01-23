



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGWWYNY%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T062735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCBfjMhK6yt0Ain3Ob97wdUCqHT4w6UnsN5falByjEZTgIhAL5bJM2dAeJcMLa%2FWBo2hpUq90D2haBtVznzugiSo8WKKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzH3fWCVu%2F1pT8DqRMq3ANuz8V5UwLuDjyPXLKlrjtOo3MwRUPqWiSuvMFGINkjZ1khDeoB3qriwbIDH8bYTGYpmJReNmOQymRpd%2B8DLHYbpqHBj0pS1uuxweHpESLaL5pwSZmBL7UhBKJwBRfeGD9abEC2FZSeh5IvOy%2BZtLbkWxVUA%2BHf7i3anyimItiLzrN1iwKMC%2BslRwNNsIBjoJdG8nIqhAqmSv2ycMY8NZuvkBfckcblbqgI1Hhada8KR7ARvLa0iKa2m9C3ChypJDSaZ5dkA30ze1WzuUcifLxt0WDqmeb26XUS5aK0ajUPYkuASZhXQqXIfV75vQ9EhLhZ2pwXqWb42JJNe4%2BZI6GcSm1Zdne%2BaZgrgWSQxmTlsFhyJ5SAsVcemRj4rEGOZUrPrLnE2eTp3vlt9S5WNvzld9h4NtcnKlhHEnOBZWmktWnAwqq8LKaZkZtLVEYrdQF3JnmvQY1cIHUeGuvpLQZhZR1cx%2BTMuyBkJV%2FW41lYaopfNEYYULvoW6eQF7qCq93xTmcv03ct3hWiYbhTPDs0w0gKVk3EXbrnhfMgPP8EVKGXfp6soM2pHwekOmulW1CbyirkOwJlc%2FxyjcQpZEMjFaBHDA9P11SGjvnakOKRn0n0afiYscGQmHjqdTCKk8zLBjqkAWTAyLAZ04M1%2FqRbWh9hnyS%2BID8uSkMI%2FQBtt5RueI28nefzAvqhXIcbszHH%2Ffo7NbG%2Ffi6bUD%2FHAJivmyvqf%2FIxhs9asD63qYaqPOcolwFs%2FnUTR6SX6B%2FoaG3K26tdvPzQo%2Bzx1GyBcJzU6ny0AdX0b05i37xKVWxltodj%2B8POubzV%2BMXM2UKi9vp9O31bZU51dY4I9kidw%2BEmH5CO4wvhfwWU&X-Amz-Signature=b77a5029cd6c329d76442c18f948fdb00ea0b238e42ef4276b44bc8516fd3a9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGWWYNY%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T062735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCBfjMhK6yt0Ain3Ob97wdUCqHT4w6UnsN5falByjEZTgIhAL5bJM2dAeJcMLa%2FWBo2hpUq90D2haBtVznzugiSo8WKKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzH3fWCVu%2F1pT8DqRMq3ANuz8V5UwLuDjyPXLKlrjtOo3MwRUPqWiSuvMFGINkjZ1khDeoB3qriwbIDH8bYTGYpmJReNmOQymRpd%2B8DLHYbpqHBj0pS1uuxweHpESLaL5pwSZmBL7UhBKJwBRfeGD9abEC2FZSeh5IvOy%2BZtLbkWxVUA%2BHf7i3anyimItiLzrN1iwKMC%2BslRwNNsIBjoJdG8nIqhAqmSv2ycMY8NZuvkBfckcblbqgI1Hhada8KR7ARvLa0iKa2m9C3ChypJDSaZ5dkA30ze1WzuUcifLxt0WDqmeb26XUS5aK0ajUPYkuASZhXQqXIfV75vQ9EhLhZ2pwXqWb42JJNe4%2BZI6GcSm1Zdne%2BaZgrgWSQxmTlsFhyJ5SAsVcemRj4rEGOZUrPrLnE2eTp3vlt9S5WNvzld9h4NtcnKlhHEnOBZWmktWnAwqq8LKaZkZtLVEYrdQF3JnmvQY1cIHUeGuvpLQZhZR1cx%2BTMuyBkJV%2FW41lYaopfNEYYULvoW6eQF7qCq93xTmcv03ct3hWiYbhTPDs0w0gKVk3EXbrnhfMgPP8EVKGXfp6soM2pHwekOmulW1CbyirkOwJlc%2FxyjcQpZEMjFaBHDA9P11SGjvnakOKRn0n0afiYscGQmHjqdTCKk8zLBjqkAWTAyLAZ04M1%2FqRbWh9hnyS%2BID8uSkMI%2FQBtt5RueI28nefzAvqhXIcbszHH%2Ffo7NbG%2Ffi6bUD%2FHAJivmyvqf%2FIxhs9asD63qYaqPOcolwFs%2FnUTR6SX6B%2FoaG3K26tdvPzQo%2Bzx1GyBcJzU6ny0AdX0b05i37xKVWxltodj%2B8POubzV%2BMXM2UKi9vp9O31bZU51dY4I9kidw%2BEmH5CO4wvhfwWU&X-Amz-Signature=879910ebd2a28aa5ac94044981bc60ebaf74a5ffdb1a8ae2213039294925789b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







