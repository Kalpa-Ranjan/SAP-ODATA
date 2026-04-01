



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIMYVSZF%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T130955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcuPeO3rslt9ZZ3z9QTazXl4AxphC81dwXWHFpiwFdMAiBOQXbiJH8v7tpigNJaw1zTF8Bh2IQoYYWOp%2BTYKYkWECr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMTUcKTh7Pr71QS0p%2BKtwDIjy%2BqT3LpO%2B9wrnmC6gDgkU0zG1CtCzOYhA%2FxtIJHVUGPjBGgxz5Sh5bZvvPZ15fVBRdxYdTeyVvQOQ5snPZteidYiwbBHFgSJWTh87hfGWs2pzIryFnuPFyp21ujZqwgEqxi4xgDqfV3IarDpf0P3Ij43zz3JuCtgNA%2BjwD7rU1gF%2FBepIwvSGU1qWc6HwgEwejXMpHfBcIbJNU9l2jH5VTlxx3hg5VrIitopuh%2FEL7t0vbdUedSHJsh1cdCA5fSgb2SQfooNLugv0UkDswlLj3uaftshLjSVrtCv6LLkxIqD55CrO242epgayA7JXRvGdyF6Fj%2FW409O0kufB%2FBmro3XwYXLK%2F0fyPP2ePUi5Zb%2BIy%2BsEfVW8y%2FZQYU2TV%2Bekru2Wkgk01yONQL%2B6%2FppUj%2FofCtpJtGmJMLlb3yL5xihcUPRMsn7LBy9CWOFu521UOz9DkGWf0TpbJlDL0O9uJ1AaeCV8YZlNz71SWYQxLLPXCWo6FEC9%2BzmoKdfKtYQ3QI6pSBsebdRfhFr70%2FBoLAahcxzEfh2tuHFAwQ%2FvS3qooHShFID5a1Lp7OmZNft0Dhtr10vzd41aUUYdjSK5Du%2F8iYrjRz%2F0wVMZWreogeyUcvUUfgo3AXAsw1JO0zgY6pgFmBiu%2FfF%2BkBgUv4%2FiqTbY6zWzkYJOwjKO4UCfx1FG%2B66PpnPsT9%2BzfK5KbslotatVQ%2Fg47Ys7dIH7vQNrZ3fw1q7NTQNF4zXMQKgRggInPBL4hlyWtyBBqGmPSqXlrIK4NJTKfq4I%2FvUaMD58lRUNvIM04iFZVp%2Fw6GpkSyIqGxyEeLF1I4uE0ScJVBGKaK68iRBkKj6r7hgYxJGqoyi7Z4K%2Bzh8Lm&X-Amz-Signature=46293934454818755718871b07456b1acbc013d825db4673332e045235af172b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIMYVSZF%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T130955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcuPeO3rslt9ZZ3z9QTazXl4AxphC81dwXWHFpiwFdMAiBOQXbiJH8v7tpigNJaw1zTF8Bh2IQoYYWOp%2BTYKYkWECr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMTUcKTh7Pr71QS0p%2BKtwDIjy%2BqT3LpO%2B9wrnmC6gDgkU0zG1CtCzOYhA%2FxtIJHVUGPjBGgxz5Sh5bZvvPZ15fVBRdxYdTeyVvQOQ5snPZteidYiwbBHFgSJWTh87hfGWs2pzIryFnuPFyp21ujZqwgEqxi4xgDqfV3IarDpf0P3Ij43zz3JuCtgNA%2BjwD7rU1gF%2FBepIwvSGU1qWc6HwgEwejXMpHfBcIbJNU9l2jH5VTlxx3hg5VrIitopuh%2FEL7t0vbdUedSHJsh1cdCA5fSgb2SQfooNLugv0UkDswlLj3uaftshLjSVrtCv6LLkxIqD55CrO242epgayA7JXRvGdyF6Fj%2FW409O0kufB%2FBmro3XwYXLK%2F0fyPP2ePUi5Zb%2BIy%2BsEfVW8y%2FZQYU2TV%2Bekru2Wkgk01yONQL%2B6%2FppUj%2FofCtpJtGmJMLlb3yL5xihcUPRMsn7LBy9CWOFu521UOz9DkGWf0TpbJlDL0O9uJ1AaeCV8YZlNz71SWYQxLLPXCWo6FEC9%2BzmoKdfKtYQ3QI6pSBsebdRfhFr70%2FBoLAahcxzEfh2tuHFAwQ%2FvS3qooHShFID5a1Lp7OmZNft0Dhtr10vzd41aUUYdjSK5Du%2F8iYrjRz%2F0wVMZWreogeyUcvUUfgo3AXAsw1JO0zgY6pgFmBiu%2FfF%2BkBgUv4%2FiqTbY6zWzkYJOwjKO4UCfx1FG%2B66PpnPsT9%2BzfK5KbslotatVQ%2Fg47Ys7dIH7vQNrZ3fw1q7NTQNF4zXMQKgRggInPBL4hlyWtyBBqGmPSqXlrIK4NJTKfq4I%2FvUaMD58lRUNvIM04iFZVp%2Fw6GpkSyIqGxyEeLF1I4uE0ScJVBGKaK68iRBkKj6r7hgYxJGqoyi7Z4K%2Bzh8Lm&X-Amz-Signature=68959cf649b30f08b212030c0ddb99b2b412fc5228a64c50966bc5a27b098645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







