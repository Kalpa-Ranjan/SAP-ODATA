



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGQFHMXS%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T092538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQCUEE7FBIs7gOZCPMOfg2ajQZM4Cl5g9nu%2F4Tb30lnDNgIgFXOFX%2BdcNhM%2Fm4A1IfmJWbpvXWd9Fm3nKrOCOLNgJOoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDIRtdrUwCDYylmF0YSrcA3tM%2FgqSq7sdlRdadlRJ2HRBwZVpLt8LxmAJNcFTpA6lI4BXV9q%2BYA0G76ghh4rlbH6LT%2BhNdSqoGqHeveqyr3%2FjxFLldJO%2BUnPQkVTzJfUHXmoR0NlHHVZOoZCDjw%2Ft300VJYAowCw%2Fuy6wf%2Bft3U9lB1BxCPiPkt9uWskzc0i%2BNv%2FT%2F8T%2BVc1XDrTlAGlIAOjUHG4Arp%2FCwe%2BrxD762im3zkwBD0RVV%2F9jDmGSUyosghPivfiPfuZgQWu74nmAteRyEMo7f2vHRkPiqJeatoSAl0cOISCtjsYcA%2FfcIu21%2Ba60HJFGhMqyzl61UUlhjgvQ7qYXGBe9yMFjfzXtC3d9X37UIPgY0pV%2Beq%2BryWHQuc8%2FLsVFgUUQfHZHnNuJLACYGoz1LZj7ptqi0QFrcBCm9%2Ft2DVRXHKjIDNbzwH8zexQajlA4k0NEIIAYAc99bbAEQVaBUn%2B3opi6Z%2BEih3OP7gAFSftVqoDhplg9swrblSo90yTChlJ2ASOF7Z8OJcJp0s1GGe1RSAosMNrq%2F5tm%2FGItTQcRlzfZ38UK7iYAdBKjtE5CvwDTsW6h4dPUaHn5rsvnllcIO6c6vddfmwnM1iN6jBfG1tlpCCtu4qzcWFQh9Jt%2FjrAM2TSYMIrGudEGOqUB%2BgbzYdoJPceYwR0khDt55EU9vPiVvXOWHOJn2YkW8zNQdTSuGdUu5oOY68EEbgyrcDbNGEMO%2Bo0FnesRFi5%2FCMEiznP37AvN9uDR3XeXdCk3z0Fu0TU1U54DVqgzQvLdOOO14CWTmqzW5glWof5gvpRjYn22kAd2%2FmqjuSszDN6QFWt2z%2FMe4J9QFQ809zxXV4O7GGtk1O%2FJdj%2F2EWo4ge633KeF&X-Amz-Signature=8b0844a519bc13bc9f481d3ca74c71dc6e3ec7074d5d03fbf671e6697c0fac48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGQFHMXS%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T092539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQCUEE7FBIs7gOZCPMOfg2ajQZM4Cl5g9nu%2F4Tb30lnDNgIgFXOFX%2BdcNhM%2Fm4A1IfmJWbpvXWd9Fm3nKrOCOLNgJOoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDIRtdrUwCDYylmF0YSrcA3tM%2FgqSq7sdlRdadlRJ2HRBwZVpLt8LxmAJNcFTpA6lI4BXV9q%2BYA0G76ghh4rlbH6LT%2BhNdSqoGqHeveqyr3%2FjxFLldJO%2BUnPQkVTzJfUHXmoR0NlHHVZOoZCDjw%2Ft300VJYAowCw%2Fuy6wf%2Bft3U9lB1BxCPiPkt9uWskzc0i%2BNv%2FT%2F8T%2BVc1XDrTlAGlIAOjUHG4Arp%2FCwe%2BrxD762im3zkwBD0RVV%2F9jDmGSUyosghPivfiPfuZgQWu74nmAteRyEMo7f2vHRkPiqJeatoSAl0cOISCtjsYcA%2FfcIu21%2Ba60HJFGhMqyzl61UUlhjgvQ7qYXGBe9yMFjfzXtC3d9X37UIPgY0pV%2Beq%2BryWHQuc8%2FLsVFgUUQfHZHnNuJLACYGoz1LZj7ptqi0QFrcBCm9%2Ft2DVRXHKjIDNbzwH8zexQajlA4k0NEIIAYAc99bbAEQVaBUn%2B3opi6Z%2BEih3OP7gAFSftVqoDhplg9swrblSo90yTChlJ2ASOF7Z8OJcJp0s1GGe1RSAosMNrq%2F5tm%2FGItTQcRlzfZ38UK7iYAdBKjtE5CvwDTsW6h4dPUaHn5rsvnllcIO6c6vddfmwnM1iN6jBfG1tlpCCtu4qzcWFQh9Jt%2FjrAM2TSYMIrGudEGOqUB%2BgbzYdoJPceYwR0khDt55EU9vPiVvXOWHOJn2YkW8zNQdTSuGdUu5oOY68EEbgyrcDbNGEMO%2Bo0FnesRFi5%2FCMEiznP37AvN9uDR3XeXdCk3z0Fu0TU1U54DVqgzQvLdOOO14CWTmqzW5glWof5gvpRjYn22kAd2%2FmqjuSszDN6QFWt2z%2FMe4J9QFQ809zxXV4O7GGtk1O%2FJdj%2F2EWo4ge633KeF&X-Amz-Signature=dba1f32b1a8f14c5926f21e98cf13920592328284f9fc3cae818cadd3637b2ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







