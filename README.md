



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RGFZEG7%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T180946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrR5Z5Mav3Qa4GgopKYrQ5Ar5UJkA8hUwQn8tBgVbq%2BAiEAmPBvH%2Fe0SYZtF0qHWQd6AixCNOy9PIW0NDnY7Ttcpo0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOpioV2KM9NdoRP1PCrcA%2F%2FEGBj1eJtERvzBMBlsxRQ6j6I%2FqvxlVkIK2g1CDmkCaMWV3iQ2R26UuANU54RjahoiyQIqtE0JMmQeQmBmtE%2FGsV9bjgE2AQXT0nv4t2S3YRMeIBsWHi1RPtVX4%2FnWfpVFXRYQxb9Lk8CxS1O%2BQjFNzwEQXIBrW88k3Ua3nMm3xD3dBWQjCY6qoWq80YeGpu8f1gSo8JCxayp6sMiFp2na8bytBk8cLqE%2B5t0RHjmPf34ZXAPcKmUSLwqg4ckXwc16RcZTEOoN2z0gqknwi3HlxYuyS48MtL0IhBDSeLlHGb4s8SIQzma1JhAKlKERrbFMZukhBXhkt4ajWi2AQL6qPJ7SXueW%2BEV9zNOE05CBSrMU5ztxuqeAtSra1hlXnjYvSVv1Qdu1v4hnYP2TU17koyF2JgS6ybPRhf%2FKHOwtDkCxtovw7s70iE3GjKZDMMmUMd0p19O4QfslmAqoSHqkuQi8V2Bfq6eX%2FSmwcbKujkTDPY38d6nWGwlW2RuKCSYjSQX1m3H5OPSbiskz96Q%2FZhQlQPzJGdHj3dwRHIavhei7cd25uBbTcZlUXE95X3sKBlJl27BrFUW1MbgVWRamljnDTugAaME8QABHmLJra68nPwwslF3f%2FceaMMmAgdUGOqUBIjeZGxI66gjpdcme4L0%2F6iPgW7u6aMOyTHb03vcNzFhkvRnCbl7SR1D0Uy6VQheNk0Tfi37fx9J1a2txpI1S5sua3BsTX1lvw9Mo%2BV5HkQnVrXOp%2FJIXwzw8dcd3lmD3%2Bhg2jxHuGWyDCR0AnNlzWRf%2Bx73072fhieakQaR4RzgVW0N29EHhsRSEe%2BSs9Xhy%2BhAPSz7ze2hbI2SIeDgEVDS72%2B5v&X-Amz-Signature=cdc606ac3a2bfdc5e4db3b6b9220ca1a5403a8afc14db4742a8d0f29457285fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RGFZEG7%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T180946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrR5Z5Mav3Qa4GgopKYrQ5Ar5UJkA8hUwQn8tBgVbq%2BAiEAmPBvH%2Fe0SYZtF0qHWQd6AixCNOy9PIW0NDnY7Ttcpo0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOpioV2KM9NdoRP1PCrcA%2F%2FEGBj1eJtERvzBMBlsxRQ6j6I%2FqvxlVkIK2g1CDmkCaMWV3iQ2R26UuANU54RjahoiyQIqtE0JMmQeQmBmtE%2FGsV9bjgE2AQXT0nv4t2S3YRMeIBsWHi1RPtVX4%2FnWfpVFXRYQxb9Lk8CxS1O%2BQjFNzwEQXIBrW88k3Ua3nMm3xD3dBWQjCY6qoWq80YeGpu8f1gSo8JCxayp6sMiFp2na8bytBk8cLqE%2B5t0RHjmPf34ZXAPcKmUSLwqg4ckXwc16RcZTEOoN2z0gqknwi3HlxYuyS48MtL0IhBDSeLlHGb4s8SIQzma1JhAKlKERrbFMZukhBXhkt4ajWi2AQL6qPJ7SXueW%2BEV9zNOE05CBSrMU5ztxuqeAtSra1hlXnjYvSVv1Qdu1v4hnYP2TU17koyF2JgS6ybPRhf%2FKHOwtDkCxtovw7s70iE3GjKZDMMmUMd0p19O4QfslmAqoSHqkuQi8V2Bfq6eX%2FSmwcbKujkTDPY38d6nWGwlW2RuKCSYjSQX1m3H5OPSbiskz96Q%2FZhQlQPzJGdHj3dwRHIavhei7cd25uBbTcZlUXE95X3sKBlJl27BrFUW1MbgVWRamljnDTugAaME8QABHmLJra68nPwwslF3f%2FceaMMmAgdUGOqUBIjeZGxI66gjpdcme4L0%2F6iPgW7u6aMOyTHb03vcNzFhkvRnCbl7SR1D0Uy6VQheNk0Tfi37fx9J1a2txpI1S5sua3BsTX1lvw9Mo%2BV5HkQnVrXOp%2FJIXwzw8dcd3lmD3%2Bhg2jxHuGWyDCR0AnNlzWRf%2Bx73072fhieakQaR4RzgVW0N29EHhsRSEe%2BSs9Xhy%2BhAPSz7ze2hbI2SIeDgEVDS72%2B5v&X-Amz-Signature=4327daa9f0816fdea06ae227264df19cca2b9ff53bdae27a792f48662c20c8af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







