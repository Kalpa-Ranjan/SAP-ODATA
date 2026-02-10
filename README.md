



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIFM2PWS%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T185919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHytosDVEY7PfVhDo3nZpxHtJjGkj%2FMEz23KiwOUqfv0AiEA4DkZddvTWjLwrg3HmbEJj5lA5JqhB%2BhB9l6UykexvBsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7NZd1MZzAeP63yLSrcA2C4vLodbCXgk1YvA3zWBteXu5H%2FqVtm7waD2fX%2F5IzDpRgPGmuTPspLFTqIJ8WtqW3m0hd%2BWK5ptUL4MufS27Jos5i74zYaZVkOivOHWv7thVKF0syYOVMSanz0wDI%2F0RA7JZydQtdba%2FlXYiOrT%2BYW3kom5j%2BAuH%2BNdRo%2FRzIdGT1FAQVx%2FAg%2FMUYZcv%2B86yya2NgHY2%2BXqKDHKuG3QJo0Re4QLu6cUvdbLH4axhzGtceNwdQrtu43K7piY4xzqc9FahPSEBPN1jJFSTNLqX6W3tJCwwZKAMkDqcZlZZJJvhk%2BDq%2FkTHo6e%2Bb008gfRJ4G5H%2BmnVKjMxEx0wyzWXPhixSeYdZMS0tUrYzXZeczckOv%2BolqTV0RDdSPhYfU%2FjaccNVK%2BLm2esWDkUTZKUThu8PrOW%2BZdgsGi3aWVGDdhMV5cFVUyhsW18%2BGYf8T5cHyFQT1WGT3qWfwiuXDW92gsNNiSq1%2BGOhRBsZyyzbGp%2F626qaljThAV2L6UNj1Pe7KmkQpaukYZKFUHd7zT1t6jzTOSK8aiDl6jV5bY3WDwKCjXrlCAq9ZzU5adP%2FUBLcuPE6sHr%2Ba4UFLuna4km01QgUHMYzi99LZJWYnSaG3RunwnPRIJAvU3crIMPXdrcwGOqUB1r5O3gtKZHI4ROQzCP32hxO92SYr0nIZN74ghkJnm4IEQ1Lru12tmLe%2FO588s%2FlZskjoCvx83KfAhNWjvy1y0XboAvCO4I0U3C7OgFPV%2Br9CpKM2yqclKXfVxPI00vxuiVn7DUZ42iV8I2y36pmTl6tfL0wjWribx2cL4lN0hWUS2fhyCLgZKeDdiQvkEUSIYqR5WiWRk5g7v4IS8WpFk9OyqkgU&X-Amz-Signature=3fb7289088c6e94a7234ea22e051b9951f937f0be29e3a67c1958ca2b3ad3b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIFM2PWS%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T185919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHytosDVEY7PfVhDo3nZpxHtJjGkj%2FMEz23KiwOUqfv0AiEA4DkZddvTWjLwrg3HmbEJj5lA5JqhB%2BhB9l6UykexvBsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7NZd1MZzAeP63yLSrcA2C4vLodbCXgk1YvA3zWBteXu5H%2FqVtm7waD2fX%2F5IzDpRgPGmuTPspLFTqIJ8WtqW3m0hd%2BWK5ptUL4MufS27Jos5i74zYaZVkOivOHWv7thVKF0syYOVMSanz0wDI%2F0RA7JZydQtdba%2FlXYiOrT%2BYW3kom5j%2BAuH%2BNdRo%2FRzIdGT1FAQVx%2FAg%2FMUYZcv%2B86yya2NgHY2%2BXqKDHKuG3QJo0Re4QLu6cUvdbLH4axhzGtceNwdQrtu43K7piY4xzqc9FahPSEBPN1jJFSTNLqX6W3tJCwwZKAMkDqcZlZZJJvhk%2BDq%2FkTHo6e%2Bb008gfRJ4G5H%2BmnVKjMxEx0wyzWXPhixSeYdZMS0tUrYzXZeczckOv%2BolqTV0RDdSPhYfU%2FjaccNVK%2BLm2esWDkUTZKUThu8PrOW%2BZdgsGi3aWVGDdhMV5cFVUyhsW18%2BGYf8T5cHyFQT1WGT3qWfwiuXDW92gsNNiSq1%2BGOhRBsZyyzbGp%2F626qaljThAV2L6UNj1Pe7KmkQpaukYZKFUHd7zT1t6jzTOSK8aiDl6jV5bY3WDwKCjXrlCAq9ZzU5adP%2FUBLcuPE6sHr%2Ba4UFLuna4km01QgUHMYzi99LZJWYnSaG3RunwnPRIJAvU3crIMPXdrcwGOqUB1r5O3gtKZHI4ROQzCP32hxO92SYr0nIZN74ghkJnm4IEQ1Lru12tmLe%2FO588s%2FlZskjoCvx83KfAhNWjvy1y0XboAvCO4I0U3C7OgFPV%2Br9CpKM2yqclKXfVxPI00vxuiVn7DUZ42iV8I2y36pmTl6tfL0wjWribx2cL4lN0hWUS2fhyCLgZKeDdiQvkEUSIYqR5WiWRk5g7v4IS8WpFk9OyqkgU&X-Amz-Signature=9e677c73ba6db58f828d569d643948833e85306b6c74c688b01534ef353ca082&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







