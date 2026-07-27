



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6NIESE5%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T191845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8DqfLq16DwSSv4fAyj2JopFGS4YxVENfhgnNIsV9uKQIgYLlmXw%2BWSz7eOq1OSrPf9I4cW2keZL898Z%2FpBivpn9Iq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDEomTAx%2BqnHLwU787ircA2e7xbRqgXx0Y4JEiM9M2cHpbqYxz4jRZbEFhiWKITT6Vj8DrK4Si40OrlUmsDAIkkOn3ZfwctFVMvLlrzoFYYyO%2FCpNAmN81sAykvcu487od7k7iggYaZs%2FNIPrdnzNtibVHXW%2Bg%2BNKKwqXniC5%2FRtvJeFMxmYHuuqQfWOeORqwCpuWt%2BOgzgZILOzu7pFzA8Yk0oWzG%2FNT6Aqqiar%2Fl7WwZPtFuIA%2FFoFWoFWmwiTKBXex%2Fz0r%2FiBifVvQCFIrmHiKfx6cpARfv8noRysFC%2F63aVvJrUNuvHkIBc2soEcLvxLoRzBXqjLshp%2F8Guw%2BMkL%2FM%2BCV2%2F%2BVXo2y9J6vNHH0kJVdgTdYmMyd7gCQ6LYH8BzAA5SFIgH1cooQnOU0U6oQum2BuZMijCgVSCnU2%2FV5bWfq0u1Dn7a1kf%2Bn2J1UMSLHFym3MqvFMXFTkIovHYjFe4yHMfgbx7uhHAzDsunePvdCTdAWjZiFhLsto6t99LcmTM%2Bp3Ht4mO1H8pCLaCWXL4uodaEOx75oh%2FRcWrf4X0TDdh3jV18CnpXC07HmckLsJj4r%2FOdhJ9YvrPc%2FE0QwLeeuAZqT51C6U2xeqxazzltWoh1%2FV3%2BC1MVOi%2Bkh5phHV1Jkjdq791UdMK%2FFntMGOqUB%2B7IIkRZYb9bjj1YQQfyISAXQ8fY0v8A6U9FeQVBInE0I3W2ldrjSVLkSGyV4JnG1l7eYBDWJed5Fzm1BikQ68Qfd7rUWOuHo3A9w84yFfbVLOTFceamSV%2BdK22AMpMm5%2FKhDXX%2F%2BtFRxSf7XVGYu6s3yjdXHI5zaK2%2BxQsUFu4gxycxtLRKpL5EriuevbfNT7N9VnjvAI3Fj4V9Aw640x9OOZBEh&X-Amz-Signature=246f932e43a980ec3b90d00c36e8d255c64edf4991e99c5dc4970a14352cdfda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6NIESE5%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T191845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8DqfLq16DwSSv4fAyj2JopFGS4YxVENfhgnNIsV9uKQIgYLlmXw%2BWSz7eOq1OSrPf9I4cW2keZL898Z%2FpBivpn9Iq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDEomTAx%2BqnHLwU787ircA2e7xbRqgXx0Y4JEiM9M2cHpbqYxz4jRZbEFhiWKITT6Vj8DrK4Si40OrlUmsDAIkkOn3ZfwctFVMvLlrzoFYYyO%2FCpNAmN81sAykvcu487od7k7iggYaZs%2FNIPrdnzNtibVHXW%2Bg%2BNKKwqXniC5%2FRtvJeFMxmYHuuqQfWOeORqwCpuWt%2BOgzgZILOzu7pFzA8Yk0oWzG%2FNT6Aqqiar%2Fl7WwZPtFuIA%2FFoFWoFWmwiTKBXex%2Fz0r%2FiBifVvQCFIrmHiKfx6cpARfv8noRysFC%2F63aVvJrUNuvHkIBc2soEcLvxLoRzBXqjLshp%2F8Guw%2BMkL%2FM%2BCV2%2F%2BVXo2y9J6vNHH0kJVdgTdYmMyd7gCQ6LYH8BzAA5SFIgH1cooQnOU0U6oQum2BuZMijCgVSCnU2%2FV5bWfq0u1Dn7a1kf%2Bn2J1UMSLHFym3MqvFMXFTkIovHYjFe4yHMfgbx7uhHAzDsunePvdCTdAWjZiFhLsto6t99LcmTM%2Bp3Ht4mO1H8pCLaCWXL4uodaEOx75oh%2FRcWrf4X0TDdh3jV18CnpXC07HmckLsJj4r%2FOdhJ9YvrPc%2FE0QwLeeuAZqT51C6U2xeqxazzltWoh1%2FV3%2BC1MVOi%2Bkh5phHV1Jkjdq791UdMK%2FFntMGOqUB%2B7IIkRZYb9bjj1YQQfyISAXQ8fY0v8A6U9FeQVBInE0I3W2ldrjSVLkSGyV4JnG1l7eYBDWJed5Fzm1BikQ68Qfd7rUWOuHo3A9w84yFfbVLOTFceamSV%2BdK22AMpMm5%2FKhDXX%2F%2BtFRxSf7XVGYu6s3yjdXHI5zaK2%2BxQsUFu4gxycxtLRKpL5EriuevbfNT7N9VnjvAI3Fj4V9Aw640x9OOZBEh&X-Amz-Signature=04901ef9e2a09a7b250720c88964e984f9b5281cf627b7682f462ef8300b02b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







