



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGX46KNX%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T180943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQC41xhmLP2tXqQoqEIK0sLwpgq%2BDECsIqWuAGIS7sV5eAIgGqgPWfFG9eLzcjYsIc5%2FsGuFnFq4%2BluQZKgchqbccuIqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtt%2FTZq2oUNY5uC5SrcA64FRKmSSzpQRu%2FKrY9coCp8T3QQYv0NJy7udjCD3BSczCfHsF1%2FWjECTyL3EjG0x2ahwRLtoelW2F8DjjePcv2fO%2FZCHY1msRcnQjrLFZbgN3fH7bCUCNARDFhBBztOxn9ZKwsgt7GE59jz7xCp9ewv0HM0%2F1zKEGe%2BVzr289s%2B8h%2F7KXqWCmY83HrRsiVksRM5FSSXARJOgIXTQDLC0e5%2FF2SMUkXPeU5FafZGYTeMGyGZCAlJN5nOtEX8GeLGtTkwFXyQqfC0D29Tb2KqdeyIcT9ESkoLWm0woNLvtYUX4859b9T1ShFpM52urm1CdsI6xOHQYJyD%2FoI2kOzP1d0mjnMnpUa9X6Wpda1OaQiH4LHEqzli5vP3N2Yq2hECcJmTZCB3D9lacjWL7OqHWj5nOB%2Frf8n%2FDYaqj1mo%2Bvit%2FXbfLG4OIoh1kU5BeXsIrkPMEg08x3HJ%2B0OgEiFCa4SAtiiVVsLAwH4NX87Lsk8A4QJz%2FB0Fs8nbQu4YB1zw0Tasy7d9UpURHbGfQ%2FX7iPRqRlcUZWlqanz4%2BUpFoKCS8vpu2oQvsKiV0tO2sjqL3b%2BIxmHw%2BVRZIl%2F%2FwXUF4jflEop4Oohq8aeatWz8CpsjKHQ7on86ZZZnZvIbMMCUxNYGOqUBZz6xlp9C2xCCpKIw%2Fhsyjw477u9eM6ZvxhNaAUZUVFWtk0rWpMBz1fL3w0uNs4ypcYVKEcs%2Bx4kmqUZGa%2BdFEgNbEpNiWBt%2FYSkOYZQZ8lM%2B2%2BkbadjN6DYeHXkSklsWLDleeBVrYXWrhdstwSlki7AoZlJNtQLTDz%2BLcszHjyNRID%2B8uhF%2Fr474pXDl52LIuH5sjNCou1Vbh%2BdemyWBybC8syu7&X-Amz-Signature=155643b732541739dc5ba19252ca062fbd8baeaa6ecb10f2dcdf12da8ba7a33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGX46KNX%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T180943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQC41xhmLP2tXqQoqEIK0sLwpgq%2BDECsIqWuAGIS7sV5eAIgGqgPWfFG9eLzcjYsIc5%2FsGuFnFq4%2BluQZKgchqbccuIqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtt%2FTZq2oUNY5uC5SrcA64FRKmSSzpQRu%2FKrY9coCp8T3QQYv0NJy7udjCD3BSczCfHsF1%2FWjECTyL3EjG0x2ahwRLtoelW2F8DjjePcv2fO%2FZCHY1msRcnQjrLFZbgN3fH7bCUCNARDFhBBztOxn9ZKwsgt7GE59jz7xCp9ewv0HM0%2F1zKEGe%2BVzr289s%2B8h%2F7KXqWCmY83HrRsiVksRM5FSSXARJOgIXTQDLC0e5%2FF2SMUkXPeU5FafZGYTeMGyGZCAlJN5nOtEX8GeLGtTkwFXyQqfC0D29Tb2KqdeyIcT9ESkoLWm0woNLvtYUX4859b9T1ShFpM52urm1CdsI6xOHQYJyD%2FoI2kOzP1d0mjnMnpUa9X6Wpda1OaQiH4LHEqzli5vP3N2Yq2hECcJmTZCB3D9lacjWL7OqHWj5nOB%2Frf8n%2FDYaqj1mo%2Bvit%2FXbfLG4OIoh1kU5BeXsIrkPMEg08x3HJ%2B0OgEiFCa4SAtiiVVsLAwH4NX87Lsk8A4QJz%2FB0Fs8nbQu4YB1zw0Tasy7d9UpURHbGfQ%2FX7iPRqRlcUZWlqanz4%2BUpFoKCS8vpu2oQvsKiV0tO2sjqL3b%2BIxmHw%2BVRZIl%2F%2FwXUF4jflEop4Oohq8aeatWz8CpsjKHQ7on86ZZZnZvIbMMCUxNYGOqUBZz6xlp9C2xCCpKIw%2Fhsyjw477u9eM6ZvxhNaAUZUVFWtk0rWpMBz1fL3w0uNs4ypcYVKEcs%2Bx4kmqUZGa%2BdFEgNbEpNiWBt%2FYSkOYZQZ8lM%2B2%2BkbadjN6DYeHXkSklsWLDleeBVrYXWrhdstwSlki7AoZlJNtQLTDz%2BLcszHjyNRID%2B8uhF%2Fr474pXDl52LIuH5sjNCou1Vbh%2BdemyWBybC8syu7&X-Amz-Signature=8de03744b3e76936f6a29d673a7773591fa631f5cf78b74d510502e9e4c11cf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







