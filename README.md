



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RMOMG2K%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T190024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIELKyAORvfQSAq0xCQ1feom08d5O2CK8zTJDe8UVbxrdAiEA7aAuX9NnR2lRDaVB%2FIgtiel1YFJSsvuGBXkZajHKjFoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8QJTcMRfs6i3GfOSrcA2AHBcdbxgWohknOuVV0qoo0N%2FxG2Ad87tSPmiuecyGlVCjeh%2F1vrSHQCOjVCbvAwehmegMKuCRvqBYgH1ZykWBXpsgvZj5WrfYdbz2d8%2Fv6AMcQCnZRDvI%2Bqbv2I2oL1nywk6X9yzOV9Rx92VGnr630vklPBIuSdG7LQkht%2FebLNpHMMBuM2vMPxSqb4HeKEjo24DPGFqtCBNChcWRy6STPfpyLK0GzRSzEaiHMOcFg2rSkGNVM%2BpZYIeJ6457CBcAcCUJCmiC3s3TjckvmJmiUwZ%2BD50hnOkeh6gE2TK1JVPcvAss2XoKKYeJ3NFy2r2NdHMXrv%2B%2B3nbnLoHocGxPK2TKUJqpzd9vkoeTkGfL9gqkkID5NyDpmxRH7wIJRDWVpKPcrds7crKXfQRfvxKvGeoG%2BMQvbbsWVw3zQN4RaDoD0X5I1Z1B5tf8HCjVU1ZvKo4KudInewfEfg%2BFlp5sgypgzk0WQfokxh%2Bv%2BKgFCMs9bvafRdysZA%2BEp8iRgjGDVIMUxi79izzcvDodE2N5E2%2BFDKskKf4NbNA1gNroMLAFybKx6fNe084qsqcmPfk2TxVsz1LH1T5un%2BafU0Ga%2FvsBkt7ji83aRQmZ%2F2HpCCr4YwGaXJ5PK0%2FDOMOL0uNMGOqUBjbGNkqqU9OVKJ04O7nWOTjSTgiPQhZikEwS0uQGYCm9qpDe100tkj2brZxL3Wlu5j8vyYroEYRLYvqNhbuT4emzVDEcypanRE1KtbQkFaxyGLr9gCM9rZ5zVBFsZWwZUnT0tgviLxmPWxHdjoDVo76tAqQEmnZu07K5Njcn1fHVVi9zyOBv5%2F%2B3lYwCjMescMDgRJ9xufcm%2B0WBO%2BD7tM1wqsSAB&X-Amz-Signature=4523560ab874212aa4e023daa4b6ca3706e0297f599de3a0800af54df03ea79a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RMOMG2K%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T190024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIELKyAORvfQSAq0xCQ1feom08d5O2CK8zTJDe8UVbxrdAiEA7aAuX9NnR2lRDaVB%2FIgtiel1YFJSsvuGBXkZajHKjFoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8QJTcMRfs6i3GfOSrcA2AHBcdbxgWohknOuVV0qoo0N%2FxG2Ad87tSPmiuecyGlVCjeh%2F1vrSHQCOjVCbvAwehmegMKuCRvqBYgH1ZykWBXpsgvZj5WrfYdbz2d8%2Fv6AMcQCnZRDvI%2Bqbv2I2oL1nywk6X9yzOV9Rx92VGnr630vklPBIuSdG7LQkht%2FebLNpHMMBuM2vMPxSqb4HeKEjo24DPGFqtCBNChcWRy6STPfpyLK0GzRSzEaiHMOcFg2rSkGNVM%2BpZYIeJ6457CBcAcCUJCmiC3s3TjckvmJmiUwZ%2BD50hnOkeh6gE2TK1JVPcvAss2XoKKYeJ3NFy2r2NdHMXrv%2B%2B3nbnLoHocGxPK2TKUJqpzd9vkoeTkGfL9gqkkID5NyDpmxRH7wIJRDWVpKPcrds7crKXfQRfvxKvGeoG%2BMQvbbsWVw3zQN4RaDoD0X5I1Z1B5tf8HCjVU1ZvKo4KudInewfEfg%2BFlp5sgypgzk0WQfokxh%2Bv%2BKgFCMs9bvafRdysZA%2BEp8iRgjGDVIMUxi79izzcvDodE2N5E2%2BFDKskKf4NbNA1gNroMLAFybKx6fNe084qsqcmPfk2TxVsz1LH1T5un%2BafU0Ga%2FvsBkt7ji83aRQmZ%2F2HpCCr4YwGaXJ5PK0%2FDOMOL0uNMGOqUBjbGNkqqU9OVKJ04O7nWOTjSTgiPQhZikEwS0uQGYCm9qpDe100tkj2brZxL3Wlu5j8vyYroEYRLYvqNhbuT4emzVDEcypanRE1KtbQkFaxyGLr9gCM9rZ5zVBFsZWwZUnT0tgviLxmPWxHdjoDVo76tAqQEmnZu07K5Njcn1fHVVi9zyOBv5%2F%2B3lYwCjMescMDgRJ9xufcm%2B0WBO%2BD7tM1wqsSAB&X-Amz-Signature=bf77cb5ed6478f8be11bc9d499baf74be9d3b65b6516fd9111e107c6f60c2f81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







