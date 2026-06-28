



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UNS63V2%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T025609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHrxx%2FI0iqlR0%2Fx13d5AdVnZOaIOokI7JS%2FriXyO2ri7AiEAheD7GKCgQWrX%2B6319FoIZTJHxGmrJnIZMNJrB4T0Io4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEgungYbXeYFV%2BO9NyrcAxIvPJeAr%2B73e14msu%2B3dwZ8DWLTo6LyZORbl%2F%2Fr5TRqbHbvMc8TBEscXbmDycNhuCgaex1h2mHzm6Ui%2BJNWjCTO8LaBLCA8Ri0wL3lUR722z2T%2Fp%2F%2FzBd%2FESIYZ2MiAisgIxMT3s2Al%2FtbymdCquFKyCsy14LPeSXV3%2FcKuyNP39M%2FxjiUqmtR09pdxmrmSJP6o7G71L2uQsr%2BFSAq8sNQKEqWuNC81cn%2F0U9lhkTm1ZGxbBbZ9LCCK%2B9NmUZ9wDCDCyC1sWfQ%2BdkE6h4HMoKexWIkXtt%2BuXd%2F200B81hLRlN7G2KyX%2BgQsgdKlzPgKVU43JRznKoVQm8WVmC3HAxQ2uO8Km43sUgfFuNs1UHlYKHYxymlUyjszHjFTymD3OHUnhiwC%2F7hBUlPFF0jLmWorWAAao0pdGhVKEZR4Im4UZK7b9HqSposg09InVYWNYXqdvYxIQ9xRJlYxhT9LsZr77D3ETqMYwUto0380TvAPjfJqCsQi1Z2sRfxG4KlTvsleoV0EEEctdvS0g47BpunpFw%2F3fgIodjV%2FLZQlrTJhBFCUAxVz2wPUww8w6zpzAKWLyjiNYWHLWsYIxg4J7Zfs63TmZhn60S1DOj2qJs9bQWZxSsDv2stYS19zMP7FgdIGOqUBEQX2N87NHCU9hYQ14kQZm4uXlrdIPdreL7ZJIHIMJnU8RvFInhNMJfXQQcV47fWZtTk59hW5IT3MW1Ma3s2KSl4eC%2Bhp0g4MLWbP4SiFv8jqYyCfoJIkr9TYXlzVJlMEIklWczDoQl0%2FGFRFdvmmfgFLp7EasDAUWw4Or1oE%2Fx6s%2F271e%2FKxwBPGD6S0kYclCTIYzdMdciw7MJkH81%2BX8M6IqpnH&X-Amz-Signature=89322e277b66f2558b684e1168e08a96b051357cca180dc4a76d527a0272d578&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UNS63V2%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T025609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHrxx%2FI0iqlR0%2Fx13d5AdVnZOaIOokI7JS%2FriXyO2ri7AiEAheD7GKCgQWrX%2B6319FoIZTJHxGmrJnIZMNJrB4T0Io4qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEgungYbXeYFV%2BO9NyrcAxIvPJeAr%2B73e14msu%2B3dwZ8DWLTo6LyZORbl%2F%2Fr5TRqbHbvMc8TBEscXbmDycNhuCgaex1h2mHzm6Ui%2BJNWjCTO8LaBLCA8Ri0wL3lUR722z2T%2Fp%2F%2FzBd%2FESIYZ2MiAisgIxMT3s2Al%2FtbymdCquFKyCsy14LPeSXV3%2FcKuyNP39M%2FxjiUqmtR09pdxmrmSJP6o7G71L2uQsr%2BFSAq8sNQKEqWuNC81cn%2F0U9lhkTm1ZGxbBbZ9LCCK%2B9NmUZ9wDCDCyC1sWfQ%2BdkE6h4HMoKexWIkXtt%2BuXd%2F200B81hLRlN7G2KyX%2BgQsgdKlzPgKVU43JRznKoVQm8WVmC3HAxQ2uO8Km43sUgfFuNs1UHlYKHYxymlUyjszHjFTymD3OHUnhiwC%2F7hBUlPFF0jLmWorWAAao0pdGhVKEZR4Im4UZK7b9HqSposg09InVYWNYXqdvYxIQ9xRJlYxhT9LsZr77D3ETqMYwUto0380TvAPjfJqCsQi1Z2sRfxG4KlTvsleoV0EEEctdvS0g47BpunpFw%2F3fgIodjV%2FLZQlrTJhBFCUAxVz2wPUww8w6zpzAKWLyjiNYWHLWsYIxg4J7Zfs63TmZhn60S1DOj2qJs9bQWZxSsDv2stYS19zMP7FgdIGOqUBEQX2N87NHCU9hYQ14kQZm4uXlrdIPdreL7ZJIHIMJnU8RvFInhNMJfXQQcV47fWZtTk59hW5IT3MW1Ma3s2KSl4eC%2Bhp0g4MLWbP4SiFv8jqYyCfoJIkr9TYXlzVJlMEIklWczDoQl0%2FGFRFdvmmfgFLp7EasDAUWw4Or1oE%2Fx6s%2F271e%2FKxwBPGD6S0kYclCTIYzdMdciw7MJkH81%2BX8M6IqpnH&X-Amz-Signature=589aeedb05c7ec9832c644c6d221cd40b37618543a7de8ce8215cafc3014b234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







