



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGNUPPR%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T155422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSCUANYv8n%2BDmVoCIGBw7etKGXu9XsENVGIUF%2BA8jqtwIgEix9awnqZYrEi2aIyhI7fOxLNSmBgPzKPmWuuUWO848q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEhrQ6oJ2nuOQcnuIircA%2FAU%2FNr5G7wChUeEvfI8BWvXXylzVofSQbhsPRm9ueHojHhGrZu1OzYlYsicugavtwTT3raAqKoMLNr02h6Bvxgsp9uxS9OslFOsM4tILzzWiwHfpen%2FSMQENeOwq%2BbT33zT2R9dLEidNfl%2B6%2F2mOpgvf2bFhQCCsa%2FEBITYWajsJ713aZXSOe1CJL7oXF1aF58FfJBjSZyHDU5hRTptYzwIUljsmmpXZqfucnOhLyEBZGNUZesWt%2BrUAnjP36C1WrPhL%2FpxqEt0e80mCo7LcaJZuCsEJv8KCRbmYr8AOD6uZcfNgcjKtHjUFEYjxB2bI6DQY%2F0%2FxNHeH3JAFNAtwIOMGBPmPOlrWG8FD5hWbWqS%2BY1%2BKyMdcKiisfx9qRarInsUPCUTgdPOWseNcQOx4ikK8gV%2B0rG2BfQ1iKZbkb5wlx0LugRos4%2BT0QZNbON5hGCJSlHMPeAw6e%2BkYbG8piH6sSFDnJUOxv5gNCbNpsXoaN%2Ffjaql0%2FFv7stOxETebboWNpA%2FHq9qHnFZ9SA4CCZFiHHldZ%2BSNzwZhiG%2FodyAblMigej7x6UActIiO9aL4boz7VLMA7%2BcvLNSIkFxr6hRQkLlI9%2BZUnaj4cmL1TLdtJxQYviKqjEwp5FdMNfP0NQGOqUBl8dOunAmQhD9K%2ByBFReakSf3LtbkGOn6q0mOUR%2FgY%2Bd0opIvWgubPn5uqspAiTKNWPhXCfYh0HfrfwECH5vKp9AUjECif2PqT%2BonrwnOv1BVFWIU%2B1ZrdiZy28s7VAUtZJ65CVH1OquEs8RLvyOXX%2BM%2FFEbY85QQV79Ms2RdU0H42dWhXiy39IUO6wmHASdiepev6LP%2BS0SrYofhzjoRZTXRDHne&X-Amz-Signature=8d9273a3ccd391cbbc4d86d9b0f6085055d6d1e6160489f1cbff4bbe07937a05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBGNUPPR%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T155422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSCUANYv8n%2BDmVoCIGBw7etKGXu9XsENVGIUF%2BA8jqtwIgEix9awnqZYrEi2aIyhI7fOxLNSmBgPzKPmWuuUWO848q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEhrQ6oJ2nuOQcnuIircA%2FAU%2FNr5G7wChUeEvfI8BWvXXylzVofSQbhsPRm9ueHojHhGrZu1OzYlYsicugavtwTT3raAqKoMLNr02h6Bvxgsp9uxS9OslFOsM4tILzzWiwHfpen%2FSMQENeOwq%2BbT33zT2R9dLEidNfl%2B6%2F2mOpgvf2bFhQCCsa%2FEBITYWajsJ713aZXSOe1CJL7oXF1aF58FfJBjSZyHDU5hRTptYzwIUljsmmpXZqfucnOhLyEBZGNUZesWt%2BrUAnjP36C1WrPhL%2FpxqEt0e80mCo7LcaJZuCsEJv8KCRbmYr8AOD6uZcfNgcjKtHjUFEYjxB2bI6DQY%2F0%2FxNHeH3JAFNAtwIOMGBPmPOlrWG8FD5hWbWqS%2BY1%2BKyMdcKiisfx9qRarInsUPCUTgdPOWseNcQOx4ikK8gV%2B0rG2BfQ1iKZbkb5wlx0LugRos4%2BT0QZNbON5hGCJSlHMPeAw6e%2BkYbG8piH6sSFDnJUOxv5gNCbNpsXoaN%2Ffjaql0%2FFv7stOxETebboWNpA%2FHq9qHnFZ9SA4CCZFiHHldZ%2BSNzwZhiG%2FodyAblMigej7x6UActIiO9aL4boz7VLMA7%2BcvLNSIkFxr6hRQkLlI9%2BZUnaj4cmL1TLdtJxQYviKqjEwp5FdMNfP0NQGOqUBl8dOunAmQhD9K%2ByBFReakSf3LtbkGOn6q0mOUR%2FgY%2Bd0opIvWgubPn5uqspAiTKNWPhXCfYh0HfrfwECH5vKp9AUjECif2PqT%2BonrwnOv1BVFWIU%2B1ZrdiZy28s7VAUtZJ65CVH1OquEs8RLvyOXX%2BM%2FFEbY85QQV79Ms2RdU0H42dWhXiy39IUO6wmHASdiepev6LP%2BS0SrYofhzjoRZTXRDHne&X-Amz-Signature=4b1e69123766b8fd9571bcbffc6adb05202a1ad35c1da96b5d9ada41ac9db3a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







