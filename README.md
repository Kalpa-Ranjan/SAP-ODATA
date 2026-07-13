



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLJFJNH%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T191718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDHef5BJlDkEan7PSj%2FXxfb3Wu9M2bH9jhtSKUwtmZctwIhAPmzlexEWmdhoWPxYBsClWiYoiXO8li814XIj%2FendCVWKv8DCAMQABoMNjM3NDIzMTgzODA1IgzqQKje6gtzmG0z794q3AOgkFFEYuimI8CmTQwZgj%2FUWzt%2FFwal9Hbg5PF%2BVklFai91s1DJ3MTQSu67ox7oPrJ9eK1QHUS%2BaeiteGSSmEVPfHToouTRhQvVMYgZ0UXIVjYV52ZVjhmJ0ZzZTfbLbQt7r0Qn5MCX%2BbcZtcEqDOpJhhqaWZOzkz%2FSjBq7pHkULT5MR096dbbXn6r700kdJ%2Fima36zHLiDdwvsyVlO1MRmUd8lH7TJxkB2lvVQy9VgDvpSNITchVCeGW9l0Z3rmFxSDCsRJ49A9RWYwe0hUdj8Va7kLIiHvD%2BljJhajbIwBsMGADH3IKqGZEN16HC4lIOiPvnNygiIBnZRcS84KaodeVoezLbBaRxbBWOVmdcdcNxTekHGetjyw%2BRVE9SQUxVLP4g%2BgTL8vLLL%2F9Y%2BCvvIrBFm4KETzuvAI8vSWpl6LZoVlWmu1uBlQ5XtwAh2pWCA73GH%2F%2FCDTy9NPuUnKMb0%2F6kq8Xu1o0RWlyp0rXB7dg1Rsfg2vhDIV7BsyitBz%2BZKPiWXlfS%2FPWcWM0HbuTc92G%2BH%2FD39Ou4zRypAhzv5jdBPG9et14XT88H1oFUWwG%2FS8JFzzwr1hf4kzGocL1vXSGxl9Jxpp0NceaPoi5deSY4FZRIqrb%2FatsiN9TCp1NTSBjqkAU%2B9PqvNjnUErdZNky%2FElJADH3iQkJ3yw2hQllm76u18D%2B3ACnYvn%2FZscwuRRJY%2BlNpvbFiQg3mkfAYPOAroTgIWeL7YM6EE4nD6jvBBnbUFKUKjJdzoYTGucCzLpwOyOwJ5%2BwqQy4Xi0i%2B7m%2Bg59FNdvJcGW%2B0x9lSqBOxEuQUCj7gULi1YA7ReazS7H7n6B1NM7PQ9tzlyyzplkbuf5hrTVxry&X-Amz-Signature=e9ce573197d6a1574a4fcc8510e6dfcac584ee99137c191e33abddbd0b5e06c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLJFJNH%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T191718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDHef5BJlDkEan7PSj%2FXxfb3Wu9M2bH9jhtSKUwtmZctwIhAPmzlexEWmdhoWPxYBsClWiYoiXO8li814XIj%2FendCVWKv8DCAMQABoMNjM3NDIzMTgzODA1IgzqQKje6gtzmG0z794q3AOgkFFEYuimI8CmTQwZgj%2FUWzt%2FFwal9Hbg5PF%2BVklFai91s1DJ3MTQSu67ox7oPrJ9eK1QHUS%2BaeiteGSSmEVPfHToouTRhQvVMYgZ0UXIVjYV52ZVjhmJ0ZzZTfbLbQt7r0Qn5MCX%2BbcZtcEqDOpJhhqaWZOzkz%2FSjBq7pHkULT5MR096dbbXn6r700kdJ%2Fima36zHLiDdwvsyVlO1MRmUd8lH7TJxkB2lvVQy9VgDvpSNITchVCeGW9l0Z3rmFxSDCsRJ49A9RWYwe0hUdj8Va7kLIiHvD%2BljJhajbIwBsMGADH3IKqGZEN16HC4lIOiPvnNygiIBnZRcS84KaodeVoezLbBaRxbBWOVmdcdcNxTekHGetjyw%2BRVE9SQUxVLP4g%2BgTL8vLLL%2F9Y%2BCvvIrBFm4KETzuvAI8vSWpl6LZoVlWmu1uBlQ5XtwAh2pWCA73GH%2F%2FCDTy9NPuUnKMb0%2F6kq8Xu1o0RWlyp0rXB7dg1Rsfg2vhDIV7BsyitBz%2BZKPiWXlfS%2FPWcWM0HbuTc92G%2BH%2FD39Ou4zRypAhzv5jdBPG9et14XT88H1oFUWwG%2FS8JFzzwr1hf4kzGocL1vXSGxl9Jxpp0NceaPoi5deSY4FZRIqrb%2FatsiN9TCp1NTSBjqkAU%2B9PqvNjnUErdZNky%2FElJADH3iQkJ3yw2hQllm76u18D%2B3ACnYvn%2FZscwuRRJY%2BlNpvbFiQg3mkfAYPOAroTgIWeL7YM6EE4nD6jvBBnbUFKUKjJdzoYTGucCzLpwOyOwJ5%2BwqQy4Xi0i%2B7m%2Bg59FNdvJcGW%2B0x9lSqBOxEuQUCj7gULi1YA7ReazS7H7n6B1NM7PQ9tzlyyzplkbuf5hrTVxry&X-Amz-Signature=a8d941d15f874e2a9552edb0f299e8c474e60ed1da5ffff9d006f458d68887ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







