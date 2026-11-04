



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVFAFJ4Y%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T180527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzL1naCrZcmcTQ2klnZn0h88ORa7Zmu7ELDou%2Fvu93xQIgUVXOe8P8GYUA1WGzysm1yQbCb1sCJphtjk7akvvxQtkqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYxiDIryDru1Z9gDSrcA3aejMUxbhmOXd8T8GLc%2FqRTGFytD0uf3nrBcJFzc858l%2Bi9IWzKDQLkvos2%2F9z5St9NLiQSNvE6Io%2FdXm11XBpoUY%2FQbQ16RvufFeAPl%2F5S4MnWFSCXwj90BkdmMa9HTSXaStm2ZxJo4mXvzuBPI2fGRR%2BTx7hm1riiCKhfQ0FbTABsOf0HPgqrA1VnvmoADnv3R%2FwoyuRQ8V4V6nxL4rgQBKYpeWhq%2B78%2BewcJlrwwcVTzW6oK4mdAWRwHhpZ0qZ41g0bmkCziIt0GateR9rSZzsKu8hQBnvHsibMKnbhraDqKapXA2N9FqvY2nC2xCi6YuhuY4xB7p0aYNH26R7ClIcoO8wVJULYpGbOxUegKl26jrCe%2FM26Pei9Z5%2BQkUx4DtSPnAJ8iVF7vYv93u%2Fbrn8Zn40s9C3dvVM7Cx%2FUvt76Dkc%2B8%2FO36749P8AJMGmss3uscgtdKoiRKmdS2yoog5fYtRnX1MXpPutGKZupzH1qcJIkIZeR79U%2FH0XZkMEyrwxWKhU5wSkBJhPmMP520cnR0bk85YswPMoU5CQJ6z%2FblMrcV%2BRy8Vq5dKTZ4Y9cicmkNqr6B6sgWEWuQdOoxHZ9toZLAYzzU3VBGDuhZX9pFKJcPSm%2F%2FUrLPMLbGrdcGOqUBzzluLBBg49TLvkrnmNMFiq7Cq4OhvEU2dx6SSVaP%2FEc%2BGmWzDwmec83mRo1RsfEzs4dwKMMyPXIVl220QjFR6P5N%2Fv61zNZKXNLO1xI7aHpvZ1EdSiAL8GjtZYp1iVBFBmVV4KbMEZ%2F54uSVfp062esjsIf3PpWhZFVKeStn3p2blJ%2FkeTxoKhAwSGQos4wLm%2BYCZopOlUFKZxhMpvQXwsQaF77v&X-Amz-Signature=2215fa474fcf57615f1a1357b8f8d8927c922d8c21510af283f7b4c9ac3e9570&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVFAFJ4Y%2F20261104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261104T180527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzL1naCrZcmcTQ2klnZn0h88ORa7Zmu7ELDou%2Fvu93xQIgUVXOe8P8GYUA1WGzysm1yQbCb1sCJphtjk7akvvxQtkqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYxiDIryDru1Z9gDSrcA3aejMUxbhmOXd8T8GLc%2FqRTGFytD0uf3nrBcJFzc858l%2Bi9IWzKDQLkvos2%2F9z5St9NLiQSNvE6Io%2FdXm11XBpoUY%2FQbQ16RvufFeAPl%2F5S4MnWFSCXwj90BkdmMa9HTSXaStm2ZxJo4mXvzuBPI2fGRR%2BTx7hm1riiCKhfQ0FbTABsOf0HPgqrA1VnvmoADnv3R%2FwoyuRQ8V4V6nxL4rgQBKYpeWhq%2B78%2BewcJlrwwcVTzW6oK4mdAWRwHhpZ0qZ41g0bmkCziIt0GateR9rSZzsKu8hQBnvHsibMKnbhraDqKapXA2N9FqvY2nC2xCi6YuhuY4xB7p0aYNH26R7ClIcoO8wVJULYpGbOxUegKl26jrCe%2FM26Pei9Z5%2BQkUx4DtSPnAJ8iVF7vYv93u%2Fbrn8Zn40s9C3dvVM7Cx%2FUvt76Dkc%2B8%2FO36749P8AJMGmss3uscgtdKoiRKmdS2yoog5fYtRnX1MXpPutGKZupzH1qcJIkIZeR79U%2FH0XZkMEyrwxWKhU5wSkBJhPmMP520cnR0bk85YswPMoU5CQJ6z%2FblMrcV%2BRy8Vq5dKTZ4Y9cicmkNqr6B6sgWEWuQdOoxHZ9toZLAYzzU3VBGDuhZX9pFKJcPSm%2F%2FUrLPMLbGrdcGOqUBzzluLBBg49TLvkrnmNMFiq7Cq4OhvEU2dx6SSVaP%2FEc%2BGmWzDwmec83mRo1RsfEzs4dwKMMyPXIVl220QjFR6P5N%2Fv61zNZKXNLO1xI7aHpvZ1EdSiAL8GjtZYp1iVBFBmVV4KbMEZ%2F54uSVfp062esjsIf3PpWhZFVKeStn3p2blJ%2FkeTxoKhAwSGQos4wLm%2BYCZopOlUFKZxhMpvQXwsQaF77v&X-Amz-Signature=747c9f85d6662b8520de03f54e6db6a1be902febefeea4cde79569c0115e9f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







