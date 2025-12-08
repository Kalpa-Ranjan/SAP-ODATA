



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWIFVLZR%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T123406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI8mFoBFKtAKZA9h2LkUW1LWNIKGwNMnFh22SVT2f6qAiAvTcRSwL2svyrXyXBy%2FVPs2bVRV8F%2BAq88P7%2BYdbDaECqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMshrjEDCiCCujto7kKtwDbORamIqaLb2boNclBxttKjK6IXD8rRa5lfFwlX0saS3oPeYWy2VHdUyNZL0AwyU8D3o9ycm8h5rkcmBedO43r8FjH26POYWzrNxRzdGKIZtR1PKxpA9x%2FrdXlGmKBYKsGJv8T2D1RPYkvZo9brUP878IU34UjEwici6LBJqr4V7%2B8pESIyLfvFEGcUjaJ%2Fs867aFBhATdPS8uGgFCLuF5L5yzubU5EGvfRyzkGgY6TPIdGANgPQ8Csk%2FC%2BkucqL81ao89E5CQ2sAGOXorLoXJapDFGUr3AbvI4CG%2FL0zj%2FEzmYZTOVX9CPO7V6WulqtbiGjadgF1iZ5JHuI4dhgeY%2FIO%2FBRNBFn4OWnUPQ1sPFGNaECUAFOSeLtJaE8xyGlJaj4Cvq%2Fn7ZtySmYog4UlPzOZWvcAHtlaG5PsYAvARi7HPYsIM5y7Llde4DHIYw8rx96LVXSFKnUOHBNLX4oHoEjFc9hXjA%2BFu0ZCha3N21X8HA15Sk1pRIeSalQPSL5g%2FyLyDq3Iv3TIBTh8D6AvPx%2B1vjtfytK4LpObhscG22zXmNNcBT6Fv5ngwFbs%2FW9DueTnau7ABERCFGHh%2FMSnrhz6ZXP9UeFAYnzydesD1malGJ1OXlJ3Q5YKhRQw9vLayQY6pgGS%2BLjQAXadOHVSIIH1ueiCYrhpo868i0W54QOQYMJ%2F6Rl%2FNSVN7mz%2FFTnNEQxXlZ6Ex2KFx9ehX9lHrVhQmPw8BLo1bpR%2Fye9mOaSspPoHiuhaIgt0w9jn3DSxgV3tt3HxKNoMgJSGWuzyKHbXNcc8g9EZDB7o2L3cPwBJqvb32QMa0cqFB9elNEzqKskygLjGuuPu%2BdQbuDmqAYE6JfNTEahQ09dj&X-Amz-Signature=cf5ef5131c93c6b733925815b441138440d852ad9d0f5c58de1b1ad3465aec3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWIFVLZR%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T123406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI8mFoBFKtAKZA9h2LkUW1LWNIKGwNMnFh22SVT2f6qAiAvTcRSwL2svyrXyXBy%2FVPs2bVRV8F%2BAq88P7%2BYdbDaECqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMshrjEDCiCCujto7kKtwDbORamIqaLb2boNclBxttKjK6IXD8rRa5lfFwlX0saS3oPeYWy2VHdUyNZL0AwyU8D3o9ycm8h5rkcmBedO43r8FjH26POYWzrNxRzdGKIZtR1PKxpA9x%2FrdXlGmKBYKsGJv8T2D1RPYkvZo9brUP878IU34UjEwici6LBJqr4V7%2B8pESIyLfvFEGcUjaJ%2Fs867aFBhATdPS8uGgFCLuF5L5yzubU5EGvfRyzkGgY6TPIdGANgPQ8Csk%2FC%2BkucqL81ao89E5CQ2sAGOXorLoXJapDFGUr3AbvI4CG%2FL0zj%2FEzmYZTOVX9CPO7V6WulqtbiGjadgF1iZ5JHuI4dhgeY%2FIO%2FBRNBFn4OWnUPQ1sPFGNaECUAFOSeLtJaE8xyGlJaj4Cvq%2Fn7ZtySmYog4UlPzOZWvcAHtlaG5PsYAvARi7HPYsIM5y7Llde4DHIYw8rx96LVXSFKnUOHBNLX4oHoEjFc9hXjA%2BFu0ZCha3N21X8HA15Sk1pRIeSalQPSL5g%2FyLyDq3Iv3TIBTh8D6AvPx%2B1vjtfytK4LpObhscG22zXmNNcBT6Fv5ngwFbs%2FW9DueTnau7ABERCFGHh%2FMSnrhz6ZXP9UeFAYnzydesD1malGJ1OXlJ3Q5YKhRQw9vLayQY6pgGS%2BLjQAXadOHVSIIH1ueiCYrhpo868i0W54QOQYMJ%2F6Rl%2FNSVN7mz%2FFTnNEQxXlZ6Ex2KFx9ehX9lHrVhQmPw8BLo1bpR%2Fye9mOaSspPoHiuhaIgt0w9jn3DSxgV3tt3HxKNoMgJSGWuzyKHbXNcc8g9EZDB7o2L3cPwBJqvb32QMa0cqFB9elNEzqKskygLjGuuPu%2BdQbuDmqAYE6JfNTEahQ09dj&X-Amz-Signature=ce40312f99991aa44b68c99fc6431762b0adc182fcb98ab94b5b700f1d592477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







