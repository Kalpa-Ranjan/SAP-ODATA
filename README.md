



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPFEEFPU%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T125358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDsjyhHCMRIF%2BIcp%2FhxTZefeG4VKVrEFId8OgIpP2wy2QIgCAZUT8%2BWTs8AylGcgvv2jiEPq9p5muvjhI6IHFFF9QgqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2BAisDDUhMoyO%2BXDSrcA55Uw%2F75dXXNuaPiqa%2FS%2F%2BIKHrgk7XGp2hlguRtaa8%2BcuP%2BjruIq2sniz52RVmrXcBTxbysAdT4GGhQScmr3xvCVBcnnYhhHJBkiPwfT5pBbqa2YtTPKiCyzareFOCKdig54sI31FgXm7rKgPyAnyCUUcTfh1BjO%2FaJz6sOSp2WuUD2IaJawYZDpP3DYfr%2FN4%2F6XNhRHyYSYJb91Q1ikMCERuuU1oZBUe8onKwCnoQdEUi6cPHOFyPrCFDC%2BGwB68nLRIHHpAP63tkgj8N4ZRnw%2FhRWMa5IIpe4QdeK9Jv%2FE0mGsmgKqmA5uXStZarteCqESaJOV3amhtJbAhs6b%2BKBwEnUjNYif%2FYVaWI%2Femdnp77H92x8rC0eOSYdJhP4%2BtxOHzHZwhTT5DCGD%2BStQ6raAO6lEe8aYpf4Jei1c7ulbkceIt0TvAWeXnnW5BV3SjyhZM9v4T4vr%2FUDj6J5s08qOwm8F2DVfToHwentRuDtt2nTcTuZ%2BMjzRTad71pk%2FqYvmHbS5SSv0eihMk3IFJ8X6kkSHiN1rGz2Oa7UmIPS7BWaJro3WfHctA6axDBVYFVPtyHDwaKNN5tIpq%2Fhm0iQy3P3E6wftqEHmLVZLFB1Mti%2FLZfZnLi55HXaBMIL%2B8MwGOqUBbDLHeIyh9iZvt6aHlXrw61jA8OyRVakiv0MJTAJcVc%2BI%2BNKmeaMaEDOmI5H8bGpzaZ89nEQfj1QUyZuTOCPGZvHBM02QM5En7v3StGH9gLlWPXi%2FohgNE6cg2hIZQvTD8cwA2T7Rnif5MA6%2F4M3zIdmhjgeAn8G0nXCH1ZSMvGmyAXU6eHJoVHQ5F1dKyxpcGSv2MF56XJIpaqr7HKGnmJj1SeHe&X-Amz-Signature=af1ff5eb241c99203c52e894fa265d86b0298960a9b7a48619938cb83fccb1a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPFEEFPU%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T125359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQDsjyhHCMRIF%2BIcp%2FhxTZefeG4VKVrEFId8OgIpP2wy2QIgCAZUT8%2BWTs8AylGcgvv2jiEPq9p5muvjhI6IHFFF9QgqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2BAisDDUhMoyO%2BXDSrcA55Uw%2F75dXXNuaPiqa%2FS%2F%2BIKHrgk7XGp2hlguRtaa8%2BcuP%2BjruIq2sniz52RVmrXcBTxbysAdT4GGhQScmr3xvCVBcnnYhhHJBkiPwfT5pBbqa2YtTPKiCyzareFOCKdig54sI31FgXm7rKgPyAnyCUUcTfh1BjO%2FaJz6sOSp2WuUD2IaJawYZDpP3DYfr%2FN4%2F6XNhRHyYSYJb91Q1ikMCERuuU1oZBUe8onKwCnoQdEUi6cPHOFyPrCFDC%2BGwB68nLRIHHpAP63tkgj8N4ZRnw%2FhRWMa5IIpe4QdeK9Jv%2FE0mGsmgKqmA5uXStZarteCqESaJOV3amhtJbAhs6b%2BKBwEnUjNYif%2FYVaWI%2Femdnp77H92x8rC0eOSYdJhP4%2BtxOHzHZwhTT5DCGD%2BStQ6raAO6lEe8aYpf4Jei1c7ulbkceIt0TvAWeXnnW5BV3SjyhZM9v4T4vr%2FUDj6J5s08qOwm8F2DVfToHwentRuDtt2nTcTuZ%2BMjzRTad71pk%2FqYvmHbS5SSv0eihMk3IFJ8X6kkSHiN1rGz2Oa7UmIPS7BWaJro3WfHctA6axDBVYFVPtyHDwaKNN5tIpq%2Fhm0iQy3P3E6wftqEHmLVZLFB1Mti%2FLZfZnLi55HXaBMIL%2B8MwGOqUBbDLHeIyh9iZvt6aHlXrw61jA8OyRVakiv0MJTAJcVc%2BI%2BNKmeaMaEDOmI5H8bGpzaZ89nEQfj1QUyZuTOCPGZvHBM02QM5En7v3StGH9gLlWPXi%2FohgNE6cg2hIZQvTD8cwA2T7Rnif5MA6%2F4M3zIdmhjgeAn8G0nXCH1ZSMvGmyAXU6eHJoVHQ5F1dKyxpcGSv2MF56XJIpaqr7HKGnmJj1SeHe&X-Amz-Signature=e83729ca3504831c7d7575efc1bfc34226a365f3185ac3c7211b6526167b9fd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







