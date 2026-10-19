



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S46VAIF%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T180951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIBq21uSfr0weLDIWKPUQI9iB2Cilv58B6KDToZI1dfXvAiEAhmTlG%2BezyEAW3XQ95HTWhvjCUwWSw%2FclKSXAi8vYk4Qq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDCjzmaewglY9JxG4ZSrcA5S1hbzdJTfUQmcTT5zyLJ7Dfcr4nvQa8VZS%2FIEc9CiQm1IEyhJWoIMvs3KMp2F4Paaq%2FD7PY8ZshUWUjB15QLOHz8kFcavcqPLGMmUkRia0rBUlM%2BJvf4LXCshrawCMSoqItM8Vgt%2B1%2Ff8XA6qqKqGtZWZyzlHi72Ty%2FEF%2FrWjAGlJ4jDGFEwICtJg9w6o%2B1eU1%2FDr2clYH5MfeMyOGAUPmQNilt%2BGWpIz5NOc6f4c7RmX%2FZNCNsVWqhyY3%2FV1s2tKWmv7iM3Jrf4w3ybc2KiqmHFNabZUpfDZsARJv8GT%2Fasb2Zq2GyZd5Al%2BtTGgTs%2FgF81qZaMqyMhr1SPBqmaGxGxsvO3bvVuz5vb0enT7gZTCudjtE5EOcnwBwXlpnYAblgv%2BhUflZQ%2Fxpe6RTWgOhpZbMuDwU%2BNgeOViC4IbWTzl5ptNxjLWAtDGuw%2FYPv20kVm3NzF7TeOAyOo4UgEKH6Hz6Qw9Tm7wfvYGqm4C3Wu9NHXqBj7HN3YI4EoZY%2BuA3lE44aDYoOVe2LQyPjgQjOUDFwmqSYYz16EjNzsfCaxc%2FUnHUeDYiN0yj%2FTtxUaioGiTZTuA0MuB%2BMaezF3vM09nEERL9YEHAqsBdnTo4IUpI5kWSsZkCd75hMOnf2NYGOqUBrSMeN16A7PxlrDBTGPN3ZYW2zS5Dbr6JyW0WWU8cCk3w%2FroK7jch1mCLHUMl1AxGf7pwBQgsiFPnKkKzDB3bG22WF5HaQgsrdOEDmGrDRg3Z7Kon%2B0iLv0PEFQJtF9dTAuItXRA9Gf7AkstPCeH%2F5gX4iNzg6DoBdyaqQA05Gvf%2F%2FjA4MIGuxEl6FxApMhSHj1jxRp9oEnsGgx4UU6uZfgzRaiQk&X-Amz-Signature=861881e1670e22678501f78e2a900b9b4d2fc7e4fac1506341ac9a37551ff43a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S46VAIF%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T180951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIBq21uSfr0weLDIWKPUQI9iB2Cilv58B6KDToZI1dfXvAiEAhmTlG%2BezyEAW3XQ95HTWhvjCUwWSw%2FclKSXAi8vYk4Qq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDCjzmaewglY9JxG4ZSrcA5S1hbzdJTfUQmcTT5zyLJ7Dfcr4nvQa8VZS%2FIEc9CiQm1IEyhJWoIMvs3KMp2F4Paaq%2FD7PY8ZshUWUjB15QLOHz8kFcavcqPLGMmUkRia0rBUlM%2BJvf4LXCshrawCMSoqItM8Vgt%2B1%2Ff8XA6qqKqGtZWZyzlHi72Ty%2FEF%2FrWjAGlJ4jDGFEwICtJg9w6o%2B1eU1%2FDr2clYH5MfeMyOGAUPmQNilt%2BGWpIz5NOc6f4c7RmX%2FZNCNsVWqhyY3%2FV1s2tKWmv7iM3Jrf4w3ybc2KiqmHFNabZUpfDZsARJv8GT%2Fasb2Zq2GyZd5Al%2BtTGgTs%2FgF81qZaMqyMhr1SPBqmaGxGxsvO3bvVuz5vb0enT7gZTCudjtE5EOcnwBwXlpnYAblgv%2BhUflZQ%2Fxpe6RTWgOhpZbMuDwU%2BNgeOViC4IbWTzl5ptNxjLWAtDGuw%2FYPv20kVm3NzF7TeOAyOo4UgEKH6Hz6Qw9Tm7wfvYGqm4C3Wu9NHXqBj7HN3YI4EoZY%2BuA3lE44aDYoOVe2LQyPjgQjOUDFwmqSYYz16EjNzsfCaxc%2FUnHUeDYiN0yj%2FTtxUaioGiTZTuA0MuB%2BMaezF3vM09nEERL9YEHAqsBdnTo4IUpI5kWSsZkCd75hMOnf2NYGOqUBrSMeN16A7PxlrDBTGPN3ZYW2zS5Dbr6JyW0WWU8cCk3w%2FroK7jch1mCLHUMl1AxGf7pwBQgsiFPnKkKzDB3bG22WF5HaQgsrdOEDmGrDRg3Z7Kon%2B0iLv0PEFQJtF9dTAuItXRA9Gf7AkstPCeH%2F5gX4iNzg6DoBdyaqQA05Gvf%2F%2FjA4MIGuxEl6FxApMhSHj1jxRp9oEnsGgx4UU6uZfgzRaiQk&X-Amz-Signature=9e7638900b7b20a135c4d1b99d0ebe8133644f37aa6735b0abd1e89afca764c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







