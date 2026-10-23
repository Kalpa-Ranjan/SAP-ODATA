



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWZYP2P5%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T061255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhyRbPpSxziI%2BpWRBDwfh0gA1w%2FmY1N7qj2KoX%2FymPtwIhALVwk5CCuUTXfhAMFVqpiqt743MnAKYHbNxKj%2FeUSeqDKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqRflOpzuhAh05HJ0q3ANjtoCu%2F2waufHm2eK%2BFPYhW4BJpWgIBFliQGJ1gxZqhZkAUskKNXL7ghDSoKssrcsTsJ9sqnOmRVvuV%2BkdEHGx2IVcyreyZTpRrJ28t9XyWgJuiI6GrHYNam3HV47WC5pYDNV5yCUyAPSdo%2B1GrdtZzy%2BbtWWFr4QITvtD8rjrz19g2rw%2BtkHzgyhuBMN%2Bkq0lX3g0nXcJyHbOrpQaeweRg7rCxg%2BpRFbAOHv8bCemR9%2BdQOxjb29z%2BLpqKDddNktVBj4SZ0Roo3Zg%2BAFAJNYq3Wv1HQScn0imjf14FeIxzSEPAdaM2v355xkBOd5LY0Z7Swohy30hI3MdCkwyednf%2Fn2klfsW30INzon%2F0mumc38KtJvuzI5k2TbwWFYpbgB%2FKmzBJM8%2BA1iQGC%2BRtQeK6USla5s99oCuJbj7h3t7cgD%2BCDWN5AOAaiNRVF9xxOnV3Xd%2FtY2AtaXlyA%2FWYdpUXhmQ63j08mW9UNsznMu6ppAhjU4%2B%2Bg%2BtglZlyeeSkDY9Sfx%2FyzM2Ny2qsD9S7x7kfoRgliW1xg6k5jMxSzkdiicem7AlezdvQpiGc4sWGyyWMMJZVM6C30z0yqkQaZJGpHjpEJ2%2BYtEcaS7L%2FPEzLXiQSV9SJwvPP3HI7DDShOvWBjqkASQgF1Rx0dTV8sST7HS4MtAxpRwqez9dzRCy1f0SRqYG8RtMMyrCTdXTU1qI1vnOVp6dO7wgQguw84mf%2FDzY9FRXqUHvBEF1q1CTRMRMcFhECN4EAE8DWd2CAL5pjL%2BVtmOj9iuhZ21iM0oMbvt01%2BkKRTdm8Qu3L4U4XDHXA9W65ckBprbU1KBGRLzapJhh%2FQ3s2eNUV6cvWE6IR7pM7AATFXk3&X-Amz-Signature=8db60b17fd35b19017d2baa04723217a562a9d40dda65da803b5bb20a0f4658d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWZYP2P5%2F20261023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T061256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhyRbPpSxziI%2BpWRBDwfh0gA1w%2FmY1N7qj2KoX%2FymPtwIhALVwk5CCuUTXfhAMFVqpiqt743MnAKYHbNxKj%2FeUSeqDKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqRflOpzuhAh05HJ0q3ANjtoCu%2F2waufHm2eK%2BFPYhW4BJpWgIBFliQGJ1gxZqhZkAUskKNXL7ghDSoKssrcsTsJ9sqnOmRVvuV%2BkdEHGx2IVcyreyZTpRrJ28t9XyWgJuiI6GrHYNam3HV47WC5pYDNV5yCUyAPSdo%2B1GrdtZzy%2BbtWWFr4QITvtD8rjrz19g2rw%2BtkHzgyhuBMN%2Bkq0lX3g0nXcJyHbOrpQaeweRg7rCxg%2BpRFbAOHv8bCemR9%2BdQOxjb29z%2BLpqKDddNktVBj4SZ0Roo3Zg%2BAFAJNYq3Wv1HQScn0imjf14FeIxzSEPAdaM2v355xkBOd5LY0Z7Swohy30hI3MdCkwyednf%2Fn2klfsW30INzon%2F0mumc38KtJvuzI5k2TbwWFYpbgB%2FKmzBJM8%2BA1iQGC%2BRtQeK6USla5s99oCuJbj7h3t7cgD%2BCDWN5AOAaiNRVF9xxOnV3Xd%2FtY2AtaXlyA%2FWYdpUXhmQ63j08mW9UNsznMu6ppAhjU4%2B%2Bg%2BtglZlyeeSkDY9Sfx%2FyzM2Ny2qsD9S7x7kfoRgliW1xg6k5jMxSzkdiicem7AlezdvQpiGc4sWGyyWMMJZVM6C30z0yqkQaZJGpHjpEJ2%2BYtEcaS7L%2FPEzLXiQSV9SJwvPP3HI7DDShOvWBjqkASQgF1Rx0dTV8sST7HS4MtAxpRwqez9dzRCy1f0SRqYG8RtMMyrCTdXTU1qI1vnOVp6dO7wgQguw84mf%2FDzY9FRXqUHvBEF1q1CTRMRMcFhECN4EAE8DWd2CAL5pjL%2BVtmOj9iuhZ21iM0oMbvt01%2BkKRTdm8Qu3L4U4XDHXA9W65ckBprbU1KBGRLzapJhh%2FQ3s2eNUV6cvWE6IR7pM7AATFXk3&X-Amz-Signature=7a62ea1febff671df834d7b3479ac71e25a72a64d788b8b3c0babac9f519ca92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







