



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKPYL4HS%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T064132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNtGJrSeMNSXs4SwaWFpOui9Tgenet2Ghnq4yCkjPv1QIhAPJr0P4VKttjil2N6vl5h1lUJV%2B0pjDqj96kTqs64u4CKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYtKIcA6VtSgMR4FQq3ANKBf1YbgnGJIW3MC49gWWLYzfrH0D5nf%2F%2B%2F0ACDbdaSmV5kpEsoFaeqTEMZZsjk7Z0Z4sPrMRVBUAtgWUDmG5PHyG1Xd2ReVT%2FdDY9z%2BVNJq6BCmfvfCR1j3if6Cxp3h3t%2BO1hBsWc2AwZzbeZDzrVkLM567M5SbZkq6%2BtCl3NyMbPjiDCtqmm4aRQn%2Fz7p%2BgyZt2QgBLCo%2FKrTlQnr9NhydwhcvAuhQYB9yxA0o%2B0NVoT2HABFd7U1wnS0Gl27dr1xIY5EMsKAy%2Bll9zUmu83T6yk5TC7TKWK7W9ngR6EPboVkEsEq6pSynle1zKdPdGaHoE7hoeRmMlqPVts2xWMmHGLvqxslx43K3YDc2CXSGgwazRC19lAlgpFtukliIRuQ9ngfG%2FKx9m3cv3u8sg3gQDHG8djWaA%2BvFpseIJ5b%2F6zXRjYmQ6Jlw0C6Crzil8HSkH6U6xchKLgGQP%2BbOVMyQ4%2BHzwOy3J16U6JjO8mUjx5euJU%2BBJLiShjtgtDsaGguVXOmLzYtfpxmVsqYRl0cRAuexhfIe1RTcIvZtVw%2FWmt1JqbGTBlvO3lagN1WDh4A7jntkLaIr9CgNks4nu%2FC3Qb%2Bd9DAVMPuhgmzvCvD4CxSLia9atGC5%2BbRDDCk%2FHLBjqkAf1HdSc6gDtT5TnULf0UcTM%2BO3zPF1erpc8aRf70LJpfpgVp4nsp43A%2FZS6IuBqu6obOrDkmkHje%2BKZinTqLjghJA8zxQmPIPN%2BuhMl5yPqW4nDzpwYbfxLzsQlLPG0s0kKDONUp5JCtUJ%2BjHvEzMvpKbI7SSAWIIuS5r7x4oCtTayQEus9f2%2BPRXOy%2FbHLrhB6ICXxFQicYKfd6lBB4CrPDNYb7&X-Amz-Signature=61cadacfdadc1f32cb2b2e885abb971a81ffe03ee2b4cff1022c056a58c5bdf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKPYL4HS%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T064132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNtGJrSeMNSXs4SwaWFpOui9Tgenet2Ghnq4yCkjPv1QIhAPJr0P4VKttjil2N6vl5h1lUJV%2B0pjDqj96kTqs64u4CKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYtKIcA6VtSgMR4FQq3ANKBf1YbgnGJIW3MC49gWWLYzfrH0D5nf%2F%2B%2F0ACDbdaSmV5kpEsoFaeqTEMZZsjk7Z0Z4sPrMRVBUAtgWUDmG5PHyG1Xd2ReVT%2FdDY9z%2BVNJq6BCmfvfCR1j3if6Cxp3h3t%2BO1hBsWc2AwZzbeZDzrVkLM567M5SbZkq6%2BtCl3NyMbPjiDCtqmm4aRQn%2Fz7p%2BgyZt2QgBLCo%2FKrTlQnr9NhydwhcvAuhQYB9yxA0o%2B0NVoT2HABFd7U1wnS0Gl27dr1xIY5EMsKAy%2Bll9zUmu83T6yk5TC7TKWK7W9ngR6EPboVkEsEq6pSynle1zKdPdGaHoE7hoeRmMlqPVts2xWMmHGLvqxslx43K3YDc2CXSGgwazRC19lAlgpFtukliIRuQ9ngfG%2FKx9m3cv3u8sg3gQDHG8djWaA%2BvFpseIJ5b%2F6zXRjYmQ6Jlw0C6Crzil8HSkH6U6xchKLgGQP%2BbOVMyQ4%2BHzwOy3J16U6JjO8mUjx5euJU%2BBJLiShjtgtDsaGguVXOmLzYtfpxmVsqYRl0cRAuexhfIe1RTcIvZtVw%2FWmt1JqbGTBlvO3lagN1WDh4A7jntkLaIr9CgNks4nu%2FC3Qb%2Bd9DAVMPuhgmzvCvD4CxSLia9atGC5%2BbRDDCk%2FHLBjqkAf1HdSc6gDtT5TnULf0UcTM%2BO3zPF1erpc8aRf70LJpfpgVp4nsp43A%2FZS6IuBqu6obOrDkmkHje%2BKZinTqLjghJA8zxQmPIPN%2BuhMl5yPqW4nDzpwYbfxLzsQlLPG0s0kKDONUp5JCtUJ%2BjHvEzMvpKbI7SSAWIIuS5r7x4oCtTayQEus9f2%2BPRXOy%2FbHLrhB6ICXxFQicYKfd6lBB4CrPDNYb7&X-Amz-Signature=97660dc28dedd4b263b9cfa4349e8119212f64cd0dbea11d040648c78af21c27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







