



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKSYYTEC%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T095256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr3BG1tQlcrmOJqYfF%2FxK4nmD2Xq9IH6L9ardkYl%2F4IQIgNDccuMNcqgMeQAEdPWdRQ8wJBHDUK4w0nFdP74w6jcQqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTz1HTM8f5Aekjc%2BSrcA5uUZHg%2BCBIdPiqH5a%2FXLJZwzYpTvjm1R8m8Om%2BXrGOX7dpKv7Cq2ysTHvPV4AZ71cdgGB0g9vSX2jOPnHhvy%2FbH95341ZLUsyM%2BF1%2BtoH7syRp%2FGKlK%2Bdf41EokmYqmgNc1gAml5cOW0BW6HFbs6iqug2QlDM3PJVMwBwUDRl8qIWSIz6hi6Mtssgz0SOXrqeo4tK%2B0fYc6Owy8lkBQYvgyDJ9gbYyLNTXbPNM2KH%2BUjveSMtf76%2BBq7f0OsPy8GkM7YmG%2BMfDZJdpZ%2FqJ1pI4tvJdzf3HTn7HIDJue%2FPwghu1Xm5pc7fL8ygNHBHDRpKqakJtQBfow106KXCzhucBRrcIEkR2G%2Flfu7zUK2L4yD8KKECoQzKXWS9UDMmySDh%2BKmY242Lc4tGfUsFgMafQ8833YuQ0FhRi03wPtnIq35kVJFo7xzD6tYi3Slai6TsrOxxMCcRfT4s8kx7AKkr9Oha54f433wCC%2BtRLUJhsx0aQM64HtDSRt2XqPiF7XYeLjY9lUE6AliQApQLIpsb%2BTRxUISQucHBMXxMOcjMkshrR7BghR2WCFLpbjypXX6Qr2aCVZ286dk0qYmc9s%2FH40FktWJHy40PwU54Vcm7vZLN4eAFYTjyaHBL1EMLCR4NAGOqUByZa91noCqq6bT42jf1aHJKcDS72%2FpbdnvT6WPL2o55CXtMne3e4bJH0jxUfQXC9NB1JVXnFQknpEUhvr8klD4J5ahjIcyq1wYiWpVdE7e5WQ155jKrR6bPA%2FlMPmEXGQ%2BdU9Ud%2B9JXHRi%2BMymApkkC7iIFyYWMrOXIWbcxFFBik4PyYp4w0lQ1YZJFVWcFJkThCJMV%2ByRFos0P5XzKqQfhKAfkoh&X-Amz-Signature=49fd17dd850e104e5a2837fd7d96133594f7ee7574c80236238128709d04d8f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKSYYTEC%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T095257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCr3BG1tQlcrmOJqYfF%2FxK4nmD2Xq9IH6L9ardkYl%2F4IQIgNDccuMNcqgMeQAEdPWdRQ8wJBHDUK4w0nFdP74w6jcQqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTz1HTM8f5Aekjc%2BSrcA5uUZHg%2BCBIdPiqH5a%2FXLJZwzYpTvjm1R8m8Om%2BXrGOX7dpKv7Cq2ysTHvPV4AZ71cdgGB0g9vSX2jOPnHhvy%2FbH95341ZLUsyM%2BF1%2BtoH7syRp%2FGKlK%2Bdf41EokmYqmgNc1gAml5cOW0BW6HFbs6iqug2QlDM3PJVMwBwUDRl8qIWSIz6hi6Mtssgz0SOXrqeo4tK%2B0fYc6Owy8lkBQYvgyDJ9gbYyLNTXbPNM2KH%2BUjveSMtf76%2BBq7f0OsPy8GkM7YmG%2BMfDZJdpZ%2FqJ1pI4tvJdzf3HTn7HIDJue%2FPwghu1Xm5pc7fL8ygNHBHDRpKqakJtQBfow106KXCzhucBRrcIEkR2G%2Flfu7zUK2L4yD8KKECoQzKXWS9UDMmySDh%2BKmY242Lc4tGfUsFgMafQ8833YuQ0FhRi03wPtnIq35kVJFo7xzD6tYi3Slai6TsrOxxMCcRfT4s8kx7AKkr9Oha54f433wCC%2BtRLUJhsx0aQM64HtDSRt2XqPiF7XYeLjY9lUE6AliQApQLIpsb%2BTRxUISQucHBMXxMOcjMkshrR7BghR2WCFLpbjypXX6Qr2aCVZ286dk0qYmc9s%2FH40FktWJHy40PwU54Vcm7vZLN4eAFYTjyaHBL1EMLCR4NAGOqUByZa91noCqq6bT42jf1aHJKcDS72%2FpbdnvT6WPL2o55CXtMne3e4bJH0jxUfQXC9NB1JVXnFQknpEUhvr8klD4J5ahjIcyq1wYiWpVdE7e5WQ155jKrR6bPA%2FlMPmEXGQ%2BdU9Ud%2B9JXHRi%2BMymApkkC7iIFyYWMrOXIWbcxFFBik4PyYp4w0lQ1YZJFVWcFJkThCJMV%2ByRFos0P5XzKqQfhKAfkoh&X-Amz-Signature=0a25f65aca371a1cfca6e7db5b419db8c8c948063649fb8abe46cfcc79ee809c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







