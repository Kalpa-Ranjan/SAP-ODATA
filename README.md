



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626JQNZYR%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T062732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDy54MOUA%2FxGn%2BItZLctWHlIILmUnOWT8ed8O3TfEZUMAIgLshmdM9JGtGxMo0lvaQxhQ9veWz7ZVSPyVtLA%2FEViXYq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDFU4K%2B6cw%2BAw4Vv5VCrcA3%2BUg8KUvhmABQIpJBJyej%2BLdPvh%2FwCd%2B%2BychL679K%2FEY%2B1fj14BBclxS89t2mHEU3Cys9oZLPKvM%2FERhc2Q0mh0F65v%2F31CLqpvPwN7bdiA87L6RYLQMK8t4fGXGFlW3HsEM3ccXVDRDR3eYZzH44Tq5eUAEpI%2BL0yNMySbnEElvjy1HkERxuofp8l7upa9KwDFofNBjQGR5I%2BUlWfBj4clS9fHpH1H3HtZhi4kvOcqTPNUrRw9U7oFAJSTL4Sn4ISw%2FSTPfHZB5fHncSq0prrOfFfd21%2FFFAE2ZIZOiNGt%2Bkt37QM7llS920NRoI4c9i0baSDCJ6G9gEDRMx%2BOXVFZyJ7ZFUhGxtyics5B9olIR37DDivlQe6sCy7BMjWazuYVrzIHt63WqzrPOWUI34on%2FQ54vUnPL8eAjUXzhS%2BMpoPb6vy%2BdYHPoYj1A5GaUc88iwgqvlNNEiFAP5TEFMBtklnvm5fjil0tt9YyNIM%2FvfUbsP2i4MSjeJDODkYTFgf5xaH88u1gqKBtDaiGMYnLatSz5nyjg89XXkQ%2Bnzfl%2BofBa86N6oF0QFMmtr%2FKtSdhfLgOKg9xm3iPbCSP7i%2BKBoYzJoHMVfcA2pbDTfG3RHcOnhfRfPMi6KL7MMy18soGOqUBHl0KQ6TBXNEFLhfHCDUBtTzt1xhTGUpYXYQVRp9SqFrJiJTXMsvE9mOLU27sYEHA2SB8jRkNppFZueiUaekxG1%2ByAnUxn0%2B11aprk6D3yjZiKH3hatBxf%2BqEE7KwsPECo0Anvdfbh3%2BsfWwcipyUB3wDy0hrM2SvSVVHQbHGWvo%2BDcBybZr0tsPZ8Au9mEJtP9J41oJXGjTMUEWgN6F7UwWefIcW&X-Amz-Signature=0c380f354f755c94890787ad484798cba16bbcf9ae48642b50fb1a9ad02620bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626JQNZYR%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T062732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDy54MOUA%2FxGn%2BItZLctWHlIILmUnOWT8ed8O3TfEZUMAIgLshmdM9JGtGxMo0lvaQxhQ9veWz7ZVSPyVtLA%2FEViXYq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDFU4K%2B6cw%2BAw4Vv5VCrcA3%2BUg8KUvhmABQIpJBJyej%2BLdPvh%2FwCd%2B%2BychL679K%2FEY%2B1fj14BBclxS89t2mHEU3Cys9oZLPKvM%2FERhc2Q0mh0F65v%2F31CLqpvPwN7bdiA87L6RYLQMK8t4fGXGFlW3HsEM3ccXVDRDR3eYZzH44Tq5eUAEpI%2BL0yNMySbnEElvjy1HkERxuofp8l7upa9KwDFofNBjQGR5I%2BUlWfBj4clS9fHpH1H3HtZhi4kvOcqTPNUrRw9U7oFAJSTL4Sn4ISw%2FSTPfHZB5fHncSq0prrOfFfd21%2FFFAE2ZIZOiNGt%2Bkt37QM7llS920NRoI4c9i0baSDCJ6G9gEDRMx%2BOXVFZyJ7ZFUhGxtyics5B9olIR37DDivlQe6sCy7BMjWazuYVrzIHt63WqzrPOWUI34on%2FQ54vUnPL8eAjUXzhS%2BMpoPb6vy%2BdYHPoYj1A5GaUc88iwgqvlNNEiFAP5TEFMBtklnvm5fjil0tt9YyNIM%2FvfUbsP2i4MSjeJDODkYTFgf5xaH88u1gqKBtDaiGMYnLatSz5nyjg89XXkQ%2Bnzfl%2BofBa86N6oF0QFMmtr%2FKtSdhfLgOKg9xm3iPbCSP7i%2BKBoYzJoHMVfcA2pbDTfG3RHcOnhfRfPMi6KL7MMy18soGOqUBHl0KQ6TBXNEFLhfHCDUBtTzt1xhTGUpYXYQVRp9SqFrJiJTXMsvE9mOLU27sYEHA2SB8jRkNppFZueiUaekxG1%2ByAnUxn0%2B11aprk6D3yjZiKH3hatBxf%2BqEE7KwsPECo0Anvdfbh3%2BsfWwcipyUB3wDy0hrM2SvSVVHQbHGWvo%2BDcBybZr0tsPZ8Au9mEJtP9J41oJXGjTMUEWgN6F7UwWefIcW&X-Amz-Signature=c0af30b2c088a4804537f8c92f718a389b8dc5bcda188e60e57174172a9cd89a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







