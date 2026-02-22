



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MBEL24I%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T182824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCtfflt8DA90o8j%2FRU54UQL8pYPjD7nkXRq%2FElc78AXEQIgTTMNA4pCZhc5UXv1NRZd2kDbed0HlblAmS6WY%2ByRI3kqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErnFG1M8ftkcJoY2yrcAxPeZMHyFaoL3KQexvVmDyLZIenvD98CgkKQ3cNC6Ks65ltt6cm2Pong%2B6FC0nB9HcGByL92dVOQsVh9Yjxy8Hgc1%2BGUTioqPBLxMmZetmRBSmtyCreResMjzyQswBxI2FCdBG%2Bc59%2FVQKTRumENCmbEAe6%2BLaHAQEXXGIkWk0HrI7k3ubH%2FV7CVClyZf9gRFQnEHT8mFHVGgJY1QZL%2BlOZmx4XbWRQqm98ghBQSHfMYkLEAYtT0grmU3lshN97TbWdhOCN0lhF9o4IMf4iw6WkONdlvSrsQGW%2FBCdbmiVnOw%2F2lnhXllnmMF8sm1ECo3IoVjmOb0QkNQkvckxAwzvictww0Z8ybqz0whLpZFezjgKNcqEghYpPczzNi3lp%2FQi8IVvnrMjTjgXvjLV0LXvyWBZfZDPw9ETAUfcxaU%2BR1ak6LIG6IDVyQ7LkqvL3BuyGgZYy5gdhlql58VQ3jTxQDRm4ylIRqAmzXFQvXwggZ73W70Qbd4%2F6ydu43SBOUAmvkfdbol%2FED1pPx%2FNiz%2B%2BuBqiXYJ2Wzo6yFmFxNcXRiTNDbBTJTlFix5YoGIz1RKQByZX%2Fcgd1HT5rvdR%2B%2FiNVDX8ZcEGhw6ldAQaKFpWGDKQh%2FUlUAAb90WHRaMNyE7cwGOqUBBP%2FG6Dn4Xkrk4Jwl0EgdKW%2F6prLJ1W%2B2aVEQFjj8x2FD9mtTEk9%2BrP1flKy3QUijUBfmOsAPKTC9Hh%2Bji8Ru1xHIK%2FOBMfYN7rgIYvB90QAa13u7UKNmgkQ12vtXC6k%2BT6hZDpWqpU1D%2FlMDZjCS8metREmCZHNXs1NyCIPrvU%2F8Xz3kWNd1Qoc9C%2Fe63Rxjcz20FCxR%2BB%2B1cfAfU8WEU%2FUcyi%2Fe&X-Amz-Signature=ae78fa0acb4d07caf2b2a140a0e404c4b217e7c78ddfe92ebded29f94dc393e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MBEL24I%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T182824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCtfflt8DA90o8j%2FRU54UQL8pYPjD7nkXRq%2FElc78AXEQIgTTMNA4pCZhc5UXv1NRZd2kDbed0HlblAmS6WY%2ByRI3kqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErnFG1M8ftkcJoY2yrcAxPeZMHyFaoL3KQexvVmDyLZIenvD98CgkKQ3cNC6Ks65ltt6cm2Pong%2B6FC0nB9HcGByL92dVOQsVh9Yjxy8Hgc1%2BGUTioqPBLxMmZetmRBSmtyCreResMjzyQswBxI2FCdBG%2Bc59%2FVQKTRumENCmbEAe6%2BLaHAQEXXGIkWk0HrI7k3ubH%2FV7CVClyZf9gRFQnEHT8mFHVGgJY1QZL%2BlOZmx4XbWRQqm98ghBQSHfMYkLEAYtT0grmU3lshN97TbWdhOCN0lhF9o4IMf4iw6WkONdlvSrsQGW%2FBCdbmiVnOw%2F2lnhXllnmMF8sm1ECo3IoVjmOb0QkNQkvckxAwzvictww0Z8ybqz0whLpZFezjgKNcqEghYpPczzNi3lp%2FQi8IVvnrMjTjgXvjLV0LXvyWBZfZDPw9ETAUfcxaU%2BR1ak6LIG6IDVyQ7LkqvL3BuyGgZYy5gdhlql58VQ3jTxQDRm4ylIRqAmzXFQvXwggZ73W70Qbd4%2F6ydu43SBOUAmvkfdbol%2FED1pPx%2FNiz%2B%2BuBqiXYJ2Wzo6yFmFxNcXRiTNDbBTJTlFix5YoGIz1RKQByZX%2Fcgd1HT5rvdR%2B%2FiNVDX8ZcEGhw6ldAQaKFpWGDKQh%2FUlUAAb90WHRaMNyE7cwGOqUBBP%2FG6Dn4Xkrk4Jwl0EgdKW%2F6prLJ1W%2B2aVEQFjj8x2FD9mtTEk9%2BrP1flKy3QUijUBfmOsAPKTC9Hh%2Bji8Ru1xHIK%2FOBMfYN7rgIYvB90QAa13u7UKNmgkQ12vtXC6k%2BT6hZDpWqpU1D%2FlMDZjCS8metREmCZHNXs1NyCIPrvU%2F8Xz3kWNd1Qoc9C%2Fe63Rxjcz20FCxR%2BB%2B1cfAfU8WEU%2FUcyi%2Fe&X-Amz-Signature=002d0555ad986b137425d3ee46d1e106524398cdd37131bec63f9bd8d4d1a12c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







