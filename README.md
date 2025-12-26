



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAOVQN2%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T011649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIB9qxJyTkB%2Bygyuy%2B%2Bp73oNrZxgjud3MgISypr1%2FOBm1AiEAmx57IvNrJngo9VpGvr7CsOW%2Fa5H2jO6wzy2At39cSr8q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDLHCPx14Ry%2FtGHzfCCrcA25zC7KOdlSgrlUkWLpV0xiOSMv2F%2FhxNM%2BMN7%2FRVa%2BBSjoocjU1GajipDqNPt7vc5HKtQOW0uQ6JQmA4MAN5RP8mhChVI26sHPXU1YAa7FAf60Krf0rd1gwh6Kjp66kQGhNFjShT0e4gXm33RnfqPXWL6IDYAItTIT2PEEeKjKN5w7z%2FvVbpdVwZuInDVJgHrg7qSaw28nKC%2F4axLVrjeFucosI3kEHqSIjtfQ7wGk0xj7HGosjNBmuq7fe75pw3AoZOSXfbo6SK3Q%2FxSmtwn3pv96QhErW42dLjT6zVly38Y8RTradC%2BKHhyTI6MUnTmo7M8ZIkzTQvKhkici63rAecP5LGk8px2%2FuSKk%2F43S97Wu6x7cV0yr9sHL0kfiyUh70jzGkKNlp14l0PPqxy%2BhtVwfK8RvMrt9vhEXLD67ZupUA375x33vkUOJlPoFMXme5mHJ7OtoNbQoGDwNuGDrKsAb2mI1r9%2BDO5xUTFJa1NOSnb7W58UUBcr3RjOvikpvablCIolm16e9XurEHZ7MK3ec4Y3EynKEFDG2EDlHF6anOStNVk6qeV4hevregZOd86s4S8EvxWAbFvfcUGX%2B%2B9f2eUaMuT0GFBconD2i58D4rbMjQsutosnh7MMOutsoGOqUBOREa61Yx6hHS4kvk86khqlJU4AZo3QL4G8C18R1QQ3wCgSlg%2BMlVsLsuIEgIuT3IV%2BGILHxD1ep8UgHp553vUk2GT2zTGSMW2R8VUI5la0ZfBXkFz5EFn8hyoGAfTXpu6qvEQ%2B79TGDUS1h1EI8JRvLEmYxxOjJxqhgFZrtsacsXG5hFdV5zwHXSK%2FdTVdxM9FVP5ZTroZokTliAYUAXIFUn%2B0a0&X-Amz-Signature=0d998744b4fc3f306a80f4be22cb9c0e6cd3aa411478303bd710013b0533f44d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAOVQN2%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T011649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIB9qxJyTkB%2Bygyuy%2B%2Bp73oNrZxgjud3MgISypr1%2FOBm1AiEAmx57IvNrJngo9VpGvr7CsOW%2Fa5H2jO6wzy2At39cSr8q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDLHCPx14Ry%2FtGHzfCCrcA25zC7KOdlSgrlUkWLpV0xiOSMv2F%2FhxNM%2BMN7%2FRVa%2BBSjoocjU1GajipDqNPt7vc5HKtQOW0uQ6JQmA4MAN5RP8mhChVI26sHPXU1YAa7FAf60Krf0rd1gwh6Kjp66kQGhNFjShT0e4gXm33RnfqPXWL6IDYAItTIT2PEEeKjKN5w7z%2FvVbpdVwZuInDVJgHrg7qSaw28nKC%2F4axLVrjeFucosI3kEHqSIjtfQ7wGk0xj7HGosjNBmuq7fe75pw3AoZOSXfbo6SK3Q%2FxSmtwn3pv96QhErW42dLjT6zVly38Y8RTradC%2BKHhyTI6MUnTmo7M8ZIkzTQvKhkici63rAecP5LGk8px2%2FuSKk%2F43S97Wu6x7cV0yr9sHL0kfiyUh70jzGkKNlp14l0PPqxy%2BhtVwfK8RvMrt9vhEXLD67ZupUA375x33vkUOJlPoFMXme5mHJ7OtoNbQoGDwNuGDrKsAb2mI1r9%2BDO5xUTFJa1NOSnb7W58UUBcr3RjOvikpvablCIolm16e9XurEHZ7MK3ec4Y3EynKEFDG2EDlHF6anOStNVk6qeV4hevregZOd86s4S8EvxWAbFvfcUGX%2B%2B9f2eUaMuT0GFBconD2i58D4rbMjQsutosnh7MMOutsoGOqUBOREa61Yx6hHS4kvk86khqlJU4AZo3QL4G8C18R1QQ3wCgSlg%2BMlVsLsuIEgIuT3IV%2BGILHxD1ep8UgHp553vUk2GT2zTGSMW2R8VUI5la0ZfBXkFz5EFn8hyoGAfTXpu6qvEQ%2B79TGDUS1h1EI8JRvLEmYxxOjJxqhgFZrtsacsXG5hFdV5zwHXSK%2FdTVdxM9FVP5ZTroZokTliAYUAXIFUn%2B0a0&X-Amz-Signature=2c0bcc1090bb0cadefd56651aa6ae844e2e9ebb2ecbf8278db75a8b4f71f3962&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







