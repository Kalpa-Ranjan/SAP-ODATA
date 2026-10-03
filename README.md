



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNGIG5GB%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T002044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBedj7xBjZHjWAApSL%2B9OIJqWwjehIKiY86WRVIXskWKAiBAyuH5yecqcwdUInQlONmGuIlUz2AeY%2FCch6haFf49JyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGf8MKBZv0VZBATP7KtwDip8NRlbx%2BdXNQYjyTTGFkDiNLWTNf4idwgJUlNdVSQiAhamb0gMDsHo%2FRWHoyEcxPqQ7%2FoDzLA%2FEsuToadWwEc7ahfi6xT66F5m%2FncGqk9dBstV3oTWGcWoloJg9Avv2Z9zB%2F1FqnpWekDU5EBx%2FPZnZbKXIYxGsYq4jsuo1iDwrlNqNZaWUZ0bPLqElnm%2BLIcXTURf1yR4M%2BBb5oPHyvV9BBQDdclJH%2FRjU%2FUS7LhM9jQg35yF723u7omvLuKr7t6HCydUHp5kUdKCXQrqlbpy3oUcdPqj0tihZdWP3hPDjZy6IaxLj81Un74608XvijWf%2F%2BfmFSeIOtGvEt2EPuPr2bjLnTU8BLfcXZg1d727zP5AduwVfao8bm17va4mwIwURN%2FRqwpyB1fL%2F9NLg5tl6R%2BFZbmMQpMXrbNrs4ki0gVb%2Bmbjb7aj0JYNc5RTdKmWA5a%2FkZH0AnP4PB0YGbSuUM0wcrjbQnB2rlZH%2BQOTszPhIoaFiZuF7bCuYgsu9Gy17GvzkcJoTvf5SyQoeX%2FH56Zr1bl2gQ%2B7%2Fbk1YB3PUe%2BzFtZOzyqYoUr5O6%2FdK30AN38YI%2BiFVR4kBuz1dIl8WO0U6hFcwbx1JfExXBc7ck5jBHqgu39JQhbIwut2A1gY6pgFV2ZI%2FrTpXgxkKFIXBcUDZNBjD6ZgICNLmlmxkCdu381PTpKkRAm5UN9JZrrfl0D5tIBsUPHXheJpDHfLSJ5MregiQhCYdyrmce5F3MW5nfmLDPacVbeH2mgI9hJyNAl5SavNKuKe%2Fk74SptV4qJlZLrDHmXerRMC7byJr1i0bAF8cILk4yhnrl1cVrFkSyBZjIUGJ5gaqpcTPGVJC6XPs1Gm8RIYN&X-Amz-Signature=5d217149acdd7bc7e6de99ec9480c86cf86dfe3e72bff825029412241a77a5c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNGIG5GB%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T002044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBedj7xBjZHjWAApSL%2B9OIJqWwjehIKiY86WRVIXskWKAiBAyuH5yecqcwdUInQlONmGuIlUz2AeY%2FCch6haFf49JyqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGf8MKBZv0VZBATP7KtwDip8NRlbx%2BdXNQYjyTTGFkDiNLWTNf4idwgJUlNdVSQiAhamb0gMDsHo%2FRWHoyEcxPqQ7%2FoDzLA%2FEsuToadWwEc7ahfi6xT66F5m%2FncGqk9dBstV3oTWGcWoloJg9Avv2Z9zB%2F1FqnpWekDU5EBx%2FPZnZbKXIYxGsYq4jsuo1iDwrlNqNZaWUZ0bPLqElnm%2BLIcXTURf1yR4M%2BBb5oPHyvV9BBQDdclJH%2FRjU%2FUS7LhM9jQg35yF723u7omvLuKr7t6HCydUHp5kUdKCXQrqlbpy3oUcdPqj0tihZdWP3hPDjZy6IaxLj81Un74608XvijWf%2F%2BfmFSeIOtGvEt2EPuPr2bjLnTU8BLfcXZg1d727zP5AduwVfao8bm17va4mwIwURN%2FRqwpyB1fL%2F9NLg5tl6R%2BFZbmMQpMXrbNrs4ki0gVb%2Bmbjb7aj0JYNc5RTdKmWA5a%2FkZH0AnP4PB0YGbSuUM0wcrjbQnB2rlZH%2BQOTszPhIoaFiZuF7bCuYgsu9Gy17GvzkcJoTvf5SyQoeX%2FH56Zr1bl2gQ%2B7%2Fbk1YB3PUe%2BzFtZOzyqYoUr5O6%2FdK30AN38YI%2BiFVR4kBuz1dIl8WO0U6hFcwbx1JfExXBc7ck5jBHqgu39JQhbIwut2A1gY6pgFV2ZI%2FrTpXgxkKFIXBcUDZNBjD6ZgICNLmlmxkCdu381PTpKkRAm5UN9JZrrfl0D5tIBsUPHXheJpDHfLSJ5MregiQhCYdyrmce5F3MW5nfmLDPacVbeH2mgI9hJyNAl5SavNKuKe%2Fk74SptV4qJlZLrDHmXerRMC7byJr1i0bAF8cILk4yhnrl1cVrFkSyBZjIUGJ5gaqpcTPGVJC6XPs1Gm8RIYN&X-Amz-Signature=eed49019baeb5e1edae110b3645bb35bcc52ab5bb4b082766116039588511bb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







