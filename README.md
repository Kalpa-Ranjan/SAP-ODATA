



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM4D3LQ3%2F20261024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261024T120928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDkxrPJH6Hj4bwcsoZ%2B2Q7vqq4IGNL1GrJuGQ%2Bh93zhgIhALZcp5r3CFDBX0lVUCBq3Uy9vMilL1SvW8JH1Z5fMPbyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyi6Cmbw%2FBUaV8f1n0q3AMi4TtRPxb6NLRRJNHEt2hCMSv4mFBZxJW9k4OKqHl5QUqfziwFjWWzDB%2Fx1RVTQrTcxF62qyN%2F0P7cHKcqyvQTLX0SPpWjMumOM1nrWQUW7evIfuR6lSEJguTJXCJVruSs9VwXz1CQEmM8tz2qZ0FmktLn%2FSQEV6lf1rM7lcEOvngz%2F8FDhyArSUTKAAqYsLQ%2FXjZLWmaO%2FgHRBjxVdlpB6C4K7qY8EaoG127AJvErU7nnxm6lEtAZcP9NUhdG0nCKNDm7ug5%2FgE%2Fa%2BCFT4jdSnckvE5yre3jlWbVXlo3IjR5lRvEXJEs5Auiq66mAdOMO7W5vSGFp1wrh1jzpNiU4s436NiCl4oADlrXzuwrJ5WbbSGksjA7Z9vbuUTRb2fU0sBJ12CqV8XfRkwno3SJbfWyfqNwTna4mkYfWYuRGDCZx7IIRYbC083LdDSVxb483JC4Y3yMp7m53VmNBMevcoEVhAxMtiifOjukZUKqjeXEuIcVb7mRxgEa7UgwtNJsEysEbfpxGtuJI3mkBJoNtQhQIDmZn9pg%2BIBZrtPfDILLGnDy2%2BqAjOVFRPCtYTwvJ%2B9zTjs3VQZ6g%2BZ5ry90VcUDAYspk3mO3IBCSu6bdrloguIGLYzKnZk2NozCdqPLWBjqkAV3uLuunIbIJM1sigoSHkYlEUI94EU%2Fgadvyh3bCr%2Ft6gdL0Dm6CpyW2WI6fRYIQ923U%2BWKy4rAC5K4uNCh4osZj0ZjRvDxMSuoIBdEVGS%2F9IOayAVLzjVLbYyKrvZWJVo978Uvyiy4ZNBNnpVtGj2KxBx7O6gYlF0o8%2FnWMWpH5hRQ1v1egoei0jXXD9IIX50aQGK%2Fv%2F2yS8UKw6T4NIzgtYtlL&X-Amz-Signature=56065731c1865726026d68ba901b0d213edb61f116f27b543ebb448c68224c0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM4D3LQ3%2F20261024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261024T120928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDkxrPJH6Hj4bwcsoZ%2B2Q7vqq4IGNL1GrJuGQ%2Bh93zhgIhALZcp5r3CFDBX0lVUCBq3Uy9vMilL1SvW8JH1Z5fMPbyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyi6Cmbw%2FBUaV8f1n0q3AMi4TtRPxb6NLRRJNHEt2hCMSv4mFBZxJW9k4OKqHl5QUqfziwFjWWzDB%2Fx1RVTQrTcxF62qyN%2F0P7cHKcqyvQTLX0SPpWjMumOM1nrWQUW7evIfuR6lSEJguTJXCJVruSs9VwXz1CQEmM8tz2qZ0FmktLn%2FSQEV6lf1rM7lcEOvngz%2F8FDhyArSUTKAAqYsLQ%2FXjZLWmaO%2FgHRBjxVdlpB6C4K7qY8EaoG127AJvErU7nnxm6lEtAZcP9NUhdG0nCKNDm7ug5%2FgE%2Fa%2BCFT4jdSnckvE5yre3jlWbVXlo3IjR5lRvEXJEs5Auiq66mAdOMO7W5vSGFp1wrh1jzpNiU4s436NiCl4oADlrXzuwrJ5WbbSGksjA7Z9vbuUTRb2fU0sBJ12CqV8XfRkwno3SJbfWyfqNwTna4mkYfWYuRGDCZx7IIRYbC083LdDSVxb483JC4Y3yMp7m53VmNBMevcoEVhAxMtiifOjukZUKqjeXEuIcVb7mRxgEa7UgwtNJsEysEbfpxGtuJI3mkBJoNtQhQIDmZn9pg%2BIBZrtPfDILLGnDy2%2BqAjOVFRPCtYTwvJ%2B9zTjs3VQZ6g%2BZ5ry90VcUDAYspk3mO3IBCSu6bdrloguIGLYzKnZk2NozCdqPLWBjqkAV3uLuunIbIJM1sigoSHkYlEUI94EU%2Fgadvyh3bCr%2Ft6gdL0Dm6CpyW2WI6fRYIQ923U%2BWKy4rAC5K4uNCh4osZj0ZjRvDxMSuoIBdEVGS%2F9IOayAVLzjVLbYyKrvZWJVo978Uvyiy4ZNBNnpVtGj2KxBx7O6gYlF0o8%2FnWMWpH5hRQ1v1egoei0jXXD9IIX50aQGK%2Fv%2F2yS8UKw6T4NIzgtYtlL&X-Amz-Signature=1d099e863880f5476ed8cd8e0f9fd03abd3188c1fb145a6e862ec54c030c0aba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







