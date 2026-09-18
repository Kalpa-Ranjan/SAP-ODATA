



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV626JNU%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T061302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCioX7dFZjb1Ctop6iK8nM6tTv2KT8M6woqPDzjjPT5MAIhAM6VCbZqbMywUMupj48CB7ZTfuVdNHVP8PM6Ew6wxeDhKv8DCD0QABoMNjM3NDIzMTgzODA1Igy3xvv0LRVY2A%2Bv%2F7Iq3AMms0hqLAM3IL163ocnYS9iaslg2jJ9ym0WJz46IrbupwoChWjwIEZOe0r1MncpE1MKUDV%2BIqUfWYCD6AAld3Epd1IgPZSSWI7%2Br6ny0prY9P1NaXVyN9O6migL2Dx4ydDTyJmPqZytQDlLqb9soj195IgSl6%2FORbli8tTfZNfsYkaIwGLoxUSrJ%2BW7bndeJBY5064xQRIx3xv51vmyFlZ0wyn2B180sj%2FPqgnE9pQRL0xFvFpty0usCDzQCkQqdJfMAUkxlVJwwA5H2aNtS%2FDzCIzF9E5xhS0aSoeIJVge%2BZE7B206s9oF3Vr8cpR9pIZO1LSrPM0x9lFrjIkQItXLLivA8k54R%2F7JTWbhyJg3zFhwcuxnWNAdpc9t%2FulsVNPPFQgpn3jfL9wstKCVh%2F3ybhC1Kq3hmoFcOo6YOsXrQORjfj08%2Bv4394PHVUc1Jzg8a8ydJzm24ITeSqdcGJEYKDMIBBdwq8Tkb6t80I%2FAIwmtNYf3Nb7RVfjdZaiNKYWTP4reve471ccCb%2FGA5hRCVZKucD65dbqZ7Ev5IbvZ21o%2F%2Fdm2DLkDsxo0zztrkTkN3tipPw2r9R3Gx9uSG4EWgNu5S4c6i6N3kRilf4pC27G%2Bfq0PlUEAGOXosjDZ97LVBjqkASoTTGGacyC5c%2FAQ5pCPd9cLqcORt2nk%2F%2BUIrj98jv4vs2eNrUaXY%2FmMIBJ2naSOHCK46bAoMnGeA%2BccAxq5wIxxoEGQoav%2BGu8CZEFZr%2B2eMXDJ1daXPwJ%2BdxHFfSwDiuEGK%2Bzvy5tmntT5O0CeNnGfS%2BfYAV0Ky7yG9l8O18Vm8w1MEm4GDezPuPEFZkn%2BwMcF9hye9jDw%2FjxNCiWLOBTOMoki&X-Amz-Signature=3c4b542cfce38a6c496a4baa4ad67d20ab3063a7bb0dadb65a27db1f1019e540&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV626JNU%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T061302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCioX7dFZjb1Ctop6iK8nM6tTv2KT8M6woqPDzjjPT5MAIhAM6VCbZqbMywUMupj48CB7ZTfuVdNHVP8PM6Ew6wxeDhKv8DCD0QABoMNjM3NDIzMTgzODA1Igy3xvv0LRVY2A%2Bv%2F7Iq3AMms0hqLAM3IL163ocnYS9iaslg2jJ9ym0WJz46IrbupwoChWjwIEZOe0r1MncpE1MKUDV%2BIqUfWYCD6AAld3Epd1IgPZSSWI7%2Br6ny0prY9P1NaXVyN9O6migL2Dx4ydDTyJmPqZytQDlLqb9soj195IgSl6%2FORbli8tTfZNfsYkaIwGLoxUSrJ%2BW7bndeJBY5064xQRIx3xv51vmyFlZ0wyn2B180sj%2FPqgnE9pQRL0xFvFpty0usCDzQCkQqdJfMAUkxlVJwwA5H2aNtS%2FDzCIzF9E5xhS0aSoeIJVge%2BZE7B206s9oF3Vr8cpR9pIZO1LSrPM0x9lFrjIkQItXLLivA8k54R%2F7JTWbhyJg3zFhwcuxnWNAdpc9t%2FulsVNPPFQgpn3jfL9wstKCVh%2F3ybhC1Kq3hmoFcOo6YOsXrQORjfj08%2Bv4394PHVUc1Jzg8a8ydJzm24ITeSqdcGJEYKDMIBBdwq8Tkb6t80I%2FAIwmtNYf3Nb7RVfjdZaiNKYWTP4reve471ccCb%2FGA5hRCVZKucD65dbqZ7Ev5IbvZ21o%2F%2Fdm2DLkDsxo0zztrkTkN3tipPw2r9R3Gx9uSG4EWgNu5S4c6i6N3kRilf4pC27G%2Bfq0PlUEAGOXosjDZ97LVBjqkASoTTGGacyC5c%2FAQ5pCPd9cLqcORt2nk%2F%2BUIrj98jv4vs2eNrUaXY%2FmMIBJ2naSOHCK46bAoMnGeA%2BccAxq5wIxxoEGQoav%2BGu8CZEFZr%2B2eMXDJ1daXPwJ%2BdxHFfSwDiuEGK%2Bzvy5tmntT5O0CeNnGfS%2BfYAV0Ky7yG9l8O18Vm8w1MEm4GDezPuPEFZkn%2BwMcF9hye9jDw%2FjxNCiWLOBTOMoki&X-Amz-Signature=c150665188a1e99c778285ae9019f817906a0a8890ebac7ea8122f9cb9bf79dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







