



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNZ4DVP6%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T062945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH31Q1dlZ%2BQ7mjtaNeu8DWWl6OP5Ui5welZJWUg7XpH5AiAwBDP6j10DPFweNLzsg0dGnAjrCUD%2BFMkwg4je%2FOzXfyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMU%2B14yUalhaOPVP0%2FKtwDCUwJE5iqT1Ve1pZl2cC0DK1str57r%2BsiE6lYlgT40y1urJt2%2FBih%2FDW9%2F1MG45oUgdtyECTMu4OE4RUtmQ0eyCbOvPwXiQuBDWY7apTKCXqEQ9dskwvOzsgB3z3so%2BxtrCYqm9N1j55tHFDEMCVLRmEVB%2Fe%2FUOrzPTDKgvtjtOSIGeuRmeZ9pyXJA3OBNpUlFxh0YL8rXrzfEODIeF%2Bwrz8raExarYf0nL4PTaRddFj9DPSem%2FGbzj4larY2giqSYe6elj7JDro1i2GP0yP3OBSVZtO0rs%2BOK3bPFG5iY5ralYZCZJXYW3%2Bjc1zqkS9t%2BrXPgck2EUtksSlqeJ9ZFoQq4NMCXPjWP0I5R2x6W5eF%2FH0%2Fqbmfv85%2B0iyqJ8g4y0uLCkz76mFpdeqkydxmh6FuALIzkwMzcnZIUEIKQy4A4Gl2%2FZlF9JK1h4gEur%2BCv7E6gStZaogL1%2F%2BcYXiqcuHWdX5lgO0OThkgWDBTI1vxoLASINgyxyIpRRVQD0fZ87153GrSGoHT4vLMlQADvFZ7YdptBSPLZNr1LB%2FJjC6MtIXf%2FWytKz28eTswu%2BvxUqMhJs2dogZ2%2FO7o4UctW5bjyBElJYXfw0LH22bkOaap%2BT%2F09N4Tn7GjMcMwx7PmywY6pgGXX2%2Bf3I6KvCOTyNdyc1X4vY3P47%2FlEPUwSwyfqmVQJEBtRwV1jymNgwF1IiHRE56kiwaYOD0unWjg%2FsW6CmWnzqLwDSM71VM8xa7VsRu60rYpZ81wfEulkPfr7TfpZUSr%2BvEkheUNH2avcyNzWzxK4h3WYsgi0QBJNAl9aUZCRxW6i%2BG6Eir4xiVIMzdJ6UP9fpO1ouqEbeuYiFUp6ScRa0Nsgl3X&X-Amz-Signature=d98cf9bcf313706eeb68f83cc8a962cc37a7b99318c189a3e4105a5d1126c504&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNZ4DVP6%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T062945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH31Q1dlZ%2BQ7mjtaNeu8DWWl6OP5Ui5welZJWUg7XpH5AiAwBDP6j10DPFweNLzsg0dGnAjrCUD%2BFMkwg4je%2FOzXfyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMU%2B14yUalhaOPVP0%2FKtwDCUwJE5iqT1Ve1pZl2cC0DK1str57r%2BsiE6lYlgT40y1urJt2%2FBih%2FDW9%2F1MG45oUgdtyECTMu4OE4RUtmQ0eyCbOvPwXiQuBDWY7apTKCXqEQ9dskwvOzsgB3z3so%2BxtrCYqm9N1j55tHFDEMCVLRmEVB%2Fe%2FUOrzPTDKgvtjtOSIGeuRmeZ9pyXJA3OBNpUlFxh0YL8rXrzfEODIeF%2Bwrz8raExarYf0nL4PTaRddFj9DPSem%2FGbzj4larY2giqSYe6elj7JDro1i2GP0yP3OBSVZtO0rs%2BOK3bPFG5iY5ralYZCZJXYW3%2Bjc1zqkS9t%2BrXPgck2EUtksSlqeJ9ZFoQq4NMCXPjWP0I5R2x6W5eF%2FH0%2Fqbmfv85%2B0iyqJ8g4y0uLCkz76mFpdeqkydxmh6FuALIzkwMzcnZIUEIKQy4A4Gl2%2FZlF9JK1h4gEur%2BCv7E6gStZaogL1%2F%2BcYXiqcuHWdX5lgO0OThkgWDBTI1vxoLASINgyxyIpRRVQD0fZ87153GrSGoHT4vLMlQADvFZ7YdptBSPLZNr1LB%2FJjC6MtIXf%2FWytKz28eTswu%2BvxUqMhJs2dogZ2%2FO7o4UctW5bjyBElJYXfw0LH22bkOaap%2BT%2F09N4Tn7GjMcMwx7PmywY6pgGXX2%2Bf3I6KvCOTyNdyc1X4vY3P47%2FlEPUwSwyfqmVQJEBtRwV1jymNgwF1IiHRE56kiwaYOD0unWjg%2FsW6CmWnzqLwDSM71VM8xa7VsRu60rYpZ81wfEulkPfr7TfpZUSr%2BvEkheUNH2avcyNzWzxK4h3WYsgi0QBJNAl9aUZCRxW6i%2BG6Eir4xiVIMzdJ6UP9fpO1ouqEbeuYiFUp6ScRa0Nsgl3X&X-Amz-Signature=5fd0efe341e5fac4d8109e0c12e509038bb3edc9956b1151fb5ef548c6404966&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







