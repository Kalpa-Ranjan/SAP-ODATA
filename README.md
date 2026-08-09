



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMRDFEXQ%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T011557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPTpTk2rn9Cgk8pixyTN2NaLH%2FSldQ55GLH8BYvJZ54gIgBjeUtqcqB%2BrMuZI4WX0xbxUHCtpZe2ORYYfuHNTDGDEq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDN9o609JcxYfNfMFZyrcA19XPzAOCIu8vwuGwqATlpR2U58sFmAHRyPK%2BOZozSazm1sPdkxvoTvW4KOtHkHYcAayZ91VGSpBWUfrpdLAKWZt6FGNes1iBQTD1e8uASym0zYIUMErxZGfMKMpx28MhSYn4UHcRVKpKZ%2FALTWm9tRSQGxUuN3W6r4VvFyEPz6gof7DxIHr7Tsf6FMSiD%2BfS5f5E7B2tKJKBac1UWzbeqvbR1%2FxfQDPf7LXPlzGVnD9eFLpiC%2B%2BoH25%2Bp05g2TrmDWeLDyY5LNoSELo8j0RLfbyUQ0wLb2HPIgos0N2PS3GY0vwMEdzFJagCHDTRHNbZQAkWmpSHbbFIbdz7%2BmEvrVRhobFD%2Fk7OWNOAbOY%2FOUuEW2%2F60x%2FbVwmdFCzv%2FHW%2BugpRq%2FZwDgVG3ofEfPdQb3niALXUKqFHbvYBwntZDW5jPSb1zU1DmH0A62DI5GI7UzEzrFKN0Rz8uSS4gqbpTP3T0mdDP%2FUJUdJGuzgwb0qpoVTNKS5vBYSZTJJ7wAn3apOljoGKT55w1qUjtjgR81jakn6ASUfue%2BoQ71viBA%2FYGujwpXUqMCGGksB6%2BMSWsfoY8jBp7c%2FG5%2BSnGcpMtiEz2kk47Cr0r34Lw4ZoX43P%2FKjws03rZFpVudDMPrV3tMGOqUB9AYQ4%2FxZk54X0ww1AgO4LqnrA3QFPKqXhM6yHij0naICy6Kl52ZDzETmO8zVt7U7jySp2bAQgAXvftPnBzGXK5MxfjJjRsfNbBHWvYvMR73iZhIrgYTc4q0ZHnSjIXPn62RuICgj8m2G4F6YGFiE7MbQJusNfegXplMTr6Y9l9KesbXvICgonhWOtAE68SiiC5ZdFk9CePu5q%2FVHkTbZX%2FA7KD3X&X-Amz-Signature=b4b99fdbf7af48d219d861eb387ddba2656bac8df727e576a64410c6f0e948bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMRDFEXQ%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T011557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPTpTk2rn9Cgk8pixyTN2NaLH%2FSldQ55GLH8BYvJZ54gIgBjeUtqcqB%2BrMuZI4WX0xbxUHCtpZe2ORYYfuHNTDGDEq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDN9o609JcxYfNfMFZyrcA19XPzAOCIu8vwuGwqATlpR2U58sFmAHRyPK%2BOZozSazm1sPdkxvoTvW4KOtHkHYcAayZ91VGSpBWUfrpdLAKWZt6FGNes1iBQTD1e8uASym0zYIUMErxZGfMKMpx28MhSYn4UHcRVKpKZ%2FALTWm9tRSQGxUuN3W6r4VvFyEPz6gof7DxIHr7Tsf6FMSiD%2BfS5f5E7B2tKJKBac1UWzbeqvbR1%2FxfQDPf7LXPlzGVnD9eFLpiC%2B%2BoH25%2Bp05g2TrmDWeLDyY5LNoSELo8j0RLfbyUQ0wLb2HPIgos0N2PS3GY0vwMEdzFJagCHDTRHNbZQAkWmpSHbbFIbdz7%2BmEvrVRhobFD%2Fk7OWNOAbOY%2FOUuEW2%2F60x%2FbVwmdFCzv%2FHW%2BugpRq%2FZwDgVG3ofEfPdQb3niALXUKqFHbvYBwntZDW5jPSb1zU1DmH0A62DI5GI7UzEzrFKN0Rz8uSS4gqbpTP3T0mdDP%2FUJUdJGuzgwb0qpoVTNKS5vBYSZTJJ7wAn3apOljoGKT55w1qUjtjgR81jakn6ASUfue%2BoQ71viBA%2FYGujwpXUqMCGGksB6%2BMSWsfoY8jBp7c%2FG5%2BSnGcpMtiEz2kk47Cr0r34Lw4ZoX43P%2FKjws03rZFpVudDMPrV3tMGOqUB9AYQ4%2FxZk54X0ww1AgO4LqnrA3QFPKqXhM6yHij0naICy6Kl52ZDzETmO8zVt7U7jySp2bAQgAXvftPnBzGXK5MxfjJjRsfNbBHWvYvMR73iZhIrgYTc4q0ZHnSjIXPn62RuICgj8m2G4F6YGFiE7MbQJusNfegXplMTr6Y9l9KesbXvICgonhWOtAE68SiiC5ZdFk9CePu5q%2FVHkTbZX%2FA7KD3X&X-Amz-Signature=c9b8f3e914fc047d221881d137a56ed6ac0ba161974649d9f49e5104a7836c2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







