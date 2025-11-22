



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M6S7J3V%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T122725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCv6kVxi4INaT2%2BQCA24UiW%2FmeBR204ATT%2Bz51AjKWvOgIgInQyTAmO%2FHZQNxOYZycL9R5haA9zXqBeYlmAU4fJsOoq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLtQGvPKESYAZ4UNwyrcA3d4B05INnQ838t4%2FHU4G1xDGdy06%2BENvOUbWZPBUsfZHLpCwRvTaKLZqbMJC1ujXSii%2B6lMdEf7dYu1aW%2FZLhjzRlJKUGYj%2FEjV8G43uS%2BU3MJQPeJa41J9sGZV%2F%2BiLy4qXX%2BhREJmzbQwt8AuF3f4zuhEu4ZUlilhINhULvVwJfyBPYeT%2FCZQsT%2B6EwWBlA0A0gOIdxrJ%2BRjZWZYLbKFn%2FzqJKDYsME4Z%2Bw4HxXi3EPJ%2B4yOTY7D1kUf3RZtZeLBRB0AM93bSGlyG91R6P%2BsSw0ZidMPQpvlpz9UKY%2FKipgEpqYWTVJxFVLg8L58ETb3v%2B%2FCQQRa%2F0h9KNYhYSVOBJlkS%2FxJ8n6JCh7mjxdfikpGt03q6ey2Cgf3zMQ3yriyigKMnpKN8J0Wo8oEyCTulYSJAYgMQITL8iozAGk4BxXYpXBEKld%2F3s2dHoGI2Knyc1rwwYFED7%2F4%2FMLCARgrse5iMhwT%2FG33o8nBKXG70J3WO2FtGsXHraUqOnYs2CEu7nXVNWe5XigeAOhxs7PH%2FuCEdCfJuYBSIROq9mPx83Ib9UVtPh5HU2MzcBihlXLBbmJRoQ6KcjqKSWH2Q0cQMFzfIpn0m5Lo7wDW5EFVj8TTNkHtg3%2F%2FwpbcOHMJm5hskGOqUB9WoldJg3Qyy3wRl9hJX27chlSETwUrduYXcKiB%2Boj9IFBv5HCYe8rpq4Z0HvaSOvZWZvtVkgoaAfr9bEbEYwUmrhylymmWmtrmCxfgm8bpgut9Yfy%2BDMU%2Fo294zhrM%2Bopcw7sin3KG4%2FC4TOrA2kweiE2A%2F%2BLLGw61rV86Ti4zXUYdOOoc5Af7UlAIKtrLe%2BTWInseZEAq19OaU1ws5HLMRbEvq3&X-Amz-Signature=532d61912a4d8c408d19f7fb0192f72a6d8e269f0c48031f8a6617da16ec9f1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M6S7J3V%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T122725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCv6kVxi4INaT2%2BQCA24UiW%2FmeBR204ATT%2Bz51AjKWvOgIgInQyTAmO%2FHZQNxOYZycL9R5haA9zXqBeYlmAU4fJsOoq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDLtQGvPKESYAZ4UNwyrcA3d4B05INnQ838t4%2FHU4G1xDGdy06%2BENvOUbWZPBUsfZHLpCwRvTaKLZqbMJC1ujXSii%2B6lMdEf7dYu1aW%2FZLhjzRlJKUGYj%2FEjV8G43uS%2BU3MJQPeJa41J9sGZV%2F%2BiLy4qXX%2BhREJmzbQwt8AuF3f4zuhEu4ZUlilhINhULvVwJfyBPYeT%2FCZQsT%2B6EwWBlA0A0gOIdxrJ%2BRjZWZYLbKFn%2FzqJKDYsME4Z%2Bw4HxXi3EPJ%2B4yOTY7D1kUf3RZtZeLBRB0AM93bSGlyG91R6P%2BsSw0ZidMPQpvlpz9UKY%2FKipgEpqYWTVJxFVLg8L58ETb3v%2B%2FCQQRa%2F0h9KNYhYSVOBJlkS%2FxJ8n6JCh7mjxdfikpGt03q6ey2Cgf3zMQ3yriyigKMnpKN8J0Wo8oEyCTulYSJAYgMQITL8iozAGk4BxXYpXBEKld%2F3s2dHoGI2Knyc1rwwYFED7%2F4%2FMLCARgrse5iMhwT%2FG33o8nBKXG70J3WO2FtGsXHraUqOnYs2CEu7nXVNWe5XigeAOhxs7PH%2FuCEdCfJuYBSIROq9mPx83Ib9UVtPh5HU2MzcBihlXLBbmJRoQ6KcjqKSWH2Q0cQMFzfIpn0m5Lo7wDW5EFVj8TTNkHtg3%2F%2FwpbcOHMJm5hskGOqUB9WoldJg3Qyy3wRl9hJX27chlSETwUrduYXcKiB%2Boj9IFBv5HCYe8rpq4Z0HvaSOvZWZvtVkgoaAfr9bEbEYwUmrhylymmWmtrmCxfgm8bpgut9Yfy%2BDMU%2Fo294zhrM%2Bopcw7sin3KG4%2FC4TOrA2kweiE2A%2F%2BLLGw61rV86Ti4zXUYdOOoc5Af7UlAIKtrLe%2BTWInseZEAq19OaU1ws5HLMRbEvq3&X-Amz-Signature=59e81ef5448a39e78b26e5817d43e15571a56bfd054eadc9370f50b782945a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







