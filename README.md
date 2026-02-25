



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663LYIC6L%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T065642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDKy8bDrriy5kDTKI7bSd2Y41MlzDj%2FZh0ac9%2F9ylxvQAIgCiTzITiX%2FPHiplPOfRw0OIvquzRnFa8PRm3NH7OjMu4q%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDPmdpQxwapOLvFAHSyrcA80C1bJxEYvEXdfC%2FjxZWQOwopOEoer2wQVyRpnuZNw3fdzSLMBiIVqHtF7pOOlInK5bHaQDCigJTdi5pn0QPiN0eyHu9jy%2BLOx%2BdIMevnAcpZY1uSiF9XZ0A6xDxemRfUOIeYGYf%2FU0VYl61k08F6fRNwfqCEYuaUUzVt7eGDkKQ296io%2FLBfABFXaAo9H8Lrk8oqjPj1OwjDSChXRnb8cX67ZfAnS1CgElbJcs61Bj761%2BYf8ROSEsASKw2m0wnzU4FWkT2z%2BG5gnHCdkKqSVtyDu8WAM8DphZPqBA0WNOGdJ6%2Bcl4xfOzUv59f4U5JS%2FF5WMvdkkl%2BYE2hgLwZF41g3UMtPdA%2FsKCKOTyXMfK1Ub%2FGJZ0zKF1ceUBo0dJwjqd6Flpsb7aX0LXX5P5%2B631vz0mVH5eukMmvT5benRn6l6Nn1qPCUfbLNJY55EOq8MJJ9A0s0g8FjqXzbkzlxBeEuCBY3FH%2BQ9Vl%2Bh3GvN05RguzpRQcgQJd57%2BeTyM4jn4otmhxXC%2FN%2F8XCjci%2FxEL8fPEapvlV4TCLRDYfuFwGdEybJJ2GXFHVC1AMtaAlGX17mpbbAdgDcp5UvS16AvTFGPj%2B1Xb%2BxeRIh4jSedLkVPTvpQe7A7N0VXAMJ%2Bg%2BswGOqUBGvhjGPHMwKHXnZHQnnRVHPxxMQIIwY7lMYmo4oYNOdSRi%2FXcGCBSsmTDX22cgmg5Hvb%2BOhZ2VCO6JPQ28sAcUprQkJSfzjbbic9BNE1jRuJhXth%2F3uTk02D20IAmZs08u%2F76Tn4r54HigiXs6ZDEqg5jY3SN10qlqw6ZIcim9iHG%2B7RWICxmDmUzCaBebRiWs329NLa6T9YHkE0DOwvoFqaTa5Ud&X-Amz-Signature=a0c438086fedcecaf68a8d6d43fb5b4c8940b4c5305f72bb77f0294464c4e1a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663LYIC6L%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T065642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDKy8bDrriy5kDTKI7bSd2Y41MlzDj%2FZh0ac9%2F9ylxvQAIgCiTzITiX%2FPHiplPOfRw0OIvquzRnFa8PRm3NH7OjMu4q%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDPmdpQxwapOLvFAHSyrcA80C1bJxEYvEXdfC%2FjxZWQOwopOEoer2wQVyRpnuZNw3fdzSLMBiIVqHtF7pOOlInK5bHaQDCigJTdi5pn0QPiN0eyHu9jy%2BLOx%2BdIMevnAcpZY1uSiF9XZ0A6xDxemRfUOIeYGYf%2FU0VYl61k08F6fRNwfqCEYuaUUzVt7eGDkKQ296io%2FLBfABFXaAo9H8Lrk8oqjPj1OwjDSChXRnb8cX67ZfAnS1CgElbJcs61Bj761%2BYf8ROSEsASKw2m0wnzU4FWkT2z%2BG5gnHCdkKqSVtyDu8WAM8DphZPqBA0WNOGdJ6%2Bcl4xfOzUv59f4U5JS%2FF5WMvdkkl%2BYE2hgLwZF41g3UMtPdA%2FsKCKOTyXMfK1Ub%2FGJZ0zKF1ceUBo0dJwjqd6Flpsb7aX0LXX5P5%2B631vz0mVH5eukMmvT5benRn6l6Nn1qPCUfbLNJY55EOq8MJJ9A0s0g8FjqXzbkzlxBeEuCBY3FH%2BQ9Vl%2Bh3GvN05RguzpRQcgQJd57%2BeTyM4jn4otmhxXC%2FN%2F8XCjci%2FxEL8fPEapvlV4TCLRDYfuFwGdEybJJ2GXFHVC1AMtaAlGX17mpbbAdgDcp5UvS16AvTFGPj%2B1Xb%2BxeRIh4jSedLkVPTvpQe7A7N0VXAMJ%2Bg%2BswGOqUBGvhjGPHMwKHXnZHQnnRVHPxxMQIIwY7lMYmo4oYNOdSRi%2FXcGCBSsmTDX22cgmg5Hvb%2BOhZ2VCO6JPQ28sAcUprQkJSfzjbbic9BNE1jRuJhXth%2F3uTk02D20IAmZs08u%2F76Tn4r54HigiXs6ZDEqg5jY3SN10qlqw6ZIcim9iHG%2B7RWICxmDmUzCaBebRiWs329NLa6T9YHkE0DOwvoFqaTa5Ud&X-Amz-Signature=1c62cdf14ddd27d0d83cbd5705d220af0ea72acd1f2cc71deb9bdc1544a14ffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







