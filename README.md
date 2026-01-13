



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U64SXRB%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T062705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIBHRYvxFpMa3FiBgg4ZkBEwDvwLtqBZPyrRGSNXnrXyAAiEA4hrt6Gngd3BdRI8umXSg9FdQhseWJk9cTnF58tyn7qcqiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP40t3XAGE6ZW%2FTS8yrcA8sTwg3KNZVQAp8f%2FR1Efb%2FPPajMB6ivZeW%2F9tpKSBfaD6wZVBe2cx26hkms8u6V2qHM7fmVWroza82ycBUo3TTikAMi03NFTp%2Bxs0AnMe%2BIu1I0v5EaFykofp8NTCbBgVdMxKKEV3xBX%2FKG1ZsR61WvwJ1lxe8y7xFmOWHjoeDgEq22wBvqy2Ove7vNWZYCASbYEqtlUttsxTH%2B7aTXD4Dq8yHHNJq%2BmwqQCvXeRTNkFjwXKmURJ7YUR9ilWtbM4Ac5H6hMjrKmBkIPMHOLy7oBI5sE%2FujDs55cJzzbnThWGNPF%2FW0w6tLYOWDqi3efanj%2BP0ZXNcybvI4c%2FDt07WKKbvf5NitUDsGDtY7wwaD5LkHSuFn3E8fbuwQSt9PkhpALbpdD%2FWmnhuXZv4wvivasHw%2B2BaDrTSiQ7EyjZtchmD8CqssYZixN1rYNoC1lsYwrEea2S8mJRHC%2BoZy1dAoFZA%2BsrmzgZHhMJ1l0ktkqvE9RzQ4xhu8P%2FZRJc%2FoyLGrV0BS6%2BBy4UKwAEQc8kWvGmlDVcZQSjiW%2BuMMY0yUaUdL7bKnMB7g3yOmqpEMh%2B84gKoZOGehfcYGajaOnTEELoCQGcGdydeqoBHzmQAqtczKVrwhVbUzvWEkCMM2hl8sGOqUBfT8da5NrrkJ067yE4w9Zr1p8k973ekQ8k24wcKgR1mcd%2BI4eEBJrzmjOzktOQEjWvKJUkOTZYf0dhVLAN9YnDEaANEYGgh0%2FSExXQfBavxyDApTrGGPmAOgaVqZGkhhvVKC4P5jqzdmxvpAX0FgSxBfwBLV27eaLSSfyJNbAcvGQ1F9sYUmrBqOiwcsIaYjWnNGzg8RYlCoNUH0Hte0drnYK%2Fen%2B&X-Amz-Signature=7768fe8e349881c93d9d912c57361737f7c5b80c31ce7fdeb775193596caef63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U64SXRB%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T062705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJHMEUCIBHRYvxFpMa3FiBgg4ZkBEwDvwLtqBZPyrRGSNXnrXyAAiEA4hrt6Gngd3BdRI8umXSg9FdQhseWJk9cTnF58tyn7qcqiAQI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP40t3XAGE6ZW%2FTS8yrcA8sTwg3KNZVQAp8f%2FR1Efb%2FPPajMB6ivZeW%2F9tpKSBfaD6wZVBe2cx26hkms8u6V2qHM7fmVWroza82ycBUo3TTikAMi03NFTp%2Bxs0AnMe%2BIu1I0v5EaFykofp8NTCbBgVdMxKKEV3xBX%2FKG1ZsR61WvwJ1lxe8y7xFmOWHjoeDgEq22wBvqy2Ove7vNWZYCASbYEqtlUttsxTH%2B7aTXD4Dq8yHHNJq%2BmwqQCvXeRTNkFjwXKmURJ7YUR9ilWtbM4Ac5H6hMjrKmBkIPMHOLy7oBI5sE%2FujDs55cJzzbnThWGNPF%2FW0w6tLYOWDqi3efanj%2BP0ZXNcybvI4c%2FDt07WKKbvf5NitUDsGDtY7wwaD5LkHSuFn3E8fbuwQSt9PkhpALbpdD%2FWmnhuXZv4wvivasHw%2B2BaDrTSiQ7EyjZtchmD8CqssYZixN1rYNoC1lsYwrEea2S8mJRHC%2BoZy1dAoFZA%2BsrmzgZHhMJ1l0ktkqvE9RzQ4xhu8P%2FZRJc%2FoyLGrV0BS6%2BBy4UKwAEQc8kWvGmlDVcZQSjiW%2BuMMY0yUaUdL7bKnMB7g3yOmqpEMh%2B84gKoZOGehfcYGajaOnTEELoCQGcGdydeqoBHzmQAqtczKVrwhVbUzvWEkCMM2hl8sGOqUBfT8da5NrrkJ067yE4w9Zr1p8k973ekQ8k24wcKgR1mcd%2BI4eEBJrzmjOzktOQEjWvKJUkOTZYf0dhVLAN9YnDEaANEYGgh0%2FSExXQfBavxyDApTrGGPmAOgaVqZGkhhvVKC4P5jqzdmxvpAX0FgSxBfwBLV27eaLSSfyJNbAcvGQ1F9sYUmrBqOiwcsIaYjWnNGzg8RYlCoNUH0Hte0drnYK%2Fen%2B&X-Amz-Signature=d03032570a3768ec83eaf0023976194395555f86a97cb846ad1ac9c00cbc1c31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







