



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRRQ7NC6%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T181110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeH6HTlDT%2FVlW2DcYkkKvz%2Bu8E8s1krDnlo%2FIJB37tSAIgXmzK4EyUC0tNq%2FTa1n5%2BOv%2FsW5pzD%2BSGAiMAaG%2Bir4sqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtlr3IvLC%2BSn1gTzSrcA3h0Hc60RmwK8uI7JedJuocDMuGHolhyPNAXT4RPFrwZLY7AyNwIV4PUIQW6T8BbD1zOTE6HF%2FS%2B0QygneJ3oH%2BUlSM6VS2wJDhAWoDn3N4LKhnUq22Dhbt%2F8Yz0fhzAD9k2ILILjdUj8w%2FHz1YZBaLFVJfS9szC9hcbXbVXFCm9McTPjuxcgf6xDb%2BldS%2BecC1rrjLYgoDcEMCjSd3zBxai17ZUO4MY%2FKXgXOuzwx%2FqzDVFMDvlmxbAzENdDwDkAzr%2F%2B1%2B64%2BAbBW6rQtzx%2BMdRxxQb1Pf4xrf9u%2Bo3vK9SqjzHLZj%2ByBgk5UOpZI56m0V7fqqalg%2FH3tvxcO20uTMU5RjFylq6tBNFZ0zG63CpdycbzYjV2TWqEX2VpCbpxZUcb%2F7tl3rJJTgqZmmagiShMbHdLy8vzCJMTaDSd4SjRLO17QyiAWjS53xAIx6cYsfkkXydnNeCcJmIdl6%2Fm3S3OUeLiEl3Ce3Gwsk2mdur6UoAiFzVL1RkHBA%2F96Vxxe65dhtwJ8Zvp%2BPr23RDTh23vpoc4iZX3uZJQ7J5iWfZ%2FmyzgsThNOWNyO44yyeIZ6Sc4J8gvd92%2Fllt1hd0zu7j2IsO%2BT4z1dNttQNLG8EU3y2Q1oZD26OFlYNtMJ%2FZudYGOqUB9Zbq3KaEdbjocPoWqUTaycPpeR4LB3kOiKatqAOlJs%2FUWqcYeewqJwRtq8r824BgTycU%2FhVkGlw3lDORx5GJB5yPQ9PX9Z8eCBi4xoZ1NcZfZ%2BGd7lq6QQ9kggTTCLvbjRcAdEIbsvW%2BxQnJDqY3O5XxTxqgC7PRFVzUuOx7%2Fe79Sb4YzZ%2BGyorcFaVpEUvRLqQyKleX3TY5iOA5Vc1qavCwNTrA&X-Amz-Signature=d7f34dbb68cb4ae5e474b3f6f7cbaa1024bbce17254b06b8d9aac53eba380b08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRRQ7NC6%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T181110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeH6HTlDT%2FVlW2DcYkkKvz%2Bu8E8s1krDnlo%2FIJB37tSAIgXmzK4EyUC0tNq%2FTa1n5%2BOv%2FsW5pzD%2BSGAiMAaG%2Bir4sqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtlr3IvLC%2BSn1gTzSrcA3h0Hc60RmwK8uI7JedJuocDMuGHolhyPNAXT4RPFrwZLY7AyNwIV4PUIQW6T8BbD1zOTE6HF%2FS%2B0QygneJ3oH%2BUlSM6VS2wJDhAWoDn3N4LKhnUq22Dhbt%2F8Yz0fhzAD9k2ILILjdUj8w%2FHz1YZBaLFVJfS9szC9hcbXbVXFCm9McTPjuxcgf6xDb%2BldS%2BecC1rrjLYgoDcEMCjSd3zBxai17ZUO4MY%2FKXgXOuzwx%2FqzDVFMDvlmxbAzENdDwDkAzr%2F%2B1%2B64%2BAbBW6rQtzx%2BMdRxxQb1Pf4xrf9u%2Bo3vK9SqjzHLZj%2ByBgk5UOpZI56m0V7fqqalg%2FH3tvxcO20uTMU5RjFylq6tBNFZ0zG63CpdycbzYjV2TWqEX2VpCbpxZUcb%2F7tl3rJJTgqZmmagiShMbHdLy8vzCJMTaDSd4SjRLO17QyiAWjS53xAIx6cYsfkkXydnNeCcJmIdl6%2Fm3S3OUeLiEl3Ce3Gwsk2mdur6UoAiFzVL1RkHBA%2F96Vxxe65dhtwJ8Zvp%2BPr23RDTh23vpoc4iZX3uZJQ7J5iWfZ%2FmyzgsThNOWNyO44yyeIZ6Sc4J8gvd92%2Fllt1hd0zu7j2IsO%2BT4z1dNttQNLG8EU3y2Q1oZD26OFlYNtMJ%2FZudYGOqUB9Zbq3KaEdbjocPoWqUTaycPpeR4LB3kOiKatqAOlJs%2FUWqcYeewqJwRtq8r824BgTycU%2FhVkGlw3lDORx5GJB5yPQ9PX9Z8eCBi4xoZ1NcZfZ%2BGd7lq6QQ9kggTTCLvbjRcAdEIbsvW%2BxQnJDqY3O5XxTxqgC7PRFVzUuOx7%2Fe79Sb4YzZ%2BGyorcFaVpEUvRLqQyKleX3TY5iOA5Vc1qavCwNTrA&X-Amz-Signature=b0197f6637456dc7dfdb201042d1fe5da3d9f2a307091826272e688efe6813fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







