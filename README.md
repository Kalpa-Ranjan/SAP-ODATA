



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGAHHGX3%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T181024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDM8ypegG%2FQA9kRw8xjhTJVcXrA09TSnd%2BoVDdy0SZqygIhAPnO5yI1z96ez5Lp10nuF8odFdFP9U84VEkuzDfBsUlTKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGUfBId4HS%2B%2BW7e18q3AOCQCKFBDdO82tu3agC1QSnJMq2UP1SZIKjcfPFDXMZ29Ut2HIWcgIYU82u8Ie0Ls84wJ2Bsn%2BpnMa88RigPAo7dgpAJt2NMYHU6FbEE4f6YAzyH4q7Svn3w%2Ft1ZgMd1w8BaoIboH0VkxASpyWXzG9qvnImffOpf2w1MMTfY63HJX%2BqrS3tRNunI0rZNjXas5W18wa74mUGh8e7xNEQS3cHiosJA3r9bW3DC1jw6m7o63SvcNHOMriFQgZTG2AVM1UnNIRBlCM9yNsBX79Wi5FNGvlkQLmhMNlywgG2nrzcmgowWxTdd7Mc9AX4dlhPbxbouB5PygnjuttzEoz%2BuqfSjIEotK%2FgEcsSfTWnclW3Owt%2FNMwZeHrffS88EW4Oqzk9kP3jwxbi2F3B%2Beaijpmxp%2BWK4bdp7Xzp2sbI%2B77zx6uPK71Mn%2BZm37h5%2FjBnnb4HJn0nBPnf6DnV5ao%2FxxU97jLvBhP2TMlUVJVnShmU94OHbvaPCayOPmI6r84BkN7jXfsyd9N6JWVA4SPVejTIOeZ0oKGPqZ%2F334B%2F7PT3Qn4OGVyAXXA0qyKW1rHXJTnRIgLmO8Z%2BiYkW6ThdVgjjTxr5an0KEKtJ%2Bd8bR4%2FtVHAfHZ%2BUg9NgOyyzRzCkwo%2FWBjqkAdYcpINeM5gq8JxwB%2FP0Ga%2FDs4%2BXSusZPLRr5eeom4w8SSiZNhWOM7O2xW6hbyJ2x7K0NQFYNCFHdqa8zGQbFZpLv2pFSrQwk%2BppO81b2p8nIWQmGrhz%2BzrBjKzsznOiwSXd%2FEcmd0MPR8xyNO2iIffY6AyNszMSiEPObG2hseNF5M6rBf4GSV2ypvVtJNM5%2F5w%2FP49uiOVkiYCv5pk9MRhZFp3K&X-Amz-Signature=f3a371db1347c2f12afae9b5f9438f383fade173c7a5d30dc7ffb4ff415efbeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGAHHGX3%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T181024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDM8ypegG%2FQA9kRw8xjhTJVcXrA09TSnd%2BoVDdy0SZqygIhAPnO5yI1z96ez5Lp10nuF8odFdFP9U84VEkuzDfBsUlTKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGUfBId4HS%2B%2BW7e18q3AOCQCKFBDdO82tu3agC1QSnJMq2UP1SZIKjcfPFDXMZ29Ut2HIWcgIYU82u8Ie0Ls84wJ2Bsn%2BpnMa88RigPAo7dgpAJt2NMYHU6FbEE4f6YAzyH4q7Svn3w%2Ft1ZgMd1w8BaoIboH0VkxASpyWXzG9qvnImffOpf2w1MMTfY63HJX%2BqrS3tRNunI0rZNjXas5W18wa74mUGh8e7xNEQS3cHiosJA3r9bW3DC1jw6m7o63SvcNHOMriFQgZTG2AVM1UnNIRBlCM9yNsBX79Wi5FNGvlkQLmhMNlywgG2nrzcmgowWxTdd7Mc9AX4dlhPbxbouB5PygnjuttzEoz%2BuqfSjIEotK%2FgEcsSfTWnclW3Owt%2FNMwZeHrffS88EW4Oqzk9kP3jwxbi2F3B%2Beaijpmxp%2BWK4bdp7Xzp2sbI%2B77zx6uPK71Mn%2BZm37h5%2FjBnnb4HJn0nBPnf6DnV5ao%2FxxU97jLvBhP2TMlUVJVnShmU94OHbvaPCayOPmI6r84BkN7jXfsyd9N6JWVA4SPVejTIOeZ0oKGPqZ%2F334B%2F7PT3Qn4OGVyAXXA0qyKW1rHXJTnRIgLmO8Z%2BiYkW6ThdVgjjTxr5an0KEKtJ%2Bd8bR4%2FtVHAfHZ%2BUg9NgOyyzRzCkwo%2FWBjqkAdYcpINeM5gq8JxwB%2FP0Ga%2FDs4%2BXSusZPLRr5eeom4w8SSiZNhWOM7O2xW6hbyJ2x7K0NQFYNCFHdqa8zGQbFZpLv2pFSrQwk%2BppO81b2p8nIWQmGrhz%2BzrBjKzsznOiwSXd%2FEcmd0MPR8xyNO2iIffY6AyNszMSiEPObG2hseNF5M6rBf4GSV2ypvVtJNM5%2F5w%2FP49uiOVkiYCv5pk9MRhZFp3K&X-Amz-Signature=23727d286046e748b0597120ef3d3c7c05dbbbc9d769f23e2063e9ffcdfa6cd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







