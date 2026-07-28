



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRW7OHWR%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T135206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXNvgrj6CWSfWWWIG5mavm7OtEXUEJzVNJYdW%2B%2FXfmSAiEAwyX1AgDqLLSxAiv3%2B5TEiQvYSUKxiU5N1uMfOIrFmSEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDNgPvLS48RMQbrdKIyrcA8h1z2Uv0EY9m6yhhitGL63vgiC%2BYAfOuVfRjktOIIIDNTOT6orRGkNwg2VoIXOujvYoa%2BSCvHZAkr%2BsFWrGlenJO%2BfV8nSbfHKhS4RYVjnBpN0jFu6ueuTOyjRK%2Bi6Fx1fDcGfG2AoMkkGCKpk%2BoBMTFQcHEGSrGhCv10h5fNWS%2BVf8YPe1t1rgfbPnRWCrxNyYY3PNi%2BGdTqwGX2HB%2F9jtRq7B%2FMxL0hMFUz3Cy0WmZ5ItZHJztQW9c0I5HOZCJyI%2BCRlZgs1v7AOF0unRsnRlmqqW%2FQTDStpmK0kUamGbRFQSm6cJRESrjvdAV8udTg%2FsL7Tr%2B60IL2zu96AijmmkisLbd8Op1ToAdp4T703JxNOYM2LyNvr9SL3Rx52kf%2FXSSEHYzjNUkY6YSRPgyBY0dakrjaRYObYH68MMejRwwOTqqFCVRrxLwjzOD1yES2KHTJYlJwhGya045HGygjFPzMlkS1PqOCSb0ahsrho1JXsrfjpFrvuiH0d0gEC9SPsaFY0iYgxOqs%2F2nztVHvvygQbWGFuYB8bvf8ktYoV1eRnag%2BIpVoF7TCG1k%2FgxgpS8BeS5eA4kPERVng%2BdbiS5FYRlVWHKLZrPJMLsPeEMcYiePNVXA2fUHuh4MPrUotMGOqUBQSBVEChkraZToFtlfMxj6ghycxqtATsDGKvtcFMe5cIaiejk%2BavelPTjjLkX1H9WcMggctRGpbigU2TdpmlJVzX4S4ZirOMzGSL94pbagGoLfnfxSYezUJuWZJtJxf1VVnPlYfsCwhLD6KDx3iv2ItiBrKpVt0%2BMgsZTs%2FJ5IG3lJhttq42b0bhMZecM98JvJT5Hkp7i1edp%2Fpb6Qoe30ZcvPKlY&X-Amz-Signature=cbc8b7c2f35378308d5fbd58d25ec5912c83847766984074e3a1cc6d1e847bfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRW7OHWR%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T135207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXNvgrj6CWSfWWWIG5mavm7OtEXUEJzVNJYdW%2B%2FXfmSAiEAwyX1AgDqLLSxAiv3%2B5TEiQvYSUKxiU5N1uMfOIrFmSEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDNgPvLS48RMQbrdKIyrcA8h1z2Uv0EY9m6yhhitGL63vgiC%2BYAfOuVfRjktOIIIDNTOT6orRGkNwg2VoIXOujvYoa%2BSCvHZAkr%2BsFWrGlenJO%2BfV8nSbfHKhS4RYVjnBpN0jFu6ueuTOyjRK%2Bi6Fx1fDcGfG2AoMkkGCKpk%2BoBMTFQcHEGSrGhCv10h5fNWS%2BVf8YPe1t1rgfbPnRWCrxNyYY3PNi%2BGdTqwGX2HB%2F9jtRq7B%2FMxL0hMFUz3Cy0WmZ5ItZHJztQW9c0I5HOZCJyI%2BCRlZgs1v7AOF0unRsnRlmqqW%2FQTDStpmK0kUamGbRFQSm6cJRESrjvdAV8udTg%2FsL7Tr%2B60IL2zu96AijmmkisLbd8Op1ToAdp4T703JxNOYM2LyNvr9SL3Rx52kf%2FXSSEHYzjNUkY6YSRPgyBY0dakrjaRYObYH68MMejRwwOTqqFCVRrxLwjzOD1yES2KHTJYlJwhGya045HGygjFPzMlkS1PqOCSb0ahsrho1JXsrfjpFrvuiH0d0gEC9SPsaFY0iYgxOqs%2F2nztVHvvygQbWGFuYB8bvf8ktYoV1eRnag%2BIpVoF7TCG1k%2FgxgpS8BeS5eA4kPERVng%2BdbiS5FYRlVWHKLZrPJMLsPeEMcYiePNVXA2fUHuh4MPrUotMGOqUBQSBVEChkraZToFtlfMxj6ghycxqtATsDGKvtcFMe5cIaiejk%2BavelPTjjLkX1H9WcMggctRGpbigU2TdpmlJVzX4S4ZirOMzGSL94pbagGoLfnfxSYezUJuWZJtJxf1VVnPlYfsCwhLD6KDx3iv2ItiBrKpVt0%2BMgsZTs%2FJ5IG3lJhttq42b0bhMZecM98JvJT5Hkp7i1edp%2Fpb6Qoe30ZcvPKlY&X-Amz-Signature=cd984aad63cbb8c9fc977cfd06cbb2888e4d6706fc25dd957d270123185f6230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







