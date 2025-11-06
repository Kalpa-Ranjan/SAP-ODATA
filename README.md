



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YITTM4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T182315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0GhC1eH7wY1wkZNaf2g2F8xPaRkCbcwkTHJcXIO0UogIgc0VGp1WiTE8dTyXj9%2BMmNwafiZW571LCV1W4qUyQAhAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2Fl7FzNoxuKGBAlSircA%2F7Wsor1NW%2B1a9goYjSBMKpScJK8gRBmGUOqLXueM1xQQO5xPWVvcGfnTD3zk6EmvGYFx2kzRZ5kgtPoLKwVQVNHhpVvypmd4%2Fvtrvyd5XWK%2BQ5AYm7oOs1GIbRqkkhF0HRJ2Vpn0oyWoqOhExRCV%2FpUKqFG5P5pw5k4cz6rNM76Jtqbk1%2BWA1scUWaZdYIkDiXeBhgnimDO8DqFN71SUhkgcw0UQzHfqcXC%2BqneAlXukugQC5LjyPzdTjdnSqOaE2BsmSMVxZcVIr5PwhFbofP%2FJsl9SWWX7SK0udJdisMfeGeKFjqhUD%2Fi8DLyYLSmE1lOr9c3zeWhJqeA3H38aUjUMeW6kd7mL1ayLo9WpMzysoxpqj%2FVnr88bF8M6QqZBO8U%2FXoJRvHV4Y%2FP5GW5pTC%2F%2FaTLzuLC9m2aSAQenl2Ta8hLQPbs1%2BHuenb3DrzTh7mFz9rH9DVRMh6oCIgRBcmKtaWA%2FsId%2FcBaFR%2F0bpBtbLdxHwnTe%2BDiX11szUtOLSXxg5BxbXWku6janqRXTUAAOulS8sQioDO2WqrHHP%2Fez2n4lEf7hFfYgdBLFvjrkd6nZyKhcaBMBzTWJxtKBsbxzhP5dzTKNsP4zP03c9j6OQdzOYUK6FDJR0YIMPi1s8gGOqUBE%2BBvArh6ryaV0hGg0jsfE7HQVBHapoR14%2FcxM6TiUkS35NBUF8L4YBIqPjW48BWADdhRpG4ygQdZIZjOqLQLEiKGFsAYzEvtCDMk8jzrXC7eGa9yBylMRoalMhttjQ0skuGw9Qxvyf8wnZ8%2FXceCpu1hC4H8VIlBpneJg5CyQOyjUgYSdvtCPVyMFFKBPIDWrMUsgX73iMd%2FQGkJQAszIfHNDFd5&X-Amz-Signature=1d82e5a26a563b7c1c6e51d865bc87c4dc2a959908e44cdc6a1673bd53e2e720&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YITTM4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T182316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0GhC1eH7wY1wkZNaf2g2F8xPaRkCbcwkTHJcXIO0UogIgc0VGp1WiTE8dTyXj9%2BMmNwafiZW571LCV1W4qUyQAhAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2Fl7FzNoxuKGBAlSircA%2F7Wsor1NW%2B1a9goYjSBMKpScJK8gRBmGUOqLXueM1xQQO5xPWVvcGfnTD3zk6EmvGYFx2kzRZ5kgtPoLKwVQVNHhpVvypmd4%2Fvtrvyd5XWK%2BQ5AYm7oOs1GIbRqkkhF0HRJ2Vpn0oyWoqOhExRCV%2FpUKqFG5P5pw5k4cz6rNM76Jtqbk1%2BWA1scUWaZdYIkDiXeBhgnimDO8DqFN71SUhkgcw0UQzHfqcXC%2BqneAlXukugQC5LjyPzdTjdnSqOaE2BsmSMVxZcVIr5PwhFbofP%2FJsl9SWWX7SK0udJdisMfeGeKFjqhUD%2Fi8DLyYLSmE1lOr9c3zeWhJqeA3H38aUjUMeW6kd7mL1ayLo9WpMzysoxpqj%2FVnr88bF8M6QqZBO8U%2FXoJRvHV4Y%2FP5GW5pTC%2F%2FaTLzuLC9m2aSAQenl2Ta8hLQPbs1%2BHuenb3DrzTh7mFz9rH9DVRMh6oCIgRBcmKtaWA%2FsId%2FcBaFR%2F0bpBtbLdxHwnTe%2BDiX11szUtOLSXxg5BxbXWku6janqRXTUAAOulS8sQioDO2WqrHHP%2Fez2n4lEf7hFfYgdBLFvjrkd6nZyKhcaBMBzTWJxtKBsbxzhP5dzTKNsP4zP03c9j6OQdzOYUK6FDJR0YIMPi1s8gGOqUBE%2BBvArh6ryaV0hGg0jsfE7HQVBHapoR14%2FcxM6TiUkS35NBUF8L4YBIqPjW48BWADdhRpG4ygQdZIZjOqLQLEiKGFsAYzEvtCDMk8jzrXC7eGa9yBylMRoalMhttjQ0skuGw9Qxvyf8wnZ8%2FXceCpu1hC4H8VIlBpneJg5CyQOyjUgYSdvtCPVyMFFKBPIDWrMUsgX73iMd%2FQGkJQAszIfHNDFd5&X-Amz-Signature=4f72e2e3f93b30703bb0d637562f9e6e9cb25c5ed515e348c7ae7eeb2d90cd71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







