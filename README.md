



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QUMNP4M%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T022729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFn2uxtAMEyBmDO%2FmZPu3hhuIHZB9B6oSIWHK6Bnh447AiBperZo7jLP2ze0A%2BE5xfUGbszFy3X9VuuD5Ut0Jsy7LCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMV3rw6fehHmTE2cMUKtwDSGH1EWnJbwy6yO51z9uOd4luEyghSZ5am%2F9On4PD3aDq9zxDS0LvIduxGR4I1lIvlMOTE3qOC%2FROZXGexW59znuIO%2B4qFh7Nk%2FDv4Svji%2FWvnEHCS29f5rDYD4gmOofZ0z3CGNsNZCPTaklceXaKW%2BJE7VVHwAW5x6A15QttCRpWupPLu8TADW3PUYQgzCOHyNgZPkgtuFk%2BVsJV2MBaKJA8z3nwVSYUsdM05QbV0GmooVPgGIw0w02uykSFU06460omqZysRtGoYibADTAQIyDdgTrSAEAOA%2B%2Bf%2B4bfbDgiFzvKP%2BQ2JuSwg1UZHukXQBxBj7c6WTxjcCNyG5QJElECoE7gQFZt3Ah9OK%2FOv6rt4t1XxC%2BftIn4Zf8rCvg0S90TMN6JzG%2B%2FwdxN4qRFBjzqF5hhSRPSwzK61MWmLlmnIS7RAqX9FqeSljCjZcIcJRbnizzuKy2T6T%2BqV8TMqYQsQeExNis5d%2BMR2B4TPNQwNCMh0l9elrNKuiIyycE1aYBush9T7qSkhy%2FKMXdxbb8nEySwgN8AEUEOt6yuhTUWvXUWPaH41OfLbfem3448khyfCuNXsfFesoCwo5seI0tACxYMVcd6flGS2GOakLoMmoirTD0qB1bFHFIw1vffzwY6pgHP%2BiL38oX06wL17JM0%2BFQM3KBDC%2F9aTvXhYjIKRdEk81OrYEbGg4Wpj%2Bg9Eqapui2BeroZiVSf1cFbt5Ev2uaICXVbIf%2BF8yer6VumNxfuIIP5gyiAFlHkSf0Wel1ZBMuUz1bIaVuuBZ04oE6GgVaZ31XeRnaztCDzPE%2Fl44sblpitl2VIJ6HSDxGB1PmgmZtXP5RID2S%2BU3zte0vSAaPDJInj3aiv&X-Amz-Signature=b4f937d953ba3070dc7632c24bb5364459fb000aeab0ff724bc1173ad715e0f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QUMNP4M%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T022729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFn2uxtAMEyBmDO%2FmZPu3hhuIHZB9B6oSIWHK6Bnh447AiBperZo7jLP2ze0A%2BE5xfUGbszFy3X9VuuD5Ut0Jsy7LCr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMV3rw6fehHmTE2cMUKtwDSGH1EWnJbwy6yO51z9uOd4luEyghSZ5am%2F9On4PD3aDq9zxDS0LvIduxGR4I1lIvlMOTE3qOC%2FROZXGexW59znuIO%2B4qFh7Nk%2FDv4Svji%2FWvnEHCS29f5rDYD4gmOofZ0z3CGNsNZCPTaklceXaKW%2BJE7VVHwAW5x6A15QttCRpWupPLu8TADW3PUYQgzCOHyNgZPkgtuFk%2BVsJV2MBaKJA8z3nwVSYUsdM05QbV0GmooVPgGIw0w02uykSFU06460omqZysRtGoYibADTAQIyDdgTrSAEAOA%2B%2Bf%2B4bfbDgiFzvKP%2BQ2JuSwg1UZHukXQBxBj7c6WTxjcCNyG5QJElECoE7gQFZt3Ah9OK%2FOv6rt4t1XxC%2BftIn4Zf8rCvg0S90TMN6JzG%2B%2FwdxN4qRFBjzqF5hhSRPSwzK61MWmLlmnIS7RAqX9FqeSljCjZcIcJRbnizzuKy2T6T%2BqV8TMqYQsQeExNis5d%2BMR2B4TPNQwNCMh0l9elrNKuiIyycE1aYBush9T7qSkhy%2FKMXdxbb8nEySwgN8AEUEOt6yuhTUWvXUWPaH41OfLbfem3448khyfCuNXsfFesoCwo5seI0tACxYMVcd6flGS2GOakLoMmoirTD0qB1bFHFIw1vffzwY6pgHP%2BiL38oX06wL17JM0%2BFQM3KBDC%2F9aTvXhYjIKRdEk81OrYEbGg4Wpj%2Bg9Eqapui2BeroZiVSf1cFbt5Ev2uaICXVbIf%2BF8yer6VumNxfuIIP5gyiAFlHkSf0Wel1ZBMuUz1bIaVuuBZ04oE6GgVaZ31XeRnaztCDzPE%2Fl44sblpitl2VIJ6HSDxGB1PmgmZtXP5RID2S%2BU3zte0vSAaPDJInj3aiv&X-Amz-Signature=3812ea3f711f3a16041773a4a81300228cf78b02ad5d3a771a4d0ebd6d64cc89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







