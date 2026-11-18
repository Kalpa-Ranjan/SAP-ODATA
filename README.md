



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM3WWZT6%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T001243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIHpSaxmOsoGsFw6ZL3LzE5HU9E87%2FofpJEXqMHxquKqlAiEA2CpjYhxf6kcOmDxR2vY5EXG%2F4OfaouORs72Cvwqz6WgqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPUT%2FvuPXvsCZPgoYCrcA%2BhjsqNlF8EPBAMxkVoA74hmV8QuEDyxUgHijakcthkUaLmCGceR%2FWutHxoMF%2ByBNcAN%2FeBXc59wBjS2qUp0lDmSIzUAYnZIdUcBpGOFDbf%2Ft1bq%2BjOiKdUo59gHe1Nfj5to5zw4lVvKAT6KJjzByvzNCDhwGv3rrSjLCssIxjJxUH3DK2Xt9HVYcgp9H4KSUiuvQxvU5in2tyc4r6DFFdzoEQ811dR7DHDOgRfTThV5g%2B4RR1vyHNVEj%2BTJIoC31cKzzSUj855ACwi9JqLg9gX3i1uHAgEHta%2BDvqpMioLbaEGP2%2FxB2mNi5fc%2B00vYA8gq5MYx59P12KNYwbD8oLfg13A1r%2B67%2F2CUhGYNMEYNwzvQKV2A4CxuPw3SXhbUJyfT4Qkii6A79pKO4EMBelQ0l%2B6kNnSqHCN5uYx7izy2ovQf6cmksxmUPhRba%2BkTGl9%2F8C15EA0H9ZukZfhC53xwBNNQCCwoSFEDjRDJIF9IPvD6qsB8EK5JPuCHvqZpP1wPOmFo3MEPJOvWvkbuBuPif2hSsU0hH1tLrv3RC0tq%2FlBEFe7kVuHjR8WfWDz6KK3aPVnqzsCJc4RPp7kA6xvFX%2FWt%2B%2FlHLVby%2FQm54ZsMTuqLFHsdC6gdjhiOMJ2989cGOqUBR1TNYosDNA2Xos4eSpkDb9K7mYlOJq12plF6L%2FPQJ7LHI5ERNhNMp%2FfULR3pQpcSq%2FileG8sb9de85n%2Fv%2F9W8s7DVV323d3zKeNlURMgqJyrBJSnqWEKqM4HLUFVMESAxqT2swgcxiNTThIadFCUYNlKNW7FtUXeY4ILIxMHJFP0nsX3GF%2FmtbTrNzMhCQsGQjd9GtNI8dCEMEaZQtOpT678LYgK&X-Amz-Signature=e4356435211a44c1066436fa7b3d4020853fda67fd28a9fd88bb3fffc3b5e9f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM3WWZT6%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T001243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIHpSaxmOsoGsFw6ZL3LzE5HU9E87%2FofpJEXqMHxquKqlAiEA2CpjYhxf6kcOmDxR2vY5EXG%2F4OfaouORs72Cvwqz6WgqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPUT%2FvuPXvsCZPgoYCrcA%2BhjsqNlF8EPBAMxkVoA74hmV8QuEDyxUgHijakcthkUaLmCGceR%2FWutHxoMF%2ByBNcAN%2FeBXc59wBjS2qUp0lDmSIzUAYnZIdUcBpGOFDbf%2Ft1bq%2BjOiKdUo59gHe1Nfj5to5zw4lVvKAT6KJjzByvzNCDhwGv3rrSjLCssIxjJxUH3DK2Xt9HVYcgp9H4KSUiuvQxvU5in2tyc4r6DFFdzoEQ811dR7DHDOgRfTThV5g%2B4RR1vyHNVEj%2BTJIoC31cKzzSUj855ACwi9JqLg9gX3i1uHAgEHta%2BDvqpMioLbaEGP2%2FxB2mNi5fc%2B00vYA8gq5MYx59P12KNYwbD8oLfg13A1r%2B67%2F2CUhGYNMEYNwzvQKV2A4CxuPw3SXhbUJyfT4Qkii6A79pKO4EMBelQ0l%2B6kNnSqHCN5uYx7izy2ovQf6cmksxmUPhRba%2BkTGl9%2F8C15EA0H9ZukZfhC53xwBNNQCCwoSFEDjRDJIF9IPvD6qsB8EK5JPuCHvqZpP1wPOmFo3MEPJOvWvkbuBuPif2hSsU0hH1tLrv3RC0tq%2FlBEFe7kVuHjR8WfWDz6KK3aPVnqzsCJc4RPp7kA6xvFX%2FWt%2B%2FlHLVby%2FQm54ZsMTuqLFHsdC6gdjhiOMJ2989cGOqUBR1TNYosDNA2Xos4eSpkDb9K7mYlOJq12plF6L%2FPQJ7LHI5ERNhNMp%2FfULR3pQpcSq%2FileG8sb9de85n%2Fv%2F9W8s7DVV323d3zKeNlURMgqJyrBJSnqWEKqM4HLUFVMESAxqT2swgcxiNTThIadFCUYNlKNW7FtUXeY4ILIxMHJFP0nsX3GF%2FmtbTrNzMhCQsGQjd9GtNI8dCEMEaZQtOpT678LYgK&X-Amz-Signature=7e83fbdf9ddd6fd920e068366becf12c4ba1966a1c725723477e7612df468624&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







