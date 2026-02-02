



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IAYTJ6X%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T124843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCICaoc1KTvXSkfXdk1CWjB0Lt2usqCd1M0l%2F7fh1gckmjAiB09bejYy0AatgEaYEdnrR1L72EoKm9kM4NP8%2BUkhZhSSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrVlotfR40zTWLODPKtwD4jpn%2FlGkKVTPqXeTTAe12owRPCciraagZ7VJjNNuHGrDr7XfjG31vXT4NZN6XjR7lXOoSjSVULX1JKWq4lHgP3XzUlmMYYvBoZqpbJpC01S%2B4GVM26TjxZCj%2F622IZVzRTrxwth8lBdjEKUIITjVqta5DW5iIbNmNI4cvrOTxH5bf0z3Dp3qfFPYqK34tgjIEOZ8jrpMWxZOeyE518esEn1%2FMmca78eWoe3b1ojstSo1a%2FWi6wgLoQv2bPBn2nVkiklFfu1NNuWaum3TNOloBsdooXc%2BfFcWF1ChIfLv8PPatGx4oLjiqif1qOw44MvdjaER%2FpRjE%2FeU2AUog%2Bcg7gCgKYCyIs3W34IvjfkernjNU7dC3UG7GP%2BzInnJVFLF%2Bm89rzcmCYuNseLz3g1XqyqEisLU7Z5kNGuJAJO0LgeqDClsetOo5nulcEhA6ewVBbiI%2FoUY88pGAczhWkzCItNsrS9MjuL6FhPLVW7jx6fJ7K411swQzaNcoKYf%2B%2BiAxlVeGMjF0OrzUFZ3Gli4KqWm1Q7iqOeZYVctH40mspIal0%2FD4TyeU7qiJK3aJ96sH%2F8rPD5wF83q95kdK8urekPvWMIySjkDiaEWR0yBVX4diewsfqT%2FmQSD1KkwipqCzAY6pgF%2FFe7TH7botVnjjmsySzlbUeKBv0G0wESoTsBfqJd7n69P0UhZlrRrnnCTE6b00HDYo7RtG3QUvuEwbAKOw3bYFOvyV6VQVXYmxdYPPb73uNAgFlDelMTOEYQPrdkBX0epEtCwIR9PsgD5mH%2BIRwwVRtiMrf3KjecNQWuFEPbybyDicuK4DZGBC0fPHG03X3vl%2BFAMB7feDb8ZVcUqPpcTWVX87Q9p&X-Amz-Signature=44795ae53a9696ec3d6d542d26fe3bcd192a8018bcee7d8ae8d8251b9a5c573b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IAYTJ6X%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T124843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCICaoc1KTvXSkfXdk1CWjB0Lt2usqCd1M0l%2F7fh1gckmjAiB09bejYy0AatgEaYEdnrR1L72EoKm9kM4NP8%2BUkhZhSSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrVlotfR40zTWLODPKtwD4jpn%2FlGkKVTPqXeTTAe12owRPCciraagZ7VJjNNuHGrDr7XfjG31vXT4NZN6XjR7lXOoSjSVULX1JKWq4lHgP3XzUlmMYYvBoZqpbJpC01S%2B4GVM26TjxZCj%2F622IZVzRTrxwth8lBdjEKUIITjVqta5DW5iIbNmNI4cvrOTxH5bf0z3Dp3qfFPYqK34tgjIEOZ8jrpMWxZOeyE518esEn1%2FMmca78eWoe3b1ojstSo1a%2FWi6wgLoQv2bPBn2nVkiklFfu1NNuWaum3TNOloBsdooXc%2BfFcWF1ChIfLv8PPatGx4oLjiqif1qOw44MvdjaER%2FpRjE%2FeU2AUog%2Bcg7gCgKYCyIs3W34IvjfkernjNU7dC3UG7GP%2BzInnJVFLF%2Bm89rzcmCYuNseLz3g1XqyqEisLU7Z5kNGuJAJO0LgeqDClsetOo5nulcEhA6ewVBbiI%2FoUY88pGAczhWkzCItNsrS9MjuL6FhPLVW7jx6fJ7K411swQzaNcoKYf%2B%2BiAxlVeGMjF0OrzUFZ3Gli4KqWm1Q7iqOeZYVctH40mspIal0%2FD4TyeU7qiJK3aJ96sH%2F8rPD5wF83q95kdK8urekPvWMIySjkDiaEWR0yBVX4diewsfqT%2FmQSD1KkwipqCzAY6pgF%2FFe7TH7botVnjjmsySzlbUeKBv0G0wESoTsBfqJd7n69P0UhZlrRrnnCTE6b00HDYo7RtG3QUvuEwbAKOw3bYFOvyV6VQVXYmxdYPPb73uNAgFlDelMTOEYQPrdkBX0epEtCwIR9PsgD5mH%2BIRwwVRtiMrf3KjecNQWuFEPbybyDicuK4DZGBC0fPHG03X3vl%2BFAMB7feDb8ZVcUqPpcTWVX87Q9p&X-Amz-Signature=dbd4f34079ae83af24525f98033ae1d8c65116c54d7c2c61310a0582cd464697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







