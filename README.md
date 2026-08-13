



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FXJGRHT%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T071740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBqxTaV2G3m0POIO6nWIy3jQnUse4hKxem%2FrWRYqO6kCAiEAwuGg1TL6WrhwnUqaU1qpNNpSTU0rH6FDGjgR8x8BnfgqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNhCOpnFhg%2FkJ9KRCrcA4nEGqChKf6Cq8nlPTKYMZj5ImFcijatMlZp8O76ZSde1%2FcBWZD8spMW5B%2BNhYX3uOJ8WcJAf4641sa3GreSThYXRkvbT2zTuwkzXhQZtdr8%2FQGeQeG%2B47I%2FMkRgnLSgkMSAyWmR%2BVbZsnM0ZVw%2BdyWL%2F5kdaM1v3ThwUA8N5dqDllPbFhWLmqGmDAOYee2G75D29VjIT7hqgFSxIWKsPK262hLEFb8%2BdMFVy2cXttD68T5lAt%2FUiiQn2wKoiHtw5lfcwTVzXxlFgSbXpm2Bn4DxmTMQhe6q2lBrLW4UELGif%2B6vKSWe11Y%2BBGiu8p1fiYPr2dT5cfuVvdONaChJxqsTYJX6vO2OcGG3azfFr7am1RwsxS2dnikyF7VCw3UuJtI%2BP3HvnK3cvt0qv3iaQTn8IRtM5EDT2GmomjonEizbZFnor61p5wIJhIjUc7E41O9tJc0HdjBT%2BRH%2BDZIwpOtaJomjGu4w9HyucGP7hLjZ4%2FoecZhAs3Kygwbyaxlt6cXFr%2BBIj80q3WXHu%2BHg90bYakVD9MXeX9dJYtRqQlb%2BqXwoPb1q8vaqqzv8vuKkdVTqZITW7s%2BllqQnNEQ1y3eYN6bjht8SRyvC%2B%2B%2FFbB09d8M4UZUQC4vTjPGFMJW99dMGOqUBOKHxrLbk80DPR7gqIa6yBzRllF%2F6YYmDWClROBxTogtJzzH0qZiCw5yJ40O4tFISFbeEbYvwYFq6TGnSSiRq2WXP2q2w%2FV9vzBxNHt76OGxPkPJmquJxW%2FkRkeh1J1889YVJXiSMvgH1ufOALtQobMRibZ5kmA7H9brPr6iGya7doGSbsZ3TbYFRtDD9h31LFWhYT%2Fe2Tj5muVTtZtaIALjJBFEE&X-Amz-Signature=e3fff5522c8c55eb918b1a88cd0cd51815005cc27fbac2de773f70b1a24e256e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FXJGRHT%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T071740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIBqxTaV2G3m0POIO6nWIy3jQnUse4hKxem%2FrWRYqO6kCAiEAwuGg1TL6WrhwnUqaU1qpNNpSTU0rH6FDGjgR8x8BnfgqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNhCOpnFhg%2FkJ9KRCrcA4nEGqChKf6Cq8nlPTKYMZj5ImFcijatMlZp8O76ZSde1%2FcBWZD8spMW5B%2BNhYX3uOJ8WcJAf4641sa3GreSThYXRkvbT2zTuwkzXhQZtdr8%2FQGeQeG%2B47I%2FMkRgnLSgkMSAyWmR%2BVbZsnM0ZVw%2BdyWL%2F5kdaM1v3ThwUA8N5dqDllPbFhWLmqGmDAOYee2G75D29VjIT7hqgFSxIWKsPK262hLEFb8%2BdMFVy2cXttD68T5lAt%2FUiiQn2wKoiHtw5lfcwTVzXxlFgSbXpm2Bn4DxmTMQhe6q2lBrLW4UELGif%2B6vKSWe11Y%2BBGiu8p1fiYPr2dT5cfuVvdONaChJxqsTYJX6vO2OcGG3azfFr7am1RwsxS2dnikyF7VCw3UuJtI%2BP3HvnK3cvt0qv3iaQTn8IRtM5EDT2GmomjonEizbZFnor61p5wIJhIjUc7E41O9tJc0HdjBT%2BRH%2BDZIwpOtaJomjGu4w9HyucGP7hLjZ4%2FoecZhAs3Kygwbyaxlt6cXFr%2BBIj80q3WXHu%2BHg90bYakVD9MXeX9dJYtRqQlb%2BqXwoPb1q8vaqqzv8vuKkdVTqZITW7s%2BllqQnNEQ1y3eYN6bjht8SRyvC%2B%2B%2FFbB09d8M4UZUQC4vTjPGFMJW99dMGOqUBOKHxrLbk80DPR7gqIa6yBzRllF%2F6YYmDWClROBxTogtJzzH0qZiCw5yJ40O4tFISFbeEbYvwYFq6TGnSSiRq2WXP2q2w%2FV9vzBxNHt76OGxPkPJmquJxW%2FkRkeh1J1889YVJXiSMvgH1ufOALtQobMRibZ5kmA7H9brPr6iGya7doGSbsZ3TbYFRtDD9h31LFWhYT%2Fe2Tj5muVTtZtaIALjJBFEE&X-Amz-Signature=f109e6eeb53f9618164abe0eb4dbf8b7816098e96fc1ce211ea4584a8ca68b23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







