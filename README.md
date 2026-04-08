



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCO5KBPW%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T071113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDe3d9ecxuPWhTNsZgbqFrgTW6kJ%2Fc6q4WkNIVJf1j0zAIhAM56sHWUkwbliiweHQgF8WYtDAswXz0B6xeLkG4KqnFoKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZhKB1QQFnZmV7MNsq3AM2%2FFquZ6ONvGtr7dtrMzuZhXjQMlFqI2j3ha0VwTsvBDp17sF%2BmKB6KNZrj9WNnKaeGc15GDHQvo174gMGNUeMbjk%2FfDRYeHOpnkDMh8C%2BJVRXT8zp8TL7%2F%2FyxB0iWfrFj2t%2BrDrn7x3vL24JLv1hNrz9BTxy4t5gOcWDbUDA%2BNLQmeb2SghfJ6fnv%2B33uQ%2Fjb5W%2BiXNo6%2FpTg4N35KPBBYtsBH1mPyGpRlUo%2Bva2gakTTDylAKc%2B%2FgCUaOCoYlDE8qZSANP%2FJm%2BcRPwEB9uCW4oygxEpJOxk%2Bkm5hThXn0YpFfmwWTBYTzM%2B1xNWyMJSHsuCjyK8xdYc03ftt3LOm6P6lub7s6G%2B2r9ZsiS87KWrEjelZmqdnIdhBdp06l7fJUeDKW8HJQx5mDFLEYQsvbyIiBnDVSsteDgF7iaOqSsfB5GmyJ9fpUX7PFGkeJpKg4TGjP2a%2BfpxL%2FSsjS2Brs6gj5Lm8OPOQdIGpazer5xeFWwXoME6VIbMMqTZl4y5Ahppm2mXWJhhuuLawJPeWhJ7nrbYAJ72Hj0g8vpy4pCuJ6dDdV4VJ2qM6TyieyZvQEdYBehdyeBOdqCiD0gJEoSWhhdJltm3ABEr1zfINW2qq8gQcGoEJzWBvFzDv9dfOBjqkAc95loCcn7V1s6vKhwhMzcANs0e7mkzxNHYG%2BPKyvlsL4vl9p00CDk8LS9MR%2BVeeMhl1TKMXGEWbtvpJybvL8JrMzpuVtmEkM4aeukTROaiz4wpVyMeCUrIAfpjnTHhzPNjqKASSRVdxFptYPGgZr%2FGZ1pIOJZXFq1bUwIR0CrbmMek3alU5SH5ESD6ThfDcPF%2BXdk7DP1r3RI3sjQwFLACJoEBM&X-Amz-Signature=f6566922d44fb5f2d213dfe7a40984acd21f0eceae8d0cc86d181971ceba8a4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCO5KBPW%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T071113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDe3d9ecxuPWhTNsZgbqFrgTW6kJ%2Fc6q4WkNIVJf1j0zAIhAM56sHWUkwbliiweHQgF8WYtDAswXz0B6xeLkG4KqnFoKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZhKB1QQFnZmV7MNsq3AM2%2FFquZ6ONvGtr7dtrMzuZhXjQMlFqI2j3ha0VwTsvBDp17sF%2BmKB6KNZrj9WNnKaeGc15GDHQvo174gMGNUeMbjk%2FfDRYeHOpnkDMh8C%2BJVRXT8zp8TL7%2F%2FyxB0iWfrFj2t%2BrDrn7x3vL24JLv1hNrz9BTxy4t5gOcWDbUDA%2BNLQmeb2SghfJ6fnv%2B33uQ%2Fjb5W%2BiXNo6%2FpTg4N35KPBBYtsBH1mPyGpRlUo%2Bva2gakTTDylAKc%2B%2FgCUaOCoYlDE8qZSANP%2FJm%2BcRPwEB9uCW4oygxEpJOxk%2Bkm5hThXn0YpFfmwWTBYTzM%2B1xNWyMJSHsuCjyK8xdYc03ftt3LOm6P6lub7s6G%2B2r9ZsiS87KWrEjelZmqdnIdhBdp06l7fJUeDKW8HJQx5mDFLEYQsvbyIiBnDVSsteDgF7iaOqSsfB5GmyJ9fpUX7PFGkeJpKg4TGjP2a%2BfpxL%2FSsjS2Brs6gj5Lm8OPOQdIGpazer5xeFWwXoME6VIbMMqTZl4y5Ahppm2mXWJhhuuLawJPeWhJ7nrbYAJ72Hj0g8vpy4pCuJ6dDdV4VJ2qM6TyieyZvQEdYBehdyeBOdqCiD0gJEoSWhhdJltm3ABEr1zfINW2qq8gQcGoEJzWBvFzDv9dfOBjqkAc95loCcn7V1s6vKhwhMzcANs0e7mkzxNHYG%2BPKyvlsL4vl9p00CDk8LS9MR%2BVeeMhl1TKMXGEWbtvpJybvL8JrMzpuVtmEkM4aeukTROaiz4wpVyMeCUrIAfpjnTHhzPNjqKASSRVdxFptYPGgZr%2FGZ1pIOJZXFq1bUwIR0CrbmMek3alU5SH5ESD6ThfDcPF%2BXdk7DP1r3RI3sjQwFLACJoEBM&X-Amz-Signature=2ae6e0daf2fc334ffb191522ff63ffb88d971f0afba6d02e3fa4a2dbc7fc0909&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







