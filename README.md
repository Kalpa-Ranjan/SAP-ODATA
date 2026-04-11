



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667365MXZV%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T015233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQCGu%2BjORKRccSUjqXXVZPm1uXszAJumI34kxTc4PxZ08AIgTS37g8vkq1xcd2cc%2BGggIQma56g7a0zggbIAhx5umZIq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDDbZDz4QiGmXRCQFrircA5152DUMWksfMzs3T9YvSXwkuBUTFDHTDq4uC3j4LIO7wZRm2CVssk%2BvbTpSoF1i6Sg7pjHa6GJ7XhRDhBv11gWqS%2BQ6ye1a%2Bzu3rzQgPS%2BcpY9T7Wapd3A6%2FH7EajylkT4F6ZwJzgvzRHIQUaX89Py7p%2FLCLKQIu2M8z7w2b6rkx7ouMdIgqPauFKomBy1ZAQ2zR8TcfPJIp5GB9GO2mqvXGB0hpgtafzWZnT66EidfCTnUkOSZeBFwhJxPrRQXKG%2BAHCz4Op4LwVI3gnDtGF%2FS%2FZbSbZ9O2VqukVGa13BKXMBormcH4nXmc8AAnUoddtgah3UmIbkxw%2B%2BIH6QFY3oytuuVYzurjkAAROcIBDahe27qsOgxlw%2FYDUUFDN7XtN7TsT3eR96S8MnYEe5v3UcnNSH8QEXvn22bQ%2Fpvn3JozbHFRjQYPvkepbS16krpivIskXiymgodtOLaqPX9%2F0kXaQNS1Q1hTNKkzYmv9P6pQA64ICejMi209XNZHLFbfPI2C00IFWOzfZQuG0cfiOI%2FP0hxlCuNx56Vtk0qKn3bCMHuDsR2pQf0nNV5hr9v7rxH3BcBn0Hr2%2BH2qviW7KvPrgxPXImJtGILjbkr6EZZCH6kg4RG0M8rffdeMKKw5s4GOqUBfK9f%2BJz0zWCtftCCt40pimBa%2FXVAn0kUkrI39HQ70CQgoW7KAisEiz0olkv0a2qZeoPe8PmxknR%2Bv5YUT0Z1YS5xh%2BMeKNQqaMQ9hRl03NLw0JEIhMHC4w4kLpJr5hgT9m9v7L5SyRWJh3VRPiXaDTufcBiBlEZw3h3W%2BppVaUhBUhVxHyNxgdU4rQCXPwrj0QQxrK7jAI9gtgwDV08mMiPl0dl3&X-Amz-Signature=be23ab5f75b321cf9c53d7a2ed728cd9c4ec5bdb9f7b379df6a8bdd5fd9f83f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667365MXZV%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T015233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQCGu%2BjORKRccSUjqXXVZPm1uXszAJumI34kxTc4PxZ08AIgTS37g8vkq1xcd2cc%2BGggIQma56g7a0zggbIAhx5umZIq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDDbZDz4QiGmXRCQFrircA5152DUMWksfMzs3T9YvSXwkuBUTFDHTDq4uC3j4LIO7wZRm2CVssk%2BvbTpSoF1i6Sg7pjHa6GJ7XhRDhBv11gWqS%2BQ6ye1a%2Bzu3rzQgPS%2BcpY9T7Wapd3A6%2FH7EajylkT4F6ZwJzgvzRHIQUaX89Py7p%2FLCLKQIu2M8z7w2b6rkx7ouMdIgqPauFKomBy1ZAQ2zR8TcfPJIp5GB9GO2mqvXGB0hpgtafzWZnT66EidfCTnUkOSZeBFwhJxPrRQXKG%2BAHCz4Op4LwVI3gnDtGF%2FS%2FZbSbZ9O2VqukVGa13BKXMBormcH4nXmc8AAnUoddtgah3UmIbkxw%2B%2BIH6QFY3oytuuVYzurjkAAROcIBDahe27qsOgxlw%2FYDUUFDN7XtN7TsT3eR96S8MnYEe5v3UcnNSH8QEXvn22bQ%2Fpvn3JozbHFRjQYPvkepbS16krpivIskXiymgodtOLaqPX9%2F0kXaQNS1Q1hTNKkzYmv9P6pQA64ICejMi209XNZHLFbfPI2C00IFWOzfZQuG0cfiOI%2FP0hxlCuNx56Vtk0qKn3bCMHuDsR2pQf0nNV5hr9v7rxH3BcBn0Hr2%2BH2qviW7KvPrgxPXImJtGILjbkr6EZZCH6kg4RG0M8rffdeMKKw5s4GOqUBfK9f%2BJz0zWCtftCCt40pimBa%2FXVAn0kUkrI39HQ70CQgoW7KAisEiz0olkv0a2qZeoPe8PmxknR%2Bv5YUT0Z1YS5xh%2BMeKNQqaMQ9hRl03NLw0JEIhMHC4w4kLpJr5hgT9m9v7L5SyRWJh3VRPiXaDTufcBiBlEZw3h3W%2BppVaUhBUhVxHyNxgdU4rQCXPwrj0QQxrK7jAI9gtgwDV08mMiPl0dl3&X-Amz-Signature=6b3348495059d437fcdc5aa8316360d32200314870f4f8df0c87bc5b787696d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







