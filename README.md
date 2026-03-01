



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UI4RJAU%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T123813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICvOJokh9SCt%2FXpe18rrvWIOqcSLIuwGpQ8ha98wffa2AiEAzjtoRJg93bXslxEeQA88jDt1SPBql2vIQeuDayS6BPQq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDN0SSQKTeajdP%2BMyxyrcA2DPvJ0il18n1aTAwb259mhG4OsN%2FJ3L8IymOsWJ5xELa9s7bBiVJoBPbrLj69vClM5%2FO7469pYjiqAKZ9oSJjuBlRzma%2FZDGVSsjaZI0ZftNKC94m7RfYv6B0KjCh55SXclRgi5Tt%2BH9r7guwFueKtvX019Zf5iaoRhLBK1Uq9L8D%2B%2FblpKZdHY5eguBJSCdXu0N7BVFRkP4wkBUdOLww6QXMoC2W3eJqdV6Mt7b5UPbL%2Bnh632tl%2FpoaGqxEzWMj0UKCq4gp9vlEhvrUJHB5w1WXh0h5f%2B8L1g4Z1Wqa31mUkymMu4SCKnILIKWeCvdVxYUaYdXKJJ0xTXczORY7xMeOWtfx5ut7mRydFAyjVKEAL5cLdW1BrjOIWB2b6dIhID7104bqfXAGQ%2BqCiY2XLY%2F3yIHkbIovDQS3obuEZib4%2BhvdrBob1dcVIWp5xEt4JqdGvlggFVWRhJz58%2B1pa18h1y4AKC3yHa%2FPDIeHXcnR6HgcPgBMh7HyugTh9LNpw7M2jX4YaDh%2FFjel5Ijub7qgffXgJ1ByHJp%2B%2BjPIsASRXh2Ot5hvD4lU9j3lfniodkcoltQ2hwvoW9Cb3M9ihkoxQ51uxRb2a%2Ff0yeQLYdP037Ez4un1%2FikkbHMITyj80GOqUBoR11h9tp4MDLwRWoIrxHB7tjgNTgFBBnW%2FPLE8HvtbDGxqWzZy2WSlMXzqbe3jKTi4vDH%2FGmkAkaYFLW5Cr3liDEXkCYV%2FjGnlw%2BW2xO4HlA9CR6mt3zQIS%2BFAwfy1%2F%2BjQHbYo4ZKxHQ5YDJx39J9SsFtXtU3Y%2BJzC9HzFSGiPJabk5NoYmPvBvhH66hA0Vz5AbbWLBsRZ6SQUJCEiR0OYV9Slf3&X-Amz-Signature=829d6cad59987d5266e7d03d00c3b91350c18e34dcfb2988159a7e133b69fd9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UI4RJAU%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T123813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICvOJokh9SCt%2FXpe18rrvWIOqcSLIuwGpQ8ha98wffa2AiEAzjtoRJg93bXslxEeQA88jDt1SPBql2vIQeuDayS6BPQq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDN0SSQKTeajdP%2BMyxyrcA2DPvJ0il18n1aTAwb259mhG4OsN%2FJ3L8IymOsWJ5xELa9s7bBiVJoBPbrLj69vClM5%2FO7469pYjiqAKZ9oSJjuBlRzma%2FZDGVSsjaZI0ZftNKC94m7RfYv6B0KjCh55SXclRgi5Tt%2BH9r7guwFueKtvX019Zf5iaoRhLBK1Uq9L8D%2B%2FblpKZdHY5eguBJSCdXu0N7BVFRkP4wkBUdOLww6QXMoC2W3eJqdV6Mt7b5UPbL%2Bnh632tl%2FpoaGqxEzWMj0UKCq4gp9vlEhvrUJHB5w1WXh0h5f%2B8L1g4Z1Wqa31mUkymMu4SCKnILIKWeCvdVxYUaYdXKJJ0xTXczORY7xMeOWtfx5ut7mRydFAyjVKEAL5cLdW1BrjOIWB2b6dIhID7104bqfXAGQ%2BqCiY2XLY%2F3yIHkbIovDQS3obuEZib4%2BhvdrBob1dcVIWp5xEt4JqdGvlggFVWRhJz58%2B1pa18h1y4AKC3yHa%2FPDIeHXcnR6HgcPgBMh7HyugTh9LNpw7M2jX4YaDh%2FFjel5Ijub7qgffXgJ1ByHJp%2B%2BjPIsASRXh2Ot5hvD4lU9j3lfniodkcoltQ2hwvoW9Cb3M9ihkoxQ51uxRb2a%2Ff0yeQLYdP037Ez4un1%2FikkbHMITyj80GOqUBoR11h9tp4MDLwRWoIrxHB7tjgNTgFBBnW%2FPLE8HvtbDGxqWzZy2WSlMXzqbe3jKTi4vDH%2FGmkAkaYFLW5Cr3liDEXkCYV%2FjGnlw%2BW2xO4HlA9CR6mt3zQIS%2BFAwfy1%2F%2BjQHbYo4ZKxHQ5YDJx39J9SsFtXtU3Y%2BJzC9HzFSGiPJabk5NoYmPvBvhH66hA0Vz5AbbWLBsRZ6SQUJCEiR0OYV9Slf3&X-Amz-Signature=97d21edd709286514331d27a16cba027f67457ac4198261dd974f254fe014ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







