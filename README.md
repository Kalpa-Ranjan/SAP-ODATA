



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MAUCF2%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T123450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTn4Sxa5JERyC%2B7r2s9RL%2FBcggS6RPbxv%2FF8JQlPROaAIhAMKiTRi05qZCnjaUEclM89TYLqMx1XgXIHyV48zg%2FEO4Kv8DCHQQABoMNjM3NDIzMTgzODA1IgzHcOLjJwwJlihUV8cq3AO87XZGWm7cdm327FYHkxBXogOacqKo7TCZiyeXO%2BpCkOB4w7cxa4ntDN2VwTl7LiHbT78Gb7sMtPjSuBf%2Fxrt%2BMW8NKYgaukw2kOam6CXjoYTs21BMDFHM9xXHOXg8YiGf5w%2FnvyoMNLwKbanNkESc6169vEU2ZWTok5wrm3LS2Ua2y3Q20I3PZ8j8aJ9iIU24s0jv0okSajp3VYEE8oa%2FaVVOj5kHhDZbh%2FWcFMSOdEUPvCh63y0OkcFSUP2q1i%2FlwdqDeaG%2BD4%2BQ38xkdLiDyFcYF%2Bd44Wi9nY0RyAiuVVhxfDrCG4gB7u38%2BrCJvfkVv8XiuqKzkNzddSGMDyQ4RMJuW%2FWJmUg8xdjPbcNz7JUo%2BSSZBPo6jhiWTRx4QvxZFNOJfr6YWbpN96Epc1J%2Fw9rCOB3xqk7doLtWuPGgNIjFCYkS61BUgz1PDFJ61mTbLKBqIpjupIYgYRxZKAsUWuHo0EvJgPasgcBBbHizOk4jZ7yjL25SD5WWtgvJQIYHNxFO0VXuNnIGGoVv10Ucs03fbYt3EafCedWYYLRKVGSbRRiejv0f%2Fu%2F8kEahQsG0qupu9gQ%2BY9qbo%2BRt26IiT0PbrsCGfck%2Fc2YODXUd%2BXlIPpfEPGJvfU3jFzCGm5bUBjqkAQmlv4rl7EvoRe%2Fr7FCSrETnyLnpbYAdXXac593PymDUdW%2BthOvs5nDKf1uhFB%2BaH0%2FH2IbXTwS4CNBPqNajUxaDrXU3J5zTC5GVbICkGQqbF2P33c89ZR4nnxCZ04llEEVx%2FCB6iQIwxj2LjW9XySlZH3yw7GdXJymUR1U%2BWD5Cjo8KFf2%2BVoM0kb21bazO1HSp6bvsxg8PAB5DEwfcCTVH7b7d&X-Amz-Signature=86d9544a6a3b678c1ea6464da8e02e2fa261679156c0cce7cced7d53921bde99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MAUCF2%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T123450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTn4Sxa5JERyC%2B7r2s9RL%2FBcggS6RPbxv%2FF8JQlPROaAIhAMKiTRi05qZCnjaUEclM89TYLqMx1XgXIHyV48zg%2FEO4Kv8DCHQQABoMNjM3NDIzMTgzODA1IgzHcOLjJwwJlihUV8cq3AO87XZGWm7cdm327FYHkxBXogOacqKo7TCZiyeXO%2BpCkOB4w7cxa4ntDN2VwTl7LiHbT78Gb7sMtPjSuBf%2Fxrt%2BMW8NKYgaukw2kOam6CXjoYTs21BMDFHM9xXHOXg8YiGf5w%2FnvyoMNLwKbanNkESc6169vEU2ZWTok5wrm3LS2Ua2y3Q20I3PZ8j8aJ9iIU24s0jv0okSajp3VYEE8oa%2FaVVOj5kHhDZbh%2FWcFMSOdEUPvCh63y0OkcFSUP2q1i%2FlwdqDeaG%2BD4%2BQ38xkdLiDyFcYF%2Bd44Wi9nY0RyAiuVVhxfDrCG4gB7u38%2BrCJvfkVv8XiuqKzkNzddSGMDyQ4RMJuW%2FWJmUg8xdjPbcNz7JUo%2BSSZBPo6jhiWTRx4QvxZFNOJfr6YWbpN96Epc1J%2Fw9rCOB3xqk7doLtWuPGgNIjFCYkS61BUgz1PDFJ61mTbLKBqIpjupIYgYRxZKAsUWuHo0EvJgPasgcBBbHizOk4jZ7yjL25SD5WWtgvJQIYHNxFO0VXuNnIGGoVv10Ucs03fbYt3EafCedWYYLRKVGSbRRiejv0f%2Fu%2F8kEahQsG0qupu9gQ%2BY9qbo%2BRt26IiT0PbrsCGfck%2Fc2YODXUd%2BXlIPpfEPGJvfU3jFzCGm5bUBjqkAQmlv4rl7EvoRe%2Fr7FCSrETnyLnpbYAdXXac593PymDUdW%2BthOvs5nDKf1uhFB%2BaH0%2FH2IbXTwS4CNBPqNajUxaDrXU3J5zTC5GVbICkGQqbF2P33c89ZR4nnxCZ04llEEVx%2FCB6iQIwxj2LjW9XySlZH3yw7GdXJymUR1U%2BWD5Cjo8KFf2%2BVoM0kb21bazO1HSp6bvsxg8PAB5DEwfcCTVH7b7d&X-Amz-Signature=fad77c2b85ca043693402c35714046b0831f335de2b554b58a7a9289a59c890a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







