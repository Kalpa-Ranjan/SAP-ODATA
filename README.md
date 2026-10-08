



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CNCZLAB%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T121204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIDkccCjitLddTLj15x9ua7J7ikGFYa1O29noNr7EJENAAiEAgFapl8QEz%2Fd4W9csu8Evr5wbmcugsP%2Be6scDVxqsdSsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNaRCNgQmbwg7QkqHCrcA%2BXi3O9CiKWvcVZU8mEYfCX0T1VVaaeKvf2tbvhbrzJZR94qr%2BP%2Bibr2KzPw9lubsfUCHtPF1q06beiPcFb0KDSs1kJS13xUlo0%2BqwlEM7x0CbETW2SfYUg2m3gvktaxnmPI49DH7rFqnStEr8S9ha8DIrfQlxdP3zjLjPAREbUkW2C%2FqndC7k6ItXNZ%2BLn2ALLHSZdHA6shjiJOyD%2FyKpo77wHQ%2BmptDZhQCoRhQBLDdaO4pYBkwc0xS0zJ5Mz8IFs0Z8Ucr3AURWpzEzGE4mhyJGlQeDpsDLquVpvnoOBigNj9V5%2FhseCVoZfcPdNifdlmoVyLhsb3r%2BhjrRLAlcf7wLSCVMFEzio1fxh6FxSOoALR32MrG1IQ5r9BRMqVOj5WnpkXDaJ7n3oo4xS%2Bzr1TyIYze6V3S7WpEYrhFATH49LEk%2BEkXMD9%2Bf13zkps0mvREpHmjk2Mnn5bbDaWn3DO4T%2BGD1U3ovQc4JHGe5TDj4n4j4cXkaQ%2FS9fZ0oGhKK%2BuW8EC2YCnuuhkwX76De5ax1elN630IsKKZl1EUl%2FX2Z2tBZW9zgfv%2FFM1gQdJ1X3U3jtU7GdNYnHJPFsLFfCXI21LFYmvcZbl23yKdOZNEUdIcH2DNMnEAmnhMOrsndYGOqUBmZYMFrfTCdgcMdaPwNb9C2Pwamx%2BGnjJznyf7gaq11OZ8dJAFDBrO6gwAkkJjXu1ClbuuVpy3YdpMU%2BZ60TqgvQVnbYTy1CX8Lczk4y5HIzp8w0xYILZLNJJEEJfHyVsvpA1E4HBtmimosBpSR88j%2B5D%2Fz0%2F23kZzKhIyX5yQrKgjpri8E%2BnrtTqZB57cTkttKBlM1im8e18v6eRE64jZT%2FvPAcX&X-Amz-Signature=8d8da22f427f6abbbfd03f84074753b14ae73ff3d1b486b39061be426ad1c2a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CNCZLAB%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T121204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIDkccCjitLddTLj15x9ua7J7ikGFYa1O29noNr7EJENAAiEAgFapl8QEz%2Fd4W9csu8Evr5wbmcugsP%2Be6scDVxqsdSsq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNaRCNgQmbwg7QkqHCrcA%2BXi3O9CiKWvcVZU8mEYfCX0T1VVaaeKvf2tbvhbrzJZR94qr%2BP%2Bibr2KzPw9lubsfUCHtPF1q06beiPcFb0KDSs1kJS13xUlo0%2BqwlEM7x0CbETW2SfYUg2m3gvktaxnmPI49DH7rFqnStEr8S9ha8DIrfQlxdP3zjLjPAREbUkW2C%2FqndC7k6ItXNZ%2BLn2ALLHSZdHA6shjiJOyD%2FyKpo77wHQ%2BmptDZhQCoRhQBLDdaO4pYBkwc0xS0zJ5Mz8IFs0Z8Ucr3AURWpzEzGE4mhyJGlQeDpsDLquVpvnoOBigNj9V5%2FhseCVoZfcPdNifdlmoVyLhsb3r%2BhjrRLAlcf7wLSCVMFEzio1fxh6FxSOoALR32MrG1IQ5r9BRMqVOj5WnpkXDaJ7n3oo4xS%2Bzr1TyIYze6V3S7WpEYrhFATH49LEk%2BEkXMD9%2Bf13zkps0mvREpHmjk2Mnn5bbDaWn3DO4T%2BGD1U3ovQc4JHGe5TDj4n4j4cXkaQ%2FS9fZ0oGhKK%2BuW8EC2YCnuuhkwX76De5ax1elN630IsKKZl1EUl%2FX2Z2tBZW9zgfv%2FFM1gQdJ1X3U3jtU7GdNYnHJPFsLFfCXI21LFYmvcZbl23yKdOZNEUdIcH2DNMnEAmnhMOrsndYGOqUBmZYMFrfTCdgcMdaPwNb9C2Pwamx%2BGnjJznyf7gaq11OZ8dJAFDBrO6gwAkkJjXu1ClbuuVpy3YdpMU%2BZ60TqgvQVnbYTy1CX8Lczk4y5HIzp8w0xYILZLNJJEEJfHyVsvpA1E4HBtmimosBpSR88j%2B5D%2Fz0%2F23kZzKhIyX5yQrKgjpri8E%2BnrtTqZB57cTkttKBlM1im8e18v6eRE64jZT%2FvPAcX&X-Amz-Signature=fd2767d2bba6ee0528c4af76a0d5f666c9e61dbe1e59e254e4123e80271eacbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







