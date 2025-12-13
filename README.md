



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K4352BS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T011209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCH1Fua%2BNds6ft8dI7KQStfi86sJjJWQKyQAu8QTgLTHwIgT4ZdQD1OC6VrWmrakEc2hNAsvpVh2kRnBq%2Fkv%2BNp%2F5Aq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDEosvqjk3VNWycve7yrcA0%2BsRdic8lXyuF7Te9fSb3wRRd7eZlOSgccjUrqQPDfvCmpJDuwv9ixOuCB8uwx9aneUkSeXP6rZnSMar3uOjU3HSS%2Ba8a4WyKSxNK0pcYzkYbNJBkBid07aibKVZ0tWZLT0s175D4ejRGR4tFser9yg%2BPysnqDBkhVrV6x4YizEf5JfPnjRs9YdtyQ%2BF0Nn5JoxWIZd3BdXvNycdEEQD9Mbohzb9%2BZDMNm4%2B0M8XqZAL4%2BUF7yetjYSFK0DtuN5DzORJlNj9oun45e3luv1ZgC9Ch0tc9aC1Z%2B0y9VRMjChePD2yepjLkwF6XtQZ7oN8jixIU%2FgytO%2FkaWis8pjxfca7Z%2BEbOaW9o2T%2F7MWvX5XYCP7ZHKNfiAbXhVBt3pRFrBszwvRiSjGeOQYrVsGOcpLRrT1AD%2FVIX6sDzhlSb3%2BujYM%2BnIwjlz9C8YQXl9uz0wDltzc4dHYmpVH9f3gIBd%2Bbcwt3VrNQF9iRtYeskPyzGVU4tANj4tn591fdnpMjMF3nWI5beliSFveoJ7713YFepEZoJfFj57vB0d%2B1fj%2F9hllew%2Fn4YoV4AV40P7Wk6yGQjV9cFq5Z968mt3A%2BDjsU%2FLTbKPUw7eXOLzQWsFq4jA%2BhHi8%2F6uO%2B%2FdEMLPz8skGOqUBbM8uREANyvGL6L3SeZ4PWPQiyxF6nXVfhCH2UDx8brck3l4iS4eoNTV5ksM%2FgpgNvZcqNtCXXOjUKIpNwE3kvBsLwOQAs2v1NjrQ3tPu%2Bx8WmJFBb5ISi1uyWDZ2rTrR6NgX%2FiwuhdC5uwHKJqXgHrO5SJSqX1ujxfmta975IE9PB%2BrS6jPf0OGJ0Ng35Bc3yLTNAeBA6yXNU4VTavuxSstYsW8M&X-Amz-Signature=85180831b09c8091fdb33bb4c27390ad03103befde620f97eba3b62089c411d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K4352BS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T011209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCH1Fua%2BNds6ft8dI7KQStfi86sJjJWQKyQAu8QTgLTHwIgT4ZdQD1OC6VrWmrakEc2hNAsvpVh2kRnBq%2Fkv%2BNp%2F5Aq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDEosvqjk3VNWycve7yrcA0%2BsRdic8lXyuF7Te9fSb3wRRd7eZlOSgccjUrqQPDfvCmpJDuwv9ixOuCB8uwx9aneUkSeXP6rZnSMar3uOjU3HSS%2Ba8a4WyKSxNK0pcYzkYbNJBkBid07aibKVZ0tWZLT0s175D4ejRGR4tFser9yg%2BPysnqDBkhVrV6x4YizEf5JfPnjRs9YdtyQ%2BF0Nn5JoxWIZd3BdXvNycdEEQD9Mbohzb9%2BZDMNm4%2B0M8XqZAL4%2BUF7yetjYSFK0DtuN5DzORJlNj9oun45e3luv1ZgC9Ch0tc9aC1Z%2B0y9VRMjChePD2yepjLkwF6XtQZ7oN8jixIU%2FgytO%2FkaWis8pjxfca7Z%2BEbOaW9o2T%2F7MWvX5XYCP7ZHKNfiAbXhVBt3pRFrBszwvRiSjGeOQYrVsGOcpLRrT1AD%2FVIX6sDzhlSb3%2BujYM%2BnIwjlz9C8YQXl9uz0wDltzc4dHYmpVH9f3gIBd%2Bbcwt3VrNQF9iRtYeskPyzGVU4tANj4tn591fdnpMjMF3nWI5beliSFveoJ7713YFepEZoJfFj57vB0d%2B1fj%2F9hllew%2Fn4YoV4AV40P7Wk6yGQjV9cFq5Z968mt3A%2BDjsU%2FLTbKPUw7eXOLzQWsFq4jA%2BhHi8%2F6uO%2B%2FdEMLPz8skGOqUBbM8uREANyvGL6L3SeZ4PWPQiyxF6nXVfhCH2UDx8brck3l4iS4eoNTV5ksM%2FgpgNvZcqNtCXXOjUKIpNwE3kvBsLwOQAs2v1NjrQ3tPu%2Bx8WmJFBb5ISi1uyWDZ2rTrR6NgX%2FiwuhdC5uwHKJqXgHrO5SJSqX1ujxfmta975IE9PB%2BrS6jPf0OGJ0Ng35Bc3yLTNAeBA6yXNU4VTavuxSstYsW8M&X-Amz-Signature=2d052723e3bba2f96795764d32ff8c8e54f982470ee97413b699c9b422553e69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







