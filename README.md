



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5L7F4BI%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T182226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCOr1ib4bihrWfLziVDPTNtewzIxwsnXJZ3CzH2f%2FbIOAIgamtr6Vc6NEodM1eMO1fWAvUMmpkUVhIFkiGkqG9%2FDm4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDPurz9RF9SJ6TUNyJSrcA52ekCcwjsLW2wx44WV16q14UU%2Bw%2Fe672KgO%2Ft11p2WK5sb1S7bPtdarlh4pKTSmj%2B9kIL4IhSIeO1%2FrZVp5eMyiwu4Mvk%2BiKurPVXOKTBsF41LZJjzj5xGfacq5rNCpcVLMZTAnzclpoG8t9F1jeFhrlruAfrjZOyH0x1B%2B2OYfcytG7r4Ve3kA9KRzfffiYUI31H5RNem6mDCbwlWqTRH%2BBmplidVCIQ0ImUkScFh1Hpc2Sah3YNy1wHRPCB%2BAiMDlEzFe4I%2FT8xEp9VN8BbeI87fUgOfg9ZBLuSdoF3obOrkyXHhOAy0nXPHHHRjkBIR6Zm9lGp8B%2F9rd4X4%2BaxjuVNCPTVDbZbm2UOTAdPEmrMiYZYuYZXEMowJcqdxnqX39u%2BlgROqz2Ysys%2FYSPVM2bepl99uhNGLbAcej8aHCnNIS2Y9FL1PI34T%2FS1JWG5QLXlBZbEtFBLIpc1EWi7Zej%2BYeJCNdAfuX2%2FRoVbyylXL3md8MXfgsK8xO%2BvDXH5wSgkblsSiyP%2BKEyIGBQkmCsaFgGCMNGCPNRogvOzCEm13QLwejy3LN0Z7wDdVi27pg%2FVi0bBcpGJZmTUq2RnWQSDxzQ9DvJPa7wpIn%2B%2FbdtSxq7LWrW2UhRJFkMJX1k8gGOqUBAzAFjuqH%2B1TipiOcGgzfWnGXqN0sgzdsTUKcRP0%2BH%2FcfGvIzY6XGeSlwf0G1ZMpFW%2BjhdqP2bH2hqx6HSzvnDpim%2FIt1GcC%2FfFQDfhljARw%2Fin6DojlqlGFKUD9eNn1Ir6Pre1onKerMMCzM7KRvZX%2BQ9pkpN6xLPAp3dtD%2FvsNcxIW%2FYIHMGA2Ua6tc0KeNpwYJJOFUL7Gc8jnDaoC%2FR9F3H1Op&X-Amz-Signature=791b2ca04e46f02862d40a1c0fc5b6c0d13457ded94dadbfbdb164d3070fe01a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5L7F4BI%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T182226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCOr1ib4bihrWfLziVDPTNtewzIxwsnXJZ3CzH2f%2FbIOAIgamtr6Vc6NEodM1eMO1fWAvUMmpkUVhIFkiGkqG9%2FDm4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDPurz9RF9SJ6TUNyJSrcA52ekCcwjsLW2wx44WV16q14UU%2Bw%2Fe672KgO%2Ft11p2WK5sb1S7bPtdarlh4pKTSmj%2B9kIL4IhSIeO1%2FrZVp5eMyiwu4Mvk%2BiKurPVXOKTBsF41LZJjzj5xGfacq5rNCpcVLMZTAnzclpoG8t9F1jeFhrlruAfrjZOyH0x1B%2B2OYfcytG7r4Ve3kA9KRzfffiYUI31H5RNem6mDCbwlWqTRH%2BBmplidVCIQ0ImUkScFh1Hpc2Sah3YNy1wHRPCB%2BAiMDlEzFe4I%2FT8xEp9VN8BbeI87fUgOfg9ZBLuSdoF3obOrkyXHhOAy0nXPHHHRjkBIR6Zm9lGp8B%2F9rd4X4%2BaxjuVNCPTVDbZbm2UOTAdPEmrMiYZYuYZXEMowJcqdxnqX39u%2BlgROqz2Ysys%2FYSPVM2bepl99uhNGLbAcej8aHCnNIS2Y9FL1PI34T%2FS1JWG5QLXlBZbEtFBLIpc1EWi7Zej%2BYeJCNdAfuX2%2FRoVbyylXL3md8MXfgsK8xO%2BvDXH5wSgkblsSiyP%2BKEyIGBQkmCsaFgGCMNGCPNRogvOzCEm13QLwejy3LN0Z7wDdVi27pg%2FVi0bBcpGJZmTUq2RnWQSDxzQ9DvJPa7wpIn%2B%2FbdtSxq7LWrW2UhRJFkMJX1k8gGOqUBAzAFjuqH%2B1TipiOcGgzfWnGXqN0sgzdsTUKcRP0%2BH%2FcfGvIzY6XGeSlwf0G1ZMpFW%2BjhdqP2bH2hqx6HSzvnDpim%2FIt1GcC%2FfFQDfhljARw%2Fin6DojlqlGFKUD9eNn1Ir6Pre1onKerMMCzM7KRvZX%2BQ9pkpN6xLPAp3dtD%2FvsNcxIW%2FYIHMGA2Ua6tc0KeNpwYJJOFUL7Gc8jnDaoC%2FR9F3H1Op&X-Amz-Signature=fa8eec8ac10e1c38c09f2106eaa92a181989e38009d33194b2c3108cbac7c39b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







