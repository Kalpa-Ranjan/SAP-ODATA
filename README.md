



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNFUVA35%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T061325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIBeBDRnLJozf0K535zUXta0FoIqMYVFceqzXpoZHxBttAiEAgRpSNIMizVopr8XwT3f%2By%2FyaBggPtBEVO2UVZWuSmKwqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFokAP6NBGbQJA4jsSrcAyXnP16Ivv3UigalkSGKj1HQVR6UwUOzuP1uT2fqdiaYnXa78knWi6u%2BLKMrUVbiCX1LXm9eqVYZuI0sMkY4CRZxTAUmlLpnvAuMa92mTHhtBHKVS9vFnSr6iTanzf0zLNx8iTVW8Vq%2BqywDTg7E%2BAtQsv8RC0bXp%2FoFlYl7X76CeGVyjvI62ALFmQEY%2Fw6GfrFh%2BpWZzGOZwW0V1Ubwu40MXWvXTpqF6idD%2Bc7ajntqCtGU7VU%2F5CAHRd7aSPTrJkn3BFINFkHI%2FP2N4P7UwFXaiVVP%2BmlTLe2acN65FoxkmEvZSs3IjhlaK9vAwxzftg87xMYCvHQgub0osQpSH8x9wV%2BbHI8LyoTcGVRFGYRQMwCS9bP%2FsJtaXjIKu3%2B9hJLF%2FWi%2BTAHjjIxR0IiMvIGwaP%2FQ%2Fl2Qcagqdzf4YyogW1AFZ0lVhk0Pe5pnsuPzY%2BBs3GkfKogM%2BcIJEOF8NnJi6s2Km8aBT9YVTNcdU132kl0n3b6zCYwA6A8zLa8oBuu8TFAYvU2E2E%2BERqPSmOapasuqfKkVSFd%2FW9ICzLstT3XsPrH%2BkBYM2njUtd1%2F9bfmNREIiuVrIx%2BKRaTli4TmBUsu%2BTxroA7egMJRL9pfcNXTD3MLUZJ9rH5NMKeXgNcGOqUBwsE5zz1Ti1yayzRSa%2BtNI2ciuB0%2BeEkhZiK5%2BNY4RtCrar9w2OGTQoBjllnepmg4Wkt%2FHWt4f7yWqbcSDK1fDDwZlSL0QgW%2FguueaPIL48Jm66e8YFvFiKx9%2FLC4snwme2XRnkjbGaqI96qj5JgPG4HXBxGyUYrzHPmYZQwSVKiRW1PoB2WoCEe8VoFwuQaIjw8aCzSPkvM9w2lIYlo1bZVaFKld&X-Amz-Signature=1647b9ee0c849d5cc9863334199a3c1e5a2f6883eefdd69afba6b69d23df84bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNFUVA35%2F20261027%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261027T061325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIBeBDRnLJozf0K535zUXta0FoIqMYVFceqzXpoZHxBttAiEAgRpSNIMizVopr8XwT3f%2By%2FyaBggPtBEVO2UVZWuSmKwqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFokAP6NBGbQJA4jsSrcAyXnP16Ivv3UigalkSGKj1HQVR6UwUOzuP1uT2fqdiaYnXa78knWi6u%2BLKMrUVbiCX1LXm9eqVYZuI0sMkY4CRZxTAUmlLpnvAuMa92mTHhtBHKVS9vFnSr6iTanzf0zLNx8iTVW8Vq%2BqywDTg7E%2BAtQsv8RC0bXp%2FoFlYl7X76CeGVyjvI62ALFmQEY%2Fw6GfrFh%2BpWZzGOZwW0V1Ubwu40MXWvXTpqF6idD%2Bc7ajntqCtGU7VU%2F5CAHRd7aSPTrJkn3BFINFkHI%2FP2N4P7UwFXaiVVP%2BmlTLe2acN65FoxkmEvZSs3IjhlaK9vAwxzftg87xMYCvHQgub0osQpSH8x9wV%2BbHI8LyoTcGVRFGYRQMwCS9bP%2FsJtaXjIKu3%2B9hJLF%2FWi%2BTAHjjIxR0IiMvIGwaP%2FQ%2Fl2Qcagqdzf4YyogW1AFZ0lVhk0Pe5pnsuPzY%2BBs3GkfKogM%2BcIJEOF8NnJi6s2Km8aBT9YVTNcdU132kl0n3b6zCYwA6A8zLa8oBuu8TFAYvU2E2E%2BERqPSmOapasuqfKkVSFd%2FW9ICzLstT3XsPrH%2BkBYM2njUtd1%2F9bfmNREIiuVrIx%2BKRaTli4TmBUsu%2BTxroA7egMJRL9pfcNXTD3MLUZJ9rH5NMKeXgNcGOqUBwsE5zz1Ti1yayzRSa%2BtNI2ciuB0%2BeEkhZiK5%2BNY4RtCrar9w2OGTQoBjllnepmg4Wkt%2FHWt4f7yWqbcSDK1fDDwZlSL0QgW%2FguueaPIL48Jm66e8YFvFiKx9%2FLC4snwme2XRnkjbGaqI96qj5JgPG4HXBxGyUYrzHPmYZQwSVKiRW1PoB2WoCEe8VoFwuQaIjw8aCzSPkvM9w2lIYlo1bZVaFKld&X-Amz-Signature=9f27a35287007b60c71d5d3171410628ba9f3c50fe291d858cba4a6f641eb152&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







