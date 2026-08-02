



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56JG7JE%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T081234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCql2ctE0V7VIZo%2BkGPpn1%2BT9CnQdKD%2FqPOiCQsKAW5VAIhAOaMo7tKoc2%2FVg4AHHYE4t2qv4EoGsemUBpLIDNYg8ZgKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6WfxpiVnUXz%2BOxpQq3APaDPSJEdjiNB7EVLGKT5p03GuDS8YveBriITS9u5Z8%2F7Q8HWPsPr2cL340cZsm8qyKuT5lzPAw7TY46vdKpdOVd%2BFFivwgjwfO74wpg5wfQMzGJyrGZGN%2FvQ4PYKEBmjP9biq6lUWzLmaYGcTDsvJZ0xRCJl7AmrUSBn2vv3IWCUhEP3pSkSXUb7%2BYdeD6%2BYqXl%2BLvQon7tkCqLAA7C%2F3T8MN9z7NZ99iS8R45nw3JorHKm9FlZe%2BMrFkhAdGmUhGHdmsUG9bxs3jN8US1sIdPv2iI57WyHHIynR6CzQ%2BecvnmzThAKjhwtJlmI6gCxYAnkmfvdJ%2B81%2FOzqBkpQ7YBbGCQD27y1oU%2FoOD8najuEXwDgnbfIfjO9Im55moglrS8p5pNmzBjBcS6AvMfH7B2PdYon2Wtx15BQoRUF3xGT7CR%2BxpmcV8eVYgVyiIgv17hXmondvyAKeiJnhfP1uZPB5ylIZ4UGlR8480sLOV3tN16SDPbfcr%2Bfh6kLw%2BeqLSeWuOym7GKzykZ5XZLFhI%2BPzhuZm7Xq3myDAsguyznjIcQ81my8DxSnTlqEU7MVaEnuhttBYJ0AFdaguc7xhg8R%2B%2B8EoFPHsRo%2BunzBNz0Zf%2Bm3mxM7WjGj4EtPzCQ8bvTBjqkARkR2dZQIRFu5bdr53rBI3xvMovjShCq2nL7xHDZFZUUDasIMi4qZdk4ZN1gPQsVFUh%2BZ9nd6KKogu9o%2FNCptDcIFk2xqN02Smaq3aPr9yIotcZYLba6qr7NmQJURO7C5VKLrS1byXjlVHZ78tpAUaXQfb7sqiQUvJNsDcOJdsKdBL4GWkIyPViwWA%2B3g2oo2Xdb1l0RCV1ieEgAPEoJJzZLkYFx&X-Amz-Signature=24efba6070a0550e12d9e072ebf642c54dac61503870cc727badb4c9fe0bc884&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56JG7JE%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T081234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCql2ctE0V7VIZo%2BkGPpn1%2BT9CnQdKD%2FqPOiCQsKAW5VAIhAOaMo7tKoc2%2FVg4AHHYE4t2qv4EoGsemUBpLIDNYg8ZgKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6WfxpiVnUXz%2BOxpQq3APaDPSJEdjiNB7EVLGKT5p03GuDS8YveBriITS9u5Z8%2F7Q8HWPsPr2cL340cZsm8qyKuT5lzPAw7TY46vdKpdOVd%2BFFivwgjwfO74wpg5wfQMzGJyrGZGN%2FvQ4PYKEBmjP9biq6lUWzLmaYGcTDsvJZ0xRCJl7AmrUSBn2vv3IWCUhEP3pSkSXUb7%2BYdeD6%2BYqXl%2BLvQon7tkCqLAA7C%2F3T8MN9z7NZ99iS8R45nw3JorHKm9FlZe%2BMrFkhAdGmUhGHdmsUG9bxs3jN8US1sIdPv2iI57WyHHIynR6CzQ%2BecvnmzThAKjhwtJlmI6gCxYAnkmfvdJ%2B81%2FOzqBkpQ7YBbGCQD27y1oU%2FoOD8najuEXwDgnbfIfjO9Im55moglrS8p5pNmzBjBcS6AvMfH7B2PdYon2Wtx15BQoRUF3xGT7CR%2BxpmcV8eVYgVyiIgv17hXmondvyAKeiJnhfP1uZPB5ylIZ4UGlR8480sLOV3tN16SDPbfcr%2Bfh6kLw%2BeqLSeWuOym7GKzykZ5XZLFhI%2BPzhuZm7Xq3myDAsguyznjIcQ81my8DxSnTlqEU7MVaEnuhttBYJ0AFdaguc7xhg8R%2B%2B8EoFPHsRo%2BunzBNz0Zf%2Bm3mxM7WjGj4EtPzCQ8bvTBjqkARkR2dZQIRFu5bdr53rBI3xvMovjShCq2nL7xHDZFZUUDasIMi4qZdk4ZN1gPQsVFUh%2BZ9nd6KKogu9o%2FNCptDcIFk2xqN02Smaq3aPr9yIotcZYLba6qr7NmQJURO7C5VKLrS1byXjlVHZ78tpAUaXQfb7sqiQUvJNsDcOJdsKdBL4GWkIyPViwWA%2B3g2oo2Xdb1l0RCV1ieEgAPEoJJzZLkYFx&X-Amz-Signature=6140f04ff66594fed7fea8d4e379093c1308c8eeecb6f53e6656bbd295ac29a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







