



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ246HZP%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T125530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAZrpIK7eEw%2FfqK9Owcrs4aHhZ8wYGtE2%2BlNb2WKcWDxAiEAo9rtkiHj140jH4icEGjAh3qwxiPx6d694AyR%2BGSd32AqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2pXFI4TzVhazd88ircA4%2BRxtvbvXX7ACmnOHCPAjGj1f7kdkPAbM7pGCMK7N7EgHcIeixahlGdh8Pr6t9KJtd7eEBYbqGqEr77oZIe%2Fjh%2F9kfDTfyISaV0x5TCyg9hoJ4K9%2FrT382IGZVmk4FhgYRiDrVKzyk20iQOF2I2jJrQw%2Fx52VlUNkwnyP3HI2tBQLSwxtXPSSDXHWIXA%2FONpZ36HUQ0b9zcKqh71xNoVZnp%2FRFzgeqbfv1PSWagkUZ3Gw4o5NlR8nAvqoNAUE7F9WHiWKNl1bq0fMw58GiT7w3EZU3HdsJw7D1ldpPumsBu2HlMfEJYuX32sFSgyLM2gZr%2FyjPih13uX4I5IVcFvPI71BacEGdsXp5ypHkQLOHC3no1Td7jWkefc%2BfzcH7XV6awCCTpB6Qu1jBa6yT7UVvXMrYNbZF%2F8UpR5cKVlbsdYk4OG6fzlS5hmaxeNua2FmvyOdmelRgmswiq4lE%2FsfQKVztGARW0vWcDRSwhBUKxkVBaueIbQ5Of0qnpjuHLuSZRYyUzPETs4mFL41f842qgMzc8xWao%2BB6hJXGp4iwrYniGvlS0ZR%2F9HUL4fwnnvQnAodPL0mTBQp0SiGi5HIIpBUGFlJlgBcuEeQdDojUMEGdrwe%2BYFqwGV01AMOm4mc4GOqUBL1us48cqE1TBoComvhaV4nrnrudxxLniXulEtjb%2FArAlu%2FhISVb0wpZapd5de4ON21hLcHWx3fQqNJKE%2B4SYeqpDOZ1R1enbJ4rjgq5Xitl5w53jRaJF8Ws5jHog6vso00QQiPsFUf%2FVEKHJ0pKXfS9Mz6flrgvS7IHw3YdpmTjdZSnbrLRXfFOwh8zh%2Femq5L19%2FoCxd4v54%2BEx0fHQ4o5Z%2B1UK&X-Amz-Signature=ee75ed8a1f90de9aae8755c854b0b25a74bebf33d2c93affc8912e4999ff93f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ246HZP%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T125530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIAZrpIK7eEw%2FfqK9Owcrs4aHhZ8wYGtE2%2BlNb2WKcWDxAiEAo9rtkiHj140jH4icEGjAh3qwxiPx6d694AyR%2BGSd32AqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2pXFI4TzVhazd88ircA4%2BRxtvbvXX7ACmnOHCPAjGj1f7kdkPAbM7pGCMK7N7EgHcIeixahlGdh8Pr6t9KJtd7eEBYbqGqEr77oZIe%2Fjh%2F9kfDTfyISaV0x5TCyg9hoJ4K9%2FrT382IGZVmk4FhgYRiDrVKzyk20iQOF2I2jJrQw%2Fx52VlUNkwnyP3HI2tBQLSwxtXPSSDXHWIXA%2FONpZ36HUQ0b9zcKqh71xNoVZnp%2FRFzgeqbfv1PSWagkUZ3Gw4o5NlR8nAvqoNAUE7F9WHiWKNl1bq0fMw58GiT7w3EZU3HdsJw7D1ldpPumsBu2HlMfEJYuX32sFSgyLM2gZr%2FyjPih13uX4I5IVcFvPI71BacEGdsXp5ypHkQLOHC3no1Td7jWkefc%2BfzcH7XV6awCCTpB6Qu1jBa6yT7UVvXMrYNbZF%2F8UpR5cKVlbsdYk4OG6fzlS5hmaxeNua2FmvyOdmelRgmswiq4lE%2FsfQKVztGARW0vWcDRSwhBUKxkVBaueIbQ5Of0qnpjuHLuSZRYyUzPETs4mFL41f842qgMzc8xWao%2BB6hJXGp4iwrYniGvlS0ZR%2F9HUL4fwnnvQnAodPL0mTBQp0SiGi5HIIpBUGFlJlgBcuEeQdDojUMEGdrwe%2BYFqwGV01AMOm4mc4GOqUBL1us48cqE1TBoComvhaV4nrnrudxxLniXulEtjb%2FArAlu%2FhISVb0wpZapd5de4ON21hLcHWx3fQqNJKE%2B4SYeqpDOZ1R1enbJ4rjgq5Xitl5w53jRaJF8Ws5jHog6vso00QQiPsFUf%2FVEKHJ0pKXfS9Mz6flrgvS7IHw3YdpmTjdZSnbrLRXfFOwh8zh%2Femq5L19%2FoCxd4v54%2BEx0fHQ4o5Z%2B1UK&X-Amz-Signature=d547c799bd7ea1a43042be8482529a4f41d6fb7ab3d81745a3d5c22a61b85c33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







