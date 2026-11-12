



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652CACAIT%2F20261112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261112T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp07%2B9V9dyy2lxfKMbNnOr8MDnaJEXHU1shToKPppG%2BAiEAp9nBAkZU8GH7szPvxs5nBpBmXQoK6XR73dVRV8Io1Lwq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDNk9Ut0l631r2VTObCrcAyWwKhOZQWiRAVbebgtrMCqLPVrkvC9wBDNl82AvEPAQrq5ftVpFj5ZlUqX6q%2BAIxytetWg3UGsYp17%2FLNQ14Z6QpLKliT67A6Xka7YvdrJ%2FC76sfUIpFVsC%2FbS4u7JTNjwFsXWTD6WRcG3r6DBeDQjNgt4qtMNm7sCTOE%2BAJgZVqNzaWJqwV6le4q6pyAQtB2s7LOoimOJSwx7oVWP2timJa2uNlBv3k8YRxl7hBz7Npym%2F1S%2FgsWzjVY0eRP2QlBFFJICsvaiaZvKZHjYcVf7vivk2aabCbKDPRdm%2Fo%2FSfZdSQUvsiojAN3IWn0%2BigSY1R1f9%2FOOZfbjAWxCy7W8R9%2FKSzq7wTejQt%2Bma2SrEl4QcvJu518B%2BOkHWTuinNn%2F00wDv2SYsrN%2F9YtxILZdtXYa1H4RGA51qTrAlu4vt8uPHUsVQymuvjtzitc%2BoVFmsGRLNrGUyRFros%2FMvO5gD2GZJ%2Bk4XBhGPzLIaubO0wi1g6a2eIRGD1ae%2FqrqpssgQHYyj8PSTOaXMqtZupj%2F%2BzYtLz2Gh%2B%2BsIeca2bgpehqdf2FduBhoa1G3r6YAwTra5NDQgZfp%2BqqV8geb9OFBwM%2BxfYWSeNq2zzwz5rhDtudhLH65PeW4rrjvPMMMHs19cGOqUBkIREVxXPZGtW9st4b3SDmwbX41gqhjGL5D6s%2BJPOFpaRmvEgHrG2Ah4rnXFQ3v0kmR8FM%2B0soqrgdX3qQZrufpYqLsxT6GSV5kzPQ2pLGY%2BGs23%2BtbL3yDRVnvCr%2B5IEhjEfqXOeYPLk3nWRIyCHdKE3aEdL9sMmmVocRQjCo2aOxd8GnoKlHgpB4cpe8EUjaiX5YQ7iEqm1hzYN8gDobeoohzCi&X-Amz-Signature=70b3d6cbc4373e732e4c5ac2e0a5c8812702b9849ee7e2646ad93612f465acf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652CACAIT%2F20261112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261112T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp07%2B9V9dyy2lxfKMbNnOr8MDnaJEXHU1shToKPppG%2BAiEAp9nBAkZU8GH7szPvxs5nBpBmXQoK6XR73dVRV8Io1Lwq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDNk9Ut0l631r2VTObCrcAyWwKhOZQWiRAVbebgtrMCqLPVrkvC9wBDNl82AvEPAQrq5ftVpFj5ZlUqX6q%2BAIxytetWg3UGsYp17%2FLNQ14Z6QpLKliT67A6Xka7YvdrJ%2FC76sfUIpFVsC%2FbS4u7JTNjwFsXWTD6WRcG3r6DBeDQjNgt4qtMNm7sCTOE%2BAJgZVqNzaWJqwV6le4q6pyAQtB2s7LOoimOJSwx7oVWP2timJa2uNlBv3k8YRxl7hBz7Npym%2F1S%2FgsWzjVY0eRP2QlBFFJICsvaiaZvKZHjYcVf7vivk2aabCbKDPRdm%2Fo%2FSfZdSQUvsiojAN3IWn0%2BigSY1R1f9%2FOOZfbjAWxCy7W8R9%2FKSzq7wTejQt%2Bma2SrEl4QcvJu518B%2BOkHWTuinNn%2F00wDv2SYsrN%2F9YtxILZdtXYa1H4RGA51qTrAlu4vt8uPHUsVQymuvjtzitc%2BoVFmsGRLNrGUyRFros%2FMvO5gD2GZJ%2Bk4XBhGPzLIaubO0wi1g6a2eIRGD1ae%2FqrqpssgQHYyj8PSTOaXMqtZupj%2F%2BzYtLz2Gh%2B%2BsIeca2bgpehqdf2FduBhoa1G3r6YAwTra5NDQgZfp%2BqqV8geb9OFBwM%2BxfYWSeNq2zzwz5rhDtudhLH65PeW4rrjvPMMMHs19cGOqUBkIREVxXPZGtW9st4b3SDmwbX41gqhjGL5D6s%2BJPOFpaRmvEgHrG2Ah4rnXFQ3v0kmR8FM%2B0soqrgdX3qQZrufpYqLsxT6GSV5kzPQ2pLGY%2BGs23%2BtbL3yDRVnvCr%2B5IEhjEfqXOeYPLk3nWRIyCHdKE3aEdL9sMmmVocRQjCo2aOxd8GnoKlHgpB4cpe8EUjaiX5YQ7iEqm1hzYN8gDobeoohzCi&X-Amz-Signature=99f61b328900aed99f09b2e09e9fa78175319ffbc3b1873294741c284edfa376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







