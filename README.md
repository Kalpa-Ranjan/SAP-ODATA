



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQRTUPOO%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T185421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDlZh5%2BkxWhhzzFPxTHhcnIqeyN5IoLkC%2FkkD0B1E6b%2BAIgR6NC8dwB7yP5ZX7IBBfKsWIyu2CGCW%2Fy4OLMD0dYQNsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkvimyTHj3Dy9qISyrcA16txHTeB4Z%2F9HuanupiyNobJy6CYgrwPwynnQPFu%2B2pWLFNl1wNiqbbMGwpBhMpeEHThFHgnUs3AnkgHQyKgJ%2BR1O7ivY%2B5Oj0mVhHG%2FML7UX6bsi%2BTfHn2ovc2SP2Buzzbsi46xJbOUIUjxVXsPeNyquJ00l0nVamQ4lxCq6qufWnyizlzV7yeUokk%2FmnUZB0zG33a%2FZFn2Xfxbtp8Ag5quJIfghSjgoTqaanJqlwEz8%2BPELt2LFvNT%2Bm9fkwKqdXGHVzOMkrmsZeoga4TD8DSkufJE4JaqXaLBuZ%2Bec5tI1iXIr2uPVlJhVsNu1%2BMJFUXortzRt6K%2F%2FK3wdUVcPqJvrSCuO%2FsmT6AS6%2FkE3PUyEAXii5jtHK81ZqunqgzFYWL5qrw6Y6JH80GDOZcce2E%2FMCwNJ5MgfoAaCZmHpo23Ly5iNUABalx0XzV5Xpe%2F%2FUNqALaH55V0sqvi5gGO0w5gFKaJeLh1%2FCIO35RMcWm01bO2xynqu68pCQxVYYXF3f9PKx4mGNQF%2FBSzGgsibyDn5ZyciQcMoZ6zRSdn3QeOJzMulYhe1BEk5jpZ3HogMS9eK0VeRjbGSf6Munu%2B8ktdOj0gix084SMrp6yekTJNmqP1W2FBtFdePH5MNOy8tMGOqUBMJP8hGiytoN9EqAsc2Xuq6MTkY1q6BdWMTcglg3qLkVAAhfXUpbq6WGPuHUT%2FJc5zCZ0c%2BrZiJHpBCiEq50dU3ogjIuC5zT8lkc0wQlPZOMQJAlPzxeU3A%2FAZlb5imZte7mkh1YGeCRfYpqa3smtM1XTq%2B%2BF0l3zHQ7VYmuvNG1roSWlna8G5UIbAxl609pZdU5teolmAgSKZLQW0%2FVawHkKqq%2Bn&X-Amz-Signature=85f14650d941c617eabdb97514dd679d6241c64be124d3541f22d8035d326c5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQRTUPOO%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T185421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDlZh5%2BkxWhhzzFPxTHhcnIqeyN5IoLkC%2FkkD0B1E6b%2BAIgR6NC8dwB7yP5ZX7IBBfKsWIyu2CGCW%2Fy4OLMD0dYQNsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkvimyTHj3Dy9qISyrcA16txHTeB4Z%2F9HuanupiyNobJy6CYgrwPwynnQPFu%2B2pWLFNl1wNiqbbMGwpBhMpeEHThFHgnUs3AnkgHQyKgJ%2BR1O7ivY%2B5Oj0mVhHG%2FML7UX6bsi%2BTfHn2ovc2SP2Buzzbsi46xJbOUIUjxVXsPeNyquJ00l0nVamQ4lxCq6qufWnyizlzV7yeUokk%2FmnUZB0zG33a%2FZFn2Xfxbtp8Ag5quJIfghSjgoTqaanJqlwEz8%2BPELt2LFvNT%2Bm9fkwKqdXGHVzOMkrmsZeoga4TD8DSkufJE4JaqXaLBuZ%2Bec5tI1iXIr2uPVlJhVsNu1%2BMJFUXortzRt6K%2F%2FK3wdUVcPqJvrSCuO%2FsmT6AS6%2FkE3PUyEAXii5jtHK81ZqunqgzFYWL5qrw6Y6JH80GDOZcce2E%2FMCwNJ5MgfoAaCZmHpo23Ly5iNUABalx0XzV5Xpe%2F%2FUNqALaH55V0sqvi5gGO0w5gFKaJeLh1%2FCIO35RMcWm01bO2xynqu68pCQxVYYXF3f9PKx4mGNQF%2FBSzGgsibyDn5ZyciQcMoZ6zRSdn3QeOJzMulYhe1BEk5jpZ3HogMS9eK0VeRjbGSf6Munu%2B8ktdOj0gix084SMrp6yekTJNmqP1W2FBtFdePH5MNOy8tMGOqUBMJP8hGiytoN9EqAsc2Xuq6MTkY1q6BdWMTcglg3qLkVAAhfXUpbq6WGPuHUT%2FJc5zCZ0c%2BrZiJHpBCiEq50dU3ogjIuC5zT8lkc0wQlPZOMQJAlPzxeU3A%2FAZlb5imZte7mkh1YGeCRfYpqa3smtM1XTq%2B%2BF0l3zHQ7VYmuvNG1roSWlna8G5UIbAxl609pZdU5teolmAgSKZLQW0%2FVawHkKqq%2Bn&X-Amz-Signature=220d322a7dcc9924a0300a8406db0e508bf8a6faa178a31e5fb7bcc78dabc6f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







