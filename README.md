



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PEGAGOM%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T180505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHy5JN%2BmXKE1DOF8I%2BLqxDlY5IfJVvcup2mWM1pB8eAICIBUcRNJqILj1%2By0YGrS7%2F7880UzeNfdquaMCsOTgldjvKv8DCGkQABoMNjM3NDIzMTgzODA1IgwjaKMC8%2BJxRbJLLEwq3ANB%2BLARy5lRXJsLzuPEUCrXkMSeL0nVIbHqkZq%2BaAvaxS6n0E5dWNNwYwR63JLs%2BWF15Rhpje4YSN5LoId4%2BV3GVsmAGnlf1u%2BQajRMQIWw%2Fkh1PUT7pdU4KDxqDnnoBnkqNHhywHgtHKoKTG%2FE%2F33bYcZ3NQHJAwGHT6H97XykHPqT4sUwb%2BOhfIROWyzwLz97WM%2B3ZSR2kOwvozY%2FdoOFaLE%2F37%2BG%2BzvclQCYP27e%2Bb47F7yE6mmVksfzLCtRr5%2Fj8XqGKaLQCU0JcX9%2F82unVd78yEk2hQpKvHEpuCLf7XvtSyst7awmP7lCrHutIUYpkHiot41nxyoR%2B8F%2F9iT58El2LM21VhKbAtWAaoWEJSh4LBeZRWOeOUXoz%2FmEu0qo3KLjLH8jzoOpAEFyabO1eVRjvADXSKeljmeHOlzu6O0SpWlsuadTnAwVIsp1xtZV1xDLmPn%2FTm6lzGDQiuVDTNuWDaGAgxSnKRF98fGL%2B5RMTWkZqY0a6e1FygHGnD1RoF3VX7xxlZoiEEaDtah9TGIGzfpbmrjD6mz5bXNIXBpXzIRzUdzDw4hDc0weeinGR0ATxcp4Bgd5%2BKPRIcGkwkchFVgNJloC%2F1z5CPtnN7dwAVOgsO1SZ30HTTCSzp3XBjqnAfh9ndfY7pypNWYisOgkWPrviYOgVkN91vljNWgZn%2BntT48Xbhu2ajAI4pVMqYa4qfY4Y8wPZYvDVQuLqvwXlwDUhuTT2Dg8KIGnI3p%2Bhub8yovghuyzglHvoB4ZB%2Bx7CmdToOZzsHOlwe0rT9gkyyP%2BBgyWTIQ2BLZjiaGSuTEwhPQxEwTBRuq2lfRCY0SuarSMqWEI%2BZegi4t2%2Fm5ORkH7SkHl54GH&X-Amz-Signature=ccf859c96719a0b8f52611dc03849c00033db1bf836a49ac562cbea1da0b8a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PEGAGOM%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T180505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHy5JN%2BmXKE1DOF8I%2BLqxDlY5IfJVvcup2mWM1pB8eAICIBUcRNJqILj1%2By0YGrS7%2F7880UzeNfdquaMCsOTgldjvKv8DCGkQABoMNjM3NDIzMTgzODA1IgwjaKMC8%2BJxRbJLLEwq3ANB%2BLARy5lRXJsLzuPEUCrXkMSeL0nVIbHqkZq%2BaAvaxS6n0E5dWNNwYwR63JLs%2BWF15Rhpje4YSN5LoId4%2BV3GVsmAGnlf1u%2BQajRMQIWw%2Fkh1PUT7pdU4KDxqDnnoBnkqNHhywHgtHKoKTG%2FE%2F33bYcZ3NQHJAwGHT6H97XykHPqT4sUwb%2BOhfIROWyzwLz97WM%2B3ZSR2kOwvozY%2FdoOFaLE%2F37%2BG%2BzvclQCYP27e%2Bb47F7yE6mmVksfzLCtRr5%2Fj8XqGKaLQCU0JcX9%2F82unVd78yEk2hQpKvHEpuCLf7XvtSyst7awmP7lCrHutIUYpkHiot41nxyoR%2B8F%2F9iT58El2LM21VhKbAtWAaoWEJSh4LBeZRWOeOUXoz%2FmEu0qo3KLjLH8jzoOpAEFyabO1eVRjvADXSKeljmeHOlzu6O0SpWlsuadTnAwVIsp1xtZV1xDLmPn%2FTm6lzGDQiuVDTNuWDaGAgxSnKRF98fGL%2B5RMTWkZqY0a6e1FygHGnD1RoF3VX7xxlZoiEEaDtah9TGIGzfpbmrjD6mz5bXNIXBpXzIRzUdzDw4hDc0weeinGR0ATxcp4Bgd5%2BKPRIcGkwkchFVgNJloC%2F1z5CPtnN7dwAVOgsO1SZ30HTTCSzp3XBjqnAfh9ndfY7pypNWYisOgkWPrviYOgVkN91vljNWgZn%2BntT48Xbhu2ajAI4pVMqYa4qfY4Y8wPZYvDVQuLqvwXlwDUhuTT2Dg8KIGnI3p%2Bhub8yovghuyzglHvoB4ZB%2Bx7CmdToOZzsHOlwe0rT9gkyyP%2BBgyWTIQ2BLZjiaGSuTEwhPQxEwTBRuq2lfRCY0SuarSMqWEI%2BZegi4t2%2Fm5ORkH7SkHl54GH&X-Amz-Signature=9b2f943a06830816ea48b22999a2247ad4d6c673c0fd7945a9b148e6a1867fcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







