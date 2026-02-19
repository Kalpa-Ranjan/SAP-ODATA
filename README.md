



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGWM2BTH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T065505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDagmMczLaJIWoVXKUot0zf8lRbC4NA3UvoCEtjxbACsgIhAKgmowckZL%2BRWLpnaoGrhxVOgM1zuEu0lkzm2ll%2FNA2lKv8DCHgQABoMNjM3NDIzMTgzODA1IgwNGDX5XqI663j80u8q3AORp2TGcqQrFc0weoHtlOpRbbKjAQE9btlTSkrjVnuiXFEx9%2BAoagX%2FGPAPr33nWlsqRMKH6ndvf30KD1A7%2Feaz18FqRNI%2B5QS50vi8BEu18W5JpEoyTJohxKEZDzVCgjNtLd1IQnwblRN1%2B3ipxE9HZp0ljvx2eFrdVam2U0w3nXbfVkf2dJz4Z5glIUxuRX07e8rGf2%2BeuvRinOg255zSYXRXqu9wE4IKSgzCUUGS8O1woq88aJF571hDVFrraSzfepzrkIJOM08jhSwVgKiDTaBVxiwoZ1B%2FRiW2Lx%2BoHYc9jg3iZhNeOzuWh4Fcww7K6ucWCKTo1C%2Fvcck0n%2FntYV9S0U04o%2BDXd0EPW6N2jdYRsSVEXGa7QyQ%2BV6FMFhvm4MVCENEFyWjxD8AcJAabrfVHdlRrWneoFkkXMex%2BX8XrTnqSiU85dcQodaJczT63lAObMBq5agBqVVsUrAlffcH3ZeRCmX9N77%2BPgStswJMJqZnjMGQVNd37%2F5VtuYKn35ralDTVH5aVxpyGFQEPLuw5G2KFD%2BkQOkWJ5Yn2cdbua2jzg5XMg2KKu899w1KzJhf0eQKG%2FMnRzLyNMfThZ8o1dF2l5RaiTFCsk%2FunViMLOJLc8qiwpJxeijDM3NrMBjqkAf4tgvtNhFYOAgUTgwJ%2BMeCITHYXi1LCVYZC4PkY1aBQ6sfBLWhw01xvPuZ4JNr4PRchuLZ9EpLdO9q2Dfi9oxeHn5w3ewiX0xDYlMRdRL%2F7ymci%2FWVsvIZb2s0N7Gpl9Cq3WsSFQfegZ0otBL%2BOeq6X5lIB68v%2FGe4tRSRWBcl4lhLOdGOUk%2F8gAGL%2FfOxmgERLp9dsBe1cdJzPhkmo17YNS%2FUj&X-Amz-Signature=2cc05fdb1df7075756560660c8c20946b1e165a355f3b916efa17860e954a0eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGWM2BTH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T065506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDagmMczLaJIWoVXKUot0zf8lRbC4NA3UvoCEtjxbACsgIhAKgmowckZL%2BRWLpnaoGrhxVOgM1zuEu0lkzm2ll%2FNA2lKv8DCHgQABoMNjM3NDIzMTgzODA1IgwNGDX5XqI663j80u8q3AORp2TGcqQrFc0weoHtlOpRbbKjAQE9btlTSkrjVnuiXFEx9%2BAoagX%2FGPAPr33nWlsqRMKH6ndvf30KD1A7%2Feaz18FqRNI%2B5QS50vi8BEu18W5JpEoyTJohxKEZDzVCgjNtLd1IQnwblRN1%2B3ipxE9HZp0ljvx2eFrdVam2U0w3nXbfVkf2dJz4Z5glIUxuRX07e8rGf2%2BeuvRinOg255zSYXRXqu9wE4IKSgzCUUGS8O1woq88aJF571hDVFrraSzfepzrkIJOM08jhSwVgKiDTaBVxiwoZ1B%2FRiW2Lx%2BoHYc9jg3iZhNeOzuWh4Fcww7K6ucWCKTo1C%2Fvcck0n%2FntYV9S0U04o%2BDXd0EPW6N2jdYRsSVEXGa7QyQ%2BV6FMFhvm4MVCENEFyWjxD8AcJAabrfVHdlRrWneoFkkXMex%2BX8XrTnqSiU85dcQodaJczT63lAObMBq5agBqVVsUrAlffcH3ZeRCmX9N77%2BPgStswJMJqZnjMGQVNd37%2F5VtuYKn35ralDTVH5aVxpyGFQEPLuw5G2KFD%2BkQOkWJ5Yn2cdbua2jzg5XMg2KKu899w1KzJhf0eQKG%2FMnRzLyNMfThZ8o1dF2l5RaiTFCsk%2FunViMLOJLc8qiwpJxeijDM3NrMBjqkAf4tgvtNhFYOAgUTgwJ%2BMeCITHYXi1LCVYZC4PkY1aBQ6sfBLWhw01xvPuZ4JNr4PRchuLZ9EpLdO9q2Dfi9oxeHn5w3ewiX0xDYlMRdRL%2F7ymci%2FWVsvIZb2s0N7Gpl9Cq3WsSFQfegZ0otBL%2BOeq6X5lIB68v%2FGe4tRSRWBcl4lhLOdGOUk%2F8gAGL%2FfOxmgERLp9dsBe1cdJzPhkmo17YNS%2FUj&X-Amz-Signature=08711f3c1f462437f2e45502ed3cfab1fc36a6d67faa9852e696734054527df2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







