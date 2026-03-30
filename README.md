



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYNNSYHF%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T185338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIDPRgyQ8tE6KGIke3ejLwT1D%2BjQ0HY%2B4sBY1MCCXquUWAiBUxcdPxN%2BYwOW%2BNx%2FWySGHztSLo%2FAYkhB2y81KPp0q9ir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMVK8UMLKeOy1fOzxtKtwDo9pBYd7%2BBCKqSR%2FHWGabfWZn1MXBBKnBJU0fX1e9Hm463x7tT6Ax9mXTUccnU4YNUn7rU5FHh3kKIaIJnaUSp98hmsZcXsd6BbV3cFHzzGUJCIbeI9VemfSSd90fCdRCdPQqqbWbyEj%2F3zOmq3dH0gn8HTS1gAAwhvnX11QUD%2BtOMuHeSQYgDcKbAjakKBHeGSxHw7qwUq%2F%2FpHuLCMiJmw8L7gwxyIg2FMRmS1f5K6ZMglwf6dvkzUH2I8giXt6s243%2BeJvwI98MPQhBsjkaN4wpcHp1qD5eNQO%2FGwKQN%2FvBls%2Fffx0TZ%2BPUd0XvM6tBQ1GYici2AaeLwg0f2A2LV0pKKmC1SGBwceWDGz4q9e%2BCwhlzU2CJtL%2BcCjiR18IYUlU6buY8kfLBHkJydYcCacw4%2Fp9Y8qYoc84iWOXd57rDiufX5PvaddDBNqCZHbiMFs76b5sGSJq%2FYNmjtH7lx%2BgGipIlX3hdBw%2F33lua%2Fbg3J0H1rm1STja60XwmUJLDIGKCdE5v0ePxN6%2FrAYXrMhR2pYJf3R1JF%2BWwwFfDoaH5ZImDIE7YXE68oiy4euIfO4JRBPZdVJ21lMW9Dcv3NAeYkDIp5vypAWWWYjvKda%2FWKfXJMy7MvZcR1Skw04WrzgY6pgHYdhvFX7PGHtShdOy1%2B3hAve%2BqftvlpW%2F70Z0YlfqJv%2BVrXS7iQe3RxIY9DfkKYVUKwnipy4hGrMdcTFsLFqd4CXnG4proMC9ZL7FoR0UDsVgV3QmKsYnW%2Fq%2F5QF7kmYxlT5QjnEVvEiSnbnqJwF3LzuvbelaJz8FVJZcaNV6EuvXCiVi1LJunMPLdr9pEiWvCqCcfSq5qtKWDGTII%2FGnbW3J3pw3l&X-Amz-Signature=7146091f0832988f032f1e4f50a3e5c86b161b85353e733c746726658c907586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYNNSYHF%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T185338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIDPRgyQ8tE6KGIke3ejLwT1D%2BjQ0HY%2B4sBY1MCCXquUWAiBUxcdPxN%2BYwOW%2BNx%2FWySGHztSLo%2FAYkhB2y81KPp0q9ir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMVK8UMLKeOy1fOzxtKtwDo9pBYd7%2BBCKqSR%2FHWGabfWZn1MXBBKnBJU0fX1e9Hm463x7tT6Ax9mXTUccnU4YNUn7rU5FHh3kKIaIJnaUSp98hmsZcXsd6BbV3cFHzzGUJCIbeI9VemfSSd90fCdRCdPQqqbWbyEj%2F3zOmq3dH0gn8HTS1gAAwhvnX11QUD%2BtOMuHeSQYgDcKbAjakKBHeGSxHw7qwUq%2F%2FpHuLCMiJmw8L7gwxyIg2FMRmS1f5K6ZMglwf6dvkzUH2I8giXt6s243%2BeJvwI98MPQhBsjkaN4wpcHp1qD5eNQO%2FGwKQN%2FvBls%2Fffx0TZ%2BPUd0XvM6tBQ1GYici2AaeLwg0f2A2LV0pKKmC1SGBwceWDGz4q9e%2BCwhlzU2CJtL%2BcCjiR18IYUlU6buY8kfLBHkJydYcCacw4%2Fp9Y8qYoc84iWOXd57rDiufX5PvaddDBNqCZHbiMFs76b5sGSJq%2FYNmjtH7lx%2BgGipIlX3hdBw%2F33lua%2Fbg3J0H1rm1STja60XwmUJLDIGKCdE5v0ePxN6%2FrAYXrMhR2pYJf3R1JF%2BWwwFfDoaH5ZImDIE7YXE68oiy4euIfO4JRBPZdVJ21lMW9Dcv3NAeYkDIp5vypAWWWYjvKda%2FWKfXJMy7MvZcR1Skw04WrzgY6pgHYdhvFX7PGHtShdOy1%2B3hAve%2BqftvlpW%2F70Z0YlfqJv%2BVrXS7iQe3RxIY9DfkKYVUKwnipy4hGrMdcTFsLFqd4CXnG4proMC9ZL7FoR0UDsVgV3QmKsYnW%2Fq%2F5QF7kmYxlT5QjnEVvEiSnbnqJwF3LzuvbelaJz8FVJZcaNV6EuvXCiVi1LJunMPLdr9pEiWvCqCcfSq5qtKWDGTII%2FGnbW3J3pw3l&X-Amz-Signature=eeefedd6ab67e8c9d8091002d04f2334574af0dc6d6ea1a754632a5210cf304f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







