



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDXEK6D%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T064308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIA1yn62GL6rP5RR6jOe1s6dM%2FCo9%2F44M4wNg3D1ni6JPAiAZ%2FzxetBDzlEzjOCv%2F9z7KFCyV%2FWzvsAkab9RoIXgP%2FyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRyxvfAXjGmi7KJ74KtwDkdJpxpOMxIaXPfzj%2Bf2YL%2Fq42Wd4TDCmcFftmasTT9eh1uCsUwmi1N67%2B5lVH2h0KEK4R7N9kGYWs7TA2MAwl04Cv%2FjC286%2BfBTqEZYxgkR0ajrhTv823gX41VZpxbb5JV%2FYW0p%2FHpnQEfzIQ81yXUbHSLOp2%2BcqHXpDpJgPAn5dinN27rHVGA5mSCjd6Q4gdw35LPhPvSMRtPQ8diVWaT3LybVXtNA6QLyrRpJqE4f1ncO1BD9QRNs9BxygG%2F%2FpxUHyGrz6o5myelLv2kdxI5XWXS%2BNRrP3WutdgOcLwvcxoH7LVlxG3BUqkDIQCYlUrSQhXYX4o%2FwmmiKys1nBpxZyHesDuD4mGAeOXMOyZhf%2B1EQ0qEivDjMhRt10mKvb0nA9ayo4iHUa%2F2nubG52dvBCEgm3syWPZfKTUPdnWaGd61LXYtHGp%2F4LbUzLnX5DEt2TnILv6W0NVzKBNG0suVsfPiDuo6sXQkMTwPOPCvK7N5qSj4EjQajM39Y1onzaRt3ASQvXYdh7NK4Kd2URpladLFmgkJmGAUjcgMTS0HIHUf47fEFCpjLAbk8CKHuelraLzgD6pFz1tGXjCmGH0fdjlADYLguWGTeesDcOjd6lI7aNdmWCQCMxwTcwhpuGzAY6pgGC8W5Klrc1EiYDBV4Rn%2BujXnBYEZ1YsTOD9M9S0CCwlJww8jdrRuRqTVicUrgS0OyeS3KqA29crmnPBR7LYupyOivY9uKu8YJqTFtnpe2kOeLtqk9SwBq737OZ1EuBwzkAOJKbnO53j2Yd6kRQIkOyVGgoaEqebSuopE5V8INa5c2%2BNz1prGBPJVsDi89NmM6ni1klrhoconPfvPKQzjciWMPsl01T&X-Amz-Signature=cdb6d40ffe9873f6ed3b23d3a5dde679f8c98af5598bf06822032408a381b31f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDXEK6D%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T064308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIA1yn62GL6rP5RR6jOe1s6dM%2FCo9%2F44M4wNg3D1ni6JPAiAZ%2FzxetBDzlEzjOCv%2F9z7KFCyV%2FWzvsAkab9RoIXgP%2FyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRyxvfAXjGmi7KJ74KtwDkdJpxpOMxIaXPfzj%2Bf2YL%2Fq42Wd4TDCmcFftmasTT9eh1uCsUwmi1N67%2B5lVH2h0KEK4R7N9kGYWs7TA2MAwl04Cv%2FjC286%2BfBTqEZYxgkR0ajrhTv823gX41VZpxbb5JV%2FYW0p%2FHpnQEfzIQ81yXUbHSLOp2%2BcqHXpDpJgPAn5dinN27rHVGA5mSCjd6Q4gdw35LPhPvSMRtPQ8diVWaT3LybVXtNA6QLyrRpJqE4f1ncO1BD9QRNs9BxygG%2F%2FpxUHyGrz6o5myelLv2kdxI5XWXS%2BNRrP3WutdgOcLwvcxoH7LVlxG3BUqkDIQCYlUrSQhXYX4o%2FwmmiKys1nBpxZyHesDuD4mGAeOXMOyZhf%2B1EQ0qEivDjMhRt10mKvb0nA9ayo4iHUa%2F2nubG52dvBCEgm3syWPZfKTUPdnWaGd61LXYtHGp%2F4LbUzLnX5DEt2TnILv6W0NVzKBNG0suVsfPiDuo6sXQkMTwPOPCvK7N5qSj4EjQajM39Y1onzaRt3ASQvXYdh7NK4Kd2URpladLFmgkJmGAUjcgMTS0HIHUf47fEFCpjLAbk8CKHuelraLzgD6pFz1tGXjCmGH0fdjlADYLguWGTeesDcOjd6lI7aNdmWCQCMxwTcwhpuGzAY6pgGC8W5Klrc1EiYDBV4Rn%2BujXnBYEZ1YsTOD9M9S0CCwlJww8jdrRuRqTVicUrgS0OyeS3KqA29crmnPBR7LYupyOivY9uKu8YJqTFtnpe2kOeLtqk9SwBq737OZ1EuBwzkAOJKbnO53j2Yd6kRQIkOyVGgoaEqebSuopE5V8INa5c2%2BNz1prGBPJVsDi89NmM6ni1klrhoconPfvPKQzjciWMPsl01T&X-Amz-Signature=6494c48d06b06c187b531ef09691b94bcf9d6abca7be2fc1dbbbee3022efb08e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







