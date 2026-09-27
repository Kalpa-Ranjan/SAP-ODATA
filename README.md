



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZWIIEY%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T061309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFJ%2BLuVOLqYz5dsfd8ZNh8avkXGXuQ876P28IKb%2FFcLYAiANJuTrQfVIu2ROQj9aohqQY%2Fn1RMq5Y6MZoBdJMo%2FVqyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIM8hThKFNctL1rcJyeKtwDJQLEfS3IIBr5mMErWChAZa%2FX1YV2%2FYZXur9A4qzctkFNIZqG3nmsoLLRBfkfnYMABu5OQaTyb8%2FanWZj%2FHrMPZI7f7OHs%2FGM2Q15MK3vgv4IetR%2BhJlZBYK9D3bPyp1fbk48Ytpi8uADPoKVyLvHO%2BnEiL1N%2BtAiKqcW9rLXAdO%2BeU%2FQiNv0iF5X1WaiNAzxgqBwjlDnpVWZBRN4%2BDDCR4%2FXS1Ij60K73Xt7urcp6USBzszdV9UlUVoDSjLOLxfa7JbUXMEPSV447NF34btpJcopqwPuN%2B0NMFQH3Wjhl0cvAg32brFvt8LSF1aHg%2F29e7FFUFMZkuD3yP1h%2BfzuY0TQnvVkoaYRNQ1lujvhUlQcM32d1yRg%2Fabs52J9C%2F44nz8pCvn68PFko3NGww241DHrVf9%2FiXVO8oexBOlAk6WHNzrE%2FjtRh%2F07NTeC2hoftbPjTFvvM73pqPJFuqS5zpLS6Tf4UsvuTwa3P7aH%2FNImjEgggYhAs8DHDXM8v4isJy8S36J3eRaOHkvWztDu6L9Jwgz3BxhUNGNrvlyEWLT17REdp7vPzrfbdSKu%2F3SFnGZyQ9z%2B%2BkrMH5rK47SCW7GeMKLp7fEhrKohWmVH0BYnqcN8XN63QUDOPe4wwrji1QY6pgEiiTQ69byLQOuHf5BqoOaCYTwC4xXlLUNss8Lpokwcl3nKva8EBasgHYIPOcLo3Bs6Qzma33Wypi5S5EAp5TrGuGtEFQSgQa9H3wRtrIrPfkdUJ%2BqZ8maYlfzPeDx0DuYzVUSHND%2FGWKRKq2h0vWihat6yo7f%2BXVZSnlnl7n9m3RHUItVwiAja5lxH4ewH7cr%2BE3a8JlZ7%2BHJMLsBDtGKVTl%2B6fVVJ&X-Amz-Signature=2f5e9f69c639a3f77512cf50a6a54327e7e7eb2ff5ec3fa443d56a1028ecd8f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZWIIEY%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T061309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFJ%2BLuVOLqYz5dsfd8ZNh8avkXGXuQ876P28IKb%2FFcLYAiANJuTrQfVIu2ROQj9aohqQY%2Fn1RMq5Y6MZoBdJMo%2FVqyr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIM8hThKFNctL1rcJyeKtwDJQLEfS3IIBr5mMErWChAZa%2FX1YV2%2FYZXur9A4qzctkFNIZqG3nmsoLLRBfkfnYMABu5OQaTyb8%2FanWZj%2FHrMPZI7f7OHs%2FGM2Q15MK3vgv4IetR%2BhJlZBYK9D3bPyp1fbk48Ytpi8uADPoKVyLvHO%2BnEiL1N%2BtAiKqcW9rLXAdO%2BeU%2FQiNv0iF5X1WaiNAzxgqBwjlDnpVWZBRN4%2BDDCR4%2FXS1Ij60K73Xt7urcp6USBzszdV9UlUVoDSjLOLxfa7JbUXMEPSV447NF34btpJcopqwPuN%2B0NMFQH3Wjhl0cvAg32brFvt8LSF1aHg%2F29e7FFUFMZkuD3yP1h%2BfzuY0TQnvVkoaYRNQ1lujvhUlQcM32d1yRg%2Fabs52J9C%2F44nz8pCvn68PFko3NGww241DHrVf9%2FiXVO8oexBOlAk6WHNzrE%2FjtRh%2F07NTeC2hoftbPjTFvvM73pqPJFuqS5zpLS6Tf4UsvuTwa3P7aH%2FNImjEgggYhAs8DHDXM8v4isJy8S36J3eRaOHkvWztDu6L9Jwgz3BxhUNGNrvlyEWLT17REdp7vPzrfbdSKu%2F3SFnGZyQ9z%2B%2BkrMH5rK47SCW7GeMKLp7fEhrKohWmVH0BYnqcN8XN63QUDOPe4wwrji1QY6pgEiiTQ69byLQOuHf5BqoOaCYTwC4xXlLUNss8Lpokwcl3nKva8EBasgHYIPOcLo3Bs6Qzma33Wypi5S5EAp5TrGuGtEFQSgQa9H3wRtrIrPfkdUJ%2BqZ8maYlfzPeDx0DuYzVUSHND%2FGWKRKq2h0vWihat6yo7f%2BXVZSnlnl7n9m3RHUItVwiAja5lxH4ewH7cr%2BE3a8JlZ7%2BHJMLsBDtGKVTl%2B6fVVJ&X-Amz-Signature=011bc326efeecf1f338a416810848c931b20c5dbdb87af224af6ca3bf41f1e69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







