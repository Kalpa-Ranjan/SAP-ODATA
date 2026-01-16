



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJZHUD3C%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T062743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQDnMZmktKTguEPM0XHDot2flRHkcyfOrYttRkQl%2BwAl2AIgP7%2BxdHlzJ2gaSJ9j1glCEP%2FYWF7E%2FvGjHp6fKwTwXjgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGBSlg%2B4EFbwLLlwjircA8R1q77B3kwPNZH5muooNiZ7sDZZBUDHh9iZ1llif%2F9s0WSpAq7KnvXAmNAKhXIrdIXENiRXp9HeuTCpT598kkX%2Fgglwa%2Flnep3s2RQWoP1jHObR9n5%2BTJ5NgeZuansdzrW22pq03uxHMxKgPX40sd5fitt8j2jJnItmrfgYYVSpyR8mripWsRcy%2F%2BeWYbSDxf9sdXRJvZlVPklQOHB6vxCLLcoRJADKW8zTnPQD%2F6AfqYPuv99GpKmohCsfb9l8azmTd3aCBvF0j6rHRf0j5Nmd7pBUp6dIJISXkxDEScsASv4hL82GybRUO6O6vviw%2F%2B3LXHkO3pKfKX9sTqpeVydbL2xWkbSSbdhRES1x%2Fnq9U%2F%2BEkGpBA6R23UMauYnoc0mZaMkQZi4vGAwRaK0sV0lCW76dFci6M050b9uC7eVL5N6XwKfKhVyZcemTTe3T9xgLO0OHeK3w7s1KRicnspDNJJd2HhNcvJHGFbAQj1SA7ReD7oIGyWulmKC0u88e7WM%2BuUkvCNk3XNRrIcHaHV2xZr8VT8TfMd1Q%2BXMK2oxk18W%2F%2B53L1hSEvqtqTlUql9v0eUHQXVjUA4GCMF2dJmCFkcG0vF%2BiZ0MWx9b9uB%2BG11mi6kbpFPy7WqZhMOStp8sGOqUBy%2BKa%2F7rQtNb6HLYo25h5TkLMLzo45XvUVYbPRkTGl84YephWtM2k4i4f6fuzeWF%2FkVtAG%2BG3Jxr6eSc6h3AHsRKic%2FeLVgkupi7yiP09tNJQTGBDhSkaL4K9TmJX5%2B1FfgmfJWVchYAHo5dG8PnRD9OvAA7ARwgWtdoBuaaIYztZ4Rs6WicO3CyUjM0nwes8a1n6tH5i8avcNQZSmwn4IPrqpgow&X-Amz-Signature=0ce7307e30ded38274db3e087ba55fd1385bb0cc96b190f6cb7975f18410b9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJZHUD3C%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T062743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQDnMZmktKTguEPM0XHDot2flRHkcyfOrYttRkQl%2BwAl2AIgP7%2BxdHlzJ2gaSJ9j1glCEP%2FYWF7E%2FvGjHp6fKwTwXjgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGBSlg%2B4EFbwLLlwjircA8R1q77B3kwPNZH5muooNiZ7sDZZBUDHh9iZ1llif%2F9s0WSpAq7KnvXAmNAKhXIrdIXENiRXp9HeuTCpT598kkX%2Fgglwa%2Flnep3s2RQWoP1jHObR9n5%2BTJ5NgeZuansdzrW22pq03uxHMxKgPX40sd5fitt8j2jJnItmrfgYYVSpyR8mripWsRcy%2F%2BeWYbSDxf9sdXRJvZlVPklQOHB6vxCLLcoRJADKW8zTnPQD%2F6AfqYPuv99GpKmohCsfb9l8azmTd3aCBvF0j6rHRf0j5Nmd7pBUp6dIJISXkxDEScsASv4hL82GybRUO6O6vviw%2F%2B3LXHkO3pKfKX9sTqpeVydbL2xWkbSSbdhRES1x%2Fnq9U%2F%2BEkGpBA6R23UMauYnoc0mZaMkQZi4vGAwRaK0sV0lCW76dFci6M050b9uC7eVL5N6XwKfKhVyZcemTTe3T9xgLO0OHeK3w7s1KRicnspDNJJd2HhNcvJHGFbAQj1SA7ReD7oIGyWulmKC0u88e7WM%2BuUkvCNk3XNRrIcHaHV2xZr8VT8TfMd1Q%2BXMK2oxk18W%2F%2B53L1hSEvqtqTlUql9v0eUHQXVjUA4GCMF2dJmCFkcG0vF%2BiZ0MWx9b9uB%2BG11mi6kbpFPy7WqZhMOStp8sGOqUBy%2BKa%2F7rQtNb6HLYo25h5TkLMLzo45XvUVYbPRkTGl84YephWtM2k4i4f6fuzeWF%2FkVtAG%2BG3Jxr6eSc6h3AHsRKic%2FeLVgkupi7yiP09tNJQTGBDhSkaL4K9TmJX5%2B1FfgmfJWVchYAHo5dG8PnRD9OvAA7ARwgWtdoBuaaIYztZ4Rs6WicO3CyUjM0nwes8a1n6tH5i8avcNQZSmwn4IPrqpgow&X-Amz-Signature=40ac07e44d28df6d983bc3c511303f52b5a6f62fcf72c933530cf5a4e2637757&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







