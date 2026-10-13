



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI2MIR5M%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T121320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDY87ZOvPCvGfjsxC752vWWBLj%2FSFdZo5QltyGP%2BHLxUAiBPmG%2BKQfEBSOkzyiLwPqJlzZl5Skv9eFRdEv4G0nnI2CqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2NEN9Sg8mOJpF5e4KtwDeakVLIwiy%2Bw%2F3nBI42O71OCYG2amkbyMWGugwT6urT4rlNpMj7bYZnqyF0AQofdzl2c4ass41HO82hQ3jxw1%2FafowDk3c%2FR%2FYmcjWJS1enqdyzaLkpHXuufyZN7CfVEfSLZzKOFzlwa0f6lhsY5STnUKpd56xS%2FtJciUpkc%2FlhgsHyhQKtWs01JVzGqCMbi0BRVksWLmrQ7KjL1n%2F3zc54UmMgBj4wwqZDdhtJrWgkxHWuq9E0E13GX5XHsiUbXYlzOtrIc53Sku7sM6Pg1Y2EuhcEK8ZoBMGeXGJZHZxmSarOzNhdP0aB5JpHvM1tf6g0ZUAXaljzsY47xcVJ5GY7twVfScFYY%2BK996F73CIhcu160E1RoEIFGJCVrb8gJ4KFDN6BfWRriHPm5CK3EPa3%2BjW0RW0MWlOyKzf85rL1MK0Io6WevhbXAnMrr5gRRjacY0EU7r4MT8xKVR98af9PLH01Al7L4%2Fgdbo%2BhAE%2F5z5u3PKuCvLZzdCkZRjySfixLWlgVhqMYv03ZZ%2Frq4GKpt%2BPVH7ol%2FzYKJNV37OdiqN%2BBaGFYjoEHIownOXtwOLZ6NY4HSoWuyy7bX6ekMfN7M4pFoIOy982An1ZwHoGCWIC%2Fto9D9zKtTZG%2B4w8q%2B41gY6pgHhJ%2BVo0NgDOi2pBNc64wJi%2BODkG6FYdThZ0GU5xq1Ipc49mdip4Vd7eZs8WpWQ54SuVFrVjnJiN5TS0H8c6rkngZ0BaK%2B6EFjcyIVZ0kCTfX8U29kweRG7YEAHoJ9YdhEZP4EXP8Z1V1fKiJjh4WJr%2BQ5AD2bF2hxaDwfADBkGCpSB1jCXzywESrKNkxhZTUJOYZBtTOKOPGazkNQGTbPZFsefMdYQ&X-Amz-Signature=b586279c34f014961b1fd32009800b69187089c37dfb8126636ea0b72b5f3735&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI2MIR5M%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T121320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDY87ZOvPCvGfjsxC752vWWBLj%2FSFdZo5QltyGP%2BHLxUAiBPmG%2BKQfEBSOkzyiLwPqJlzZl5Skv9eFRdEv4G0nnI2CqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2NEN9Sg8mOJpF5e4KtwDeakVLIwiy%2Bw%2F3nBI42O71OCYG2amkbyMWGugwT6urT4rlNpMj7bYZnqyF0AQofdzl2c4ass41HO82hQ3jxw1%2FafowDk3c%2FR%2FYmcjWJS1enqdyzaLkpHXuufyZN7CfVEfSLZzKOFzlwa0f6lhsY5STnUKpd56xS%2FtJciUpkc%2FlhgsHyhQKtWs01JVzGqCMbi0BRVksWLmrQ7KjL1n%2F3zc54UmMgBj4wwqZDdhtJrWgkxHWuq9E0E13GX5XHsiUbXYlzOtrIc53Sku7sM6Pg1Y2EuhcEK8ZoBMGeXGJZHZxmSarOzNhdP0aB5JpHvM1tf6g0ZUAXaljzsY47xcVJ5GY7twVfScFYY%2BK996F73CIhcu160E1RoEIFGJCVrb8gJ4KFDN6BfWRriHPm5CK3EPa3%2BjW0RW0MWlOyKzf85rL1MK0Io6WevhbXAnMrr5gRRjacY0EU7r4MT8xKVR98af9PLH01Al7L4%2Fgdbo%2BhAE%2F5z5u3PKuCvLZzdCkZRjySfixLWlgVhqMYv03ZZ%2Frq4GKpt%2BPVH7ol%2FzYKJNV37OdiqN%2BBaGFYjoEHIownOXtwOLZ6NY4HSoWuyy7bX6ekMfN7M4pFoIOy982An1ZwHoGCWIC%2Fto9D9zKtTZG%2B4w8q%2B41gY6pgHhJ%2BVo0NgDOi2pBNc64wJi%2BODkG6FYdThZ0GU5xq1Ipc49mdip4Vd7eZs8WpWQ54SuVFrVjnJiN5TS0H8c6rkngZ0BaK%2B6EFjcyIVZ0kCTfX8U29kweRG7YEAHoJ9YdhEZP4EXP8Z1V1fKiJjh4WJr%2BQ5AD2bF2hxaDwfADBkGCpSB1jCXzywESrKNkxhZTUJOYZBtTOKOPGazkNQGTbPZFsefMdYQ&X-Amz-Signature=31597950ccd31c8c4991076ce9ab8393e9553817bfda2db939fe0b5cc1b7152b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







