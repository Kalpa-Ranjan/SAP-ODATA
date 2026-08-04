



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL7JXWTM%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T192310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAHD5x%2B7K17mxws2pbpaY4pgCg9Bha5EtPeurucSThmDAiAE7vPZIDhziNwzlZNi8Ag%2F4g5IS11XarJfBGvCQYpHzyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMeq25wJrfLVWuHsH4KtwDJjy2tvaXLAwCcDopelVmkUnghBnKgnCYLKBaf4MDl6YsccuCuFUGWE2Bz1sRs%2BUWmjtoG925Hezyi%2Fb5zNpg5KeE%2FrtZ%2BS9%2BUo9X%2BHU3MoZd8Ig7jBAH6dz5wcyUvg6DCzsAU%2BKdd1tQVBZ9yd%2BDnjWkt%2FFlbLORAr1QH7ffQmGbvLWYLlPjuIkMyKVoQXKHcE0O1H2YnnRKOxQaeY7r52ZzyKBxm7sutZ5IT8awTUTeMu6%2BPYBsTO4V0hd1h9alHOUmFlR8OPOExpnzXhpne1wMc4UzBolCEXrWyEa6M3r0s3QmN9VJKklAqro8mlHWtJ1Mrji4NiMSmoHak57UxD0q5uJpB0PF7aJK%2Bv5EooInALCLlIsKKNQan3L%2B%2F0kcZMWPcLHL69XuCCACK6ovQHQOt220tr14JX49RoUtRVILCW3QlSS9QrPofRJijuvz%2BNfyvzDnUcdBepm%2BDkHqkRzXbmVjOjgnuvVVFBFdzx4NvKg8ePP7ZxiYp7V25vYxCOY%2FnYIfWx3wQx%2Bd2%2B8u19YDo6rUmpcXWN2NBy%2Byc1RNM2Z7XWTDmzW6TYPwWYpbxHpRNispKnEvlF1tLLr%2B18mwjz5vQxwgJpYLlGp0I6C0%2B2DgQAmfDV3Jc7Aw047I0wY6pgEpz7JUPjyWG1WCAczWUTiTq5ZimETRHNIXIkvTx%2BkrST6u2rmTDyDpUp1DuE06xKmoLvl%2BDj59hqt5CVpDL4f6l3kDc9Wua8FecF7V%2B%2B4xy3%2FOsSFuihQv2irffzdBdvZ1DHHAmsCmElXGzEfhddeZjfpHN3z4XpN%2Fl55xkcOJ%2Fr6b9nNoG8UMllx0Bh7zsYHXWk2scgFCdyYlG8Z38dUFAgUj32tc&X-Amz-Signature=333a20c532d167b93e7bacd4252f54022840139310c3b4c3a592176a677b9b91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL7JXWTM%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T192310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAHD5x%2B7K17mxws2pbpaY4pgCg9Bha5EtPeurucSThmDAiAE7vPZIDhziNwzlZNi8Ag%2F4g5IS11XarJfBGvCQYpHzyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMeq25wJrfLVWuHsH4KtwDJjy2tvaXLAwCcDopelVmkUnghBnKgnCYLKBaf4MDl6YsccuCuFUGWE2Bz1sRs%2BUWmjtoG925Hezyi%2Fb5zNpg5KeE%2FrtZ%2BS9%2BUo9X%2BHU3MoZd8Ig7jBAH6dz5wcyUvg6DCzsAU%2BKdd1tQVBZ9yd%2BDnjWkt%2FFlbLORAr1QH7ffQmGbvLWYLlPjuIkMyKVoQXKHcE0O1H2YnnRKOxQaeY7r52ZzyKBxm7sutZ5IT8awTUTeMu6%2BPYBsTO4V0hd1h9alHOUmFlR8OPOExpnzXhpne1wMc4UzBolCEXrWyEa6M3r0s3QmN9VJKklAqro8mlHWtJ1Mrji4NiMSmoHak57UxD0q5uJpB0PF7aJK%2Bv5EooInALCLlIsKKNQan3L%2B%2F0kcZMWPcLHL69XuCCACK6ovQHQOt220tr14JX49RoUtRVILCW3QlSS9QrPofRJijuvz%2BNfyvzDnUcdBepm%2BDkHqkRzXbmVjOjgnuvVVFBFdzx4NvKg8ePP7ZxiYp7V25vYxCOY%2FnYIfWx3wQx%2Bd2%2B8u19YDo6rUmpcXWN2NBy%2Byc1RNM2Z7XWTDmzW6TYPwWYpbxHpRNispKnEvlF1tLLr%2B18mwjz5vQxwgJpYLlGp0I6C0%2B2DgQAmfDV3Jc7Aw047I0wY6pgEpz7JUPjyWG1WCAczWUTiTq5ZimETRHNIXIkvTx%2BkrST6u2rmTDyDpUp1DuE06xKmoLvl%2BDj59hqt5CVpDL4f6l3kDc9Wua8FecF7V%2B%2B4xy3%2FOsSFuihQv2irffzdBdvZ1DHHAmsCmElXGzEfhddeZjfpHN3z4XpN%2Fl55xkcOJ%2Fr6b9nNoG8UMllx0Bh7zsYHXWk2scgFCdyYlG8Z38dUFAgUj32tc&X-Amz-Signature=35b67184b10f8851e6ba830b5f5b56e62f196e0d7d07717ef0efff8aed0e962e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







