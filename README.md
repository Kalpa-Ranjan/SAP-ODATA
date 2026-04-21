



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN2WODGJ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T072738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIHWmg9uvD6EZLTbCFe3zNfby3Q%2FaqZi2RwA8e6ESVQuYAiBodIdCCwvVKArWS%2FGC2WcXuw46sP507j22SU%2BQ7X73fSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMruD8MWzz416i6EqlKtwDztn0bbO5Ek2Rdmc5LOb8MbPE0FDW%2FgvQuS5w%2BjWuolFGRzNijkeyoTYJzOpmRHxkjvjJrSV9LCYVyn3FZBUcHGgtceqj0G9NkQoGeIVYGzDb7lsMU6Yw7po61gXVxvMPuHic8b%2BA%2B1fnQ9jlCBd8%2Fb3CNMQHwLnZk17wxV8BnuTQcWze4N3q%2Bc676e4zTQ5YqJnYNXmF3NbOf2r8WhNzpz%2BX9MYnvtJGquUQDOgrDMYj2viWBQg038IGi%2BI2uQqBYyLgdfua04QfFn6Gol8FSt7%2FZlF2Huw4uI1TZDj4gekH847YFqrA4Z%2FRHnvxcPOGg%2BOddTX7tyagyH%2Bom2CBB%2BZCyF3fYiHfEK0q6wz3aW3vDw%2Fb%2FsQiMtK9qXV43uu3lM%2F%2FxAwryZmPRayZYH5wTk9esJbsw4UyI9zuweAtfX9Zs4fUloECUwoUbAwCLIxP5xR9eBEPM8mdV3tKP%2FDTg%2BhN5Xl83EPD9LH9q%2B98NYKRf8c3TM0EO5yWL46ogorPlYSrpq%2FRavRfstUpGgWNGIEH7wfH6IS84mw9XGhAke09H7xlLmP%2FGBa%2FyPzuXqIfuh2EEl%2FPmr94baWuRHqaZQceGM5dZ8y5B56k0XxoEuu6SLlz1DIpcE9oMF8wzq2czwY6pgEKNlRquCBX41IbxLc9XONYndjYlW%2Fp0xRUlxkeDUAtf3h%2FITQwsLK3LDIj37RVEESytcj6sB4pdHuagJXKGxBpFAVhQRYQBBzElXja%2FNgSRr90Bwv5ZB6hOGhDbgVN%2Bv4EcoA1KyYJzRktDPoLq0MGxCFdC099%2BDgb2TGZlJiUPPizMc42qlHgPDjmI60FBgmt6cpj%2BJJU9yDBk4N49hRmBOxmmsET&X-Amz-Signature=d0be47e6898395b82a75c1b603be3ee85df29fb4b415d7633bfe11a7606d6d76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN2WODGJ%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T072738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIHWmg9uvD6EZLTbCFe3zNfby3Q%2FaqZi2RwA8e6ESVQuYAiBodIdCCwvVKArWS%2FGC2WcXuw46sP507j22SU%2BQ7X73fSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMruD8MWzz416i6EqlKtwDztn0bbO5Ek2Rdmc5LOb8MbPE0FDW%2FgvQuS5w%2BjWuolFGRzNijkeyoTYJzOpmRHxkjvjJrSV9LCYVyn3FZBUcHGgtceqj0G9NkQoGeIVYGzDb7lsMU6Yw7po61gXVxvMPuHic8b%2BA%2B1fnQ9jlCBd8%2Fb3CNMQHwLnZk17wxV8BnuTQcWze4N3q%2Bc676e4zTQ5YqJnYNXmF3NbOf2r8WhNzpz%2BX9MYnvtJGquUQDOgrDMYj2viWBQg038IGi%2BI2uQqBYyLgdfua04QfFn6Gol8FSt7%2FZlF2Huw4uI1TZDj4gekH847YFqrA4Z%2FRHnvxcPOGg%2BOddTX7tyagyH%2Bom2CBB%2BZCyF3fYiHfEK0q6wz3aW3vDw%2Fb%2FsQiMtK9qXV43uu3lM%2F%2FxAwryZmPRayZYH5wTk9esJbsw4UyI9zuweAtfX9Zs4fUloECUwoUbAwCLIxP5xR9eBEPM8mdV3tKP%2FDTg%2BhN5Xl83EPD9LH9q%2B98NYKRf8c3TM0EO5yWL46ogorPlYSrpq%2FRavRfstUpGgWNGIEH7wfH6IS84mw9XGhAke09H7xlLmP%2FGBa%2FyPzuXqIfuh2EEl%2FPmr94baWuRHqaZQceGM5dZ8y5B56k0XxoEuu6SLlz1DIpcE9oMF8wzq2czwY6pgEKNlRquCBX41IbxLc9XONYndjYlW%2Fp0xRUlxkeDUAtf3h%2FITQwsLK3LDIj37RVEESytcj6sB4pdHuagJXKGxBpFAVhQRYQBBzElXja%2FNgSRr90Bwv5ZB6hOGhDbgVN%2Bv4EcoA1KyYJzRktDPoLq0MGxCFdC099%2BDgb2TGZlJiUPPizMc42qlHgPDjmI60FBgmt6cpj%2BJJU9yDBk4N49hRmBOxmmsET&X-Amz-Signature=9654401f6c527fb6950fb1d53880c6530430ceb1459a15f52c50f0c04a4e12dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







