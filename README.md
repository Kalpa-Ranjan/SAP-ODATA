



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7O4FZV%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T121057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIF8nfw02lBNid3%2FrpivxN%2BB7ePsXjmEaJaCZZ2o9O23jAiEA%2FBIP9Y%2FYu1yTZ01vgj9c7%2FJgU3vqXzpCCCR9RyXtCXoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAK1Rd46go4jyzN%2BCSrcAx9VeZgzLr6zSs6JqbJxGeUw1%2FJRUfj0E0ZXcxNmejf4MNL7q5zm7BJks8qa6oQ8pPLQZH3ognKOlRJWQegU6U7OyUBM82xS0qWu5YwKMmeAIA1eCtpxeUJvYJTKidSD1usiT9brKbY5xeq0QMfQrGSSFVZB3L6WRv8%2Fdtd5zq2CMMDQUK1M2Mh8uGTik8cZ2JWYPMNkgpIMrvExsWpdOvMQDFgGfCXcuZek9WqwLB2G5OyqTTios%2BWpATrZgvKEvJcaBzD2WYQczmO3OKCUcjfQLxuIR4OYnWfhpsuSvtFi7ZdCjbR2izpdFJQFv%2BRDM7inoSPSXRyyYmUWQGkmphUkksmgkTgckmkJon1w2J6sOIjoOXmw2QNZg9p5FC5KATE5XJbHUDNDNMxrmRvSeBOCxnpQEqAvurgs4EPGH%2Frf7ASvaYEx219Pt9mq5gQN5ufxOSO61VbYqXAKYCYBagkTV7%2B9gIl2B1Y7O5mRm%2BS0B7VflFWpEoFsfZwknMrxZY7I0rIwOwqSb8HWe5aSsTt03bCtdB6FDX6LW8PjX9YDcVAsitKUg2l6QzAsL23uO3u2KkWp%2Fz7cJg3K%2F9bhtt%2Fdi5TshqjCVBIqk8T4JJUtj9SgjASNw9idOZ1kMJXCs9UGOqUBLu%2B7BmWSa%2BpJxkzZ%2FyRdJpHSJR%2Fn9RPovEXM1CnRQipLR3amMY3Jc5gcGZ9FjRj9MdnP8WzH6ibQzQrmIJ0bckJ6sLnFxxudj1zBpoWLzWfu0BxSPq%2B93wCZl4xx6LvyR1C1iZ09uWxd8c9FmGmnCSrfcB7qsuRGU0SSLl6lZpeU8Vv1JhmClKVIpBOC6wMUHtxV6yBAYLuLfpyn7XK2f7B1C5mC&X-Amz-Signature=8f1ce62cc7d8d9d44fcb2e684fe13af2be57f8df5939fee11c13fad56309f5a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7O4FZV%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T121057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIF8nfw02lBNid3%2FrpivxN%2BB7ePsXjmEaJaCZZ2o9O23jAiEA%2FBIP9Y%2FYu1yTZ01vgj9c7%2FJgU3vqXzpCCCR9RyXtCXoq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDAK1Rd46go4jyzN%2BCSrcAx9VeZgzLr6zSs6JqbJxGeUw1%2FJRUfj0E0ZXcxNmejf4MNL7q5zm7BJks8qa6oQ8pPLQZH3ognKOlRJWQegU6U7OyUBM82xS0qWu5YwKMmeAIA1eCtpxeUJvYJTKidSD1usiT9brKbY5xeq0QMfQrGSSFVZB3L6WRv8%2Fdtd5zq2CMMDQUK1M2Mh8uGTik8cZ2JWYPMNkgpIMrvExsWpdOvMQDFgGfCXcuZek9WqwLB2G5OyqTTios%2BWpATrZgvKEvJcaBzD2WYQczmO3OKCUcjfQLxuIR4OYnWfhpsuSvtFi7ZdCjbR2izpdFJQFv%2BRDM7inoSPSXRyyYmUWQGkmphUkksmgkTgckmkJon1w2J6sOIjoOXmw2QNZg9p5FC5KATE5XJbHUDNDNMxrmRvSeBOCxnpQEqAvurgs4EPGH%2Frf7ASvaYEx219Pt9mq5gQN5ufxOSO61VbYqXAKYCYBagkTV7%2B9gIl2B1Y7O5mRm%2BS0B7VflFWpEoFsfZwknMrxZY7I0rIwOwqSb8HWe5aSsTt03bCtdB6FDX6LW8PjX9YDcVAsitKUg2l6QzAsL23uO3u2KkWp%2Fz7cJg3K%2F9bhtt%2Fdi5TshqjCVBIqk8T4JJUtj9SgjASNw9idOZ1kMJXCs9UGOqUBLu%2B7BmWSa%2BpJxkzZ%2FyRdJpHSJR%2Fn9RPovEXM1CnRQipLR3amMY3Jc5gcGZ9FjRj9MdnP8WzH6ibQzQrmIJ0bckJ6sLnFxxudj1zBpoWLzWfu0BxSPq%2B93wCZl4xx6LvyR1C1iZ09uWxd8c9FmGmnCSrfcB7qsuRGU0SSLl6lZpeU8Vv1JhmClKVIpBOC6wMUHtxV6yBAYLuLfpyn7XK2f7B1C5mC&X-Amz-Signature=af10aebfafd04b8e8f3a23d4807f6673e4a1af154b368593e91f0433f18cdcd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







