



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUO2NOS2%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQCoWQ0WttbqHDDfMUQswxtkcH5p9yBkNaVPVGS1hx591wIhAMW%2BocZ3y1sABn4DuXYOzlGW6Gq141ur1JRpaOS3X%2FEHKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4OolVNL92Y%2BKx070q3ANRw41Q8CQCaxI0x4fnQoJXQLslOuGXW2vGPLKa9DtyqxSgZLTncRwvuRu3u7oq8usTJrI3AkDuGwGGRwTCxD94HIU7t5cbstC623YdJdPI4IyTRxYYbfhD45XKAFNY14J%2BRp9DCWuO3WzrecyJJolIcnfseUAmoNo2kwjxzFfKkOM0hhjudFv2uPZVQGBkoZFz1ixZP0MMS2iSTq9P9lg%2B%2BojIXcfqmJRac9x3cgTW39tS03nSNt4bMDxURqorcE8Wuh4ohr7johr6UAAMZxuWw3GCNuBjhiCgf8WOchCKnA3nuoOXIZz6S7oDpVmWGhW%2BBS%2BM4DiR0sGxBfS6mN%2FymATvTlF%2BOoBxaUPwbHRmCw%2BiV2AnjSOsEr0o4KFfN%2BwXiqs%2FnlldPPOlSAgFe1%2B2BcoJo7G6pqBshX%2F9V5Xlga7Oqb%2BlARN1G3%2FDTFOXQ2qribCAStC2eJWVGFWiUyWOiL5bhea9Cc%2B2v0sMURPIwGPL9sRskYNj9mcnXmmyGP2nPU1g7m2hek5wdskRbS%2BJEHbg2ETHgFxzMpqcaFstQvo8TzpIKCEi4ji0QRx%2BSYJmNhrob80e3zqD3NhJTatAnTLUwQrChVfNEjTVTGN2eLNNA8Fxs1uD6ZXX0DDzxo%2FIBjqkAaCT4jp7SAnYJTU4A5geYNMFxgX%2Bm3e8O8mPlBMTMliPq009ikS%2BeBhU002Y%2BCw%2B59Apd%2BwESBED42lXWsfm%2BEdgJA9m2uescTWzDXui2iz%2BLGUyVyn%2FUGW8%2FdvJqUnGl6ltdhFUf%2F8e4pnMnEqqaDupAH4FJuX1HKi%2FsE%2BZx1aqvxRFk96WEujcEUlOTt7PS4hWvCQtZrNE8qG%2BCIxaULgPWSKO&X-Amz-Signature=75e25017f5480b941abecfc1d6fc3215a79c01ae1f3acbe1fb2e0d8479cdca9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUO2NOS2%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQCoWQ0WttbqHDDfMUQswxtkcH5p9yBkNaVPVGS1hx591wIhAMW%2BocZ3y1sABn4DuXYOzlGW6Gq141ur1JRpaOS3X%2FEHKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4OolVNL92Y%2BKx070q3ANRw41Q8CQCaxI0x4fnQoJXQLslOuGXW2vGPLKa9DtyqxSgZLTncRwvuRu3u7oq8usTJrI3AkDuGwGGRwTCxD94HIU7t5cbstC623YdJdPI4IyTRxYYbfhD45XKAFNY14J%2BRp9DCWuO3WzrecyJJolIcnfseUAmoNo2kwjxzFfKkOM0hhjudFv2uPZVQGBkoZFz1ixZP0MMS2iSTq9P9lg%2B%2BojIXcfqmJRac9x3cgTW39tS03nSNt4bMDxURqorcE8Wuh4ohr7johr6UAAMZxuWw3GCNuBjhiCgf8WOchCKnA3nuoOXIZz6S7oDpVmWGhW%2BBS%2BM4DiR0sGxBfS6mN%2FymATvTlF%2BOoBxaUPwbHRmCw%2BiV2AnjSOsEr0o4KFfN%2BwXiqs%2FnlldPPOlSAgFe1%2B2BcoJo7G6pqBshX%2F9V5Xlga7Oqb%2BlARN1G3%2FDTFOXQ2qribCAStC2eJWVGFWiUyWOiL5bhea9Cc%2B2v0sMURPIwGPL9sRskYNj9mcnXmmyGP2nPU1g7m2hek5wdskRbS%2BJEHbg2ETHgFxzMpqcaFstQvo8TzpIKCEi4ji0QRx%2BSYJmNhrob80e3zqD3NhJTatAnTLUwQrChVfNEjTVTGN2eLNNA8Fxs1uD6ZXX0DDzxo%2FIBjqkAaCT4jp7SAnYJTU4A5geYNMFxgX%2Bm3e8O8mPlBMTMliPq009ikS%2BeBhU002Y%2BCw%2B59Apd%2BwESBED42lXWsfm%2BEdgJA9m2uescTWzDXui2iz%2BLGUyVyn%2FUGW8%2FdvJqUnGl6ltdhFUf%2F8e4pnMnEqqaDupAH4FJuX1HKi%2FsE%2BZx1aqvxRFk96WEujcEUlOTt7PS4hWvCQtZrNE8qG%2BCIxaULgPWSKO&X-Amz-Signature=0fa5c66b7ad915695f2a0e16f4630ca0fe6d72f72fcd1a6c102b31b431c24097&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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





Test Github-Notion synch



