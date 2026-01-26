



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUTOZR%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T123757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDUmOGvJxHYoI6JSRi8IA%2BrdL6vJQohea1n8njOhGii6gIhAJsiLzCbX57UWbt1eo2ZSkLoNTIGB1Ezcdn60vG9k5QpKv8DCD0QABoMNjM3NDIzMTgzODA1IgyhQd17hSgcVhFxL38q3AO22Xsry17ujvH2e%2FQdQw1MVBgQ93ez8%2FPZVlbpKwfG7ifYcMYOylesUklHt7nDVNrfuUS8aPeUNFuVQbaXdlDZjNhV4BYlqaDM24KGq0w5P2RKmMR94fiV5lGmHlO1xoDwd694MR4bhHfENGRA%2BJeDWDJhMeaG2H0RYDr7VvJTeQtiz8tIytyT7N2NY7pB3ht841bxJPYgKp4NBzOU6ZnSmIgh%2Fignv2QSAfy8wvT9Dyv6S%2BeXCo4mwZLwwRT1lo8T12qAZVC226%2FQcDF1%2FDI4Gv2BIgrw5TyZ1934j6spefh8lgipIDojq%2BhD%2BI2nvKfHFTmvlWIfkFdejlvrvrAWBMCfQWEoq0JqftKfR0lWkPRvwSYkLAWQj7FArYPGcVPdUNTQEIETb%2B2wd%2FiN4EehKDf2M6aBjqCAvxkyUKmJyJ2oBl26WGiwaWJUNSi2UWyUhenfV04d8lkyNLsMCfNkWQqIe8dPp5HzstEUbcq2tzf28f3X%2FkCErQqyONpHnWzIU5hE%2Fbjclqlfl%2BpPqXL996HK3VjVBoEQzLZddELTeCC3MLPiK1hdDXGGpNxkUqzv1ibGWMuiBtM0rgVtzco3JzYFocuVn4fsUYSwGXv4ITdyMD5%2BgeywaPVOzjDhtN3LBjqkAVrjPdVAihk%2B0Xvpor5MMsViTV7WMZgo3pCKQ%2BAG3u%2FjSSkVMVKn2oy%2FrY%2FIrXC0b2zr6a6%2BbMG5%2BwdXSJZ4q4%2F5dW3HqKhP9mrvxSlelGGMFt4sEIh%2BFwxJ1%2F1qKNV1IoxBaR4FqoJxO3UnrPT4dinqC%2FRUGF57QlUXE8%2FciADYBsZTW5mYNWFwrhkxCSmXVDQbGUJ995lneolOFvPM61%2FSpES3&X-Amz-Signature=0b80bcd45a615c7414e8fba3bd7c5d7cf8cf48220cc8d8f487996dff35d449b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PZUTOZR%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T123758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDUmOGvJxHYoI6JSRi8IA%2BrdL6vJQohea1n8njOhGii6gIhAJsiLzCbX57UWbt1eo2ZSkLoNTIGB1Ezcdn60vG9k5QpKv8DCD0QABoMNjM3NDIzMTgzODA1IgyhQd17hSgcVhFxL38q3AO22Xsry17ujvH2e%2FQdQw1MVBgQ93ez8%2FPZVlbpKwfG7ifYcMYOylesUklHt7nDVNrfuUS8aPeUNFuVQbaXdlDZjNhV4BYlqaDM24KGq0w5P2RKmMR94fiV5lGmHlO1xoDwd694MR4bhHfENGRA%2BJeDWDJhMeaG2H0RYDr7VvJTeQtiz8tIytyT7N2NY7pB3ht841bxJPYgKp4NBzOU6ZnSmIgh%2Fignv2QSAfy8wvT9Dyv6S%2BeXCo4mwZLwwRT1lo8T12qAZVC226%2FQcDF1%2FDI4Gv2BIgrw5TyZ1934j6spefh8lgipIDojq%2BhD%2BI2nvKfHFTmvlWIfkFdejlvrvrAWBMCfQWEoq0JqftKfR0lWkPRvwSYkLAWQj7FArYPGcVPdUNTQEIETb%2B2wd%2FiN4EehKDf2M6aBjqCAvxkyUKmJyJ2oBl26WGiwaWJUNSi2UWyUhenfV04d8lkyNLsMCfNkWQqIe8dPp5HzstEUbcq2tzf28f3X%2FkCErQqyONpHnWzIU5hE%2Fbjclqlfl%2BpPqXL996HK3VjVBoEQzLZddELTeCC3MLPiK1hdDXGGpNxkUqzv1ibGWMuiBtM0rgVtzco3JzYFocuVn4fsUYSwGXv4ITdyMD5%2BgeywaPVOzjDhtN3LBjqkAVrjPdVAihk%2B0Xvpor5MMsViTV7WMZgo3pCKQ%2BAG3u%2FjSSkVMVKn2oy%2FrY%2FIrXC0b2zr6a6%2BbMG5%2BwdXSJZ4q4%2F5dW3HqKhP9mrvxSlelGGMFt4sEIh%2BFwxJ1%2F1qKNV1IoxBaR4FqoJxO3UnrPT4dinqC%2FRUGF57QlUXE8%2FciADYBsZTW5mYNWFwrhkxCSmXVDQbGUJ995lneolOFvPM61%2FSpES3&X-Amz-Signature=4996ccee5925239e721ddac04882787991f5601cd7bb7a265f94c4c10fa8d3f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







