



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN7G2OE4%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T064449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHIX2qi673gvIVRMGhFS0Yc2tRZuJBUCoh7eXGiDoJDAiEA4nVZAEYhkNj3WyOOkdY%2BMW8K5vRrrXTTbubh%2FeQZq74q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDC1wlIEOhFeOYgB6rircAyOjTG%2F%2BClCeDq5%2FR1Gox6G%2FRw%2F0AelENXHBg01NfRbbROo4DAXSbiohoWSGWb4QYjc1OxFBLU9ao8sAU2Tc%2BVICb5gpO27PQIQtSpaecKSlvghjU5jg4pyd3O3gC20jJLGranuYIaCAMtvq9IxKvGj2MiAj6Ghj0pZZWXxZ%2BWcdz5DVeGK%2BRlcm%2Fy3kpLeh9%2BmJ3iRlcc30G%2FBl7oVcnMZgU03NiuB7Mi4TBns0oDQLzpFI6Fq%2BdGS67FKko0lFomDWiIv7Z8782nKA6O%2FbwKMFUMC5t5YJAhx4p5%2Bdnn3pRyKeRALK16rgnXVMb94NLjlxoMM%2FFEG4AE9RSsI0D%2BsMvSvwWE55Cd60yX0ZhCDEtntHs0fuVCv814cAHD0eJki%2B1TtmIykXY%2BZ5JiWufBcckqyDN2w3Cts3iiqyxr3R%2FNdd8whhHXQbzlCZh5Eel1UwjXkMfG2Xufs1rMceux3o9SOn%2BQTX0MEGBXByJnBXLG1aOh2CF187y1T5DS94z29xerMdqJFrXxQUkNkGOGAxPwiOnaALdMVTgS4iIGnjt83cUQXdzR8sKFs49onrLcA4CR0ZJ0cS%2FaPQ7kMpjcdYkqoTdMQINMZOtplwos0dMEv8YzlPqPzRSXYsMMaLxM0GOqUBLoJdPXjxaWEmfbhT8htkAfzX%2BXA7Pkqp2SzHf65RoOIRyS%2BJoxEtsVAhA%2FeZdbmW2pJlMB1cIgX2a%2FG6eqF06Nmg6F9iULNtbtLX75ncaFXKJvwiLQdNQnEgJB12yD0CwN9%2FUzJR03xcfXqz7KiQ2%2FedpSSgCa3mvch5vvii0Rs2Mdgy9Towyg1qoxOxkr4LVUiBFdmtlhFr5qAdGShfBzZ1%2BssP&X-Amz-Signature=c0e114cd230c7023e26c5012a0d4f927883b915449d990699dd084a562c345bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN7G2OE4%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T064449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHIX2qi673gvIVRMGhFS0Yc2tRZuJBUCoh7eXGiDoJDAiEA4nVZAEYhkNj3WyOOkdY%2BMW8K5vRrrXTTbubh%2FeQZq74q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDC1wlIEOhFeOYgB6rircAyOjTG%2F%2BClCeDq5%2FR1Gox6G%2FRw%2F0AelENXHBg01NfRbbROo4DAXSbiohoWSGWb4QYjc1OxFBLU9ao8sAU2Tc%2BVICb5gpO27PQIQtSpaecKSlvghjU5jg4pyd3O3gC20jJLGranuYIaCAMtvq9IxKvGj2MiAj6Ghj0pZZWXxZ%2BWcdz5DVeGK%2BRlcm%2Fy3kpLeh9%2BmJ3iRlcc30G%2FBl7oVcnMZgU03NiuB7Mi4TBns0oDQLzpFI6Fq%2BdGS67FKko0lFomDWiIv7Z8782nKA6O%2FbwKMFUMC5t5YJAhx4p5%2Bdnn3pRyKeRALK16rgnXVMb94NLjlxoMM%2FFEG4AE9RSsI0D%2BsMvSvwWE55Cd60yX0ZhCDEtntHs0fuVCv814cAHD0eJki%2B1TtmIykXY%2BZ5JiWufBcckqyDN2w3Cts3iiqyxr3R%2FNdd8whhHXQbzlCZh5Eel1UwjXkMfG2Xufs1rMceux3o9SOn%2BQTX0MEGBXByJnBXLG1aOh2CF187y1T5DS94z29xerMdqJFrXxQUkNkGOGAxPwiOnaALdMVTgS4iIGnjt83cUQXdzR8sKFs49onrLcA4CR0ZJ0cS%2FaPQ7kMpjcdYkqoTdMQINMZOtplwos0dMEv8YzlPqPzRSXYsMMaLxM0GOqUBLoJdPXjxaWEmfbhT8htkAfzX%2BXA7Pkqp2SzHf65RoOIRyS%2BJoxEtsVAhA%2FeZdbmW2pJlMB1cIgX2a%2FG6eqF06Nmg6F9iULNtbtLX75ncaFXKJvwiLQdNQnEgJB12yD0CwN9%2FUzJR03xcfXqz7KiQ2%2FedpSSgCa3mvch5vvii0Rs2Mdgy9Towyg1qoxOxkr4LVUiBFdmtlhFr5qAdGShfBzZ1%2BssP&X-Amz-Signature=106e6feb22b279547231d1beb77fd091b9e3cb3b9f7af3456186329f98325347&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







