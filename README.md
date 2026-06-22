



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX7MSNMM%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T203809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQC%2B9VmwXk6TKrCM%2BsLUcIGCreRk%2B8xlJVEGZBOC0gzo5gIhANh9toqyz4R9Yzd%2B%2FfG8VQarS7fNOK%2FVVdUGy6vnA1WDKv8DCAsQABoMNjM3NDIzMTgzODA1IgyPug7%2Bxj6v0XH%2BYRgq3AOVSDtIfNjXbr8lBbpYcUzEmx%2BQRqJGXgVq3%2FFCVN4uuNubHUiENPGKCHMfbDZS0TazEUyW4Qsb6KvA0NM%2Fw%2FHTO8pETOSW2S22LTkbY3SbxmpmxbUK5fUxJdhFkGg6tdt1xGx86HKvCNM4IhPk93ynlurXedl4y4LjPVSWzQ4pw%2FVm0t4gLIrkLT4Lsmpig1%2FrsugfFjKUOQuyIW1lAD7%2BvY%2BBC9u%2FHIkykXSDDpKhpVKFY2dapSzCR0CEirEADSo8aqBFTsIgDwcsyayo2b0qOLDgWuUzkTUYO%2BjLYq37E%2Fxakwlo3%2BJ3f0AFDIjeu87DNVeFZLQiu5AJxvT5X5L5EAz1oDs70sN4GeWkPibIwmjlKurpOksrlLahHipZxSNE63NmDYy%2Bc9R6XRjjECGwfpGDRilDbR87s8gLxBtA2pHNhIugRM%2BTQw48ZyPSXO9YO3JdjThEhoGOGJ2hj8GuXMrjIaIKqvKy3M%2F7TrBdq25q%2Bvzhu6XZdvFhXyVyMZPkuCNnGOH2TQPEe%2BBE8tVESdfLGHV1X%2FcvBVEHZ6YLzzumGBwVYNVeEW8HpHAH6Q9AFuc2JBjHJuAn8yGUeTQqqqIM6aG6ly1h0lzRdfuEXi6KNe1vXGZpc3hQ0TC%2B%2BuXRBjqkATcmrcLmHY6tW2%2BYToWmoUFgUDHaDs5aXrp2mUYWYo3ZOmJl8PJxCOt6dskmtKBmeRiK9UW%2BtJ%2BUckKR1xibORLzkZqI8aknDVWTyYEN1bhOCHxEBuSzIal51zOsVHUWhjXeKcDse8Hg2g%2BVM7o3Nc4R43axfV2Rqi6P5T0MusRq5z3HgELeTf8gC1XcSJ3iU8tnaC1D3iJIGQaBe7HC9cjjo8X1&X-Amz-Signature=0f294854ba2430b985c2db9a3f6321b6523da6f7956788e275f980c6f22314dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX7MSNMM%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T203809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQC%2B9VmwXk6TKrCM%2BsLUcIGCreRk%2B8xlJVEGZBOC0gzo5gIhANh9toqyz4R9Yzd%2B%2FfG8VQarS7fNOK%2FVVdUGy6vnA1WDKv8DCAsQABoMNjM3NDIzMTgzODA1IgyPug7%2Bxj6v0XH%2BYRgq3AOVSDtIfNjXbr8lBbpYcUzEmx%2BQRqJGXgVq3%2FFCVN4uuNubHUiENPGKCHMfbDZS0TazEUyW4Qsb6KvA0NM%2Fw%2FHTO8pETOSW2S22LTkbY3SbxmpmxbUK5fUxJdhFkGg6tdt1xGx86HKvCNM4IhPk93ynlurXedl4y4LjPVSWzQ4pw%2FVm0t4gLIrkLT4Lsmpig1%2FrsugfFjKUOQuyIW1lAD7%2BvY%2BBC9u%2FHIkykXSDDpKhpVKFY2dapSzCR0CEirEADSo8aqBFTsIgDwcsyayo2b0qOLDgWuUzkTUYO%2BjLYq37E%2Fxakwlo3%2BJ3f0AFDIjeu87DNVeFZLQiu5AJxvT5X5L5EAz1oDs70sN4GeWkPibIwmjlKurpOksrlLahHipZxSNE63NmDYy%2Bc9R6XRjjECGwfpGDRilDbR87s8gLxBtA2pHNhIugRM%2BTQw48ZyPSXO9YO3JdjThEhoGOGJ2hj8GuXMrjIaIKqvKy3M%2F7TrBdq25q%2Bvzhu6XZdvFhXyVyMZPkuCNnGOH2TQPEe%2BBE8tVESdfLGHV1X%2FcvBVEHZ6YLzzumGBwVYNVeEW8HpHAH6Q9AFuc2JBjHJuAn8yGUeTQqqqIM6aG6ly1h0lzRdfuEXi6KNe1vXGZpc3hQ0TC%2B%2BuXRBjqkATcmrcLmHY6tW2%2BYToWmoUFgUDHaDs5aXrp2mUYWYo3ZOmJl8PJxCOt6dskmtKBmeRiK9UW%2BtJ%2BUckKR1xibORLzkZqI8aknDVWTyYEN1bhOCHxEBuSzIal51zOsVHUWhjXeKcDse8Hg2g%2BVM7o3Nc4R43axfV2Rqi6P5T0MusRq5z3HgELeTf8gC1XcSJ3iU8tnaC1D3iJIGQaBe7HC9cjjo8X1&X-Amz-Signature=375b28e28f2830b6e291d91f145a876af1a5d6d79f155a9e3b6f227d2cd89cb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







