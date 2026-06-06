



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2NPC3RM%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T132108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDF8WlQo68PqEl%2FyBxQSl57zdTBTDGxQfUHoR623FMMxAiAmtgLyG3bywofiJOHl5aJLkWyge4qc5h4waaCfkoSnyiqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZ0DtuWCpYa70BEuKtwD%2Bf%2FCaMgQ2DmdLVJqnWTyM5X3p5Ew3gXQmS9vdSOhjfJgGSeuJKxi1IE2%2BrkVMO6yHm5m1Kmb4TxwrPjARIEN9P0miAQ9rGdqeBeFR35VKd%2BqIRxRpFO1tEzi0xpsUzsMO0MAoUEcBkVh%2BLprtMqI%2BYwZVT64LPW7NTWhlx2kelE9HUiYwqXH4DAqtjkomC36vw0RZcv7moAIOgc1xmkXGO8ds%2BVhZfb9a%2Fwf40IFKppFXEbK2SjOris5UYj8wjuP35VuJh1%2FxRz6zrs0KacdoXZeVnU32c9jtfyU9V3zN5fYUkEYosJXVxbBWGfE9qeQNPKkNkdw%2B3Z7T9VaJ6EG80BSXkKHvHg2spo1SaCLmQHPwH2F%2FU1wEAsmSn1haLee6lQIsTFCbFQg9E63fExSwUh3icvONTgnWiMPzC86CGuwPZRkCJHQN4SDjtAfvG1vJlYHDs6NDg2WioY2MWOS477os230lb8UsHtqbaUx6DXSSjiNk%2FDK8HVJ99hznIdGDw8woxUt2sTZX3PR7YF3g7f6F%2FTE1iWZM7k%2BZUTESbNA08EgZlZV5YeYBjs4BGsr9OfCAdQZln07a%2FfaWMkJh8KtNnttdnVcSuevZu3GPIWYcW5VmVh731853Rswp4qQ0QY6pgGTdC64PBWNBt%2FQuIAiNk8hsIDXT8nfOVq4VD%2F0u0Nkciv0SlihhJVkiecJn8RBRfr1k%2FSL57TYtOwyAV38fdCSSFm9vk%2BVd2iWJAaHV0%2FpNjH6mvnGgYX0UiMesIrC%2BJf5G%2FFCb94NBDD3yAVmlq2Iyf%2BpTXuclGzb5ny76Y00aQWfRCGpI9vMAmVgPxCklf32QgiF1j%2BHYJmIcgD%2BNQD576MX822P&X-Amz-Signature=a85fcb57c99d9948cd0bea31e370662960fb77b733286575ebfea19cc3200230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2NPC3RM%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T132108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDF8WlQo68PqEl%2FyBxQSl57zdTBTDGxQfUHoR623FMMxAiAmtgLyG3bywofiJOHl5aJLkWyge4qc5h4waaCfkoSnyiqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZ0DtuWCpYa70BEuKtwD%2Bf%2FCaMgQ2DmdLVJqnWTyM5X3p5Ew3gXQmS9vdSOhjfJgGSeuJKxi1IE2%2BrkVMO6yHm5m1Kmb4TxwrPjARIEN9P0miAQ9rGdqeBeFR35VKd%2BqIRxRpFO1tEzi0xpsUzsMO0MAoUEcBkVh%2BLprtMqI%2BYwZVT64LPW7NTWhlx2kelE9HUiYwqXH4DAqtjkomC36vw0RZcv7moAIOgc1xmkXGO8ds%2BVhZfb9a%2Fwf40IFKppFXEbK2SjOris5UYj8wjuP35VuJh1%2FxRz6zrs0KacdoXZeVnU32c9jtfyU9V3zN5fYUkEYosJXVxbBWGfE9qeQNPKkNkdw%2B3Z7T9VaJ6EG80BSXkKHvHg2spo1SaCLmQHPwH2F%2FU1wEAsmSn1haLee6lQIsTFCbFQg9E63fExSwUh3icvONTgnWiMPzC86CGuwPZRkCJHQN4SDjtAfvG1vJlYHDs6NDg2WioY2MWOS477os230lb8UsHtqbaUx6DXSSjiNk%2FDK8HVJ99hznIdGDw8woxUt2sTZX3PR7YF3g7f6F%2FTE1iWZM7k%2BZUTESbNA08EgZlZV5YeYBjs4BGsr9OfCAdQZln07a%2FfaWMkJh8KtNnttdnVcSuevZu3GPIWYcW5VmVh731853Rswp4qQ0QY6pgGTdC64PBWNBt%2FQuIAiNk8hsIDXT8nfOVq4VD%2F0u0Nkciv0SlihhJVkiecJn8RBRfr1k%2FSL57TYtOwyAV38fdCSSFm9vk%2BVd2iWJAaHV0%2FpNjH6mvnGgYX0UiMesIrC%2BJf5G%2FFCb94NBDD3yAVmlq2Iyf%2BpTXuclGzb5ny76Y00aQWfRCGpI9vMAmVgPxCklf32QgiF1j%2BHYJmIcgD%2BNQD576MX822P&X-Amz-Signature=d0c5007bad44ed92ffd27666735d3da3c4babdf9e9e835f158cb4e84e095db88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







