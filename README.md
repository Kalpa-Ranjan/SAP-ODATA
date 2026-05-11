



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7TLFH7N%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T143801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDW8KUwupQHGVR8yPODZ7mzkNVwEQX85SfP5rUHOXnzhQIgMjcpAyGbM8AQDBRamGfu0LNRL%2BcWBffEZp19trnGqqQq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDE3XuZG9WfLuZjOUbCrcA5eGhVWkqUhZCrRqP%2F9D4xZ89Az6ABmVCFIF6jYrTurL3BQshYDPkdOKsBM6NJDHTreDBoTcQkozgUJllTWN1j262aZqBQ5PZQ9KXp9QVKSRs%2B6Bs66XywQ2xwb6d73O66J3jYLtXdFQsKsGIDbmyjRQRGVlLE0%2FeK%2F5WFX720w8gojZpKKpk8i1I526FYKylcUC5D84Qzpkvc5%2FIhxHj9P%2BKPie%2B5dA%2FwqS67EtVMgAoA%2FKapxzuNmKw6xeoWSKSesXSg8OGYAfeQO9IQk%2FIMIkIbnEC4CU%2B%2F%2BlSgP0V8pedIuwDHEw6v4zs1Pyj7Fda3fjQJ1jtUbqWsHYWB3lWGeYps0wfNQk2o0T3SHfKLUGL8Fueo%2Bu9JmYH0x1hOA3AxlQ7wXpYLYilxMz5iU7e4q%2BcQklIFiiMZ6pxZdf8%2F5qSf0gshTqBpacfQHhyhOgnRUmWlp8yPrRCIZCr5lzPTYvjnvg8GLdUXUgXyPhCeQnDr9kcYkbq3o5%2B9wcT8R5G5VF0uOuFnLhD9YHqficVWEUl4wp%2F3zauSFk4YbPqsRM5OL6fi8TjfIYxA1Dfg0hv5NxuHN%2FeywE1lz3rbI5LsokTlP%2B6m767aEGnFsoHYtsHDjQgPqlfA9%2F%2F2DHMJrNh9AGOqUBdr%2BJ%2B5M6K%2FRFJ6n%2FzRgAzCvgxtZoOfYDsi72t1OF7aCGOi9OxSM4gtaz3MWoYf%2Byv2WpOF2yAFKtFEQJTiGx1J2eXtfu2sBXgXaKyUGBs%2FeQm5tYOYtNQWvvY411Bn08VhpCMmqnUsairHM0UGC337fIWtTp8T5Ip%2BrNuUFm2aEKIQTUqu%2B8qaNfdYmYh9Ep8No7hWOmmlK5Y16%2BgTHq9TsED0Sh&X-Amz-Signature=e5a2ae1a0e88b8fa731a7daa5eacd5aefe0abcb856d7bb10cfc9da24a80c5424&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7TLFH7N%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T143801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDW8KUwupQHGVR8yPODZ7mzkNVwEQX85SfP5rUHOXnzhQIgMjcpAyGbM8AQDBRamGfu0LNRL%2BcWBffEZp19trnGqqQq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDE3XuZG9WfLuZjOUbCrcA5eGhVWkqUhZCrRqP%2F9D4xZ89Az6ABmVCFIF6jYrTurL3BQshYDPkdOKsBM6NJDHTreDBoTcQkozgUJllTWN1j262aZqBQ5PZQ9KXp9QVKSRs%2B6Bs66XywQ2xwb6d73O66J3jYLtXdFQsKsGIDbmyjRQRGVlLE0%2FeK%2F5WFX720w8gojZpKKpk8i1I526FYKylcUC5D84Qzpkvc5%2FIhxHj9P%2BKPie%2B5dA%2FwqS67EtVMgAoA%2FKapxzuNmKw6xeoWSKSesXSg8OGYAfeQO9IQk%2FIMIkIbnEC4CU%2B%2F%2BlSgP0V8pedIuwDHEw6v4zs1Pyj7Fda3fjQJ1jtUbqWsHYWB3lWGeYps0wfNQk2o0T3SHfKLUGL8Fueo%2Bu9JmYH0x1hOA3AxlQ7wXpYLYilxMz5iU7e4q%2BcQklIFiiMZ6pxZdf8%2F5qSf0gshTqBpacfQHhyhOgnRUmWlp8yPrRCIZCr5lzPTYvjnvg8GLdUXUgXyPhCeQnDr9kcYkbq3o5%2B9wcT8R5G5VF0uOuFnLhD9YHqficVWEUl4wp%2F3zauSFk4YbPqsRM5OL6fi8TjfIYxA1Dfg0hv5NxuHN%2FeywE1lz3rbI5LsokTlP%2B6m767aEGnFsoHYtsHDjQgPqlfA9%2F%2F2DHMJrNh9AGOqUBdr%2BJ%2B5M6K%2FRFJ6n%2FzRgAzCvgxtZoOfYDsi72t1OF7aCGOi9OxSM4gtaz3MWoYf%2Byv2WpOF2yAFKtFEQJTiGx1J2eXtfu2sBXgXaKyUGBs%2FeQm5tYOYtNQWvvY411Bn08VhpCMmqnUsairHM0UGC337fIWtTp8T5Ip%2BrNuUFm2aEKIQTUqu%2B8qaNfdYmYh9Ep8No7hWOmmlK5Y16%2BgTHq9TsED0Sh&X-Amz-Signature=c9814f6cbcf85de36f8de390c888d68f24565ffd6eff725c60dd733a4300f769&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







