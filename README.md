



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634LK5OHL%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T125900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHgKZ7n5%2FiQLQADRPe13HxC7j2eizKLGaFcDvcOa8tjfAiBEKavr7QtKl0RneWgtL2nXmdAiP8ZwvoZIAzmTEEMcqSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMLmqvEMbYPcsQgAS3KtwDYSgE4myh%2BF4kbeT2%2BgJhGbd56yyPk2p3ZIi6worZAkhicxaMgiIXOTehQJw1SLrHcTGZtAj48DhtKg%2BWP%2F%2Be3vJhu93slFK7QpGl%2FOSXN60jcx%2FSFMXbFrn4qr4wcC00tUPyOz2ej7FeaxWZobG7EvO8ffKkHIx1b8Sj8hxrDwWQDEo1zLd0Q3lM5l0l2RCEUu68LHl2lJykKi3%2BuH2kP1ffii80TpzWjHHdZkFCoKMyTpKQRVGB%2FOzacouKONoh7DTiW1v%2Fl1q01v2TitYxqh1fjLtLKJEc1IBnVWlgHfymFhWuqAL5XY5VNHZzCTc7DM6q4ZLY%2BgCVAToM3g0u23ASAsdYmvrmoNV2cPzHSbXXu97jJXRQQO0b1swwUnXMs1IAHoACYZqcAmNzunXtfZ9JWQ5y%2BY2VVZUIFOIXFcEyyh%2F2H41tWDzYQVJWvlvcBB7Awj5fwElgWB6A7gesqOnIXeW12hkeQsuSvJynwtRrlnY%2BSRUecZhpzOc2Qdij%2BW5lutoeUIllS%2BJix4ce%2FWFfInkpp%2F8%2BKolow4X%2F9bUaj1scnB0vz0PW8TWAS%2FR8sRjhh8PdlrDIPB32%2BD5drJZouHXrFcj6Mp1%2FOPqkBg9EtM5j5RZ9dAk1QRQwxaTXzwY6pgHHCQYBmUExAqNuAM4GRDMi1G3uZVxUkG3QkN7k7KXcAQQ961k%2FhUq5j4sn8GxqwjmFMBPJ40DQHM5Y7yzYRzQiYQZoOGD3tGtlSEQas0GvSgMajjzGgyXoZJjh1%2FSYw5w8RlBY%2FBMnPn8nF%2BbKmtu8D3FGm3EiaKhjz%2B7PR2ePp%2BMwEzx1ujA4qq%2Fmf3iWp8CPMPeuaabOOBv6sO5cHgQT8yX4dHuy&X-Amz-Signature=14f628bf2ca75af215d521e3b3b573ee746f9d8bb764f97d231f0d3e67604d1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634LK5OHL%2F20260502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260502T125900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHgKZ7n5%2FiQLQADRPe13HxC7j2eizKLGaFcDvcOa8tjfAiBEKavr7QtKl0RneWgtL2nXmdAiP8ZwvoZIAzmTEEMcqSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMLmqvEMbYPcsQgAS3KtwDYSgE4myh%2BF4kbeT2%2BgJhGbd56yyPk2p3ZIi6worZAkhicxaMgiIXOTehQJw1SLrHcTGZtAj48DhtKg%2BWP%2F%2Be3vJhu93slFK7QpGl%2FOSXN60jcx%2FSFMXbFrn4qr4wcC00tUPyOz2ej7FeaxWZobG7EvO8ffKkHIx1b8Sj8hxrDwWQDEo1zLd0Q3lM5l0l2RCEUu68LHl2lJykKi3%2BuH2kP1ffii80TpzWjHHdZkFCoKMyTpKQRVGB%2FOzacouKONoh7DTiW1v%2Fl1q01v2TitYxqh1fjLtLKJEc1IBnVWlgHfymFhWuqAL5XY5VNHZzCTc7DM6q4ZLY%2BgCVAToM3g0u23ASAsdYmvrmoNV2cPzHSbXXu97jJXRQQO0b1swwUnXMs1IAHoACYZqcAmNzunXtfZ9JWQ5y%2BY2VVZUIFOIXFcEyyh%2F2H41tWDzYQVJWvlvcBB7Awj5fwElgWB6A7gesqOnIXeW12hkeQsuSvJynwtRrlnY%2BSRUecZhpzOc2Qdij%2BW5lutoeUIllS%2BJix4ce%2FWFfInkpp%2F8%2BKolow4X%2F9bUaj1scnB0vz0PW8TWAS%2FR8sRjhh8PdlrDIPB32%2BD5drJZouHXrFcj6Mp1%2FOPqkBg9EtM5j5RZ9dAk1QRQwxaTXzwY6pgHHCQYBmUExAqNuAM4GRDMi1G3uZVxUkG3QkN7k7KXcAQQ961k%2FhUq5j4sn8GxqwjmFMBPJ40DQHM5Y7yzYRzQiYQZoOGD3tGtlSEQas0GvSgMajjzGgyXoZJjh1%2FSYw5w8RlBY%2FBMnPn8nF%2BbKmtu8D3FGm3EiaKhjz%2B7PR2ePp%2BMwEzx1ujA4qq%2Fmf3iWp8CPMPeuaabOOBv6sO5cHgQT8yX4dHuy&X-Amz-Signature=ba43bf06f33f59a539970efaad3da8f82342b3dc44a83d0a4d96c528025b1835&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







