



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIUYSOHP%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T093723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8RpOHSxPoqhVkkqZilLsMtqlOoGj3K%2BS8d8VDGGUq%2FAiEAvZqdSWQILRnzgT9ksHl6RtFCDM0lzlYu0rG3TCEcV2Yq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDHvXruca1F1MXvamIircA%2FZkDUI1FtN9%2BjanEe5DoJRG4GSADjMFkvkbUSh%2FF1HNUtQp2fgQzJnz9KeujpEBagb%2Ffkt78aqcE1wgyDoNTHmNKa0aEPdv41lVbq8dm3sx0USvVdBGpMG%2BAYbwPvJmgmSJLwCy66LRS2ZNeNiEHtKG%2FWnuXxsXPkN1%2FG3IIu1TiFl008vsyMN7vycumCK3lYqXkezohE2%2B9RkV7Bmoj9tppcVnxzRwhBiNtUMBwnJ2NqpqRhNjCbgy6PJz1eKD1DvfsmxZ4fkREEZs9MYaeGXTTeMnDS9A2ltpjkcQ5%2BgBYCjacDbeLsBXB8U5KnxTq%2B1a7e1dHNrRzVxLth3Pj88%2BxpyI1lxTCsVDAKLZ2hCnI3NNaYRl1nEAScw4IOJ3A6ROWLSzISAFWXX83uqrOPmKLTF0sXHw9UwUZTclso3UppB%2Ffx0BEuDkiGFE7DwnFmUF1oBoBfZkaWVR2amuYgIsiBD0qHJhmFlgEuBx2At%2BfRksTL6UEiBTGX%2Fgjp%2Fr9cVcNAaxqNwyAFQJjRPhoWk0o56CbHWOvn6VJLJ12MUM7bzORg58F%2FyatPn0AbwoLk%2FfPHzGsdvwOzJJIYqvTPkkFMX6Fwlera01xLVx9OeweQzedl4mg4JTg2xUMIaQitEGOqUBc0F848N4oHkpGnv825uOsXav3s9RGwmYYydSPukIGIgbZHIWSJNn1CAa7w%2B5eqLlhyuw5WoQC7dadSpL59UEga8Ipd%2Fllzz91TNPkhipZyCiRWX8xA9vJOmRTfiCdV65Gwg9GXgJ%2FvPhmJwGVcJvD8498HxTayvOdQTKneqYKYzsQTVSNbw5tVMEtxz%2F3QP2Lvb9zENHq0MJBXH5x%2BjF8c74U15j&X-Amz-Signature=711424d5b4e170e6689eb31cb841ff02cceae2c6d0ad1e479984566f6fe2489f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIUYSOHP%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T093723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8RpOHSxPoqhVkkqZilLsMtqlOoGj3K%2BS8d8VDGGUq%2FAiEAvZqdSWQILRnzgT9ksHl6RtFCDM0lzlYu0rG3TCEcV2Yq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDHvXruca1F1MXvamIircA%2FZkDUI1FtN9%2BjanEe5DoJRG4GSADjMFkvkbUSh%2FF1HNUtQp2fgQzJnz9KeujpEBagb%2Ffkt78aqcE1wgyDoNTHmNKa0aEPdv41lVbq8dm3sx0USvVdBGpMG%2BAYbwPvJmgmSJLwCy66LRS2ZNeNiEHtKG%2FWnuXxsXPkN1%2FG3IIu1TiFl008vsyMN7vycumCK3lYqXkezohE2%2B9RkV7Bmoj9tppcVnxzRwhBiNtUMBwnJ2NqpqRhNjCbgy6PJz1eKD1DvfsmxZ4fkREEZs9MYaeGXTTeMnDS9A2ltpjkcQ5%2BgBYCjacDbeLsBXB8U5KnxTq%2B1a7e1dHNrRzVxLth3Pj88%2BxpyI1lxTCsVDAKLZ2hCnI3NNaYRl1nEAScw4IOJ3A6ROWLSzISAFWXX83uqrOPmKLTF0sXHw9UwUZTclso3UppB%2Ffx0BEuDkiGFE7DwnFmUF1oBoBfZkaWVR2amuYgIsiBD0qHJhmFlgEuBx2At%2BfRksTL6UEiBTGX%2Fgjp%2Fr9cVcNAaxqNwyAFQJjRPhoWk0o56CbHWOvn6VJLJ12MUM7bzORg58F%2FyatPn0AbwoLk%2FfPHzGsdvwOzJJIYqvTPkkFMX6Fwlera01xLVx9OeweQzedl4mg4JTg2xUMIaQitEGOqUBc0F848N4oHkpGnv825uOsXav3s9RGwmYYydSPukIGIgbZHIWSJNn1CAa7w%2B5eqLlhyuw5WoQC7dadSpL59UEga8Ipd%2Fllzz91TNPkhipZyCiRWX8xA9vJOmRTfiCdV65Gwg9GXgJ%2FvPhmJwGVcJvD8498HxTayvOdQTKneqYKYzsQTVSNbw5tVMEtxz%2F3QP2Lvb9zENHq0MJBXH5x%2BjF8c74U15j&X-Amz-Signature=6d9d828e31e5dcaef878bc46b850ceeb8c3e515f17a443f005a96dea642123b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







