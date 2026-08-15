



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KIMQKM%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T005459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDvwj%2BqsTA%2FrB8UiGLQj%2BhtQsSwReqTEV8MoTHGCC2foAIgAUavModRcjF8oSVtil1H3G8i1DduaQIkQ0XMDDuYzXgq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDOQdrBBguPuIsXMNoircA2ANSxgz81wtp6UMwUqhGDn3iHCg5j%2FBqQiZ7T2hpUZ1cCBssG0J382b2PInXqeHBJmuo3y9oaI%2FcxPMu4Yp5wPjNZ46TRPb%2B99Z66Hom8hsghONTPqNCLwb%2BtvPa8XP%2BBLhLTXyk%2FSfwO%2FWL4I4o3ewALsOMnWqucYk3ioy1t3zXOtnWmNEKeb97HgVjYjiKQmiQsn%2FzR16AbKq7f52CAyKjkWcBpJ02F8WchJYzPYSb35NO2JShey1CMnC%2BG0er%2BvlM4QJFeIADvmi%2BYm0JgC3s1QCSu1zOCV4kVJFVmZNH9CZxWS8V%2FkGOP5Ln9rHrW3r%2BJwT%2FYOKUc%2FvJNA6mAip0XNotQlC02jhXzobMPIyySBQhLFnzoo7voB9UPensw791B9amcCRXSZXVWXgT%2BUNnokS%2FLR0Z4uf1POxrHWYwaUihC0fdFo45Hli8twlrIgDCsliUYz2aaCNzbDToczXVbADdpNqrihUvJ59gsacbjU3M%2F3vjWF0lTTftcxYa4KhD1tiknzc5Xyjy4lqBNU82s%2B0UiJ6z5IbEImmKZ3hi9SzzUZW4c7ArQYseeih1tV0gHcTPyN5UzyKDKXzAPcNoXTK6ar%2FMKAnZMKi8eEwjkDSmoVo%2BIj33l0qMMPD%2FtMGOqUBdPubgk79yKq%2BaYBwV%2BPt4WoNNABXQJTN3y8u%2BO%2Bf2eVsKgjB86IE%2F5d4ojvbih7vKqkYzDjGpCYuDgxhTca6OEeRq5Y4onlh%2F9ZqcQ5V0bMpFfJgB1b71Rgu%2F5C66mFpRCGapI9K0Z9LWLbjXsnhNnPhOJPozgZBAm1XW%2BicKM%2FwKSiLFtkGnETjgcLSgkzTu%2B1uvKmujhIO97pW01kpNZ5gK%2FwO&X-Amz-Signature=5ca051880a77b5b238058e5840cf0f84c2dd0bc5ff90ce223c4cc96d2a5c06d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5KIMQKM%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T005459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDvwj%2BqsTA%2FrB8UiGLQj%2BhtQsSwReqTEV8MoTHGCC2foAIgAUavModRcjF8oSVtil1H3G8i1DduaQIkQ0XMDDuYzXgq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDOQdrBBguPuIsXMNoircA2ANSxgz81wtp6UMwUqhGDn3iHCg5j%2FBqQiZ7T2hpUZ1cCBssG0J382b2PInXqeHBJmuo3y9oaI%2FcxPMu4Yp5wPjNZ46TRPb%2B99Z66Hom8hsghONTPqNCLwb%2BtvPa8XP%2BBLhLTXyk%2FSfwO%2FWL4I4o3ewALsOMnWqucYk3ioy1t3zXOtnWmNEKeb97HgVjYjiKQmiQsn%2FzR16AbKq7f52CAyKjkWcBpJ02F8WchJYzPYSb35NO2JShey1CMnC%2BG0er%2BvlM4QJFeIADvmi%2BYm0JgC3s1QCSu1zOCV4kVJFVmZNH9CZxWS8V%2FkGOP5Ln9rHrW3r%2BJwT%2FYOKUc%2FvJNA6mAip0XNotQlC02jhXzobMPIyySBQhLFnzoo7voB9UPensw791B9amcCRXSZXVWXgT%2BUNnokS%2FLR0Z4uf1POxrHWYwaUihC0fdFo45Hli8twlrIgDCsliUYz2aaCNzbDToczXVbADdpNqrihUvJ59gsacbjU3M%2F3vjWF0lTTftcxYa4KhD1tiknzc5Xyjy4lqBNU82s%2B0UiJ6z5IbEImmKZ3hi9SzzUZW4c7ArQYseeih1tV0gHcTPyN5UzyKDKXzAPcNoXTK6ar%2FMKAnZMKi8eEwjkDSmoVo%2BIj33l0qMMPD%2FtMGOqUBdPubgk79yKq%2BaYBwV%2BPt4WoNNABXQJTN3y8u%2BO%2Bf2eVsKgjB86IE%2F5d4ojvbih7vKqkYzDjGpCYuDgxhTca6OEeRq5Y4onlh%2F9ZqcQ5V0bMpFfJgB1b71Rgu%2F5C66mFpRCGapI9K0Z9LWLbjXsnhNnPhOJPozgZBAm1XW%2BicKM%2FwKSiLFtkGnETjgcLSgkzTu%2B1uvKmujhIO97pW01kpNZ5gK%2FwO&X-Amz-Signature=896e6d85ad3d150b37646dd0c14c7858d8e9891fbf4c2c2c142a7ccccf5aded9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







