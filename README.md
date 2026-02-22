



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7MNSIHH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T123844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdpJjKpl8bOozQ8%2F3crPwor%2FVe5Z8HHftz15CBrTFs5AiA%2BQD1dM5xDfnG27nVSn4MDgXRUxJcMXXEDygjmAdMTtSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHR0ob8RUm918bJQPKtwD8TEZPM6Rhbw7iuOn%2FmYuLji6rk1nTkD79nqUAswj%2F3CMYq1c5f3ON%2BJ9dKm%2Fi3PIvVDTpPnSbt0hvBpxAc%2Fj3ibl2LlrwuMbSnMAzSR%2BKqw%2B4dMNCJcp9CYcZ6K9%2BrsdshlVGxM2%2FB3ueD0PZ9ZrSg3djcJHqUxxgobDv9dFE0%2BYfvDEj5ivQD%2BA7wAcMCLWFkcpJNDfxBVFtQ0WYQq0QDxIs2oIm9sfSJw%2FUdZ4ldnLGqpLe6p%2F0xVvDrrlCjaT0tmIAf4K5zNqNbWrw5cm4cgZxrO5LDyg%2BoNAT2jx9356jqmeldqu%2FPjx9S7ItMBBaGZCnLM7%2BBuF8C8vPUkneQ3wKYFYquYiK19KDiq2qe6LIIGP2EKIgf5sU3Z%2Bhx3PN29p3pz%2FE2W%2BfBZhsNdSpbxp3zD6gRnjkGay48%2B1ihSQ6wuddx9KkaYTlK4o%2F0rXC9cJSq%2FD9U5bmf%2BnhjJNk48PD%2FfbRT7KY2SnnWGkynQkfKqJsZN5ajRB4zumhEUq0L%2BrSEDy5oKSaeK4GynR6e1lVD%2F%2B0eZGlnRicgXF11DtxSqyM%2FSr1n8NrjzS2%2BattfTm0kczRGkQG1aNGZD1jioKuTY2Pi%2BG0nwr0MFW%2Faqou59LyBZC2v3JCcYwgujrzAY6pgE28x2iq3pP3oekmBszkxrd5XXuNnwZcFVIc79AkkgLn1d8CFw3cxGdrIjcAqR1QV36%2FTXibh1HStqFjFtKW4JlzCnV7%2FQE925V66OLTg4hx6z6lyNBpk65HQLBLt65MPdXGvXpE8vKOy6BlJEYNQkJylKUMhioztYI7LQd3nCxNNjCTsNTqDb2cUlJrhw%2F8adafy7pcfVJpk9WUgko%2B3U8DygDDUi%2B&X-Amz-Signature=83b7510b7f53228ebe1466f983251b0e6a6d48305dfb761d9501e3d0962a59bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7MNSIHH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T123845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdpJjKpl8bOozQ8%2F3crPwor%2FVe5Z8HHftz15CBrTFs5AiA%2BQD1dM5xDfnG27nVSn4MDgXRUxJcMXXEDygjmAdMTtSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHR0ob8RUm918bJQPKtwD8TEZPM6Rhbw7iuOn%2FmYuLji6rk1nTkD79nqUAswj%2F3CMYq1c5f3ON%2BJ9dKm%2Fi3PIvVDTpPnSbt0hvBpxAc%2Fj3ibl2LlrwuMbSnMAzSR%2BKqw%2B4dMNCJcp9CYcZ6K9%2BrsdshlVGxM2%2FB3ueD0PZ9ZrSg3djcJHqUxxgobDv9dFE0%2BYfvDEj5ivQD%2BA7wAcMCLWFkcpJNDfxBVFtQ0WYQq0QDxIs2oIm9sfSJw%2FUdZ4ldnLGqpLe6p%2F0xVvDrrlCjaT0tmIAf4K5zNqNbWrw5cm4cgZxrO5LDyg%2BoNAT2jx9356jqmeldqu%2FPjx9S7ItMBBaGZCnLM7%2BBuF8C8vPUkneQ3wKYFYquYiK19KDiq2qe6LIIGP2EKIgf5sU3Z%2Bhx3PN29p3pz%2FE2W%2BfBZhsNdSpbxp3zD6gRnjkGay48%2B1ihSQ6wuddx9KkaYTlK4o%2F0rXC9cJSq%2FD9U5bmf%2BnhjJNk48PD%2FfbRT7KY2SnnWGkynQkfKqJsZN5ajRB4zumhEUq0L%2BrSEDy5oKSaeK4GynR6e1lVD%2F%2B0eZGlnRicgXF11DtxSqyM%2FSr1n8NrjzS2%2BattfTm0kczRGkQG1aNGZD1jioKuTY2Pi%2BG0nwr0MFW%2Faqou59LyBZC2v3JCcYwgujrzAY6pgE28x2iq3pP3oekmBszkxrd5XXuNnwZcFVIc79AkkgLn1d8CFw3cxGdrIjcAqR1QV36%2FTXibh1HStqFjFtKW4JlzCnV7%2FQE925V66OLTg4hx6z6lyNBpk65HQLBLt65MPdXGvXpE8vKOy6BlJEYNQkJylKUMhioztYI7LQd3nCxNNjCTsNTqDb2cUlJrhw%2F8adafy7pcfVJpk9WUgko%2B3U8DygDDUi%2B&X-Amz-Signature=33921c05e7caf0bdf0972e53261c200a521a2f72d2751ca5291c091fcb21e0a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







