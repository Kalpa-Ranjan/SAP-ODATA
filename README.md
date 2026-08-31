



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z26URXTN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T221815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCM%2BjYp581W7xuel5grieScSkQxUKC88RNgl0FMS2UkhgIgXUtu%2F%2BVqKmBhR2psUHjU1n7rdK474sal7Wt3rFCT7xoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBLGz0AogJh3PdvbyrcA%2FO4Pr%2FRx%2BInCwnzIne3FpNqSd9%2Fit7ihHknuIJ8w5N%2FXxk0PQ0GRauRG52aXU8bYm0A31FIcDGGcRhgdX4R2u1BRC%2F%2FLkKOV01ESYe%2BxrWH1NmoL%2B8bc7xZxY31ClbjewYa%2Fk767DvqaIHIU93Wh0vrAQtvfemw4OYAI1xzaoV5DjazQ0F4dXPjySv9kNgTHMJc1GnIoThczm1wK5OLtDcvJreACrlSdqkZGB5MLFCjCTkSRIxU5OMorDMlWQQyhvv3q6BfKO6OLxk%2Bg%2FRPzN8jpOba0SxxN1OqQgP%2FZRN81CY1lbrDgIHOEIt%2F7HSPZEXWT%2B4K1ncH1QCUmohxaHqlKZiW1XK4W6DaueJ5uI%2B%2BA9lluNamGQwxhxQZ3RB7eJJGY4RyzUtqu33ACQysQAdek0krqQpTHTeX0IQBW1XdrZNrwLM%2B7bUE2eXOryQ4Knyzl8%2F9qYy4nflDMnypWbUMjyGBg3hZOkRFntdBeCI%2BMOkdaVA27xRQqGXhUExIwIb6ikwSCMo5NmueD45BzS%2BLcB%2FsvHP8ZipCF1dxnliopc2h8m1W7WEHvDUWXzFeBX0Jq7GybvU5%2FPpYTgoL%2FuTqJzTtIjW2TT4JovNr8%2FsWz%2F7WLvNjtQ7iNMP0MJjx19QGOqUBcl2Gaf1a8bYdli3O1nw4w96Z7EzSgcLb9%2FvSuhdvzWG2v0dWqe9PgFYW%2BecswRWDb%2BbfQ79ZeO%2FlPQsbv01UbghDAA%2BW9LFIaxu78wzztr6tNXxch3sJxvhgF4U3Hl%2BIKJdxmmzFytp4FTN2lzuei1IZFg74Pe54g8rE%2BBT2r8XyqRBUuKonSm5n4DgbS4TcZI970EXsygdsiAiNdJ0H3JsRRW1G&X-Amz-Signature=43603438307b885bb80b3bc04475e20e0b200c44fed1f5b7e3b8348254aa7b4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z26URXTN%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T221815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCM%2BjYp581W7xuel5grieScSkQxUKC88RNgl0FMS2UkhgIgXUtu%2F%2BVqKmBhR2psUHjU1n7rdK474sal7Wt3rFCT7xoqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBLGz0AogJh3PdvbyrcA%2FO4Pr%2FRx%2BInCwnzIne3FpNqSd9%2Fit7ihHknuIJ8w5N%2FXxk0PQ0GRauRG52aXU8bYm0A31FIcDGGcRhgdX4R2u1BRC%2F%2FLkKOV01ESYe%2BxrWH1NmoL%2B8bc7xZxY31ClbjewYa%2Fk767DvqaIHIU93Wh0vrAQtvfemw4OYAI1xzaoV5DjazQ0F4dXPjySv9kNgTHMJc1GnIoThczm1wK5OLtDcvJreACrlSdqkZGB5MLFCjCTkSRIxU5OMorDMlWQQyhvv3q6BfKO6OLxk%2Bg%2FRPzN8jpOba0SxxN1OqQgP%2FZRN81CY1lbrDgIHOEIt%2F7HSPZEXWT%2B4K1ncH1QCUmohxaHqlKZiW1XK4W6DaueJ5uI%2B%2BA9lluNamGQwxhxQZ3RB7eJJGY4RyzUtqu33ACQysQAdek0krqQpTHTeX0IQBW1XdrZNrwLM%2B7bUE2eXOryQ4Knyzl8%2F9qYy4nflDMnypWbUMjyGBg3hZOkRFntdBeCI%2BMOkdaVA27xRQqGXhUExIwIb6ikwSCMo5NmueD45BzS%2BLcB%2FsvHP8ZipCF1dxnliopc2h8m1W7WEHvDUWXzFeBX0Jq7GybvU5%2FPpYTgoL%2FuTqJzTtIjW2TT4JovNr8%2FsWz%2F7WLvNjtQ7iNMP0MJjx19QGOqUBcl2Gaf1a8bYdli3O1nw4w96Z7EzSgcLb9%2FvSuhdvzWG2v0dWqe9PgFYW%2BecswRWDb%2BbfQ79ZeO%2FlPQsbv01UbghDAA%2BW9LFIaxu78wzztr6tNXxch3sJxvhgF4U3Hl%2BIKJdxmmzFytp4FTN2lzuei1IZFg74Pe54g8rE%2BBT2r8XyqRBUuKonSm5n4DgbS4TcZI970EXsygdsiAiNdJ0H3JsRRW1G&X-Amz-Signature=555b6625716a9c9d4ce5edb450582a2bdff8dbfaadc11bb8c5fc7aa927d57cb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







