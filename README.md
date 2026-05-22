



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7Y5Y6V3%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T085357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFYqxtfTOtht1xe51VbGdIDbrO437hLBU8Hzte2WvTOhAiEAvZQVjSxkwn%2BW%2BXaSuc5wBRqQum07x2ybhnaZRfV2xRAq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDH41yTPa9WElnLpleCrcAy1KoQ4BOeNTP1j0a8VftmeFl%2B7RmdbItR9ddGH%2F0Cw39iRx9MLWpvGnkaV%2BSx6VsJatdIRMqPAuSeaf5VIFLTMP5lt0R0nS8mdLzIdPKmdhEPT3KugTsJNp7msI3uirt2PyQZ19CkV3lfYUcc0nqOFjkXjypoNm020E4SAnsHq5rGeQMVMRUzPbSUzdoLpVzdTQlyvgZfajJL1LJO4A2z891D78ugOw%2B5l6bOgaV6xmhlEkVBmer%2BBoDOEa9zsk0ooWRedt9dbyJhdnAAa2VQhpB%2BbFZZLVKoFerzoJoZtY1UYQRTmuqBP01JYAoVZyQiyQsbeIu5LHekOpdeB4fn8yE%2BOHwTQCwhfrmfzgbB7aHIck9jcrEBdslIEiFNvyZTeUig0cnVFpQfJ6PKr8%2Bls0ypoTrIEmrgK1HxECoAJjfMBAqB%2FNmomgZtnA%2F%2BAKsV8Lb9sR2F68TwkDrtYXyFQq%2BqvTe7Ma5y4jfwdE2EqVIT9nLAFEfUTwr7TFo5STIT0Pt%2BKfSZv7PahkpivHWsgrvMXlqhsaNp%2Fn8TDnnQu4Y09RP%2FFeaqgzKCuNzF4fLMmT0PL6asIm5%2Fk3Qyvjq3piJ6b62sYzTlv0oE1ak2B9vw2oWbszN6fOoe6mMNWcwNAGOqUBKC1b3mq8iqGQ1FgbBg8TxeBz5FP%2B4gTriySEjk1OVUBBpQDuR%2FxikPZJ5OEKDMZLQ7aJbQ5d4XYUsySoMSBDLw7etssRna8aQnXwmGtbQnL%2BYHk8RvcHVkcunGRwVYzKQF0cSpu%2Brllup6GG1qytuYLftNHi9dJcPSPareLxdSmGb%2FI3QK0UsHy4Eg23P%2B%2BRibnY8iFoRkl8ETtOnnjRFf%2FaMmKw&X-Amz-Signature=566fde84455dc1f49b7478e5d1f568f6e79bde049c38d29f9ec9dcf76632ad61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7Y5Y6V3%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T085357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFYqxtfTOtht1xe51VbGdIDbrO437hLBU8Hzte2WvTOhAiEAvZQVjSxkwn%2BW%2BXaSuc5wBRqQum07x2ybhnaZRfV2xRAq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDH41yTPa9WElnLpleCrcAy1KoQ4BOeNTP1j0a8VftmeFl%2B7RmdbItR9ddGH%2F0Cw39iRx9MLWpvGnkaV%2BSx6VsJatdIRMqPAuSeaf5VIFLTMP5lt0R0nS8mdLzIdPKmdhEPT3KugTsJNp7msI3uirt2PyQZ19CkV3lfYUcc0nqOFjkXjypoNm020E4SAnsHq5rGeQMVMRUzPbSUzdoLpVzdTQlyvgZfajJL1LJO4A2z891D78ugOw%2B5l6bOgaV6xmhlEkVBmer%2BBoDOEa9zsk0ooWRedt9dbyJhdnAAa2VQhpB%2BbFZZLVKoFerzoJoZtY1UYQRTmuqBP01JYAoVZyQiyQsbeIu5LHekOpdeB4fn8yE%2BOHwTQCwhfrmfzgbB7aHIck9jcrEBdslIEiFNvyZTeUig0cnVFpQfJ6PKr8%2Bls0ypoTrIEmrgK1HxECoAJjfMBAqB%2FNmomgZtnA%2F%2BAKsV8Lb9sR2F68TwkDrtYXyFQq%2BqvTe7Ma5y4jfwdE2EqVIT9nLAFEfUTwr7TFo5STIT0Pt%2BKfSZv7PahkpivHWsgrvMXlqhsaNp%2Fn8TDnnQu4Y09RP%2FFeaqgzKCuNzF4fLMmT0PL6asIm5%2Fk3Qyvjq3piJ6b62sYzTlv0oE1ak2B9vw2oWbszN6fOoe6mMNWcwNAGOqUBKC1b3mq8iqGQ1FgbBg8TxeBz5FP%2B4gTriySEjk1OVUBBpQDuR%2FxikPZJ5OEKDMZLQ7aJbQ5d4XYUsySoMSBDLw7etssRna8aQnXwmGtbQnL%2BYHk8RvcHVkcunGRwVYzKQF0cSpu%2Brllup6GG1qytuYLftNHi9dJcPSPareLxdSmGb%2FI3QK0UsHy4Eg23P%2B%2BRibnY8iFoRkl8ETtOnnjRFf%2FaMmKw&X-Amz-Signature=df4653f52d19e8ac6f207949493d6935f019b56ef3ac5ab3bd91af2597c814bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







