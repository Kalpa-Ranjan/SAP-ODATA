



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GM6YAKJ%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T062319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDo6iOwXXb%2F2%2Fy8EsDnl5EBwE5jtvug4hUJwhIQz8t1dgIhAMlgt%2BiYpH9DAn8PSnqfT9fNcMzH%2FgYA36ftAi%2B08fnjKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxt4%2Brop72WjdHHFwQq3AOcbmvSoPKeIa8a50BFZkEFQBQhWPkDuvCSTJZCFgJHEhLML4zeKmrUPdG3RvH6E6a211mhSkm0beVHpTzUhhR7BxHhsNJwv%2BFo24Y%2BWdEjnS2qkEgslgHmDf0ORWCcRQpkiaNEnz7uM%2FyT30%2B4vs0xPn7GmlU7tGNd8WdFtdSd%2B5IIVTnWMY35%2BU8vcIQ4Is%2FxvkebpnmaSa73K6EeCxOHg22nDSBirzIjKkP25zeucMRDemmLeaRs8vgW2dZSXnepeDN3WIsyTTD%2F3IQjwX8YxSXBzuJZKRIu9%2FHA5sNvH4SsyMmHJVO%2Bb2HaIvAVDRXzZgKwjY5LWD5xBGpQkWY%2F2T9oHkh139XT6GhkEKZlqP2ufoiCtOxLseXR9mmcW%2FQIe14%2FuILroCNCaB9is%2B2evbfs47Wy6oNUudoPuq8MP8W1plyG8Oa0m9HKjL8vemWzbC004zkAjKjF0%2FpodJScMqo6ZpuQ097A7b0U9eEqMOsqg8snoL9xILk9zjz7eWRmN%2BBnOyPr%2FzavaYQ8IAkliJun9XlkoxmAb4iXXSygHTj%2F2Umkcst3zKCL27ECwX9OnRIYME9E9yGguXDhS9NKxGQUcNItvGDtLLJT9efbh%2BIXkxVhVV7An%2FwSgTCnopHIBjqkARd3Afj7dwp8CKmgSpRYQYcWSeZiZYRUsRSh4bmiuuwOSU%2BiVCLkG4qbBzWemAjDSfLtBaN%2Fh9CF9U48AhyQ6YXUXfflwTUHpC3gQ5fY0v0bgrfEhyOths3%2FR9yWQYELOiGe687zhx5ehWlzm04vImznsHDqQZ0y20jflB3loxHyOKLiE1h%2BJOphce7rUPI6zQQY%2FMr4QSGxY4GCztfs%2BMeW3hhY&X-Amz-Signature=317ad6c276adfca2986a473414c3dac9cb2bb0035f0c7becb9f5ccbd1b784c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GM6YAKJ%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T062319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDo6iOwXXb%2F2%2Fy8EsDnl5EBwE5jtvug4hUJwhIQz8t1dgIhAMlgt%2BiYpH9DAn8PSnqfT9fNcMzH%2FgYA36ftAi%2B08fnjKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxt4%2Brop72WjdHHFwQq3AOcbmvSoPKeIa8a50BFZkEFQBQhWPkDuvCSTJZCFgJHEhLML4zeKmrUPdG3RvH6E6a211mhSkm0beVHpTzUhhR7BxHhsNJwv%2BFo24Y%2BWdEjnS2qkEgslgHmDf0ORWCcRQpkiaNEnz7uM%2FyT30%2B4vs0xPn7GmlU7tGNd8WdFtdSd%2B5IIVTnWMY35%2BU8vcIQ4Is%2FxvkebpnmaSa73K6EeCxOHg22nDSBirzIjKkP25zeucMRDemmLeaRs8vgW2dZSXnepeDN3WIsyTTD%2F3IQjwX8YxSXBzuJZKRIu9%2FHA5sNvH4SsyMmHJVO%2Bb2HaIvAVDRXzZgKwjY5LWD5xBGpQkWY%2F2T9oHkh139XT6GhkEKZlqP2ufoiCtOxLseXR9mmcW%2FQIe14%2FuILroCNCaB9is%2B2evbfs47Wy6oNUudoPuq8MP8W1plyG8Oa0m9HKjL8vemWzbC004zkAjKjF0%2FpodJScMqo6ZpuQ097A7b0U9eEqMOsqg8snoL9xILk9zjz7eWRmN%2BBnOyPr%2FzavaYQ8IAkliJun9XlkoxmAb4iXXSygHTj%2F2Umkcst3zKCL27ECwX9OnRIYME9E9yGguXDhS9NKxGQUcNItvGDtLLJT9efbh%2BIXkxVhVV7An%2FwSgTCnopHIBjqkARd3Afj7dwp8CKmgSpRYQYcWSeZiZYRUsRSh4bmiuuwOSU%2BiVCLkG4qbBzWemAjDSfLtBaN%2Fh9CF9U48AhyQ6YXUXfflwTUHpC3gQ5fY0v0bgrfEhyOths3%2FR9yWQYELOiGe687zhx5ehWlzm04vImznsHDqQZ0y20jflB3loxHyOKLiE1h%2BJOphce7rUPI6zQQY%2FMr4QSGxY4GCztfs%2BMeW3hhY&X-Amz-Signature=c720079dfc5a5a50f1d31a63d9832e66eadc4a8724e93335d852fe2a78ac5c79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







