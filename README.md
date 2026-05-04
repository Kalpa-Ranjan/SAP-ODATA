



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK66AQKD%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T134721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BXfwOV6RdvOOrRJQ3072AixZOdYQvnkzZ0g6j4bJnDAiAhDdValFB0aYAs1%2B%2BR6Re2CLcqKB37JV8lYt5CBk7VnCr%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM6VAb7V19ervHyycQKtwDdyjVxBrvogWmbeYWWhzmSsRNPgnB65dwvJdgs0jwz6eaESjMFfWThdGmSOJbiRxdONhRW8jBGrDtDXCT%2BjBjQIk4xkNDBB4PM%2BR5PJ08p%2FvxOHc9fRRqQXmagA7w8dJE%2FuKh1e%2B2P8%2Fq%2BAd0uC3brYkAT6nvGXVV%2B%2B698%2FCtYQug4eUek9J%2FDrtaOoeLb8P8AQrDxMZIzsyuMnVL8dFzDk7mSGj67VRGA2ZFeGwyfxQsEU%2BtU5czJRm90omZdaTS4HSZT20H6dmMLElEbVkh%2FcRFJb4HVxooEBOUI9%2BxbcPl205vmNbOwbzgsj%2FtRcwJ8DwLZCI%2B3Aw0B5Ro%2F9hZwlCFCG6gqx91C4W%2FTQoSv7VLgHTkg3cs3SgLCu6DnI4ShNTTGz79PVkZpKT3nCggJJADn6dDaEd2PnDrnqlTr4EFlfol637%2BFY%2Fh94%2F2%2BQoUEuCayTc6sWnKrRH1Xs4CHtUXiCfG%2Btn4wTylnedSABMZJGy5%2FaqlTxWnQq1u4ZQrPB%2BebPHJ9AI0CuobEXOBwezcCWx87Yw6siBd4T3skRYsr%2FdnOG1EmyZS%2BAHOHZE9JqCC02lMigAj5Q2EZJh4nuFbVeBWs%2BvNyQjjdsx%2BrOhkB1bE%2Fln4DFd%2FYJEwg7LizwY6pgEz5UaWr1bOTWgeqR3%2FFbQhFwe40vVVFUVYDaAVrakYbDqauFxxbqh3LuCS8vFqmHc1ZnLcUGuLWvEYIntEPlhjuoWtJdKWc9ayFm09HixSXnFBqOCkxR4g42g13EBFz6S%2Bxhcb5DkO%2BUhMQOu2YbqPNhkuNhJ9qLkuy4EZU7uqkqLtSdWDXsMnThU4pPwZ%2BDzX5p1Jp5rYZFtgS0bqok8KZ%2FLJw9rp&X-Amz-Signature=ddd1f5004f7e0763cdfaaf770f524672065c7fe2f50a2c0b9f9eb076639cca6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK66AQKD%2F20260504%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260504T134721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BXfwOV6RdvOOrRJQ3072AixZOdYQvnkzZ0g6j4bJnDAiAhDdValFB0aYAs1%2B%2BR6Re2CLcqKB37JV8lYt5CBk7VnCr%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIM6VAb7V19ervHyycQKtwDdyjVxBrvogWmbeYWWhzmSsRNPgnB65dwvJdgs0jwz6eaESjMFfWThdGmSOJbiRxdONhRW8jBGrDtDXCT%2BjBjQIk4xkNDBB4PM%2BR5PJ08p%2FvxOHc9fRRqQXmagA7w8dJE%2FuKh1e%2B2P8%2Fq%2BAd0uC3brYkAT6nvGXVV%2B%2B698%2FCtYQug4eUek9J%2FDrtaOoeLb8P8AQrDxMZIzsyuMnVL8dFzDk7mSGj67VRGA2ZFeGwyfxQsEU%2BtU5czJRm90omZdaTS4HSZT20H6dmMLElEbVkh%2FcRFJb4HVxooEBOUI9%2BxbcPl205vmNbOwbzgsj%2FtRcwJ8DwLZCI%2B3Aw0B5Ro%2F9hZwlCFCG6gqx91C4W%2FTQoSv7VLgHTkg3cs3SgLCu6DnI4ShNTTGz79PVkZpKT3nCggJJADn6dDaEd2PnDrnqlTr4EFlfol637%2BFY%2Fh94%2F2%2BQoUEuCayTc6sWnKrRH1Xs4CHtUXiCfG%2Btn4wTylnedSABMZJGy5%2FaqlTxWnQq1u4ZQrPB%2BebPHJ9AI0CuobEXOBwezcCWx87Yw6siBd4T3skRYsr%2FdnOG1EmyZS%2BAHOHZE9JqCC02lMigAj5Q2EZJh4nuFbVeBWs%2BvNyQjjdsx%2BrOhkB1bE%2Fln4DFd%2FYJEwg7LizwY6pgEz5UaWr1bOTWgeqR3%2FFbQhFwe40vVVFUVYDaAVrakYbDqauFxxbqh3LuCS8vFqmHc1ZnLcUGuLWvEYIntEPlhjuoWtJdKWc9ayFm09HixSXnFBqOCkxR4g42g13EBFz6S%2Bxhcb5DkO%2BUhMQOu2YbqPNhkuNhJ9qLkuy4EZU7uqkqLtSdWDXsMnThU4pPwZ%2BDzX5p1Jp5rYZFtgS0bqok8KZ%2FLJw9rp&X-Amz-Signature=3bc4c3c538041244d4f70aacffd1a9fe02b0b35d21f3008daf52d67374ade1c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







