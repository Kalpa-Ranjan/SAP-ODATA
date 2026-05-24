



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJ4OCYI%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T131439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDD8GNvgiL39T3AmUppgfmKbJL%2FwxTjQgWrm%2Bcssc4c5wIhALn3g934WTQmnwuvczP00yNbSp9nM1VQjBT6XXkng7vKKv8DCEkQABoMNjM3NDIzMTgzODA1Igy9w6NqJxBhWOgVpTYq3ANKpHcawZlKeIX9QXhsyu308Vj51M0NmCL0QD6anpP7qQcrmqE24oHnp8Cmt%2BZAfCGH2RmokmKHTqsFWentZygdnytB%2B9s8ymw4B57XQ5KwL6oL8Wb01%2FlYef56zbwQSkCJDX1Qp174Z9kw5zA1fZa9zaXIcpocHIs5J9Rb%2BAJObscYAB2r6T0gBeZemzpVTybvGmxdon3CyKJhHlWfnXisgppiu6EopOM8OkLYnit7BdwcUJNh9fAKN5MEAGRJ2UcgPww0ctKAr%2BNqEfOXlShRoJpRMlJImSYbmS7kKAi9Wye7U4O1%2FwAsy%2BFUj8nDwmxBFnVlhwTw%2BPkQczkMTRjkdk5WT4AlGRrFjpjd07%2BDYplFictOF28%2Bnj1c45u1%2Baj6eItALJiuuBfsNA7IVXiRE7KzpSJh2oiWxxTYLAMtBLUkXN2%2BLf%2FQYHRFePwMyVB0tBMPjqiAIHDquAqbUFdoCu368eaNGKgKJRU5tG3yPcHW6DuluaWlcjvJPcBu3%2B6tonpyx5QJ%2FVvODRHrxvSRCw5HlIr8%2BDYt%2FbbekCz6gbJ59duSkLOGzqumTQHkyem6fhVRvDyVqhfj6rDB5He3I7iH953HV4pEpGwLlUkSTpz1JDZd%2Bvmk5ClexDDF6MrQBjqkAaVJ6KyVMGTRIgeZ2pjSWpLFlohnGh%2FuUALHyDF8qzA%2F1LzRW1RRfGndOCvbD8x0CkLh5%2B3%2BYDJLptUxnpWeVLNHwWI%2BLHbb0XAz6RUGC%2F8HRcXL9061TanUOQVOMtp3WVmdcIh5E1VzxrbnbyLeu3aU35ZWE86JufE6H6eRZpFfhFabNTOvZCv%2FBkbbbiCScINSsgQIAvs3AGg8j9SSCrb8SmGe&X-Amz-Signature=88a2aae5d663e5bffc2897565bc1468ed255c9df5e9ddf2a6200fdf3bc355e24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYJ4OCYI%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T131439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDD8GNvgiL39T3AmUppgfmKbJL%2FwxTjQgWrm%2Bcssc4c5wIhALn3g934WTQmnwuvczP00yNbSp9nM1VQjBT6XXkng7vKKv8DCEkQABoMNjM3NDIzMTgzODA1Igy9w6NqJxBhWOgVpTYq3ANKpHcawZlKeIX9QXhsyu308Vj51M0NmCL0QD6anpP7qQcrmqE24oHnp8Cmt%2BZAfCGH2RmokmKHTqsFWentZygdnytB%2B9s8ymw4B57XQ5KwL6oL8Wb01%2FlYef56zbwQSkCJDX1Qp174Z9kw5zA1fZa9zaXIcpocHIs5J9Rb%2BAJObscYAB2r6T0gBeZemzpVTybvGmxdon3CyKJhHlWfnXisgppiu6EopOM8OkLYnit7BdwcUJNh9fAKN5MEAGRJ2UcgPww0ctKAr%2BNqEfOXlShRoJpRMlJImSYbmS7kKAi9Wye7U4O1%2FwAsy%2BFUj8nDwmxBFnVlhwTw%2BPkQczkMTRjkdk5WT4AlGRrFjpjd07%2BDYplFictOF28%2Bnj1c45u1%2Baj6eItALJiuuBfsNA7IVXiRE7KzpSJh2oiWxxTYLAMtBLUkXN2%2BLf%2FQYHRFePwMyVB0tBMPjqiAIHDquAqbUFdoCu368eaNGKgKJRU5tG3yPcHW6DuluaWlcjvJPcBu3%2B6tonpyx5QJ%2FVvODRHrxvSRCw5HlIr8%2BDYt%2FbbekCz6gbJ59duSkLOGzqumTQHkyem6fhVRvDyVqhfj6rDB5He3I7iH953HV4pEpGwLlUkSTpz1JDZd%2Bvmk5ClexDDF6MrQBjqkAaVJ6KyVMGTRIgeZ2pjSWpLFlohnGh%2FuUALHyDF8qzA%2F1LzRW1RRfGndOCvbD8x0CkLh5%2B3%2BYDJLptUxnpWeVLNHwWI%2BLHbb0XAz6RUGC%2F8HRcXL9061TanUOQVOMtp3WVmdcIh5E1VzxrbnbyLeu3aU35ZWE86JufE6H6eRZpFfhFabNTOvZCv%2FBkbbbiCScINSsgQIAvs3AGg8j9SSCrb8SmGe&X-Amz-Signature=00926bcdfefc3e0fbd0bc95ae609bc9bfa6db89d6bd2b6d765a007ae3984af8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







