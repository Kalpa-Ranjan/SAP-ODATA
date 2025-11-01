



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3EUFZB%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T181909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQC%2Fq%2ByYn301l2KoVFMV9eB1dfhmdh3PvLi97I3bMtDQpgIgSasmOVydSfYBmoE4Xts5o2JzoVVEi6ZxyZm5A%2B1ReEAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDA3kD8rnRqeSsk6ypyrcAx6ebi7Zb%2Bh6LGUiIzIekx4XpfYFKFyLBfI3y%2BQMykgz8qNXNE4PtZie2TJMsVWGOKNxOC%2F09TpIZCNTnguSXlqnL%2Fpeig7J7EFIMne9klF0RtR7NVFWtSUQQ2SobL1T5fFdf6TEVjTiRB%2Bk1NazMXG9iEx3DX1X1xTre%2Fk%2FxYK2sQ2fEz5ixBVWtNyP%2BmZiZbW%2FhFzMUvzsriV05U15Tuo8%2BUk%2BI4tMS7KVpoeqWYo1dAQu8o%2FrkWnOZxMYaQzyO0o3DPbvOQTHoM%2Flr5miF6LSEYc2RHJstuHyt1TqlcD%2FnKgWY5T%2FmsisrhC3BipOaE%2FqufaQJqI8%2BVZSOCh2DO83uR11fQYVFvnoketgALi8l0w99FvfrajXbkj0jUJDxcoI04ddDoCeo0t%2BGJKLqXS1rh%2BltwL4cKnGvcMKyCrH1%2F0w%2FdunNZ5yflyuxy32l1gl7k8gkjwY1mLpoRfc%2FZ%2BUP2Zr2BiVqBkQbXUbVeGU0v9rAJi0AW4pv4glZa672Xde9%2FKvCy5EyRaizd7S0dK%2BByOLymrdCaYyAWwMvhtKOvfyq2ohz67htY0%2B0RayN3RL%2FiZxauE4I3XQ6Lqxpx4zidyavRx4YHSEqltfbWeumbrOh%2F%2FmYzfWALLqMMWPmcgGOqUBvIzDz%2FjUpCtfDIIM%2FAzruZaWI6M8SITdfsoPFLOG4dIKzStdgQU0WgVBDPnqxlGIM3kRYY8ofhyfKWdU0f4BIgL1c2pyJisRiijmlJfzyllP3X%2FZmmHpr8PR4FxFxt57QX1Q7rks48FaYB%2BZfNkHahoOc98g%2FtNvzzrbKZIWw4xamGRsnSoHbUxzAgniX%2BL87iQ6Cnqnuf2Kc2GuKJm3Lf2jXrJI&X-Amz-Signature=a6b6751cbcbd007f6f945d4dc79f7cfab58870fa28acf2a8588789f321a6eb50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3EUFZB%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T181909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQC%2Fq%2ByYn301l2KoVFMV9eB1dfhmdh3PvLi97I3bMtDQpgIgSasmOVydSfYBmoE4Xts5o2JzoVVEi6ZxyZm5A%2B1ReEAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDA3kD8rnRqeSsk6ypyrcAx6ebi7Zb%2Bh6LGUiIzIekx4XpfYFKFyLBfI3y%2BQMykgz8qNXNE4PtZie2TJMsVWGOKNxOC%2F09TpIZCNTnguSXlqnL%2Fpeig7J7EFIMne9klF0RtR7NVFWtSUQQ2SobL1T5fFdf6TEVjTiRB%2Bk1NazMXG9iEx3DX1X1xTre%2Fk%2FxYK2sQ2fEz5ixBVWtNyP%2BmZiZbW%2FhFzMUvzsriV05U15Tuo8%2BUk%2BI4tMS7KVpoeqWYo1dAQu8o%2FrkWnOZxMYaQzyO0o3DPbvOQTHoM%2Flr5miF6LSEYc2RHJstuHyt1TqlcD%2FnKgWY5T%2FmsisrhC3BipOaE%2FqufaQJqI8%2BVZSOCh2DO83uR11fQYVFvnoketgALi8l0w99FvfrajXbkj0jUJDxcoI04ddDoCeo0t%2BGJKLqXS1rh%2BltwL4cKnGvcMKyCrH1%2F0w%2FdunNZ5yflyuxy32l1gl7k8gkjwY1mLpoRfc%2FZ%2BUP2Zr2BiVqBkQbXUbVeGU0v9rAJi0AW4pv4glZa672Xde9%2FKvCy5EyRaizd7S0dK%2BByOLymrdCaYyAWwMvhtKOvfyq2ohz67htY0%2B0RayN3RL%2FiZxauE4I3XQ6Lqxpx4zidyavRx4YHSEqltfbWeumbrOh%2F%2FmYzfWALLqMMWPmcgGOqUBvIzDz%2FjUpCtfDIIM%2FAzruZaWI6M8SITdfsoPFLOG4dIKzStdgQU0WgVBDPnqxlGIM3kRYY8ofhyfKWdU0f4BIgL1c2pyJisRiijmlJfzyllP3X%2FZmmHpr8PR4FxFxt57QX1Q7rks48FaYB%2BZfNkHahoOc98g%2FtNvzzrbKZIWw4xamGRsnSoHbUxzAgniX%2BL87iQ6Cnqnuf2Kc2GuKJm3Lf2jXrJI&X-Amz-Signature=b1de154c7908dfd098552dbc6e0fd90a39ce4e517333abe230cd525d32a58b77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







