



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKBGELE7%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T001630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnN6QrQydIDP7r5cbM2bw1gszTLR2GOEmPrw6uHrcNcwIgBUkk%2F%2BcgEkLTYWydJiwIBpWRjKrjFPjIn4FXX53Po6Qq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDO%2FxV4Fry60U24p2OircA0LF6n4sNL44sdh9%2BcN2MEpwIEOCDgkidc9BgTK5E%2FEU7PIzdFJ4f0%2FkaXbfXVHSJQSsTCC7yFnt3ISrEX4uOQ0HAp8%2F1Y6PAx7pkNdArx7Yr0qpyQc%2BW2R2W4PlpO96PnJa%2BWTyBHt6qYp%2BZYZD1AcVUXdF21UH0QlHKvMsE4fOXo%2BpMpGJ0BNbinOThS3%2F9CaydA03s1%2FmhQoqdIt7c%2FADWgbPggP480NjTNiMpyrhkVE0EZhS74FJkiBVg8BhXpdiPQJq6MG0psOxNg9gZoCXOwYC93njR9hdNNigP8qSKVV%2Fz0w6IDrJKQZOQYYVtxIr4DgZTi95SWAJ%2BYNqb5IYjUTAEkkMaRknpdFWOQ7PmDx6JTQD%2BvnVPmadY8QvuHjIkRRIZalUXfr6VIe5Inzl0c3kk2NyM%2B21%2BZWXoA9sPyd3j%2Fe1wn9p3EeMvDwe0aojDa4eqayDgiMIjg2IAfUfEeFJHIkOHjhZoauHuqOQfO9oKOFnzlPNA%2B1ewS5UAg%2B7o2GUAUslyJ%2BfMEjz%2FQPw4tOzappwv10ehFVukIwCbrneddkbxN%2FMe%2BckQv%2BP2HphXsRDhKU6AHLi6LZnLXNMpxswvDQ5KbjR0T%2FOjmMkKifKrfXDHIURGpxMMKHPmdcGOqUBhk5kdgvsP0ztjss4yo8ceUqRyOqCUzEE6%2BnIe2oXAS%2F0%2B%2BXVXfAjDs2hvLXtC2Clen%2BlWIy5cZo17TTtAC7hWQbBJa%2B5plfJZrLPO4Nl54OyKSktetVJERH5IUTOjCATmlX55eXA1QxnAnnLpqTgKPOW%2BpOGCBj9rIgQE%2FkrZtefW2iOmmABuUfpFw%2Bch4GOayF6aPJ4KT4qM1QZFqUUKjKlvBg%2F&X-Amz-Signature=32076852ab057de1661ed4635140f5f3b477c73cf84bdf7017d25739cd530891&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKBGELE7%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T001631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnN6QrQydIDP7r5cbM2bw1gszTLR2GOEmPrw6uHrcNcwIgBUkk%2F%2BcgEkLTYWydJiwIBpWRjKrjFPjIn4FXX53Po6Qq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDO%2FxV4Fry60U24p2OircA0LF6n4sNL44sdh9%2BcN2MEpwIEOCDgkidc9BgTK5E%2FEU7PIzdFJ4f0%2FkaXbfXVHSJQSsTCC7yFnt3ISrEX4uOQ0HAp8%2F1Y6PAx7pkNdArx7Yr0qpyQc%2BW2R2W4PlpO96PnJa%2BWTyBHt6qYp%2BZYZD1AcVUXdF21UH0QlHKvMsE4fOXo%2BpMpGJ0BNbinOThS3%2F9CaydA03s1%2FmhQoqdIt7c%2FADWgbPggP480NjTNiMpyrhkVE0EZhS74FJkiBVg8BhXpdiPQJq6MG0psOxNg9gZoCXOwYC93njR9hdNNigP8qSKVV%2Fz0w6IDrJKQZOQYYVtxIr4DgZTi95SWAJ%2BYNqb5IYjUTAEkkMaRknpdFWOQ7PmDx6JTQD%2BvnVPmadY8QvuHjIkRRIZalUXfr6VIe5Inzl0c3kk2NyM%2B21%2BZWXoA9sPyd3j%2Fe1wn9p3EeMvDwe0aojDa4eqayDgiMIjg2IAfUfEeFJHIkOHjhZoauHuqOQfO9oKOFnzlPNA%2B1ewS5UAg%2B7o2GUAUslyJ%2BfMEjz%2FQPw4tOzappwv10ehFVukIwCbrneddkbxN%2FMe%2BckQv%2BP2HphXsRDhKU6AHLi6LZnLXNMpxswvDQ5KbjR0T%2FOjmMkKifKrfXDHIURGpxMMKHPmdcGOqUBhk5kdgvsP0ztjss4yo8ceUqRyOqCUzEE6%2BnIe2oXAS%2F0%2B%2BXVXfAjDs2hvLXtC2Clen%2BlWIy5cZo17TTtAC7hWQbBJa%2B5plfJZrLPO4Nl54OyKSktetVJERH5IUTOjCATmlX55eXA1QxnAnnLpqTgKPOW%2BpOGCBj9rIgQE%2FkrZtefW2iOmmABuUfpFw%2Bch4GOayF6aPJ4KT4qM1QZFqUUKjKlvBg%2F&X-Amz-Signature=77cf1d1a62cc4eb497a8a27146a7e3570d3cae34a75a53b7404d8c66c196f441&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







