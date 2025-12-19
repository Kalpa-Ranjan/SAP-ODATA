



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG34JDP4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T123302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE56GdpIUIEoLqVDUBVmmLzakggrVO2KwWI9qZV%2BZIdMAiEA7UsvI7MrpiR2mD3nSWTEN%2BkkHr4AgN4g7TC47ZMOO80qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIULGZoeCdeU0zNySrcA5jp%2F16Kd6lLN0tS9wj8n%2FIOQaoseWSRpoCnkKEeDJfmRd5hu7022pwV0mwnAh8BSz2ncgl9BghXuFy3u7%2Fra60NzpV1iz7w7D2Ctm9lk%2Bg62Oh303VMEba8R0QEVh8hrC61v497bSBBt9naDe%2BeWwQryTfDErxAQqfujYKZ1dXgJUBTK%2BPG5wiBu5BodTr1sfyffPZCr9MqcUaS0wIzR3QtZcL2xQRWC8pzH%2F7EDpQP0LURPrIw6wd6RmnKVgYTVQb9vkayMfSQ140PEBOzv0Vg26Es500%2F2U4RET8uTIudbopGglgjceSx3Qda6O1YhxfRT658VPK1lEIrtlp0YVMEJ7q9sU2GprWZ6IlV2P5G9yrT08zZI8NVtG1bXIhok9qpM9nopVOIL9fJmKKn08XsR3eWOLVEoLuEsVkEeWYDchccxvUdlkkSmW6M4QDoPB9rEWo1OgLcODbLtzHN1CQvkOMIhEjGzKT8jlSG8F2RzjSjcl4bJkkcq3BEAzQCv3DdQkadH7auYQdfMIsG%2BlERDKh36ufqnirKGvHRCvFq0xPaJsHAe7og%2BIM635r1jWHg37Yt31hD6DzMkzk0iKo%2FF2kZN%2Bv2y%2BUBbKZTOL5G3ZtHotuBY%2BWq159mMNOAlcoGOqUBm36VNXiQL906dvD4OSJis3OhPAhuit6MEYX9Y5%2FINVgXiVy7SquxcGkQ0ZwLDD8TZ9aBRebtQYVHVVAFVPK%2BIEcEdUaGDwOWnuigVHenmrMAYgLQ7lJZLACTYbvID2JwyvvF06s%2Fxso9rFAGkodhhJVQG9%2F7UplasrsfA2BfzKfxlUQ%2FX8oM2%2F8NoQzyFYFExqxc%2BwOuzVGs0GmnH4HVYzB0jvVr&X-Amz-Signature=e6ef418f2f9e6654fb37da9487933c5e19388dc6cbbe1f0b56748d5546128f8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG34JDP4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T123302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE56GdpIUIEoLqVDUBVmmLzakggrVO2KwWI9qZV%2BZIdMAiEA7UsvI7MrpiR2mD3nSWTEN%2BkkHr4AgN4g7TC47ZMOO80qiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIULGZoeCdeU0zNySrcA5jp%2F16Kd6lLN0tS9wj8n%2FIOQaoseWSRpoCnkKEeDJfmRd5hu7022pwV0mwnAh8BSz2ncgl9BghXuFy3u7%2Fra60NzpV1iz7w7D2Ctm9lk%2Bg62Oh303VMEba8R0QEVh8hrC61v497bSBBt9naDe%2BeWwQryTfDErxAQqfujYKZ1dXgJUBTK%2BPG5wiBu5BodTr1sfyffPZCr9MqcUaS0wIzR3QtZcL2xQRWC8pzH%2F7EDpQP0LURPrIw6wd6RmnKVgYTVQb9vkayMfSQ140PEBOzv0Vg26Es500%2F2U4RET8uTIudbopGglgjceSx3Qda6O1YhxfRT658VPK1lEIrtlp0YVMEJ7q9sU2GprWZ6IlV2P5G9yrT08zZI8NVtG1bXIhok9qpM9nopVOIL9fJmKKn08XsR3eWOLVEoLuEsVkEeWYDchccxvUdlkkSmW6M4QDoPB9rEWo1OgLcODbLtzHN1CQvkOMIhEjGzKT8jlSG8F2RzjSjcl4bJkkcq3BEAzQCv3DdQkadH7auYQdfMIsG%2BlERDKh36ufqnirKGvHRCvFq0xPaJsHAe7og%2BIM635r1jWHg37Yt31hD6DzMkzk0iKo%2FF2kZN%2Bv2y%2BUBbKZTOL5G3ZtHotuBY%2BWq159mMNOAlcoGOqUBm36VNXiQL906dvD4OSJis3OhPAhuit6MEYX9Y5%2FINVgXiVy7SquxcGkQ0ZwLDD8TZ9aBRebtQYVHVVAFVPK%2BIEcEdUaGDwOWnuigVHenmrMAYgLQ7lJZLACTYbvID2JwyvvF06s%2Fxso9rFAGkodhhJVQG9%2F7UplasrsfA2BfzKfxlUQ%2FX8oM2%2F8NoQzyFYFExqxc%2BwOuzVGs0GmnH4HVYzB0jvVr&X-Amz-Signature=f5c10d902b3cd594dbdcbd25376520e34fdc3bb066b933f4d6cc3b488db163c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







