



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT6VDIOD%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T005728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC%2FlrCU7BnPEGYJRBR30U0QPnhUzRVRotDzDdjXIJlkQQIgct7XyxaM%2BGD3eSCRKj0ihhTQxeyfY0YjId8AKYJVOw0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFY%2BAvLVHHDIYlrprSrcAzuKzFaEV1bEvB86ayk7nH4NwXMT8ef6ZvrrI%2FMRTejCtgF6e%2FqMqnX2fe6dec3q%2BbVpDhvA6zutxnGZNXPKeG3fR9lyCL15pAmzr9%2F78%2F7H5TnA3ka8VKGTGcbmJDX6LO0BPfrtLmMsVA7QUIhOvmtioHtKTHbzQ3%2BgmQelLVSuizdEMD84NflRbWwmaIBOUipiTFmTA4vmtlhWU%2B8O7P7aOiHw7WFGARSWf9VhXEs1PXj2K0ihWG%2Fl2FMJbq%2BaTlzHGBy4iOPXDF4v6Y%2FA5E0lNFPkMAJVDflFYMVbhxM5REGsv%2FAUubq3yZaUHBBTn96238DRvX7YtHpwGfHS8q40x8853ChfGe63rv4Ca2o7SlJ9ov0j5W1nNU3yNWfqJF9LSpXRdAOGTbYyFXccGkMMNJyEmlCFV85mCsVhkKoDTaW58zAjdd8saYpVQsGLSowDhiSnbLzSz3sOjTDPaGYGWX6uvDHeq5c8Gx0MyClieXA95eCpCweVbppeYdr0dhojppDRpeP3GwBOVatBrvLlJWWToPslIkiFWjPSU%2FlN5jI8viZoRWWMPGoobGBKT36B5p0BRBHERnrRYSJ380EYg8Nl2A%2BX3TOFxRVsKH7Vy950cK3ISC3HRdSDML2Qs9QGOqUBQfE%2BxFlgQUCv9Fz4xCMkFDWtEvNHlIv%2BoeMhMh5GzGTil6LF1hUfWp93VKXy95%2FiNl5eiSL9X7gvMdM8%2BnZXAMTQoeuqSbiZZC80HvdmYAE4106ht%2FwgUm2Fpz0pZNapQxGIBiDbWRURV57quodOitmCJt8iKhKBiHk9d5ziiPE6FzKis2mgEKQLysHu%2Fmz3eFovhjEbxaNP9RhNjID3Ezpdhs6T&X-Amz-Signature=7407fd97bd38186484f5ae80f3c444a699bb9ec94b36e37f80fb8f671f9a3541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT6VDIOD%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T005728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC%2FlrCU7BnPEGYJRBR30U0QPnhUzRVRotDzDdjXIJlkQQIgct7XyxaM%2BGD3eSCRKj0ihhTQxeyfY0YjId8AKYJVOw0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFY%2BAvLVHHDIYlrprSrcAzuKzFaEV1bEvB86ayk7nH4NwXMT8ef6ZvrrI%2FMRTejCtgF6e%2FqMqnX2fe6dec3q%2BbVpDhvA6zutxnGZNXPKeG3fR9lyCL15pAmzr9%2F78%2F7H5TnA3ka8VKGTGcbmJDX6LO0BPfrtLmMsVA7QUIhOvmtioHtKTHbzQ3%2BgmQelLVSuizdEMD84NflRbWwmaIBOUipiTFmTA4vmtlhWU%2B8O7P7aOiHw7WFGARSWf9VhXEs1PXj2K0ihWG%2Fl2FMJbq%2BaTlzHGBy4iOPXDF4v6Y%2FA5E0lNFPkMAJVDflFYMVbhxM5REGsv%2FAUubq3yZaUHBBTn96238DRvX7YtHpwGfHS8q40x8853ChfGe63rv4Ca2o7SlJ9ov0j5W1nNU3yNWfqJF9LSpXRdAOGTbYyFXccGkMMNJyEmlCFV85mCsVhkKoDTaW58zAjdd8saYpVQsGLSowDhiSnbLzSz3sOjTDPaGYGWX6uvDHeq5c8Gx0MyClieXA95eCpCweVbppeYdr0dhojppDRpeP3GwBOVatBrvLlJWWToPslIkiFWjPSU%2FlN5jI8viZoRWWMPGoobGBKT36B5p0BRBHERnrRYSJ380EYg8Nl2A%2BX3TOFxRVsKH7Vy950cK3ISC3HRdSDML2Qs9QGOqUBQfE%2BxFlgQUCv9Fz4xCMkFDWtEvNHlIv%2BoeMhMh5GzGTil6LF1hUfWp93VKXy95%2FiNl5eiSL9X7gvMdM8%2BnZXAMTQoeuqSbiZZC80HvdmYAE4106ht%2FwgUm2Fpz0pZNapQxGIBiDbWRURV57quodOitmCJt8iKhKBiHk9d5ziiPE6FzKis2mgEKQLysHu%2Fmz3eFovhjEbxaNP9RhNjID3Ezpdhs6T&X-Amz-Signature=19c4fdf53a1cfe66fcfdd8dfe92b6f13ab9f1168c1060d61b4ccb54c18df9537&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







