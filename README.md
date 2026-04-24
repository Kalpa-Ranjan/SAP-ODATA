



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKQNQ56H%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T131245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHO0e4tUfr0nrs3Mtmc1%2Bz0fdcWI1xJGDchEULUP27kIAiEAsH05i0DqHlPIINzFsZy5g0gwTM2xKI54DhD0Xpd41PQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDHNQ8OHO0ICS8qXVIyrcAxxCwyE79W5IiFrp4j5AKQl5%2F2kkxba8QJdyBdU5e52e9Rzd9hPke9OakJVBJPb6BGPcoLr%2FJ0YPhn30BE7FwJgJ5XAo7%2FGXOEx3XN6rKPD3Mw%2BfmZk8GqPul79oMl6j%2BceZZqMEmuKTdDMBQEYUvi6TDDL5NQuK9pwOnHMFTC20etxS6bceD4%2BmONNJsOdX3SvrgV2IrQ0jqTRS3mQh9mqvjvbcTMY%2BNwma2UiK6SP0cVs%2FCA3hygL7iTzEppv0HAeMlqm6YObeQc%2B2qhHDDZavjAI2sR7VyR8HwBsjsjZvBkdfZYwbLLkLFTy7YCGzoaT%2FJaiTNK49Qf9EUkskgB95u%2Bnky0sdhSaForDTzGZPSYXxd72KDtfn3kiI8KIQhL3gD4HuVofYF6Ba%2Fo5ZBKXP8ZZ24otyIDSdaq6SP474QmHRW2T3HrCeU3pmJKzaIiJVI0ESAlntie073lw2dqNq9hrUAM3beRkcFVPXwvJveONPDgpj2RdfMhrVl%2F7yILhBVBbn7MTlRofxrk5jgWEYR09J%2FUloGoHbQTpTqgdBTjACgGtlg9pruu0Wt7J2RWwqEKu5PTUNTiKW0xTUG67DWoxBaO8oAUVWH5lR6xjN31kfQp7AheBVz0mfMNTNrc8GOqUBnSDSlHJd8uX2oAzKwGfF6bfZU50gxsENhUMr4diD%2FYRp2dsMtUXuSJqfXob0jdIk4zJHmdfXw9gWzIUV7u4eAb0cBbVedd%2BHnXUK7vHuJisWGjzbgrxDH3hMuSHoPgjo9K4kbiiakjdYDjJ2x0W9XZLEzPQ%2FeVLdeb1a%2FvKg5%2BEnKo5cVZTqIL9Arbh60PMPfTTiExqb43cudbwr89AghUj2qb3J&X-Amz-Signature=c10e56b91c328cedfb0a096949d9431191b8f1a8ca8ec90ee95efc579212efdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKQNQ56H%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T131245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHO0e4tUfr0nrs3Mtmc1%2Bz0fdcWI1xJGDchEULUP27kIAiEAsH05i0DqHlPIINzFsZy5g0gwTM2xKI54DhD0Xpd41PQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDHNQ8OHO0ICS8qXVIyrcAxxCwyE79W5IiFrp4j5AKQl5%2F2kkxba8QJdyBdU5e52e9Rzd9hPke9OakJVBJPb6BGPcoLr%2FJ0YPhn30BE7FwJgJ5XAo7%2FGXOEx3XN6rKPD3Mw%2BfmZk8GqPul79oMl6j%2BceZZqMEmuKTdDMBQEYUvi6TDDL5NQuK9pwOnHMFTC20etxS6bceD4%2BmONNJsOdX3SvrgV2IrQ0jqTRS3mQh9mqvjvbcTMY%2BNwma2UiK6SP0cVs%2FCA3hygL7iTzEppv0HAeMlqm6YObeQc%2B2qhHDDZavjAI2sR7VyR8HwBsjsjZvBkdfZYwbLLkLFTy7YCGzoaT%2FJaiTNK49Qf9EUkskgB95u%2Bnky0sdhSaForDTzGZPSYXxd72KDtfn3kiI8KIQhL3gD4HuVofYF6Ba%2Fo5ZBKXP8ZZ24otyIDSdaq6SP474QmHRW2T3HrCeU3pmJKzaIiJVI0ESAlntie073lw2dqNq9hrUAM3beRkcFVPXwvJveONPDgpj2RdfMhrVl%2F7yILhBVBbn7MTlRofxrk5jgWEYR09J%2FUloGoHbQTpTqgdBTjACgGtlg9pruu0Wt7J2RWwqEKu5PTUNTiKW0xTUG67DWoxBaO8oAUVWH5lR6xjN31kfQp7AheBVz0mfMNTNrc8GOqUBnSDSlHJd8uX2oAzKwGfF6bfZU50gxsENhUMr4diD%2FYRp2dsMtUXuSJqfXob0jdIk4zJHmdfXw9gWzIUV7u4eAb0cBbVedd%2BHnXUK7vHuJisWGjzbgrxDH3hMuSHoPgjo9K4kbiiakjdYDjJ2x0W9XZLEzPQ%2FeVLdeb1a%2FvKg5%2BEnKo5cVZTqIL9Arbh60PMPfTTiExqb43cudbwr89AghUj2qb3J&X-Amz-Signature=28281c84fb51a5cf85c93910996dac3c31f049f0245b2692425262f6ab76a60c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







