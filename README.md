



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FEVKTDC%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T131402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDS5rv%2FMBRIPHLkt%2Bh0YpXCq2EYZEoEolLpuraBt4QOGgIhAPSvxxhQLntOEFbAP1CQCdbIcvDQ1JD%2F2kU0ucEyTBFnKv8DCDQQABoMNjM3NDIzMTgzODA1IgzLgaWnD3%2B1zHtFK3Uq3APIgLPdRRtAlPqxE%2FqHthPN1SEIif1dy1QkRdRXYHCdd2dWM4BhRTZgRLHD2BUs239ahynMcnFiqpNoaRktd%2Bzw9SI52EXA%2B2%2FeKWd4YHitgEgUnj5gLD06bduOcnUhZEfP%2BLqr1Oh%2FZOcyNETYRqfASUXYOf64BTLSRSB7wLbSzRbh%2FP5ePm7qdE8zTT9QncZ1uuN%2BHIca8MUtBlQ%2FgDuRJKNLHrruNuHj6A83Uyvdlgc7NRm9hdYu6xy3irNH7wISr31zGSBQmccc%2F6TyfpJQt14YYy9o%2F9tXUXBkcKGRnxormu2DTvt1Ig9cDzCMazDVs9svClxa7QLJ8nZvjFr30ylbt7dLKS1KMgfL6UnjL0c%2B0XG93g%2BZ4CcJ5Ju3mRSI6tGZ2f8YnMrunXcNxTD42tNWFePf%2BcUzg6hT%2Bh8Gp%2FaEbqjWO7vDmc8ILek6opDugG6QC3DqkAjhcLlsrxcMyifaOZXFAMufbLcYro6vQLhbgmBj3npp4a876xN%2BC%2Fybv1LJ5hu09v%2FCkwz7fT55%2Fh4ADJMkTrpy%2BTdmRkoX80hXQLeANKj6ctNEPp5guB9tC7svEh4oHttyvCnRsNHlVMe9SKqIuawJG3ZKyjMAEMGqZMqHczeoGNN%2B%2FzCekMbQBjqkAezw5jfCsi%2BlfG5NXD40KGzxjqoKmGIIvcmVXi1SZuHJL36Cc3e2Wi8yKaTty78prWRqCfbu2YqpLGNQznc2xoE4NS%2F2bsJUkCOIVg4mlLcbH3WF7%2BffDpYNO5O9p4z%2Bz5U89H4f2SNlA8RqxGFs7xQ%2BdhhkZXp9ybE7FkbOs%2BmuiFidR%2FrsfwKootZuXvNRRO6YVArtFg74p0TZbuPc9lMzpSt7&X-Amz-Signature=2779eb0a77060faa2122d933a75f80c451c02e7ef61b9012a017f799709407fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FEVKTDC%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T131402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDS5rv%2FMBRIPHLkt%2Bh0YpXCq2EYZEoEolLpuraBt4QOGgIhAPSvxxhQLntOEFbAP1CQCdbIcvDQ1JD%2F2kU0ucEyTBFnKv8DCDQQABoMNjM3NDIzMTgzODA1IgzLgaWnD3%2B1zHtFK3Uq3APIgLPdRRtAlPqxE%2FqHthPN1SEIif1dy1QkRdRXYHCdd2dWM4BhRTZgRLHD2BUs239ahynMcnFiqpNoaRktd%2Bzw9SI52EXA%2B2%2FeKWd4YHitgEgUnj5gLD06bduOcnUhZEfP%2BLqr1Oh%2FZOcyNETYRqfASUXYOf64BTLSRSB7wLbSzRbh%2FP5ePm7qdE8zTT9QncZ1uuN%2BHIca8MUtBlQ%2FgDuRJKNLHrruNuHj6A83Uyvdlgc7NRm9hdYu6xy3irNH7wISr31zGSBQmccc%2F6TyfpJQt14YYy9o%2F9tXUXBkcKGRnxormu2DTvt1Ig9cDzCMazDVs9svClxa7QLJ8nZvjFr30ylbt7dLKS1KMgfL6UnjL0c%2B0XG93g%2BZ4CcJ5Ju3mRSI6tGZ2f8YnMrunXcNxTD42tNWFePf%2BcUzg6hT%2Bh8Gp%2FaEbqjWO7vDmc8ILek6opDugG6QC3DqkAjhcLlsrxcMyifaOZXFAMufbLcYro6vQLhbgmBj3npp4a876xN%2BC%2Fybv1LJ5hu09v%2FCkwz7fT55%2Fh4ADJMkTrpy%2BTdmRkoX80hXQLeANKj6ctNEPp5guB9tC7svEh4oHttyvCnRsNHlVMe9SKqIuawJG3ZKyjMAEMGqZMqHczeoGNN%2B%2FzCekMbQBjqkAezw5jfCsi%2BlfG5NXD40KGzxjqoKmGIIvcmVXi1SZuHJL36Cc3e2Wi8yKaTty78prWRqCfbu2YqpLGNQznc2xoE4NS%2F2bsJUkCOIVg4mlLcbH3WF7%2BffDpYNO5O9p4z%2Bz5U89H4f2SNlA8RqxGFs7xQ%2BdhhkZXp9ybE7FkbOs%2BmuiFidR%2FrsfwKootZuXvNRRO6YVArtFg74p0TZbuPc9lMzpSt7&X-Amz-Signature=f8bdd635c385d17acca8293cbbcbaf17e16c68255942f77cdda65ff695c0f375&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







