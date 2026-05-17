



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPEUXMI5%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T081355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSHUwM0AxCjY7NfYbcnw9gqUa1Zc2HGYvGB2%2Fg9GIn%2BAiEA2U02pZXabJjnnuSdjHxS7JhxefaXT%2B2c%2B0xdHSNdDOwqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd%2BwvTlHihvSDGNPSrcAzQq1W%2BSZ4Fu9sF5hGrqApKe6ubF35YatD85OL6C0jx1C46%2BQy3U%2B22u6IeRp3y%2Fq77jTxI4eeaDCrRNMeQopiTeGub88%2FX82y4hfQDOnTV4XSk99BvTxLlTEOgWOlEctIfhD%2FJsK3rSyDKzNjv9fezJlOVWTFP%2BzCFnJ7OlsE1a4PCcjQgyb76nwamBAa%2Fo8mJ%2Br1XB1GntMvPb57bIYiYXE0q1GtKi1OtYpFtWieCEccmJDFBHiFdCTSODGrLWV3zvcoaJDRD77Dwi%2FE7QWYEJlMC6CP9Ye4Mp9Dz0hnIsX2fnOp3h0Fuiyb9kbsZoPOtjSw7M40gXpzKjt%2BxRJz%2FauQb3lvYqjbniMAVvr5eqQ9uidYnPnE6zWP6iG1opbijfhpHiLVR2%2BIxsI81VlAxRwz%2BBRN9kqCTtnHN9TFKMFokhFG3NkJm%2BGonNRWOY6poKq5sYZMTSqQX%2BfZkmaDwoAQMoIWGFaYd4iVwLHQlEulyqSHMTQJoLwL3vz5uTEry6erUOz7nSAY7XlRjJZW71UvyOmD8ndkhwINVsYJPxJtjD52wN8OhYOg8gg%2B19fpSiDGPG%2Bx0JPOWKk4s3gHQp1cRaG1UWa3%2FOCw%2BJ4TaMIX2FYA6A1w%2Bm1jo4MK7epdAGOqUBctCBpUR3oD2nJdftQ4MDmo4fq6T0yxdi4Nl8A5VQu7isupl3uAsUC3XdSSddpaknIq70L3VtLSNDhhf6YU%2B8CVHBRv%2FQ7ckmFvHvHfMxR2AUca0aMiCgLa37o4DY8jd%2Fb4g5G0sYX7qnkfXsfmipKapdZ570S14PhW9GTkSUyMf%2BWysC%2FL1IFZa56sIS0EzTDcVwhnPCwF9polfsK1pXDPAXIXCe&X-Amz-Signature=73af7a49206d014c94036a4b0762674010b3a0cf05db3d2e6bcfaf7053a53b83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPEUXMI5%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T081355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHSHUwM0AxCjY7NfYbcnw9gqUa1Zc2HGYvGB2%2Fg9GIn%2BAiEA2U02pZXabJjnnuSdjHxS7JhxefaXT%2B2c%2B0xdHSNdDOwqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd%2BwvTlHihvSDGNPSrcAzQq1W%2BSZ4Fu9sF5hGrqApKe6ubF35YatD85OL6C0jx1C46%2BQy3U%2B22u6IeRp3y%2Fq77jTxI4eeaDCrRNMeQopiTeGub88%2FX82y4hfQDOnTV4XSk99BvTxLlTEOgWOlEctIfhD%2FJsK3rSyDKzNjv9fezJlOVWTFP%2BzCFnJ7OlsE1a4PCcjQgyb76nwamBAa%2Fo8mJ%2Br1XB1GntMvPb57bIYiYXE0q1GtKi1OtYpFtWieCEccmJDFBHiFdCTSODGrLWV3zvcoaJDRD77Dwi%2FE7QWYEJlMC6CP9Ye4Mp9Dz0hnIsX2fnOp3h0Fuiyb9kbsZoPOtjSw7M40gXpzKjt%2BxRJz%2FauQb3lvYqjbniMAVvr5eqQ9uidYnPnE6zWP6iG1opbijfhpHiLVR2%2BIxsI81VlAxRwz%2BBRN9kqCTtnHN9TFKMFokhFG3NkJm%2BGonNRWOY6poKq5sYZMTSqQX%2BfZkmaDwoAQMoIWGFaYd4iVwLHQlEulyqSHMTQJoLwL3vz5uTEry6erUOz7nSAY7XlRjJZW71UvyOmD8ndkhwINVsYJPxJtjD52wN8OhYOg8gg%2B19fpSiDGPG%2Bx0JPOWKk4s3gHQp1cRaG1UWa3%2FOCw%2BJ4TaMIX2FYA6A1w%2Bm1jo4MK7epdAGOqUBctCBpUR3oD2nJdftQ4MDmo4fq6T0yxdi4Nl8A5VQu7isupl3uAsUC3XdSSddpaknIq70L3VtLSNDhhf6YU%2B8CVHBRv%2FQ7ckmFvHvHfMxR2AUca0aMiCgLa37o4DY8jd%2Fb4g5G0sYX7qnkfXsfmipKapdZ570S14PhW9GTkSUyMf%2BWysC%2FL1IFZa56sIS0EzTDcVwhnPCwF9polfsK1pXDPAXIXCe&X-Amz-Signature=4275ca73c407ff6a5012fa86a1466175f2c54d0808fe92247a38b2ac8e85d562&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







