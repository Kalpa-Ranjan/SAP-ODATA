



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q2R57J2%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T104647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzYx8nFZ0TFgUcyfgQSu18JGVSfebBnp2XWj3EKX3B6QIgfOvTBvf333J2%2Bj9kY6q6LZJx3sspEfg9L1acS0sD52kqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwSt8oBgx%2BftK1sESrcA9I72sBfcZK9otc1FnaiFm01W%2BLQzoyb93mkO%2B9lLpd5bhhw8CtcG5OYZjKqnmuKOR7PXqaZc3Dfrcf9XoQ3hJELETqS4SGHP%2BIJBzYOiWrD3SQkyjxcLMoCaXtOxgTtIMxXHyI8IRGeuMMCZ9JiX7UMua9%2BNmtERZRWYmivDI9tqxnjudZvgFHvmDG40hEmJaDw5tvHAtq64cuMzj0S%2Bn4ucnqUeDKIOMKNIQO2sn%2Fd4w4zDIDmKil8PdXhKrn4gtZLlKTpuHOk%2F071l56NbxACWbg0kn8SLfcpLpYoW%2BclvJN7MfCN8Qs%2F6hCbObOLBCbZ7dWXbzc4KvQoZ4ytsM2nKvOQsepJCG8Uwj6e4qIlzugDG4CUpVxraAvM8nAvXQylTOVceaPFizIH5Mm840TACoLNfvvge30CUbGvCf8O60972kErhp0wSvqvbbbKyxshMMbSpYKg8ys3ZP8ur72%2B32tzvZe3wk6d6%2FJ6gcYT2IU6BKYk0mtNjQV6T%2F5KzJpGeX5V%2Bpn0PkU2rqbfRlyUgPQTdDcz9DqLqkd2YXu5Kce0fYXhE0%2FGE5f%2BeymcpPaBVXe8IDs7bHxgK%2FeG3dyMldE4a4v%2BQyrmGYkj%2F6pi%2BAopN4lRDL7OQV57MN77iNIGOqUB4YVliluupMHH4sdEU9T3K3B1jql%2FWE54hvA8sMeZ%2BZhMc%2BiEcBH%2FUn%2BQgcvrJ%2B4Mzq9aUkFxWcoukB%2FaKSFnclr%2Fb3BtdnANE2gyoRv3L5a8B6SUmSmvi63KkgXug4YZWbxt%2F1C2J2jeTEb4FJMlXYXVddmqHLFOXo%2FrtOq1WFmVkvhB7YNOjsdDn4B2Tc6f1unwSchlQG4mh1N8udRNeS%2FG50Jt&X-Amz-Signature=8bdbc27368a36ebfabeb66147a11ee10ba0bb6fc10e18620c914890e141e502b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q2R57J2%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T104647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzYx8nFZ0TFgUcyfgQSu18JGVSfebBnp2XWj3EKX3B6QIgfOvTBvf333J2%2Bj9kY6q6LZJx3sspEfg9L1acS0sD52kqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwSt8oBgx%2BftK1sESrcA9I72sBfcZK9otc1FnaiFm01W%2BLQzoyb93mkO%2B9lLpd5bhhw8CtcG5OYZjKqnmuKOR7PXqaZc3Dfrcf9XoQ3hJELETqS4SGHP%2BIJBzYOiWrD3SQkyjxcLMoCaXtOxgTtIMxXHyI8IRGeuMMCZ9JiX7UMua9%2BNmtERZRWYmivDI9tqxnjudZvgFHvmDG40hEmJaDw5tvHAtq64cuMzj0S%2Bn4ucnqUeDKIOMKNIQO2sn%2Fd4w4zDIDmKil8PdXhKrn4gtZLlKTpuHOk%2F071l56NbxACWbg0kn8SLfcpLpYoW%2BclvJN7MfCN8Qs%2F6hCbObOLBCbZ7dWXbzc4KvQoZ4ytsM2nKvOQsepJCG8Uwj6e4qIlzugDG4CUpVxraAvM8nAvXQylTOVceaPFizIH5Mm840TACoLNfvvge30CUbGvCf8O60972kErhp0wSvqvbbbKyxshMMbSpYKg8ys3ZP8ur72%2B32tzvZe3wk6d6%2FJ6gcYT2IU6BKYk0mtNjQV6T%2F5KzJpGeX5V%2Bpn0PkU2rqbfRlyUgPQTdDcz9DqLqkd2YXu5Kce0fYXhE0%2FGE5f%2BeymcpPaBVXe8IDs7bHxgK%2FeG3dyMldE4a4v%2BQyrmGYkj%2F6pi%2BAopN4lRDL7OQV57MN77iNIGOqUB4YVliluupMHH4sdEU9T3K3B1jql%2FWE54hvA8sMeZ%2BZhMc%2BiEcBH%2FUn%2BQgcvrJ%2B4Mzq9aUkFxWcoukB%2FaKSFnclr%2Fb3BtdnANE2gyoRv3L5a8B6SUmSmvi63KkgXug4YZWbxt%2F1C2J2jeTEb4FJMlXYXVddmqHLFOXo%2FrtOq1WFmVkvhB7YNOjsdDn4B2Tc6f1unwSchlQG4mh1N8udRNeS%2FG50Jt&X-Amz-Signature=7ca51558b01288b1deec1bfdd65c9af22b12b69003cbbf477330b9de812a07fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







