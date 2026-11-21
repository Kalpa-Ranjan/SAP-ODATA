



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FK3BRY5%2F20261121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261121T060719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCICi924A3Ewyv68CQ4teakMRnAvS5JhAR1V5K%2FOM4pvK4AiBJT6lqQdaij%2BWwFdBI9W2ELeCEgWjZfxEuGrJRgrXt0ir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMYQI79yDhGfWUyd5UKtwDUcAOYAY9k8ugspP4qXUScAjbk7FqaVycDX01O41yTJFDsD7jZpwqPoJBf%2B4Z4aAypHhSQ42QNtxZC4sqhTAFNDuNxxyzKz19yhqZnb93jA3KjBp%2BWs8y6sCd6k6ZjRPtJdIDRqlwD6kEEMCfBGnE00cmx4iFfoTa%2BlNdodUg%2FGBRFt6AdnRVJksZXD7%2Bw5BhYA%2Bfqd1O0I%2FsrgwVhi7biu%2FhjxSoC9Yi5ritwMtMDTvsSCtdgSUZm6vm3sDO0Gm3DLrFXyfmfI%2Fml7WBh4XOqS3DySjuq7uBBOtMFQAVtGjA1DvDU0XvnAIqHaZmoqU7bwDGJfiDSCqQjO5Z5i4tMYJG0wuqlQ%2FURWKdCehjX%2BTD2jbfbK7bFEddCGH9TYuy%2BJEbQbc1SrEDeIO5gNuDODQ%2FEoE74tP9ZVhrpII8zklqi5QtlctqbET9Y%2B1bVToHLg7KUvRB6o4VQmyCunYandavlDx%2BTa%2FR8Of0Vbp6HveLW7zSkArWRSB85WQESZoUSbDE1VmdeWLM7pgZHZ%2B5ps%2Fjl3nGDgPhv%2BKGCNHC7oBfJacKfytAYWi8qfqV3w3o%2B8ZfE0J%2FWxWpjyLzv0P0CSdSDnoORT0ix6WOaILeOxFpZOVfTCXRadUdwVgwsqiE2AY6pgFiByRDuX4rY4ap4RRrjLFJsgTJFedyei4yN1SBDNRJkFcpNt6uLI4uazUYp9lwjngNJcvm%2FPwWPfBsFv1KhiT8KTRk0IUmOQAnkuMjaUiZNz8TnNBQusbqxgFS4bI6XzWlM%2FGdtNX8gDue29G0YkSk36cqL1eRViObS2XqeypKO3D0jfjrjGUAz5NijTmsU3sgyZC7gFNdV7S8hPnVLm81pUWdn7xm&X-Amz-Signature=9e9499a9279337c89cae7e0ce3bbb747bba53644528497d4897fb954580d3632&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FK3BRY5%2F20261121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261121T060719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCICi924A3Ewyv68CQ4teakMRnAvS5JhAR1V5K%2FOM4pvK4AiBJT6lqQdaij%2BWwFdBI9W2ELeCEgWjZfxEuGrJRgrXt0ir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMYQI79yDhGfWUyd5UKtwDUcAOYAY9k8ugspP4qXUScAjbk7FqaVycDX01O41yTJFDsD7jZpwqPoJBf%2B4Z4aAypHhSQ42QNtxZC4sqhTAFNDuNxxyzKz19yhqZnb93jA3KjBp%2BWs8y6sCd6k6ZjRPtJdIDRqlwD6kEEMCfBGnE00cmx4iFfoTa%2BlNdodUg%2FGBRFt6AdnRVJksZXD7%2Bw5BhYA%2Bfqd1O0I%2FsrgwVhi7biu%2FhjxSoC9Yi5ritwMtMDTvsSCtdgSUZm6vm3sDO0Gm3DLrFXyfmfI%2Fml7WBh4XOqS3DySjuq7uBBOtMFQAVtGjA1DvDU0XvnAIqHaZmoqU7bwDGJfiDSCqQjO5Z5i4tMYJG0wuqlQ%2FURWKdCehjX%2BTD2jbfbK7bFEddCGH9TYuy%2BJEbQbc1SrEDeIO5gNuDODQ%2FEoE74tP9ZVhrpII8zklqi5QtlctqbET9Y%2B1bVToHLg7KUvRB6o4VQmyCunYandavlDx%2BTa%2FR8Of0Vbp6HveLW7zSkArWRSB85WQESZoUSbDE1VmdeWLM7pgZHZ%2B5ps%2Fjl3nGDgPhv%2BKGCNHC7oBfJacKfytAYWi8qfqV3w3o%2B8ZfE0J%2FWxWpjyLzv0P0CSdSDnoORT0ix6WOaILeOxFpZOVfTCXRadUdwVgwsqiE2AY6pgFiByRDuX4rY4ap4RRrjLFJsgTJFedyei4yN1SBDNRJkFcpNt6uLI4uazUYp9lwjngNJcvm%2FPwWPfBsFv1KhiT8KTRk0IUmOQAnkuMjaUiZNz8TnNBQusbqxgFS4bI6XzWlM%2FGdtNX8gDue29G0YkSk36cqL1eRViObS2XqeypKO3D0jfjrjGUAz5NijTmsU3sgyZC7gFNdV7S8hPnVLm81pUWdn7xm&X-Amz-Signature=5a47e172ecb6f0763d3635c94e62165723a5cc5a68f992956e1781cf083284a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







