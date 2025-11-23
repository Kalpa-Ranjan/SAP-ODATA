



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VHJ2DNK%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T182023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQC8VzDoR5jCM4JfEgFAnXXXo1bIc8Gns%2F8Y6TjdJW0HCQIhAPALS6Q1%2Frk9Z1Qc8aIbjij%2FWLeGd7ObDARIyFsV0JTMKv8DCEAQABoMNjM3NDIzMTgzODA1IgxAccG8P2pb9X2XE1Iq3AO9rdjCzMGQGdn%2BlDs%2BvZumprmYVRH8uiy5c8cJwx9aUNBcEihxLwi3clRAjE1cXxzQiSxFn3UXqRDSmCYRlZ39QgaDsrDYbmbilUtTfj1ssQSRw5wG1JPcgl3Z63nxvPeuedpBTz8PZoDs4i3aEUO%2Fjedip8kBdutt1xs1csTTcmQgqNervPPEwULTIQ9VtnnCrNTNvx7vBgKvg1Y4HCIfAhpZFsGVQZ3%2FBrI74aanohTdpQUHm92I%2Bov%2B4z%2BBnOc6QtVQAtmVlBHXuxkzw0IESdQlqHIbPWusK5RUf%2BfBq%2BvtnXO7nCNl8F3UUdf%2FRpqrcIex07XkkLcRj%2F076W16XT6OkgL%2BaJ2fYBEJqdQvcrHerlLTso2sW1D7H9cA2eaDRY4IdCvenphklHHT1oeR0CEGmLe%2FKiO0mj%2B14%2BWT9anrR1j7feTIDiKyB6uRYVMv8rZ028FRHSlrl260aV%2FiQEQvN%2BW4CxbhUgovN6j51cQFR3atEB5W0WT5B93E7Yw1GhJL8nRbLUg381f%2FKI%2BvSQuPpzh6fLvgF1PXYswIegxCbalv4d2Yfbk5a4Vx3Dz1lTv%2F5TFfrJwd2bUz7EQzVw3wKBItXkWK5S1Awc7SXqDx8kRDUiISDvzNMjDYzYzJBjqkAUA4QGtOsMdOX5YQAfvJDu%2FuYHuvocmz04zJiqJEmzpDndoJMzI6ek9XkTFEcImrg0TWzdhkuSYijjQ116MQseyPah1wkPLt353xbgMHkjAHa21sJhmE%2Br6nUG3DD17CKeiZAQGJ6LBy1kRAZAQDLXonnMMi7hTapOSbPWpP2B0ybZvaS1vXIIai9KLVEemFNhAxkXdZQM00JjPrcim3K0KOkjp2&X-Amz-Signature=e31b71623356544e7c8dc4e4d8e6b1e7cf613a901f369c465edba9c51d1de8b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VHJ2DNK%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T182023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQC8VzDoR5jCM4JfEgFAnXXXo1bIc8Gns%2F8Y6TjdJW0HCQIhAPALS6Q1%2Frk9Z1Qc8aIbjij%2FWLeGd7ObDARIyFsV0JTMKv8DCEAQABoMNjM3NDIzMTgzODA1IgxAccG8P2pb9X2XE1Iq3AO9rdjCzMGQGdn%2BlDs%2BvZumprmYVRH8uiy5c8cJwx9aUNBcEihxLwi3clRAjE1cXxzQiSxFn3UXqRDSmCYRlZ39QgaDsrDYbmbilUtTfj1ssQSRw5wG1JPcgl3Z63nxvPeuedpBTz8PZoDs4i3aEUO%2Fjedip8kBdutt1xs1csTTcmQgqNervPPEwULTIQ9VtnnCrNTNvx7vBgKvg1Y4HCIfAhpZFsGVQZ3%2FBrI74aanohTdpQUHm92I%2Bov%2B4z%2BBnOc6QtVQAtmVlBHXuxkzw0IESdQlqHIbPWusK5RUf%2BfBq%2BvtnXO7nCNl8F3UUdf%2FRpqrcIex07XkkLcRj%2F076W16XT6OkgL%2BaJ2fYBEJqdQvcrHerlLTso2sW1D7H9cA2eaDRY4IdCvenphklHHT1oeR0CEGmLe%2FKiO0mj%2B14%2BWT9anrR1j7feTIDiKyB6uRYVMv8rZ028FRHSlrl260aV%2FiQEQvN%2BW4CxbhUgovN6j51cQFR3atEB5W0WT5B93E7Yw1GhJL8nRbLUg381f%2FKI%2BvSQuPpzh6fLvgF1PXYswIegxCbalv4d2Yfbk5a4Vx3Dz1lTv%2F5TFfrJwd2bUz7EQzVw3wKBItXkWK5S1Awc7SXqDx8kRDUiISDvzNMjDYzYzJBjqkAUA4QGtOsMdOX5YQAfvJDu%2FuYHuvocmz04zJiqJEmzpDndoJMzI6ek9XkTFEcImrg0TWzdhkuSYijjQ116MQseyPah1wkPLt353xbgMHkjAHa21sJhmE%2Br6nUG3DD17CKeiZAQGJ6LBy1kRAZAQDLXonnMMi7hTapOSbPWpP2B0ybZvaS1vXIIai9KLVEemFNhAxkXdZQM00JjPrcim3K0KOkjp2&X-Amz-Signature=0b16d581a526f5e3973cf5e9934d1ee6aba185a7ed3833b5e124bec1b0f6b959&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







