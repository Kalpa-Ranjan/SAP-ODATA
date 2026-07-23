



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG5UF2TR%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T190617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIEQxLwpP0flDp12UVkDOuM0GtMNYf7L1NEwi1A7VeNkcAiEApkJOxc0PDxY3H49PGZQuKuWyaRd85MAwoiArTChIH24qiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDINto6p7drqOE%2BLvMircA2DiWYc7aCOsZCxBtUlU0nkUOjw1jGm2Be0D54uIUXbcadQsslc2yPbeSQH7rIYXjTG%2B1bIdLVnbkQwy7FONIopi%2FkhisXkTwBoD677BeZ7I2ATu1lVreeTbojNGrObHDUO1R1pkYP5kIfmNODua7slkmjbUx0aEys8Xv1oEDLOkkjp7Hcvrtig%2FK8%2Fi92ZRwh5p%2BGKw00G6mZpxz4CIxB%2FFSorMQ4TUmQSWQjZ7x36mUszaGiYRafFLWYXbPnjnyUmCT4eBkt9roS%2Fo2sFo7pDOk0fAzB%2FwbzKZNL8WZOdz4UqHN%2Bzk2A7nR%2BHshCZcWEpwYA1H1PbpWamg1NoeXEgqKksVEe8KCGT8RkYrIystUr7Ljmnt%2BwsGYZvVwOfoLIXw6PqUs0WIdPoViomeuhfm2RlvudmMMimrKy1wyij7nH3CQ05zLDKnN71CUXOHwxr8gWcfDw6p9qrUlRHcFfHrlfaLtC9%2Bz6bCRaJJb2OZIckfv1icJ6m0v5m1UvbI7xK8bNni8Sae%2FRf6bZomEW93y3qofmGOJgOpcaTb6EFsck%2BDPdDRyJunOuqU%2FSGhJgEJ93DmzwZcVOp%2B2z87H4aFOcQIZHk1IGeGYwRr0prkUDbYbR7WltZfPyBgMK6MidMGOqUBDAvS%2FXdlbb%2B%2FMJiM6NZvnYLsRlJMB%2F4QScH7HXcwT%2B2RR4aI58bx5yelilxwnUudLuvbfzg1PHScUbpENdC6fGB3%2FvBp2EP%2F7K0kLPVfMlHgbVFU3dBTG1n%2FuVtqNA8TeAor06YwNBuyNLKzGSyyd76Waeap57PNXCHVaO1aw0TYv7DfsDS%2F36ODuF0%2B1jJB%2B%2Fv4cXXZ%2FWMCd1MfcljthhqfK9yy&X-Amz-Signature=36dc45dde1fc33f644009ca7455154db48f91d660dee02171cd5ef93fc3137a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG5UF2TR%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T190617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIEQxLwpP0flDp12UVkDOuM0GtMNYf7L1NEwi1A7VeNkcAiEApkJOxc0PDxY3H49PGZQuKuWyaRd85MAwoiArTChIH24qiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDINto6p7drqOE%2BLvMircA2DiWYc7aCOsZCxBtUlU0nkUOjw1jGm2Be0D54uIUXbcadQsslc2yPbeSQH7rIYXjTG%2B1bIdLVnbkQwy7FONIopi%2FkhisXkTwBoD677BeZ7I2ATu1lVreeTbojNGrObHDUO1R1pkYP5kIfmNODua7slkmjbUx0aEys8Xv1oEDLOkkjp7Hcvrtig%2FK8%2Fi92ZRwh5p%2BGKw00G6mZpxz4CIxB%2FFSorMQ4TUmQSWQjZ7x36mUszaGiYRafFLWYXbPnjnyUmCT4eBkt9roS%2Fo2sFo7pDOk0fAzB%2FwbzKZNL8WZOdz4UqHN%2Bzk2A7nR%2BHshCZcWEpwYA1H1PbpWamg1NoeXEgqKksVEe8KCGT8RkYrIystUr7Ljmnt%2BwsGYZvVwOfoLIXw6PqUs0WIdPoViomeuhfm2RlvudmMMimrKy1wyij7nH3CQ05zLDKnN71CUXOHwxr8gWcfDw6p9qrUlRHcFfHrlfaLtC9%2Bz6bCRaJJb2OZIckfv1icJ6m0v5m1UvbI7xK8bNni8Sae%2FRf6bZomEW93y3qofmGOJgOpcaTb6EFsck%2BDPdDRyJunOuqU%2FSGhJgEJ93DmzwZcVOp%2B2z87H4aFOcQIZHk1IGeGYwRr0prkUDbYbR7WltZfPyBgMK6MidMGOqUBDAvS%2FXdlbb%2B%2FMJiM6NZvnYLsRlJMB%2F4QScH7HXcwT%2B2RR4aI58bx5yelilxwnUudLuvbfzg1PHScUbpENdC6fGB3%2FvBp2EP%2F7K0kLPVfMlHgbVFU3dBTG1n%2FuVtqNA8TeAor06YwNBuyNLKzGSyyd76Waeap57PNXCHVaO1aw0TYv7DfsDS%2F36ODuF0%2B1jJB%2B%2Fv4cXXZ%2FWMCd1MfcljthhqfK9yy&X-Amz-Signature=053b9277b36b8698dc45c75cc78e1b72148defdbcce7a1acbb3c319c57f242ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







