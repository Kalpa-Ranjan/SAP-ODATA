



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IY3MDHC%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T065645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEGaifHmUVybkG%2ByR6LaXwNrMxB45e35VdVoGNF4vnkeAiAeiJao2I5m8pJ9vVMkpssd5p%2BzbE31nYpnVrpnbV5GViqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuNYa6qzDpc6gs9HLKtwDyoDxN0Q0JOBHEU4iRBO6az0fJq5HqDtVcqK%2Bp6vJgkw7z%2BAxlqoW5oie7YHo%2BmXAAc1K2UBb%2BuOGEgCwv6C5quxyZs85lrm4yHShsYHJjLfWTTi3JBUlFlRpmqh3E9dXor5xFlgoOc8u5DGlt7ZO%2BrwDMGxHn4ExA4accJOj8Tg%2BDoie0BbZlG4Hq%2BT37Q%2Fx9Dzcp6SZOvg0Dwqu4LX8v2kO%2BaGgOc3hJ7TrsrYTKMLKb6fhK5SBA%2F%2BeIOumBUgZplwjrm0vZVYQrclY5Iv%2BOSJoyZU2ml9rWrfPXvwbX63OLj8P3fj7678aLZO8n5lvxvdIoimMCLicwH%2BxmOyjOHzuI7rNkPvvmKD0ZUQ5XcpPoNT%2FjDiD7hpHtHzmcCYaC1CrGQEDzMjxPTjM8yN7UftrpPoqbr0YA6lxTo14iJ%2FZVQVmpjpPxrx4%2BJpBxtGBO7VVl6KLnIeyZkzrnu3Lsl2yELeyMO571a1COAsDobmVWiu8CG6O2vEqpFSesq2IwakvsDmIVKuzPYgWuECBMcb7yJmge180C3pOgByf%2BYDsqnmUW2I2IflbBDxiAixr5SxHPmqSzn6QyZetv3%2FnvsmEKIu1P%2BJFsCIW2Sl8Ln%2BgLOtiez0GivGwaKcwhv%2BNzgY6pgHvj0AplcWgaJu8Z07LpwE83CzrJNcAvPUKuJoor2b3hJdMcR1GWe4bj4AAt98VKINXdscIiKIRxO%2BGtDEtv6e9oHfbBDMuN5SAEe73%2B2Q0Lh%2F8%2BnIgyx2fn9I1ZRRUyWP8EFRKFrHAxn07aMsSQHA%2BOXV2LUqAozHt2h0GldBREfLBH%2FJqD4QleYoN%2B2QqQ14d5vwvcc%2BuvaNHnIxoTVbBDD9A9eR3&X-Amz-Signature=3983b61e994baf082ae5731a2c1e4dfd3242eb595368d51c5410a596fc496e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IY3MDHC%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T065645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEGaifHmUVybkG%2ByR6LaXwNrMxB45e35VdVoGNF4vnkeAiAeiJao2I5m8pJ9vVMkpssd5p%2BzbE31nYpnVrpnbV5GViqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuNYa6qzDpc6gs9HLKtwDyoDxN0Q0JOBHEU4iRBO6az0fJq5HqDtVcqK%2Bp6vJgkw7z%2BAxlqoW5oie7YHo%2BmXAAc1K2UBb%2BuOGEgCwv6C5quxyZs85lrm4yHShsYHJjLfWTTi3JBUlFlRpmqh3E9dXor5xFlgoOc8u5DGlt7ZO%2BrwDMGxHn4ExA4accJOj8Tg%2BDoie0BbZlG4Hq%2BT37Q%2Fx9Dzcp6SZOvg0Dwqu4LX8v2kO%2BaGgOc3hJ7TrsrYTKMLKb6fhK5SBA%2F%2BeIOumBUgZplwjrm0vZVYQrclY5Iv%2BOSJoyZU2ml9rWrfPXvwbX63OLj8P3fj7678aLZO8n5lvxvdIoimMCLicwH%2BxmOyjOHzuI7rNkPvvmKD0ZUQ5XcpPoNT%2FjDiD7hpHtHzmcCYaC1CrGQEDzMjxPTjM8yN7UftrpPoqbr0YA6lxTo14iJ%2FZVQVmpjpPxrx4%2BJpBxtGBO7VVl6KLnIeyZkzrnu3Lsl2yELeyMO571a1COAsDobmVWiu8CG6O2vEqpFSesq2IwakvsDmIVKuzPYgWuECBMcb7yJmge180C3pOgByf%2BYDsqnmUW2I2IflbBDxiAixr5SxHPmqSzn6QyZetv3%2FnvsmEKIu1P%2BJFsCIW2Sl8Ln%2BgLOtiez0GivGwaKcwhv%2BNzgY6pgHvj0AplcWgaJu8Z07LpwE83CzrJNcAvPUKuJoor2b3hJdMcR1GWe4bj4AAt98VKINXdscIiKIRxO%2BGtDEtv6e9oHfbBDMuN5SAEe73%2B2Q0Lh%2F8%2BnIgyx2fn9I1ZRRUyWP8EFRKFrHAxn07aMsSQHA%2BOXV2LUqAozHt2h0GldBREfLBH%2FJqD4QleYoN%2B2QqQ14d5vwvcc%2BuvaNHnIxoTVbBDD9A9eR3&X-Amz-Signature=dbc28f081ba57afd66a5d3fbf6639a66db45eac73af173f75e755ca1ba23b031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







