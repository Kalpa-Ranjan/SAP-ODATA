



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDIYKUO%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T012400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAEd80gEvMxLQkihvEMaCfqmDnW%2BAqZpJPS%2BCj1jed7PAiAD%2FA3bdeWgUm6R2FS%2FhP4BPKn1z1QfGpXYcpbPaIUNPiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcVK%2BtBEeAi7fekaKtwD%2FszgjcIDbgy6qyFluaCJZR44x7ry029UB2TY7%2FW%2FhgxJQXslgT%2B8hJAnX2Hl3%2BB7g3rU70Ldubr2PuKIdIIXsRdx%2Fhg1LsMZWfcHCgdcUtt%2BD0W1f7v6VWgyzTJJ0xgFmIOGMIGCGRpCxdY%2BwCkFTiCCGNeqmbdVV8YjthMuRiUepGOcMi3NueZLSQJI61HPOXD%2BFVDKPDoQnfdRshkUIKLA7Ylacx3deBgcjgV0vOTl8kSsSRZEckRu3%2BjRz6Yh%2FB7fGbXY0OfBGc1UtDhxvbbxRLGQSj1ChOvrUX1%2BTqHCA%2BctEz1WzAjYINqW9hdrFobqbMrP%2BPIsrzNJPWLLxPbUSmlqpR6bhaXMHJy%2FUqwJSu%2BSs3K%2FLiVgdlmszq6lcItKzzQjVqKY%2B008wvXCX%2Bt7HT3S39KpUqQZf%2FBYfdGHJvEES519JPS3vOeNi0Kae18MWNOdS7yPN3l%2BLjNFfA7drI%2BAwyak%2BcfB7xpOuTf07ti%2BYbgsFE1TILtTYDC3mX97BosMj47KryfeF%2Fzc83crUXC%2Fc93rs02fK8BQORz5v6fLF8mEVZ%2B5%2BdPQ22fEVWZla7P7u2HKkAkb9sZIK%2Fj6kI7ian48ss0gUu4O6qMDWLN2t1IWSONUTtIwqebu0wY6pgHCoiXuyQhnpgZcb92DXxSxD0VV2oVDnp2LDL6fz3kHXmcje60hKP43JEC2O3LVA5LesNBSXPBr865HolW6Z3T9Q4Lot2NVyOORrDNBcIZnBYflxMRYIudmHFpyHDSIUJVrgq80afCwMs41BqUiwVWw8A0SbSRzdt26TWTS8Sf6eoXFw33lfgtHbrgOrqKNRLCR2WAeOaEXDunKp4932BSTqFvMoEgQ&X-Amz-Signature=05e00440d8cd030281817830579eeef42390f66eaaf09dfdf385fea65662d605&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDIYKUO%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T012400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAEd80gEvMxLQkihvEMaCfqmDnW%2BAqZpJPS%2BCj1jed7PAiAD%2FA3bdeWgUm6R2FS%2FhP4BPKn1z1QfGpXYcpbPaIUNPiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIcVK%2BtBEeAi7fekaKtwD%2FszgjcIDbgy6qyFluaCJZR44x7ry029UB2TY7%2FW%2FhgxJQXslgT%2B8hJAnX2Hl3%2BB7g3rU70Ldubr2PuKIdIIXsRdx%2Fhg1LsMZWfcHCgdcUtt%2BD0W1f7v6VWgyzTJJ0xgFmIOGMIGCGRpCxdY%2BwCkFTiCCGNeqmbdVV8YjthMuRiUepGOcMi3NueZLSQJI61HPOXD%2BFVDKPDoQnfdRshkUIKLA7Ylacx3deBgcjgV0vOTl8kSsSRZEckRu3%2BjRz6Yh%2FB7fGbXY0OfBGc1UtDhxvbbxRLGQSj1ChOvrUX1%2BTqHCA%2BctEz1WzAjYINqW9hdrFobqbMrP%2BPIsrzNJPWLLxPbUSmlqpR6bhaXMHJy%2FUqwJSu%2BSs3K%2FLiVgdlmszq6lcItKzzQjVqKY%2B008wvXCX%2Bt7HT3S39KpUqQZf%2FBYfdGHJvEES519JPS3vOeNi0Kae18MWNOdS7yPN3l%2BLjNFfA7drI%2BAwyak%2BcfB7xpOuTf07ti%2BYbgsFE1TILtTYDC3mX97BosMj47KryfeF%2Fzc83crUXC%2Fc93rs02fK8BQORz5v6fLF8mEVZ%2B5%2BdPQ22fEVWZla7P7u2HKkAkb9sZIK%2Fj6kI7ian48ss0gUu4O6qMDWLN2t1IWSONUTtIwqebu0wY6pgHCoiXuyQhnpgZcb92DXxSxD0VV2oVDnp2LDL6fz3kHXmcje60hKP43JEC2O3LVA5LesNBSXPBr865HolW6Z3T9Q4Lot2NVyOORrDNBcIZnBYflxMRYIudmHFpyHDSIUJVrgq80afCwMs41BqUiwVWw8A0SbSRzdt26TWTS8Sf6eoXFw33lfgtHbrgOrqKNRLCR2WAeOaEXDunKp4932BSTqFvMoEgQ&X-Amz-Signature=68e8e48a854ccc4218e0f02c74f9de52865137156772e09ed0f55ce34a35d25d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







