



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VORQLVLK%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T121112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH4vn%2Br2ky3JMOBAvpdWgl%2BPKpls%2Betv0POW%2FzIX%2BreQAiEAqDv3u1%2Ft7T3cNaUAq9JL%2F69XWnQZFjALcQKEVr%2B0cd0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJZMhYmsx%2F491pwU4yrcA697RwFy9%2B%2F9s%2B%2FkWKD5uLmDPzVhoc%2BybVRIb%2BNnNekelAcGCxaTto4c%2BaC3Pr83qGQFEbExapa1xhFjNM01cYCda3MlyJYUUEXwAroJGvWXd8MI%2BbpaZOMM9vbxUfwlrK%2FycNIySe2Mtz1W58x8X49RIzZW6gW%2FByODQoufwhUHIXhEWRtCAIvJQEFhDXXalZspTUl3z5aNkXgmdSg%2F94nmKyedCSxnvhpJivqdeCb7bsEjrHUtplSoWia%2BKPCtkdQmupnjqa%2B56E4snxEQvZ13dlm7sklGxf91NhxCYYZzU3SlKH8Rq0F3nNwQobtRt3tmhCaY452j9Je6H%2BH9rqzOM6gnVjMl0S%2BawsUsIBgfunO6o9EPoEBeMWYAncvQTUlES%2BCAkqV%2BEy5%2B%2FAuHeqapzk5AkyOn3vnX087nMpsRuOulYj6tGtHQ7z8GhSp9%2Fs5UumuI1j1xTgGmpiSUQRZtogrU%2FzKh95tyB4FT9rXlYXKfPxou3JtFNuusODBn65bLYyFiGRmQ25TXMy4FoPpOQCFetHlhldKYoyZGpBuEXtLhxzGtPXaxC5CDYg%2F80DNvwX%2B74WUQG2qfbwPDofQQthzmDcIL%2BMrqRrGWqfnmrBYJpvXRS%2BxKJ2tmMIWmxNUGOqUB7LaZVnFNcNvZl5uPxKfjToXYfiXg4E%2BBz0D9xQHn9F5dEwofGFICA%2FE%2FOkTo9RA84LwNJ6hlBdZVMJ3O2y1WxNOtk3989aRMUmNQOQCiSi4X5Tx3sw4AZaxwCLy%2BLLj%2BHINC21qcBKek0rv3IyCFqN39kdHS5QAhZzN6QYXBylRH4GUSNeE972l%2FZcIYYtb7R4DP73O60%2FjEm8onGNKXmzSk%2Fx9p&X-Amz-Signature=efd3e71acca00c23250585709abcf84e1f37f0020cc188b780015e6999418d08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VORQLVLK%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T121112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH4vn%2Br2ky3JMOBAvpdWgl%2BPKpls%2Betv0POW%2FzIX%2BreQAiEAqDv3u1%2Ft7T3cNaUAq9JL%2F69XWnQZFjALcQKEVr%2B0cd0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJZMhYmsx%2F491pwU4yrcA697RwFy9%2B%2F9s%2B%2FkWKD5uLmDPzVhoc%2BybVRIb%2BNnNekelAcGCxaTto4c%2BaC3Pr83qGQFEbExapa1xhFjNM01cYCda3MlyJYUUEXwAroJGvWXd8MI%2BbpaZOMM9vbxUfwlrK%2FycNIySe2Mtz1W58x8X49RIzZW6gW%2FByODQoufwhUHIXhEWRtCAIvJQEFhDXXalZspTUl3z5aNkXgmdSg%2F94nmKyedCSxnvhpJivqdeCb7bsEjrHUtplSoWia%2BKPCtkdQmupnjqa%2B56E4snxEQvZ13dlm7sklGxf91NhxCYYZzU3SlKH8Rq0F3nNwQobtRt3tmhCaY452j9Je6H%2BH9rqzOM6gnVjMl0S%2BawsUsIBgfunO6o9EPoEBeMWYAncvQTUlES%2BCAkqV%2BEy5%2B%2FAuHeqapzk5AkyOn3vnX087nMpsRuOulYj6tGtHQ7z8GhSp9%2Fs5UumuI1j1xTgGmpiSUQRZtogrU%2FzKh95tyB4FT9rXlYXKfPxou3JtFNuusODBn65bLYyFiGRmQ25TXMy4FoPpOQCFetHlhldKYoyZGpBuEXtLhxzGtPXaxC5CDYg%2F80DNvwX%2B74WUQG2qfbwPDofQQthzmDcIL%2BMrqRrGWqfnmrBYJpvXRS%2BxKJ2tmMIWmxNUGOqUB7LaZVnFNcNvZl5uPxKfjToXYfiXg4E%2BBz0D9xQHn9F5dEwofGFICA%2FE%2FOkTo9RA84LwNJ6hlBdZVMJ3O2y1WxNOtk3989aRMUmNQOQCiSi4X5Tx3sw4AZaxwCLy%2BLLj%2BHINC21qcBKek0rv3IyCFqN39kdHS5QAhZzN6QYXBylRH4GUSNeE972l%2FZcIYYtb7R4DP73O60%2FjEm8onGNKXmzSk%2Fx9p&X-Amz-Signature=cba6db0d30fb98d8ceb6871b94d5a3e06132b9bea5439d15616838a44cee8364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







