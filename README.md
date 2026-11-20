



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CJKDH5L%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T120703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FsIfuEeI0m1DC8vDOxkZmtFU55FfUxx8hNqV0ZLAJAIhANl9ZKWo3OXOKvM5jzC3XgzR9lq8k9ZOUl%2BIt7Cb8TvVKv8DCCwQABoMNjM3NDIzMTgzODA1IgzgEmQttarKMy7bDgcq3APYrZdL8dUEkMlGFMyyZ52c4Sn3cASZ28LQm%2BrhyJDve2MF5JopTkxPrOLHL6zEWySFjLWrZO1Iuh9phUFCeChggwCexOsnFgbRy13A4ln8P5vXd8mAyJkgWrKy2EmkQih2umeDNw%2FiVy274MuscY2UpTUyKN6CF%2F8%2BeJn2wQI48uD%2FRtFPFHvzaxLrspDQEFILJHi8Fn5DlwyD5LeUSYvCaRh9wUQAt%2FfoCIL%2FRyXXdeWTot%2Bo%2BowWg2ZZKcmK0%2F48Agmt3U0hyqKOlCyej5Ri0jEHE0kozcz3uNCqbyuK24EljCHgYRZhRS3j3Ef%2FBxoIiEQx0SRhEqVHef71or2q56jGl14I0tQ92KS8B5utam%2FjDR8SKhOZlD1Tpht8oiinIXHcHLh9BOROGt0mScjKTbwraFRjqe3uGWGIU3aUWth%2B%2BlwGbUAaZ53YZC01inqLiANBNTVeItPIRPPrOdh2tNoaYrdJoGq6LOMg5GYP8ATO44pFiWslPkVP9kMLyjlc7DbmScDHH2UqDqff8FR%2FpzV4R2RiexMSbbW7lJVWhkhWTm%2F2uxtEwTecSVIjOFj9OH7dI2%2BqAby3ab22Q%2BS08JHJ%2BC6vVNSLZF9D%2FcvBNY%2Fk7P84m1Er8kUr9TCTyYDYBjqkAfiLBjs8EIa7MvzLwAEDucAI%2F3OgN%2F38vzsrYxJ4G3WWJROUR4Dn0ZwCYFlhIECZfVkVWFWWgkEDumsHwRcvgazeSwDh%2FWDgf%2FMIOvlEGv6V6zp3XjZFr3bfMq69brU4k9PtQPwy4gBf7t57IK4N4SlOUTp%2F6MpC17oIL5P8NcyiNJIrzDfCrqy62WY7IHyMfqhftQUdy70Gg7jaVhkjx2tpthL0&X-Amz-Signature=d38eca39261245f30b39efc508f381852889e13f991baedc9c83108d9c2fb9d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CJKDH5L%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T120703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD%2B%2FsIfuEeI0m1DC8vDOxkZmtFU55FfUxx8hNqV0ZLAJAIhANl9ZKWo3OXOKvM5jzC3XgzR9lq8k9ZOUl%2BIt7Cb8TvVKv8DCCwQABoMNjM3NDIzMTgzODA1IgzgEmQttarKMy7bDgcq3APYrZdL8dUEkMlGFMyyZ52c4Sn3cASZ28LQm%2BrhyJDve2MF5JopTkxPrOLHL6zEWySFjLWrZO1Iuh9phUFCeChggwCexOsnFgbRy13A4ln8P5vXd8mAyJkgWrKy2EmkQih2umeDNw%2FiVy274MuscY2UpTUyKN6CF%2F8%2BeJn2wQI48uD%2FRtFPFHvzaxLrspDQEFILJHi8Fn5DlwyD5LeUSYvCaRh9wUQAt%2FfoCIL%2FRyXXdeWTot%2Bo%2BowWg2ZZKcmK0%2F48Agmt3U0hyqKOlCyej5Ri0jEHE0kozcz3uNCqbyuK24EljCHgYRZhRS3j3Ef%2FBxoIiEQx0SRhEqVHef71or2q56jGl14I0tQ92KS8B5utam%2FjDR8SKhOZlD1Tpht8oiinIXHcHLh9BOROGt0mScjKTbwraFRjqe3uGWGIU3aUWth%2B%2BlwGbUAaZ53YZC01inqLiANBNTVeItPIRPPrOdh2tNoaYrdJoGq6LOMg5GYP8ATO44pFiWslPkVP9kMLyjlc7DbmScDHH2UqDqff8FR%2FpzV4R2RiexMSbbW7lJVWhkhWTm%2F2uxtEwTecSVIjOFj9OH7dI2%2BqAby3ab22Q%2BS08JHJ%2BC6vVNSLZF9D%2FcvBNY%2Fk7P84m1Er8kUr9TCTyYDYBjqkAfiLBjs8EIa7MvzLwAEDucAI%2F3OgN%2F38vzsrYxJ4G3WWJROUR4Dn0ZwCYFlhIECZfVkVWFWWgkEDumsHwRcvgazeSwDh%2FWDgf%2FMIOvlEGv6V6zp3XjZFr3bfMq69brU4k9PtQPwy4gBf7t57IK4N4SlOUTp%2F6MpC17oIL5P8NcyiNJIrzDfCrqy62WY7IHyMfqhftQUdy70Gg7jaVhkjx2tpthL0&X-Amz-Signature=499b9cba82b0830d9615614c8b77fca05563d29f5393d720f5df806aa41bfb9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







