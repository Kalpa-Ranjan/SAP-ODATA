



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JKZ7CRH%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T180801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcgeVBbtwGgUy31yfWCjJCdlEyjGXX22cfPO7LVOAsOwIgfqEpaqmvZnhigJLQB5QXdpUb9w0%2Bi4UJU2uOy5DLrb4qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXcqd56qzhbN7SFhyrcAwDTscVjz4D1XW1SBE9k8Ua8hCGfeUy5rIXCwhfyjpEmz1cQM9quIeheZ1wI4pXBzUyas7vhLbj8iJhFH%2Fc2APRkWp2jCxo1XVML3SMm0uX27d9UMvjn2r%2Bt4k%2BrYX71LjhgZ4GmaAioNVT7ethHwcz2ESnqNSQhiIgAYdpDG1Fv%2Fucnx8sCkH8T%2FMoqr1ctc1A8MlYNUHshQ1ltZdLvKMdtpCreyXpKoFNtnZDVfAw2HWCLj%2FWAB7aPuCBNzOzPyLEOhlUOURuSe3x1kFubzckLM58DEraoolJpTBmtvPgBSVonwAMFEPlHBcQCaoiBv3sBYCq1lniygIlMQ4lL8JHJRwjVpF4S%2Bh4800hsXhg5jMuAYJADYpPyZDRaLLNewFH9Y6RMabR4a5dTIP%2FQBtr17LSm138jUCU6CbF9wWpLfxIcSJzbRR1ba4QcJPgibIaZGPu9bz4vL4WtyXYOl58Z8dMUZ0BqpFhuyIlR2Z8rwB4GAm4t7SdfFlAkSemmy1gYOy%2FA1mR4CPSIg10X0rJQOcEO5zO0NdQWgIHlLswGo%2FkqgE3beXg9oS52tCTOB6FKpjSF6d6UdWm9wzJkzR8rrJDJdPcp6fvBw%2BVVlRwVG1kZX3MiOY2JLb9GMP6UltUGOqUB7KNFYgBthSG4MNsQ6Ib7juEYvNBP3Vw44S3jcuKf%2FHsoZbUFTnakK8hMGF%2BsleRdL4ApsErzl6cODA9VhwTt5XE04xQd74sgHR9y786Akgy9JJB58HVP%2BLY%2Fb5ZldiQVOYc1sTFWn8BfERiUYMBOWFz06U9Yn4X6YjNuHVPxhh6EctXB7tqFlxY2cMqAB0Wl617nRVybfT6dbxCsfzV2Q7GKCpX%2B&X-Amz-Signature=afafec1438ef5cdfe2ac7127c058d88cd91d021a5843bcf8b370b1d13404bfc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JKZ7CRH%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T180803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcgeVBbtwGgUy31yfWCjJCdlEyjGXX22cfPO7LVOAsOwIgfqEpaqmvZnhigJLQB5QXdpUb9w0%2Bi4UJU2uOy5DLrb4qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXcqd56qzhbN7SFhyrcAwDTscVjz4D1XW1SBE9k8Ua8hCGfeUy5rIXCwhfyjpEmz1cQM9quIeheZ1wI4pXBzUyas7vhLbj8iJhFH%2Fc2APRkWp2jCxo1XVML3SMm0uX27d9UMvjn2r%2Bt4k%2BrYX71LjhgZ4GmaAioNVT7ethHwcz2ESnqNSQhiIgAYdpDG1Fv%2Fucnx8sCkH8T%2FMoqr1ctc1A8MlYNUHshQ1ltZdLvKMdtpCreyXpKoFNtnZDVfAw2HWCLj%2FWAB7aPuCBNzOzPyLEOhlUOURuSe3x1kFubzckLM58DEraoolJpTBmtvPgBSVonwAMFEPlHBcQCaoiBv3sBYCq1lniygIlMQ4lL8JHJRwjVpF4S%2Bh4800hsXhg5jMuAYJADYpPyZDRaLLNewFH9Y6RMabR4a5dTIP%2FQBtr17LSm138jUCU6CbF9wWpLfxIcSJzbRR1ba4QcJPgibIaZGPu9bz4vL4WtyXYOl58Z8dMUZ0BqpFhuyIlR2Z8rwB4GAm4t7SdfFlAkSemmy1gYOy%2FA1mR4CPSIg10X0rJQOcEO5zO0NdQWgIHlLswGo%2FkqgE3beXg9oS52tCTOB6FKpjSF6d6UdWm9wzJkzR8rrJDJdPcp6fvBw%2BVVlRwVG1kZX3MiOY2JLb9GMP6UltUGOqUB7KNFYgBthSG4MNsQ6Ib7juEYvNBP3Vw44S3jcuKf%2FHsoZbUFTnakK8hMGF%2BsleRdL4ApsErzl6cODA9VhwTt5XE04xQd74sgHR9y786Akgy9JJB58HVP%2BLY%2Fb5ZldiQVOYc1sTFWn8BfERiUYMBOWFz06U9Yn4X6YjNuHVPxhh6EctXB7tqFlxY2cMqAB0Wl617nRVybfT6dbxCsfzV2Q7GKCpX%2B&X-Amz-Signature=f20c2a64760b694a88886204db518d5cf0c814d536db22fee611835e5bdcb08d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







