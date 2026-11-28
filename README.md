



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGFC2LI5%2F20261128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261128T120631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIQDkSJPmM%2FrmfOqBwAYLzNrfcjGyMF2qJm4fKUAey3co8gIgdkhLF5lE5LKm%2Ba9bAN6UF5Vt5GK8GIOVR9eJmBgdyYUqiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrK8bnTT3%2FFjyIKoircA40MO91E4AjZ5YSldPnYBZVfDEDgbDj1WRmj6WrULMlD%2BNLVcdVVXCQJYFnysaUqtODW3tvXLT4StE6OcBpF6DOn%2Bxl3LRj7dzrrfQSo0k7SAxRlRcn6YTwy9hWXTdNGl4B26Y1bsVs8Cjj3sTRE3NwuIkS7XBxcp2t2reZuSR%2FNBF87lADy96UTqmE64IzI9QqMyKzRYMXwqcLwqnL1ZJIjWlM1bpgOfHBQeSidmWpXmjDV6OSe9MXF6%2Fv5cqdSXxOzUeGu5NDWqYpBitZ1mBy0dl9JUH84t5yeej3y7Rovt5pEoTU84qD5OmjvR6TLPp3gHfXCZWZfwVQos4sCJ%2FTnnfYB9JyegU73sXRPqXZ5eH3cXksBo%2B5ntPpk5Vt6FFlL%2BKXCIoPelBykGpECxD6jd44%2FGSansOiLn7kKlEHD09ygv7qvpWNN%2Bl9BK44LqSVqPK%2FaPA9EolM5IB8YLvcaA8rn75PqQIcgZzLzbNxqgVO%2FygbcOTUynf4RTva8q%2BjriSFCisJ1n0V5AoqRr45%2BtSQqQRP495IEDkspC05SKFX9iWZZSsOHHtSSE5gAXbFJT7F8iCq3f8PPbgA7pOJI1tPiNA6dNX94s23j%2FnrbZIH7DsS7nJsonOJoMIz%2BqdgGOqUB7n40VKhUO6k0dA8sExIg2Z8n7l6IUGNOH7xVKglE79099tTtIMXWBbr1bBXMuQl%2FZr2xoWTlmYUQvq%2Fy4HYvoVFUf9kmNWvdHR01KUn9Ifarl8UzRU5yEwN5DwBaabYU5kp6es7GhnXBHX4M6T47ERTCwjm680Fg8cYnB3noz%2F4j%2FyScUJcWuVJGiurHimEOOwf1gvpmmfPGmRrbCazPZzrzgOjn&X-Amz-Signature=d9b6bb2b6f17cd5112ff5e8090f744eb4908385c3cab8e341feb1052e0276359&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGFC2LI5%2F20261128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261128T120631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIQDkSJPmM%2FrmfOqBwAYLzNrfcjGyMF2qJm4fKUAey3co8gIgdkhLF5lE5LKm%2Ba9bAN6UF5Vt5GK8GIOVR9eJmBgdyYUqiAQI6P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrK8bnTT3%2FFjyIKoircA40MO91E4AjZ5YSldPnYBZVfDEDgbDj1WRmj6WrULMlD%2BNLVcdVVXCQJYFnysaUqtODW3tvXLT4StE6OcBpF6DOn%2Bxl3LRj7dzrrfQSo0k7SAxRlRcn6YTwy9hWXTdNGl4B26Y1bsVs8Cjj3sTRE3NwuIkS7XBxcp2t2reZuSR%2FNBF87lADy96UTqmE64IzI9QqMyKzRYMXwqcLwqnL1ZJIjWlM1bpgOfHBQeSidmWpXmjDV6OSe9MXF6%2Fv5cqdSXxOzUeGu5NDWqYpBitZ1mBy0dl9JUH84t5yeej3y7Rovt5pEoTU84qD5OmjvR6TLPp3gHfXCZWZfwVQos4sCJ%2FTnnfYB9JyegU73sXRPqXZ5eH3cXksBo%2B5ntPpk5Vt6FFlL%2BKXCIoPelBykGpECxD6jd44%2FGSansOiLn7kKlEHD09ygv7qvpWNN%2Bl9BK44LqSVqPK%2FaPA9EolM5IB8YLvcaA8rn75PqQIcgZzLzbNxqgVO%2FygbcOTUynf4RTva8q%2BjriSFCisJ1n0V5AoqRr45%2BtSQqQRP495IEDkspC05SKFX9iWZZSsOHHtSSE5gAXbFJT7F8iCq3f8PPbgA7pOJI1tPiNA6dNX94s23j%2FnrbZIH7DsS7nJsonOJoMIz%2BqdgGOqUB7n40VKhUO6k0dA8sExIg2Z8n7l6IUGNOH7xVKglE79099tTtIMXWBbr1bBXMuQl%2FZr2xoWTlmYUQvq%2Fy4HYvoVFUf9kmNWvdHR01KUn9Ifarl8UzRU5yEwN5DwBaabYU5kp6es7GhnXBHX4M6T47ERTCwjm680Fg8cYnB3noz%2F4j%2FyScUJcWuVJGiurHimEOOwf1gvpmmfPGmRrbCazPZzrzgOjn&X-Amz-Signature=8a5ed1faee105a88df4a71543896f5bf7ca064d5362b83c673565f2b63ba8641&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







