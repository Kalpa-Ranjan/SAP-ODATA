



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO6HEJT6%2F20261105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261105T060802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChyHL6%2FbFlyZWIJPQSn07Xl1oj8dbvMf%2BobBMsiwgInAIhAINU7oRsCyaSqNo2zwjzOjVKvxwxosl05YD3SjDq7YRbKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzoj%2FnPZSS83xUJnmMq3ANujAS6ekXKkqCr6RRZbY9WqLPbc5NOClRfhdD7dAafTfvaC4fK4NQhDgRQsc0XSd09hMG4kPWWVVgHT%2FP0%2Bp7dbmP8B0XDIjFiyDnC6Z%2BUqbIQSuJ6bURUVMsHgf6BmbvGV4NyIZ00aS0t3rJW6D32uXKjsr40g1%2B%2FsBWhYJ08TzWy3dQp65BG5%2BLv33oWqfcxxzYEkeAZfOLHvjVkR%2BOjfZGPSV%2Fu3qcTWTFz0Lt6QEDSwOUlA7TIDs4i7SMhzIU4QnQmhTVqorsE8Ur5guLCYr03tBpn%2B5O5H7mn5DSYpBCmKmyh6KsBhRuGXPshNHPkMJW3JVuxUrkfL%2Fh57q6uZ7ot6d%2F1ec2vhdrEP78uClcR7qoRjKkl2xinSZguKAQvPSAgcOTVJqMCRD4X9lJ%2B87UhjXHDwPa67NAKoA5ejTyfgEmz5zOhRzXbe2qWhXXEberD0BvopNKGixqbtVLxFnYNxACbciduD6E0GNqjaKYd9IYlML9ZTBERF%2FiWmrCSekyoZNo4LBXT59WCon6%2Bq%2Fcbav%2BgwIvo1IqqTHJ5mptI13zM9vGmbTSejb9vrbSBEkWIEIbF9T8JqhtJZES0Q%2FRpbAcLYVuXQGIl5Vf47AnZbQzCSCnbJnz%2BcTCcibDXBjqkATQ0MOyJE1hzbHt6%2BjWnv93eU3%2BiIi9jpRhf6GULp%2BCvjba%2Bn8GtWqpVMELGJabRMPgfKyMA2WI187Bzv8ZhyDllTt9giXEdp%2FJMZsddu%2BAnbGwt5PK6ee7GtYwiAfivqHFHf5BpRHw3c3VNAxd9lN7k7UbHBKXnrqOR9V%2F25mcAevVS6fv9MtX3iNuo6WEoJwtPSJPixHSzNc0dsL76UeAUTBY7&X-Amz-Signature=14a462ff81e39750a73599d3e6affbe3d0ead350f162076e90022c8d201f8221&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO6HEJT6%2F20261105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261105T060802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChyHL6%2FbFlyZWIJPQSn07Xl1oj8dbvMf%2BobBMsiwgInAIhAINU7oRsCyaSqNo2zwjzOjVKvxwxosl05YD3SjDq7YRbKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzoj%2FnPZSS83xUJnmMq3ANujAS6ekXKkqCr6RRZbY9WqLPbc5NOClRfhdD7dAafTfvaC4fK4NQhDgRQsc0XSd09hMG4kPWWVVgHT%2FP0%2Bp7dbmP8B0XDIjFiyDnC6Z%2BUqbIQSuJ6bURUVMsHgf6BmbvGV4NyIZ00aS0t3rJW6D32uXKjsr40g1%2B%2FsBWhYJ08TzWy3dQp65BG5%2BLv33oWqfcxxzYEkeAZfOLHvjVkR%2BOjfZGPSV%2Fu3qcTWTFz0Lt6QEDSwOUlA7TIDs4i7SMhzIU4QnQmhTVqorsE8Ur5guLCYr03tBpn%2B5O5H7mn5DSYpBCmKmyh6KsBhRuGXPshNHPkMJW3JVuxUrkfL%2Fh57q6uZ7ot6d%2F1ec2vhdrEP78uClcR7qoRjKkl2xinSZguKAQvPSAgcOTVJqMCRD4X9lJ%2B87UhjXHDwPa67NAKoA5ejTyfgEmz5zOhRzXbe2qWhXXEberD0BvopNKGixqbtVLxFnYNxACbciduD6E0GNqjaKYd9IYlML9ZTBERF%2FiWmrCSekyoZNo4LBXT59WCon6%2Bq%2Fcbav%2BgwIvo1IqqTHJ5mptI13zM9vGmbTSejb9vrbSBEkWIEIbF9T8JqhtJZES0Q%2FRpbAcLYVuXQGIl5Vf47AnZbQzCSCnbJnz%2BcTCcibDXBjqkATQ0MOyJE1hzbHt6%2BjWnv93eU3%2BiIi9jpRhf6GULp%2BCvjba%2Bn8GtWqpVMELGJabRMPgfKyMA2WI187Bzv8ZhyDllTt9giXEdp%2FJMZsddu%2BAnbGwt5PK6ee7GtYwiAfivqHFHf5BpRHw3c3VNAxd9lN7k7UbHBKXnrqOR9V%2F25mcAevVS6fv9MtX3iNuo6WEoJwtPSJPixHSzNc0dsL76UeAUTBY7&X-Amz-Signature=727db58adf5d307ce32e87a7cc9dce0cfe1071f291a169118fca6bcd106ffd36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







