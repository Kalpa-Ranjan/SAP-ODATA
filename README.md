



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPFDTQ7B%2F20261030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T001538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID42h%2FyAO8h9dh5CIvnGEky%2F6g9X2Tj28H9ha8JEg4FYAiEAyPeMVntgC7Q6HqoGX11xyOD1cLu3eqKpX91XTT6Lop0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOy%2BqlhiLlMTLV3CnCrcA72W1NrexwqSZ4sn850AjTGquCRNdZrURqpoVn7mVs5jmC%2BpbvG7z0pQHEtzBzlX5yXPdquq3Gdzeo3iO7FWY6hycClZF%2FYsoUCKiNGS6DQihMzHr8vXMkiJfmHo%2Frq12xBPnejz3v%2Fbka6VIv9goJTaEDPykSPMH%2B8TUzXsBd%2BH5wamRNkEvFRsiD3joC9qr%2BvcIxiVRuwPri%2Bt3weoknIUurU8MiBF2C3eb98qUysOdIwAkieXerXO9K2glPOEmEPsENoLFIQ8KfWYwTpN1Azqdu2UP16qUJxPCxw4NWRdSfXdST5rj06znINsUOrpdC%2FRdEGkWdK7Y10qolZMDOgKkUsy1ZZB7aDu0dl74Mx6TweOGUcghSuErPjcpOy%2FcasajZiFr5eICFkJiYONc9g%2Fb9JbZX3yUdqnejOMRyWXNt7BTHwH5jTvUm4y4mVVDGubmuzzhrApyJk65iVVPu%2FThBT2wBK62waj%2BGeDCofxWp2JLuHWY4c3I0wiHPBFqMe3zvbQW8c1XqC8gIt2Sk97OGhuVdcy8erEYaTv3wp7ythigSSFvm4Due5VhNhfUUML8ot0bhklb1%2F7YV%2F1aKy5RmhLAiDxXsicQ94pDHtfsq8iKj7eXfWPb2%2FUMN%2Bcj9cGOqUBpQ55mOsYrD6pl4YryXzvIJo%2Be85FIIZ9pWh0Vdq%2FVLRPDnke9nb4kTH3o1j2dDnqJkqRW6cgnvpOdE4hDimlVInPvzXNGt8B5ydAialDH7wrBRT5mk%2B0atXY56i63Js4aBSff2OQOulVvv8up94uJarJDuQz60xtLrdvEMd63uTSP417XWakJ8L0pwA3nTVIcBCl3DAtrWVLb7rpddZNQInTW5eg&X-Amz-Signature=e378310527245cccdf12dea48d37eb2cb8efd36d7f28eaa0a988e90910db82b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPFDTQ7B%2F20261030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T001539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID42h%2FyAO8h9dh5CIvnGEky%2F6g9X2Tj28H9ha8JEg4FYAiEAyPeMVntgC7Q6HqoGX11xyOD1cLu3eqKpX91XTT6Lop0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOy%2BqlhiLlMTLV3CnCrcA72W1NrexwqSZ4sn850AjTGquCRNdZrURqpoVn7mVs5jmC%2BpbvG7z0pQHEtzBzlX5yXPdquq3Gdzeo3iO7FWY6hycClZF%2FYsoUCKiNGS6DQihMzHr8vXMkiJfmHo%2Frq12xBPnejz3v%2Fbka6VIv9goJTaEDPykSPMH%2B8TUzXsBd%2BH5wamRNkEvFRsiD3joC9qr%2BvcIxiVRuwPri%2Bt3weoknIUurU8MiBF2C3eb98qUysOdIwAkieXerXO9K2glPOEmEPsENoLFIQ8KfWYwTpN1Azqdu2UP16qUJxPCxw4NWRdSfXdST5rj06znINsUOrpdC%2FRdEGkWdK7Y10qolZMDOgKkUsy1ZZB7aDu0dl74Mx6TweOGUcghSuErPjcpOy%2FcasajZiFr5eICFkJiYONc9g%2Fb9JbZX3yUdqnejOMRyWXNt7BTHwH5jTvUm4y4mVVDGubmuzzhrApyJk65iVVPu%2FThBT2wBK62waj%2BGeDCofxWp2JLuHWY4c3I0wiHPBFqMe3zvbQW8c1XqC8gIt2Sk97OGhuVdcy8erEYaTv3wp7ythigSSFvm4Due5VhNhfUUML8ot0bhklb1%2F7YV%2F1aKy5RmhLAiDxXsicQ94pDHtfsq8iKj7eXfWPb2%2FUMN%2Bcj9cGOqUBpQ55mOsYrD6pl4YryXzvIJo%2Be85FIIZ9pWh0Vdq%2FVLRPDnke9nb4kTH3o1j2dDnqJkqRW6cgnvpOdE4hDimlVInPvzXNGt8B5ydAialDH7wrBRT5mk%2B0atXY56i63Js4aBSff2OQOulVvv8up94uJarJDuQz60xtLrdvEMd63uTSP417XWakJ8L0pwA3nTVIcBCl3DAtrWVLb7rpddZNQInTW5eg&X-Amz-Signature=7a0ecae6a79fe996432953a8ce8dca1f6ed362b84c5ca2001ed1f33f5ff12dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







