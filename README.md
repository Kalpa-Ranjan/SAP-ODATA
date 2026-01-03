



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVN7GN7R%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T062435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJGMEQCIBvzIl8yVT%2BNZeU6G04zfgHH2iu5LCeQJ2RSlAbpwbjMAiABs%2FJ3bT8IlC5ofNs6RDqtcT66BHJ%2BLFx0%2B3%2FBkVOoeyr%2FAwgOEAAaDDYzNzQyMzE4MzgwNSIMX1%2BQEK4SRD1GdDHjKtwDwnVcfoRUMqRN7AvFQ2JYwfBzltDUvPx0EchtXj1S48Yq8Ia02%2FIGrDqRLOOo%2BOvnxaSKEJOjAra6sB63Ld3s%2Bda252uYfz%2FnJCnFhUzJtgLXM3df3fo9NScpCnPhqKn6ONGu82QEqGpEQsx8wVXgVuSmKJs6jww6XYwL3I7MMrZAwVljsgxWk4cppLdzNr6%2F9wnOltfItHZ3z2CFAX07%2ByQGiAdOV3mL412YMeaCv0dWVRgiA9GEjCtOoKP7xKfZNAbWLUelmoURneoXE0wsdLv4Jaxbjmd0aicpDRAP%2BVNwjXyi1NIHnHcSm7o6RFrsFw7XFY7Wj5%2BEmj9LEHAQDUGAPs0yfCBDI0p9%2F3KoBVh4wx0O9xzIl4kzbfYeulSScJ74ZB0nR2x7xgsZHOy9ekuRoz9tbu7k8Wpx4ChoA8Ek4V4xgvLof1hu3LUk9JZouvduqKhxFYkZbMHlyMp3KN4phVBQGOmOB%2FcbnuixmgkXBw11Qr4ywQ5q%2BazI89pZo%2FWLf0zVBFQzRl8HCyLWHKjdQIEnACl5Hn0LwSElkKLb1%2B1QcxoihqXEuxKcSX08awE2fCQoiwGiBZybyaG7O45nBM2s%2BFwnzWHUvMw6dEXDmsyeTyTc93rWSdQw6rfiygY6pgEKzKiI7XW1VUfU5CKvnj10APV%2FKR82MOc8RFxpfvU%2F7%2FpeLQTFBxd0nlsPqfPAdJozY%2B18hM%2BrhXqmyjM0JzOmRgS2cTXFdQjnKEvbiniiOCk718Zip%2FcoY3zQdf2xzKcE8EL4CaQnEnw%2Fy6vqSTVkL99bvKmbodBz5j6xDyM8pSyJEJ%2BP%2BjvJhXxX%2F74yN%2BzrI6Izl%2B73i9Oz9KDzGP6rzId2psjC&X-Amz-Signature=dd5f5c48d599bff6c82233541ecd6c4cd1ef13251d49d0aec907a78c90aba387&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVN7GN7R%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T062435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJGMEQCIBvzIl8yVT%2BNZeU6G04zfgHH2iu5LCeQJ2RSlAbpwbjMAiABs%2FJ3bT8IlC5ofNs6RDqtcT66BHJ%2BLFx0%2B3%2FBkVOoeyr%2FAwgOEAAaDDYzNzQyMzE4MzgwNSIMX1%2BQEK4SRD1GdDHjKtwDwnVcfoRUMqRN7AvFQ2JYwfBzltDUvPx0EchtXj1S48Yq8Ia02%2FIGrDqRLOOo%2BOvnxaSKEJOjAra6sB63Ld3s%2Bda252uYfz%2FnJCnFhUzJtgLXM3df3fo9NScpCnPhqKn6ONGu82QEqGpEQsx8wVXgVuSmKJs6jww6XYwL3I7MMrZAwVljsgxWk4cppLdzNr6%2F9wnOltfItHZ3z2CFAX07%2ByQGiAdOV3mL412YMeaCv0dWVRgiA9GEjCtOoKP7xKfZNAbWLUelmoURneoXE0wsdLv4Jaxbjmd0aicpDRAP%2BVNwjXyi1NIHnHcSm7o6RFrsFw7XFY7Wj5%2BEmj9LEHAQDUGAPs0yfCBDI0p9%2F3KoBVh4wx0O9xzIl4kzbfYeulSScJ74ZB0nR2x7xgsZHOy9ekuRoz9tbu7k8Wpx4ChoA8Ek4V4xgvLof1hu3LUk9JZouvduqKhxFYkZbMHlyMp3KN4phVBQGOmOB%2FcbnuixmgkXBw11Qr4ywQ5q%2BazI89pZo%2FWLf0zVBFQzRl8HCyLWHKjdQIEnACl5Hn0LwSElkKLb1%2B1QcxoihqXEuxKcSX08awE2fCQoiwGiBZybyaG7O45nBM2s%2BFwnzWHUvMw6dEXDmsyeTyTc93rWSdQw6rfiygY6pgEKzKiI7XW1VUfU5CKvnj10APV%2FKR82MOc8RFxpfvU%2F7%2FpeLQTFBxd0nlsPqfPAdJozY%2B18hM%2BrhXqmyjM0JzOmRgS2cTXFdQjnKEvbiniiOCk718Zip%2FcoY3zQdf2xzKcE8EL4CaQnEnw%2Fy6vqSTVkL99bvKmbodBz5j6xDyM8pSyJEJ%2BP%2BjvJhXxX%2F74yN%2BzrI6Izl%2B73i9Oz9KDzGP6rzId2psjC&X-Amz-Signature=4e2a78241e3bd6752210ec213e8336193068c245733cb85125bf1859b03aed44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







