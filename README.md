



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPN7WCTQ%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T212606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCDBdAgAMUqXVYBrouRZzf9mmiQxCEIMVZKR%2Bw6Ps6oCAIgYH56egQ%2BRk4I3wUsAmFsopeSC344fOMIG5ZzU0dJjT4q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDCdCJN10V1kIqWYFwircA0JlBD%2F0RGrHrk6y%2BAOWJuszR5gAXu43mRTHw1SmOaX%2B%2BdPM%2BVM6LmpGiuWbZqKeGIfJpcs%2FX8xFBfx4lnl2XWUFQGlNVU1Jv%2BmuR4XQSJzYdCDiPj0oPBIspdi9iC%2Fn0Jp4raRx5uDHLjR8upotOaYHo0Y%2B3eGJXBueyZ7dKrrmIYFqEP1TyxWPVnmuKPOyeAvGOgUPDFHqsn2%2BViEMTGxgFY0XNXfvLFW%2FGxqNsi6C%2F5LecqJA8Mzn1zcvKZLq2nmPRV6uyyJb258eGj39lpe%2Fn4Qk040HPdTUl3zC8wkoPBor7oWaPkgXXeXjX8rEaKfnxLG5fc42wG2cBgLFuL%2BqyKVHtusls7uWZ4cJ%2BGruvMRekTTbH7wYagppABHcs6TrbVxhmnJGTvKNpXeuCTu45EWMm6QLMymmbH0eS6hZl%2FSHLZjLzsg6BEq9VokQqemFD8jR1fHukQLsuzancb0xfvbbOdhxDLXuKfk8%2BL%2Fc1DgsUuqfJHbF38Rmdn%2BlZXZoKYW8OO%2Ftk%2FpoE3gG%2BSOoKoACKsQ%2Bb0T35vaDV3UoSZfHoY7gPIZ5ilXMA1HDd4G2a1I2xoQXcUwk5pJg0yZvKeM4U%2B3EXwMvmBoIB9Wj38V0Fu1jvV7De3R%2BMLnc99AGOqUBGTWwlnHRnD%2FgSolONThoWkAwIYHkliuv6lKGNMcYKBzIwgm%2FUl7ktB1LqcB00u7InZDPSS5qv4tbH9wFkgdO3rWGgrXYeYHtAAJYjiYXEvRphJdN5wa8P2e9wHc5YgMIX6U0zScs9n68BHQ%2FfYBjbAApKgUIpdzqAx8uY42H9WKRSoSUfO3zjBo6yDai2vfrDiyD0DlD7R1J1MEBvvrXip%2F233aT&X-Amz-Signature=ea7cb0d708f99d8ebd302b5b837d16aef14507a815d33ce6e272bd66fa2fab9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPN7WCTQ%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T212606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCDBdAgAMUqXVYBrouRZzf9mmiQxCEIMVZKR%2Bw6Ps6oCAIgYH56egQ%2BRk4I3wUsAmFsopeSC344fOMIG5ZzU0dJjT4q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDCdCJN10V1kIqWYFwircA0JlBD%2F0RGrHrk6y%2BAOWJuszR5gAXu43mRTHw1SmOaX%2B%2BdPM%2BVM6LmpGiuWbZqKeGIfJpcs%2FX8xFBfx4lnl2XWUFQGlNVU1Jv%2BmuR4XQSJzYdCDiPj0oPBIspdi9iC%2Fn0Jp4raRx5uDHLjR8upotOaYHo0Y%2B3eGJXBueyZ7dKrrmIYFqEP1TyxWPVnmuKPOyeAvGOgUPDFHqsn2%2BViEMTGxgFY0XNXfvLFW%2FGxqNsi6C%2F5LecqJA8Mzn1zcvKZLq2nmPRV6uyyJb258eGj39lpe%2Fn4Qk040HPdTUl3zC8wkoPBor7oWaPkgXXeXjX8rEaKfnxLG5fc42wG2cBgLFuL%2BqyKVHtusls7uWZ4cJ%2BGruvMRekTTbH7wYagppABHcs6TrbVxhmnJGTvKNpXeuCTu45EWMm6QLMymmbH0eS6hZl%2FSHLZjLzsg6BEq9VokQqemFD8jR1fHukQLsuzancb0xfvbbOdhxDLXuKfk8%2BL%2Fc1DgsUuqfJHbF38Rmdn%2BlZXZoKYW8OO%2Ftk%2FpoE3gG%2BSOoKoACKsQ%2Bb0T35vaDV3UoSZfHoY7gPIZ5ilXMA1HDd4G2a1I2xoQXcUwk5pJg0yZvKeM4U%2B3EXwMvmBoIB9Wj38V0Fu1jvV7De3R%2BMLnc99AGOqUBGTWwlnHRnD%2FgSolONThoWkAwIYHkliuv6lKGNMcYKBzIwgm%2FUl7ktB1LqcB00u7InZDPSS5qv4tbH9wFkgdO3rWGgrXYeYHtAAJYjiYXEvRphJdN5wa8P2e9wHc5YgMIX6U0zScs9n68BHQ%2FfYBjbAApKgUIpdzqAx8uY42H9WKRSoSUfO3zjBo6yDai2vfrDiyD0DlD7R1J1MEBvvrXip%2F233aT&X-Amz-Signature=d98222975a15a5586e9dd793b2157118f897dbaf20c1c38311897525cfb5d65a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







