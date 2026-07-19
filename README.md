



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFYUMSY4%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T130457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH4LGYstBL0TaqeVdkZEqsglVwPKR35qbVqibtKfXjstAiBWBUVpMiHHAhNCejquOPIFjc%2FfzluDuG68E98ynqlzviqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzL4iXW9yzJ0qErBkKtwDdsvHeREsLXmO82PfZNJN6bUUnVxUe8CZoNZ60MAtQfOBu86NRNHT1D4402lqwAvy4h5MlNkPt60lfiLAs39vNxGko9YvTmwh8hNIBMMTmlW79TuuoKK7VrMfjEmN9DxmGEsEyO2vz%2Bs7Fwd73cuEJHtu5Pr%2By8ksbnOhQVq5oZ2wk%2BAKj70RA7rnFBn3AE9muzwV9Eg5gULP1PFyKZ8jVBv4CMhIn9foXcgZ1JlqQqFh9Jy1ee5nC3qzs4ZMQrfAUq80%2F%2FDRz0HGX0EG9V6na%2FwktceLmSgtfRbDmHvOyZAoNI9Bhu7RjDer1RKDwbKIsdfrA0AyiYomfnpPQmgOn1LLuOZG7zaEXQzT%2F9O%2FW4wg8bofHMOQDjH9u89HZ0y5wykS2I2ce0%2BUiDvwV6wV7EtKVtRsyuhzBFOSBilUIo25h6TuAENrf%2BX3O1wiAp9LNRX3S1hRwO8jseKryrbKuaF1jJeEutHiAco7wj7mlbTtO8iPp2dFMDS6f78uXjB8uAoUrUGW12URq5mRUvi7hoH9QrNNiwiT9o80mgB8FfyUgPgAUkHiNSKrrwMTdO02cZRyqE0v7ndMkKpRmVYRH1ZZFi02yMJHrR1FQ7UUbCFKvGC7%2FgsnxxtDZXEw46jy0gY6pgHNCngXeyr8DB9%2FSUAtblGwIo9BjfvGTxWEz%2F%2BkZv70WJuk96TBN0srr1OX5vEo4U2%2FzPCrX0EJ5wbLc1NnHgWwBenGR%2B%2FbhsRIqmT4XSz0vJrSioAdd5otTotq8I%2FCEEZhUMh0FDVxTGSeLFMGNkMU1gT5DqMkcmYePx7I6WCSiZdbgITAXQj66jlMcHNrY3C92GjZ8DyYcriV0kHnoBFAjTh01N%2Bg&X-Amz-Signature=592c939e2751410b91dcc0131384076ab71f059c69d328cd127c3928e828ca05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFYUMSY4%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T130458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH4LGYstBL0TaqeVdkZEqsglVwPKR35qbVqibtKfXjstAiBWBUVpMiHHAhNCejquOPIFjc%2FfzluDuG68E98ynqlzviqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzL4iXW9yzJ0qErBkKtwDdsvHeREsLXmO82PfZNJN6bUUnVxUe8CZoNZ60MAtQfOBu86NRNHT1D4402lqwAvy4h5MlNkPt60lfiLAs39vNxGko9YvTmwh8hNIBMMTmlW79TuuoKK7VrMfjEmN9DxmGEsEyO2vz%2Bs7Fwd73cuEJHtu5Pr%2By8ksbnOhQVq5oZ2wk%2BAKj70RA7rnFBn3AE9muzwV9Eg5gULP1PFyKZ8jVBv4CMhIn9foXcgZ1JlqQqFh9Jy1ee5nC3qzs4ZMQrfAUq80%2F%2FDRz0HGX0EG9V6na%2FwktceLmSgtfRbDmHvOyZAoNI9Bhu7RjDer1RKDwbKIsdfrA0AyiYomfnpPQmgOn1LLuOZG7zaEXQzT%2F9O%2FW4wg8bofHMOQDjH9u89HZ0y5wykS2I2ce0%2BUiDvwV6wV7EtKVtRsyuhzBFOSBilUIo25h6TuAENrf%2BX3O1wiAp9LNRX3S1hRwO8jseKryrbKuaF1jJeEutHiAco7wj7mlbTtO8iPp2dFMDS6f78uXjB8uAoUrUGW12URq5mRUvi7hoH9QrNNiwiT9o80mgB8FfyUgPgAUkHiNSKrrwMTdO02cZRyqE0v7ndMkKpRmVYRH1ZZFi02yMJHrR1FQ7UUbCFKvGC7%2FgsnxxtDZXEw46jy0gY6pgHNCngXeyr8DB9%2FSUAtblGwIo9BjfvGTxWEz%2F%2BkZv70WJuk96TBN0srr1OX5vEo4U2%2FzPCrX0EJ5wbLc1NnHgWwBenGR%2B%2FbhsRIqmT4XSz0vJrSioAdd5otTotq8I%2FCEEZhUMh0FDVxTGSeLFMGNkMU1gT5DqMkcmYePx7I6WCSiZdbgITAXQj66jlMcHNrY3C92GjZ8DyYcriV0kHnoBFAjTh01N%2Bg&X-Amz-Signature=7927c7f43ec776a80873d674e5ddceffbc19be47f0ff5b1b4ae45f2127d1989e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







