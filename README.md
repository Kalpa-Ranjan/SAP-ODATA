



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HHSFU%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T012143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDjmEy56jrdyxoOwb0BOvG6OcH2TyYwno9b%2F8QQ5gl9sQIhAO1g7Hwxx6Upe8Dz5brFXXyOx%2Fa%2BeCwzQ0FqBCDuqaPoKv8DCBIQABoMNjM3NDIzMTgzODA1IgxJGBhBzekuj2pDo6Uq3AOUnDutUPbrXRmV1aSKwsiEj34SDCgurfn8w4BNtn0MMn2L9q4mCzGwXMbVImocNUToi%2FpZjr9vz8YH0PoT%2FxNyRQnINGhaXJi1YKVip6Lpk6%2FIN%2Fs%2BvnvjwtRRR7w1qkpxVTrAZayTZyJpJAq%2BBwadYQPXZnPaferm3caO58p0XM%2Bxvcg%2Bw2tbV3jaT4ywF8Qn%2FIc%2FLn8QTha5gFobi776TBN7mjzSBNYQNpwGfyxbdZq5ICZbutN4ANdjoB36cgiAi0uTQYeYvi9HUm7vBkwGiX8PACJ5AvVj2mYGbf3Y%2F6RJuKpM3%2BMvKgOa5C7H3taRNq3vGhhtqWPbc8IWve9vVYkKh8zgfmaMhNRd8e3tSeEGsPMXi06CWCCbthbqJXd7w6k8QqaCnShkK5m3GkbcswDbYOMw8LLYdQTyzNm%2BlepW5htjwqaTANxYBCjpmkP%2BYo4Iewr3SrFZ5BzlemonZ6bNzTFmYs2XnD4cgnmpuH6Ay%2FIOpEwEa353VScUdgn298R%2F6pzvAaLKUtug7U8Rlgk%2BHkds8Q6qPedOFhzKxRiAltVLesKx%2FDXea6vRK38YJYJaVt9wTP%2FcXx3r4iwOoYpxpsrheuCHhcW7uhCaYMxMRdPU8Kcw5pJUMzD%2FzZvLBjqkAR0XRoeJU6TC1yye7cbayFjP%2FLjaDj5GsWm96aCGzZDQwt6QLHE%2FjgScVbeQpHYDwmvCa5CIbsujcOejFUcJ0mGsMO8vZA09F%2BDA1O6SbQfMWRjLn51847h5PxHtzS3YxjdvyKPHGf7Zu5yFEt0fsa2brINFvewQJAZezjrbQbecYNLJ2%2FhSfyTe%2BS%2FbJb%2Bk8Tsm4bYs%2B9zL3WATVrImgmfP8lLT&X-Amz-Signature=42f6ed55ab38f81dc12ab6dbfc87320c24c78657e135b13019fb58cd69090120&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HHSFU%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T012144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDjmEy56jrdyxoOwb0BOvG6OcH2TyYwno9b%2F8QQ5gl9sQIhAO1g7Hwxx6Upe8Dz5brFXXyOx%2Fa%2BeCwzQ0FqBCDuqaPoKv8DCBIQABoMNjM3NDIzMTgzODA1IgxJGBhBzekuj2pDo6Uq3AOUnDutUPbrXRmV1aSKwsiEj34SDCgurfn8w4BNtn0MMn2L9q4mCzGwXMbVImocNUToi%2FpZjr9vz8YH0PoT%2FxNyRQnINGhaXJi1YKVip6Lpk6%2FIN%2Fs%2BvnvjwtRRR7w1qkpxVTrAZayTZyJpJAq%2BBwadYQPXZnPaferm3caO58p0XM%2Bxvcg%2Bw2tbV3jaT4ywF8Qn%2FIc%2FLn8QTha5gFobi776TBN7mjzSBNYQNpwGfyxbdZq5ICZbutN4ANdjoB36cgiAi0uTQYeYvi9HUm7vBkwGiX8PACJ5AvVj2mYGbf3Y%2F6RJuKpM3%2BMvKgOa5C7H3taRNq3vGhhtqWPbc8IWve9vVYkKh8zgfmaMhNRd8e3tSeEGsPMXi06CWCCbthbqJXd7w6k8QqaCnShkK5m3GkbcswDbYOMw8LLYdQTyzNm%2BlepW5htjwqaTANxYBCjpmkP%2BYo4Iewr3SrFZ5BzlemonZ6bNzTFmYs2XnD4cgnmpuH6Ay%2FIOpEwEa353VScUdgn298R%2F6pzvAaLKUtug7U8Rlgk%2BHkds8Q6qPedOFhzKxRiAltVLesKx%2FDXea6vRK38YJYJaVt9wTP%2FcXx3r4iwOoYpxpsrheuCHhcW7uhCaYMxMRdPU8Kcw5pJUMzD%2FzZvLBjqkAR0XRoeJU6TC1yye7cbayFjP%2FLjaDj5GsWm96aCGzZDQwt6QLHE%2FjgScVbeQpHYDwmvCa5CIbsujcOejFUcJ0mGsMO8vZA09F%2BDA1O6SbQfMWRjLn51847h5PxHtzS3YxjdvyKPHGf7Zu5yFEt0fsa2brINFvewQJAZezjrbQbecYNLJ2%2FhSfyTe%2BS%2FbJb%2Bk8Tsm4bYs%2B9zL3WATVrImgmfP8lLT&X-Amz-Signature=81393130d274e88fd3e76a98a5efd67dabca624cd33ce58551352696e48c81a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







