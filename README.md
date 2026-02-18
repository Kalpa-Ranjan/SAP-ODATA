



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5TM7ZX6%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T184542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfCRI%2FlR%2FjJALj%2Bqk2mmzT%2Ba1lJBvwDMohNhCu0mn3VwIhALW0%2FxD5X%2BPjzaWbhLWWMAW%2BObedarwQAsDayD7n%2B%2Bt7Kv8DCGwQABoMNjM3NDIzMTgzODA1IgzYHCB1ztfGTSGf0GEq3AM5MBinobsbBCIR9df7r2abi%2FjHLogbnnjeMrfwwjLBYq8PRiOnj4FdyCOpY%2BJnvpq7hW%2BXMzzfXM3V%2B7pCDYF3a7JsM3hmy9054cKuui0XRxZxAuY6XKuikgG0dYrkZyK3e6R6V%2BZdfip6MD3l9%2Fzan6ZXYn2n0o7PczTksY7haRr4hIU4Zf8%2ByMKH4vrhwCkigrAN6%2BO1t%2F3jtxmHMGnh18FZ%2B0j7UrRXMMHmNvoIN8r4bWUZPcvWsSAceApIY5slIrAvJ60wnx4B4YGest%2Fv1Tx8byoYUFyddIXgZWbkUGqAkkas%2Bcf3tkkxj4QNdKqdGzqq4jefoJ8QkKYFkFzNQkXQUpMedXyt7y2ZQCoDArLWOLQWVYNPukIvLfy3oZwUXaZSSYm7ST33aAVOurF%2FrFJr7ekUi5dpH5rcee9fdlKcABr%2BPK1H8XHTtsRfzWkANfT5q%2FVCEB3k%2BfeqvEUFXCygjiEQxTjL%2BHTdVwrXzExxK7jpuDi85vGo13tKXIlEBd6zyzn9U6oMeuzoDEKLfUswoQuyP4DemmZUHkahbWxZlH5IA%2BIdlG0lOYhCZSNwqSXKo4Hf4NIgnYeYshwOqiEVEBGKRBzTZdQcjp%2B9npq9f1ng%2BsAGMEShmDDCitjMBjqkATG6Vs6WVQj9iLB7y66R5seYMn9Dq7LPVaDd7vHnuBvvaZczN7Jt%2BB8T5B4JZGlIkkcEGGh9NFsu9GpGnbzBBafVpCiBqERQTv0wHrU%2BFL5cSqL92J8BetCK3OrVisZAHZrbAusNk0fS2RrLeGSiBdw7PLI9VavM2QTAHBjdscezWebVgI%2FkWe3w5IPrkKKGf88u4iYG50UjhMOsEfsVI1zT1jCC&X-Amz-Signature=3b1f0db157fa9dd60dd1e7ea8c08f422c6e22cb7d5aec4df344940c18cd95694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5TM7ZX6%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T184542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfCRI%2FlR%2FjJALj%2Bqk2mmzT%2Ba1lJBvwDMohNhCu0mn3VwIhALW0%2FxD5X%2BPjzaWbhLWWMAW%2BObedarwQAsDayD7n%2B%2Bt7Kv8DCGwQABoMNjM3NDIzMTgzODA1IgzYHCB1ztfGTSGf0GEq3AM5MBinobsbBCIR9df7r2abi%2FjHLogbnnjeMrfwwjLBYq8PRiOnj4FdyCOpY%2BJnvpq7hW%2BXMzzfXM3V%2B7pCDYF3a7JsM3hmy9054cKuui0XRxZxAuY6XKuikgG0dYrkZyK3e6R6V%2BZdfip6MD3l9%2Fzan6ZXYn2n0o7PczTksY7haRr4hIU4Zf8%2ByMKH4vrhwCkigrAN6%2BO1t%2F3jtxmHMGnh18FZ%2B0j7UrRXMMHmNvoIN8r4bWUZPcvWsSAceApIY5slIrAvJ60wnx4B4YGest%2Fv1Tx8byoYUFyddIXgZWbkUGqAkkas%2Bcf3tkkxj4QNdKqdGzqq4jefoJ8QkKYFkFzNQkXQUpMedXyt7y2ZQCoDArLWOLQWVYNPukIvLfy3oZwUXaZSSYm7ST33aAVOurF%2FrFJr7ekUi5dpH5rcee9fdlKcABr%2BPK1H8XHTtsRfzWkANfT5q%2FVCEB3k%2BfeqvEUFXCygjiEQxTjL%2BHTdVwrXzExxK7jpuDi85vGo13tKXIlEBd6zyzn9U6oMeuzoDEKLfUswoQuyP4DemmZUHkahbWxZlH5IA%2BIdlG0lOYhCZSNwqSXKo4Hf4NIgnYeYshwOqiEVEBGKRBzTZdQcjp%2B9npq9f1ng%2BsAGMEShmDDCitjMBjqkATG6Vs6WVQj9iLB7y66R5seYMn9Dq7LPVaDd7vHnuBvvaZczN7Jt%2BB8T5B4JZGlIkkcEGGh9NFsu9GpGnbzBBafVpCiBqERQTv0wHrU%2BFL5cSqL92J8BetCK3OrVisZAHZrbAusNk0fS2RrLeGSiBdw7PLI9VavM2QTAHBjdscezWebVgI%2FkWe3w5IPrkKKGf88u4iYG50UjhMOsEfsVI1zT1jCC&X-Amz-Signature=7272dced1b2c5ead922bea9242c193f24c87bf459665ca80adbdf03bcefe1ea1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







