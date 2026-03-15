



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CR2U3TJ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T183140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT2R9zqVA5%2Fh%2FVP1DD4ddgkU8JJd%2FZ7hEbUT4PB3BPZwIgCX1wTpcTUtc0cpKCu4bkjVsy8bkwVs0qatp3ilq9N6IqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlbUa2KlEuX57wqzircA9YmYFaUepfFgYTS0QNYubfcGd9LKcDixiECkJHQUDKvOc%2BMq4SjrLKnaZ%2BT6eqogjGwykFv5tsRGY9J2E9lepkYQLDH%2F2pVU3wppvjYabrVb%2Be67DixAtDT3txJ0XeDD975PqXHE%2BJJjBYwhLNlDhLY%2FnPe6n%2BkrbSZE2WSe42joDgAotVdz69loj1bsRtgKIQwnXNgXyvp7fvjHOBz0Hsvy%2FU6RZC95%2BAaULD5zZtpFt2ShlgERxpQ6pKeWq0O%2FovCJP1SJAxZ6DBrO9HEktCvV6pxjPAbH9Hy9SXBjafcOSIVe8SY2za1rSX%2FbJwMnPXdGzOWE94KpxgSkrpObxQ%2FM9wyDXEMNeATqzEPJAiPJUaajFgcohST6bwWgLsvxVGseGwNcExh2uTNCHbFXHwoVHfRa1H3GxKZo32Z2r9PA3w4KtfeT5WfwtjOzjQXznearfT4gl9jR9W2usi0ypWlr%2BjyYn4lxoMm%2BEBwpJktchVMI%2Bcev8nMoNYy8Y7NWI9eDwk7ZXBVxZQ7%2BBJKfPfsQBSjQSh%2F2TLpjy5TWjt%2Beg3yoLt8K1LFsqSrAZaUuz21%2F2zQnTOjrQmZV26nCn9RnnA%2BhlRNKWCpLSJ9OZrNWjUrUanK2zLHS5R%2BMM2E280GOqUBonFSXMrIJCUNb%2FR2UtCwFjUV5xi2Yp015eE78fCXYrN1BgrXhCrYRionmyOMGLSh5ZIgHx%2FcRnH%2BXca4P7g7E%2B11G3rdB01IrTpLgKCmaJ7VTYj6bHKiiV9M2vE0155IXqPuqORcEtb1FK4G6CeTRBkX9U5mmeVp6aBpBbdDzKkQjqr1h5C8I85sp5S%2B6MVb%2FVotTCQFIcc1J5RJlngQ3HV9025W&X-Amz-Signature=0ae9ca4253fe15dd2c09d79fb8813c943b3cb99c2bf1af1e9827ef6e2f6f3ba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CR2U3TJ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T183140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT2R9zqVA5%2Fh%2FVP1DD4ddgkU8JJd%2FZ7hEbUT4PB3BPZwIgCX1wTpcTUtc0cpKCu4bkjVsy8bkwVs0qatp3ilq9N6IqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKlbUa2KlEuX57wqzircA9YmYFaUepfFgYTS0QNYubfcGd9LKcDixiECkJHQUDKvOc%2BMq4SjrLKnaZ%2BT6eqogjGwykFv5tsRGY9J2E9lepkYQLDH%2F2pVU3wppvjYabrVb%2Be67DixAtDT3txJ0XeDD975PqXHE%2BJJjBYwhLNlDhLY%2FnPe6n%2BkrbSZE2WSe42joDgAotVdz69loj1bsRtgKIQwnXNgXyvp7fvjHOBz0Hsvy%2FU6RZC95%2BAaULD5zZtpFt2ShlgERxpQ6pKeWq0O%2FovCJP1SJAxZ6DBrO9HEktCvV6pxjPAbH9Hy9SXBjafcOSIVe8SY2za1rSX%2FbJwMnPXdGzOWE94KpxgSkrpObxQ%2FM9wyDXEMNeATqzEPJAiPJUaajFgcohST6bwWgLsvxVGseGwNcExh2uTNCHbFXHwoVHfRa1H3GxKZo32Z2r9PA3w4KtfeT5WfwtjOzjQXznearfT4gl9jR9W2usi0ypWlr%2BjyYn4lxoMm%2BEBwpJktchVMI%2Bcev8nMoNYy8Y7NWI9eDwk7ZXBVxZQ7%2BBJKfPfsQBSjQSh%2F2TLpjy5TWjt%2Beg3yoLt8K1LFsqSrAZaUuz21%2F2zQnTOjrQmZV26nCn9RnnA%2BhlRNKWCpLSJ9OZrNWjUrUanK2zLHS5R%2BMM2E280GOqUBonFSXMrIJCUNb%2FR2UtCwFjUV5xi2Yp015eE78fCXYrN1BgrXhCrYRionmyOMGLSh5ZIgHx%2FcRnH%2BXca4P7g7E%2B11G3rdB01IrTpLgKCmaJ7VTYj6bHKiiV9M2vE0155IXqPuqORcEtb1FK4G6CeTRBkX9U5mmeVp6aBpBbdDzKkQjqr1h5C8I85sp5S%2B6MVb%2FVotTCQFIcc1J5RJlngQ3HV9025W&X-Amz-Signature=c88de3a4ce196f161581b100a6cacdff4f89b296cf2153889e5e3884cd98d216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







