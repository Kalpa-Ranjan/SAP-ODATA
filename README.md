



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TOO22JO%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T182420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCScpY25tE0eGnfqYcz%2FTo5I0w7qJ3XdOrVXlvuSwtvowIhAMKZIvJFmdVMsR5oVBBD6TUDX18kas2DLHUpB6uFqNtEKv8DCHQQABoMNjM3NDIzMTgzODA1Igwf7rsWuF3OWaHODvsq3AMTpjxURb5lT9BX7otJje%2BSlO0Kp9fWn0d5cUuDo9jfvQQCKf2cumhxFDpdDWGbsbwr2GD4E4G%2FxrD65MKQZESCRvZD%2BY2%2F0vKHt9yaqxYKodMMys4WWJOn0bQJbg33ZjmHvQ0CrymCaUITMpfIeWSPxRURO9KNnu6AcffCBmSRDM3LG5eeXcLPSaB7XbPPDpUSC8KpxgLOFMb47rqkfD8DWCdK6xJcQVTUgP%2BEK8p4ldAd1lvie57d%2B5%2Fo2Z%2BdIfT%2BR6jaugGTpIG4o%2FHIzLVlwZFiIpRn0qpLASQwOOMkVxuf879Y%2B1bDXPx85lPccLZ98HW4KEyJwZ1PSGlzqImC9ueV%2BBehLxxSdKJye2U7MlNGjqgpl9NtOhAAWI1FrXFmzXRFMyBQC9l0T7gT%2Fsm6Zr44JJyl7fd4nB7sOuee4sMwZ%2BDSn%2BjIvTb2anHaOcv%2FlODRa4IgG70nYKm7FoFOFXfATZ5GVIksb47VeUpp7BTLxYXJMPDcScoi1QtETHerRUixsL2OJ7NnR%2BVvDyRSusUxWPl11kEM4Tqjzu1GrVqwJzmXreHJtteiusZxD6k4g0hNzVY2%2Fsn8e0NggqTbxMZ%2BNQz%2FKYKe%2BsP0c66x1rX509GaZZ%2B6r3xPAjDh55fJBjqkAZsAkco%2BO%2FkubiwqZHy9%2Bu1HFzXnV1lhIaBQ0klLBaXEBJvgpaaFg1RlJVWMlLJ1bJ9X5ntDvGKiJh1g2%2FgMCpW2uWelBb6bhYb51VxNqknoK1Xi6jHRSm0KdRq6hLhjpuM7JFmCFzgajV0hSDIn9BuTSF9mIet1zZmc8YC%2BcEr6YTDg6sAECd6s1WLGbMF5m1HLbQdjvl8Z9xGfIRHoSEJroPXd&X-Amz-Signature=3f799123d6deade1987b142e6c5014580959b7987550be27214457aeb13e3a71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TOO22JO%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T182420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCScpY25tE0eGnfqYcz%2FTo5I0w7qJ3XdOrVXlvuSwtvowIhAMKZIvJFmdVMsR5oVBBD6TUDX18kas2DLHUpB6uFqNtEKv8DCHQQABoMNjM3NDIzMTgzODA1Igwf7rsWuF3OWaHODvsq3AMTpjxURb5lT9BX7otJje%2BSlO0Kp9fWn0d5cUuDo9jfvQQCKf2cumhxFDpdDWGbsbwr2GD4E4G%2FxrD65MKQZESCRvZD%2BY2%2F0vKHt9yaqxYKodMMys4WWJOn0bQJbg33ZjmHvQ0CrymCaUITMpfIeWSPxRURO9KNnu6AcffCBmSRDM3LG5eeXcLPSaB7XbPPDpUSC8KpxgLOFMb47rqkfD8DWCdK6xJcQVTUgP%2BEK8p4ldAd1lvie57d%2B5%2Fo2Z%2BdIfT%2BR6jaugGTpIG4o%2FHIzLVlwZFiIpRn0qpLASQwOOMkVxuf879Y%2B1bDXPx85lPccLZ98HW4KEyJwZ1PSGlzqImC9ueV%2BBehLxxSdKJye2U7MlNGjqgpl9NtOhAAWI1FrXFmzXRFMyBQC9l0T7gT%2Fsm6Zr44JJyl7fd4nB7sOuee4sMwZ%2BDSn%2BjIvTb2anHaOcv%2FlODRa4IgG70nYKm7FoFOFXfATZ5GVIksb47VeUpp7BTLxYXJMPDcScoi1QtETHerRUixsL2OJ7NnR%2BVvDyRSusUxWPl11kEM4Tqjzu1GrVqwJzmXreHJtteiusZxD6k4g0hNzVY2%2Fsn8e0NggqTbxMZ%2BNQz%2FKYKe%2BsP0c66x1rX509GaZZ%2B6r3xPAjDh55fJBjqkAZsAkco%2BO%2FkubiwqZHy9%2Bu1HFzXnV1lhIaBQ0klLBaXEBJvgpaaFg1RlJVWMlLJ1bJ9X5ntDvGKiJh1g2%2FgMCpW2uWelBb6bhYb51VxNqknoK1Xi6jHRSm0KdRq6hLhjpuM7JFmCFzgajV0hSDIn9BuTSF9mIet1zZmc8YC%2BcEr6YTDg6sAECd6s1WLGbMF5m1HLbQdjvl8Z9xGfIRHoSEJroPXd&X-Amz-Signature=72cb6be89f03aaee761bce10c95478b785a94c4977175b9a5c53d6aa9db5ab5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







