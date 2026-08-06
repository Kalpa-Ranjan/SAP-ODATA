



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3MTJ3K%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T135219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQD4nSLn42awwVECpKzv7oRpin8a%2BfZLwND8fnrQ9Tv1lAIhAPtaJ6a%2Fpk0Bb5bEu8n%2B2fn%2ByFHFFM1FPz3XkL8Ikxo2Kv8DCD4QABoMNjM3NDIzMTgzODA1IgxQ4sajloWKuHuZDQYq3AONpOchYQYhtT1sf%2FEFWB5uWaSaxdpqoBIzPM7SIKNFYqfIw7bSt1IF%2BZZrCAJuCohuYOf0lTVnRha1OpOuI3bHht00SlaWNAz9kDTNfuweluJZ6BZAUpeD4lMrwAigrZn3yOaaSIZyaa7OFMzkW%2FMwXR2k%2F3B675jEVpBaqDCiRIF3hc%2FuwXtWstVTV2oCE95W8o9qKR4gafB6RnVgR8NynIaCvdqGR5W8MIsBOfk60wDaVTQU%2BjLkLL1T6aaA5n5R1lTSyZI1Io%2F62aJtPKoHuOglA%2FW%2BTiQcfufMRyR1W8Os3H8QUL3w1e8RgQRTyG2ua9Mnf9%2BxVdOLs59O67N%2F%2Bi%2FdtdMR42zIgOHeakw19zwJ6aZ0LjZoucGS6u0P8ZwihdfoiqiRByABSD2e8cycZg5F8j1ROh2B73zA8UYFYM9%2FNm1JoxetnDXWrG7vz4wHLMHT0sBhyMIzTkxirt6hJXmg2FhWC9E38%2BoQB3ozUA3IYzIlPWzxEjyTYpb5qBpjtvz0IdfPRpEcTtKyRT402CbAu5Zy1iyDDxCK8a8JbKNzIm21QyOL2SN%2FaYojfvzCulUSTbGuYGsipPAfamiPQTRNsL%2FbuOKbF6dKoPe2q3s0Z%2Bd5Pg84nI733zDSi9LTBjqkAVY1NE2iP7WxQTrA90UuicH8%2FX1tr2O9QHbFIlUq41mCjg8e3ADTt8qcmpAGqsLmWsWq%2FNR7GEk3%2BemJ%2BIKCE7sILSkb8xgiOEgt0pX5d2LVnDUl5FBiaupi07NIr17Kv4MbXSd9hFJBtJ5iQUL%2BfS0LOtKmoO2%2BAeejOFbBbuyBhqpuyipPbb1UMbFv78o05A2sy6QqSXF%2FXaqlDjK9psX6tR%2Fh&X-Amz-Signature=93febbcd94358097bd292485c37ae5270c66ec108e1357bddf558a6f0e38a598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3MTJ3K%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T135219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQD4nSLn42awwVECpKzv7oRpin8a%2BfZLwND8fnrQ9Tv1lAIhAPtaJ6a%2Fpk0Bb5bEu8n%2B2fn%2ByFHFFM1FPz3XkL8Ikxo2Kv8DCD4QABoMNjM3NDIzMTgzODA1IgxQ4sajloWKuHuZDQYq3AONpOchYQYhtT1sf%2FEFWB5uWaSaxdpqoBIzPM7SIKNFYqfIw7bSt1IF%2BZZrCAJuCohuYOf0lTVnRha1OpOuI3bHht00SlaWNAz9kDTNfuweluJZ6BZAUpeD4lMrwAigrZn3yOaaSIZyaa7OFMzkW%2FMwXR2k%2F3B675jEVpBaqDCiRIF3hc%2FuwXtWstVTV2oCE95W8o9qKR4gafB6RnVgR8NynIaCvdqGR5W8MIsBOfk60wDaVTQU%2BjLkLL1T6aaA5n5R1lTSyZI1Io%2F62aJtPKoHuOglA%2FW%2BTiQcfufMRyR1W8Os3H8QUL3w1e8RgQRTyG2ua9Mnf9%2BxVdOLs59O67N%2F%2Bi%2FdtdMR42zIgOHeakw19zwJ6aZ0LjZoucGS6u0P8ZwihdfoiqiRByABSD2e8cycZg5F8j1ROh2B73zA8UYFYM9%2FNm1JoxetnDXWrG7vz4wHLMHT0sBhyMIzTkxirt6hJXmg2FhWC9E38%2BoQB3ozUA3IYzIlPWzxEjyTYpb5qBpjtvz0IdfPRpEcTtKyRT402CbAu5Zy1iyDDxCK8a8JbKNzIm21QyOL2SN%2FaYojfvzCulUSTbGuYGsipPAfamiPQTRNsL%2FbuOKbF6dKoPe2q3s0Z%2Bd5Pg84nI733zDSi9LTBjqkAVY1NE2iP7WxQTrA90UuicH8%2FX1tr2O9QHbFIlUq41mCjg8e3ADTt8qcmpAGqsLmWsWq%2FNR7GEk3%2BemJ%2BIKCE7sILSkb8xgiOEgt0pX5d2LVnDUl5FBiaupi07NIr17Kv4MbXSd9hFJBtJ5iQUL%2BfS0LOtKmoO2%2BAeejOFbBbuyBhqpuyipPbb1UMbFv78o05A2sy6QqSXF%2FXaqlDjK9psX6tR%2Fh&X-Amz-Signature=82cc18ecda130f92133956f804a04adf71d3a4d913b8694500407c3f64dc8ef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







