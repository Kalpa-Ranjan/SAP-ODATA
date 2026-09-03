



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SLQYBRT%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T103326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIFWw0iP9Y0%2FO9IQNXbbPz3VYAea2cPCdz87ideDip3gfAiAKKgIau8FIh%2FuGDV5b3Meegwhndnryt16gPtU%2BBAE0vSqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYduqsZmP5mSk%2FG3KtwDa3DAC1c8Z0WYmi2t6q0ntRidtNLFX%2BH9iYth5DwJ5ogFql1Uj3FITFL2vTGbW6qDxgOi2%2BLJ%2FZlxbFHqen0re5EJaXOtZ83wtwPdnuMyGMk5%2Fui55fubzQaOR0%2FCdBOOgMrL2KDOgbRPCK4WsLaKpm9Aj1DgL%2BcaHVMumz3ee4%2F7PiCOKxr4VGXxEjRhfUeqkHnx6iZlOrBYP1vl2gnS1TZNiV2CNIBcE%2BVWy1fbTDEYSzXOUaZfRu8R7fcY0dX3bErMgvHdV0yA1%2B6x9nHt%2B1VET4jm3iHb0%2B27sUAqoO5llLpMKmLGddB657JWBtmGsXyySNimmUoFxhAKO00t8bwqJiFrtwsw5LwRXeoa2tRDcZuHLJG3pFQkTQP9tIqJbjwhO78XFK5Ro8GYH%2FjwkTkDagmDCCiE0iXtSBNFEYtyJ79Wl8qvptEnUDKfzwShIBH6Ey85%2FzR2SnFDkW1zeo%2FMjJycyo5kxcZCyfBmO6Vjsh336LyUC7AtQ4qX%2FQ5mZMo%2BthnhOXUhGz8L%2Fk5DjO22Q02MIHzLNumKmFdJSCyPIcA7Vc0WKb27Aph7tXvTkr1QPMFdljkd7gzOhqvdZccHW4QagOias0Zsj9c%2BnEkuMMw2QXH7ztawCJYwju7k1AY6pgFFCj%2BFuCXaFtx0ANVw5NfryQ2fEnvbnmvWbIVnaY15S1SzmfRggo1lgfLCqCP2chKvsQGQqPsFF9IRFPjqoUxPFI7ab8FXZfPSTragDtoREsA3gRsq8YOvj%2Fugt66HOy3o%2FtDlJfxuJs%2BnTpWZer4TeXY24Yj63C94bxN2U0rZRKNDFUb5JjRCpGrCTR9KWta6AvffVXIKM8wdi6H%2B61LgFsYYquK%2F&X-Amz-Signature=2ed2fc1b822a08bac465fbeb5e2c874737bf3b94dae10e7257161f53f94edd44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SLQYBRT%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T103326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIFWw0iP9Y0%2FO9IQNXbbPz3VYAea2cPCdz87ideDip3gfAiAKKgIau8FIh%2FuGDV5b3Meegwhndnryt16gPtU%2BBAE0vSqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYduqsZmP5mSk%2FG3KtwDa3DAC1c8Z0WYmi2t6q0ntRidtNLFX%2BH9iYth5DwJ5ogFql1Uj3FITFL2vTGbW6qDxgOi2%2BLJ%2FZlxbFHqen0re5EJaXOtZ83wtwPdnuMyGMk5%2Fui55fubzQaOR0%2FCdBOOgMrL2KDOgbRPCK4WsLaKpm9Aj1DgL%2BcaHVMumz3ee4%2F7PiCOKxr4VGXxEjRhfUeqkHnx6iZlOrBYP1vl2gnS1TZNiV2CNIBcE%2BVWy1fbTDEYSzXOUaZfRu8R7fcY0dX3bErMgvHdV0yA1%2B6x9nHt%2B1VET4jm3iHb0%2B27sUAqoO5llLpMKmLGddB657JWBtmGsXyySNimmUoFxhAKO00t8bwqJiFrtwsw5LwRXeoa2tRDcZuHLJG3pFQkTQP9tIqJbjwhO78XFK5Ro8GYH%2FjwkTkDagmDCCiE0iXtSBNFEYtyJ79Wl8qvptEnUDKfzwShIBH6Ey85%2FzR2SnFDkW1zeo%2FMjJycyo5kxcZCyfBmO6Vjsh336LyUC7AtQ4qX%2FQ5mZMo%2BthnhOXUhGz8L%2Fk5DjO22Q02MIHzLNumKmFdJSCyPIcA7Vc0WKb27Aph7tXvTkr1QPMFdljkd7gzOhqvdZccHW4QagOias0Zsj9c%2BnEkuMMw2QXH7ztawCJYwju7k1AY6pgFFCj%2BFuCXaFtx0ANVw5NfryQ2fEnvbnmvWbIVnaY15S1SzmfRggo1lgfLCqCP2chKvsQGQqPsFF9IRFPjqoUxPFI7ab8FXZfPSTragDtoREsA3gRsq8YOvj%2Fugt66HOy3o%2FtDlJfxuJs%2BnTpWZer4TeXY24Yj63C94bxN2U0rZRKNDFUb5JjRCpGrCTR9KWta6AvffVXIKM8wdi6H%2B61LgFsYYquK%2F&X-Amz-Signature=0383640e24d9a7a48518d15c8fd144aa36ffd9a2766fd5ad55caf32dc9b05697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







