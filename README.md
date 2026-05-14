



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JXJL4M6%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T024113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9AmpBUigYR9KnGYwqTQY4WMzJMVBJR34u1KfZ6ERGAAiEAqqC7bSccPdanr2xlvHOa7EiOVG4x2l5NSoujjSMdbiMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDBnFtoiy2d31sD0jeyrcA9MimrpuMzb9ngLyb%2F24C%2B178J0VLHXQFSa6uTMgwyu1UzpEUS0nHWmOfmMIjh2G%2BCYVqRKwYA1xF3whU8rYF%2FueZE1JCM2UWHCbMYgS5sNIsP65ohVRV4r5OC7k6E6yB27oamRuMsP6QIT1L1i%2Bfa7llyZnIAgmwCmKk9fAZ28wz21Rda6rvXSgEenQJE4WI6za9xZ2RYkfuq2MxP4uT1v4y878%2FJKHdDgfH8Dt2zMuHOgiJbK5CEb%2BlsSdXpzDmb%2F4x%2F9XufeposHhySPrNXWtFcH5QBsVHf%2BnWWA%2BbsAdrVLBtiQNOdWbbPIFaVcoXjEmnYfnVVnmBgKd9FuzhfS%2F0LRHsZYkzlD2Zsw%2F%2F%2BZIx0G43QqzEj0pbpHSyThlhmGFHq8HkbSnNyYbWdhnb3HpYvFIXJpNmAVj0G%2F00P1x4Cy94jqFVCYFUHK3U2Vi7R0DgXPja1SUylLgtShwgOuCMjD37LrQzgX%2FtpAR7SMQGLC29kh26BQOgKrf5LAo%2FJhlZLX1GeCMhrAVJq%2Bojqao2KHOlkQcOjjOkrTC%2BVPUYD4wrn3Zz7MhZ9wpaeWg9nDpZCFS6HX3OMN8dRxODQ03HglgJbc3gp7l1Sq58qV0P%2BwZgeO38kT6E2QgMODAlNAGOqUB54NnEpUlUhkDXuBShn7kZuCI2%2FdiZbDWh5NLxI49XycNh1LXCwgbvY7czK2FD%2FwR7TQHPU%2BTzz4i2Za%2BYajwmEt1lsJycu2WQg1lAgjO5FQPAPC%2B5MBudGJOjJORJyIW89r8UwtRkqq9VdCeoJDq9bLjK7C71ibWdbB8ec6t15dqhdT2yCed%2B7jkG5u24B2aOVaJXrkhbVNZ1UvBsQTLxTx805sq&X-Amz-Signature=9d029fb08a91996dd9622d4b384b9741a907fdbd3759179e4960827346fd3c14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JXJL4M6%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T024114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9AmpBUigYR9KnGYwqTQY4WMzJMVBJR34u1KfZ6ERGAAiEAqqC7bSccPdanr2xlvHOa7EiOVG4x2l5NSoujjSMdbiMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDBnFtoiy2d31sD0jeyrcA9MimrpuMzb9ngLyb%2F24C%2B178J0VLHXQFSa6uTMgwyu1UzpEUS0nHWmOfmMIjh2G%2BCYVqRKwYA1xF3whU8rYF%2FueZE1JCM2UWHCbMYgS5sNIsP65ohVRV4r5OC7k6E6yB27oamRuMsP6QIT1L1i%2Bfa7llyZnIAgmwCmKk9fAZ28wz21Rda6rvXSgEenQJE4WI6za9xZ2RYkfuq2MxP4uT1v4y878%2FJKHdDgfH8Dt2zMuHOgiJbK5CEb%2BlsSdXpzDmb%2F4x%2F9XufeposHhySPrNXWtFcH5QBsVHf%2BnWWA%2BbsAdrVLBtiQNOdWbbPIFaVcoXjEmnYfnVVnmBgKd9FuzhfS%2F0LRHsZYkzlD2Zsw%2F%2F%2BZIx0G43QqzEj0pbpHSyThlhmGFHq8HkbSnNyYbWdhnb3HpYvFIXJpNmAVj0G%2F00P1x4Cy94jqFVCYFUHK3U2Vi7R0DgXPja1SUylLgtShwgOuCMjD37LrQzgX%2FtpAR7SMQGLC29kh26BQOgKrf5LAo%2FJhlZLX1GeCMhrAVJq%2Bojqao2KHOlkQcOjjOkrTC%2BVPUYD4wrn3Zz7MhZ9wpaeWg9nDpZCFS6HX3OMN8dRxODQ03HglgJbc3gp7l1Sq58qV0P%2BwZgeO38kT6E2QgMODAlNAGOqUB54NnEpUlUhkDXuBShn7kZuCI2%2FdiZbDWh5NLxI49XycNh1LXCwgbvY7czK2FD%2FwR7TQHPU%2BTzz4i2Za%2BYajwmEt1lsJycu2WQg1lAgjO5FQPAPC%2B5MBudGJOjJORJyIW89r8UwtRkqq9VdCeoJDq9bLjK7C71ibWdbB8ec6t15dqhdT2yCed%2B7jkG5u24B2aOVaJXrkhbVNZ1UvBsQTLxTx805sq&X-Amz-Signature=9171e5822898d7a715927c1d7aa82363597a8c257e99f48a90080aa094a70d92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







