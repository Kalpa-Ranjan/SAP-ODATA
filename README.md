



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753PUOCY%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T131127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0zY1j2NitXxP6RaeWEhPN%2B3YrUyCOhsjCxo9qd3II9QIgQxPXSdWOD%2B1T4rhVorWh2sfdIeM0%2FDgQ9vxZNvPdN4UqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM5dxsnQs4GhnRjxbCrcAxRmfSTTzgv9asinl3HLDQ%2F5shvQxXHMhwDP5eMDmuFMLpS%2FF2PSVkHrW1U2Gczlb10tnnutTZrA4afO4kxIZMK0%2BsFGNFurSj0F9SwgAaLz415ttr8iDeWG4WuSxI7sh3SnZrLvWPKE9%2F8kK1%2BllqCCMImNbCllAWMqlcl6Bfqtf4G1M3GIoVZpZu98mRYREcr7HZpfi35tq0THr0KBLXw4KHkiixoeDrQQHyocBOyNka%2FkRZsTKJsXLo6JDFi0BmR3nyd6w7W5yq2TYnU1KrzBZ3w60CvTKfbPNX1w0JCD7gqN2LHqTCzQAbxZhpGwxQWEjYpmkL8nhXtWJg4OUvetb2gmKuzNKAcwE7fXi%2FQ7IPeiOR5ZlvcYjCSXvmuf30R%2BjpQSL086vQMEtqA20JNLhgj0m98Xhsnrslb6w8VerWBOohaD%2FgU9jbo%2FyhGLjdu8s4Rd0gFhxrPTjimFEc0ar%2B5U6UrEghPpflwGnQjVMIGr9n7KxW6MkFveKCZTL3VoXSZcPvukP6QP6uE3tasvq2ZflUMytPeoWT%2B%2BxcAyQVUhfnKqfrAk7aC7zBexEEFe9kIsTmA0R6iEhqpp%2BNGWdSSiMiJgWSadwhUzsmPbYvL%2Bi2uwQf8zykmoMI7soNAGOqUBI%2B2pc%2BoJXfHSJxVEwDy4%2BbKMTvOyPaJtqrx1UkLEYvbPTtCJ4SBYsJ5I%2BkMWBmtM1It2LDiYOdKEiGT4QUwNyDmR%2BujZ344CzDoHLXV0waN5BGCyx3YeMPpe14FKIXsM%2B2DPx%2BocOCPBbmpzC8i6zgyctuE%2FBZI9JdsTKZQ94FcEuhXIP85Xik8epPKx9K9jFINILzrQoGBFUEWgSThl7EHacwGI&X-Amz-Signature=a2fef84044ce6ddb860619cf6f79ae84a8a141f594d0577aeb7f087a752fa824&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753PUOCY%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T131127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0zY1j2NitXxP6RaeWEhPN%2B3YrUyCOhsjCxo9qd3II9QIgQxPXSdWOD%2B1T4rhVorWh2sfdIeM0%2FDgQ9vxZNvPdN4UqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM5dxsnQs4GhnRjxbCrcAxRmfSTTzgv9asinl3HLDQ%2F5shvQxXHMhwDP5eMDmuFMLpS%2FF2PSVkHrW1U2Gczlb10tnnutTZrA4afO4kxIZMK0%2BsFGNFurSj0F9SwgAaLz415ttr8iDeWG4WuSxI7sh3SnZrLvWPKE9%2F8kK1%2BllqCCMImNbCllAWMqlcl6Bfqtf4G1M3GIoVZpZu98mRYREcr7HZpfi35tq0THr0KBLXw4KHkiixoeDrQQHyocBOyNka%2FkRZsTKJsXLo6JDFi0BmR3nyd6w7W5yq2TYnU1KrzBZ3w60CvTKfbPNX1w0JCD7gqN2LHqTCzQAbxZhpGwxQWEjYpmkL8nhXtWJg4OUvetb2gmKuzNKAcwE7fXi%2FQ7IPeiOR5ZlvcYjCSXvmuf30R%2BjpQSL086vQMEtqA20JNLhgj0m98Xhsnrslb6w8VerWBOohaD%2FgU9jbo%2FyhGLjdu8s4Rd0gFhxrPTjimFEc0ar%2B5U6UrEghPpflwGnQjVMIGr9n7KxW6MkFveKCZTL3VoXSZcPvukP6QP6uE3tasvq2ZflUMytPeoWT%2B%2BxcAyQVUhfnKqfrAk7aC7zBexEEFe9kIsTmA0R6iEhqpp%2BNGWdSSiMiJgWSadwhUzsmPbYvL%2Bi2uwQf8zykmoMI7soNAGOqUBI%2B2pc%2BoJXfHSJxVEwDy4%2BbKMTvOyPaJtqrx1UkLEYvbPTtCJ4SBYsJ5I%2BkMWBmtM1It2LDiYOdKEiGT4QUwNyDmR%2BujZ344CzDoHLXV0waN5BGCyx3YeMPpe14FKIXsM%2B2DPx%2BocOCPBbmpzC8i6zgyctuE%2FBZI9JdsTKZQ94FcEuhXIP85Xik8epPKx9K9jFINILzrQoGBFUEWgSThl7EHacwGI&X-Amz-Signature=5f82537035545a14fa2d55076b71131bdca679bc2cd18fda19e9b9926bc32848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







