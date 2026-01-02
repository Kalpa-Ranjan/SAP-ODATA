



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBEWQA2%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T011840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQDvzb5n%2BFdEYwWhuJRrUpFgYYsX4fbrIpEDiMWLA%2FYNHAIhAJ2Nj72sJr3GplBYKyhoVcFXxdI377hAcJoAw1oxtgS0KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsUo4nCeA%2F9DNY0%2Bkq3AOPgYwlc3mz81PkOUqL9zEJUrYTp%2B0j65IuIHAkSd6Io4gSozQ2313rAxtH%2FlGhQNHKDUDGR0WZmCnlKD2ziMWYbTZe1srMfxl3AU6uL9DQt4Dn5vtONwHnGiq0bfRxUaplgqwW9xkGePJr1n1iheEA7drqoD%2F4zLkcoSGLUlDjVx8b7oiO3DwHY0fFA5gmKUCqaUi13tY%2BJSc8Zz1zwCQgfOzUiCENSOToimELTQoiM4WRnf4zQmuMxWphLWE0u%2BSZkX5slVfepXCrIgrIogWNQ4gBn7EvEbl1rOBTSQ36KkM1a19oTU9YV%2BTFSNRoNjzAmEU5P%2Fo07cmamapVXLS02%2BhIiuyitu2owSOc9CDNK7OS9BRrTEXHbeRFwcA4fVFRu5szbWOeqcaXIQB5uBht95eAkRh7dg1fIu1O1j2ojKSbGA88adaxOrSqOs4xabfyJWDc29n3R1VkPNOIR4RAcCrXQEF6UafnSi%2FoI5nPr8yHlJR6kJBkRlqMPgmcW23Gjj8u%2FJlZ1fQ05U9l%2Fy6Jovn7Av3jFi1M%2FVrzprmuzRo4MoxjbDiZxmhLGW%2BjyHdduwe%2FswAhpC3%2FaqbA%2BaHxLcWUzwuxyQ1PkgiZFWaBuExJGJFQj3by6alThTDml9vKBjqkAWB3iy2ScJEZBSlUg4Ivb%2B%2BwvyAWI6omW9sg1mdw1Yy%2FPmSUczsnAo%2BFhiqJ3UTwgFxZyYv80OyVgvjEzrx7VB%2FdjL6YR26BsYlaga3icE2xI2z5PBNOvpolm9Yg90OWOCHGOcBuULnMC41NMTSx3lXeWLc8QZ2IltQVsTuaRLYwxEPQ5Or2wjvUf6GcX0qWHGPJwMuy6%2ByPIGo4H21bOQmK7OMS&X-Amz-Signature=8df646e1d103d795c69f6c787e3ae469d2a887278e9e9e7c145f066327e4ec84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBEWQA2%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T011840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQDvzb5n%2BFdEYwWhuJRrUpFgYYsX4fbrIpEDiMWLA%2FYNHAIhAJ2Nj72sJr3GplBYKyhoVcFXxdI377hAcJoAw1oxtgS0KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsUo4nCeA%2F9DNY0%2Bkq3AOPgYwlc3mz81PkOUqL9zEJUrYTp%2B0j65IuIHAkSd6Io4gSozQ2313rAxtH%2FlGhQNHKDUDGR0WZmCnlKD2ziMWYbTZe1srMfxl3AU6uL9DQt4Dn5vtONwHnGiq0bfRxUaplgqwW9xkGePJr1n1iheEA7drqoD%2F4zLkcoSGLUlDjVx8b7oiO3DwHY0fFA5gmKUCqaUi13tY%2BJSc8Zz1zwCQgfOzUiCENSOToimELTQoiM4WRnf4zQmuMxWphLWE0u%2BSZkX5slVfepXCrIgrIogWNQ4gBn7EvEbl1rOBTSQ36KkM1a19oTU9YV%2BTFSNRoNjzAmEU5P%2Fo07cmamapVXLS02%2BhIiuyitu2owSOc9CDNK7OS9BRrTEXHbeRFwcA4fVFRu5szbWOeqcaXIQB5uBht95eAkRh7dg1fIu1O1j2ojKSbGA88adaxOrSqOs4xabfyJWDc29n3R1VkPNOIR4RAcCrXQEF6UafnSi%2FoI5nPr8yHlJR6kJBkRlqMPgmcW23Gjj8u%2FJlZ1fQ05U9l%2Fy6Jovn7Av3jFi1M%2FVrzprmuzRo4MoxjbDiZxmhLGW%2BjyHdduwe%2FswAhpC3%2FaqbA%2BaHxLcWUzwuxyQ1PkgiZFWaBuExJGJFQj3by6alThTDml9vKBjqkAWB3iy2ScJEZBSlUg4Ivb%2B%2BwvyAWI6omW9sg1mdw1Yy%2FPmSUczsnAo%2BFhiqJ3UTwgFxZyYv80OyVgvjEzrx7VB%2FdjL6YR26BsYlaga3icE2xI2z5PBNOvpolm9Yg90OWOCHGOcBuULnMC41NMTSx3lXeWLc8QZ2IltQVsTuaRLYwxEPQ5Or2wjvUf6GcX0qWHGPJwMuy6%2ByPIGo4H21bOQmK7OMS&X-Amz-Signature=61f0d63ae097935ae37449868ce827f7a7b085e417642629bb8cb8bf7e357de9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







