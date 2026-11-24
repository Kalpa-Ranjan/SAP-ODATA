



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7ABNWO4%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T120724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BMAoV6ZAA%2B4%2BJwfccXPV1w61%2FBQqhiINUrqs7TCLbFgIhAKlCJOOqhOwkxsFHJZUM2ajd%2BQAYdx3zxFuYds50M9Z8KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbVLtz2LS1E6Bn6Fcq3AMev%2FRw%2FU3TSJEr9fIVwoEoWkgpp%2FRdYimCtOsv6u3X1Zv4B9eGNelHYJxdwUYFkOUVAQbj%2BGVnJRqOk9db43gScIbL5%2BgRDGuqEEJTvuMIQMZdF2sh8YF8SX%2F%2Fa3ujS5Q6MtGBC0Xeah%2FBvAmBxAmMI5gdlT0s%2FBuw%2Fia1sW71C9EmXt3X%2BbM25LdK63UzfTfqnm%2BXdoVIB8y%2BdZvw7F5Vv%2FOt%2B%2B5IwQW6qpFMno2GB2md6c1flYIJUGIO19Y2niTq9GBLiyiiZU29fmimTVzr2K%2Fjq42TuvYU0IN9qqMxqbrE%2FiqNH%2FnEtKPDeMRDasjsdSGPb8QKWMEdxwS8%2FB21DC7vpxpDAH7XflVSbU6PPG3z87rHzgJSksOK9q3MbFLprESGxCgzH99dkW2IpavhjZWzTes4jM5YvAaM93ybORRkAQtlvHvqpxP1WGhlisdXG73UELFZZOzltyE2xo2Qf2S%2B27tz0cfT3lEme8Ljm2pygnSXiEdp3IKcy5tZmB2OVXGhHW65jJZawRPRqcEs%2B7SVZEpXJa68zV69pxS2OIEKgx31uaB67z36khrL6HIdlxvYK83FYMqid4gDYdNuuMEX3kW3OITGwPnXYhUeJWyPnBY5pwjBGV%2FtJTC02JXYBjqkAa8hFNdzuIWmH%2BN7T3pqN2r%2F2TjeEg%2FGTd%2FGcT8d6WEmWuYNrCLnp7adFwAnKB%2BIIrsy7vICz6jQ3ycUofuTK3KxuLpe001XRZ%2FaVKrStxF4VXg5DO9%2B58U1aK0e8eDF3pRQv4wv7v9wUPVAopNDJtiWzyMZCviNLtGq%2BM%2F7IlQNvLueWytgI53RzN3dO24bnukiCb4sOPqNzBRVgCpZXiwBKFZG&X-Amz-Signature=44adb37f86f00d34441b8e69bc77956686b8459d98d54053c43e388ffe333a9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7ABNWO4%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T120724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BMAoV6ZAA%2B4%2BJwfccXPV1w61%2FBQqhiINUrqs7TCLbFgIhAKlCJOOqhOwkxsFHJZUM2ajd%2BQAYdx3zxFuYds50M9Z8KogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbVLtz2LS1E6Bn6Fcq3AMev%2FRw%2FU3TSJEr9fIVwoEoWkgpp%2FRdYimCtOsv6u3X1Zv4B9eGNelHYJxdwUYFkOUVAQbj%2BGVnJRqOk9db43gScIbL5%2BgRDGuqEEJTvuMIQMZdF2sh8YF8SX%2F%2Fa3ujS5Q6MtGBC0Xeah%2FBvAmBxAmMI5gdlT0s%2FBuw%2Fia1sW71C9EmXt3X%2BbM25LdK63UzfTfqnm%2BXdoVIB8y%2BdZvw7F5Vv%2FOt%2B%2B5IwQW6qpFMno2GB2md6c1flYIJUGIO19Y2niTq9GBLiyiiZU29fmimTVzr2K%2Fjq42TuvYU0IN9qqMxqbrE%2FiqNH%2FnEtKPDeMRDasjsdSGPb8QKWMEdxwS8%2FB21DC7vpxpDAH7XflVSbU6PPG3z87rHzgJSksOK9q3MbFLprESGxCgzH99dkW2IpavhjZWzTes4jM5YvAaM93ybORRkAQtlvHvqpxP1WGhlisdXG73UELFZZOzltyE2xo2Qf2S%2B27tz0cfT3lEme8Ljm2pygnSXiEdp3IKcy5tZmB2OVXGhHW65jJZawRPRqcEs%2B7SVZEpXJa68zV69pxS2OIEKgx31uaB67z36khrL6HIdlxvYK83FYMqid4gDYdNuuMEX3kW3OITGwPnXYhUeJWyPnBY5pwjBGV%2FtJTC02JXYBjqkAa8hFNdzuIWmH%2BN7T3pqN2r%2F2TjeEg%2FGTd%2FGcT8d6WEmWuYNrCLnp7adFwAnKB%2BIIrsy7vICz6jQ3ycUofuTK3KxuLpe001XRZ%2FaVKrStxF4VXg5DO9%2B58U1aK0e8eDF3pRQv4wv7v9wUPVAopNDJtiWzyMZCviNLtGq%2BM%2F7IlQNvLueWytgI53RzN3dO24bnukiCb4sOPqNzBRVgCpZXiwBKFZG&X-Amz-Signature=6e68bfac9ab8d97fc1f168a4104e5839736cb5e8352d2e6bb863aea88dc788fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







