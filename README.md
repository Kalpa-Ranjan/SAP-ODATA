



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YYPKGKB%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T021251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCy6HGaBiRuaB4ePpFCp88ZH1EAmRNraO8KRcmY7isSOAIgSQKjRfHn098pVeyShDZQRdSboZJAg0aWJn7qEoXT31YqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn8ww%2F2yZxkUkmsRyrcA9lj9o2jt%2B7Wch0rfVpvvB%2BW8cLIYFUaS33xdUywtv%2Fq6qz3JaVzWFkAaIoOzIOwQuKCWuexL9yiYPgqsu%2FYi8ao9wO8iWLvGFNWYd57z4%2FW3xLlyF29AlfIWomZH44O0gIx6sIWJwjovQKTMII89wtlCiAwlmQW5C4l6hibcE%2BGexT5NumAFh7fAqkwYlLnTnwcJaGLZXS8ltsAZ%2FiWtRBOiborabze7e%2BTQ%2BJiP%2FMNaxs5vOMrRljaHyUSqfSa1Co9GcseEvqQtkrjUumSUE5EkVXeGc77tomCXchmSFsE%2Brv7JJ0xgO93QrQtAeDbU6Rbn6rEsRxt9W0XpYlC3oHZazpHz9z0V8NH%2FwR%2FI17%2BBJ5YLkgtxz60kdTGCwPQcLEeWCw7v1DXPeFZGY5OgAwBZYv%2Bc2RXGKqDh4zj5WdNuCpkhu5Z9VUiFLUp4kbOFfKNgyn1hObG36woRIvgZT%2F7dDEduBO6MqiC%2FO7Zkiq9uEbIm3y%2BweaYOIsXjhMx4nMY0FSsDOs9JNiGt6pOrRM3D38gF2NiRPY6A7GyESpC9xzdROuyW4%2B4aNp%2FmDuSP3Wgkio%2F9k2ELJinS3%2Fy7S%2Fbi97%2B2ZzzeWO75X79koOylRFpphvdf6koZH%2FkMOzCutMGOqUBYPf%2Fyn7%2B20BLBFR2Jj5KfTuGuvyFFKb9EfEH9M4C51tKVoJ2hULC0GdGTNhGgbeVn%2BXNedSSqa5aIEltaEIKhi6Mww6GhJu0HiUNpW1fLVBEt92Rj7aF9lmL5J28vmSlDFZS7UN6qLVIEYzMT9A8LTnDGFSgXteXl3JuIQQ3DJBGymbV1djSFcK%2Bn1IG1013kk4qOHBaqpwWwopjFXdBeWuJzYH6&X-Amz-Signature=b5644f5883d307800949a0cbbec20d621e083bbd8e26653ecb85f6a3fbd378c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YYPKGKB%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T021251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCy6HGaBiRuaB4ePpFCp88ZH1EAmRNraO8KRcmY7isSOAIgSQKjRfHn098pVeyShDZQRdSboZJAg0aWJn7qEoXT31YqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn8ww%2F2yZxkUkmsRyrcA9lj9o2jt%2B7Wch0rfVpvvB%2BW8cLIYFUaS33xdUywtv%2Fq6qz3JaVzWFkAaIoOzIOwQuKCWuexL9yiYPgqsu%2FYi8ao9wO8iWLvGFNWYd57z4%2FW3xLlyF29AlfIWomZH44O0gIx6sIWJwjovQKTMII89wtlCiAwlmQW5C4l6hibcE%2BGexT5NumAFh7fAqkwYlLnTnwcJaGLZXS8ltsAZ%2FiWtRBOiborabze7e%2BTQ%2BJiP%2FMNaxs5vOMrRljaHyUSqfSa1Co9GcseEvqQtkrjUumSUE5EkVXeGc77tomCXchmSFsE%2Brv7JJ0xgO93QrQtAeDbU6Rbn6rEsRxt9W0XpYlC3oHZazpHz9z0V8NH%2FwR%2FI17%2BBJ5YLkgtxz60kdTGCwPQcLEeWCw7v1DXPeFZGY5OgAwBZYv%2Bc2RXGKqDh4zj5WdNuCpkhu5Z9VUiFLUp4kbOFfKNgyn1hObG36woRIvgZT%2F7dDEduBO6MqiC%2FO7Zkiq9uEbIm3y%2BweaYOIsXjhMx4nMY0FSsDOs9JNiGt6pOrRM3D38gF2NiRPY6A7GyESpC9xzdROuyW4%2B4aNp%2FmDuSP3Wgkio%2F9k2ELJinS3%2Fy7S%2Fbi97%2B2ZzzeWO75X79koOylRFpphvdf6koZH%2FkMOzCutMGOqUBYPf%2Fyn7%2B20BLBFR2Jj5KfTuGuvyFFKb9EfEH9M4C51tKVoJ2hULC0GdGTNhGgbeVn%2BXNedSSqa5aIEltaEIKhi6Mww6GhJu0HiUNpW1fLVBEt92Rj7aF9lmL5J28vmSlDFZS7UN6qLVIEYzMT9A8LTnDGFSgXteXl3JuIQQ3DJBGymbV1djSFcK%2Bn1IG1013kk4qOHBaqpwWwopjFXdBeWuJzYH6&X-Amz-Signature=489c7cf10c6addb2fa7a23b8a6dcca1f78b8f7f35e000ca990c64faa229e443f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







