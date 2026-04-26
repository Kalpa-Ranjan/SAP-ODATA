



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM4TMEUE%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T072147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELaAhsRJ0cZMZFO7CcTIxf2aB4Dh6H0NiQLw%2BBNpQecAiADPTXPpJYKEMGoH9Sd1q%2Bw6ZZBMTAyqnX4VNa1lTynfyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8HXNDP837d%2BABUQSKtwDOev1T2V9PAyusiPMYE6NpOyfMhHH6Elx6EzUjY0nyTbWCG%2B0OUteSYPDbjDIW0Nh26iKuDJlWxuhF5jFUNPkndm7aLTEMtriG8cKJ74cFU%2F5mSsnxzzOj5TeY%2BW5Z9UcIVzd%2BebOzUIagWgr%2BlGGFusE5fpVY6s2cpWUw%2BhTvFwqSg3I3oYgIpE7PHbk0uCrhfG8JbSyGplLabdnGTn2%2FQQM3gAOO5FNtf%2BOgyQ8JFraTSfjy0xlKP1YTAjk%2FxoKRvg2SZwU5wDiWqLeLYU%2FXsY3eJ%2BRflsJSDIQVw%2B8wNIeIU%2FFpdCPoNN044C%2BLWCKFrOrZfwTfgbzCtWOCFfs3EoQ%2Bwajz13z6ovtHGXXwYWc6jC%2FjH999Ab%2BpRxgxNAN09GK2fYznxb4pMP5N8JQVg%2BEaXAAB6UfwNW8LipoZnUXqvuARpSRDssoghPMtVFOKhualfS54b691PRabZB1r4t0%2FW5yEMfy2TKVzgKNLs5smetAOoRPQqYafQhiYZJ3%2FrVCUy0jxmOfASsLFXlZvYCFpdOpMofl78wMwcOfg5S%2BIr1EhDENZK%2Fm5lPXW5CHpttON2YtgozYOyLEd6lrqIBbAuPETCQI5jeC2Z2FpbpUCYcfnEHF%2BH9pzJ0w%2B%2FS2zwY6pgFcgXMpG9VZgJTJAj7bvxLD%2Bajf%2FosVmaI9aVR6WNS67Uay9n1mJX874F1bJkTOFPegmaMjvjFB4dQqtQc1lRj32lS9HqLU6DAz6y3V4RjCFhZKjXjevEfcx9ku2B%2FOaCE8i3YIq%2BOXt%2BgKJZon2dHuzNK%2BHFqzrm2ioWSTz8aNyVEByHf15BE3V1vMfVfGwvEecGUz4MMfnGlifrw9GdoFM%2BHvHzSx&X-Amz-Signature=07f3d577d1d0d79f60e96c360f866aab51b728a923e066699b5965c999d4a154&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM4TMEUE%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T072147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELaAhsRJ0cZMZFO7CcTIxf2aB4Dh6H0NiQLw%2BBNpQecAiADPTXPpJYKEMGoH9Sd1q%2Bw6ZZBMTAyqnX4VNa1lTynfyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8HXNDP837d%2BABUQSKtwDOev1T2V9PAyusiPMYE6NpOyfMhHH6Elx6EzUjY0nyTbWCG%2B0OUteSYPDbjDIW0Nh26iKuDJlWxuhF5jFUNPkndm7aLTEMtriG8cKJ74cFU%2F5mSsnxzzOj5TeY%2BW5Z9UcIVzd%2BebOzUIagWgr%2BlGGFusE5fpVY6s2cpWUw%2BhTvFwqSg3I3oYgIpE7PHbk0uCrhfG8JbSyGplLabdnGTn2%2FQQM3gAOO5FNtf%2BOgyQ8JFraTSfjy0xlKP1YTAjk%2FxoKRvg2SZwU5wDiWqLeLYU%2FXsY3eJ%2BRflsJSDIQVw%2B8wNIeIU%2FFpdCPoNN044C%2BLWCKFrOrZfwTfgbzCtWOCFfs3EoQ%2Bwajz13z6ovtHGXXwYWc6jC%2FjH999Ab%2BpRxgxNAN09GK2fYznxb4pMP5N8JQVg%2BEaXAAB6UfwNW8LipoZnUXqvuARpSRDssoghPMtVFOKhualfS54b691PRabZB1r4t0%2FW5yEMfy2TKVzgKNLs5smetAOoRPQqYafQhiYZJ3%2FrVCUy0jxmOfASsLFXlZvYCFpdOpMofl78wMwcOfg5S%2BIr1EhDENZK%2Fm5lPXW5CHpttON2YtgozYOyLEd6lrqIBbAuPETCQI5jeC2Z2FpbpUCYcfnEHF%2BH9pzJ0w%2B%2FS2zwY6pgFcgXMpG9VZgJTJAj7bvxLD%2Bajf%2FosVmaI9aVR6WNS67Uay9n1mJX874F1bJkTOFPegmaMjvjFB4dQqtQc1lRj32lS9HqLU6DAz6y3V4RjCFhZKjXjevEfcx9ku2B%2FOaCE8i3YIq%2BOXt%2BgKJZon2dHuzNK%2BHFqzrm2ioWSTz8aNyVEByHf15BE3V1vMfVfGwvEecGUz4MMfnGlifrw9GdoFM%2BHvHzSx&X-Amz-Signature=957c3373ea6bd1da50ce5bb326d0452baca4ca60428ffcf5386bd0800ca38e36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







