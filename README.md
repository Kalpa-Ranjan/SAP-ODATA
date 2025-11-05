



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2G2GAT%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T123205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjaw3mzIHeONRkb6rYPs2OexBOAxDlKaXS9sOdz%2Fn71AIhAJu1ZxWYPI8hBlb8dLUHCoN9GHgaV8b8%2BWOyeISOEKo2KogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxitU3pYnQbGhiaRsUq3ANF4OGx80FFlIAa9E7woZpvXq%2BMLqZzsFk1i9NU8%2BFl4zoUmRktq0Qwtoy61b6TlVir%2B8Z42%2Feenhs0NScYsEi4qQSX02MP0q7XXiZ%2FZQ0B%2Fj1OiuF82ZICua%2BOo0lEXuIeJO319CmzrNpDBcgI1A5q%2Fyy%2BHDlnCBmi0IQ5DpDPnrqdTkxDMQ5jPAHk6xGZyQiAIbaI8yRpVNhSYbzYa%2B9Sem6RrxhaJJkMAaHocMx0s8dxn6GKZxWGKZCbszZPeI8980GWwjM5EuBZ1qD8VSwiIzL9zghgMTO9qidt6JKOxynb5XpLO%2B90g2%2BEKSR5IZZUYiEw8m67w1bfkQe4twGGFAt41bCJRq6S7ADP1QZtfaqdRBxat1T22JvdkrFUFOfb9w9PqPaS%2FH9cxcejR0hP2sZlhQXkfdJvoJ03JM7RIzPDcrN%2FA%2BSk3O0dVMN2S2PFEanYRQd4f%2F4E660qet7D8UT0Bp4Qt7g5YG4%2Fmt8u1%2BwXrrKoDzWsPhbQFK3D0kTeemhBONbyozBkY%2BXWVSu77g1ese2Cw428L%2F8%2BgRXoHa7yT5sM72%2BwS0n7QqLxnnNRoXsnjoiv%2F53If3hjtFQB9pAgVM0TgEf0tuxZ8Z11NTjo1NAKn%2BGnZ9BJBjC65qzIBjqkATsNUnG4pym89zlzBfgOYFyTxmcmRNmM%2FsWbZDOD9sq3s6Mh4r0lgt8fhMzIkxQ3TuQpoOKKV6c5mrxak1IUxBbbelDY7v%2B657XlrG5KTSWgcu8PkgZwMdOAd%2FM5fvaab1Hm63ZL2uVvYmDqn5Irdnt%2B7JV53WUgzy9QtsNBf4tx%2Blivnze%2BIM0Y%2FG1p8wQGCY0qEYQTnApavf3Zj7ADXrYtS4HQ&X-Amz-Signature=327a7fe3648c4bd56e16ee1e2a3fc76fac77e8b2efa815c84800185cd20868f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2G2GAT%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T123205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjaw3mzIHeONRkb6rYPs2OexBOAxDlKaXS9sOdz%2Fn71AIhAJu1ZxWYPI8hBlb8dLUHCoN9GHgaV8b8%2BWOyeISOEKo2KogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxitU3pYnQbGhiaRsUq3ANF4OGx80FFlIAa9E7woZpvXq%2BMLqZzsFk1i9NU8%2BFl4zoUmRktq0Qwtoy61b6TlVir%2B8Z42%2Feenhs0NScYsEi4qQSX02MP0q7XXiZ%2FZQ0B%2Fj1OiuF82ZICua%2BOo0lEXuIeJO319CmzrNpDBcgI1A5q%2Fyy%2BHDlnCBmi0IQ5DpDPnrqdTkxDMQ5jPAHk6xGZyQiAIbaI8yRpVNhSYbzYa%2B9Sem6RrxhaJJkMAaHocMx0s8dxn6GKZxWGKZCbszZPeI8980GWwjM5EuBZ1qD8VSwiIzL9zghgMTO9qidt6JKOxynb5XpLO%2B90g2%2BEKSR5IZZUYiEw8m67w1bfkQe4twGGFAt41bCJRq6S7ADP1QZtfaqdRBxat1T22JvdkrFUFOfb9w9PqPaS%2FH9cxcejR0hP2sZlhQXkfdJvoJ03JM7RIzPDcrN%2FA%2BSk3O0dVMN2S2PFEanYRQd4f%2F4E660qet7D8UT0Bp4Qt7g5YG4%2Fmt8u1%2BwXrrKoDzWsPhbQFK3D0kTeemhBONbyozBkY%2BXWVSu77g1ese2Cw428L%2F8%2BgRXoHa7yT5sM72%2BwS0n7QqLxnnNRoXsnjoiv%2F53If3hjtFQB9pAgVM0TgEf0tuxZ8Z11NTjo1NAKn%2BGnZ9BJBjC65qzIBjqkATsNUnG4pym89zlzBfgOYFyTxmcmRNmM%2FsWbZDOD9sq3s6Mh4r0lgt8fhMzIkxQ3TuQpoOKKV6c5mrxak1IUxBbbelDY7v%2B657XlrG5KTSWgcu8PkgZwMdOAd%2FM5fvaab1Hm63ZL2uVvYmDqn5Irdnt%2B7JV53WUgzy9QtsNBf4tx%2Blivnze%2BIM0Y%2FG1p8wQGCY0qEYQTnApavf3Zj7ADXrYtS4HQ&X-Amz-Signature=b5abf718ad05e0737478f7a7a9035b9ce0280533fa837dc8b30a58dbfe36a716&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







