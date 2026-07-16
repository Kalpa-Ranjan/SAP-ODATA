



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7AUMMM%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T133901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCxtvldxL2%2Bf9zOeCJLiYt9PD4tZg8xqZjsYuYpXq4zdAIhAMhYDQBAzxxsLrBJ3GWJ8r6mIlUWzwJLG2F%2BMzyqlNHvKv8DCEUQABoMNjM3NDIzMTgzODA1IgwQBYAv5slsRBIHzKYq3AOPuj56z3nfU0O2yROoSI0Lbxmd8hDsn35bqwIICQERVwn3268YQV0cRx5s0JtXzVv%2BJTth6aBK7gzKZqfwmC6t3mw88eJ37Nr8d9hSnEZx2i7aATUCnaYaYJS4YC9%2FEUzxggeqgVP82BlWCq72Tm9hbK0u0vrvaG1aZpqiDDbux8%2BZFaLOM7uXnrgC2qyfgh0v5rRTh2RF3Fi5hilLl4r66Sn5Wy8WXQ7nngYQV%2BlY9gcyUMGw1EizAZaAAKAceDERsu0oeTkTrcYN4cs8Brah0bvQXe6AmPKUB3XJRYoUV4S213jXjXc%2BNRgTcmMhhkHLkd0nK1o4jACyAHkrhrbXCo7wWn2lhqYtJeV%2B7SaG6rilJ9Jcjh6lV083av1PDfycPqIf8z5XRqXBGURC0aZDJCBpA%2BiQZvcJpK%2B3hYyKpahTSSTcLZgAw1hQshrYV8szWLbuMlxKGlzWIKyKdiX8iVS0WwAaUtIRNFUy%2BEWmylhQwAn6Tzy%2B31om3MaACjTGTU%2F0NaUn3TihV9RUe8qxscmlmSbPZMO%2BeO1Zxdg5V0q2WR793WgZGdH%2BPxLj3l8Y895WBSQUYjKowf%2BHLZGKnQ9dlrb9dJ20XUsvdG7SsmjAz0AlYZmYdhSKoTDNjePSBjqkAYlqthw%2FXM8zCCbYCxqeV0AqVUk71YlhRnW6BfaODd70mdq6Cbd2dYZz4fCCcZDsYcNucdBV4eXU5GAuyYH%2BStVE%2FPJkRizhW58k%2BkH6u7f9db8559ij4CkOFsbxdSiLgvgWBL4esIv3964mtOXlPJ6ywtsGMu%2FFyowGlJYY%2FXwetCK5wEpTW%2BxSY4kBWw3BMdXh0tp2L4urHACWdjaO7iKvpKS0&X-Amz-Signature=065519f6d3809b90082934f765a1004c88913cfdbb0ae738a52442e9b2b244a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7AUMMM%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T133901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCxtvldxL2%2Bf9zOeCJLiYt9PD4tZg8xqZjsYuYpXq4zdAIhAMhYDQBAzxxsLrBJ3GWJ8r6mIlUWzwJLG2F%2BMzyqlNHvKv8DCEUQABoMNjM3NDIzMTgzODA1IgwQBYAv5slsRBIHzKYq3AOPuj56z3nfU0O2yROoSI0Lbxmd8hDsn35bqwIICQERVwn3268YQV0cRx5s0JtXzVv%2BJTth6aBK7gzKZqfwmC6t3mw88eJ37Nr8d9hSnEZx2i7aATUCnaYaYJS4YC9%2FEUzxggeqgVP82BlWCq72Tm9hbK0u0vrvaG1aZpqiDDbux8%2BZFaLOM7uXnrgC2qyfgh0v5rRTh2RF3Fi5hilLl4r66Sn5Wy8WXQ7nngYQV%2BlY9gcyUMGw1EizAZaAAKAceDERsu0oeTkTrcYN4cs8Brah0bvQXe6AmPKUB3XJRYoUV4S213jXjXc%2BNRgTcmMhhkHLkd0nK1o4jACyAHkrhrbXCo7wWn2lhqYtJeV%2B7SaG6rilJ9Jcjh6lV083av1PDfycPqIf8z5XRqXBGURC0aZDJCBpA%2BiQZvcJpK%2B3hYyKpahTSSTcLZgAw1hQshrYV8szWLbuMlxKGlzWIKyKdiX8iVS0WwAaUtIRNFUy%2BEWmylhQwAn6Tzy%2B31om3MaACjTGTU%2F0NaUn3TihV9RUe8qxscmlmSbPZMO%2BeO1Zxdg5V0q2WR793WgZGdH%2BPxLj3l8Y895WBSQUYjKowf%2BHLZGKnQ9dlrb9dJ20XUsvdG7SsmjAz0AlYZmYdhSKoTDNjePSBjqkAYlqthw%2FXM8zCCbYCxqeV0AqVUk71YlhRnW6BfaODd70mdq6Cbd2dYZz4fCCcZDsYcNucdBV4eXU5GAuyYH%2BStVE%2FPJkRizhW58k%2BkH6u7f9db8559ij4CkOFsbxdSiLgvgWBL4esIv3964mtOXlPJ6ywtsGMu%2FFyowGlJYY%2FXwetCK5wEpTW%2BxSY4kBWw3BMdXh0tp2L4urHACWdjaO7iKvpKS0&X-Amz-Signature=41dc42e176410f8ac0d31340d773bf0bb52d56705139e184216ba3fa70af1943&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







