



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHRFBLP6%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T012616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBduhhBhNB53HnfpFps20snElvqRvdLJyCpiO538Fe50AiEAj1kvnXaSZmVsoYJub8u%2BrP0ZHLNsA%2Byh%2FHwq5fUxAswq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNZwoo8fGIwZqKTXRCrcA2EClPSlDup%2F30Niu4UYKwo1eBn4u7i5kLAULSuYw7d3nbGQ%2BMToP9UQWLC6dpEqdvn3fvdiUPCkLyg2Nvd8XIT6OlfJg3kLCzwi4mXHP%2B%2BoKqeecnheaiFUG8GPvfZBgmLEDcXFYVIr4qfra%2BrxEZaMx7kXLvKWnJbtcfA%2FQ5L7hqU3WSvhW8e7hIP1t7frRYDFyydgE4dd9V71ZZ%2BLF4PT%2FrDl%2F%2BxGKjfiW4ownhNnbl29u%2Bnbr8d6elpG%2BrXIGqF5waIzRYbSBiHBqvN%2ByqqN3V2RdfqwBNkBXyteHnQLNOuj8NNB0K8wXqnJDO3tjYSGS0DBDI8Z%2F6HTvET%2FOGhU7dtLTU9dI2wnPVq3I0tre72R09HKE4w7TzgHRxXQW179t3BjfEEgBiPTK9WWPyp%2Fpz3ALpPNcv%2FqEFaPjOz7%2F5%2Fed5jQs%2FD4O5RsmnoxReilcK6LLzJgK6Y2NfsEvVl7O%2BV1p30WReJgFPZkfvfMYh1ic3hmfPWfx3x4YOLzETKZsoio60e5xnAVNjMX1LndXQMBD%2Fm1ws8cgbn8D1obnC2DC3IaN1%2Fo1t%2BT8bFp0kBTi8ZFng1Af3Lge1tpqPmNNVXtIdaH5tvC6faVtsMF3Tmvdq3YEfJTMB9HMPWk5soGOqUBSrz8SgR1gm0eyEBZUWayrB9AMwJW4nd43zv3TY1SYOl50hSX%2BJly34rIWB3tBfkMmJyPYcTbXnPvOgjoA1WubNbeoziyEcwBZRjxcq%2BP3nF%2FzLwWx99mjaiXJbOcjnu6OKTaXOoecWnqcj18Dr8zVQ3OnCB%2BJ28diZwDeCE%2Bto%2Bwq0jGsqTRmqryoT%2Fiz5HKQJqa7JM0SsZ%2FLOWVoaY%2FDKWFlc7N&X-Amz-Signature=927a285f0c8b1aaab9bf0c3d90db5eebcb4638b319785718b92b6e7c7078d3a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHRFBLP6%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T012616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIBduhhBhNB53HnfpFps20snElvqRvdLJyCpiO538Fe50AiEAj1kvnXaSZmVsoYJub8u%2BrP0ZHLNsA%2Byh%2FHwq5fUxAswq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNZwoo8fGIwZqKTXRCrcA2EClPSlDup%2F30Niu4UYKwo1eBn4u7i5kLAULSuYw7d3nbGQ%2BMToP9UQWLC6dpEqdvn3fvdiUPCkLyg2Nvd8XIT6OlfJg3kLCzwi4mXHP%2B%2BoKqeecnheaiFUG8GPvfZBgmLEDcXFYVIr4qfra%2BrxEZaMx7kXLvKWnJbtcfA%2FQ5L7hqU3WSvhW8e7hIP1t7frRYDFyydgE4dd9V71ZZ%2BLF4PT%2FrDl%2F%2BxGKjfiW4ownhNnbl29u%2Bnbr8d6elpG%2BrXIGqF5waIzRYbSBiHBqvN%2ByqqN3V2RdfqwBNkBXyteHnQLNOuj8NNB0K8wXqnJDO3tjYSGS0DBDI8Z%2F6HTvET%2FOGhU7dtLTU9dI2wnPVq3I0tre72R09HKE4w7TzgHRxXQW179t3BjfEEgBiPTK9WWPyp%2Fpz3ALpPNcv%2FqEFaPjOz7%2F5%2Fed5jQs%2FD4O5RsmnoxReilcK6LLzJgK6Y2NfsEvVl7O%2BV1p30WReJgFPZkfvfMYh1ic3hmfPWfx3x4YOLzETKZsoio60e5xnAVNjMX1LndXQMBD%2Fm1ws8cgbn8D1obnC2DC3IaN1%2Fo1t%2BT8bFp0kBTi8ZFng1Af3Lge1tpqPmNNVXtIdaH5tvC6faVtsMF3Tmvdq3YEfJTMB9HMPWk5soGOqUBSrz8SgR1gm0eyEBZUWayrB9AMwJW4nd43zv3TY1SYOl50hSX%2BJly34rIWB3tBfkMmJyPYcTbXnPvOgjoA1WubNbeoziyEcwBZRjxcq%2BP3nF%2FzLwWx99mjaiXJbOcjnu6OKTaXOoecWnqcj18Dr8zVQ3OnCB%2BJ28diZwDeCE%2Bto%2Bwq0jGsqTRmqryoT%2Fiz5HKQJqa7JM0SsZ%2FLOWVoaY%2FDKWFlc7N&X-Amz-Signature=566a7aab774a66a8634fd022ecf60506fbfbbce37449f7897caeae7589d88dcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







