



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LJNFJCW%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T061153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHBflcYTe2JBUhdnGMa2Swi4%2FVuhmH%2FcBUgUIlSHkhKAIhAMI3rp5RX1VxisjSLkzTaX3IWibEV2l1BHRsPx%2BexoOjKv8DCG4QABoMNjM3NDIzMTgzODA1Igz7UQCZvSVNBfPp5Cgq3AO9aLNzLfL9lrto0D%2FGlbAqTqsfgdmR7vtHmy9hYTJ4MxN4jcAqim2xEn6juCtpBR5GvuRk0F950FTY%2BI%2FFy7PHd%2BDxd7nnFRc6BtcVKTTNsTgH3VzX6enksS27reK38ftK%2FoGo3jdVngP%2FVn%2BhfjUhkgpfY5TxYSADNWw%2BJMeN7eI8fxEONbj5085sbdVuhDTNEmie5HVm9wUJTiLdxkRT5sXaYfm2D20bsdv5pRIR4ROa8KekIkNlG7l%2FlL5zoatTMRB5wnzyYr5VztC0EjxxEgWjVVPyb501bI6jiq9%2BjnmIW83ylKexoDRkUH6XIh9VfkOUjDyuRPblVVQ9IeKiTUVUgkPwKKnb0TMD2duu3KRGX%2FIQlCoQNKoQnuHn4TrqbTn496yQX7dKDU7IgntXEOrwxv6Xe8v6VPf8n%2FDvv9RzWs%2BpClkg6nM%2Bakprk1C%2BPz3A1srD7IoWiZOUiZQawEIkZmiow3DwSgegcZw2RcpCpUB0pEpitzfY0YNRAsbMNP3nlL5QsuEXCTtM7R0tVE81XHgd8IdVG7Um82G0kZ0JNCxBh4%2BTl5woA90q1MtaFLj7dpaLN8SZrO4xsbvkVBv2hB6BdXIGY%2FZXXpHhRB6hUN4cSlhRMuIOaTCUlI%2FYBjqkASzu2RGxETljxwOg06f1L9fsoy1BKlpCQWe%2BdntXN79rwanla8spInoER%2Fok8%2BCopoV3M6y7965hgjXwHc7cU84GN%2BT3bfa7tvDdncS5yrk8MsXxBnr2XxTndxtpLGkx7gexCvWgEWrkBPT0SiDdUJa5g%2FCHnpLRQwtfTixNF2kFnXHG26vsf3U357bgLb0%2FI1189FDheoP%2By0TptygDP%2FLb2kj2&X-Amz-Signature=a01103491fc4e947cce5e5c88b589a6d74f6f1c06d54a5209e9e1bbf7beeb4c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LJNFJCW%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T061153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHBflcYTe2JBUhdnGMa2Swi4%2FVuhmH%2FcBUgUIlSHkhKAIhAMI3rp5RX1VxisjSLkzTaX3IWibEV2l1BHRsPx%2BexoOjKv8DCG4QABoMNjM3NDIzMTgzODA1Igz7UQCZvSVNBfPp5Cgq3AO9aLNzLfL9lrto0D%2FGlbAqTqsfgdmR7vtHmy9hYTJ4MxN4jcAqim2xEn6juCtpBR5GvuRk0F950FTY%2BI%2FFy7PHd%2BDxd7nnFRc6BtcVKTTNsTgH3VzX6enksS27reK38ftK%2FoGo3jdVngP%2FVn%2BhfjUhkgpfY5TxYSADNWw%2BJMeN7eI8fxEONbj5085sbdVuhDTNEmie5HVm9wUJTiLdxkRT5sXaYfm2D20bsdv5pRIR4ROa8KekIkNlG7l%2FlL5zoatTMRB5wnzyYr5VztC0EjxxEgWjVVPyb501bI6jiq9%2BjnmIW83ylKexoDRkUH6XIh9VfkOUjDyuRPblVVQ9IeKiTUVUgkPwKKnb0TMD2duu3KRGX%2FIQlCoQNKoQnuHn4TrqbTn496yQX7dKDU7IgntXEOrwxv6Xe8v6VPf8n%2FDvv9RzWs%2BpClkg6nM%2Bakprk1C%2BPz3A1srD7IoWiZOUiZQawEIkZmiow3DwSgegcZw2RcpCpUB0pEpitzfY0YNRAsbMNP3nlL5QsuEXCTtM7R0tVE81XHgd8IdVG7Um82G0kZ0JNCxBh4%2BTl5woA90q1MtaFLj7dpaLN8SZrO4xsbvkVBv2hB6BdXIGY%2FZXXpHhRB6hUN4cSlhRMuIOaTCUlI%2FYBjqkASzu2RGxETljxwOg06f1L9fsoy1BKlpCQWe%2BdntXN79rwanla8spInoER%2Fok8%2BCopoV3M6y7965hgjXwHc7cU84GN%2BT3bfa7tvDdncS5yrk8MsXxBnr2XxTndxtpLGkx7gexCvWgEWrkBPT0SiDdUJa5g%2FCHnpLRQwtfTixNF2kFnXHG26vsf3U357bgLb0%2FI1189FDheoP%2By0TptygDP%2FLb2kj2&X-Amz-Signature=80b48c0698e248a9f3b9cc001f6c674041611ab4f9263f8104562195bd6df495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







