



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4B7KVIW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T123402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIFBMJf6ZDTkoL89nIbR8gRi6VjzlahE%2FNPeW2zLpJIZ%2FAiB7k%2B0aD3GUaIe04LIFOqe%2FQBVOkUMcxjgkE4fyKYY2tSr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMa9lhYFIjf46jQEaaKtwDAfKUHct3Vk4VXW6L9onqASHco9AwuYILsNmPTAurao8MVEt7grQH8yqrM5Mpbcy8%2Fo54aRUqZ8Jh7rJOSejG7%2F5cQi8vSHU%2Fda%2B3o6vdEdQoNdn7YyP7CUKYy7h77fgJYCJy1A%2BsVvPjWwh1MYJzMF%2B8gTUjT6l036KjSuJgTWTiRo7TBA3ofMXXRzutRLEfP7zkoqkqzXr3Sr%2B52makyqTjPIBDhnpQwpEhmVfdThCiyOEK9CJu%2BnDD0Gl3IcufEivPQ7nR4iofACj%2FFqJ822ERcHQ43I%2BhLYQh2gzH%2F%2FhqFnjgeJpv5hn%2Fkly3PjZi74EHUc5x0kO6M0RvV%2BHux1k8HAH1EaI%2Fg7%2BqmMFPHy8Ma6qrk80qn2PhEiSfvVhh6S9UJv8wDIfnZNcMf6ywqWjgb2lzEfHA0STEs8W6sdLc0259K3DcfqZuhb24uOG%2BuY4lFI1MYlbQyKhdZLmLdddlaxKQRPzrq5KeWhSJYOfbrI%2FxqaCh3jzw8fRi6Zmu1kpY5g%2B7mH9M3zFPCe4J57WwuSKzdLlt1BQ2xAId9lKtIdmf%2Buxfn34ubtczriJr%2F7LeBFI%2BIpN%2FjS022OuauoxPq70LIYsfiS66C3gX3uxEyF%2BrC9RtLESVQT4w4fvvyQY6pgFFizXJ0w4KotWECCYk0QE%2Foc7d5SY7Xec83MQJEOeNtIUicqKISH%2F%2B11LKW1arbBXkB5094y6%2BA8kvgsi3NUM0BqDsFoD2XchMhf3QrTJmtYbov8gEtXcV%2FvtqdqTEHurDaN%2FcHZ4IIi6gza9RaOJp3Guf2j8dglsSyEPhtLGrYJof5hZ1GtIk9Du8m4%2F9pvCJ9JOQXdBFX7GNyOFxGh4vtYGuKGsR&X-Amz-Signature=a18aa06c15931990f5a9c88e02570c2fa3778a74df126a91670974ffce257268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4B7KVIW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T123402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIFBMJf6ZDTkoL89nIbR8gRi6VjzlahE%2FNPeW2zLpJIZ%2FAiB7k%2B0aD3GUaIe04LIFOqe%2FQBVOkUMcxjgkE4fyKYY2tSr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMa9lhYFIjf46jQEaaKtwDAfKUHct3Vk4VXW6L9onqASHco9AwuYILsNmPTAurao8MVEt7grQH8yqrM5Mpbcy8%2Fo54aRUqZ8Jh7rJOSejG7%2F5cQi8vSHU%2Fda%2B3o6vdEdQoNdn7YyP7CUKYy7h77fgJYCJy1A%2BsVvPjWwh1MYJzMF%2B8gTUjT6l036KjSuJgTWTiRo7TBA3ofMXXRzutRLEfP7zkoqkqzXr3Sr%2B52makyqTjPIBDhnpQwpEhmVfdThCiyOEK9CJu%2BnDD0Gl3IcufEivPQ7nR4iofACj%2FFqJ822ERcHQ43I%2BhLYQh2gzH%2F%2FhqFnjgeJpv5hn%2Fkly3PjZi74EHUc5x0kO6M0RvV%2BHux1k8HAH1EaI%2Fg7%2BqmMFPHy8Ma6qrk80qn2PhEiSfvVhh6S9UJv8wDIfnZNcMf6ywqWjgb2lzEfHA0STEs8W6sdLc0259K3DcfqZuhb24uOG%2BuY4lFI1MYlbQyKhdZLmLdddlaxKQRPzrq5KeWhSJYOfbrI%2FxqaCh3jzw8fRi6Zmu1kpY5g%2B7mH9M3zFPCe4J57WwuSKzdLlt1BQ2xAId9lKtIdmf%2Buxfn34ubtczriJr%2F7LeBFI%2BIpN%2FjS022OuauoxPq70LIYsfiS66C3gX3uxEyF%2BrC9RtLESVQT4w4fvvyQY6pgFFizXJ0w4KotWECCYk0QE%2Foc7d5SY7Xec83MQJEOeNtIUicqKISH%2F%2B11LKW1arbBXkB5094y6%2BA8kvgsi3NUM0BqDsFoD2XchMhf3QrTJmtYbov8gEtXcV%2FvtqdqTEHurDaN%2FcHZ4IIi6gza9RaOJp3Guf2j8dglsSyEPhtLGrYJof5hZ1GtIk9Du8m4%2F9pvCJ9JOQXdBFX7GNyOFxGh4vtYGuKGsR&X-Amz-Signature=3e19aa70ce46c1116a1a475fe544de709f6dea3151b96be742d0d37ba9f07132&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







