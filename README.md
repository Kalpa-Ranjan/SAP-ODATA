



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PZTH4VD%2F20261116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261116T001602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEgeEAhxb7V8Mtm2pTq7g9LZPU8%2FiazMIKl3kahk9HVgIgY6FJb4Q8jD%2BrxReCCMWtZKwswvsaHkpdRUJ2t4CwxmgqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKNW3fFJa3EjVFlEyrcAyvqXmZyT9HBIglDWCa6786PeEepZSS8cASQYhurr7GzWnTVGCuQVJyDcVqmKUPXyC5CtaB6E3ZvdkH9s4%2F%2BS9MrAg3AI3%2FiRIbsvh2dCsy2JpNZgjZC9XUt0Eo5DwP8i%2FZEB5AwvR7gpQy1y5CNADTD3hQH%2BenTPz4QZZLptr7K14U03Q5hR1UbU5cHzT4ZJiS7wgRyJ0OW8mFIWhHBTeIp%2B2Nqd2OUjgAOBLf4wmipgSPHKGXe%2FMORl882BBZPFeDs%2FGVaBnv7CdvZSuVawAgd3ESbfzBnQdWKOqZQnqTfta%2B2iYXTEZ%2BgLpXLnDkzIumiWQJQOKxrzmNspAS4BIrB411DrtGeySAhFHuKnuAL64bZme0TTvuRgaR0m6FscaiT5CWPjp%2FZvoEdL0imb6gFzlCrXR4yShY%2FBO5ehdAtyNlguCeVfXDc12cwrvj%2FhvA38NBc4mxpjKJtvXrpq1MLpw8OE2MHs6zwdYlY%2FQ7Ev2NgeWQx6xDZljJhA6rzYz6jQH9Z%2Foot%2F%2B2rBvFKtV7ikPRBPCKtAynkTQxUO0MZeNf3B9D0jkHrjSaX0oh0U6Z0Y77y7nIqeXJdlJWiHMmsr9UEzErZfpagb9nsYWCyhnrFBtrMctbaiaA0MIzD6NcGOqUB%2FGnKSTRzbbvNbHIxVHr%2BzGJMYPvzWZ22rDFmoVV1Y0ddY%2FNlePNyg7TokgST9c1WfkK795mIoLcrdNp%2Bm1IviY0rLl36uCvudAz6FCiOg2U%2FENIzZGaBykUTcP%2Fk2emVaqu1fcqaAN7yAqpDqHUaAsx6k0czLxdieOqZGJQuJ5QbJstjoLMUrtFQ7673Mh1iu3GJzibL6tfeNLoxviow0auPMz0e&X-Amz-Signature=5162561e94c46443a07de557ae3deda1eeeee8ae74425d197801abac55541164&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PZTH4VD%2F20261116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261116T001602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEgeEAhxb7V8Mtm2pTq7g9LZPU8%2FiazMIKl3kahk9HVgIgY6FJb4Q8jD%2BrxReCCMWtZKwswvsaHkpdRUJ2t4CwxmgqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKNW3fFJa3EjVFlEyrcAyvqXmZyT9HBIglDWCa6786PeEepZSS8cASQYhurr7GzWnTVGCuQVJyDcVqmKUPXyC5CtaB6E3ZvdkH9s4%2F%2BS9MrAg3AI3%2FiRIbsvh2dCsy2JpNZgjZC9XUt0Eo5DwP8i%2FZEB5AwvR7gpQy1y5CNADTD3hQH%2BenTPz4QZZLptr7K14U03Q5hR1UbU5cHzT4ZJiS7wgRyJ0OW8mFIWhHBTeIp%2B2Nqd2OUjgAOBLf4wmipgSPHKGXe%2FMORl882BBZPFeDs%2FGVaBnv7CdvZSuVawAgd3ESbfzBnQdWKOqZQnqTfta%2B2iYXTEZ%2BgLpXLnDkzIumiWQJQOKxrzmNspAS4BIrB411DrtGeySAhFHuKnuAL64bZme0TTvuRgaR0m6FscaiT5CWPjp%2FZvoEdL0imb6gFzlCrXR4yShY%2FBO5ehdAtyNlguCeVfXDc12cwrvj%2FhvA38NBc4mxpjKJtvXrpq1MLpw8OE2MHs6zwdYlY%2FQ7Ev2NgeWQx6xDZljJhA6rzYz6jQH9Z%2Foot%2F%2B2rBvFKtV7ikPRBPCKtAynkTQxUO0MZeNf3B9D0jkHrjSaX0oh0U6Z0Y77y7nIqeXJdlJWiHMmsr9UEzErZfpagb9nsYWCyhnrFBtrMctbaiaA0MIzD6NcGOqUB%2FGnKSTRzbbvNbHIxVHr%2BzGJMYPvzWZ22rDFmoVV1Y0ddY%2FNlePNyg7TokgST9c1WfkK795mIoLcrdNp%2Bm1IviY0rLl36uCvudAz6FCiOg2U%2FENIzZGaBykUTcP%2Fk2emVaqu1fcqaAN7yAqpDqHUaAsx6k0czLxdieOqZGJQuJ5QbJstjoLMUrtFQ7673Mh1iu3GJzibL6tfeNLoxviow0auPMz0e&X-Amz-Signature=2b9ccf236e8cf12bb1316e091c609418a7817b810d15888f7aa9d8bfebdee9a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







