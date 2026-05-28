



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466277QC4ZS%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T153807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAH7e4dRc6KPOMytFD4Ubb2W8t2whQTZghgyt09JXKZHAiBW6Se00ZjF6sw2IiYZciRHQ7EKyo8qqAi3bpc5HMCPiCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl%2BneNDGxxxS3t9O8KtwDeyseFh8wdCrUJJ62pj2c8e1xbsaYStI1Ee2wbcB1acgdNyGPWHUCVE5nKbs8mArsEBKlaA0lt6gCzBEi4XqUw64ZmaqQdFTXSSH7D3kHFoHNIcDXi30EI9flno8c42Qjt9yINhy0phJBOXSJ9rTaDPtUwbPy3aqEf%2BTSqhuIxgqQOGZgdCGqsUN2hoNI9P7veSryUne8nU%2BG9gXH%2BQGTHd2vM7pQsYLSO88fQl8HeslLotAwLMMw9ceQQmPR21SGlKpe5T2CVxif1UpNwkCxUWs20urYB7xTRvd2wWKWCWhqlWaKWzSlytUsDTgWhxeRvAIH0TOYxksPQzSWnv772jhzjJxjSvsjFmB0jSVA%2BuGWQEyF7RvXoEdvD754UiBVcrfDBbwCq3sO7tG8f%2Bwj11q550KOOx9Y5MD1phAmjbC4OUBm0gY9voi2FxYjR9G8pksxjsv%2BcFoOAugztmZBh%2FoEBijsUo2ADUSjAsxD63HbQWZADPLJFPBL910DHTHfqWOlSiv%2BAQUYFh0xmYMqW5TBkHF05%2Bqb2J2WKxs6KJ7Vz%2Bt9B2kGjSorWs2c%2FfwK2CcnZoV8njTXMzUH9aUGlM%2FgWFszn9QFuf9%2BtFZTLkZhy%2BLEXPbGfC%2BaWI0w4azh0AY6pgHTsNBkRLOfCvieYKlctn8EnvZx4NF1OTh2AVIAzQG8Oz8r3zOj2OaYKoLhAYSPvBdiJw9sW0tQTqf%2B213MdC294YrUf2PB7h%2FUjykxJi40s3lOnn%2FgEBTZOQSOz5FwZd8wASQJLDkAON8sidlQ4%2BrfpIsrdqeOETntgLEEFimdxlbF6aF3mGoW0QEni25EUznj9VhfPKAy%2B6qHmj7K7Dok7EKZw4cB&X-Amz-Signature=91414e52a439960012c4e65c228d91b6b9ad485425e6c8c412d63002aeacab28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466277QC4ZS%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T153807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAH7e4dRc6KPOMytFD4Ubb2W8t2whQTZghgyt09JXKZHAiBW6Se00ZjF6sw2IiYZciRHQ7EKyo8qqAi3bpc5HMCPiCqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl%2BneNDGxxxS3t9O8KtwDeyseFh8wdCrUJJ62pj2c8e1xbsaYStI1Ee2wbcB1acgdNyGPWHUCVE5nKbs8mArsEBKlaA0lt6gCzBEi4XqUw64ZmaqQdFTXSSH7D3kHFoHNIcDXi30EI9flno8c42Qjt9yINhy0phJBOXSJ9rTaDPtUwbPy3aqEf%2BTSqhuIxgqQOGZgdCGqsUN2hoNI9P7veSryUne8nU%2BG9gXH%2BQGTHd2vM7pQsYLSO88fQl8HeslLotAwLMMw9ceQQmPR21SGlKpe5T2CVxif1UpNwkCxUWs20urYB7xTRvd2wWKWCWhqlWaKWzSlytUsDTgWhxeRvAIH0TOYxksPQzSWnv772jhzjJxjSvsjFmB0jSVA%2BuGWQEyF7RvXoEdvD754UiBVcrfDBbwCq3sO7tG8f%2Bwj11q550KOOx9Y5MD1phAmjbC4OUBm0gY9voi2FxYjR9G8pksxjsv%2BcFoOAugztmZBh%2FoEBijsUo2ADUSjAsxD63HbQWZADPLJFPBL910DHTHfqWOlSiv%2BAQUYFh0xmYMqW5TBkHF05%2Bqb2J2WKxs6KJ7Vz%2Bt9B2kGjSorWs2c%2FfwK2CcnZoV8njTXMzUH9aUGlM%2FgWFszn9QFuf9%2BtFZTLkZhy%2BLEXPbGfC%2BaWI0w4azh0AY6pgHTsNBkRLOfCvieYKlctn8EnvZx4NF1OTh2AVIAzQG8Oz8r3zOj2OaYKoLhAYSPvBdiJw9sW0tQTqf%2B213MdC294YrUf2PB7h%2FUjykxJi40s3lOnn%2FgEBTZOQSOz5FwZd8wASQJLDkAON8sidlQ4%2BrfpIsrdqeOETntgLEEFimdxlbF6aF3mGoW0QEni25EUznj9VhfPKAy%2B6qHmj7K7Dok7EKZw4cB&X-Amz-Signature=6bdeaea9efccecfa8341fb96c66f18bca1e10cbbae4f07a1ea4f6592f7436695&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







