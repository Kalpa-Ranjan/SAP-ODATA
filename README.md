



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEGJ52AU%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T002300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5T5ZiXajSEWWBr3JhJck6W9aVGgQ5R44D14hlpbA2XQIhAMBVcrfR9oNg4efXH%2BpSlPDd7vrpjq3cbXr09eMOnC%2BlKv8DCGQQABoMNjM3NDIzMTgzODA1IgyUyKbPFzhiezAbp8sq3AMIDLO%2B3pzhfzEN9aGt6TBRabnhwayAKM0LBhHiOtVbKFVz1ziusmDQTz6y59no6f0XvD4Bx7GYItNchszedSu%2Baxc2flaBbc6DGhQnn8cEljVTw4H%2F99QromyRq8IZUG5IDCE6saSbyxImB9Qp7q1Hn9erDG1lX5EuZ%2BDIGs5IB9xwBomuTNuYORGxNRppabaXpUe6DnOtuiKW6PZI1kG4nl2BbWMMEqJkXfyxtC7JroevMHtBL6Vtlnh5EameB34E2LPNPxt%2Fn65rRiYdFshf9KnDK9P0U3XaaySpxqwgEx2qrAfVKBxzj5f3xT%2FDBjClxy8kMMudhB3xN10jTd0u%2BHBx4j4j10T3BuYZL3%2BxV3euGwE47IN2cGtYHoHYr2eB7pMp0PQzXdJZNjPROhXZdfM%2Bv2OEq%2F4SzDFmYW5DXCCvzGW4yb5rQGd1pybZw4FgqSq0pIodAa71jFIuLbGX7qvPnAdhcKBhaJLC%2F7rgg4fvslWyhhzYJeU7wjbQCo4ecQs5%2FTmNV7p7tRt3seat6TEA7lbCMe5JoOWi1RC0sdMjPek4xkjhKgYpnhMDDYaVivYd1%2B6FuGY56waH4UpRGXdGiYoHdek3288a0dF7fjc%2FI27I%2BGsINmWy3zCKtLvVBjqkAXlU0OIvHVv3PmYGw5JFLQIK3R%2BK%2FdPXUCtJB%2Fpd1fKTJusyoC5voctW7HtA4gEVOJEIpe2hjY55xG20lN5eMRf6aL281M3XABX3V0dgltYO2JPYhoz5QiQFLD1CwJqKc%2FaC%2BoIheRr5MBxPSnZhT41nUFeGL1QJLMfdnxUwpEyOXnIxFR7Q6IxgYxpgJOineVALWmmxklLfZL%2Fm7JHvp%2BEvgT6v&X-Amz-Signature=0d94665ba48674239c02355039af47c7fb7f2db25853a3853455892fdb8fe750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEGJ52AU%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T002300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5T5ZiXajSEWWBr3JhJck6W9aVGgQ5R44D14hlpbA2XQIhAMBVcrfR9oNg4efXH%2BpSlPDd7vrpjq3cbXr09eMOnC%2BlKv8DCGQQABoMNjM3NDIzMTgzODA1IgyUyKbPFzhiezAbp8sq3AMIDLO%2B3pzhfzEN9aGt6TBRabnhwayAKM0LBhHiOtVbKFVz1ziusmDQTz6y59no6f0XvD4Bx7GYItNchszedSu%2Baxc2flaBbc6DGhQnn8cEljVTw4H%2F99QromyRq8IZUG5IDCE6saSbyxImB9Qp7q1Hn9erDG1lX5EuZ%2BDIGs5IB9xwBomuTNuYORGxNRppabaXpUe6DnOtuiKW6PZI1kG4nl2BbWMMEqJkXfyxtC7JroevMHtBL6Vtlnh5EameB34E2LPNPxt%2Fn65rRiYdFshf9KnDK9P0U3XaaySpxqwgEx2qrAfVKBxzj5f3xT%2FDBjClxy8kMMudhB3xN10jTd0u%2BHBx4j4j10T3BuYZL3%2BxV3euGwE47IN2cGtYHoHYr2eB7pMp0PQzXdJZNjPROhXZdfM%2Bv2OEq%2F4SzDFmYW5DXCCvzGW4yb5rQGd1pybZw4FgqSq0pIodAa71jFIuLbGX7qvPnAdhcKBhaJLC%2F7rgg4fvslWyhhzYJeU7wjbQCo4ecQs5%2FTmNV7p7tRt3seat6TEA7lbCMe5JoOWi1RC0sdMjPek4xkjhKgYpnhMDDYaVivYd1%2B6FuGY56waH4UpRGXdGiYoHdek3288a0dF7fjc%2FI27I%2BGsINmWy3zCKtLvVBjqkAXlU0OIvHVv3PmYGw5JFLQIK3R%2BK%2FdPXUCtJB%2Fpd1fKTJusyoC5voctW7HtA4gEVOJEIpe2hjY55xG20lN5eMRf6aL281M3XABX3V0dgltYO2JPYhoz5QiQFLD1CwJqKc%2FaC%2BoIheRr5MBxPSnZhT41nUFeGL1QJLMfdnxUwpEyOXnIxFR7Q6IxgYxpgJOineVALWmmxklLfZL%2Fm7JHvp%2BEvgT6v&X-Amz-Signature=eabede2c6885b96f2bb2f290e8b18a52ec05309cbfc11ad870da49cba1f9129b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







