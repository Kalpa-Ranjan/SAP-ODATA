



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMPDT676%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T062511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDylZlKKPu81gRf2DFaBSpPropg9BSPJpbej4jec0Pp%2FAIgcRXyxS%2F8EOb0ZXaNVOAZq2G21Ae4gjBGnFix7J7yihsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDKvm6NIOI9h2ht6lBSrcA31zo3HhblyhM8%2FaU5A7sDsTPZDlIS8vhwkYYYZMKLinhuubZ2mt%2FOOWOMSbXBNotPAztFhqOV0PDN%2Fp3ez9IPo%2FSja5cNb9OqkZjKFkRhmMr5j%2BX2DBlGIgOOPT%2FFZ5TtkJNmm1Y29mbk0S2%2Faecb4Bte%2FpZlX91EtZ0v94sEYT%2BMxrstRa0SyFHosLGUEsdO%2B22jGbl%2FfNw02msnID200lvpCwbEKy4lccaHkJWV%2FWzWoouh4rL8HQbu5SYkgOLd7mJ6XmDIpY8PDtU%2FM7UhDCTT6T1AiA8zoYisUkaNUScnN8tb2%2Bi9TsSOTNwpg%2BJL5URDUfLS6HafZScH%2B9EwsGfpNGeZBlFsCoAZJdYke1pBgoHqdlx8qtFrpv8Aa7HU8IPK9yYZLqpaJrVFNtIPsyuglSbstYeyeYerD0h19LUtio04qNB1%2BRUUI3yVcZHLIhCpieKrYGmLXMqgG%2Bp55sT%2B2e3KQ2OIIRrK05t6eW6MaYessRKWelp%2FDh2j9oXdhlX9%2B0Jjy%2Fo3Tj3%2BpuUuTjB5NuLKPE1%2F8H%2F9lHvZ%2FiTUgjUGZevcl3bMuku8k5OWizmxMpwCI488RWpVcacjvRucK9fphdN3k0%2FYWo93vgcljgHVl1WNLizJqiMLepmskGOqUBCbWTLmkbhVcoDpJ%2BKEzqOSFgyDnt6rBj4BLtSZZ%2FrRBhYVCLNgXwylscY9mAPY0%2B2%2BaEkUPpPPO5jzXIU22W%2BAUkwI6pr6EQBDtcQwlpYDBZ6lmw7lsZ9TklWA1pVTSfi18%2FJhmjue6fqxnc16xfkep1yFEtIv%2BLdM4082g4gJHh8%2BF0tfa4zKvhcxFBoH7A%2BOaS%2FZUzr%2B7Hcdr0Odg6%2F%2BBoU%2BCf&X-Amz-Signature=5391fdc5f53a549bcb33de25ec313e3d2165a09ff844cd849c50b27b8f8ce503&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMPDT676%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T062511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDylZlKKPu81gRf2DFaBSpPropg9BSPJpbej4jec0Pp%2FAIgcRXyxS%2F8EOb0ZXaNVOAZq2G21Ae4gjBGnFix7J7yihsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDKvm6NIOI9h2ht6lBSrcA31zo3HhblyhM8%2FaU5A7sDsTPZDlIS8vhwkYYYZMKLinhuubZ2mt%2FOOWOMSbXBNotPAztFhqOV0PDN%2Fp3ez9IPo%2FSja5cNb9OqkZjKFkRhmMr5j%2BX2DBlGIgOOPT%2FFZ5TtkJNmm1Y29mbk0S2%2Faecb4Bte%2FpZlX91EtZ0v94sEYT%2BMxrstRa0SyFHosLGUEsdO%2B22jGbl%2FfNw02msnID200lvpCwbEKy4lccaHkJWV%2FWzWoouh4rL8HQbu5SYkgOLd7mJ6XmDIpY8PDtU%2FM7UhDCTT6T1AiA8zoYisUkaNUScnN8tb2%2Bi9TsSOTNwpg%2BJL5URDUfLS6HafZScH%2B9EwsGfpNGeZBlFsCoAZJdYke1pBgoHqdlx8qtFrpv8Aa7HU8IPK9yYZLqpaJrVFNtIPsyuglSbstYeyeYerD0h19LUtio04qNB1%2BRUUI3yVcZHLIhCpieKrYGmLXMqgG%2Bp55sT%2B2e3KQ2OIIRrK05t6eW6MaYessRKWelp%2FDh2j9oXdhlX9%2B0Jjy%2Fo3Tj3%2BpuUuTjB5NuLKPE1%2F8H%2F9lHvZ%2FiTUgjUGZevcl3bMuku8k5OWizmxMpwCI488RWpVcacjvRucK9fphdN3k0%2FYWo93vgcljgHVl1WNLizJqiMLepmskGOqUBCbWTLmkbhVcoDpJ%2BKEzqOSFgyDnt6rBj4BLtSZZ%2FrRBhYVCLNgXwylscY9mAPY0%2B2%2BaEkUPpPPO5jzXIU22W%2BAUkwI6pr6EQBDtcQwlpYDBZ6lmw7lsZ9TklWA1pVTSfi18%2FJhmjue6fqxnc16xfkep1yFEtIv%2BLdM4082g4gJHh8%2BF0tfa4zKvhcxFBoH7A%2BOaS%2FZUzr%2B7Hcdr0Odg6%2F%2BBoU%2BCf&X-Amz-Signature=7a972bcfe664c9c426a1e1fa76acae3c5b281b2ad92e4b748b61c0a3963ebd41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







