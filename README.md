



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKBWH3Z3%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T182814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh7%2FDqA3%2BRUfOol1tuiv9AKq9xhYe90zwT8I%2BBqT13pwIhAMSkBD272%2BnSUfa4GGwVg0LnOQYdGbYKlfTqf2Gg8TIaKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAMX5Vkh1Fr1uX7I8q3AMkjpO1H3sCgMd8NSaYvdtrt9nMekMU%2FikRQPxLKASxshuPZF9wVWwwFBMfPtP8IWtmna6nUbxzjDWumBxnChf3ayE46R5E8D8Tu8t3A%2BlA0nA2T%2Bhc%2BKP1pQeoBepmk%2BGUW6Ym7b46RfQSlkKpnQ8vljGja1FLRpLaDIu%2BG9WL4WWgW%2FL4hMQ7LnvtWAPTfs4FRcJ62PNr5fF5rL%2FCahRZuhAlCB6zgdc5sV2SPMy7Wttlzn4eieAfIiT2VVFf%2BwFH5DgiLboyYbHgIVlGIEDrQgWgJDbnMqHXcU3al29%2BLvjRpbCi9LSQsIOxHMzSvW%2Fb7Du9FLFTUZ%2B0WT4ezwuTpP92PGVYb5JeUqy0OLSItjRyd%2FqF6HgOw68pVmDXmEIdk8ZYV2nnvusnIzWq%2Fp630gCtix%2BDnpOUuL5w6T4JEePH77SuuW5yagPMrySveAmBb%2BgXRXFaIPAWZcojHjd1RFu79PO1trHSXgKiBhpvWt0kTeGg8PazRzjrCOZE4zC6AaF2wsEyXPqE%2BGX%2BkK4nC%2BivA1Yfnm8QEjZDLfRHrBCz%2BiyH7Y8i4rDe6kfdsH9lrTjlEZ8fFEUBwkXR5UnaT9dbwWd8Rcwvlu6Hngsj0hXtmlYi2beEVyo8gTDf%2FKHUBjqkAcN7EYcBcEk8WpSrK6yzyOQHd1%2BOZhX6EnX1qeOYdTu4UDmkcGIca25GCYT781Z8C7E3wBBpPfgZbnyK06dEBbM%2BU%2FvJatcvOnfG4guLrhGoI7QtjZo904EbOMS9NdLXCCwebiqGIFRiVLGX%2B5KTLb1xABvjivA80Thq0QUzZFcOLbaONlq4UJj3tSsbXtjwPPNeiAXexsy6Iap85pB%2B6sKl7%2FXB&X-Amz-Signature=30169873656f28862498216790ce5a8eba4bc346bf7c64934ccdb6b608a2b3e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKBWH3Z3%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T182814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh7%2FDqA3%2BRUfOol1tuiv9AKq9xhYe90zwT8I%2BBqT13pwIhAMSkBD272%2BnSUfa4GGwVg0LnOQYdGbYKlfTqf2Gg8TIaKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAMX5Vkh1Fr1uX7I8q3AMkjpO1H3sCgMd8NSaYvdtrt9nMekMU%2FikRQPxLKASxshuPZF9wVWwwFBMfPtP8IWtmna6nUbxzjDWumBxnChf3ayE46R5E8D8Tu8t3A%2BlA0nA2T%2Bhc%2BKP1pQeoBepmk%2BGUW6Ym7b46RfQSlkKpnQ8vljGja1FLRpLaDIu%2BG9WL4WWgW%2FL4hMQ7LnvtWAPTfs4FRcJ62PNr5fF5rL%2FCahRZuhAlCB6zgdc5sV2SPMy7Wttlzn4eieAfIiT2VVFf%2BwFH5DgiLboyYbHgIVlGIEDrQgWgJDbnMqHXcU3al29%2BLvjRpbCi9LSQsIOxHMzSvW%2Fb7Du9FLFTUZ%2B0WT4ezwuTpP92PGVYb5JeUqy0OLSItjRyd%2FqF6HgOw68pVmDXmEIdk8ZYV2nnvusnIzWq%2Fp630gCtix%2BDnpOUuL5w6T4JEePH77SuuW5yagPMrySveAmBb%2BgXRXFaIPAWZcojHjd1RFu79PO1trHSXgKiBhpvWt0kTeGg8PazRzjrCOZE4zC6AaF2wsEyXPqE%2BGX%2BkK4nC%2BivA1Yfnm8QEjZDLfRHrBCz%2BiyH7Y8i4rDe6kfdsH9lrTjlEZ8fFEUBwkXR5UnaT9dbwWd8Rcwvlu6Hngsj0hXtmlYi2beEVyo8gTDf%2FKHUBjqkAcN7EYcBcEk8WpSrK6yzyOQHd1%2BOZhX6EnX1qeOYdTu4UDmkcGIca25GCYT781Z8C7E3wBBpPfgZbnyK06dEBbM%2BU%2FvJatcvOnfG4guLrhGoI7QtjZo904EbOMS9NdLXCCwebiqGIFRiVLGX%2B5KTLb1xABvjivA80Thq0QUzZFcOLbaONlq4UJj3tSsbXtjwPPNeiAXexsy6Iap85pB%2B6sKl7%2FXB&X-Amz-Signature=5d6ed22c4ab70c9cdcc2e6d875464f4d85b9e8df07bca2f18293b5de6b7ba8fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







