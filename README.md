



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3JELGFC%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T121120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCbnjXoetKluy08KeYP7KfyIU7WZDJaoefZU2S4KyN0KgIhAOoAkwTO%2FcoQoJvyuxKnJP0eSdZTKT7aN7JS%2Bfrosi4BKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBMQ1JLAGJlgYpZaAq3AOWlm8QYsIo6clNYOwbHnHXxEu7hemHpRGGXSPx1YQLcGgGq3n33RmZvT%2FTdGlcVURHdZIDLCMpfKF5G3JUxe%2Fuxk6bc8Fs%2Fq9OORkjNsRBsuJAK%2BAf7h%2BVsRXh0RVIjHTPQVIiMq1ucx0IDq%2Fg8m8zuPfkyi1RL9J%2BlDix0eQtwjA5cyHTslS%2FM000oXUJTDlgZrIvnrLpTb3SAn%2FmiX%2FXo9JV%2BirEXBjI8MB3zAhia2JpnJ1GCWxKWBNJJmQIq6Mkn81HS%2BV5QbgAMAuR5wEDkv15akmwoFxfRkLoHLGZgtu03u%2BPOz%2FD9m3j6DlgjwDqta7WBVF8tBUgod2iYlEaBGPMP0PAzM%2BXGhfA9iHwgtGpi2U5I827WKIDRdy5NoESGF9J3FUiQLF067qXC1MAmpoAKey8FoaX3eFKhgzboh2CgcIvRp3H62wzOj5Y5MZ8wRbMV1sDBIRvZ2qKMmRyKDRtprUSQGdm%2F4t0npH7EV1pjU8cpWD8RjUgWV8wUm7wUQAI8yzI2cXwG20V7iFB%2FK4Iv7pVmEtMLjFpJTd%2Bde66yEMWTun4mmQHh%2BPfioBcL7Xe2zzjcbZZVjUS7VuUwP5n90akJ0GZWiQJsO0s6Bf6mnC9IyGQe%2FG7xTC378LWBjqkAamTmHAu58WwwHO%2F2IabJI65hBAqgBAl9nH0mCbE0qjpcRekMpZrEjqzOk9Nw5jQ2NZ18LD1faEtaxGXt2jrxO4KPUpGDi2JvinwemsAx%2Bfy2RfuC3HRGQE%2BmXxW2iqlKEFjamSUYL2x7wSRrHr6cPIRHZne8l4oogtku9rcUzAq90tvFI%2FyUAyksXOr8fJZS2EcgjHdEnSmBO%2FPINh3H6xDw7lx&X-Amz-Signature=de00823a703cf28aad1e4625fcd9fc73a6a4bb7b67e579f3c1edf05b16681f2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3JELGFC%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T121120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCbnjXoetKluy08KeYP7KfyIU7WZDJaoefZU2S4KyN0KgIhAOoAkwTO%2FcoQoJvyuxKnJP0eSdZTKT7aN7JS%2Bfrosi4BKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBMQ1JLAGJlgYpZaAq3AOWlm8QYsIo6clNYOwbHnHXxEu7hemHpRGGXSPx1YQLcGgGq3n33RmZvT%2FTdGlcVURHdZIDLCMpfKF5G3JUxe%2Fuxk6bc8Fs%2Fq9OORkjNsRBsuJAK%2BAf7h%2BVsRXh0RVIjHTPQVIiMq1ucx0IDq%2Fg8m8zuPfkyi1RL9J%2BlDix0eQtwjA5cyHTslS%2FM000oXUJTDlgZrIvnrLpTb3SAn%2FmiX%2FXo9JV%2BirEXBjI8MB3zAhia2JpnJ1GCWxKWBNJJmQIq6Mkn81HS%2BV5QbgAMAuR5wEDkv15akmwoFxfRkLoHLGZgtu03u%2BPOz%2FD9m3j6DlgjwDqta7WBVF8tBUgod2iYlEaBGPMP0PAzM%2BXGhfA9iHwgtGpi2U5I827WKIDRdy5NoESGF9J3FUiQLF067qXC1MAmpoAKey8FoaX3eFKhgzboh2CgcIvRp3H62wzOj5Y5MZ8wRbMV1sDBIRvZ2qKMmRyKDRtprUSQGdm%2F4t0npH7EV1pjU8cpWD8RjUgWV8wUm7wUQAI8yzI2cXwG20V7iFB%2FK4Iv7pVmEtMLjFpJTd%2Bde66yEMWTun4mmQHh%2BPfioBcL7Xe2zzjcbZZVjUS7VuUwP5n90akJ0GZWiQJsO0s6Bf6mnC9IyGQe%2FG7xTC378LWBjqkAamTmHAu58WwwHO%2F2IabJI65hBAqgBAl9nH0mCbE0qjpcRekMpZrEjqzOk9Nw5jQ2NZ18LD1faEtaxGXt2jrxO4KPUpGDi2JvinwemsAx%2Bfy2RfuC3HRGQE%2BmXxW2iqlKEFjamSUYL2x7wSRrHr6cPIRHZne8l4oogtku9rcUzAq90tvFI%2FyUAyksXOr8fJZS2EcgjHdEnSmBO%2FPINh3H6xDw7lx&X-Amz-Signature=00fb4a1f17d5d3c6145b60fa3508ed03d6e4eca550df7b449039c9e83a29b28e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







