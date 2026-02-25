



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJOIFOD%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T014810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCwE1TWwd8k3TT32N%2BZ9EJfYeT%2B2XObP6ldunTNM7%2BX%2FgIhAOklcCDN0UhMM22qhjwHoGKyrBevFPmq7zzU4bpcYI3XKv8DCAIQABoMNjM3NDIzMTgzODA1Igz%2BsFUr1zxlOSkhcFEq3ANlWGNvEeoCyMTOn2%2ButyHxlu%2F0BCsSBUvijiU7hOeHLZIk2yYdQEn7aBQgNKsfIY%2BWK56hBqQazP88rSKmsrpZDqc3XmggKtSLEIfyyon9vgZdzC%2B5ndqOhqB%2BpQNS9cDQmV4lkv4Eza9IrJJQL4cDpifEl%2FWuzcXAToxrX5enVW4JbGpbJGv%2BOXh7yOhMwPkWf7t6sWlPeZQ3iR40XYU7ROzw0SVz8NWmKfYIlu1rXoalaCmcMTVUMWu1fkbDm1xM7eM71RNw4VKk%2FvM6tvPee4wY4KJOGyg44C8c9EeSN8VYeaE1hgn4eFtB5%2BqMmgUCgRALhshO6xLTHJxhWyHZgcsyWBnL9IgY8dYva%2Fr2xUvG%2FLXLdNuQWl1InUIeDB3MKHoLwXw6SlqwCLqEoNLCDfddOF9fExoWVsMgVjSx8u%2FIIPJhZcs1ss6nRd8xWQyg5PgjsxInzlKFzd5%2FN0K6OGp2aMQgR%2FJIn4E%2BSFodJZ8I5gEgJ7h74dUo%2FeMf1%2FvNN%2BJj3mpX3rSYvND2hyv4ADQDGwZt4kxNTDMZHc7ILbhc8iJucQ64p92V%2FibD%2FILpx4PF6rm0jTZTlVp4BHzn32ek1Ws3fxb4BJqz3dCk86jbwPKaACbx3yGuSDDIg%2FnMBjqkAcSU3G1l%2B0UnlObKBoQkcO1Mj7BhXFEhbIQg61EaRLYeVXl%2BJk3OB16%2FxOh0U1f%2BKACzpCo3Cn%2B9fbBYymUPjjUJIDuATZIPghN2QA0lfCr21WpKarRNGBtm0lDS9QwXrB%2FQ3dyNuiWjbI7sCA3njSmu81evNDdAtFJTIGXz%2B1jirmaF%2FgLef5f%2Fe6g%2FFHFNh5Sd%2FpMveqwo%2FYjFf34sm9ufMwNK&X-Amz-Signature=5acdcc80d6e66c7786ce95fb472a3e893f847719764cf4081d2b7eb3e3776d6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJOIFOD%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T014810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCwE1TWwd8k3TT32N%2BZ9EJfYeT%2B2XObP6ldunTNM7%2BX%2FgIhAOklcCDN0UhMM22qhjwHoGKyrBevFPmq7zzU4bpcYI3XKv8DCAIQABoMNjM3NDIzMTgzODA1Igz%2BsFUr1zxlOSkhcFEq3ANlWGNvEeoCyMTOn2%2ButyHxlu%2F0BCsSBUvijiU7hOeHLZIk2yYdQEn7aBQgNKsfIY%2BWK56hBqQazP88rSKmsrpZDqc3XmggKtSLEIfyyon9vgZdzC%2B5ndqOhqB%2BpQNS9cDQmV4lkv4Eza9IrJJQL4cDpifEl%2FWuzcXAToxrX5enVW4JbGpbJGv%2BOXh7yOhMwPkWf7t6sWlPeZQ3iR40XYU7ROzw0SVz8NWmKfYIlu1rXoalaCmcMTVUMWu1fkbDm1xM7eM71RNw4VKk%2FvM6tvPee4wY4KJOGyg44C8c9EeSN8VYeaE1hgn4eFtB5%2BqMmgUCgRALhshO6xLTHJxhWyHZgcsyWBnL9IgY8dYva%2Fr2xUvG%2FLXLdNuQWl1InUIeDB3MKHoLwXw6SlqwCLqEoNLCDfddOF9fExoWVsMgVjSx8u%2FIIPJhZcs1ss6nRd8xWQyg5PgjsxInzlKFzd5%2FN0K6OGp2aMQgR%2FJIn4E%2BSFodJZ8I5gEgJ7h74dUo%2FeMf1%2FvNN%2BJj3mpX3rSYvND2hyv4ADQDGwZt4kxNTDMZHc7ILbhc8iJucQ64p92V%2FibD%2FILpx4PF6rm0jTZTlVp4BHzn32ek1Ws3fxb4BJqz3dCk86jbwPKaACbx3yGuSDDIg%2FnMBjqkAcSU3G1l%2B0UnlObKBoQkcO1Mj7BhXFEhbIQg61EaRLYeVXl%2BJk3OB16%2FxOh0U1f%2BKACzpCo3Cn%2B9fbBYymUPjjUJIDuATZIPghN2QA0lfCr21WpKarRNGBtm0lDS9QwXrB%2FQ3dyNuiWjbI7sCA3njSmu81evNDdAtFJTIGXz%2B1jirmaF%2FgLef5f%2Fe6g%2FFHFNh5Sd%2FpMveqwo%2FYjFf34sm9ufMwNK&X-Amz-Signature=63c73fc6284c20f63a6474a5e37da4a9174d0064f595a36228bc4647dd06cc02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







