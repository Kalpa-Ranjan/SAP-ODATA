



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFM2OLIW%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T182604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCCevSrAm58w4B%2B65M2iCC7%2FbRra0DlGQCPsnZJ9b%2B9lQIgEpX%2BPvygtB9Xc67ziQozVe83cb6ODb7WaFsMBYoCZbEq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDPCZdZbZdAw2OYQq1SrcA0LzVPwAPAbQcV%2FQzRBIBl1VV%2B94tXr3fNbpibZtNx3CQXbFWzfN1lEybWElDPCWy0Ac2S4JIUlkZAVeaEXygiqxkffkh8eDVQESD4koFAvG5DdtWzRmsVuokvDp6l0eA2nMAwV%2FlfuBcBker6F6dPnzrbyXSdGNWyNqXuccwxYSdWl1T%2Finzakal4o09XTjNuKHWtsCj9CidEsHxevgHj1YZ1qVAG1fIpxhZYdbIttxjxp6pxrUAzbusNUo%2B7hIzne%2FPXdqgpSb%2B5DMz%2BKc78KwrVkTw%2FFRdgpTBt35S9vL%2B7xsJXCC3VzLTixPDpZbZECxPbvtPLpOLi9ZRff%2FmOsiDG49a8mGbJnJAykAeu1B6vPBVpmAZOO4CnVK7qcnIyzWLKm9m2bwfkgQ9YUSpMDa6W6AfejF1G4KT7A%2BvpSDsDO3025KcRIyuqpjOLPOe8532h%2Bfd1g3Gx352mp%2Bq9x9Pvqde32oxaLDMlrNeCL%2FAK093xNEbOTgmgpt47SKVQ1PlCXxQw44j%2Fka8aGioJHJN1kTtg4fv8vLOYsTYwpSDaKhy%2FzNE7Y4lsRbrujQTZ4fLnBR9%2BiN%2Bi8W9H%2B%2Bbf3cEn7jgdPuKsIglssbf7RIfwXj%2FssP3s4dcmeFMIOWmssGOqUBj6DjtbNHUSwh14RJmu7k3%2FEdKLM8KkRZ8dGkqNlv5MqhQAsDYP%2F3zhVqsYUbym7TtxMY6iaoSfH040kvPWM1yT9%2FzwwdciIXrpC7N0hRhH9i9MweL9s436SP%2BIGdHfk1A6HnAc5PchoosXUpP2ttxBT5nmNbTKWORoonjaFoCYPMjDUlrH2VIWrBfnWnQXJW%2B1nM0%2BoBkS3a9PTm8PhNO%2F5ajojg&X-Amz-Signature=83d1dbe148a0ff3ac47e18c081701b4051bab9d10c23de8d1b453047fd742ae1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFM2OLIW%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T182605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCCevSrAm58w4B%2B65M2iCC7%2FbRra0DlGQCPsnZJ9b%2B9lQIgEpX%2BPvygtB9Xc67ziQozVe83cb6ODb7WaFsMBYoCZbEq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDPCZdZbZdAw2OYQq1SrcA0LzVPwAPAbQcV%2FQzRBIBl1VV%2B94tXr3fNbpibZtNx3CQXbFWzfN1lEybWElDPCWy0Ac2S4JIUlkZAVeaEXygiqxkffkh8eDVQESD4koFAvG5DdtWzRmsVuokvDp6l0eA2nMAwV%2FlfuBcBker6F6dPnzrbyXSdGNWyNqXuccwxYSdWl1T%2Finzakal4o09XTjNuKHWtsCj9CidEsHxevgHj1YZ1qVAG1fIpxhZYdbIttxjxp6pxrUAzbusNUo%2B7hIzne%2FPXdqgpSb%2B5DMz%2BKc78KwrVkTw%2FFRdgpTBt35S9vL%2B7xsJXCC3VzLTixPDpZbZECxPbvtPLpOLi9ZRff%2FmOsiDG49a8mGbJnJAykAeu1B6vPBVpmAZOO4CnVK7qcnIyzWLKm9m2bwfkgQ9YUSpMDa6W6AfejF1G4KT7A%2BvpSDsDO3025KcRIyuqpjOLPOe8532h%2Bfd1g3Gx352mp%2Bq9x9Pvqde32oxaLDMlrNeCL%2FAK093xNEbOTgmgpt47SKVQ1PlCXxQw44j%2Fka8aGioJHJN1kTtg4fv8vLOYsTYwpSDaKhy%2FzNE7Y4lsRbrujQTZ4fLnBR9%2BiN%2Bi8W9H%2B%2Bbf3cEn7jgdPuKsIglssbf7RIfwXj%2FssP3s4dcmeFMIOWmssGOqUBj6DjtbNHUSwh14RJmu7k3%2FEdKLM8KkRZ8dGkqNlv5MqhQAsDYP%2F3zhVqsYUbym7TtxMY6iaoSfH040kvPWM1yT9%2FzwwdciIXrpC7N0hRhH9i9MweL9s436SP%2BIGdHfk1A6HnAc5PchoosXUpP2ttxBT5nmNbTKWORoonjaFoCYPMjDUlrH2VIWrBfnWnQXJW%2B1nM0%2BoBkS3a9PTm8PhNO%2F5ajojg&X-Amz-Signature=0979ccccee0a75f8435ed33e6f33c8cc31fd7d07b06dd144ca6a69072e196727&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







