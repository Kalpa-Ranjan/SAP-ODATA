



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE5M47E2%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T180925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHvNAVx0aDsVeOtYbPy1qA8knW2jyXqEOm0y0U9qtqyAiEA5IU3G%2B5oLDN77LsAlRnG4dSXCec1tG2u7IuFHAS3B6Mq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNvaSPI%2F4JiuVFd%2F7SrcA%2BNLzCT1Wp4Weh9nV7vspd1HekfgP9TRC1o7STHD4xupzzQhfMs3sua2u6j%2FxWJCdh4TgvfEBqMGtA0kbspHysyXjYFOzXoyD5lM7mxAZErQ2GPM6ntndbvT%2BJ4nTgEXJ1XpcMdP52mBovCw977TcWa6rkF650Hm251BVfBfMl3N0QQW1qiu5fI0F13eB%2F%2BDATkakwpT53eIaLVdVTMHWwNLBtwOFjSUamvwDFxDXVjtZ8wrakm6lEbF14%2B6d3PEMlIyxOCBbUuIqEIPERPRDDPELjtfCG%2FkTksmsJC9RmwGJPQStpmz3%2BZO%2FJuJppKvr0ZgRRZA9WCsOYZtob3Xhd8C5JwbRARQlzPgSEveGXCM0EV6rICvc8vzdBLFypt1z%2BT5aepgEUkMGNxg9E0tHl0cKjPqe3NBCnYK%2Bg7qXri2Fxr%2FoNu1hQGj9t%2FHmDF7q4bMVfPqYjEQUkaioqdnsYEOnQ1HMTRq1aPXPdzIDTetaP4IGunSsEtYI9SVTg9aLpfx07ZwiQ7%2FiGNR4wmB2kqXlVrfZwDgXDmwtomR9gqgxu9txALCP7%2FXtqKxMwOUHPRBqLYJIQP4euNaXkDijbI8GJ%2Bl7tSTOx9HOUABA6QB9huK77kbhHHEB0QMMITuqdYGOqUBB9TiRTVBEDeTJtQMRuZu6iQaXBznPSHKz0AAQb8xeckw3f5J3ZOLEJ9HE9KRRZmx50EtUVs6j8Ucp47uqeOPvSTusNLf2EzpnCTg5WzS6BzCp%2FHVI8qBN%2Fs9X9m2ZnOdNN0SkyxJAK%2FS2QsLjurSj8YHKl98L8PT7BVjQqUCsITssyMhlEaigFJuVS62wRr%2BJTuTUGmgl4D5wgVHaQHkKvpuSu5s&X-Amz-Signature=f50034763c9211d3a7f8ae926d11c40e9e89ff5ac357780a73a6f8e4dae3be39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE5M47E2%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T180925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHvNAVx0aDsVeOtYbPy1qA8knW2jyXqEOm0y0U9qtqyAiEA5IU3G%2B5oLDN77LsAlRnG4dSXCec1tG2u7IuFHAS3B6Mq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNvaSPI%2F4JiuVFd%2F7SrcA%2BNLzCT1Wp4Weh9nV7vspd1HekfgP9TRC1o7STHD4xupzzQhfMs3sua2u6j%2FxWJCdh4TgvfEBqMGtA0kbspHysyXjYFOzXoyD5lM7mxAZErQ2GPM6ntndbvT%2BJ4nTgEXJ1XpcMdP52mBovCw977TcWa6rkF650Hm251BVfBfMl3N0QQW1qiu5fI0F13eB%2F%2BDATkakwpT53eIaLVdVTMHWwNLBtwOFjSUamvwDFxDXVjtZ8wrakm6lEbF14%2B6d3PEMlIyxOCBbUuIqEIPERPRDDPELjtfCG%2FkTksmsJC9RmwGJPQStpmz3%2BZO%2FJuJppKvr0ZgRRZA9WCsOYZtob3Xhd8C5JwbRARQlzPgSEveGXCM0EV6rICvc8vzdBLFypt1z%2BT5aepgEUkMGNxg9E0tHl0cKjPqe3NBCnYK%2Bg7qXri2Fxr%2FoNu1hQGj9t%2FHmDF7q4bMVfPqYjEQUkaioqdnsYEOnQ1HMTRq1aPXPdzIDTetaP4IGunSsEtYI9SVTg9aLpfx07ZwiQ7%2FiGNR4wmB2kqXlVrfZwDgXDmwtomR9gqgxu9txALCP7%2FXtqKxMwOUHPRBqLYJIQP4euNaXkDijbI8GJ%2Bl7tSTOx9HOUABA6QB9huK77kbhHHEB0QMMITuqdYGOqUBB9TiRTVBEDeTJtQMRuZu6iQaXBznPSHKz0AAQb8xeckw3f5J3ZOLEJ9HE9KRRZmx50EtUVs6j8Ucp47uqeOPvSTusNLf2EzpnCTg5WzS6BzCp%2FHVI8qBN%2Fs9X9m2ZnOdNN0SkyxJAK%2FS2QsLjurSj8YHKl98L8PT7BVjQqUCsITssyMhlEaigFJuVS62wRr%2BJTuTUGmgl4D5wgVHaQHkKvpuSu5s&X-Amz-Signature=f6c6fa89b4967eda313e91aaf7bd5ac1e0f53483567d667713e3683b23a9b7f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







