



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CF5M3X2%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T123334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKOwMljSTWuq12yKqhnFbLA66GEhg8eN%2FIZtk5ivMD8QIhAOspCeU9NEekFvo7T5iHyeVfojskHE%2BNV7%2FB%2B%2BhX%2BZxNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR95IJqsuUSwNeM6Uq3AOjgGQk28ag0nKgForFKfsmFUB21UfR%2BT02dmTML2GG29beVAMOGC2AmwVbwVHuXOun7HQiEojspNtViNAyDQ8%2FqBDI2XkmLTl9uHmk86EGB3CbJ5dvsgrgM9ek8ucaO0u4%2BXJY4OxjBDQaxjeAdEchXcnJR8TcjqPEyYBNPaJBr6IvgyBKxMCTUB2tyrwTbMQ0ngEEL9kKN5%2FWXlCo5%2B5ahg2c3hO5HE6AlbTtSLIOt8juDhdkSQueLmSZ3kEn1DfiIHu25EbUnaqGk3lJc6ZcXbqSBomIcYVygKQapr%2F3PSMiJwIN2%2FLvVWwwbrELJLwZmRPses%2B8CYVLVGFeCIweAheZ7bwGF3NgWxT2DNfRVUb6anu6U9MaEIfYN3d%2Bl9pmdUcfjTcEepGK%2FaVEMrmgkXuHedjtBAdO%2FeW98jjRt3SdDfr%2Fino6A3zJ%2Fr%2BFNPpafCDiKss3K9rcbK6PCEA6GWIpLJ78CXmGs58wPxVSUVJV0SS85p7J713BSknK76Wm7zP73SYeMVrg8KCZreBYnCG53kiqaJYNgj4A3eJzNW2x9XX3sR0f66Z48JZRJJfFzY%2FPUpRRd9JihYKl3I%2FRISIQ%2B5xqVQoJkE4SgjJFv7ab%2B8xU8cZyENtXtjDZuaDJBjqkAex4DGsHkErTuF%2FzPBiUOmrFug%2F1%2Bc3sIK2qdkzsnxIzstinT6kL8PdnGHXUqbx0bEEyS2MqYFUHayZZ3SmbOg5vloZrhnGDFtsPtEyawu%2BVLGEv49UlKqN7qMOovXWO77MSkDfheCiZWt3jBQP4dLt0AvSNNruY3Lf21Bv1LFZlLwZKBT3AMVOB7X9CDfa85LdCUu7uvCeBP%2B2IUFpDCnDqnDoo&X-Amz-Signature=326ceafb42cee452cad0da4a0a3dc83957c69112688a6ab6f058e659c894a274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CF5M3X2%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T123334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKOwMljSTWuq12yKqhnFbLA66GEhg8eN%2FIZtk5ivMD8QIhAOspCeU9NEekFvo7T5iHyeVfojskHE%2BNV7%2FB%2B%2BhX%2BZxNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR95IJqsuUSwNeM6Uq3AOjgGQk28ag0nKgForFKfsmFUB21UfR%2BT02dmTML2GG29beVAMOGC2AmwVbwVHuXOun7HQiEojspNtViNAyDQ8%2FqBDI2XkmLTl9uHmk86EGB3CbJ5dvsgrgM9ek8ucaO0u4%2BXJY4OxjBDQaxjeAdEchXcnJR8TcjqPEyYBNPaJBr6IvgyBKxMCTUB2tyrwTbMQ0ngEEL9kKN5%2FWXlCo5%2B5ahg2c3hO5HE6AlbTtSLIOt8juDhdkSQueLmSZ3kEn1DfiIHu25EbUnaqGk3lJc6ZcXbqSBomIcYVygKQapr%2F3PSMiJwIN2%2FLvVWwwbrELJLwZmRPses%2B8CYVLVGFeCIweAheZ7bwGF3NgWxT2DNfRVUb6anu6U9MaEIfYN3d%2Bl9pmdUcfjTcEepGK%2FaVEMrmgkXuHedjtBAdO%2FeW98jjRt3SdDfr%2Fino6A3zJ%2Fr%2BFNPpafCDiKss3K9rcbK6PCEA6GWIpLJ78CXmGs58wPxVSUVJV0SS85p7J713BSknK76Wm7zP73SYeMVrg8KCZreBYnCG53kiqaJYNgj4A3eJzNW2x9XX3sR0f66Z48JZRJJfFzY%2FPUpRRd9JihYKl3I%2FRISIQ%2B5xqVQoJkE4SgjJFv7ab%2B8xU8cZyENtXtjDZuaDJBjqkAex4DGsHkErTuF%2FzPBiUOmrFug%2F1%2Bc3sIK2qdkzsnxIzstinT6kL8PdnGHXUqbx0bEEyS2MqYFUHayZZ3SmbOg5vloZrhnGDFtsPtEyawu%2BVLGEv49UlKqN7qMOovXWO77MSkDfheCiZWt3jBQP4dLt0AvSNNruY3Lf21Bv1LFZlLwZKBT3AMVOB7X9CDfa85LdCUu7uvCeBP%2B2IUFpDCnDqnDoo&X-Amz-Signature=1caae6a236c3c0ad4953e648efeafdadf0370aede8d9a5afb4bfc8db90ea5bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







