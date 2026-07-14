



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3H45QSH%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T075328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAEzXGJkaJ5yO5MrNdnlb%2B8b6m9ke8kX%2F9v%2Fa8ABQlu2AiAUQpZv7yisMF%2F%2BAYD9wwQzNVgwYWXEB5hIRd%2FTaWd1tCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMPfd8N2%2BcVTFOca%2B5KtwDhr5rloNB1xPTaiLC1avsMTQiMeTQUfnl2qO1duETry07NLvqpd92DdlEvC6Zc4nDbAznt0SXRVNZqIxhRdFiFt06KUYkryQzIR%2FuVfd7C5TB7Gn7bvDLE%2FJ4%2BrNjFBDLjiGoXGZfH3uyyWDSaJhG2Wsj0UVD3tVyBilFYnHvGxL2nESQOzi6ce0Z7ZR%2FGCbWdQ8Nz%2BvB8z102xqmN4ZXIgj7ZjKTlBLEx1mY3yV4DCXIEJzKlwpoBEbYr9c6cvctKrLIy%2BO6Pq5938j3ge97ox6LIGTjob%2FiqNmlbnY5V5gyhQmPikQxlQKgLlBvhaLsf%2FcKPSPscq377cErtt5a4AcjztoXXsPJ8sYZ9pn0Fx%2FTopR1SGSCt0mrjSPBZhO1EUlbJtOQQZfcrjNcGm78Vjp6WiQ%2FLr%2FcAey5LcNeWLLY%2BHu5EocOLyJLsSd9Riq7Ds2%2F0pTSzB0%2Fe%2Btp%2Fm2mqiEjoQaL1VE4NhbOaN6g4rD2tIIRWhQoDYOPaMi4cnyE7WjapMU%2FGcFqIyIvbO0jWQdoTpb4qyc7avFFSR4nG9AGRrmO%2B5ogEHDNXhsrlhvrw4EDfR47fvulojgLsEPNemP13377tg1TrOxh2iATRwE6P25M8FkS9eQUjiIwls3X0gY6pgFp8q5ckCDISMx%2B7s6OY2jkcsbzw29tImGuDh0f6kM4pYFhxLN9Osd0A7%2F5Sr2694Uy80iuzSoBc42nxQ9SYhJ7DBME3hTUOiTXhs6BGoaERosmV7LSMhg%2FgvSbpW%2FkCqTuuvaBUMTTtGkRrN%2B45crZwRchd083e1UlfRmw8kXsqJvedBefwyBiFW%2FSh9k31MUI6FWSsfnElMt5bgNOtYlUrylQhQiC&X-Amz-Signature=7a7e77562cc85e148db3e73d1e5774857bf096853fcbb4781b9b3ea87ef8b0b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3H45QSH%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T075328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAEzXGJkaJ5yO5MrNdnlb%2B8b6m9ke8kX%2F9v%2Fa8ABQlu2AiAUQpZv7yisMF%2F%2BAYD9wwQzNVgwYWXEB5hIRd%2FTaWd1tCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMPfd8N2%2BcVTFOca%2B5KtwDhr5rloNB1xPTaiLC1avsMTQiMeTQUfnl2qO1duETry07NLvqpd92DdlEvC6Zc4nDbAznt0SXRVNZqIxhRdFiFt06KUYkryQzIR%2FuVfd7C5TB7Gn7bvDLE%2FJ4%2BrNjFBDLjiGoXGZfH3uyyWDSaJhG2Wsj0UVD3tVyBilFYnHvGxL2nESQOzi6ce0Z7ZR%2FGCbWdQ8Nz%2BvB8z102xqmN4ZXIgj7ZjKTlBLEx1mY3yV4DCXIEJzKlwpoBEbYr9c6cvctKrLIy%2BO6Pq5938j3ge97ox6LIGTjob%2FiqNmlbnY5V5gyhQmPikQxlQKgLlBvhaLsf%2FcKPSPscq377cErtt5a4AcjztoXXsPJ8sYZ9pn0Fx%2FTopR1SGSCt0mrjSPBZhO1EUlbJtOQQZfcrjNcGm78Vjp6WiQ%2FLr%2FcAey5LcNeWLLY%2BHu5EocOLyJLsSd9Riq7Ds2%2F0pTSzB0%2Fe%2Btp%2Fm2mqiEjoQaL1VE4NhbOaN6g4rD2tIIRWhQoDYOPaMi4cnyE7WjapMU%2FGcFqIyIvbO0jWQdoTpb4qyc7avFFSR4nG9AGRrmO%2B5ogEHDNXhsrlhvrw4EDfR47fvulojgLsEPNemP13377tg1TrOxh2iATRwE6P25M8FkS9eQUjiIwls3X0gY6pgFp8q5ckCDISMx%2B7s6OY2jkcsbzw29tImGuDh0f6kM4pYFhxLN9Osd0A7%2F5Sr2694Uy80iuzSoBc42nxQ9SYhJ7DBME3hTUOiTXhs6BGoaERosmV7LSMhg%2FgvSbpW%2FkCqTuuvaBUMTTtGkRrN%2B45crZwRchd083e1UlfRmw8kXsqJvedBefwyBiFW%2FSh9k31MUI6FWSsfnElMt5bgNOtYlUrylQhQiC&X-Amz-Signature=f16af0198f8131a20bd025527313e45889663531a93fe433da060c9e7feae735&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







