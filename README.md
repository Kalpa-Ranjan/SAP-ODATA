



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBKXO3XZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T123439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbOONEB3Xg55C9fjTq3OGBnJ9%2FR1d2zB47mj0ygXL%2FMAiEA5LwJuKyAac4tLwTnJs7JWOju3Q8tDjJcbA0mztUCgXUqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeqIbJSTGBx5e01NCrcA8SkbIUGpmgG9zuQtVZ1hkgsh%2F6m%2FiP4maL0oueFq1QhZqoFPJcf1Yg7hL%2FxzIp7MwrPo6%2FiVtoRz%2FeDPPTC%2FrpJmflG8ywWOrGZ4iy7SX%2Bd3wCVZHR0eqi1Ces%2FleoiUpluuWLwB1s1mCEtnV00P%2BAFoOkauwCTlaFc7%2Bvu0VkoGaf8gDIkIHVK%2BB25vElRbLSmImo6kUK2Wp8vMdENGZggut8%2BVgahfP1yoyXil2KhRrZ1iiCfh1zkj6%2FB%2F%2B6gmhJYJvGAA2TQaZ6lsmsjAGCnrm4I5Sjn0BSEhNge0i%2FSk3FhyAJv73Q0CpyzXRlLswBcDNLRvnolhRou%2BKVnok6ScMFOmhikqhRE%2B6jv5Gd6iW5Do4bOeiQzjB5wXQAhGNLNfvCiLjRQ%2F3aGMNpwkXaQGG7ZPFgizUgExJlGyAeYilJ8EnoPAtJtxs5hnR5B5UPF4qrfbmoPTm0MKDdLzrk3Ky1AgncbB%2Fdu55y5mu1aGJF4cSUKSeGXB1BEjiETiQZxLKb3rzZ1yTW%2FSeu68uAE3bW%2BE1gGPVbx3Nj0cY9cr6%2FyozF66rQr8LyAouPXanEQ2UVUnCCADl3nlVvjUDqMyJ49uSBFssnQFCVZMdXx4UAFcCkms%2BeDk029MPSh4MkGOqUBob7Jox%2FJ0YOg5%2FgrqlCZ7GQQFw8BtzGsZ7kLXPOKrfGeFBjdtfFBkFgNDHg%2FcVb2%2BsWRxBH%2F2VCq9t1ICywuhfm9%2BdjBfUQcr%2B5LfGIsO6iGNh6Zke9Pgjn3ftS2jGUp9lYEXaZztIgyoju%2FaT1fS3ifziPoD8qUpgoQsoOqkqym%2BsPHRkrWli74YiBdLX%2Fn6VxqeIS31GvYJ8uPUiNp5rU7T0nN&X-Amz-Signature=a9fe96e8f38f0b3002008476a7a8f3355da262bb4667a1674629e60a501f04a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBKXO3XZ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T123439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbOONEB3Xg55C9fjTq3OGBnJ9%2FR1d2zB47mj0ygXL%2FMAiEA5LwJuKyAac4tLwTnJs7JWOju3Q8tDjJcbA0mztUCgXUqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeqIbJSTGBx5e01NCrcA8SkbIUGpmgG9zuQtVZ1hkgsh%2F6m%2FiP4maL0oueFq1QhZqoFPJcf1Yg7hL%2FxzIp7MwrPo6%2FiVtoRz%2FeDPPTC%2FrpJmflG8ywWOrGZ4iy7SX%2Bd3wCVZHR0eqi1Ces%2FleoiUpluuWLwB1s1mCEtnV00P%2BAFoOkauwCTlaFc7%2Bvu0VkoGaf8gDIkIHVK%2BB25vElRbLSmImo6kUK2Wp8vMdENGZggut8%2BVgahfP1yoyXil2KhRrZ1iiCfh1zkj6%2FB%2F%2B6gmhJYJvGAA2TQaZ6lsmsjAGCnrm4I5Sjn0BSEhNge0i%2FSk3FhyAJv73Q0CpyzXRlLswBcDNLRvnolhRou%2BKVnok6ScMFOmhikqhRE%2B6jv5Gd6iW5Do4bOeiQzjB5wXQAhGNLNfvCiLjRQ%2F3aGMNpwkXaQGG7ZPFgizUgExJlGyAeYilJ8EnoPAtJtxs5hnR5B5UPF4qrfbmoPTm0MKDdLzrk3Ky1AgncbB%2Fdu55y5mu1aGJF4cSUKSeGXB1BEjiETiQZxLKb3rzZ1yTW%2FSeu68uAE3bW%2BE1gGPVbx3Nj0cY9cr6%2FyozF66rQr8LyAouPXanEQ2UVUnCCADl3nlVvjUDqMyJ49uSBFssnQFCVZMdXx4UAFcCkms%2BeDk029MPSh4MkGOqUBob7Jox%2FJ0YOg5%2FgrqlCZ7GQQFw8BtzGsZ7kLXPOKrfGeFBjdtfFBkFgNDHg%2FcVb2%2BsWRxBH%2F2VCq9t1ICywuhfm9%2BdjBfUQcr%2B5LfGIsO6iGNh6Zke9Pgjn3ftS2jGUp9lYEXaZztIgyoju%2FaT1fS3ifziPoD8qUpgoQsoOqkqym%2BsPHRkrWli74YiBdLX%2Fn6VxqeIS31GvYJ8uPUiNp5rU7T0nN&X-Amz-Signature=059033bc1b961ea01e6cf51df61c40e452599f6d58e9ff49950d412905059499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







