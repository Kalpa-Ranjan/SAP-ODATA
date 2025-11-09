



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ36LEH7%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T011512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD08JkDl2wgeDMjONPIxlh7TcWDFFQlgKk2fkC2S4OiwQIhAKc%2BQXOKFdcKckwkgI1CB%2FAHBFGDsJ2rJop1kXjKthW5KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyruKyaMtr%2BiwrOVHsq3AMGylpeL4IBpSQTloxkoXGnLJ2yBNRAwI%2F5GXawdxeLR8Cb0Atg5ySjctiVedcrkNf5aiNq0vbnyTZzR4BB0riQydyDrOrf2PAcx8QYBIEiK7C3dm%2F2fY2f%2FkE59LiXzozEkMm%2BTDhwctAGrFpUTAcyiyKuYSqlPdQj39WHnQiVcw9QqJ3oP2aoxi5dDIDRhhfTrCXludomckwllxDGh%2BkV9bcJA%2FJJxC7Q7pE%2BlUmu4wVdUGOwHm%2Bv2lE1UUuWhfITxPjhcOcpdP4GYs64DxPUl1VbaE5vNdycw3LRJBYtFBItE3EbVEnwEqvF9%2FULrufmIafZICboOJ2qEDOFZa9HW7AB5ok61ZTuvsagY%2FCuTrsT8LUQRRIzWi0GZ0PmmuPblMIZ%2Blc9cxBje2BueNDUyQEOu6MKWhYkuQ6NMWttcuN%2BnXJr%2FR9gLz%2F%2BHDgAy7Au1nMMZ28UgiYmQTYhk%2B66g9qS2cDAJReorY9mEQM0Z3Ei9hocHaPtF8V2YdxcE5OS%2BWVpUndT13aVkCiwdEd78ZHHZmejfs21J5zE56h%2Flcx%2BMSzc34N%2FdZ2cq9vlQt0gw4%2BLmeAs51%2FUo3fPWdUvWu5YQGxUP%2Bskc2826KSPxFtsr8S3ZuCCNPOqPjDct7%2FIBjqkAdV%2BYf79cPQJxWEImpJqOurlZmnIUYFuUXGKAPCUtMbriPziFua%2BdXHp4YrXyrnTWI3Y%2FFrKQ5gDySW4nFPNE02n8DE52%2FFmC4Ds4m6x4dEPrSdARgGJZi2OyUG%2B78Dbv2lwJn2oerCqcuIiGqiQvP6cjCRwWlbEmSVcvObLhVwIuckNTypFNn86s2HMcPWoWikegwHBwQi6XcXxoz3oIlg5CB1M&X-Amz-Signature=82a4c35095d3cec8c5a290360e93fafc0aca11f5df49728d7fd4e1a8e33f8a7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ36LEH7%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T011513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD08JkDl2wgeDMjONPIxlh7TcWDFFQlgKk2fkC2S4OiwQIhAKc%2BQXOKFdcKckwkgI1CB%2FAHBFGDsJ2rJop1kXjKthW5KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyruKyaMtr%2BiwrOVHsq3AMGylpeL4IBpSQTloxkoXGnLJ2yBNRAwI%2F5GXawdxeLR8Cb0Atg5ySjctiVedcrkNf5aiNq0vbnyTZzR4BB0riQydyDrOrf2PAcx8QYBIEiK7C3dm%2F2fY2f%2FkE59LiXzozEkMm%2BTDhwctAGrFpUTAcyiyKuYSqlPdQj39WHnQiVcw9QqJ3oP2aoxi5dDIDRhhfTrCXludomckwllxDGh%2BkV9bcJA%2FJJxC7Q7pE%2BlUmu4wVdUGOwHm%2Bv2lE1UUuWhfITxPjhcOcpdP4GYs64DxPUl1VbaE5vNdycw3LRJBYtFBItE3EbVEnwEqvF9%2FULrufmIafZICboOJ2qEDOFZa9HW7AB5ok61ZTuvsagY%2FCuTrsT8LUQRRIzWi0GZ0PmmuPblMIZ%2Blc9cxBje2BueNDUyQEOu6MKWhYkuQ6NMWttcuN%2BnXJr%2FR9gLz%2F%2BHDgAy7Au1nMMZ28UgiYmQTYhk%2B66g9qS2cDAJReorY9mEQM0Z3Ei9hocHaPtF8V2YdxcE5OS%2BWVpUndT13aVkCiwdEd78ZHHZmejfs21J5zE56h%2Flcx%2BMSzc34N%2FdZ2cq9vlQt0gw4%2BLmeAs51%2FUo3fPWdUvWu5YQGxUP%2Bskc2826KSPxFtsr8S3ZuCCNPOqPjDct7%2FIBjqkAdV%2BYf79cPQJxWEImpJqOurlZmnIUYFuUXGKAPCUtMbriPziFua%2BdXHp4YrXyrnTWI3Y%2FFrKQ5gDySW4nFPNE02n8DE52%2FFmC4Ds4m6x4dEPrSdARgGJZi2OyUG%2B78Dbv2lwJn2oerCqcuIiGqiQvP6cjCRwWlbEmSVcvObLhVwIuckNTypFNn86s2HMcPWoWikegwHBwQi6XcXxoz3oIlg5CB1M&X-Amz-Signature=26c2839823b8f3a939eb8e1e1c3bf02e6ba2286e8ecb036f80af2ad5e5301787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







