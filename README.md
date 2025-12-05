



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYLQ2XA4%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T182102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG28Uad5rFL%2F1laZEwbN6vXpJnnipfkClkyEWSCxEF%2BUAiBKlcX73q9ro0Hxo4wTA7%2FCY6Aorq8Zn4tz2omalwWogSr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMaRntURoeWaNFYrtBKtwDXgrix31n9RUB8asZQsgadZ42J6xYDoyPpMSr9hR9cAbdwDS00ODq32TI1xGRhV%2Bz52QYCAVd59hyg7roLvSeeDZm8GN9k%2FGW%2B6xhg7IkCB8av8NR54vDiTIqbqDQDgnpk%2FYxdKgmuPvJVBN%2FXvnMILvlPsWX97qs%2BUgfUThs7pjRKmYP0oazMVdvqvFE6A1OHvJJFCDYj9FTi%2BsxQKCID0U6hpKgRuE7B6aVm%2FyOzjd5TBbCii9ojhJ5lACM7eRTgpTvb8HxRxNr9rfI7HMOuefGE6ezDUy3dt%2FTyuzobkZOTWYYOOGopEYMP4YASQBtzETvEkJ%2FQIWF6WrBMb8bl8Wr5WNp0iEpqsNbU9b8Yw%2B3W1BJxe656DUM%2BvZWhCGPYvGfqXDQZLUIlqLEYNwNodJU%2Ftr%2FuqmcIPpK4CJJqzuDpFasW4ZOspscrRLBYZkCba0iwBMALfEuKXXDiNuQzcgAlb%2FNg4szRbVwtL3ralNw%2BD7ylzIcA0KD4XA09bXZR%2BkkQDGWlHd0BpSlFY88uT%2Fh8UJksgxmfcAfqWL%2FWh%2B79Awua%2Bd1VOSIsFD7RKP4Y5aUjCiyd91MXqI6fhF1XD1MEHkD%2BFZQC6lOdf%2Fbb%2BlPY%2FYESacvY%2ByWricwpfLLyQY6pgHq6S4GUXWsBJ8P%2Byj8N8mMT9RZ4ExLeB2IwVvZFLnk9yyU71nptrHaeWaXNaNTP5QUw3qMfyoXQmCADlsQPyYFa4xTnL%2BC1U0cgQLnfhkJeC9imUQY7NC6q7Yllpuamkno3RLlSns8dCFzsMdim7FIqw5wmAIQuM0CSIgk7CZTgqzrKWuHwwDOJbTxK8uF4DmIVc08%2FFQx%2FefKkTZrU6EO0eeusBxO&X-Amz-Signature=23ca477250bab6966dc6211a66e34925054014af155c3db4723af25d4aad3ffe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYLQ2XA4%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T182102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG28Uad5rFL%2F1laZEwbN6vXpJnnipfkClkyEWSCxEF%2BUAiBKlcX73q9ro0Hxo4wTA7%2FCY6Aorq8Zn4tz2omalwWogSr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMaRntURoeWaNFYrtBKtwDXgrix31n9RUB8asZQsgadZ42J6xYDoyPpMSr9hR9cAbdwDS00ODq32TI1xGRhV%2Bz52QYCAVd59hyg7roLvSeeDZm8GN9k%2FGW%2B6xhg7IkCB8av8NR54vDiTIqbqDQDgnpk%2FYxdKgmuPvJVBN%2FXvnMILvlPsWX97qs%2BUgfUThs7pjRKmYP0oazMVdvqvFE6A1OHvJJFCDYj9FTi%2BsxQKCID0U6hpKgRuE7B6aVm%2FyOzjd5TBbCii9ojhJ5lACM7eRTgpTvb8HxRxNr9rfI7HMOuefGE6ezDUy3dt%2FTyuzobkZOTWYYOOGopEYMP4YASQBtzETvEkJ%2FQIWF6WrBMb8bl8Wr5WNp0iEpqsNbU9b8Yw%2B3W1BJxe656DUM%2BvZWhCGPYvGfqXDQZLUIlqLEYNwNodJU%2Ftr%2FuqmcIPpK4CJJqzuDpFasW4ZOspscrRLBYZkCba0iwBMALfEuKXXDiNuQzcgAlb%2FNg4szRbVwtL3ralNw%2BD7ylzIcA0KD4XA09bXZR%2BkkQDGWlHd0BpSlFY88uT%2Fh8UJksgxmfcAfqWL%2FWh%2B79Awua%2Bd1VOSIsFD7RKP4Y5aUjCiyd91MXqI6fhF1XD1MEHkD%2BFZQC6lOdf%2Fbb%2BlPY%2FYESacvY%2ByWricwpfLLyQY6pgHq6S4GUXWsBJ8P%2Byj8N8mMT9RZ4ExLeB2IwVvZFLnk9yyU71nptrHaeWaXNaNTP5QUw3qMfyoXQmCADlsQPyYFa4xTnL%2BC1U0cgQLnfhkJeC9imUQY7NC6q7Yllpuamkno3RLlSns8dCFzsMdim7FIqw5wmAIQuM0CSIgk7CZTgqzrKWuHwwDOJbTxK8uF4DmIVc08%2FFQx%2FefKkTZrU6EO0eeusBxO&X-Amz-Signature=559f1bad076dc074e70f5850cf58ea36098225ea541331fbf534941b6de1abce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







