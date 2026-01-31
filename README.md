



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I4BZHKC%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T012756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXFAOnNEDjnoMDpYIHwM4Oay0O%2FIgA0%2Fmvy5bwzDfzNAIhAM7tqf5JKcsjV5G7lbAADxwL467cxR2URmIgMueW4niXKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJEAhTU8dbtVpmJUcq3AO0cKixNI7z8dc8cIbErqqVltk1fkIcqxGQD%2BK0YlNQpqY80OKwg1eYaZmr0TUqVTDW0O%2Ff1%2B3whauB1vsnXDwXO8g%2FKzF0Ro70bbWFsUkaC5I6ddtsMaZ5uEifPXWCO2cDk5kqvNNw6HsbV1j2oUVl7llbSo6DiYZZCCgqjPDQVDdsJLsr5%2Bg%2F8U5%2BfdbObjmgvxp2NdCjOmfCmq2qPI8zHtPu8vNzyBWxfQaIfi3tw2XlCy0VDRzoRWJgo7ju%2FJBtgzCRm8u3USniKRlSUO0JlWocMk09wQXBv14r98U53oIoUy9fFhqkmh8fP%2B2n7R8sp7gOEzIbBYtp9fpKvaYtQMatSgRHqp74fHbfp3cIrWo4rO4Z9VGYi7qeDJ2x6o61yYGY02CQVv6BgNEW7HOunYtDgnTtNYrPv2J7t2y9TfjSj%2FeNTwr44l6K1pnqWztW4%2BBRM0NnlixzFXgiXqQmczkBDJ610RImIzU0eSn52i17T2uqpU3gv5OaksjaxotdNWmzBTL0gs%2FlYxvieZNQv502vLlz6osYuRHnekCieQm%2BRtkFQD%2BLFM%2BvRmE6TMhL9rUCeLoNKkPDsqhhnQ123xamZXBsUFTLX9IZez80YMOHAqn4df4f6TxA%2BjCup%2FXLBjqkAWBr%2BDaHnANQu7PKclQzHbtL0awHEpgkPetex81tbVi2h1Vouw55LidzI3EaZ%2Fsv7hgYPKHxidIxUzB%2BVXl9N69o7pGBG%2F8TOclxIwA85NM52IJBsQesXhnxQ4bExxHYDS2KsQqVjitR85VcT0st84h695tsYzBqosjgSIQbpVqrO1LuYj%2F2RpYswx1weD95Gv1dWr33z8nUwRG87CA5lhWLDTks&X-Amz-Signature=2aaed4d6ddbc357d62edafa00fd33fc8267dddcca5e95ab9fa08fd0b59d1d549&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I4BZHKC%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T012756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXFAOnNEDjnoMDpYIHwM4Oay0O%2FIgA0%2Fmvy5bwzDfzNAIhAM7tqf5JKcsjV5G7lbAADxwL467cxR2URmIgMueW4niXKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJEAhTU8dbtVpmJUcq3AO0cKixNI7z8dc8cIbErqqVltk1fkIcqxGQD%2BK0YlNQpqY80OKwg1eYaZmr0TUqVTDW0O%2Ff1%2B3whauB1vsnXDwXO8g%2FKzF0Ro70bbWFsUkaC5I6ddtsMaZ5uEifPXWCO2cDk5kqvNNw6HsbV1j2oUVl7llbSo6DiYZZCCgqjPDQVDdsJLsr5%2Bg%2F8U5%2BfdbObjmgvxp2NdCjOmfCmq2qPI8zHtPu8vNzyBWxfQaIfi3tw2XlCy0VDRzoRWJgo7ju%2FJBtgzCRm8u3USniKRlSUO0JlWocMk09wQXBv14r98U53oIoUy9fFhqkmh8fP%2B2n7R8sp7gOEzIbBYtp9fpKvaYtQMatSgRHqp74fHbfp3cIrWo4rO4Z9VGYi7qeDJ2x6o61yYGY02CQVv6BgNEW7HOunYtDgnTtNYrPv2J7t2y9TfjSj%2FeNTwr44l6K1pnqWztW4%2BBRM0NnlixzFXgiXqQmczkBDJ610RImIzU0eSn52i17T2uqpU3gv5OaksjaxotdNWmzBTL0gs%2FlYxvieZNQv502vLlz6osYuRHnekCieQm%2BRtkFQD%2BLFM%2BvRmE6TMhL9rUCeLoNKkPDsqhhnQ123xamZXBsUFTLX9IZez80YMOHAqn4df4f6TxA%2BjCup%2FXLBjqkAWBr%2BDaHnANQu7PKclQzHbtL0awHEpgkPetex81tbVi2h1Vouw55LidzI3EaZ%2Fsv7hgYPKHxidIxUzB%2BVXl9N69o7pGBG%2F8TOclxIwA85NM52IJBsQesXhnxQ4bExxHYDS2KsQqVjitR85VcT0st84h695tsYzBqosjgSIQbpVqrO1LuYj%2F2RpYswx1weD95Gv1dWr33z8nUwRG87CA5lhWLDTks&X-Amz-Signature=7b2c62d0a8127dac08b208de60b3035a1f87464e59d2752eb9a31e24d223a9c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







