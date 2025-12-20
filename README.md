



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPLGLRVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T011251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFv4PuyEKgEjh8zIyCB%2BZ9Vdm%2FO%2ByDIAydiqtdO1b%2BmcAiA2Lz601ISYEQu4R1m14xB2UgDOEAw1s1qoblaKfjVqTSqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJkoM%2BtqVCEqL4m%2BUKtwDyJOROhqWUil%2BhhfFdtr%2BNgjo3W%2BXY7XsCMz%2FD3ChO9sjgTh1LFK5nwldZq%2FBz%2Br6ctCvH5fG64aedxeD7j%2FWEJBa64zxeeCNulfI8t4xdqAYn2p7rz82a9bOELbm4D%2FKRTqaZ5czlB2G9cc%2Bta%2Bf%2B7hS12v2eiG4KP9R8IAQFznYEHlY65uAQLzNX4Ekgs7d8f77%2BhGkXNG5I%2ByV6i67%2FGtMbhSDUmi8Npi%2F6tKkSnOGGssrAwf6ZKNaJeCes4QaVos3zNpGsSWk91cetu7TUI1lPkdUCwlXUZ0nHKr253xZOaIpEZSPJwhFUe59tamzV3ulYumjWy3UoN0g8iG1yco5s5KnWgC0Hzv57QyNYL2JQBYp9ff4GYnQj8giuWiPiAcSygdfIWyCRcN1%2Bxnj8EVviDZ7b%2FWHh%2Bzod66FVFa3vv1Mcc3Xe1nxsqqQ89f6BWCxRjs73y4IhBJtbFcQrjrUn8FJeKCeLUjcF%2Fn26W%2FYYeDopF%2B3BwbOKXgNFmscekRpjbyz%2B2t3oxgOWjDUg3ZKDr0rZqOjbX7rGh2jWa%2BJ%2B5%2Bz19VSJfzM170MKDcNR0yNfwaangl0pfBEVvkAsI3zyK3lTIfwXtoC1v7%2BazgBSX2k7Z5T%2FaVV39kw3%2BuXygY6pgEGAjf9LuSfyKZGTcfzjpw5qplRbPwB6vHO4pu16HdSFHs586EManZ61CjySzQbLFWwgRdu3sxO6MdLNqqmLDLcdDChlfbDkTpU7KeIFXUPgfsCaiXNFslG4X60jvdZY%2BH9jkFD4VoPEVbGS6ydjW7iudAO6BwHj%2Be7D5M2hoJRN%2ByzZ9HmvoQ0GUqQsTiUbu8q6gMHxP2YN3z260x1rvx3WLGQ7d4F&X-Amz-Signature=d9b0db766fa43380a0eb3626a8a65bc88bd09384509118edc54b7caf9e32d08c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPLGLRVX%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T011251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFv4PuyEKgEjh8zIyCB%2BZ9Vdm%2FO%2ByDIAydiqtdO1b%2BmcAiA2Lz601ISYEQu4R1m14xB2UgDOEAw1s1qoblaKfjVqTSqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJkoM%2BtqVCEqL4m%2BUKtwDyJOROhqWUil%2BhhfFdtr%2BNgjo3W%2BXY7XsCMz%2FD3ChO9sjgTh1LFK5nwldZq%2FBz%2Br6ctCvH5fG64aedxeD7j%2FWEJBa64zxeeCNulfI8t4xdqAYn2p7rz82a9bOELbm4D%2FKRTqaZ5czlB2G9cc%2Bta%2Bf%2B7hS12v2eiG4KP9R8IAQFznYEHlY65uAQLzNX4Ekgs7d8f77%2BhGkXNG5I%2ByV6i67%2FGtMbhSDUmi8Npi%2F6tKkSnOGGssrAwf6ZKNaJeCes4QaVos3zNpGsSWk91cetu7TUI1lPkdUCwlXUZ0nHKr253xZOaIpEZSPJwhFUe59tamzV3ulYumjWy3UoN0g8iG1yco5s5KnWgC0Hzv57QyNYL2JQBYp9ff4GYnQj8giuWiPiAcSygdfIWyCRcN1%2Bxnj8EVviDZ7b%2FWHh%2Bzod66FVFa3vv1Mcc3Xe1nxsqqQ89f6BWCxRjs73y4IhBJtbFcQrjrUn8FJeKCeLUjcF%2Fn26W%2FYYeDopF%2B3BwbOKXgNFmscekRpjbyz%2B2t3oxgOWjDUg3ZKDr0rZqOjbX7rGh2jWa%2BJ%2B5%2Bz19VSJfzM170MKDcNR0yNfwaangl0pfBEVvkAsI3zyK3lTIfwXtoC1v7%2BazgBSX2k7Z5T%2FaVV39kw3%2BuXygY6pgEGAjf9LuSfyKZGTcfzjpw5qplRbPwB6vHO4pu16HdSFHs586EManZ61CjySzQbLFWwgRdu3sxO6MdLNqqmLDLcdDChlfbDkTpU7KeIFXUPgfsCaiXNFslG4X60jvdZY%2BH9jkFD4VoPEVbGS6ydjW7iudAO6BwHj%2Be7D5M2hoJRN%2ByzZ9HmvoQ0GUqQsTiUbu8q6gMHxP2YN3z260x1rvx3WLGQ7d4F&X-Amz-Signature=3d35945eb50651a7513d6a9f3f46b041f368b48810569967fb2352a6666a8ae6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







