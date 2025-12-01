



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YITCVOXX%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T123414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDoMKSgTx4LBoVvM4gqVKruyE%2B47IOIQ%2B74ZpcdiUPQUQIgMInKwrFPBm1Wwpw7NdxGq89pvO0kXSLAraT%2BgeQ%2BqToqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrc4bh1wx%2FbHBS4ircAx6GVXORXRBF%2Bb%2BwqJOAkxB2W6Zz2mNMMBXBrrOb5gvZYv4BvSu74OW5Nb1DNQhACqfjDjvDDOx8hhaFA%2Fj3wHDHQCkWRjgaWhwQ8Kzc7kYypE%2FUv8WQ%2FViH%2FbeIPLkceJylE4ZIElKSE0bTQbT9YP1h9fYgiPdTaETqOt9Dg3BaITYjmvqvJnlu0pKRoUayFF1HTdK2gun0Bwshuwlf%2Br79%2F6V6pkl0gH50w2T7nKRJNo3jvI2h9F9BVl2jMe65aCHXJWdYViwR2tzaagSO2oZR%2FLs0vBl%2BoO%2F11amUg10LhZNVy025QcZMFyPKjuJS9trGrFPe8RvfztwBuFwOGFErmNKcmBzmuOrmnPZRSi67vStHlrCSfawkcGMlKmBPgCbid84e29TyrLxEIGf7Z0%2Fj2f%2FeRS3bf2L6Qz63AE54%2B8d3l%2FTZ%2FvF430b4oy28V4iXjfsnTvorEpGu%2B9R52%2BQQsAy%2FKqlgymqT81VR9VH36KxaVpsi1JVfXkA%2B%2FbJJW6ya9A0YOs0NQIDfl%2ByMD1vFw2StUDBecCzY6mWNqYoffgUZIl7WRbHyjXrPlEIjoLgfAmbGmwUcWLsFqN6v9pu%2FNH3NCThmIoAAP2HZ5putB%2FVqj3GAQl6fP2ypMPCotckGOqUB1EWe6kR6uMHMicZGhaO3qom%2BkKcM5xQDWwInHigf7TnmVKui7lCC21j7B9NU5wUGHOdDFZ9KvkuYZMUrmJR9tjDqIfeLB4WN1gGYoZLNOjtcKD8w9Eu4pJI%2Fc8ZFLsDCExlZx1xmJQ5llKhjpypDjvyacTHKmhZb7bdejlVYbleMCiGaWluiBuOF6gLZEmh4uhvp9uc67Eoi63eGPhXnJWW%2BCcEa&X-Amz-Signature=14083acff0d6e644361944d311bd5e3613e6003a38c5462b92980aa41ff97ad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YITCVOXX%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T123414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDoMKSgTx4LBoVvM4gqVKruyE%2B47IOIQ%2B74ZpcdiUPQUQIgMInKwrFPBm1Wwpw7NdxGq89pvO0kXSLAraT%2BgeQ%2BqToqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNrc4bh1wx%2FbHBS4ircAx6GVXORXRBF%2Bb%2BwqJOAkxB2W6Zz2mNMMBXBrrOb5gvZYv4BvSu74OW5Nb1DNQhACqfjDjvDDOx8hhaFA%2Fj3wHDHQCkWRjgaWhwQ8Kzc7kYypE%2FUv8WQ%2FViH%2FbeIPLkceJylE4ZIElKSE0bTQbT9YP1h9fYgiPdTaETqOt9Dg3BaITYjmvqvJnlu0pKRoUayFF1HTdK2gun0Bwshuwlf%2Br79%2F6V6pkl0gH50w2T7nKRJNo3jvI2h9F9BVl2jMe65aCHXJWdYViwR2tzaagSO2oZR%2FLs0vBl%2BoO%2F11amUg10LhZNVy025QcZMFyPKjuJS9trGrFPe8RvfztwBuFwOGFErmNKcmBzmuOrmnPZRSi67vStHlrCSfawkcGMlKmBPgCbid84e29TyrLxEIGf7Z0%2Fj2f%2FeRS3bf2L6Qz63AE54%2B8d3l%2FTZ%2FvF430b4oy28V4iXjfsnTvorEpGu%2B9R52%2BQQsAy%2FKqlgymqT81VR9VH36KxaVpsi1JVfXkA%2B%2FbJJW6ya9A0YOs0NQIDfl%2ByMD1vFw2StUDBecCzY6mWNqYoffgUZIl7WRbHyjXrPlEIjoLgfAmbGmwUcWLsFqN6v9pu%2FNH3NCThmIoAAP2HZ5putB%2FVqj3GAQl6fP2ypMPCotckGOqUB1EWe6kR6uMHMicZGhaO3qom%2BkKcM5xQDWwInHigf7TnmVKui7lCC21j7B9NU5wUGHOdDFZ9KvkuYZMUrmJR9tjDqIfeLB4WN1gGYoZLNOjtcKD8w9Eu4pJI%2Fc8ZFLsDCExlZx1xmJQ5llKhjpypDjvyacTHKmhZb7bdejlVYbleMCiGaWluiBuOF6gLZEmh4uhvp9uc67Eoi63eGPhXnJWW%2BCcEa&X-Amz-Signature=a7f708b55b1f97eb4b5e7a64396adb6f1222667c44842f5fae70c1199e26896e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







