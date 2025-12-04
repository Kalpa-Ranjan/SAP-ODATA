



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3AFZ3S4%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T123513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBTz%2B21RCB%2Fq42S3IhNiEEIvhljQ0v9%2FgCke7sg3PtskAiEA7Rp1LKy589hdPyLwJ%2BEw7Du3VERWMB0sRKdg%2FuGnBacq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDGMgFml663lE%2By7%2B%2BircAxbKdDtOQ7YKBhJGZtp0Y8Gxgor1Cw4szMOQSoPb%2BXK5XCKEEXu6tR0T1XaNoCcAtZkkkhJMjRnFLw8MvSssrnqdpJcSYx4pwsmAql6EnSeQuv6PUv2HyKPrbLhgZ32W6XVLA1mi3rKnLgZJwZXCyQbAc8pMasdsEkUboQWr2THFflXsthIME0iJ2hXJCF9hVakv0a1tD4kP%2FhCbIm0MW2gs5eYrYUpNfD9eMvQuxVHDKgoKKXkUgkV5adN1%2BWdvsBCwTOtXuwncg5Z9rxPyg6wAmLyUwiWpObYHTjSjLSVAvNrIKAEz%2F8Qn5L37AtndAmtzmupzB2vek7dt3Vvcy05hCI310PYSJmHWcyAs9xFZiPVo9hUAckaXtqS3PJVaBCR6lYxwhFFidgXJ8au3hZsZADTzFR%2BVdV6T6UQRll8lFmUXmBLml8B2bpVnpg2q59kG8xEHCBc0bOGoTCZq8YJaoGLld%2Fb4X3xReM%2FFrLwZ9kus4UUMzI3KDcdGgsHDvwUwEQq0sVk4gy6Zcg51LrDYpqbqHfL25jBqxTnX1Ft8yUvC2deWhkOtQ%2F9oH3yvu6blSkP69Zo7r5L0vVaZJa0i5ppFSA2u11%2B1NRtRovlg00n14uCbKr9yFRWaMN3mxckGOqUBcvO%2FqUZzbRGYAMeuueIsKuEzVEi3l3paG8tdIWRWmYxYntahmrVdv%2FoCwCYZG1lcccgWXXzECyQ74LRxoaQ5WYTM2oTwR5FeCsXSmI0f2EtjQhQ1pMd3UwuR0zMZx67xTb1gzPpsZ7yVUjfBy%2BdvXfabPMTCcLC6ECTvCvt764SfMdVRs32Y85ikzL6%2F2GDBOlrmelL%2F3YRMuRVlFK%2B7SJ5wHXvO&X-Amz-Signature=ac6bd911ccea020ca35c0920357588baa6c77e0ab07a897989aed98155294ba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3AFZ3S4%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T123513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBTz%2B21RCB%2Fq42S3IhNiEEIvhljQ0v9%2FgCke7sg3PtskAiEA7Rp1LKy589hdPyLwJ%2BEw7Du3VERWMB0sRKdg%2FuGnBacq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDGMgFml663lE%2By7%2B%2BircAxbKdDtOQ7YKBhJGZtp0Y8Gxgor1Cw4szMOQSoPb%2BXK5XCKEEXu6tR0T1XaNoCcAtZkkkhJMjRnFLw8MvSssrnqdpJcSYx4pwsmAql6EnSeQuv6PUv2HyKPrbLhgZ32W6XVLA1mi3rKnLgZJwZXCyQbAc8pMasdsEkUboQWr2THFflXsthIME0iJ2hXJCF9hVakv0a1tD4kP%2FhCbIm0MW2gs5eYrYUpNfD9eMvQuxVHDKgoKKXkUgkV5adN1%2BWdvsBCwTOtXuwncg5Z9rxPyg6wAmLyUwiWpObYHTjSjLSVAvNrIKAEz%2F8Qn5L37AtndAmtzmupzB2vek7dt3Vvcy05hCI310PYSJmHWcyAs9xFZiPVo9hUAckaXtqS3PJVaBCR6lYxwhFFidgXJ8au3hZsZADTzFR%2BVdV6T6UQRll8lFmUXmBLml8B2bpVnpg2q59kG8xEHCBc0bOGoTCZq8YJaoGLld%2Fb4X3xReM%2FFrLwZ9kus4UUMzI3KDcdGgsHDvwUwEQq0sVk4gy6Zcg51LrDYpqbqHfL25jBqxTnX1Ft8yUvC2deWhkOtQ%2F9oH3yvu6blSkP69Zo7r5L0vVaZJa0i5ppFSA2u11%2B1NRtRovlg00n14uCbKr9yFRWaMN3mxckGOqUBcvO%2FqUZzbRGYAMeuueIsKuEzVEi3l3paG8tdIWRWmYxYntahmrVdv%2FoCwCYZG1lcccgWXXzECyQ74LRxoaQ5WYTM2oTwR5FeCsXSmI0f2EtjQhQ1pMd3UwuR0zMZx67xTb1gzPpsZ7yVUjfBy%2BdvXfabPMTCcLC6ECTvCvt764SfMdVRs32Y85ikzL6%2F2GDBOlrmelL%2F3YRMuRVlFK%2B7SJ5wHXvO&X-Amz-Signature=ac9c03fcd45102c0235c6deb85d7af42cb210fc5265b7048c47d5b6050a0aadc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







