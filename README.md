



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEH3ZL3%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T011326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9rNSR9%2Fzfuxo6RDUKdafFkKK28ke8l%2BaghVmbJW6RAwIhAPI09yHXZnAaOqheSbZSYYkXhTjPjhz41sdQRI7tM%2B2NKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOtM5ClJVToUfK9tMq3AMtkEnFdiqfa7C0FkM5lTwBjR3JnV9QhhG5FNN4bO5XRXTsv63bbIFhN%2Bc%2FIk05nEmuD0TwLdeF7jZswk47wuSOoDYW%2BomfKiFZh0tsABs05uavFS05ODkxz8QBbZ0XClLSRyOhtDd57qKHJb3wq6X5LsdbJ2XbU1ezeWhU1gDn3vZoO0RK9kmxEGvfeXi39s03%2Fk%2BjFx5E4Ictds7loT9%2BEkwspMqs3BFz1k9l1ZTVQioriVn6OwlKi58qeqN31FWxmCOX1LEN1qB9RGidXew3rv8YrmfAd8sZPpjJEui7SO%2F5nuA0YXJeneY6FTEhcEKU05g0gVOluLO8ZmtogxyxMKq54mLz%2BvDddjtuqeXBMKR6CxS7Bg5k4%2BO7y6Zc3uR4nLxhRYguyYVGL0zf7GP8G8JzkXLgZLys%2BwwpEJA7U9URNPe9GcziEyXlLnSTSuCGNf%2BUZAs%2B7Zu2UD6vfbrXNSvPBs3WfCiFkdjyHX2DT2cao2arBIZBojqQTuUmzvfi1la7JNNxXl6Pu%2FiX3525QZ7eKWKbna1GhRVzlL1sRbi5dq7H0iVyHIPVyWeAO2LrWdTgshmr%2BVbpvSVbkho7byx7WywzVTNcfJzkAZOsPMDwaX8Drb4ega%2FlyjC%2FjY3KBjqkAf36nfcGC4a5VWtAAZTn4SgAwNF0Gzg6WmHMN7zyOcLppuCRhS3CbZmep7LavqCZfon1lZ1eGG8ndzyoWoDMg%2B%2BDsi3fyxsj0%2BH8TafaTq4pK7Yu2wHGzj6oNQSWKOB8mqi5bmi4hzM3b6N0pYDzqPHvVKf%2B7MAuwiYYym4Wjm1NPa1Jipz7V%2BjFItvtXtX9upUk3%2BYLd0sQlX8z0G95mEbG6SJe&X-Amz-Signature=bc3c1b4990b1205c3d5588762109799ba195ddb15c78275fc9c1d81b378c3b1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LEH3ZL3%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T011326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9rNSR9%2Fzfuxo6RDUKdafFkKK28ke8l%2BaghVmbJW6RAwIhAPI09yHXZnAaOqheSbZSYYkXhTjPjhz41sdQRI7tM%2B2NKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOtM5ClJVToUfK9tMq3AMtkEnFdiqfa7C0FkM5lTwBjR3JnV9QhhG5FNN4bO5XRXTsv63bbIFhN%2Bc%2FIk05nEmuD0TwLdeF7jZswk47wuSOoDYW%2BomfKiFZh0tsABs05uavFS05ODkxz8QBbZ0XClLSRyOhtDd57qKHJb3wq6X5LsdbJ2XbU1ezeWhU1gDn3vZoO0RK9kmxEGvfeXi39s03%2Fk%2BjFx5E4Ictds7loT9%2BEkwspMqs3BFz1k9l1ZTVQioriVn6OwlKi58qeqN31FWxmCOX1LEN1qB9RGidXew3rv8YrmfAd8sZPpjJEui7SO%2F5nuA0YXJeneY6FTEhcEKU05g0gVOluLO8ZmtogxyxMKq54mLz%2BvDddjtuqeXBMKR6CxS7Bg5k4%2BO7y6Zc3uR4nLxhRYguyYVGL0zf7GP8G8JzkXLgZLys%2BwwpEJA7U9URNPe9GcziEyXlLnSTSuCGNf%2BUZAs%2B7Zu2UD6vfbrXNSvPBs3WfCiFkdjyHX2DT2cao2arBIZBojqQTuUmzvfi1la7JNNxXl6Pu%2FiX3525QZ7eKWKbna1GhRVzlL1sRbi5dq7H0iVyHIPVyWeAO2LrWdTgshmr%2BVbpvSVbkho7byx7WywzVTNcfJzkAZOsPMDwaX8Drb4ega%2FlyjC%2FjY3KBjqkAf36nfcGC4a5VWtAAZTn4SgAwNF0Gzg6WmHMN7zyOcLppuCRhS3CbZmep7LavqCZfon1lZ1eGG8ndzyoWoDMg%2B%2BDsi3fyxsj0%2BH8TafaTq4pK7Yu2wHGzj6oNQSWKOB8mqi5bmi4hzM3b6N0pYDzqPHvVKf%2B7MAuwiYYym4Wjm1NPa1Jipz7V%2BjFItvtXtX9upUk3%2BYLd0sQlX8z0G95mEbG6SJe&X-Amz-Signature=795666966e7a658e22d90f84e4f51b2ef2a28e5ecfd005989d55ccd9bf7e6093&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







