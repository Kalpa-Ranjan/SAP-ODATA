



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W62OWD6I%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T124630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoDigySwBJWe%2FUty7RQxT8NCURkuiSaPFKNXlpfAFSkAiBm5yrFscmeN0T7hh45oeUE3V%2B5LAJL4zO2iQp04syBviqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4OVl%2Fn%2FWLI%2Bm5zXsKtwDslz0swLqoNm0lKliGJUUYy9GgrxzFN1SsaZyC78JHaWiYMFPYgCdKoYPg9za1%2FKYSyEUYAc63oq28Ta0q7mghOdJRhnWYzSIjRv7484Ojm5XemGlOKQInIFJeY7McIw74GB8s0WpK7QmSio6dvlQyqRmy1f50rqNgRixnvcDU7vjQqzK028g15nXzWJjAv1SFE%2BHuZ9L58BtfyGUWFF2I8wEKa%2FHkHuYjlHOPBKG1YCEv77om1LthvBUHVW%2F4TfvmuoMT38SBAVjBWhBMF5vSpFBJ5qTK6pikQAXCnTZtMALIncfhSVJiv5BzwTs1Ub5W4wi1wBgiUDEyzmxbHqXqOC2s%2FqOoACtfFRkqNkYGZdwr80drN%2B0AQo5E7QjXguK7KJ0xe8ytnq8pZAa66xcY7EscucUfMsVxhE0p7YupzqBV5CBf1EybiIRQzZRTkZFhpCOyIxr1jxjAYrMF7z8HDcuaY3xxFxJp7gOCpEpksKNNY3%2BKq0Yf8hBK9cB92kmjKN4GXM4ZU4%2BdIgg%2Fyc4VIcgzIjlqELYz%2FsSSye5FyISBIdfMif2WDgYs6lDVuQw9Le4xyTpofY6Yzrcq82qT%2FBpFUBH6cmj4h446DSf%2BdFF8jEgYKZexH7ImZ0wysXIzgY6pgGwbYOiudCW3NQkhalW8eIl5PRCnHgXjSEl7gMGLn9XA35A0HmVtgr12iZ5Nqp38ezrDZJ0CdlcbMQhTQ%2Fteh39f8cTZde5nbnpgkGMoL4D4vViUaj2%2FUSwHoM%2FIkcPJsSVpmcnJwO33cJ7qpckjs9i7CXuLXklEk5F60QrJPXlMLVNUeejHyZAeUp6rue0fxdjf5lu3D7rBCPVgnAgxiIoHMwwjWu2&X-Amz-Signature=4260d62c236c5c2bccb759f2739dbc65a2b3445b1f13d347943d12fac7e87400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W62OWD6I%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T124631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoDigySwBJWe%2FUty7RQxT8NCURkuiSaPFKNXlpfAFSkAiBm5yrFscmeN0T7hh45oeUE3V%2B5LAJL4zO2iQp04syBviqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4OVl%2Fn%2FWLI%2Bm5zXsKtwDslz0swLqoNm0lKliGJUUYy9GgrxzFN1SsaZyC78JHaWiYMFPYgCdKoYPg9za1%2FKYSyEUYAc63oq28Ta0q7mghOdJRhnWYzSIjRv7484Ojm5XemGlOKQInIFJeY7McIw74GB8s0WpK7QmSio6dvlQyqRmy1f50rqNgRixnvcDU7vjQqzK028g15nXzWJjAv1SFE%2BHuZ9L58BtfyGUWFF2I8wEKa%2FHkHuYjlHOPBKG1YCEv77om1LthvBUHVW%2F4TfvmuoMT38SBAVjBWhBMF5vSpFBJ5qTK6pikQAXCnTZtMALIncfhSVJiv5BzwTs1Ub5W4wi1wBgiUDEyzmxbHqXqOC2s%2FqOoACtfFRkqNkYGZdwr80drN%2B0AQo5E7QjXguK7KJ0xe8ytnq8pZAa66xcY7EscucUfMsVxhE0p7YupzqBV5CBf1EybiIRQzZRTkZFhpCOyIxr1jxjAYrMF7z8HDcuaY3xxFxJp7gOCpEpksKNNY3%2BKq0Yf8hBK9cB92kmjKN4GXM4ZU4%2BdIgg%2Fyc4VIcgzIjlqELYz%2FsSSye5FyISBIdfMif2WDgYs6lDVuQw9Le4xyTpofY6Yzrcq82qT%2FBpFUBH6cmj4h446DSf%2BdFF8jEgYKZexH7ImZ0wysXIzgY6pgGwbYOiudCW3NQkhalW8eIl5PRCnHgXjSEl7gMGLn9XA35A0HmVtgr12iZ5Nqp38ezrDZJ0CdlcbMQhTQ%2Fteh39f8cTZde5nbnpgkGMoL4D4vViUaj2%2FUSwHoM%2FIkcPJsSVpmcnJwO33cJ7qpckjs9i7CXuLXklEk5F60QrJPXlMLVNUeejHyZAeUp6rue0fxdjf5lu3D7rBCPVgnAgxiIoHMwwjWu2&X-Amz-Signature=7164e621a80bfda8145ef5a6aaf46edb308035f35f0d8f89ddc241e664cbb331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







