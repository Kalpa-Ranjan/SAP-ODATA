



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMQHUSWS%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T065302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIGdfQLKxPiw8DQO79GXrPDPnNg61L%2FbAQiSscdhyY3LAAiEAlcSMTXjWLZo73Hcjv53wJu2QQt1X1qLotQxsehzp3cEq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDHU3qyglquMkY11sfyrcA2JXchFSdUAjaRWPKxYChNsO4AkFs98kab5Kt5R2JUnmKH8AIWHGQF%2FEwnxAzI%2BYPQxWBLa00sl5%2BYvkQ82YahWnxCRKgptJfCw6ZJYZoFTSJtvlETcJw8EckVJjR6KMfqohdLpDQDOGwC4XlmiQUrYFc5YILDuT54p9j%2F7ItuBuQiOyGJho%2BtgLBmbNv70hRbBRLP1U77X%2BB2cZyFHmjV5NQTwOS6YjCpvSayaJSRZl7PIYJs1yffx0kqAIIq91kf73UirSaJXGHLTjfL%2FTMAuT4HV1kW%2BquBpB84oh3pyyLBOzMLMN%2FtSShmc9X5HgNrQSker4q98LctpnX%2BzpTP0xEblDn1q0c4Lqg2p%2BsDWALH24tdC%2FGDNI26reQNa4RcPBBQtOgxSx0fqaPIKEufwQ9vG0m0pOKWE4kMHejl1U%2BIHgx2YZJkSUB%2FNIsJi6PaJYQUpCTQLBJsZZDuiZ74h84Whu3K3wYvlJwSYNaHkAqkeVL%2BiGXMGKDLOQRFQn50GOHqdyN4pn9DWkC%2FdhVGOXxXlyisEziJiNUlOBY%2BoaKfbKGab7PBHGPWw0oNMiPAa%2BQPt%2BGw2eUKUQ8R9Xu1OFJPDhaQWlTjhDTy5MwcH%2FFiY%2BRVr5Xl6RmmPNMPWO0MwGOqUBbOWwcCAyqdvTMOjSeQcHnXqT87SFZ2D5ExBj9soo8sQP%2BGeUEpEFLEGTULuZvcSxt4JuvqVtJgtrLlAitPhKLp8EffD5Jse8TRd3wS82GvqUdMaRnIGOBsvMbwZv1A16%2BffFRjxhlb7aWh35NjOUWVaMrQ0WtMcQTiOUXqj5u1GcX%2FMaXc%2FNC5un0NRlEHdVDGEbMkbrfRnfd6O4pXdSCmvzxxup&X-Amz-Signature=6742f2fe83a0bc444c6cf5403a769772aa8803203561b76fb320ce52690b04c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMQHUSWS%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T065303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIGdfQLKxPiw8DQO79GXrPDPnNg61L%2FbAQiSscdhyY3LAAiEAlcSMTXjWLZo73Hcjv53wJu2QQt1X1qLotQxsehzp3cEq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDHU3qyglquMkY11sfyrcA2JXchFSdUAjaRWPKxYChNsO4AkFs98kab5Kt5R2JUnmKH8AIWHGQF%2FEwnxAzI%2BYPQxWBLa00sl5%2BYvkQ82YahWnxCRKgptJfCw6ZJYZoFTSJtvlETcJw8EckVJjR6KMfqohdLpDQDOGwC4XlmiQUrYFc5YILDuT54p9j%2F7ItuBuQiOyGJho%2BtgLBmbNv70hRbBRLP1U77X%2BB2cZyFHmjV5NQTwOS6YjCpvSayaJSRZl7PIYJs1yffx0kqAIIq91kf73UirSaJXGHLTjfL%2FTMAuT4HV1kW%2BquBpB84oh3pyyLBOzMLMN%2FtSShmc9X5HgNrQSker4q98LctpnX%2BzpTP0xEblDn1q0c4Lqg2p%2BsDWALH24tdC%2FGDNI26reQNa4RcPBBQtOgxSx0fqaPIKEufwQ9vG0m0pOKWE4kMHejl1U%2BIHgx2YZJkSUB%2FNIsJi6PaJYQUpCTQLBJsZZDuiZ74h84Whu3K3wYvlJwSYNaHkAqkeVL%2BiGXMGKDLOQRFQn50GOHqdyN4pn9DWkC%2FdhVGOXxXlyisEziJiNUlOBY%2BoaKfbKGab7PBHGPWw0oNMiPAa%2BQPt%2BGw2eUKUQ8R9Xu1OFJPDhaQWlTjhDTy5MwcH%2FFiY%2BRVr5Xl6RmmPNMPWO0MwGOqUBbOWwcCAyqdvTMOjSeQcHnXqT87SFZ2D5ExBj9soo8sQP%2BGeUEpEFLEGTULuZvcSxt4JuvqVtJgtrLlAitPhKLp8EffD5Jse8TRd3wS82GvqUdMaRnIGOBsvMbwZv1A16%2BffFRjxhlb7aWh35NjOUWVaMrQ0WtMcQTiOUXqj5u1GcX%2FMaXc%2FNC5un0NRlEHdVDGEbMkbrfRnfd6O4pXdSCmvzxxup&X-Amz-Signature=f16900e8b19725373f43cb71f788a540fd60dadd3919158f76f8fbe2fa494f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







