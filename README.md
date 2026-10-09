



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VKGD6I%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T121134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCYFpeRkE2PRo5Kw54LVuyS8KmqVkdUCMrmuELmVjyL3wIgW1sP26W%2BR0JvQs9Uae7yHjpSF5UV6y5QRey5ZHzCar4q%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDBZh36byHx7dAFyC7CrcA83MLQfHC3VjdbfbrkbXY%2F3vrYRRxIt0R91H3trsPLAtODIlFwk%2FBSWCbvHZnYhF2cxyNLuo%2FLrmAS3EjfsvjJvUnecI1uzyvVubZW38DW5T6aYNdJlQuHNhEBlno88XJDAd1VnOCtUDTAyE3WxktLxcbomG9ofLnSlt7%2B2rxGob4vCQA7nl7%2F7bdASkco2FwWFR6rvyoM2xzsAcSluS7spoCH5vArJvABj5ayKoyd6UfnISQ%2FF7MyGaruubSAHKO6V3daw0VVmv%2F%2Bz6TC9smScviTDiuViJZzDx23m7NVnx5BPslC4w5%2BwL2w69lCtuNWSQ4QnefAiPlcjKu7z%2BphzkrRytufslhbv47GxuJM7htNjWDtqGX9wooLkYqtpMPnbie%2B%2BWE%2BKnD0%2FOaiWHi5V6bDMNkEPGDJUgHBXnCGdfJSCLIDbqUPARKsFr4LBfj35OUu%2Fs74KFEOKyn%2B6Ey1SAUPxNm0jGRx%2FC%2Bbd%2Br5HO7qe%2BCgNDxXcDLJhqyhtC0EDDmja7kc8315tf2GbTcENrhGA%2FEcKoyObkaMYgw4ENl2BQh8gp0KbgHVv39zoLG0RBMzGKwGdHwbIHFFibxDbFgNhrqO1ynxIx0lb7r8XA0mY54EW%2FAt70y2X6MK6Do9YGOqUBJ%2BG3jIZ9PS%2BMGN%2FmMnarVeTDrIq3InCy4KMfwq5ixIFZoOaf20fZgs4w714lt3YKfifyLttKgDGXJenH%2BqxcjtPrXq3DxNrYao2tcOIB%2Fi4US45Zxnz7W1dcw%2F79G%2BJw2cUzFw3oAFjDM7bff1nziyS0u5qDIzaIuu0B5O8rzBdj3PnGEby78Px01vabyJP3%2FnKORAcRrE4X4JnF6AdnP8wCv5P1&X-Amz-Signature=0b53f0ab15afb3bc0171127e6b4234b52a019b5632dbba5c804134c86309cd9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VKGD6I%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T121134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCYFpeRkE2PRo5Kw54LVuyS8KmqVkdUCMrmuELmVjyL3wIgW1sP26W%2BR0JvQs9Uae7yHjpSF5UV6y5QRey5ZHzCar4q%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDBZh36byHx7dAFyC7CrcA83MLQfHC3VjdbfbrkbXY%2F3vrYRRxIt0R91H3trsPLAtODIlFwk%2FBSWCbvHZnYhF2cxyNLuo%2FLrmAS3EjfsvjJvUnecI1uzyvVubZW38DW5T6aYNdJlQuHNhEBlno88XJDAd1VnOCtUDTAyE3WxktLxcbomG9ofLnSlt7%2B2rxGob4vCQA7nl7%2F7bdASkco2FwWFR6rvyoM2xzsAcSluS7spoCH5vArJvABj5ayKoyd6UfnISQ%2FF7MyGaruubSAHKO6V3daw0VVmv%2F%2Bz6TC9smScviTDiuViJZzDx23m7NVnx5BPslC4w5%2BwL2w69lCtuNWSQ4QnefAiPlcjKu7z%2BphzkrRytufslhbv47GxuJM7htNjWDtqGX9wooLkYqtpMPnbie%2B%2BWE%2BKnD0%2FOaiWHi5V6bDMNkEPGDJUgHBXnCGdfJSCLIDbqUPARKsFr4LBfj35OUu%2Fs74KFEOKyn%2B6Ey1SAUPxNm0jGRx%2FC%2Bbd%2Br5HO7qe%2BCgNDxXcDLJhqyhtC0EDDmja7kc8315tf2GbTcENrhGA%2FEcKoyObkaMYgw4ENl2BQh8gp0KbgHVv39zoLG0RBMzGKwGdHwbIHFFibxDbFgNhrqO1ynxIx0lb7r8XA0mY54EW%2FAt70y2X6MK6Do9YGOqUBJ%2BG3jIZ9PS%2BMGN%2FmMnarVeTDrIq3InCy4KMfwq5ixIFZoOaf20fZgs4w714lt3YKfifyLttKgDGXJenH%2BqxcjtPrXq3DxNrYao2tcOIB%2Fi4US45Zxnz7W1dcw%2F79G%2BJw2cUzFw3oAFjDM7bff1nziyS0u5qDIzaIuu0B5O8rzBdj3PnGEby78Px01vabyJP3%2FnKORAcRrE4X4JnF6AdnP8wCv5P1&X-Amz-Signature=a69d60227329549f33922967f01879a34b751b45aa9327eea4936586462ca9e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







