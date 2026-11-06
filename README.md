



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3REHNBB%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T060904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCaxmG%2BCg0L5N5DSgymnssyycR983jQ%2BIbsLf9AjyjTWQIgJ1XB3Nk2NcaNSuxbAvH6BEkiHdrBjG0RBuwrpAe2bkAqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDIXgD1WueoaWXB0yrcA9iwvthxI8oRjyz4YEce2qVshOy4gs%2FnpuMat3Ggh1VVjZKhklL7AzPYFAA0BiOPnKzTcQv9RvTAY7nCFf5k7yCSZsXu4xPYY36m1Ru6k6PJPfwZFnDLv43W0VvhO2w0rBcNvTwnFoX7otqypGGujfe%2FTHJUbNdRZQaC8FcjMvrC8qFaydysJdJDh60RYOaxtt%2F5OgTGjCAvCIi6aZACYs5xpRH42z8EVLJdJpx0DafnBdU3ccfK3zkgBwEfgzXD3FMJaNYuvtsPam7bFxXGqRsMBWTUvM8dIGtOrfTyKc2tFbuGcE1PkAWKcCYuN1%2B0umfAkFIr%2BEJMKmLNM3twbfn9deLEqoBQEQQSQika9Fe0WjjgTMYDDgJ7KHwD2alJzCh2PeH%2FQDPG0iGzF2kJKUK81q5Lm8Lq5lx3lo23vrV0Fc2reVQk1iO9VF2%2BT47PcSPsqTk9%2B9gcfcp7DALzvzLabDTtXwZlhiVFFY432xtfQtZGGHTWMdg5jBn15KhO2eY94atpAME7m0hJ8YlzYyoRmtIpuQryxEMMTkjfyO7Njc6ECFaF3zAG6oWhZhiHxQqknM92cnDz2jcUclLFRyz33gNNJmWfAon78O5dxw45mdwqRZVhmBJfWcDsMMqitdcGOqUBc0L6KZWEM6%2BW4AKfwSRtc7DuI9ujWe59Jx439ocv%2FmxfMyldYarPEGOtBIKqBMdGqcaXk%2BhelNduajuhCwM%2BdngnyzBpHlcdgv2suzsBVaoD5RrL9y%2Fu2ZH2V0KbfKZZo0HHWg9F44eV9zTJY2AB2nDI5JzKz2pyZx63mkX1ksACczm8bBD24h1m%2FL%2BsVwQi05soZinpI5tPk1WfyxaOXOANIeho&X-Amz-Signature=90d3201d88146356b635667bdc1486266cc25d896026d739088cab41eba56741&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3REHNBB%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T060904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCaxmG%2BCg0L5N5DSgymnssyycR983jQ%2BIbsLf9AjyjTWQIgJ1XB3Nk2NcaNSuxbAvH6BEkiHdrBjG0RBuwrpAe2bkAqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDIXgD1WueoaWXB0yrcA9iwvthxI8oRjyz4YEce2qVshOy4gs%2FnpuMat3Ggh1VVjZKhklL7AzPYFAA0BiOPnKzTcQv9RvTAY7nCFf5k7yCSZsXu4xPYY36m1Ru6k6PJPfwZFnDLv43W0VvhO2w0rBcNvTwnFoX7otqypGGujfe%2FTHJUbNdRZQaC8FcjMvrC8qFaydysJdJDh60RYOaxtt%2F5OgTGjCAvCIi6aZACYs5xpRH42z8EVLJdJpx0DafnBdU3ccfK3zkgBwEfgzXD3FMJaNYuvtsPam7bFxXGqRsMBWTUvM8dIGtOrfTyKc2tFbuGcE1PkAWKcCYuN1%2B0umfAkFIr%2BEJMKmLNM3twbfn9deLEqoBQEQQSQika9Fe0WjjgTMYDDgJ7KHwD2alJzCh2PeH%2FQDPG0iGzF2kJKUK81q5Lm8Lq5lx3lo23vrV0Fc2reVQk1iO9VF2%2BT47PcSPsqTk9%2B9gcfcp7DALzvzLabDTtXwZlhiVFFY432xtfQtZGGHTWMdg5jBn15KhO2eY94atpAME7m0hJ8YlzYyoRmtIpuQryxEMMTkjfyO7Njc6ECFaF3zAG6oWhZhiHxQqknM92cnDz2jcUclLFRyz33gNNJmWfAon78O5dxw45mdwqRZVhmBJfWcDsMMqitdcGOqUBc0L6KZWEM6%2BW4AKfwSRtc7DuI9ujWe59Jx439ocv%2FmxfMyldYarPEGOtBIKqBMdGqcaXk%2BhelNduajuhCwM%2BdngnyzBpHlcdgv2suzsBVaoD5RrL9y%2Fu2ZH2V0KbfKZZo0HHWg9F44eV9zTJY2AB2nDI5JzKz2pyZx63mkX1ksACczm8bBD24h1m%2FL%2BsVwQi05soZinpI5tPk1WfyxaOXOANIeho&X-Amz-Signature=cc07108c783b841d51b68bec556f8187dd45b49752fd902112d67c8754c24ff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







