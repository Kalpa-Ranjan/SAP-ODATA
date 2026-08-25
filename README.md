



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5GM3CTU%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T063558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCgShJ2izftJQyZAfbTeImzFLFOa0KKzzlnAaZYMNpqGAIhAN%2F4MC9V8%2B3Op9r75jDZ61%2BGipWfYyDyMZodev%2BDy8HPKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZWC75dYxwCvymYAMq3APSwKTu4cTv%2BEzRJkY3sT18h9ATzs1dqliSQbvd2r7AbS8QrwoRQMSYXgcmz0F6CqmbDC2PDAZoLYcIPgMbrNr32j6sjkDpJC3fGkUivnxs4G5m0Ula4oaSHW%2BpjK03S4NebOy9jAPlQmAZ3eJtI74CNeQpaVi7F74Ad%2B7K2a3L%2BQNjWGedtP3tjCDY8jSNwAtGQB3ufhO9nF7id%2BSAKzD33TCYk4v%2FjPiHFmWZOUYRfF4JT8TZi53KukPcHzDZbIFUWhm%2BV9tTIlQPmQrDVPywDheCEWGiFjuvXVKVVLulpb2AErFTnnf8uXHcg4i%2BDWNnICateJl6eHVcJaqbA3ZHO3beQPOGtFADK%2F9bVsdTQCZjuE3nRVIFa0E%2BNd2nCO5lThXKh9xtLpo48rrUt5NnQYDZ22%2BkKySrKgaRhNPaTAaTXRLxvSMYd0LMkdYPCFqaTxLv%2FPvBa3V3jmOe1p5FESSrc6KK289VHzwDAIvUPuBSrOtXaEuSVqQb1u5gpMJJNK59kvu2WZvfe4KIxG0E%2BNzhUQejwmOsCnWNK53cMsBzIlIGBgi077sTYwjm4FJH3w09Pwgknr%2BqAfm25nAZ8xF5HxpqDN0Ni9p2jAWG2KxqE142eoheBR7tajCh07PUBjqkATQ5cMoj6Nim7LV2oM3zsr7bcV0FY1Ar78CKheA5D05LASoMiG%2F%2BqOkosm%2BrwhWG%2BmVKmBieUwSFEDxrlPPBw%2BBftYCBMXGxzRTYjyyJPT1OxK0lvDbWa4J7%2FlwpU0O1EdjlTcbomnWU6B9HAaJDzxWhbiT%2BDXDvWRAVMAbuB9OnKfBdGRiKO9cEuutXdMmZGYpWfljk7%2B9H81hh33BjCFkPfBr%2B&X-Amz-Signature=649c59d28ea3458b4e2e385f9d5d198e3d43527f9f30a23eeec88a407b7cd241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5GM3CTU%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T063558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCgShJ2izftJQyZAfbTeImzFLFOa0KKzzlnAaZYMNpqGAIhAN%2F4MC9V8%2B3Op9r75jDZ61%2BGipWfYyDyMZodev%2BDy8HPKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZWC75dYxwCvymYAMq3APSwKTu4cTv%2BEzRJkY3sT18h9ATzs1dqliSQbvd2r7AbS8QrwoRQMSYXgcmz0F6CqmbDC2PDAZoLYcIPgMbrNr32j6sjkDpJC3fGkUivnxs4G5m0Ula4oaSHW%2BpjK03S4NebOy9jAPlQmAZ3eJtI74CNeQpaVi7F74Ad%2B7K2a3L%2BQNjWGedtP3tjCDY8jSNwAtGQB3ufhO9nF7id%2BSAKzD33TCYk4v%2FjPiHFmWZOUYRfF4JT8TZi53KukPcHzDZbIFUWhm%2BV9tTIlQPmQrDVPywDheCEWGiFjuvXVKVVLulpb2AErFTnnf8uXHcg4i%2BDWNnICateJl6eHVcJaqbA3ZHO3beQPOGtFADK%2F9bVsdTQCZjuE3nRVIFa0E%2BNd2nCO5lThXKh9xtLpo48rrUt5NnQYDZ22%2BkKySrKgaRhNPaTAaTXRLxvSMYd0LMkdYPCFqaTxLv%2FPvBa3V3jmOe1p5FESSrc6KK289VHzwDAIvUPuBSrOtXaEuSVqQb1u5gpMJJNK59kvu2WZvfe4KIxG0E%2BNzhUQejwmOsCnWNK53cMsBzIlIGBgi077sTYwjm4FJH3w09Pwgknr%2BqAfm25nAZ8xF5HxpqDN0Ni9p2jAWG2KxqE142eoheBR7tajCh07PUBjqkATQ5cMoj6Nim7LV2oM3zsr7bcV0FY1Ar78CKheA5D05LASoMiG%2F%2BqOkosm%2BrwhWG%2BmVKmBieUwSFEDxrlPPBw%2BBftYCBMXGxzRTYjyyJPT1OxK0lvDbWa4J7%2FlwpU0O1EdjlTcbomnWU6B9HAaJDzxWhbiT%2BDXDvWRAVMAbuB9OnKfBdGRiKO9cEuutXdMmZGYpWfljk7%2B9H81hh33BjCFkPfBr%2B&X-Amz-Signature=cb57a1c5ee25233460780371799d944ea3fe30cd4bdf264f434b2f008f70bc49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







